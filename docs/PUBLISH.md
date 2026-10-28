# Publishing the new GitHub repository

**Requested target:** `https://github.com/chhatramani01/instagram-motiongraphics-reels`

If the repository does not yet exist, create it as a new **empty public repository** under the `chhatramani01` account. Do not initialize it with a README, `.gitignore` or license because these files are already in this package.

With GitHub CLI authenticated (`gh auth login`) and appropriate account permissions:

```bash
cd instagram-motiongraphics-reels
git init -b main
git add .
git commit -m "feat: launch Instagram Motion Graphics Reels v1.0.0"
gh repo create chhatramani01/instagram-motiongraphics-reels --public --source . --remote origin --push
```

If you created the empty repo in the web UI instead of using `gh repo create`, replace the final line with:

```bash
git remote add origin https://github.com/chhatramani01/instagram-motiongraphics-reels.git
git push -u origin main
```

Tag after reviewing CI and the video sample:

```bash
git tag -a v1.0.0 -m "First validated Instagram Reels agent skill"
git push origin v1.0.0
```

The bundled GitHub Actions workflow validates the skill and renders a short MP4 with procedural sound and a contact sheet on `ubuntu-24.04`. The generated output is uploaded as a GitHub Actions artifact. Passing CI verifies the **sample pipeline**, not every artistic style, voiceover system or Instagram placement.
