"""Shared browser/runtime utilities for an original code-rendered Reel."""
from __future__ import annotations
import os
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright, Error as PlaywrightError


def browser_path() -> str | None:
    """Optional local Chromium override; Playwright's installed browser otherwise."""
    p = os.environ.get('CHROMIUM_PATH')
    if p and not Path(p).is_file():
        raise FileNotFoundError(f'CHROMIUM_PATH does not exist: {p}')
    return p


def open_scene(playwright, path: Path, width: int, height: int):
    path = path.expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    # Serve files over loopback: file:// is blocked in some Chromium sandboxes.
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, fmt, *args): pass
    handler = partial(QuietHandler, directory=str(path.parent))
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    Thread(target=server.serve_forever,daemon=True).start()
    browser = playwright.chromium.launch(headless=True, executable_path=browser_path())
    context = browser.new_context(viewport={'width': width, 'height': height}, device_scale_factor=1)
    context.add_init_script('window.__REEL_OFFLINE__ = true; window.requestAnimationFrame = () => 0;')
    page = context.new_page()
    try:
        page.goto(f'http://127.0.0.1:{server.server_port}/{path.name}', wait_until='load')
    except PlaywrightError as exc:
        if 'ERR_BLOCKED_BY_ADMINISTRATOR' not in str(exc):
            raise
        # Some hosted runtimes block all Chromium navigation. For portable,
        # self-contained Canvas examples, load the same HTML from memory.
        page.close()
        page=context.new_page()
        page.set_content(path.read_text(encoding='utf-8'), wait_until='load')
    page.evaluate('''async ({w,h}) => {
      const canvas=document.querySelector('canvas');
      if(!canvas)throw Error('Missing <canvas>');
      canvas.width=w;canvas.height=h;
      canvas.style.width=w+'px';canvas.style.height=h+'px';
      canvas.style.maxWidth='none';canvas.style.maxHeight='none';
      await document.fonts.ready;
      await Promise.all([...document.images].map(img=>img.decode?.().catch(()=>{})||Promise.resolve()));
      if(typeof window.renderAt!=='function')throw Error('Missing window.renderAt(t)');
    }''', {'w': width, 'h': height})
    return browser, context, page, server


def screenshot(page, t: float) -> bytes:
    page.evaluate('(t) => window.renderAt(t)', t)
    return page.locator('canvas').first.screenshot(type='png', animations='disabled', timeout=30000)


def ensure_dimensions(width: int, height: int) -> None:
    if width <= 0 or height <= 0 or width % 2 or height % 2:
        raise ValueError('Video dimensions must be positive even integers')
    if abs(width / height - 9/16) > 0.002:
        raise ValueError('This Instagram skill exports 9:16 only; use matching even dimensions such as 1080x1920')
