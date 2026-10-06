"""Derive English variants from the Chinese themes.

Usage: python tools/make_en_variants.py
Only the visible text in theme.json changes (id, name, tagline, project prefix and
label); theme.css and the background are copied byte for byte. Taglines are
written for English, not translated word for word, as with Paper & Ink.
"""
import json
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
VARIANTS = {
    "mistlake": ("Mist Lake Letter", "The mist lingers. A letter has come."),
    "night": ("Night Voyage", "The lamp is still on. Thoughts drift ashore."),
    "grove": ("Grove", "Wind through the trees. Thoughts grow clear."),
}

for base, (name, tagline) in VARIANTS.items():
    src, dst = ROOT / "themes" / base, ROOT / "themes" / f"{base}-en"
    dst.mkdir(exist_ok=True)
    theme = json.loads((src / "theme.json").read_text(encoding="utf-8"))
    theme.update({
        "id": theme["id"] + "-en",
        "name": name,
        "tagline": tagline,
        "projectPrefix": "Project · ",
        "projectLabel": "Choose a project",
    })
    (dst / "theme.json").write_text(json.dumps(theme, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    for f in ("theme.css", theme["image"]):
        shutil.copyfile(src / f, dst / f)
    print(dst.name, theme["id"])
