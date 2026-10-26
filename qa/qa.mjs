let chromium; try{({chromium}=await import('/opt/node22/lib/node_modules/playwright/index.mjs'))}catch(e){({chromium}=await import('playwright'))}
import fs0 from 'fs'; const S=(process.env.QA_OUT||'/tmp/laurus-qa')+'/'; fs0.mkdirSync(S,{recursive:true});
const BASE=process.env.QA_BASE||'https://laurusdijital.com';
const sm=await (await fetch(BASE+'/sitemap.xml')).text();
const urls=[...sm.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m=>m[1]);
const b=await chromium.launch(); const report=[]; const links=new Set();
for (const [vw,vh,tag,mob] of [[390,844,'m',true],[1440,900,'d',false]]){
 const c=await b.newContext({viewport:{width:vw,height:vh},isMobile:mob,hasTouch:mob});
 for (const u of urls){
  const p=await c.newPage(); const errs=[],fails=[];
  p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>{if(m.type()==='error')errs.push('console:'+m.text().slice(0,120))});
  p.on('response',r=>{if(r.status()>=400)fails.push(r.status()+' '+r.url())}); p.on('requestfailed',r=>fails.push('fail '+r.url()));
  await p.addInitScript(()=>{try{sessionStorage.setItem('li','1')}catch(e){}});
  const res=await p.goto(u,{waitUntil:'networkidle',timeout:45000});
  // scroll through to trigger lazy/reveal
  const H=await p.evaluate(()=>document.body.scrollHeight);
  for(let y=0;y<H;y+=vh*0.8){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(120);}
  await p.waitForTimeout(600);
  const info=await p.evaluate(()=>{
    const out={};
    out.sw=document.documentElement.scrollWidth-innerWidth;
    out.title=document.title; out.desc=(document.querySelector('meta[name=description]')||{}).content||'';
    out.h1=document.querySelectorAll('h1').length; out.canon=(document.querySelector('link[rel=canonical]')||{}).href||'';
    out.imgBroken=[...document.images].filter(i=>i.complete&&i.naturalWidth===0&&i.getAttribute('loading')!=='lazy').map(i=>i.src).slice(0,5);
    out.noAlt=[...document.images].filter(i=>!i.hasAttribute('alt')).length;
    // text overflow: elements whose text is clipped horizontally
    out.clip=[...document.querySelectorAll('h1,h2,h3,p,a,button,span,b,li')].filter(e=>{const s=getComputedStyle(e);return e.offsetParent&&e.scrollWidth>e.clientWidth+2&&s.overflow!=='visible'&&s.textOverflow!=='ellipsis'&&e.clientWidth>0}).map(e=>(e.className||e.tagName)+':'+e.innerText.slice(0,40)).slice(0,6);
    // offscreen elements (overflow right edge)
    out.offR=[...document.querySelectorAll('main *, footer *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>innerWidth+2&&getComputedStyle(e).position!=='fixed'&&!e.closest('.reel,.as-sbg,.w3-track,.snap,.cuts,.as-dev,.stage,.tabs-list,[role=tablist],.svc3-row,.chips,.kplans,.table,.slide')}).map(e=>(e.className||e.tagName)+'').slice(0,5);
    // tiny text
    out.tiny=[...document.querySelectorAll('main p, main li, main a, footer a')].filter(e=>e.offsetParent&&parseFloat(getComputedStyle(e).fontSize)<12).length;
    // tap targets small (mobile)
    out.smallTap=[...document.querySelectorAll('a,button')].filter(e=>{const r=e.getBoundingClientRect();return e.offsetParent&&r.width>0&&(r.height<28||r.width<28)&&!e.closest('p,li,.crumbs,.fbot,.flinks,.knote,.lead,.as-tabs,footer')}).map(e=>e.innerText.slice(0,20)||e.getAttribute('aria-label')).slice(0,5);
    out.links=[...document.querySelectorAll('a[href]')].map(a=>a.href);
    return out;});
  info.links.forEach(l=>links.add(l)); delete info.links;
  if(tag==='m') await p.screenshot({path:S+u.replace(BASE,'').replace(/\//g,'_')+'-m.png',fullPage:true}).catch(()=>{});
  report.push({u:u.replace(BASE,'')||'/',tag,status:res.status(),errs,fails:fails.slice(0,4),...info});
  await p.close();
 }
 await c.close();
}
// link check
const bad=[];
for (const l of links){ if(!l.startsWith(BASE)) continue; const clean=l.split('#')[0]; try{const r=await fetch(clean,{redirect:'manual'}); if(r.status>=400) bad.push(r.status+' '+clean);}catch(e){bad.push('ERR '+clean)} }
const ext=[...links].filter(l=>/^https?:/.test(l)&&!l.startsWith(BASE)&&!l.includes('wa.me'));
const extBad=[]; for(const l of new Set(ext)){try{const r=await fetch(l,{method:'GET',redirect:'follow'}); if(r.status>=400) extBad.push(r.status+' '+l);}catch(e){extBad.push('ERR '+l)}}
await b.close();
import fs from 'fs'; fs.writeFileSync(S+'report.json',JSON.stringify({report,bad:[...new Set(bad)],ext:[...new Set(ext)],extBad},null,1));
const probs=report.filter(r=>r.status!==200||r.errs.length||r.fails.length||r.sw>0||r.imgBroken.length||r.clip.length||r.offR.length||r.h1!==1||r.noAlt);
console.log('pages',urls.length,'checks',report.length,'problem rows',probs.length);
for(const r of probs) console.log(JSON.stringify(r));
console.log('internal bad links',[...new Set(bad)]); console.log('ext',[...new Set(ext)].length,'extBad',extBad);
console.log('tiny/smallTap', report.filter(r=>r.tiny||r.smallTap.length).map(r=>r.u+'/'+r.tag+' tiny:'+r.tiny+' tap:'+r.smallTap.join('|')).slice(0,12));

// contact form test
{ const b2=await chromium.launch(); const c2=await b2.newContext({viewport:{width:390,height:844}}); const p2=await c2.newPage();
  await p2.addInitScript(()=>{try{sessionStorage.setItem('li','1')}catch(e){}});
  await c2.route(/wa\.me|whatsapp/, r=>r.fulfill({status:200,body:'ok'}));
  await p2.goto(BASE+'/',{waitUntil:'networkidle'});
  let ok=false; try{ await p2.fill('#f-name','Test'); await p2.fill('#f-biz','Deneme, kafe');
    const [pop]=await Promise.all([c2.waitForEvent('page',{timeout:8000}), p2.click('#quick button[type=submit]')]);
    ok=decodeURIComponent(pop.url()).includes('Merhaba, ben Test'); }catch(e){}
  console.log('form whatsapp ok:',ok); await b2.close(); }
