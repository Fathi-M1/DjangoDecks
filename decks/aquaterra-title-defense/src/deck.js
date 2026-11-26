(()=>{
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const NS='http://www.w3.org/2000/svg';
function el(tag,attrs,parent,txt){const e=document.createElementNS(NS,tag);for(const k in attrs)e.setAttribute(k,attrs[k]);if(txt!=null)e.textContent=txt;if(parent)parent.appendChild(e);return e}
function rng(seed){let s=seed>>>0||1;return()=>{s^=s<<13;s>>>=0;s^=s>>17;s^=s<<5;s>>>=0;return (s%100000)/100000}}
const fmt=(v,d=1)=>Number(v).toLocaleString('en-US',{minimumFractionDigits:d,maximumFractionDigits:d});
const stage=$('#stage'),slides=$$('.slide'),ctrl={};
let cur=0,step=0,returnTo=null,playT=null;
const steps=s=>+(s.dataset.steps||0);
function fit(){const k=Math.min(innerWidth/1920,innerHeight/1080);stage.style.transform=`translate(-50%,-50%) scale(${k})`}
addEventListener('resize',fit);fit();
function toast(t){const e=$('#toast');e.textContent=t;e.classList.add('show');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('show'),1600)}
function setStep(s){const sl=slides[cur];step=Math.max(0,Math.min(s,steps(sl)));
 $$('.rv[data-s]',sl).forEach(e=>e.classList.toggle('on',step>=+e.dataset.s));
 const c=ctrl[sl.id];if(c&&c.step)c.step(step);chrome()}
function go(i,s=0,keepReturn){i=Math.max(0,Math.min(i,slides.length-1));
 const old=slides[cur];if(ctrl[old.id]&&ctrl[old.id].leave)ctrl[old.id].leave();
 old.classList.remove('active');cur=i;const sl=slides[cur];sl.classList.add('active');
 if(!keepReturn){returnTo=null}
 $('#back').style.display=returnTo!=null?'block':'none';
 const c=ctrl[sl.id];if(c&&c.enter)c.enter();
 setStep(s==='max'?steps(sl):s);
 if($('#qov').classList.contains('show'))fillQ();if($('#rov').classList.contains('show'))fillR();
 history.replaceState(null,'','#'+sl.id)}
function goLabel(id,ret=true){const i=slides.findIndex(s=>s.id===id);if(i<0)return;const from=cur;closeAll();if(ret){returnTo=from}go(i,0,ret);if(ret)$('#back').textContent='← Back to '+(slides[from].dataset.label.startsWith('B')?slides[from].dataset.label:'slide '+(+slides[from].dataset.label))}
function next(){const sl=slides[cur];if(step<steps(sl))setStep(step+1);else if(cur<slides.length-1)go(cur+1)}
function prev(){if(step>0)setStep(step-1);else if(cur>0)go(cur-1,'max')}
const mainN=slides.filter(s=>!s.classList.contains('backup')).length;
function chrome(){const sl=slides[cur],bk=sl.classList.contains('backup');
 $('#counter').innerHTML=bk?`<b>${sl.dataset.label}</b> backup`:`<b>${sl.dataset.label}</b> / ${String(mainN-1).padStart(2,'0')}`;
 $('#progress').style.width=(bk?100:(cur/(mainN-1))*100)+'%';
 const sec=+sl.dataset.sec;$$('#rail .rs').forEach(e=>{const k=+e.dataset.sec;e.className='rs'+(k<sec?' done':k===sec?' on':'')});
 $('#seclab').innerHTML=sl.dataset.title;
 const n=steps(sl);$('#steps').innerHTML=Array.from({length:n},(_,k)=>`<span class="${k<step?'on':''}"></span>`).join('');
 $('#kq').classList.toggle('dim',!QA[sl.dataset.q]);
 const nt=$('aside.notes',sl);$('#ntxt').textContent=nt?nt.textContent.trim():'(No notes for this slide.)';
 $('#nlab').textContent='Speaker notes · '+sl.dataset.title.replace('&amp;','&')}
// overlays
function closeAll(){$$('.ov').forEach(o=>o.classList.remove('show'))}
function toggleOv(id){const o=$('#'+id),was=o.classList.contains('show');closeAll();if(!was){if(id==='qov')fillQ();if(id==='rov')fillR();if(id==='menu')fillMenu();o.classList.add('show')}}
function qaHTML(q,a,open,tag){return `<div class="qa${open?' open':''}"><button class="q"><i>Q</i><span>${q}</span></button>${tag?`<span class="tagc">${tag}</span>`:''}<div class="a">${a}</div></div>`}
function fillQ(){const sl=slides[cur],list=QA[sl.dataset.q];
 $('#qtitle').innerHTML=sl.dataset.title;
 $('#qbody').innerHTML=list?list.map((x,k)=>qaHTML(x[0],x[1],k===0)).join(''):'<p class="body" style="margin-top:20px">No section questions for this slide.</p>';
 $('#qbody').insertAdjacentHTML('beforeend','<p style="margin-top:22px"><span class="link" data-go="b-qbank">Open the full panel Q&amp;A bank →</span></p>')}
function fillR(){const sl=slides[cur],key=sl.dataset.r||sl.dataset.q,list=RT[key];
 let h='';if(list){h+=`<div class="lab" style="margin-top:14px;color:var(--sea)">${key==='bg'?'Relevant titles · click to read the summary':'Relevant to this section'}</div>`+list.map((r,k)=>`<div class="ref${k===0?' open':''}"><div class="ra">${r[0]}</div><div class="rt">${r[1]}</div><div class="rn">${r[2]}</div></div>`).join('')}
 h+=`<div class="lab" style="margin-top:26px">All references · APA 7</div>`+APA.map(a=>`<p class="apa" style="margin-top:12px;font-size:17px">${a}</p>`).join('');
 $('#rbody').innerHTML=h}
function fillMenu(){$('#mgrid').innerHTML=slides.map((s,k)=>`<button class="it${s.classList.contains('backup')?' bk':''}${k===cur?' cur':''}" data-k="${k}"><small>${s.dataset.label}</small>${s.dataset.title}</button>`).join('')}
document.addEventListener('click',e=>{
 const g=e.target.closest('[data-go]');if(g){e.preventDefault();goLabel(g.dataset.go);return}
 const q=e.target.closest('.qa .q');if(q){q.parentElement.classList.toggle('open');return}
 const r=e.target.closest('.ref');if(r){r.classList.toggle('open');return}
 const m=e.target.closest('#mgrid .it');if(m){closeAll();go(+m.dataset.k);return}
 if(e.target.classList.contains('ov'))closeAll();
 if(e.target.closest('.x'))closeAll()});
$$('#rail .rs').forEach(r=>r.onclick=()=>{const i=slides.findIndex(s=>+s.dataset.sec===+r.dataset.sec);if(i>=0){closeAll();go(i)}});
$('#back').onclick=()=>{if(returnTo!=null){const r=returnTo;returnTo=null;go(r)}};
$('#kq').onclick=()=>toggleOv('qov');$('#kr').onclick=()=>toggleOv('rov');$('#kb').onclick=()=>toggleOv('menu');
$('#kn').onclick=()=>$('#notes').classList.toggle('show');$('#kf').onclick=fs;$('#kh').onclick=()=>toggleOv('help');
$('#pv').onclick=prev;$('#nx').onclick=next;
function fs(){if(!document.fullscreenElement)document.documentElement.requestFullscreen&&document.documentElement.requestFullscreen().catch(()=>{});else document.exitFullscreen()}
addEventListener('keydown',e=>{
 if(e.target.tagName==='INPUT'&&e.target.type!=='range'){if(e.key==='Escape')e.target.blur();return}
 const k=e.key;
 if(['ArrowRight','PageDown',' '].includes(k)){e.preventDefault();next()}
 else if(['ArrowLeft','PageUp'].includes(k)){e.preventDefault();prev()}
 else if(k==='Home'){go(0)}else if(k==='End'){go(mainN-1)}
 else if(k==='f'||k==='F')fs();else if(k==='n'||k==='N')$('#notes').classList.toggle('show');
 else if(k==='q'||k==='Q'){if(QA[slides[cur].dataset.q])toggleOv('qov');else toast('No section questions here · press B for the Q bank')}
 else if(k==='r'||k==='R')toggleOv('rov');else if('bBgG'.includes(k)&&k.length===1)toggleOv('menu');
 else if(k==='?'||k==='h'||k==='H')toggleOv('help');
 else if(k==='Escape'){closeAll();$('#notes').classList.remove('show')}});
// ---------- controllers ----------
// title terms
$$('#s-hook .term').forEach(b=>b.onclick=ev=>{ev.stopPropagation();const p=$('#pop-'+b.dataset.t),was=p.classList.contains('show');$$('#s-hook .pop').forEach(x=>x.classList.remove('show'));$$('#s-hook .term').forEach(x=>x.classList.remove('on'));if(!was){p.classList.add('show');b.classList.add('on')}});
$('#s-hook').addEventListener('click',e=>{if(!e.target.closest('.pop,.term')){$$('#s-hook .pop').forEach(x=>x.classList.remove('show'));$$('#s-hook .term').forEach(x=>x.classList.remove('on'))}});
ctrl['s-hook']={leave(){$$('#s-hook .pop').forEach(x=>x.classList.remove('show'));$$('#s-hook .term').forEach(x=>x.classList.remove('on'))}};
// background count-up
ctrl['s-bg']={done:false,step(s){const n=$('#oc-num'),l=$('#oc-line');
 if(s>=2&&!this.done){this.done=true;let t0=null;l.style.strokeDashoffset=0;const f=t=>{if(!t0)t0=t;const p=Math.min(1,(t-t0)/1100);n.textContent='~'+Math.round(45*p)+'M';if(p<1)requestAnimationFrame(f)};requestAnimationFrame(f)}
 if(s<2){this.done=false;n.textContent='~45M'}}};
// objectives
const MAP=[[0,2],[0,1],[2],[3,4]];
function rqSel(i){const svg=$('#rqlines');svg.innerHTML='';$$('#s-obj .rq').forEach((b,k)=>{b.classList.toggle('on',k===i);b.classList.toggle('dim',i>=0&&k!==i)});
 $$('#s-obj .so').forEach((b,k)=>{const on=i>=0&&MAP[i].includes(k);b.classList.toggle('on',on);b.classList.toggle('dim',i>=0&&!on)});
 if(i<0)return;MAP[i].forEach(j=>{const y1=i*132+58,y2=j*104+46;el('path',{d:`M0,${y1} C90,${y1} 90,${y2} 180,${y2}`,stroke:'#d9822b','stroke-width':3,fill:'none','stroke-dasharray':'6 6'},svg);el('circle',{cx:180,cy:y2,r:6,fill:'#0e8f86'},svg)})}
$$('#s-obj .rq').forEach(b=>b.onclick=()=>{const i=+b.dataset.i;setStep(i+1)});
ctrl['s-obj']={step(s){rqSel(s-1)}};
// scope
function scopeView(v){$$('#sl-tog .chip').forEach(c=>c.classList.toggle('on',c.dataset.v===v));const A=$('#s-scope .colA'),B=$('#s-scope .colB');
 A.classList.toggle('dimc',v==='lim');B.classList.toggle('dimc',v==='scope');if(v!=='scope')B.classList.add('on')}
$$('#sl-tog .chip').forEach(c=>c.onclick=()=>{if(c.dataset.v!=='scope'&&step<2)setStep(2);scopeView(c.dataset.v)});
$$('#s-scope .lm').forEach(b=>b.onclick=()=>{const was=b.classList.contains('on');$$('#s-scope .lm').forEach(x=>x.classList.remove('on'));const B=$('#s-scope .colB');if(was)B.classList.remove('focus');else{b.classList.add('on');B.classList.add('focus')}});
ctrl['s-scope']={enter(){scopeView('both');$$('#s-scope .lm').forEach(x=>x.classList.remove('on'));$('#s-scope .colB').classList.remove('focus')}};
// data-flow pipeline (two slides)
const FL={'s-flowA':1,'s-flowB':4};let fRaf=null,fPlay=null,fLast=0;const fSpawn=new Map();
function flowStep(id,s){const sl=$('#'+id),cs=FL[id]+s;
 $$('.stg',sl).forEach(g=>{const k=+g.dataset.st;g.classList.toggle('show',k<=cs);g.classList.toggle('cur',k===cs);g.classList.toggle('past',k<cs)});
 $$('.fpath,.fhead',sl).forEach(p=>p.classList.toggle('on',+p.dataset.to<=cs));
 if(id==='s-flowA')$('#fa-tab').classList.toggle('split',cs>=3);sl._cs=cs}
function fLoop(t){const sl=slides[cur];if(!FL[sl.id]){fRaf=null;return}const dt=Math.min(60,t-(fLast||t));fLast=t;const G=$('.parts',sl);
 $$('.fpath.on',sl).forEach(p=>{const into=+p.dataset.to,curS=into===sl._cs,rate=curS?110:900;let acc=(fSpawn.get(p)||0)+dt;
  if(acc>rate){acc=0;const L=p.getTotalLength();const c=el('circle',{r:curS?5.5:4,fill:p.dataset.c||'#0e8f86',opacity:curS?.95:.5},G);c._p=p;c._L=L;c._s=0;c._v=p.classList.contains('long')?0.55:0.16}fSpawn.set(p,acc)});
 [...G.children].forEach(c=>{c._s+=dt*c._v;if(c._s>=c._L||!c._p.classList.contains('on')){c.remove();return}const q=c._p.getPointAtLength(c._s);c.setAttribute('cx',q.x);c.setAttribute('cy',q.y)});
 fRaf=requestAnimationFrame(fLoop)}
function fStart(){if(!fRaf){fLast=0;fRaf=requestAnimationFrame(fLoop)}}
function fStopRaf(){if(fRaf)cancelAnimationFrame(fRaf);fRaf=null;$$('.flow .parts').forEach(g=>g.innerHTML='')}
function fStop(){clearInterval(fPlay);fPlay=null;$$('.fplay').forEach(b=>b.textContent='▶ Play the flow')}
$$('.fplay').forEach(b=>b.onclick=()=>{if(fPlay){fStop();return}const sl=slides[cur];if(sl.id==='s-flowB'&&step>=steps(sl))setStep(0);
 $$('.fplay').forEach(x=>x.textContent='❚❚ Pause');fPlay=setInterval(()=>{const s2=slides[cur];if(!FL[s2.id]){fStop();return}
  if(step<steps(s2))setStep(step+1);else if(s2.id==='s-flowA')go(cur+1);else fStop()},2800)});
$$('.flow .stg').forEach(g=>g.addEventListener('click',e=>{if(e.target.closest('[data-go]'))return;const sl=g.closest('.slide');if(slides[cur]!==sl)return;setStep(+g.dataset.st-FL[sl.id])}));
for(const id in FL)ctrl[id]={enter:fStart,step(s){flowStep(id,s)},leave:fStopRaf};
// RF demo
const PRED=[["Landings, lag 4 (same quarter last year)",.92,0],["Quarter of the year (season)",.78,0],["Landings, lag 1",.61,0],["Mangrove history",.44,1],["Sea surface temperature",.38,1],["Prior typhoon exposure",.27,1],["Rainfall",.16,1]];
let rfImp=PRED.map(p=>p[1]),rfSeed=7,rfRanked=false;
const rfBars=$('#rf-bars');rfBars.innerHTML=PRED.map((p,k)=>`<div class="bar${p[2]?' env':''}" data-k="${k}"><div class="bn">${p[0]}</div><div class="bt"><div class="bf"></div></div><div class="bv"></div></div>`).join('');
const ALPHA=[3,1,6,2,5,0,4];// pre-rank display order (scrambled)
function rfDraw(){const K=+$('#rf-k').value;$('#rf-kv').textContent=K;const order=rfRanked?rfImp.map((v,k)=>[v,k]).sort((a,b)=>b[0]-a[0]).map(x=>x[1]):ALPHA;
 $$('.bar',rfBars).forEach(b=>{const k=+b.dataset.k,pos=order.indexOf(k);b.style.top=pos*42+'px';b.querySelector('.bf').style.width=rfRanked?(rfImp[k]*100)+'%':'0%';
  b.querySelector('.bv').textContent=rfRanked?(rfImp[k]*100).toFixed(0)+(step>=3&&pos<K?'  → GAMM':''):'';b.classList.toggle('top',rfRanked&&step>=3&&pos<K)})}
function rfTrees(show){const svg=$('#rf-trees');svg.innerHTML='';if(!show){$('#rf-vote').textContent='Press 🌳 Grow forest.';return}const R=rng(rfSeed*31);const preds=[];
 for(let t=0;t<12;t++){const cx=46+t*91,g=el('g',{style:`opacity:0;transition:opacity .4s ${t*0.06}s`},svg);const c=['#0e8f86','#5cc9bd','#d9822b'];
  el('line',{x1:cx,y1:22,x2:cx-24,y2:62,stroke:'#a5d8d0','stroke-width':2},g);el('line',{x1:cx,y1:22,x2:cx+24,y2:62,stroke:'#a5d8d0','stroke-width':2},g);
  el('line',{x1:cx-24,y1:62,x2:cx-36,y2:100,stroke:'#a5d8d0','stroke-width':2},g);el('line',{x1:cx-24,y1:62,x2:cx-12,y2:100,stroke:'#a5d8d0','stroke-width':2},g);el('line',{x1:cx+24,y1:62,x2:cx+36,y2:100,stroke:'#a5d8d0','stroke-width':2},g);
  el('circle',{cx,cy:22,r:9,fill:c[t%3]},g);el('circle',{cx:cx-24,cy:62,r:7,fill:'#0b2a3c'},g);el('circle',{cx:cx+24,cy:62,r:7,fill:'#0b2a3c'},g);
  [cx-36,cx-12,cx+36].forEach(x=>el('rect',{x:x-6,y:100,width:12,height:12,rx:3,fill:'#a5d8d0'},g));
  const v=Math.round(400+R()*130);preds.push(v);el('text',{x:cx,y:148,'text-anchor':'middle','font-size':17,'font-weight':700,fill:'#0b2a3c'},g,v);
  requestAnimationFrame(()=>requestAnimationFrame(()=>g.style.opacity=1))}
 el('text',{x:4,y:166,'font-size':13,fill:'#6f8b99'},svg,'each tree: bootstrap sample + random predictor subset → its own prediction (mt)');
 const avg=preds.reduce((a,b)=>a+b)/preds.length;$('#rf-vote').innerHTML=`12 trees predict ${Math.min(...preds)}–${Math.max(...preds)} mt → forest average <b style="color:var(--sea)">${avg.toFixed(0)} mt</b>`}
function rfBoot(){rfSeed++;const R=rng(rfSeed*97);rfImp=PRED.map(p=>Math.max(.05,Math.min(.98,p[1]+(R()-.5)*.16)));rfTrees(true);rfDraw();toast('New bootstrap · importances shift slightly')}
$('#rf-grow').onclick=()=>{setStep(Math.max(step,1));rfTrees(true)};$('#rf-rank').onclick=()=>setStep(Math.max(step,2));$('#rf-boot').onclick=()=>{if(step<1)setStep(1);rfBoot()};
$('#rf-k').oninput=()=>{if(step<3)setStep(3);rfDraw()};
ctrl['s-rf']={step(s){$$('#s-rf .steps-l li').forEach(l=>l.classList.toggle('on',s>=+l.dataset.k));if(s<1)rfTrees(false);else if(!$('#rf-trees').childNodes.length)rfTrees(true);rfRanked=s>=2;rfDraw()}};
// GAMM demo
const GT=[["season","s(quarter)","#0e8f86"],["sst","s(SST)","#d9822b"],["rain","s(rainfall)","#2f7fd6"],["lag","s(landings, lag 1)","#8a5bd6"]];
const GRP=[["Province A · Category 1",0],["Province B · Category 1",-70],["Province C · Category 2",55]];
let gOn={season:false,sst:false,rain:false,lag:false},gRE=false,gG=0,gFc=false;
const gR=rng(11),N=24,gX=Array.from({length:N+1},(_,t)=>({q:t%4,sst:Math.sin(t*0.45)+gR()*0.6-0.3,rain:Math.cos(t*0.8+1)+gR()*0.6-0.3,noise:(gR()-.5)*30}));
const fS={season:t=>[-40,55,25,-35][gX[t].q],sst:t=>-38*Math.tanh(1.4*gX[t].sst),rain:t=>14*gX[t].rain*gX[t].rain-14,lag:t=>t>0?0.25*(fS.season(t-1)):0};
const gBase=260;
function gObs(t){return gBase+fS.season(t)+fS.sst(t)+fS.rain(t)+fS.lag(t)+GRP[gG][1]+gX[t].noise}
function gFit(t){let v=gBase;for(const k in gOn)if(gOn[k])v+=fS[k](t);if(gRE)v+=GRP[gG][1];return v}
$('#g-terms').innerHTML=GT.map(g=>`<button class="term" data-k="${g[0]}" style="color:${g[2]}"><i></i><span style="color:var(--ink)">${g[1]}</span></button>`).join('');
$('#g-grp').innerHTML=GRP.map((g,k)=>`<button class="chip" data-g="${k}" style="font-size:15px;padding:7px 12px">${g[0]}</button>`).join('');
function gDraw(){$$('#g-terms .term').forEach(b=>b.classList.toggle('on',gOn[b.dataset.k]));const re=$('#g-re');re.textContent=gRE?'On':'Off';re.classList.toggle('on',gRE);
 $$('#g-grp .chip').forEach(c=>c.classList.toggle('on',+c.dataset.g===gG));$('#g-title').textContent='Landings (mt) · '+GRP[gG][0];
 $('#g-formula').innerHTML='ŷ<sub>pct</sub> = β<sub>0</sub> '+GT.map(g=>`<span class="fx${gOn[g[0]]?'':' off'}" style="color:${g[2]}">+ ${g[1]}</span>`).join(' ')+` <span class="fx${gRE?'':' off'}" style="color:var(--ink)">+ b<sub>province</sub> + b<sub>category</sub></span>`;
 const svg=$('#g-main');svg.innerHTML='';const W=1060,H=330,L=50,B=300,T=14;const ys=[];for(let t=0;t<=N;t++){ys.push(gObs(t),gFit(t))}const mn=Math.min(...ys)-20,mx=Math.max(...ys)+20;
 const X=t=>L+t*(W-L-30)/N,Y=v=>B-(v-mn)/(mx-mn)*(B-T);
 for(let k=0;k<=4;k++){const v=mn+(mx-mn)*k/4;el('line',{x1:L,x2:W-10,y1:Y(v),y2:Y(v),class:'ax'},svg);el('text',{x:L-8,y:Y(v)+5,'text-anchor':'end',class:'tick'},svg,Math.round(v))}
 for(let t=0;t<N;t+=4)el('text',{x:X(t),y:B+22,class:'tick'},svg,'Yr '+(t/4+1)+' Q1');
 el('rect',{x:X(N)-14,y:T,width:W-X(N)+4,height:B-T,fill:'#fff7e6'},svg);
 for(let t=0;t<N;t++)el('circle',{cx:X(t),cy:Y(gObs(t)),r:5,fill:'#a9bfc6'},svg);
 let d='';for(let t=0;t<N;t++)d+=(t?'L':'M')+X(t)+','+Y(gFit(t));el('path',{d,stroke:'#0e8f86','stroke-width':4,fill:'none'},svg);
 if(gFc){const fv=gFit(N);el('path',{d:`M${X(N-1)},${Y(gFit(N-1))} L${X(N)},${Y(fv)}`,stroke:'#d9822b','stroke-width':3,'stroke-dasharray':'6 5',fill:'none'},svg);el('path',{d:`M${X(N)},${Y(fv)-11} l11,11 l-11,11 l-11,-11Z`,fill:'#d9822b'},svg);el('text',{x:X(N)-22,y:T+16,'text-anchor':'end','font-size':17,'font-weight':700,fill:'#d9822b'},svg,'forecast '+Math.round(fv)+' mt')}
 let mae=0;for(let t=0;t<N;t++)mae+=Math.abs(gObs(t)-gFit(t));$('#g-err').innerHTML=`In-sample fit error (MAE): <b style="color:var(--ink)">${(mae/N).toFixed(1)} mt</b>`;
 // partial effects
 const sm=$('#g-small');sm.innerHTML='';GT.forEach(g=>{const w=250,h=118,s=el('svg',{width:w,height:h},null);sm.appendChild(s);s.style.background=gOn[g[0]]?'#f3fbf9':'#f7f9fa';s.style.borderRadius='10px';s.style.opacity=gOn[g[0]]?1:.4;
  el('text',{x:10,y:20,'font-size':14,'font-weight':700,fill:g[2]},s,g[1]);el('line',{x1:10,x2:w-10,y1:72,y2:72,class:'ax'},s);let p='';
  for(let i=0;i<=40;i++){const u=i/40;let v;if(g[0]==='season'){const q=u*3;const a=[-40,55,25,-35];const i0=Math.min(2,Math.floor(q)),f=q-i0;v=a[i0]*(1-f)+a[i0+1]*f}else if(g[0]==='sst')v=-38*Math.tanh(1.4*(u*3-1.5));else if(g[0]==='rain')v=14*(u*3-1.5)**2-14;else v=0.25*(u*120-60);p+=(i?'L':'M')+(10+u*(w-20))+','+(72-v*0.8)}
  el('path',{d:p,stroke:g[2],'stroke-width':3,fill:'none'},s);el('text',{x:w-10,y:h-6,'text-anchor':'end','font-size':12,fill:'#6f8b99'},s,g[0]==='season'?'Q1 → Q4':g[0]==='lag'?'last quarter\u2019s level':'low → high')})}
$$('#g-terms .term').forEach(b=>b.onclick=()=>{gOn[b.dataset.k]=!gOn[b.dataset.k];gDraw()});
$('#g-re').onclick=()=>{gRE=!gRE;gDraw()};$$('#g-grp .chip').forEach(c=>c.onclick=()=>{gG=+c.dataset.g;gDraw()});
ctrl['s-gamm']={step(s){gOn={season:s>=1,sst:s>=2,rain:s>=2,lag:s>=2};gRE=s>=3;gFc=s>=4;gDraw()}};
// eval
const eR=rng(23),EN=28,eTrue=[],eObs=[],eWf=[];
const eYr=Array.from({length:8},()=>(eR()-.5)*70);for(let t=0;t<EN;t++){const v=eYr[Math.floor(t/4)]+300+[-60,80,40,-50][t%4]-t*2.2+(t>=21&&t<=23?-70:0)+(t%7===3?-25:0);eTrue.push(v);eObs.push(v+(eR()-.5)*36)}
for(let t=0;t<EN;t++)eWf.push(eTrue[t]+(eR()-.5)*30);
const qlab=t=>(2018+Math.floor(t/4))+' Q'+(t%4+1);let eRollT=null;
function eDraw(){const sp=+$('#e-split').value;$('#e-lab').textContent=qlab(sp);const svg=$('#e-chart');svg.innerHTML='';const W=1190,L=50,B=360,T=36;
 const X=t=>L+t*(W-L-20)/(EN-1),Y=v=>B-(v-120)/(440-120)*(B-T);const tu=Math.max(4,sp-4);
 el('rect',{x:L,y:T,width:X(tu)-L,height:B-T,fill:'#eef9f6'},svg);el('rect',{x:X(tu),y:T,width:X(sp)-X(tu),height:B-T,fill:'#e1f2ee'},svg);el('rect',{x:X(sp)-8,y:T,width:W-X(sp)+8,height:B-T,fill:'#fff7e6'},svg);
 el('text',{x:L+10,y:T-12,'font-size':15,'font-weight':700,fill:'#0e8f86'},svg,'TRAIN');el('text',{x:X(tu)+8,y:T-12,'font-size':15,'font-weight':700,fill:'#3c5a6b'},svg,'TUNE');el('text',{x:X(sp),y:T-12,'font-size':15,'font-weight':700,fill:'#d9822b'},svg,'TEST · unseen later quarters');
 for(let k=0;k<=4;k++){const v=120+80*k;el('line',{x1:L,x2:W-10,y1:Y(v),y2:Y(v),class:'ax'},svg);el('text',{x:L-8,y:Y(v)+5,'text-anchor':'end',class:'tick'},svg,v)}
 for(let t=0;t<EN;t+=4)el('text',{x:X(t),y:B+24,class:'tick','text-anchor':'middle'},svg,2018+t/4);
 let d='';eObs.forEach((v,t)=>d+=(t?'L':'M')+X(t)+','+Y(v));el('path',{d,stroke:'#a9bfc6','stroke-width':3,fill:'none'},svg);eObs.forEach((v,t)=>el('circle',{cx:X(t),cy:Y(v),r:4,fill:'#a9bfc6'},svg));
 if(step>=1){let b='';for(let t=sp;t<EN;t++)b+=(t>sp?'L':'M')+X(t)+','+Y(eObs[t-4]);el('path',{d:b,stroke:'#7a8fa0','stroke-width':3,'stroke-dasharray':'8 6',fill:'none'},svg)}
 if(step>=2){let w='';for(let t=sp;t<EN;t++)w+=(t>sp?'L':'M')+X(t)+','+Y(eWf[t]);el('path',{d:w,stroke:'#0e8f86','stroke-width':4,fill:'none'},svg)}
 // metrics
 let sc=0,nn=0;for(let t=4;t<sp;t++){sc+=Math.abs(eObs[t]-eObs[t-4]);nn++}sc/=nn;
 const m=f=>{let a=0,r=0,n=0;for(let t=sp;t<EN;t++){const e=eObs[t]-f(t);a+=Math.abs(e);r+=e*e;n++}return{mae:a/n,rmse:Math.sqrt(r/n),mase:a/n/sc,n}};
 const mb=m(t=>eObs[t-4]),mw=m(t=>eWf[t]);const row=(lab,a,b,mx,d)=>`<div class="mt"><div class="mn"><span>${lab}</span></div>
 <div class="mr">baseline<div class="t"><div class="f" style="width:${step>=1?Math.min(100,a/mx*100):0}%;background:#7a8fa0"></div></div><b>${step>=1?fmt(a,d):'–'}</b></div>
 <div class="mr">workflow<div class="t"><div class="f" style="width:${step>=2?Math.min(100,b/mx*100):0}%;background:var(--sea)"></div></div><b>${step>=2?fmt(b,d):'–'}</b></div></div>`;
 $('#e-metrics').innerHTML=`<div class="small" style="margin-bottom:10px">${mb.n} test quarters · ${qlab(sp)} – ${qlab(EN-1)}</div>`+row('MAE (mt)',mb.mae,mw.mae,Math.max(mb.mae,mw.mae)*1.2,1)+row('RMSE (mt)',mb.rmse,mw.rmse,Math.max(mb.rmse,mw.rmse)*1.2,1)+row('MASE',mb.mase,mw.mase,Math.max(mb.mase,mw.mase,1)*1.2,2)
 +(step>=2?`<div style="font:600 19px/1.35 PF;color:var(--ink);margin-top:4px">${mw.mae<mb.mae?'Workflow beats the baseline on these quarters.':'Workflow does not beat the baseline: we would report that.'}</div>`:'')}
$('#e-split').oninput=()=>{if(step<1)setStep(1);eDraw()};
function eStop(){clearInterval(eRollT);eRollT=null;$('#e-roll').textContent='▶ Rolling origin'}
$('#e-roll').onclick=()=>{if(eRollT){eStop();return}if(step<2)setStep(2);const s=$('#e-split');s.value=12;eDraw();$('#e-roll').textContent='❚❚ Pause';eRollT=setInterval(()=>{if(+s.value>=24){eStop();return}s.value=+s.value+1;eDraw()},700)};
ctrl['s-eval']={step(){eDraw()},leave:eStop};
// contribution
const cR=rng(5),CN=8,cObs=[],cA=[],cBh=[],cBn=[];
for(let t=0;t<CN;t++){const v=320+[-50,70,30,-40][t%4]+(t===5||t===6?-85:0);cObs.push(v+(cR()-.5)*16);cA.push(v+(t===5||t===6?80:0)+(cR()-.5)*50);cBh.push(v+(t===5||t===6?18:0)+(cR()-.5)*22);}
for(let t=0;t<CN;t++)cBn.push(cA[t]+(cR()-.4)*14);
let cM='AB',cRes='help';
function cDraw(){$$('#s-contrib [data-m]').forEach(c=>c.classList.toggle('on',c.dataset.m===cM));$$('#s-contrib [data-r]').forEach(c=>c.classList.toggle('on',c.dataset.r===cRes));
 $('#c-A').classList.toggle('on',step>=1&&cM!=='B');$('#c-B').classList.toggle('on',step>=2&&cM!=='A');
 const B=cRes==='help'?cBh:cBn,svg=$('#c-chart');svg.innerHTML='';const W=1100,L=50,Bt=300,T=14;const X=t=>L+40+t*(W-L-80)/(CN-1),Y=v=>Bt-(v-150)/(460-150)*(Bt-T);
 for(let k=0;k<=3;k++){const v=150+k*100;el('line',{x1:L,x2:W-10,y1:Y(v),y2:Y(v),class:'ax'},svg);el('text',{x:L-8,y:Y(v)+5,'text-anchor':'end',class:'tick'},svg,v)}
 for(let t=0;t<CN;t++)el('text',{x:X(t),y:Bt+24,'text-anchor':'middle',class:'tick'},svg,'Test Q'+(t+1));
 el('rect',{x:X(4.6),y:T,width:X(6.4)-X(4.6),height:Bt-T,fill:'#fff7e6'},svg);el('text',{x:X(5.5),y:T+18,'text-anchor':'middle','font-size':14,'font-weight':700,fill:'#d9822b'},svg,'post-typhoon quarters');
 const line=(a,c,w,da)=>{let d='';a.forEach((v,t)=>d+=(t?'L':'M')+X(t)+','+Y(v));el('path',{d,stroke:c,'stroke-width':w,fill:'none','stroke-dasharray':da||''},svg)};
 line(cObs,'#a9bfc6',3);cObs.forEach((v,t)=>el('circle',{cx:X(t),cy:Y(v),r:5,fill:'#a9bfc6'},svg));
 if(step>=1&&cM!=='B')line(cA,'#3c5a6b',3,'8 6');if(step>=2&&cM!=='A')line(B,'#d9822b',4);
 const met=f=>{let a=0,r=0;for(let t=0;t<CN;t++){const e=cObs[t]-f[t];a+=Math.abs(e);r+=e*e}return[a/CN,Math.sqrt(r/CN),a/CN/62]};const ma=met(cA),mbb=met(B);
 const names=['MAE (mt)','RMSE (mt)','MASE'];$('#c-bars').innerHTML=names.map((n,k)=>{const mx=Math.max(ma[k],mbb[k])*1.15;return `<div style="flex:1"><div class="lab">${n}</div>
 <div class="mt" style="margin:6px 0 0"><div class="mr">A<div class="t"><div class="f" style="width:${step>=1?ma[k]/mx*100:0}%;background:#3c5a6b"></div></div><b>${step>=1?fmt(ma[k],k==2?2:1):'–'}</b></div>
 <div class="mr">B<div class="t"><div class="f" style="width:${step>=2?mbb[k]/mx*100:0}%;background:var(--coral)"></div></div><b>${step>=2?fmt(mbb[k],k==2?2:1):'–'}</b></div></div></div>`}).join('');
 $('#c-verdict').innerHTML=step<2?'Press → to add Model B.':cRes==='help'?'Model B is more accurate on unseen quarters → mangrove history and typhoon exposure <span style="color:var(--sea)">add predictive value</span>. That does not show they <i>cause</i> landings to change.':'No improvement → we report that these predictors <span style="color:var(--coral)">did not add predictive value</span> for these provinces and quarters.'}
$$('#s-contrib [data-m]').forEach(c=>c.onclick=()=>{cM=c.dataset.m;if(step<2)setStep(2);else cDraw()});
$$('#s-contrib [data-r]').forEach(c=>c.onclick=()=>{cRes=c.dataset.r;if(step<2)setStep(2);else cDraw()});
ctrl['s-contrib']={step(){cDraw()}};
// value at risk
const VC=[["Province A · Cat 1",820,640,180,150],["Province B · Cat 2",410,300,260,290],["Province C · Cat 1",150,132,180,205],["Province D · Cat 2",260,190,140,175],["Province A · Cat 3",95,104,320,300]];
let vSel=0,vP='base';
$('#v-pick').innerHTML=VC.map((c,k)=>`<button class="chip" data-v="${k}" style="font-size:15px;padding:7px 12px">${c[0]}</button>`).join('');
const vVal=(c,p)=>Math.max(0,c[1]-c[2])*1000*(p==='proxy'?c[4]:c[3])*(1+ +$('#v-price').value/100);
const peso=v=>v>=1e6?'₱'+(v/1e6).toFixed(2)+'M':'₱'+Math.round(v).toLocaleString('en-US');
const vRank=$('#v-rank');vRank.innerHTML=VC.map((c,k)=>`<div class="rk" data-k="${k}"><div class="rn"></div><div class="rl">${c[0]}</div><div class="rt"><div class="rf"></div></div><div class="rv2"></div></div>`).join('');
function vDraw(){const c=VC[vSel],pct=+$('#v-price').value;$$('#v-pick .chip').forEach(b=>b.classList.toggle('on',+b.dataset.v===vSel));$$('#s-var [data-p]').forEach(b=>b.classList.toggle('on',b.dataset.p===vP));
 const sf=Math.max(0,c[1]-c[2]),pr=(vP==='proxy'?c[4]:c[3])*(1+pct/100);
 $('#v-sf').textContent=fmt(sf,0)+' mt';$('#v-pr').textContent='₱'+pr.toFixed(0)+'/kg';$('#v-prl').textContent=(vP==='proxy'?'unit-value proxy':'historical first-sale')+(pct?` · ${pct>0?'+':''}${pct}%`:'');$('#v-val').textContent=peso(vVal(c,vP));
 const svg=$('#v-chart');svg.innerHTML='';const W=710,B=164,T=24,mx=Math.max(c[1],c[2])*1.15,Y=v=>B-v/mx*(B-T);
 el('line',{x1:20,x2:W-20,y1:B,y2:B,class:'ax'},svg);
 el('rect',{x:150,y:Y(c[1]),width:150,height:B-Y(c[1]),fill:'#cfe6e1',rx:6},svg);el('text',{x:225,y:Y(c[1])-8,'text-anchor':'middle','font-size':18,'font-weight':700,fill:'#0b2a3c'},svg,fmt(c[1],0)+' mt');el('text',{x:225,y:B+22,'text-anchor':'middle',class:'tick'},svg,'Seasonal benchmark');
 el('rect',{x:410,y:Y(c[2]),width:150,height:B-Y(c[2]),fill:'#0e8f86',rx:6},svg);el('text',{x:485,y:Y(c[2])-8,'text-anchor':'middle','font-size':18,'font-weight':700,fill:'#0b2a3c'},svg,fmt(c[2],0)+' mt');el('text',{x:485,y:B+22,'text-anchor':'middle',class:'tick'},svg,'Next-quarter forecast');
 if(step>=1){if(sf>0){el('rect',{x:410,y:Y(c[1]),width:150,height:Y(c[2])-Y(c[1]),fill:'none',stroke:'#d9822b','stroke-width':3,'stroke-dasharray':'7 5',rx:4},svg);el('text',{x:575,y:(Y(c[1])+Y(c[2]))/2+6,'font-size':17,'font-weight':700,fill:'#d9822b'},svg,'shortfall')}else el('text',{x:575,y:Y(c[2])+20,'font-size':16,'font-weight':700,fill:'#0b8a5a'},svg,'no shortfall')}
 el('line',{x1:130,x2:580,y1:Y(c[1]),y2:Y(c[1]),stroke:'#6f8b99','stroke-dasharray':'4 4'},svg);
 // ranking
 const vals=VC.map(x=>vVal(x,vP)),order=vals.map((v,k)=>[v,k]).sort((a,b)=>b[0]-a[0]).map(x=>x[1]),mxv=Math.max(...vals)||1;
 $$('.rk',vRank).forEach(r=>{const k=+r.dataset.k,pos=order.indexOf(k);r.style.top=pos*86+'px';r.querySelector('.rn').textContent=pos+1;r.querySelector('.rf').style.width=vals[k]/mxv*100+'%';r.querySelector('.rv2').textContent=vals[k]?peso(vals[k]):'₱0';r.classList.toggle('sel',k===vSel)});
 const ob=VC.map(x=>vVal(x,'base')).map((v,k)=>[v,k]).sort((a,b)=>b[0]-a[0]).map(x=>x[1]),op=VC.map(x=>vVal(x,'proxy')).map((v,k)=>[v,k]).sort((a,b)=>b[0]-a[0]).map(x=>x[1]);
 const moved=ob.filter((k,i)=>op[i]!==k).length;$('#v-stab').innerHTML=`Price sensitivity: top-ranked combination ${ob[0]===op[0]?'<b>unchanged</b>':'<b style="color:var(--coral)">changes</b>'} under the proxy price; ${moved} of ${VC.length} positions shift. A uniform ±% change scales values but keeps the order.`}
$$('#v-pick .chip').forEach(b=>b.onclick=()=>{vSel=+b.dataset.v;vDraw()});$$('#s-var [data-p]').forEach(b=>b.onclick=()=>{vP=b.dataset.p;vDraw()});
$('#v-price').oninput=()=>{if(step<2)setStep(2);vDraw()};
ctrl['s-var']={step(){vDraw()}};
// Q bank
let qbCat=-1;
function qbDraw(){const term=($('#qb-search').value||'').toLowerCase();
 $('#qb-cats').innerHTML=`<button class="qcat${qbCat<0?' on':''}" data-c="-1">All questions<span>${QB.reduce((a,c)=>a+c[1].length,0)}</span></button>`+QB.map((c,k)=>`<button class="qcat${qbCat===k?' on':''}" data-c="${k}">${c[0]}<span>${c[1].length}</span></button>`).join('');
 let h='';QB.forEach((c,k)=>{if(qbCat>=0&&k!==qbCat)return;c[1].forEach(([q,a])=>{if(term&&!(q+' '+a).toLowerCase().includes(term))return;
  const extra=q.startsWith('How will you separate prediction')?'<p style="margin-top:10px"><span class="link" data-go="b-cause">Open the backup slide →</span></p>':'';h+=qaHTML(q,'<p>'+a+'</p>'+extra,false,c[0])})});
 $('#qb-list').innerHTML=h||'<p class="body">No matching questions.</p>';$$('#qb-cats .qcat').forEach(b=>b.onclick=()=>{qbCat=+b.dataset.c;qbDraw()})}
$('#qb-search').oninput=qbDraw;ctrl['b-qbank']={enter:qbDraw};
// init
const h=location.hash.slice(1),hi=slides.findIndex(s=>s.id===h);
slides[0].classList.add('active');go(hi>0?hi:0);
window.__deck={go,next,prev,setStep,goLabel,get cur(){return cur},get step(){return step},slides};
})();
