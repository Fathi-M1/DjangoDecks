from pathlib import Path
_DECK = Path(__file__).resolve().parents[1]
URL = _DECK.joinpath('index.html').as_uri()
O = str(_DECK / 'shots' / 'v4') + '/'

from playwright.sync_api import sync_playwright
T=[('s-hook','00_cover'),('s-flowA','04_flow_A'),('s-flowB','05_flow_B'),('s-gamm','07_gamm'),('s-var','10_value_builder'),('b-refs','B3_references')]
with sync_playwright() as p:
  b=p.chromium.launch();errs=[]
  for W,H in[(1920,1080),(1366,768)]:
    pg=b.new_page(viewport={'width':W,'height':H});pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(URL);pg.wait_for_timeout(500)
    for id,n in T:
      pg.evaluate(f"__deck.goLabel('{id}',false)")
      st=pg.evaluate(f"+document.getElementById('{id}').dataset.steps||1")
      for s in range(st+1):pg.evaluate(f"__deck.setStep({s})");pg.wait_for_timeout(700 if s<st else 3500)
      pg.screenshot(path=f'{O}{n}_{W}.png')
    pg.close()
  print('errors',errs);b.close()
