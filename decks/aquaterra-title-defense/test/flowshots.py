from pathlib import Path
_DECK = Path(__file__).resolve().parents[1]
URL = _DECK.joinpath('index.html').as_uri()
O = str(_DECK / 'shots' / 'flow') + '/'

from playwright.sync_api import sync_playwright
import os;os.makedirs(O,exist_ok=True)
names={'s-flowA':['1_inputs','2_align','3_time_split'],'s-flowB':['4_random_forest','5_gamm','6_forecast','7_check','8_shortfall','9_value_at_risk']}
with sync_playwright() as p:
  b=p.chromium.launch();errs=[]
  for W,H,suf in[(1920,1080,''),(1366,768,'_1366')]:
    pg=b.new_page(viewport={'width':W,'height':H});pg.on('pageerror',lambda e:errs.append(str(e)));pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None)
    pg.goto(URL);pg.wait_for_timeout(400)
    for id,ns in names.items():
      pg.evaluate(f"__deck.goLabel('{id}',false)")
      for s,n in enumerate(ns):
        pg.evaluate(f'__deck.setStep({s})');pg.wait_for_timeout(3300)
        if suf=='' or n in('3_time_split','9_value_at_risk'):pg.screenshot(path=O+n+suf+'.png')
    # play test
    pg.evaluate("__deck.goLabel('s-flowA',false)");pg.click('#s-flowA .fplay');pg.wait_for_timeout(9000)
    print(suf,'after play 9s: cur',pg.evaluate('__deck.cur'),'step',pg.evaluate('__deck.step'))
    pg.close()
  print('errors',errs);b.close()
