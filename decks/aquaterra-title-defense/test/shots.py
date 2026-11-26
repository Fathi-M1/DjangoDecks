from pathlib import Path
_DECK = Path(__file__).resolve().parents[1]
URL = _DECK.joinpath('index.html').as_uri()
O = str(_DECK / 'shots') + '/'

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
  b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080});errs=[]
  pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None);pg.on('pageerror',lambda e:errs.append(str(e)))
  pg.goto(URL);pg.wait_for_timeout(500)
  def go(id,s):pg.evaluate(f"__deck.goLabel('{id}',false)");pg.evaluate(f'__deck.setStep({s})');pg.wait_for_timeout(900)
  pg.evaluate('__deck.go(0)');pg.evaluate('__deck.setStep(3)');pg.wait_for_timeout(900);pg.screenshot(path=O+'01_cover.png')
  go('s-bg',4);pg.wait_for_timeout(800);pg.screenshot(path=O+'02_background.png')
  go('s-rf',3);pg.fill('#rf-k','3');pg.dispatch_event('#rf-k','input');pg.click('#rf-boot');pg.wait_for_timeout(1200);pg.screenshot(path=O+'03_rf_ranked_top3.png')
  go('s-gamm',4);pg.click('#g-grp .chip[data-g="1"]');pg.wait_for_timeout(500);pg.screenshot(path=O+'04_gamm_random_effects.png')
  go('s-eval',2);pg.fill('#e-split','16');pg.dispatch_event('#e-split','input');pg.wait_for_timeout(500);pg.screenshot(path=O+'05_eval_baseline_vs_model.png')
  go('s-var',3);pg.click('#v-pick .chip[data-v="1"]');pg.click('#s-var [data-p="proxy"]');pg.wait_for_timeout(1000);pg.screenshot(path=O+'06_value_at_risk_proxy.png')
  go('s-pipe',3);pg.screenshot(path='/tmp/x_pipe.png')
  go('s-title',0);pg.click('#s-title .term[data-t="municipal"]');pg.wait_for_timeout(300);pg.screenshot(path='/tmp/x_pop.png')
  pg.keyboard.press('q');pg.wait_for_timeout(500);pg.screenshot(path='/tmp/x_q.png');pg.keyboard.press('Escape')
  go('s-bg',4);pg.keyboard.press('r');pg.wait_for_timeout(500);pg.screenshot(path='/tmp/x_r.png');pg.keyboard.press('Escape')
  go('s-scope',2);pg.click('#s-scope .lm[data-i="2"]');pg.wait_for_timeout(400);pg.screenshot(path='/tmp/x_scope.png')
  go('s-pipe',3);pg.click('#s-pipe .pnode[data-i="3"] .try');pg.wait_for_timeout(700);pg.screenshot(path='/tmp/x_back.png')
  go('b-qbank',0);pg.fill('#qb-search','causation');pg.wait_for_timeout(300);pg.click('#qb-list .qa .q');pg.wait_for_timeout(300);pg.screenshot(path='/tmp/x_qb.png')
  pg.keyboard.press('b');pg.wait_for_timeout(400);pg.screenshot(path='/tmp/x_menu.png')
  print('errors',errs)
  b.close()
