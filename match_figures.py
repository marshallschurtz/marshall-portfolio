#!/usr/bin/env python3
"""
Figure Matching and Integration Script for Dissertation

This script:
1. Scans available images in By_Chapter folders
2. Matches them to figure references in the extracted chapters
3. Copies matched images to public/assets/dissertation/figures/
4. Generates a mapping file for integration into chapter pages
"""

import os
import json
import shutil
from pathlib import Path

# Paths
SOURCE_IMAGES_DIR = 'project_assets/images/dissertation/By_Chapter'
PUBLIC_FIGURES_DIR = 'public/assets/dissertation/figures'
EXTRACTED_DIR = 'project_assets/docs/dissertation/extracted'
SUMMARY_FILE = os.path.join(EXTRACTED_DIR, 'extraction_summary.json')

def scan_available_images():
    """Scan all images in By_Chapter folders"""
    images = {}
    
    for chapter_dir in Path(SOURCE_IMAGES_DIR).glob('Chapter *'):
        chapter_num = chapter_dir.name.split()[-1]
        images[chapter_num] = []
        
        # Get all image files (jpg, png, tif, ai, pdf)
        for ext in ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff', '*.pdf', '*.ai']:
            for img_path in chapter_dir.glob(ext):
                if not img_path.name.startswith('.'):
                    images[chapter_num].append({
                        'filename': img_path.name,
                        'path': str(img_path),
                        'ext': img_path.suffix.lower()
                    })
        
        # Also check subdirectories
        for subdir in chapter_dir.glob('*'):
            if subdir.is_dir() and not subdir.name.startswith('.'):
                for ext in ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']:
                    for img_path in subdir.glob(ext):
                        if not img_path.name.startswith('.'):
                            images[chapter_num].append({
                                'filename': img_path.name,
                                'path': str(img_path),
                                'ext': img_path.suffix.lower(),
                                'subfolder': subdir.name
                            })
    
    return images

def load_figure_references():
    """Load figure references from extraction summary"""
    with open(SUMMARY_FILE, 'r') as f:
        summary = json.load(f)
    
    refs = {}
    for ch in summary['chapters']:
        refs[ch['number']] = ch['figures_referenced']
    
    return refs

def match_figures_to_images(references, available_images):
    """Attempt to match figure references to available image files"""
    matches = []
    unmatched_refs = []
    
    for chapter_num, fig_refs in references.items():
        for fig_ref in fig_refs:
            # Figure reference like "4.1" means Figure 4.1
            # We need to find an image that might correspond to it
            
            matched = False
            
            # Check if we have images for this chapter
            if chapter_num in available_images:
                chapter_images = available_images[chapter_num]
                
                # Strategy 1: Look for filename containing the figure number
                # e.g., "Figure 4.1.jpg" or "4.1-something.jpg" or "Fig4-1.png"
                for img in chapter_images:
                    filename_lower = img['filename'].lower()
                    
                    # Try different patterns
                    patterns = [
                        f"figure {fig_ref}",
                        f"figure{fig_ref}",
                        f"fig {fig_ref}",
                        f"fig{fig_ref}",
                        f"{fig_ref}",
                        f"{fig_ref.replace('.', '-')}",
                        f"{fig_ref.replace('.', '_')}",
                    ]
                    
                    for pattern in patterns:
                        if pattern.lower() in filename_lower.replace(' ', '').replace('_', '').replace('-', ''):
                            matches.append({
                                'chapter': chapter_num,
                                'figure_ref': fig_ref,
                                'source_path': img['path'],
                                'filename': img['filename'],
                                'ext': img['ext'],
                                'subfolder': img.get('subfolder', None)
                            })
                            matched = True
                            break
                    
                    if matched:
                        break
            
            if not matched:
                unmatched_refs.append({
                    'chapter': chapter_num,
                    'figure_ref': fig_ref
                })
    
    return matches, unmatched_refs

