#!/usr/bin/env python3
"""
Insert figures into dissertation chapter pages using manual mapping
"""

import json
import os
import shutil
import re
from pathlib import Path

SOURCE_DIR = 'project_assets/images/dissertation/By_Chapter'
PUBLIC_DIR = 'public/assets/dissertation/figures'
EXTRACTED_DIR = 'project_assets/docs/dissertation/extracted'
MAPPING_FILE = 'manual_figure_mapping.json'

def copy_mapped_images(mapping):
    """Copy manually mapped images to public folder"""
    
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    
    print("="*70)
    print("COPYING IMAGES TO PUBLIC FOLDER")
    print("="*70 + "\n")
    
    for chapter, figures in mapping.items():
        print(f"Chapter {chapter}:")
        
        for fig_ref, fig_data in figures.items():
            source_file = fig_data['source_file']
            source_path = None
            
            # Find the source file in Chapter folders
            chapter_dir = Path(SOURCE_DIR) / f"Chapter {chapter}"
            
            # Check main folder
            for file in chapter_dir.glob(source_file):
                source_path = file
                break
            
            # Check subfolders
            if not source_path:
                for subdir in chapter_dir.glob('*'):
                    if subdir.is_dir():
                        for file in subdir.glob(source_file):
                            source_path = file
                            break
                        if source_path:
                            break
            
            if source_path:
                # Determine destination filename
                ext = Path(source_file).suffix
                dest_filename = f"figure-{chapter}-{fig_ref.replace('.', '-')}{ext}"
                dest_path = Path(PUBLIC_DIR) / dest_filename
                
                # Copy file
                shutil.copy2(source_path, dest_path)
                print(f"  ✓ {fig_ref}: {source_file} → {dest_filename}")
                
                # Update mapping with actual public path
                fig_data['public_path_actual'] = f"/assets/dissertation/figures/{dest_filename}"
            else:
                print(f"  ✗ {fig_ref}: Could not find {source_file}")
    
    print("\n" + "="*70)
    print("IMAGES COPIED")
    print("="*70)

def insert_figures_in_chapters(mapping):
    """Insert <figure> elements into chapter markdown where figures are referenced"""
    
    print("\n" + "="*70)
    print("INSERTING FIGURES INTO CHAPTER MARKDOWN")
    print("="*70 + "\n")
    
    for chapter, figures in mapping.items():
        md_file = Path(EXTRACTED_DIR) / f"chapter-{chapter}.md"
        
        if not md_file.exists():
            print(f"Chapter {chapter}: File not found")
            continue
        
        with open(md_file, 'r') as f:
            content = f.read()
        
        modified = False
        
        for fig_ref, fig_data in figures.items():
            # Look for figure references like "Figure 4.1" or "(Figure 4.1)"
            pattern = rf'(\()?Figure {fig_ref}(:|\))?'
            
            # Find all matches
            matches = list(re.finditer(pattern, content))
            
            if matches:
                # Get the public path (prefer actual if available)
                img_url = fig_data.get('public_path_actual', fig_data['public_url'])
                caption = fig_data['caption']
                
                # Create figure HTML
                figure_html = f'''
<figure class="my-8">
  <img src="{img_url}" alt="{caption}" class="w-full border border-white/10" />
  <figcaption class="text-sm text-gray-500 mt-2">Figure {fig_ref}: {caption}</figcaption>
</figure>
'''
                
                # For each match, check if it's not already in a figure tag
                for match in reversed(matches):  # Process in reverse to maintain positions
                    start = match.start()
                    end = match.end()
                    
                    # Check if this is standalone text (not already in HTML)
                    before_context = content[max(0, start-50):start]
                    if '<figure' not in before_context:
                        # Insert figure HTML after the reference line
                        # Find the end of the current paragraph
                        next_para_end = content.find('\n\n', end)
                        if next_para_end == -1:
                            next_para_end = len(content)
                        
                        # Insert figure after current paragraph
                        content = content[:next_para_end] + figure_html + content[next_para_end:]
                        modified = True
                        break  # Only insert once per figure
        
        if modified:
            # Write back
            with open(md_file, 'w') as f:
                f.write(content)
            print(f"  ✓ Chapter {chapter}: Inserted {len(figures)} figures")
        else:
            print(f"  - Chapter {chapter}: No changes needed")
    
    print("\n" + "="*70)
    print("MARKDOWN UPDATED")
    print("="*70)

def regenerate_astro_pages():
    """Re-run integrate_chapters.py to update Astro pages"""
    print("\n" + "="*70)
    print("REGENERATING ASTRO PAGES")
    print("="*70 + "\n")
    
    import subprocess
    result = subprocess.run(['python3', 'integrate_chapters.py'], 
                          capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    
    print("="*70)
    print("ASTRO PAGES REGENERATED")
    print("="*70)

def main():
    print("\n" + "="*70)
    print("DISSERTATION FIGURE INTEGRATION")
    print("Using Manual Mapping")
    print("="*70 + "\n")
    
    # Load manual mapping
    with open(MAPPING_FILE, 'r') as f:
        mapping = json.load(f)
    
    total_figures = sum(len(figs) for figs in mapping.values())
    print(f"Loaded mapping for {total_figures} figures across {len(mapping)} chapters\n")
    
    # Step 1: Copy images
    copy_mapped_images(mapping)
    
    # Step 2: Insert figures into markdown
    insert_figures_in_chapters(mapping)
    
    # Step 3: Regenerate Astro pages
    regenerate_astro_pages()
    
    print("\n" + "="*70)
    print("✅ FIGURE INTEGRATION COMPLETE")
    print("="*70)
    print(f"\n{total_figures} figures have been integrated into the dissertation pages.")
    print("\nPages with figures:")
    for ch in sorted(mapping.keys()):
        figs = ', '.join(sorted(mapping[ch].keys()))
        print(f"  - Chapter {ch}: Figures {figs}")
    
    print("\nView at: http://localhost:4321/academic/dissertation/chapter-[2,4,5,7]")
    print("="*70)

if __name__ == "__main__":
    main()
