#!/usr/bin/env python3
"""Validate repo structure, style expansion and portable skill metadata."""
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[2]
def check():
    root=ROOT/'instagram-reels'
    main=(root/'SKILL.md').read_text(encoding='utf-8')
    assert re.match(r'^---\nname: instagram-reels\ndescription: .+\n---',main), 'Canonical SKILL frontmatter is invalid'
    paths=['.agents/skills/instagram-reels/SKILL.md','.claude/skills/instagram-reels/SKILL.md']
    available=[ROOT/x for x in paths if (ROOT/x).is_file()]
    # A standalone skill copy is valid without the repository's two thin shims.
    if available:
        assert len(available)==2, 'A repository checkout needs both agent entrypoints'
        txt=[p.read_text(encoding='utf-8') for p in available]
        assert txt[0]==txt[1], 'Agent entrypoints drifted'
        for doc in txt:assert 'instagram-reels/SKILL.md' in doc
    styles=json.loads((root/'styles/registry.json').read_text(encoding='utf-8'))
    assert len(styles)>=12 and len({s['id'] for s in styles})==len(styles)
    for s in styles:
        fp=root/'styles'/s['file'];assert fp.is_file(),fp
        guide=fp.read_text(encoding='utf-8');assert len(guide)>1700 and s['name'] in guide
        assert all(k in s['palette'] for k in ('background','foreground','accent','secondary'))
    for p in ['references/creative-direction.md','references/motion-system.md','references/mobile-layout.md','references/audio-and-captions.md','scripts/render.py','scripts/mux.py','examples/demo/scene.html']:
        assert (root/p).is_file(),p
    assert 'chhatramani01/instagram-motiongraphics-reels' in main
    print(f'PASS: 1 portable skill, 2 agent entrypoints, {len(styles)} rich visual styles, working script paths')
    return True
if __name__=='__main__':check()
