"""Build Dream Skin official-format theme packages (with manifest.json) for dreamskin.cc.

Usage: python tools/make_official_packages.py
Reads themes/<id>/ and writes packages/<id>.zip plus .sha256, using fixed entry
dates so repeated runs give identical bytes.
"""
import hashlib
import json
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
CREATED_AT = "2026-10-06T00:00:00Z"
VERSION = "1.0.0"
SOURCE = "Tested on Windows; macOS not yet tested. Source and credits: https://github.com/yoshikitanak-hash/huajuan-skins"
MEDIA = {".json": "application/json", ".css": "text/css", ".jpg": "image/jpeg",
         ".png": "image/png", ".webp": "image/webp", ".txt": "text/plain"}

AI_PAINTED = ("Background painted by Codex with OpenAI image generation (AI-generated) from mood "
              "references chosen by the project initiator; recomposed by Claude Code. Theme design "
              "and styling by Claude Code (AI). ")
PROVENANCE = {
    "paper": "Procedural vector ink-wash scene written as code by Claude Code (AI). Theme design "
             "and styling by Claude Code. ",
    "night": "Procedural vector night scene written as code by Claude Code (AI). Theme design "
             "and styling by Claude Code. ",
    "folio": AI_PAINTED + "Left-hand decorations extended by Codex image generation. ",
    "celestial": AI_PAINTED + "Left-hand decorations extended by Codex image generation. ",
    "grove": AI_PAINTED,
    "mistlake": AI_PAINTED + "Mirrored, upscaled and mist-graded on the left by Claude Code. ",
}
for _base in ("paper", "mistlake", "night", "grove"):
    PROVENANCE[f"{_base}-en"] = PROVENANCE[_base]

LICENSE_TXT = """Huajuan (画卷) theme package
https://github.com/yoshikitanak-hash/huajuan-skins

Artwork (background image): Creative Commons Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/

Code (theme.json, theme.css): MIT License
Copyright (c) 2026 Huajuan contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""".encode("utf-8")


def entry(name, data):
    return {"path": name, "mediaType": MEDIA[pathlib.Path(name).suffix], "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def build(theme_dir):
    theme = json.loads((theme_dir / "theme.json").read_text(encoding="utf-8"))
    payload = {
        "theme.json": (theme_dir / "theme.json").read_bytes(),
        "theme.css": (theme_dir / "theme.css").read_bytes(),
        theme["image"]: (theme_dir / theme["image"]).read_bytes(),
        "LICENSE.txt": LICENSE_TXT,
    }
    manifest = {
        "packageVersion": 1,
        "themeId": theme["id"],
        "version": VERSION,
        "skinApiVersion": 1,
        "minClientVersion": "1.5.19",
        "platforms": ["windows", "macos"],
        "capabilities": ["background", "tokens", "safe-css"],
        "publisher": {"id": "yoshikitanak-hash", "displayName": "画卷 Huajuan"},
        "license": "CC-BY-4.0 AND MIT",
        "provenance": {"aiGenerated": True, "summary": PROVENANCE[theme_dir.name] + SOURCE},
        "files": [entry(name, data) for name, data in payload.items()],
        "createdAt": CREATED_AT,
    }
    out = ROOT / "packages" / f"{theme_dir.name}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in [("manifest.json", (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8")),
                           *payload.items()]:
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 6, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    (ROOT / "packages" / f"{theme_dir.name}.zip.sha256").write_text(f"{digest}  {out.name}\n", encoding="utf-8", newline="\n")
    print(out.name, out.stat().st_size, digest[:16])


for d in sorted((ROOT / "themes").iterdir()):
    build(d)
