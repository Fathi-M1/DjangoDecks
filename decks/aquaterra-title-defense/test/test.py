from pathlib import Path
_DECK = Path(__file__).resolve().parents[1]
URL = _DECK.joinpath('index.html').as_uri()

import sys,json
from playwright.sync_api import sync_playwright
CHECK=r'''() => {
 const st=document.getElementById('stage'),k=st.getBoundingClientRect().width/1920,o=st.getBoundingClientRect();
 const sl=document.querySelector('.slide.active');const R=e=>{const r=e.getBoundingClientRect();return{x:(r.left-o.left)/k,y:(r.top-o.top)/k,w:r.width/k,h:r.height/k}};
 const vis=e=>{const cs=getComputedStyle(e);if(cs.visibility==='hidden'||cs.display==='none')return false;let p=e;while(p&&p!==sl){if(parseFloat(getComputedStyle(p).opacity)<0.05)return false;p=p.parentElement}return true};
 const out=[];
 // boxes: direct .abs children that have text
 const boxes=[...sl.children].filter(e=>!e.matches('aside,.bgimg,.full,.rays,svg')&&vis(e)&&e.innerText.trim().length>0);
 const Z=[];
 const hit=(r,z)=>Math.min(r.x+r.w,z[3])-Math.max(r.x,z[1])>2&&Math.min(r.y+r.h,z[4])-Math.max(r.y,z[2])>2;
 const br=R(document.querySelector('#bar'));Z.push(['bar',br.x,br.y,br.x+br.w,br.y+br.h]);
 if(0)for(const id of['#bar','#back']){const e=document.querySelector(id);if(e&&getComputedStyle(e).display!=='none'&&hit(R(e),z))out.push('CHROME '+id+' in '+z[0])}
 const scl=e=>{let a=e.parentElement;while(a&&a!==sl){const o=getComputedStyle(a).overflowY;if(o==='auto'||o==='hidden'||o==='scroll')return R(a);a=a.parentElement}return null};
 const tw=document.createTreeWalker(sl,NodeFilter.SHOW_TEXT);let tn;while(tn=tw.nextNode()){const e=tn.parentElement;if(!tn.textContent.trim()||e.closest('aside')||!vis(e))continue;
  const rg=document.createRange();rg.selectNodeContents(tn);const c=scl(e);for(const q of rg.getClientRects()){let r={x:(q.left-o.left)/k,y:(q.top-o.top)/k,w:q.width/k,h:q.height/k};
   if(c){if(r.y>=c.y+c.h-2||r.y+r.h<=c.y+2)continue;}if(r.w<1)continue;for(const z of Z)if(hit(r,z))out.push('ZONE '+z[0]+' <- '+e.tagName+':'+tn.textContent.trim().slice(0,30))}}
 const btns=[...sl.querySelectorAll('button,input,svg')].filter(e=>vis(e)&&!e.closest('.flowsvg'));for(const e of btns){const r=R(e),c=scl(e);if(c&&(r.y>=c.y+c.h-2||r.y+r.h<=c.y+2))continue;for(const z of Z)if(hit(r,z))out.push('ZONE '+z[0]+' <- '+e.tagName+'#'+(e.id||e.className.baseVal||e.className).toString().slice(0,20))}
 for(let i=0;i<boxes.length;i++)for(let j=i+1;j<boxes.length;j++){const a=R(boxes[i]),b=R(boxes[j]);const ix=Math.min(a.x+a.w,b.x+b.w)-Math.max(a.x,b.x),iy=Math.min(a.y+a.h,b.y+b.h)-Math.max(a.y,b.y);
   if(ix>4&&iy>4){const A=boxes[i],B=boxes[j];if(A.contains(B)||B.contains(A))continue;out.push('OVL '+(A.id||A.className.slice(0,25))+' x '+(B.id||B.className.slice(0,25))+' '+Math.round(ix)+'x'+Math.round(iy))}}
 // text overflow inside containers
 sl.querySelectorAll('.card,.glass,.card2,.gap,.pair .pq,.pair .po,.algo,.src2,.segl,.eq,.cl,.mb2,.li,.qa,.rk .rl,.ib span').forEach(e=>{if(!vis(e))return;if(e.scrollHeight>e.clientHeight+3&&getComputedStyle(e).overflowY!=='auto')out.push('CLIP '+(e.id||e.className.slice(0,30))+' '+e.scrollHeight+'>'+e.clientHeight);if(e.scrollWidth>e.clientWidth+3)out.push('WCLIP '+(e.id||e.className.slice(0,30)))});
 // card children beyond card bottom
 sl.querySelectorAll('.card,.glass,.card2,.gap').forEach(c=>{if(!vis(c))return;const cr=R(c);[...c.querySelectorAll('*')].forEach(ch=>{if(!vis(ch)||ch.closest('svg')&&ch.tagName!=='svg')return;const r=R(ch);if(r.h>0&&r.y+r.h>cr.y+cr.h+2&&ch.innerText!==undefined)out.push('SPILL '+(c.id||c.className.slice(0,20))+' <- '+ch.tagName+'.'+(ch.className&&ch.className.baseVal===undefined?ch.className:'').slice(0,20)+' by '+Math.round(r.y+r.h-cr.y-cr.h))})});
 {const tw2=document.createTreeWalker(sl,NodeFilter.SHOW_TEXT);let t2;while(t2=tw2.nextNode()){const e=t2.parentElement;if(!t2.textContent.trim()||e.closest('aside')||!vis(e))continue;const fs=parseFloat(getComputedStyle(e).fontSize);if(fs<17.5)out.push('FONT '+fs+' '+e.tagName+':'+t2.textContent.trim().slice(0,24))}}
 {const P=s=>{const m=s.match(/[\d.]+/g);if(!m)return[0,0,0,0];return[+m[0],+m[1],+m[2],m.length>3?+m[3]:1]};
  const comp=(top,bot)=>{const a=top[3];return[top[0]*a+bot[0]*(1-a),top[1]*a+bot[1]*(1-a),top[2]*a+bot[2]*(1-a),1]};
  const lum=c=>{const f=v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)};return .2126*f(c[0])+.7152*f(c[1])+.0722*f(c[2])};
  const cr=(a,b)=>{const x=lum(a),y=lum(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
  const tw3=document.createTreeWalker(sl,NodeFilter.SHOW_TEXT);let t3;window.__cskip=window.__cskip||0;window.__cmin=window.__cmin||99;
  while(t3=tw3.nextNode()){const e=t3.parentElement;if(!t3.textContent.trim()||e.closest('aside')||!vis(e))continue;
   let op=1,p=e;while(p&&p!==sl){op*=parseFloat(getComputedStyle(p).opacity);p=p.parentElement}if(op<.5)continue;
   const rg=document.createRange();rg.selectNodeContents(t3);const q=rg.getClientRects()[0];if(!q)continue;
   const cx=q.left+q.width/2,cy=q.top+q.height/2;if(cx<0||cy<0||cx>innerWidth||cy>innerHeight)continue;
   const stack=document.elementsFromPoint(cx,cy);const layers=[];let img=false,base=null;
   for(const el of stack){if(el.id==='stage'||el.id==='amb'||el.closest('#amb'))break;const c2=getComputedStyle(el);
     if(c2.backgroundImage!=='none'&&!el.classList.contains('slide')){img=true;break}
     const c=P(c2.backgroundColor);if(c[3]>0)layers.push(c);if(c[3]>=.99){base=1;break}
     if(el.classList.contains('slide')){layers.push([244,250,253,.94]);break}}
   if(img){window.__cskip++;continue}
   const cs=getComputedStyle(e),fg=P(cs.color);fg[3]*=op;let worst=99;
   for(const bd of[[4,32,77,1],[255,255,255,1],[255,95,162,1]]){let bg=bd;for(let i=layers.length-1;i>=0;i--)bg=comp(layers[i],bg);const f=comp(fg,bg);worst=Math.min(worst,cr(f,bg))}
   const fs=parseFloat(cs.fontSize),bold=parseInt(cs.fontWeight)>=700,lg=fs>=24||(bold&&fs>=18.6);window.__cmin=Math.min(window.__cmin,worst);
   if(worst<(lg?3:4.5))out.push('CONTRAST '+worst.toFixed(2)+' op'+op.toFixed(2)+' '+fs+'px '+e.tagName+':'+t3.textContent.trim().slice(0,26))}}
 return [...new Set(out)];
}'''
res={};WS=[(1920,1080)] if 'one' in sys.argv else [(1920,1080),(1366,768)]
with sync_playwright() as p:
  b=p.chromium.launch()
  for W,H in WS:
    pg=b.new_page(viewport={'width':W,'height':H});errs=[]
    pg.on('console',lambda m:errs.append(m.text) if m.type=='error' else None);pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(URL);pg.wait_for_timeout(600)
    n=pg.evaluate('__deck.slides.length');issues=[]
    for i in range(n):
      pg.evaluate(f'__deck.go({i})');st=pg.evaluate(f'+__deck.slides[{i}].dataset.steps||0')
      for s in range(st+1):
        pg.evaluate(f'__deck.setStep({s})');pg.wait_for_timeout(1100)
        r=pg.evaluate(CHECK)
        for x in r:issues.append(f'{i+1}.{s} {x}')
      if W==1920:pg.screenshot(path=f'/tmp/fd_{i+1:02d}.png')
      elif i in(0,2,6):pg.screenshot(path=f'/tmp/fdS_{i+1:02d}.png')
    # keys
    pg.evaluate('__deck.go(0)');kr=[]
    for k in['ArrowRight','ArrowRight','ArrowRight','ArrowRight']:pg.keyboard.press(k)
    kr.append(('right x4 -> slide',pg.evaluate('__deck.cur'),pg.evaluate('__deck.step')))
    pg.keyboard.press('ArrowLeft');kr.append(('left',pg.evaluate('__deck.cur'),pg.evaluate('__deck.step')))
    pg.keyboard.press('End');kr.append(('End',pg.evaluate('__deck.cur')))
    pg.keyboard.press('Home');kr.append(('Home',pg.evaluate('__deck.cur')))
    pg.evaluate('__deck.go(1)')
    for k,sel in[('q','#qov'),('r','#rov'),('b','#menu'),('?','#help')]:
      pg.keyboard.press(k);pg.wait_for_timeout(200);kr.append((k,pg.evaluate(f"document.querySelector('{sel}').classList.contains('show')")));pg.keyboard.press('Escape')
    pg.keyboard.press('n');kr.append(('n',pg.evaluate("document.querySelector('#notes').classList.contains('show')")));pg.keyboard.press('n')
    pg.keyboard.press('f');pg.wait_for_timeout(300);kr.append(('f',pg.evaluate('!!document.fullscreenElement')))
    res[f'{W}x{H}']={'issues':issues,'errors':errs,'keys':kr,'cmin':pg.evaluate('window.__cmin'),'cskip':pg.evaluate('window.__cskip')}
    pg.close()
  b.close()
print(json.dumps(res,indent=1))
