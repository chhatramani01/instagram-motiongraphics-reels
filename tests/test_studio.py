"""Standard-library tests for motion Reels structure/audio metadata and determinism."""
from pathlib import Path
import json
import hashlib
import os
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'instagram-reels/scripts'))
from check import check
from audio_synth import synth
from _runtime import ensure_dimensions

class TestReels(unittest.TestCase):
    def test_repo_skills_and_styles(self):
        self.assertTrue(check())
    def test_safe_canvas(self):
        self.assertIsNone(ensure_dimensions(1080,1920))
        for w,h in [(1080,1080),(1001,1920),(0,1920)]:
            with self.assertRaises(ValueError):ensure_dimensions(w,h)
    def test_sfx_is_deterministic_and_nonzero(self):
        cues={'duration':.5,'sample_rate':16000,'cues':[{'at':.1,'type':'pop','gain':.5}]}
        with tempfile.TemporaryDirectory() as td:
            a=Path(td)/'a.wav';b=Path(td)/'b.wav'
            synth(cues,a);synth(cues,b)
            self.assertEqual(hashlib.sha256(a.read_bytes()).hexdigest(),hashlib.sha256(b.read_bytes()).hexdigest())
            self.assertGreater(a.stat().st_size,15000)
    @unittest.skipUnless(os.getenv('REELS_BROWSER_TEST')=='1','Enable with REELS_BROWSER_TEST=1 and installed Chromium')
    def test_pure_time_frame_pixels(self):
        from playwright.sync_api import sync_playwright
        from _runtime import open_scene, screenshot
        with sync_playwright() as p:
            b,c,page,server=open_scene(p,ROOT/'instagram-reels/examples/demo/scene.html',270,480)
            try:
                x=screenshot(page,3.21);screenshot(page,0.11);y=screenshot(page,3.21)
                self.assertEqual(hashlib.sha256(x).digest(),hashlib.sha256(y).digest())
                self.assertGreater(len(x),1200)
            finally:c.close();b.close();server.shutdown();server.server_close()
if __name__=='__main__':unittest.main()
