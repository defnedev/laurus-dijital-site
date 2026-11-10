// Laurus Kariyer 3D: a real-looking printed CV floats in a dark studio, a gold scan line reads it
// field by field, and the readability report counts up beside it.
import * as THREE from './three-0170.min.js';
import { RoundedBoxGeometry } from './rbox-0170.js';
import { RoomEnvironment } from './roomenv-0170.js';

const host = document.querySelector('.cv3d');
const hero = host && host.closest('.chero');
if (host && hero) start();

function start() {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = innerWidth < 760;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' }); }
  catch (e) { return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, mobile ? 1.7 : 1.8));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  host.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x070b09, 16, 34);
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  const camera = new THREE.PerspectiveCamera(30, 1, 0.1, 100);
  const target = new THREE.Vector3();

  const key = new THREE.DirectionalLight(0xfff1d6, 1.55); key.position.set(-5, 7, 9);
  key.castShadow = true; key.shadow.mapSize.set(1024, 1024); key.shadow.radius = 6; key.shadow.bias = -0.0004;
  Object.assign(key.shadow.camera, { left: -7, right: 7, top: 7, bottom: -7, near: 1, far: 30 });
  scene.add(key);
  const rim = new THREE.DirectionalLight(0x9bc59d, 1.1); rim.position.set(8, 2, -6); scene.add(rim);
  scene.add(new THREE.AmbientLight(0x1c2822, 0.7));
  const scanLight = new THREE.PointLight(0xffc75a, 0, 4.5, 1.6); scene.add(scanLight);

  // ---------- helpers ----------
  const mk = (w, h) => { const c = document.createElement('canvas'); c.width = w; c.height = h; return c; };
  const rr = (g, x, y, w, h, r) => { g.beginPath(); g.roundRect(x, y, w, h, r); };
  const FONT = '"Instrument Sans", "Helvetica Neue", Arial, sans-serif';
  const DISP = '"Bricolage Grotesque", "Helvetica Neue", Arial, sans-serif';

  // ---------- the CV page ----------
  const PW = 1240, PH = 1754;
  const FIELDS = [
    { key: 'İletişim', y0: 70, y1: 300 },
    { key: 'Profil', y0: 330, y1: 520 },
    { key: 'Deneyim', y0: 550, y1: 1150 },
    { key: 'Eğitim', y0: 1180, y1: 1360 },
    { key: 'Yetenekler', y0: 1390, y1: 1640 },
  ];
  function drawCV(c, prog, ghost) {
    const g = c.getContext('2d');
    g.fillStyle = '#FBFAF5'; g.fillRect(0, 0, PW, PH);
    // paper tooth
    g.globalAlpha = 0.035; for (let i = 0; i < 2600; i++) { g.fillStyle = Math.random() > 0.5 ? '#000' : '#8a7a5a'; g.fillRect(Math.random() * PW, Math.random() * PH, 1.4, 1.4); } g.globalAlpha = 1;
    // read highlights
    FIELDS.forEach((f, i) => {
      const k = Math.min(1, Math.max(0, prog[i] || 0)); if (!k) return;
      g.fillStyle = `rgba(46,150,88,${0.09 * k})`; rr(g, 70, f.y0, PW - 140, f.y1 - f.y0, 18); g.fill();
      g.fillStyle = `rgba(46,150,88,${0.85 * k})`; rr(g, 70, f.y0, 8, f.y1 - f.y0, 4); g.fill();
      const cx = PW - 120, cy = f.y0 + 46;
      g.fillStyle = `rgba(36,140,78,${k})`; g.beginPath(); g.arc(cx, cy, 26, 0, 7); g.fill();
      g.strokeStyle = `rgba(255,255,255,${k})`; g.lineWidth = 6; g.lineCap = 'round'; g.lineJoin = 'round';
      g.beginPath(); g.moveTo(cx - 11, cy + 1); g.lineTo(cx - 3, cy + 9); g.lineTo(cx + 12, cy - 8); g.stroke();
    });
    const ink = ghost ? '#4a504c' : '#141A16', soft = '#5E6A62', gold = '#A8842E';
    const bar = (x, y, w, h = 13, col = '#AEB5AD') => { g.fillStyle = col; rr(g, x, y, w, h, h / 2); g.fill(); };
    const txt = (s, x, y, size, w = 500, col = ink, f = FONT) => { g.fillStyle = col; g.font = `${w} ${size}px ${f}`; g.fillText(s, x, y); };
    // header
    g.fillStyle = '#E3E6E1'; g.beginPath(); g.arc(200, 185, 86, 0, 7); g.fill();
    g.fillStyle = '#C5CBC4'; g.beginPath(); g.arc(200, 160, 34, 0, 7); g.fill(); g.beginPath(); g.ellipse(200, 250, 58, 40, 0, Math.PI, 0); g.fill();
    txt(ghost ? 'Mert Aydın' : 'Elif Yıldız', 330, 170, 74, 700, ink, DISP);
    txt(ghost ? 'Muhasebe Uzmanı' : 'Kıdemli Satış Temsilcisi', 332, 222, 34, 600, gold);
    txt('İstanbul  ·  0532 000 00 00  ·  elif.yildiz@ornek.com  ·  linkedin.com/in/elif', 332, 272, 24, 500, soft);
    g.fillStyle = '#E2E4DE'; g.fillRect(100, 318, PW - 200, 3);
    const head = (s, y) => { txt(s, 110, y, 26, 700, gold); g.fillStyle = '#EAD9A8'; g.fillRect(110, y + 14, 60, 4); };
    head('PROFİL', 380);
    txt('B2B satışta 7 yıl deneyim. 40 kurumsal müşterilik portföy, yıllık satışta', 110, 432, 27, 500, '#2C332E');
    txt('yüzde 18 artış. CRM, saha satışı ve ekip içi eğitim.', 110, 472, 27, 500, '#2C332E');
    head('DENEYİM', 610);
    const job = (y, t, co, d, n) => {
      txt(t, 110, y, 31, 700, ink); g.font = `500 24px ${FONT}`; txt(d, PW - 110 - g.measureText(d).width, y, 24, 500, soft);
      txt(co, 110, y + 40, 25, 600, '#4B5A50');
      for (let i = 0; i < n; i++) { g.fillStyle = gold; g.beginPath(); g.arc(122, y + 88 + i * 40, 5, 0, 7); g.fill(); bar(142, y + 81 + i * 40, 520 + ((i * 137 + y) % 330), 13); }
    };
    job(670, 'Kıdemli Satış Temsilcisi', 'Ankora Endüstri A.Ş.', 'Eki 2022 – Bugün', 3);
    job(880, 'Satış Temsilcisi', 'Mavi Lojistik', 'Şub 2019 – Eyl 2022', 3);
    head('EĞİTİM', 1240);
    txt('İşletme, Lisans', 110, 1294, 30, 700, ink); g.font = `500 24px ${FONT}`; txt('2014 – 2018', PW - 110 - g.measureText('2014 – 2018').width, 1294, 24, 500, soft);
    txt('Marmara Üniversitesi', 110, 1334, 25, 600, '#4B5A50');
    head('YETENEKLER', 1450);
    let x = 110, y = 1490;
    ['Salesforce CRM', 'Excel', 'Sunum', 'Müzakere', 'Saha satışı', 'İngilizce B2', 'Raporlama'].forEach((s) => {
      g.font = `600 25px ${FONT}`; const w = g.measureText(s).width + 44;
      if (x + w > PW - 110) { x = 110; y += 66; }
      g.fillStyle = '#F1ECDD'; rr(g, x, y, w, 50, 25); g.fill(); g.fillStyle = '#5A4A1E'; g.fillText(s, x + 22, y + 34); x += w + 14;
    });
  }
  const cvCanvas = mk(PW, PH), cvTex = new THREE.CanvasTexture(cvCanvas);
  cvTex.colorSpace = THREE.SRGBColorSpace; cvTex.anisotropy = 8;
  const ghostCanvas = mk(PW, PH); drawCV(ghostCanvas, [], true);
  const ghostTex = new THREE.CanvasTexture(ghostCanvas); ghostTex.colorSpace = THREE.SRGBColorSpace; ghostTex.anisotropy = 4;

  const SW = 3.1, SH = SW * PH / PW;
  function paper(map, curl, lift) {
    const geo = new THREE.PlaneGeometry(SW, SH, 28, 40), p = geo.attributes.position;
    for (let i = 0; i < p.count; i++) {
      const x = p.getX(i) / (SW / 2), y = p.getY(i) / (SH / 2);
      const z = -curl * x * x + lift * Math.pow(Math.max(0, x), 3) * Math.pow(Math.max(0, -y), 3) + 0.02 * Math.sin(y * 3.1);
      p.setZ(i, z);
    }
    geo.computeVertexNormals();
    const m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map, roughness: 0.9, metalness: 0, side: THREE.DoubleSide, envMapIntensity: 0.35, color: 0xe9e7df }));
    m.castShadow = true; m.receiveShadow = true; return m;
  }

  const stage = new THREE.Group(); scene.add(stage);
  const main = new THREE.Group(); stage.add(main);
  const sheet = paper(cvTex, 0.09, 0.42); main.add(sheet);
  const back1 = paper(ghostTex, 0.06, 0.1); back1.position.set(-0.55, 0.75, -2.0); back1.rotation.set(0.05, 0.12, 0.1); back1.material.color.set(0xb9bdb6); stage.add(back1);
  const back2 = paper(ghostTex, 0.05, 0.0); back2.position.set(1.7, -0.25, -3.2); back2.rotation.set(-0.04, -0.3, -0.1); back2.material.color.set(0x8f948d); stage.add(back2);

  // scan beam
  const beamTex = (() => { const c = mk(16, 256), g = c.getContext('2d'); const gr = g.createLinearGradient(0, 0, 0, 256);
    gr.addColorStop(0, 'rgba(217,178,76,0)'); gr.addColorStop(0.47, 'rgba(255,214,120,.55)'); gr.addColorStop(0.5, 'rgba(255,246,214,1)'); gr.addColorStop(0.53, 'rgba(255,214,120,.55)'); gr.addColorStop(1, 'rgba(217,178,76,0)');
    g.fillStyle = gr; g.fillRect(0, 0, 16, 256); return new THREE.CanvasTexture(c); })();
  const beam = new THREE.Mesh(new THREE.PlaneGeometry(SW * 1.04, 0.62), new THREE.MeshBasicMaterial({ map: beamTex, transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false, toneMapped: false }));
  const edgeTex = (() => { const c = mk(256, 8), g = c.getContext('2d'); const gr = g.createLinearGradient(0, 0, 256, 0);
    gr.addColorStop(0, 'rgba(255,220,140,0)'); gr.addColorStop(.12, 'rgba(255,236,190,1)'); gr.addColorStop(.88, 'rgba(255,236,190,1)'); gr.addColorStop(1, 'rgba(255,220,140,0)'); g.fillStyle = gr; g.fillRect(0, 0, 256, 8); return new THREE.CanvasTexture(c); })();
  const edge = new THREE.Mesh(new THREE.PlaneGeometry(SW * 1.12, 0.022), new THREE.MeshBasicMaterial({ map: edgeTex, transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false, toneMapped: false }));
  beam.position.z = 0.09; edge.position.z = 0.1; main.add(beam); main.add(edge);

  // report card
  const RW = 1000, RH = 660, repCanvas = mk(RW, RH), repTex = new THREE.CanvasTexture(repCanvas); repTex.colorSpace = THREE.SRGBColorSpace; repTex.anisotropy = 8;
  function drawRep(score, prog) {
    const g = repCanvas.getContext('2d'); g.clearRect(0, 0, RW, RH);
    g.fillStyle = '#F7F6F0'; rr(g, 0, 0, RW, RH, 54); g.fill();
    g.fillStyle = '#141A16'; g.font = `700 44px ${FONT}`; g.fillText('CV okunabilirlik raporu', 60, 96);
    g.fillStyle = '#7A857D'; g.font = `500 30px ${FONT}`; g.fillText('örnek', RW - 140, 96);
    const s = Math.round(score), good = s >= 85;
    g.fillStyle = good ? '#1E7A45' : '#B2462E'; g.font = `800 190px ${DISP}`; g.fillText(String(s), 54, 300); const nw = g.measureText(String(s)).width;
    g.fillStyle = '#5E6A62'; g.font = `500 34px ${FONT}`; g.fillText('/ 100 · tüm alanlar', 54 + nw + 18, 300);
    g.fillStyle = '#E4E7E1'; rr(g, 60, 340, RW - 120, 18, 9); g.fill();
    g.fillStyle = good ? '#2E9A5A' : '#D18A3A'; rr(g, 60, 340, (RW - 120) * s / 100, 18, 9); g.fill();
    FIELDS.forEach((f, i) => {
      const y = 420 + i * 48, ok = (prog[i] || 0) > 0.6;
      g.fillStyle = '#2C332E'; g.font = `500 30px ${FONT}`; g.fillText(f.key, 60, y);
      g.fillStyle = ok ? '#1E7A45' : '#B2462E'; g.font = `700 28px ${FONT}`; const t = ok ? 'okundu' : 'okunmadı';
      g.fillText(t, RW - 60 - g.measureText(t).width, y);
    });
    repTex.needsUpdate = true;
  }
  const card = new THREE.Group();
  const cardW = 2.15, cardH = cardW * RH / RW;
  const cardBody = new THREE.Mesh(new RoundedBoxGeometry(cardW + 0.06, cardH + 0.06, 0.07, 4, 0.1), new THREE.MeshPhysicalMaterial({ color: 0xc9a65a, metalness: 1, roughness: 0.3, clearcoat: 0.6, transparent: true }));
  cardBody.castShadow = true; card.add(cardBody);
  const cardFace = new THREE.Mesh(new THREE.PlaneGeometry(cardW, cardH), new THREE.MeshStandardMaterial({ map: repTex, transparent: true, roughness: 0.5, metalness: 0, envMapIntensity: 0.4 }));
  cardFace.position.z = 0.037; card.add(cardFace);
  stage.add(card);

  // gold dust
  const PC = mobile ? 500 : 1100;
  const pos = new Float32Array(PC * 3), spd = new Float32Array(PC);
  for (let i = 0; i < PC; i++) { pos[i * 3] = (Math.random() - 0.5) * 34; pos[i * 3 + 1] = (Math.random() - 0.5) * 18; pos[i * 3 + 2] = (Math.random() - 0.5) * 22 - 5; spd[i] = 0.05 + Math.random() * 0.16; }
  const pg = new THREE.BufferGeometry(); pg.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const dotC = mk(64, 64), dg = dotC.getContext('2d'), gr = dg.createRadialGradient(32, 32, 0, 32, 32, 32);
  gr.addColorStop(0, 'rgba(255,236,170,1)'); gr.addColorStop(.35, 'rgba(217,178,76,.5)'); gr.addColorStop(1, 'rgba(217,178,76,0)'); dg.fillStyle = gr; dg.fillRect(0, 0, 64, 64);
  const pm = new THREE.PointsMaterial({ size: mobile ? 0.1 : 0.085, map: new THREE.CanvasTexture(dotC), transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, toneMapped: false });
  scene.add(new THREE.Points(pg, pm));

  // ---------- layout ----------
  let W = 1, H = 1, ox = 0, oy = 0, sc = 1, camZ = 15;
  function size() {
    const r = host.getBoundingClientRect(); W = r.width || innerWidth; H = r.height || innerHeight;
    renderer.setSize(W, H, false); camera.aspect = W / H; camera.updateProjectionMatrix();
    if (W >= 1100) { ox = 4.4; oy = -0.05; sc = 0.95; camZ = 15; }
    else if (W >= 760) { ox = 3.6; oy = 0; sc = 0.7; camZ = 15.5; }
    else { ox = 0.1; oy = 3.15; sc = 0.64; camZ = 17; }
    if (W >= 760) { const vh = Math.min(H, innerHeight), f = vh / H, units = 2 * camZ * Math.tan(15 * Math.PI / 180);
      sc *= Math.min(1, Math.max(0.68, f * 1.12)); oy += (1 - f) * units / 2 * 0.95; }
    stage.position.set(ox, oy, 0); stage.scale.setScalar(sc);
    card.position.set(W >= 760 ? 0.2 : 1.0, W >= 760 ? -1.55 : -1.15, 1.25); card.userData.y = card.position.y; card.rotation.set(0.04, W >= 760 ? 0.12 : -0.2, 0.03);
    if (W < 760) card.scale.setScalar(0.85); else card.scale.setScalar(1.15);
  }
  size(); addEventListener('resize', size);

  let mx = 0, my = 0, cx = 0, cy = 0;
  addEventListener('pointermove', (e) => { mx = e.clientX / innerWidth * 2 - 1; my = e.clientY / innerHeight * 2 - 1; }, { passive: true });

  let visible = true;
  new IntersectionObserver((es) => { visible = es[0].isIntersecting; if (visible) loop(); }).observe(hero);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) loop(); });

  const clock = new THREE.Clock(); let T = 0, running = false;
  const ease = (t) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
  const eio = (t) => { t = Math.min(1, Math.max(0, t)); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };

  // scan cycle: wait, scan (top→bottom), hold, fade back
  const CYC = 11, START = 1.6, SCAN = 4.2, HOLD = 4.2;
  let lastKey = '';
  const prog = FIELDS.map(() => 0);
  function scanState(t) {
    const c = ((t - START) % CYC + CYC) % CYC, active = t > START;
    let beamY = null, fade = 1;
    if (!active) { prog.fill(0); return { beamY, s: 61, on: 0 }; }
    if (c < SCAN) { const k = eio(c / SCAN); beamY = SH / 2 - 0.05 - k * (SH - 0.1); }
    const reach = c < SCAN ? (SH / 2 - beamY) / SH * PH : (c < SCAN + HOLD ? PH + 1 : -1);
    if (c >= SCAN + HOLD) fade = Math.max(0, 1 - (c - SCAN - HOLD) / (CYC - SCAN - HOLD) * 1.6);
    FIELDS.forEach((f, i) => { const k = reach < 0 ? 0 : Math.min(1, Math.max(0, (reach - f.y0) / 160)); prog[i] = (c >= SCAN + HOLD ? (prog[i] > 0 ? 1 : 0) * fade : k); });
    const done = prog.reduce((a, b) => a + b, 0) / FIELDS.length;
    return { beamY, s: 61 + 33 * done, on: beamY === null ? 0 : 1 };
  }
  if (RM) { prog.fill(1); drawCV(cvCanvas, prog); drawRep(94, prog); } else { drawCV(cvCanvas, prog); drawRep(61, prog); }
  cvTex.needsUpdate = true;
  hero.classList.add('cv3d-on');

  function frame() {
    const rdt = clock.getDelta(), dt = Math.min(rdt, 0.05); T += Math.min(rdt, 0.25);
    const sp = Math.min(1, Math.max(0, scrollY / (hero.offsetHeight || 1)));
    const k = ease(T / 1.9);
    if (!RM) {
      const st = scanState(T);
      const key2 = prog.map((p) => Math.round(p * 12)).join(',') + '|' + Math.round(st.s);
      if (key2 !== lastKey) { lastKey = key2; drawCV(cvCanvas, prog); cvTex.needsUpdate = true; drawRep(st.s, prog); }
      const bo = st.on;
      beam.material.opacity += ((bo ? 0.8 : 0) - beam.material.opacity) * 0.15; edge.material.opacity = beam.material.opacity;
      if (st.beamY !== null) { beam.position.y = st.beamY; edge.position.y = st.beamY; }
      const wp = new THREE.Vector3(0, beam.position.y, 0.9); main.localToWorld(wp); scanLight.position.copy(wp);
      scanLight.intensity += ((bo ? 3 : 0) - scanLight.intensity) * 0.12;
    }
    const fl = RM ? 0 : Math.sin(T * 0.6) * 0.09;
    main.position.set(0, fl - (1 - k) * 2.4, (1 - k) * 1.6);
    main.rotation.set(-0.08 + (RM ? 0 : Math.sin(T * 0.37) * 0.03), -0.32 + (RM ? 0 : Math.sin(T * 0.29) * 0.07), 0.035);
    const kc = ease((T - 0.5) / 1.8);
    card.visible = kc > 0.001;
        cardFace.material.opacity = kc; cardBody.material.opacity = kc;
    const fl2 = RM ? 0 : Math.sin(T * 0.7 + 1.3) * 0.07;
    card.position.z = 1.1 + (1 - kc) * 1.5; card.position.y = card.userData.y + fl2 - (1 - kc) * 0.6;
    back1.position.y = 0.75 + (RM ? 0 : Math.sin(T * 0.45 + 2) * 0.06);
    back2.position.y = -0.25 + (RM ? 0 : Math.sin(T * 0.4 + 4) * 0.05);
    pm.opacity = 0.7 * k;
    if (!RM) { const p = pg.attributes.position.array; for (let i = 0; i < PC; i++) { p[i * 3 + 1] += spd[i] * dt; if (p[i * 3 + 1] > 9) p[i * 3 + 1] = -9; } pg.attributes.position.needsUpdate = true; }
    cx += (mx - cx) * 0.045; cy += (my - cy) * 0.045;
    stage.rotation.set(cy * 0.07 + sp * 0.1, cx * 0.18 - sp * 0.3, 0);
    camera.position.set(cx * 0.8, 0.6 - cy * 0.45 + sp * 1.1, camZ - sp * 4 + (1 - k) * 2.5);
    target.set(ox * 0.3 + cx * 0.2, oy * 0.25 + sp * 0.4, 0); camera.lookAt(target);
    host.style.opacity = String(1 - sp * 0.7);
    renderer.render(scene, camera);
  }
  function loop() {
    if (running) return; running = true; clock.getDelta();
    (function tick() {
      if (!visible || document.hidden) { running = false; return; }
      frame();
      if (RM && T > 2.6) { running = false; return; }
      requestAnimationFrame(tick);
    })();
  }
  loop();
}
