import importlib.util, os, sys, subprocess
spec = importlib.util.spec_from_file_location("b", "build.py"); b = importlib.util.module_from_spec(spec)
sys.argv=["x"]; spec.loader.exec_module(b)
parts=[]
for br in b.BRANDS:
    parts.append(f'<div class="cap" id="site-{br["id"]}" style="width:1000px;height:625px;position:relative;overflow:hidden">{b.b_site(br)}</div>')
    parts.append(f'<div class="cap" id="ig-{br["id"]}" style="width:380px;height:802px;position:relative;overflow:hidden">{b.b_ig(br)}</div>')
parts.append(f'<div class="cap" id="site-otel" style="width:1000px;height:625px;position:relative;overflow:hidden">{b.serp()}</div>')
parts.append(f'<div class="cap" id="ig-otel" style="width:380px;height:802px;position:relative;overflow:hidden">{b.otel_mobile()}</div>')
html = '<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="assets/site.css"><style>body{background:#fff;margin:0}.cap{margin:20px}.cap [data-fit]{transform:none!important}</style></head><body>'+"".join(parts).replace('loading="lazy"','')+'</body></html>'
open("/home/claude/laurus-site/_mocks.html","w").write(html.replace('href="assets/','href="/assets/').replace('src="img/','src="/img/'))
print("ok")
