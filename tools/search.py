#!/usr/bin/env python3
"""
Simple wiki search tool. Searches all .md files in wiki/ for a query string.
Usage: python tools/search.py "query"
       python tools/search.py --titles-only "query"
"""

import os
import sys
import re
from pathlib import Path
from collections import defaultdict

def extract_title_from_frontmatter(content):
    """Extract title and title_pt from YAML frontmatter."""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, None

    frontmatter = match.group(1)
    title = None
    title_pt = None

    for line in frontmatter.split('\n'):
        if line.startswith('title:'):
            title = line.split('title:', 1)[1].strip().strip('"\'')
        elif line.startswith('title_pt:'):
            title_pt = line.split('title_pt:', 1)[1].strip().strip('"\'')

    return title, title_pt

def search_titles_only(query, wiki_dir):
    """Search only in page titles and frontmatter."""
    results = []
    query_lower = query.lower()

    for md_file in Path(wiki_dir).rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            title, title_pt = extract_title_from_frontmatter(content)
            rel_path = md_file.relative_to(wiki_dir)

            matches = 0
            if title and query_lower in title.lower():
                matches += 1
            if title_pt and query_lower in title_pt.lower():
                matches += 1

            if matches > 0:
                display_title = title or title_pt or str(rel_path)
                results.append((matches, str(rel_path), display_title, 0))
        except Exception as e:
            pass

    return results

def search_all_content(query, wiki_dir):
    """Search all content including body text."""
    results = defaultdict(lambda: {'matches': 0, 'lines': []})
    query_lower = query.lower()

    for md_file in Path(wiki_dir).rglob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()

            title, title_pt = extract_title_from_frontmatter(''.join(lines))
            rel_path = md_file.relative_to(wiki_dir)

            for line_no, line in enumerate(lines, 1):
                if query_lower in line.lower():
                    results[rel_path]['matches'] += 1
                    results[rel_path]['lines'].append((line_no, line.rstrip()))

            results[rel_path]['title'] = title or title_pt or str(rel_path)
        except Exception as e:
            pass

    # Convert to list and sort by match count
    result_list = []
    for rel_path, data in results.items():
        if data['matches'] > 0:
            result_list.append((data['matches'], str(rel_path), data['title'], data['lines']))

    return sorted(result_list, key=lambda x: -x[0])

def print_results(results, titles_only=False):
    """Pretty-print search results."""
    if not results:
        print(f"No results found.")
        return

    for rank, (match_count, filepath, title, line_data) in enumerate(results, 1):
        print(f"\n[{rank}] {filepath}")
        print(f"    Title: {title}")
        print(f"    Matches: {match_count}")

        if not titles_only and line_data:
            print(f"    Context:")
            for line_no, line_text in line_data[:3]:  # Show first 3 matches
                snippet = line_text[:80].strip()
                if len(line_text) > 80:
                    snippet += "..."
                print(f"      Line {line_no}: {snippet}")
            if len(line_data) > 3:
                print(f"      ... and {len(line_data) - 3} more matches")

def main():
    if len(sys.argv) < 2:
        print("Usage: python search.py [--titles-only] <query>")
        sys.exit(1)

    titles_only = False
    if sys.argv[1] == '--titles-only':
        titles_only = True
        if len(sys.argv) < 3:
            print("Usage: python search.py [--titles-only] <query>")
            sys.exit(1)
        query = ' '.join(sys.argv[2:])
    else:
        query = ' '.join(sys.argv[1:])

    wiki_dir = Path(__file__).parent.parent / 'wiki'

    if not wiki_dir.exists():
        print(f"Error: wiki directory not found at {wiki_dir}")
        sys.exit(1)

    if titles_only:
        results = search_titles_only(query, wiki_dir)
    else:
        results = search_all_content(query, wiki_dir)

    print_results(results, titles_only=titles_only)

if __name__ == '__main__':
    main()
