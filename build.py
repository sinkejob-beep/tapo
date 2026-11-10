import base64, pathlib, sys
root = pathlib.Path(__file__).parent
out = sys.argv[1] if len(sys.argv) > 1 else "public/index.html"
src = (root / "src.html").read_text()
# screenshots ship as separate full-resolution files next to the page
for name in ["licensees", "bases", "zones", "onb_form", "onb_wizard", "onb_list", "onb_timeline", "mkt_schedule", "mkt_leadtime", "mkt_trends"]:
    key = f"__IMG_{name.upper()}__"
    assert src.count(key) == 1, key
    assert (root / "public" / "shots" / f"{name}.webp").exists(), name
    src = src.replace(key, f"shots/{name}.webp")
# small assets stay inline
src = src.replace("__IMG_JOB__", "data:image/jpeg;base64," + base64.b64encode((root / "img" / "job.jpg").read_bytes()).decode())
for key, f in [("__FONT_DENTON__", "denton.woff2"), ("__FONT_IS_N__", "is-n.woff2"), ("__FONT_IS_I__", "is-i.woff2")]:
    assert src.count(key) == 1, key
    src = src.replace(key, "data:font/woff2;base64," + base64.b64encode((root / "fonts" / f).read_bytes()).decode())
# a standalone page (not the artifact viewer) needs its own document head
if out.endswith("index.html"):
    src = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
           '<style>html,body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
           '</head>\n<body>\n' + src + '\n</body>\n</html>\n')
(root / out).write_text(src, encoding="utf-8")
print("built", out, len(src) // 1024, "KB")