def copy_images_to_public(matches):
    """Copy matched images to public folder"""
    
    # Create public directory
    os.makedirs(PUBLIC_FIGURES_DIR, exist_ok=True)
    
    copied = []
    
    for match in matches:
        # Standardize filename: figure-4-1.jpg
        new_filename = f"figure-{match['chapter']}-{match['figure_ref'].replace('.', '-')}{match['ext']}"
        dest_path = os.path.join(PUBLIC_FIGURES_DIR, new_filename)
        
        try:
            # Convert .tif to .jpg if needed (or just copy if conversion not needed)
            if match['ext'] in ['.tif', '.tiff']:
                # For now, just note it needs conversion
                match['needs_conversion'] = True
                # Still copy the original
                shutil.copy2(match['source_path'], dest_path.replace('.jpg', '.tif'))
            else:
                shutil.copy2(match['source_path'], dest_path)
            
            copied.append({
                **match,
                'public_path': f"/assets/dissertation/figures/{new_filename}",
                'public_filename': new_filename
            })
            
        except Exception as e:
            print(f"Error copying {match['filename']}: {e}")
    
    return copied

def generate_figure_mapping(copied_images):
    """Generate a mapping file for easy integration"""
    
    mapping = {}
    
    for img in copied_images:
        chapter = img['chapter']
        fig_ref = img['figure_ref']
        
        if chapter not in mapping:
            mapping[chapter] = {}
        
        mapping[chapter][fig_ref] = {
            'public_url': img['public_path'],
            'original_filename': img['filename'],
            'needs_conversion': img.get('needs_conversion', False)
        }
    
    return mapping

def main():
    print("="*70)
    print("DISSERTATION FIGURE MATCHING & INTEGRATION")
    print("="*70)
    
    # Step 1: Scan available images
    print("\n1. Scanning available images...")
    available_images = scan_available_images()
    
    total_images = sum(len(imgs) for imgs in available_images.values())
    print(f"   Found {total_images} images across {len(available_images)} chapters:")
    for ch, imgs in available_images.items():
        if imgs:
            print(f"   - Chapter {ch}: {len(imgs)} images")
    
    # Step 2: Load figure references
    print("\n2. Loading figure references from extracted chapters...")
    references = load_figure_references()
    
    total_refs = sum(len(refs) for refs in references.values())
    print(f"   Found {total_refs} figure references")
    
    # Step 3: Match figures to images
    print("\n3. Matching figure references to available images...")
    matches, unmatched = match_figures_to_images(references, available_images)
    
    print(f"   Matched: {len(matches)} figures")
    print(f"   Unmatched: {len(unmatched)} figures")
    
    # Step 4: Copy images to public folder
    print("\n4. Copying matched images to public folder...")
    copied = copy_images_to_public(matches)
    print(f"   Copied {len(copied)} images to {PUBLIC_FIGURES_DIR}")
    
    # Step 5: Generate mapping file
    print("\n5. Generating figure mapping...")
    mapping = generate_figure_mapping(copied)
    
    mapping_file = os.path.join(EXTRACTED_DIR, 'figure_mapping.json')
    with open(mapping_file, 'w') as f:
        json.dump(mapping, f, indent=2)
    print(f"   Saved mapping to {mapping_file}")
    
    # Step 6: Generate report
    print("\n" + "="*70)
    print("SUMMARY REPORT")
    print("="*70)
    
    print(f"\n✅ Successfully matched and copied: {len(copied)} figures")
    
    if copied:
        print("\nMatched figures by chapter:")
        for ch in sorted(mapping.keys()):
            figs = list(mapping[ch].keys())
            print(f"  Chapter {ch}: {', '.join(sorted(figs))}")
    
    if unmatched:
        print(f"\n⚠️  Unmatched figures ({len(unmatched)}):")
        for item in unmatched:
            print(f"  - Chapter {item['chapter']}, Figure {item['figure_ref']}")
    
    # List images that couldn't be matched to any reference
    print("\n📦 Images available but not referenced:")
    for ch, imgs in available_images.items():
        if ch in mapping:
            matched_files = [m['filename'] for m in matches if m['chapter'] == ch]
            unref_imgs = [img for img in imgs if img['filename'] not in matched_files]
            if unref_imgs:
                print(f"  Chapter {ch}:")
                for img in unref_imgs[:5]:  # Show first 5
                    print(f"    - {img['filename']}")
                if len(unref_imgs) > 5:
                    print(f"    ... and {len(unref_imgs) - 5} more")
    
    print("\n" + "="*70)
    print("NEXT STEPS:")
    print("="*70)
    print("1. Review figure_mapping.json to see which figures were matched")
    print("2. For TIF files, consider converting to JPG for web display")
    print("3. Run the figure integration script to add <figure> elements to chapters")
    print("4. Manually add captions for each figure from the dissertation if needed")
    print("="*70)

if __name__ == "__main__":
    main()
