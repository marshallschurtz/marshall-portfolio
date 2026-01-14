#!/usr/bin/env python3
"""
Integrate extracted dissertation chapters into Astro pages
Reads markdown from extracted/ and updates chapter-X.astro files
"""

import os
import re
import json

EXTRACTED_DIR = 'project_assets/docs/dissertation/extracted'
PAGES_DIR = 'src/pages/academic/dissertation'

# Chapter navigation data
CHAPTERS = [
    {"number": "1", "title": "Introduction & Geographical Background", "slug": "chapter-1"},
    {"number": "2", "title": "Historical Background of Sidekan", "slug": "chapter-2"},
    {"number": "3", "title": "Archaeological Background of Sidekan and Soran", "slug": "chapter-3"},
    {"number": "4", "title": "Excavations of Gund-i Topzawa, Ghaberstan-i Topzawa, Sidekan Bank", "slug": "chapter-4"},
    {"number": "5", "title": "Survey of the Sidekan Subdistrict", "slug": "chapter-5"},
    {"number": "6", "title": "The Landscape and Settlement Patterns of the Sidekan Subdistrict", "slug": "chapter-6"},
    {"number": "7", "title": "Conclusion - The Character and Origin of Muṣaṣir", "slug": "chapter-7"},
]


def md_to_html(md_content):
    """Convert markdown content to HTML for Astro"""
    html_lines = []
    
    lines = md_content.split('\n')
    in_frontmatter = False
    skip_frontmatter = True
    skip_chapter_title = True
    
    for line in lines:
        # Handle frontmatter
        if line.strip() == '---':
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                in_frontmatter = False
                skip_frontmatter = False
                continue
        
        if in_frontmatter:
            continue
        
        # Skip the first markdown heading (chapter title - already in layout)
        if skip_chapter_title and line.startswith('# Chapter'):
            skip_chapter_title = False
            continue
        
        # Convert markdown headings to HTML
        if line.startswith('#### '):
            html_lines.append(f'<h4>{line[5:]}</h4>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.strip():
            # Regular paragraph
            html_lines.append(f'<p>{line}</p>')
        else:
            html_lines.append('')
    
    return '\n  '.join(html_lines)


def generate_chapter_page(chapter_num, md_content):
    """Generate Astro page content for a chapter"""
    
    chapter_idx = int(chapter_num) - 1
    chapter = CHAPTERS[chapter_idx]
    
    # Get prev/next chapters
    prev_chapter = CHAPTERS[chapter_idx - 1] if chapter_idx > 0 else None
    next_chapter = CHAPTERS[chapter_idx + 1] if chapter_idx < len(CHAPTERS) - 1 else None
    
    # Convert markdown to HTML
    html_content = md_to_html(md_content)
    
    # Build Astro frontmatter for navigation
    prev_js = f"{{\n      number: '{prev_chapter['number']}',\n      title: '{prev_chapter['title']}',\n      slug: '{prev_chapter['slug']}'\n    }}" if prev_chapter else "undefined"
    next_js = f"{{\n      number: '{next_chapter['number']}',\n      title: '{next_chapter['title']}',\n      slug: '{next_chapter['slug']}'\n    }}" if next_chapter else "undefined"
    
    astro_page = f'''---
import DissertationLayout from '../../../layouts/DissertationLayout.astro';

const currentChapter = {{
  number: '{chapter["number"]}',
  title: '{chapter["title"]}',
  slug: '{chapter["slug"]}'
}};

const prevChapter = {prev_js};
const nextChapter = {next_js};
---

<DissertationLayout 
  title={{currentChapter.title}}
  chapterNumber={{currentChapter.number}}
  prevChapter={{prevChapter}}
  nextChapter={{nextChapter}}
>

  {html_content}

</DissertationLayout>
'''
    
    return astro_page


def main():
    print("="*60)
    print("Integrating extracted chapters into Astro pages")
    print("="*60)
    
    # Read extraction summary
    summary_path = os.path.join(EXTRACTED_DIR, 'extraction_summary.json')
    with open(summary_path, 'r') as f:
        summary = json.load(f)
    
    print(f"\nFound {len(summary['chapters'])} chapters to integrate")
    print(f"Total words: {summary['total_words']:,}\n")
    
    for chapter_info in summary['chapters']:
        chapter_num = chapter_info['number']
        md_file = os.path.join(EXTRACTED_DIR, f"chapter-{chapter_num}.md")
        
        # Read markdown content
        with open(md_file, 'r') as f:
            md_content = f.read()
        
        # Generate Astro page
        astro_content = generate_chapter_page(chapter_num, md_content)
        
        # Write to pages directory
        output_path = os.path.join(PAGES_DIR, f"chapter-{chapter_num}.astro")
        with open(output_path, 'w') as f:
            f.write(astro_content)
        
        print(f"  ✓ chapter-{chapter_num}.astro ({chapter_info['word_count']:,} words)")
    
    print("\n" + "="*60)
    print("INTEGRATION COMPLETE")
    print("="*60)
    print(f"\nChapter pages updated in: {PAGES_DIR}/")
    print("\nNext: Run `npm run dev` and check /academic/dissertation/chapter-[1-7]")


if __name__ == "__main__":
    main()
