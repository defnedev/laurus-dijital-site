// Laurus 3D showcase: real-looking phones and laptops, floating in a gold-dust studio,
// screens cycling through real client work.
import * as THREE from './three-0170.min.js';
import { RoundedBoxGeometry } from './rbox-0170.js';
import { RoomEnvironment } from './roomenv-0170.js';

const host = document.querySelector('.h3d');
const hero = host && host.closest('.hero3');
if (host && hero) start();

function start() {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = innerWidth < 760;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' }); }
  catch (e) { hero.classList.add('h3d-off'); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.05;
  host.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x0b120e, 20, 42);
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture;
  const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
  const target = new THREE.Vector3();

  const key = new THREE.DirectionalLight(0xfff0d2, 2.6); key.position.set(6, 9, 9); scene.add(key);
  const rim = new THREE.DirectionalLight(0xbfe3c4, 2.4); rim.position.set(-9, 4, -6); scene.add(rim);
  const fill = new THREE.DirectionalLight(0xffffff, 0.5); fill.position.set(-4, -2, 9); scene.add(fill);
  scene.add(new THREE.AmbientLight(0x22302a, 0.6));

  // ---------- helpers ----------
  const C = (w, h, draw) => { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); return new THREE.CanvasTexture(c); };
  const rr = (g, x, y, w, h, r) => { g.beginPath(); g.roundRect(x, y, w, h, r); g.fill(); };
  const mask = (w, h, r) => C(w, h, (g) => { g.fillStyle = '#000'; g.fillRect(0, 0, w, h); g.fillStyle = '#fff'; rr(g, 1, 1, w - 2, h - 2, r); });
  const logoTex = C(256, 256, (g) => {
    g.save(); g.scale(6.4, 6.4);
    g.fillStyle = '#D9B24C'; rr(g, 0, 0, 40, 40, 11);
    g.fillStyle = '#0D1611'; g.fill(new Path2D('M11 8h5.6v18.4H29V32H11z')); g.fill(new Path2D('M20.5 21.5c.2-6.4 3.6-11 9.5-13 .4 6.3-3.1 11.2-9.5 13z'));
    g.fillStyle = '#D9B24C'; g.fill(new Path2D('M21.6 20.4c1.6-3.4 3.8-6.2 6.9-8.6-.2.4-3.6 4.8-6.9 8.6z')); g.restore();
  });
  logoTex.colorSpace = THREE.SRGBColorSpace;
  const keysTex = C(1024, 400, (g, w, h) => {
    g.fillStyle = '#16191a'; g.fillRect(0, 0, w, h);
    const rows = 6, kh = h / rows;
    for (let r = 0; r < rows; r++) { const n = r === 0 ? 14 : 13, kw = w / n;
      for (let k = 0; k < n; k++) { g.fillStyle = '#0b0d0e'; rr(g, k * kw + 4, r * kh + 4, kw - 8, kh - 8, 8); } }
  });
  const loader = new THREE.TextureLoader(); const cache = {};
  function fitCover(t) {
    const a = t.image.width / t.image.height, ta = t.userData.aspect || a;
    t.repeat.set(1, 1); t.offset.set(0, 0);
    if (a > ta) { t.repeat.x = ta / a; t.offset.x = (1 - t.repeat.x) / 2; }
    else { t.repeat.y = a / ta; t.offset.y = 1 - t.repeat.y; }
    t.needsUpdate = true;
  }
  function screenTex(src, aspect) {
    const k = src + '|' + aspect; if (cache[k]) return cache[k];
    const t = loader.load(src, (t) => fitCover(t)); t.userData.aspect = aspect;
    t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; cache[k] = t; return t;
  }

  const finishes = {
    natural: { frame: 0xb9b2a6, back: 0xa9a399 },
    desert: { frame: 0xcdb08a, back: 0xbfa583 },
    black: { frame: 0x3a3b3d, back: 0x1f2022 },
    silver: { frame: 0xcfd2d4, back: 0xc3c6c8 },
    space: { frame: 0x5a5e61, back: 0x4a4d50 },
  };
  const frameMat = (f) => new THREE.MeshPhysicalMaterial({ color: finishes[f].frame, metalness: 1, roughness: 0.34, clearcoat: 0.35, clearcoatRoughness: 0.4, envMapIntensity: 1.5 });
  const backMat = (f) => new THREE.MeshPhysicalMaterial({ color: finishes[f].back, metalness: 0.25, roughness: 0.52, clearcoat: 0.45, clearcoatRoughness: 0.5, envMapIntensity: 0.9 });
  const glassBlack = new THREE.MeshPhysicalMaterial({ color: 0x020304, metalness: 0, roughness: 0.05, clearcoat: 1, clearcoatRoughness: 0.02, envMapIntensity: 1.6 });
  const lensGlass = new THREE.MeshPhysicalMaterial({ color: 0x05070b, metalness: 0.3, roughness: 0.03, clearcoat: 1, clearcoatRoughness: 0, envMapIntensity: 2.6 });
  const lensDeep = new THREE.MeshPhysicalMaterial({ color: 0x101a33, metalness: 0.9, roughness: 0.15, envMapIntensity: 2.2 });
  const darkMat = new THREE.MeshStandardMaterial({ color: 0x0a0b0c, roughness: 0.6, metalness: 0.3 });

  const rrShape = (w, h, r) => { const s = new THREE.Shape(), x = -w / 2, y = -h / 2;
    s.moveTo(x + r, y); s.lineTo(x + w - r, y); s.absarc(x + w - r, y + r, r, -Math.PI / 2, 0);
    s.lineTo(x + w, y + h - r); s.absarc(x + w - r, y + h - r, r, 0, Math.PI / 2);
    s.lineTo(x + r, y + h); s.absarc(x + r, y + h - r, r, Math.PI / 2, Math.PI);
    s.lineTo(x, y + r); s.absarc(x + r, y + r, r, Math.PI, Math.PI * 1.5); return s; };
  const slab = (w, h, r, d, b, seg = 28) => { const g = new THREE.ExtrudeGeometry(rrShape(w - 2 * b, h - 2 * b, Math.max(0.001, r - b)), { depth: d - 2 * b, bevelEnabled: true, bevelThickness: b, bevelSize: b, bevelSegments: 5, curveSegments: seg }); g.translate(0, 0, -(d - 2 * b) / 2); return g; };

  // moving glass reflection
  const sheenTex = C(256, 512, (g, w, h) => { const gr = g.createLinearGradient(0, 0, w, h);
    gr.addColorStop(0, 'rgba(255,255,255,0)'); gr.addColorStop(.36, 'rgba(255,255,255,0)'); gr.addColorStop(.47, 'rgba(255,255,255,.2)'); gr.addColorStop(.5, 'rgba(255,255,255,.06)'); gr.addColorStop(.58, 'rgba(255,255,255,.13)'); gr.addColorStop(.66, 'rgba(255,255,255,0)'); gr.addColorStop(1, 'rgba(255,255,255,0)');
    g.fillStyle = gr; g.fillRect(0, 0, w, h); });
  sheenTex.wrapS = sheenTex.wrapT = THREE.RepeatWrapping;
  const sheens = [];

  const PW = 1.5, PH = 3.08, PD = 0.165, PR = 0.25;
  const SPW = PW - 0.1, SPH = PH - 0.1, SR = PR - 0.05;
  const mP = mask(560, Math.round(560 * SPH / SPW), Math.round(SR / SPW * 560)), mIsland = mask(256, 72, 36);
  const screens = [];

  function screenPair(w, h, m, list, aspect, z, group, y = 0) {
    const geo = new THREE.PlaneGeometry(w, h);
    const a = new THREE.MeshBasicMaterial({ map: screenTex(list[0], aspect), alphaMap: m, transparent: true, toneMapped: false });
    const b = new THREE.MeshBasicMaterial({ map: screenTex(list[1 % list.length], aspect), alphaMap: m, transparent: true, opacity: 0, toneMapped: false, depthWrite: false });
    const ma = new THREE.Mesh(geo, a), mb = new THREE.Mesh(geo, b);
    ma.position.set(0, y, z); mb.position.set(0, y, z + 0.0008);
    group.add(ma); group.add(mb);
    const st = sheenTex.clone(); st.needsUpdate = true;
    const sh = new THREE.Mesh(geo, new THREE.MeshBasicMaterial({ map: st, alphaMap: m, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false, toneMapped: false, opacity: 0.9 }));
    sh.position.set(0, y, z + 0.0016); group.add(sh); sheens.push({ t: st, g: group });
    screens.push({ a, b, list, aspect, i: 0, fade: -1, next: 4 + Math.random() * 5 });
    return ma;
  }

  function makePhone(finish, list) {
    const g = new THREE.Group(); const fm = frameMat(finish), bm = backMat(finish);
    // titanium band with soft chamfer
    g.add(new THREE.Mesh(slab(PW, PH, PR, PD, 0.028), fm));
    // front glass, edge to edge
    const front = new THREE.Mesh(new THREE.ShapeGeometry(rrShape(PW - 0.03, PH - 0.03, PR - 0.015), 28), glassBlack);
    front.position.z = PD / 2 + 0.0008; g.add(front);
    const scr = screenPair(SPW, SPH, mP, list, SPW / SPH, PD / 2 + 0.0016, g);
    const isl = new THREE.Mesh(new THREE.PlaneGeometry(0.4, 0.112), new THREE.MeshBasicMaterial({ color: 0x000000, alphaMap: mIsland, transparent: true }));
    isl.position.set(0, SPH / 2 - 0.135, PD / 2 + 0.004); g.add(isl);
    const cam = new THREE.Mesh(new THREE.CircleGeometry(0.028, 20), lensDeep); cam.position.set(0.11, SPH / 2 - 0.135, PD / 2 + 0.0045); g.add(cam);
    // back glass
    const back = new THREE.Mesh(new THREE.ShapeGeometry(rrShape(PW - 0.03, PH - 0.03, PR - 0.015), 28), bm);
    back.rotation.y = Math.PI; back.position.z = -PD / 2 - 0.0008; g.add(back);
    // side buttons + antenna breaks
    [[PW / 2 + 0.006, 0.55, 0.46], [PW / 2 + 0.006, -0.42, 0.3], [-PW / 2 - 0.006, 0.98, 0.17], [-PW / 2 - 0.006, 0.62, 0.3], [-PW / 2 - 0.006, 0.25, 0.3]].forEach(([x, y, h]) => {
      const bt = new THREE.Mesh(new RoundedBoxGeometry(0.026, h, 0.062, 3, 0.012), fm); bt.position.set(x, y, 0); g.add(bt); });
    [[PW / 2, 1.18], [-PW / 2, 1.18], [PW / 2, -1.18], [-PW / 2, -1.18]].forEach(([x, y]) => {
      const a = new THREE.Mesh(new THREE.BoxGeometry(0.004, 0.022, PD - 0.06), darkMat); a.position.set(x + Math.sign(x) * 0.0005, y, 0); g.add(a); });
    // camera plateau
    const zb = -PD / 2;
    const plat = new THREE.Mesh(slab(0.78, 0.8, 0.2, 0.05, 0.016, 20), bm.clone()); plat.material.roughness = 0.3; plat.material.clearcoat = 0.9;
    plat.position.set(0.3, 1.07, zb - 0.02); g.add(plat);
    [[0.48, 1.25], [0.48, 0.89], [0.14, 1.07]].forEach(([x, y]) => {
      const lens = new THREE.Group(); lens.position.set(x, y, zb - 0.045); lens.rotation.x = Math.PI / 2;
      const ring = new THREE.Mesh(new THREE.CylinderGeometry(0.158, 0.165, 0.05, 48), fm); lens.add(ring);
      const inner = new THREE.Mesh(new THREE.CylinderGeometry(0.132, 0.132, 0.054, 48), darkMat); lens.add(inner);
      const gl = new THREE.Mesh(new THREE.CylinderGeometry(0.118, 0.118, 0.058, 48), lensGlass); lens.add(gl);
      const iris = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.0595, 32), lensDeep); lens.add(iris);
      const pupil = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 0.0605, 24), darkMat); lens.add(pupil);
      g.add(lens);
    });
    const flash = new THREE.Mesh(new THREE.CircleGeometry(0.06, 24), new THREE.MeshStandardMaterial({ color: 0xfff3cf, emissive: 0x554422, roughness: 0.35 })); flash.rotation.y = Math.PI; flash.position.set(0.1, 1.33, zb - 0.0465); g.add(flash);
    const lidar = new THREE.Mesh(new THREE.CircleGeometry(0.05, 24), lensGlass); lidar.rotation.y = Math.PI; lidar.position.set(0.1, 0.8, zb - 0.0465); g.add(lidar);
    const logo = new THREE.Mesh(new THREE.PlaneGeometry(0.34, 0.34), new THREE.MeshPhysicalMaterial({ map: logoTex, transparent: true, alphaMap: mask(128, 128, 36), metalness: 0.9, roughness: 0.22, clearcoat: 0.6 }));
    logo.rotation.y = Math.PI; logo.position.set(0, -0.1, zb - 0.0016); g.add(logo);
    g.userData.screen = scr; return g;
  }

  function makeLaptop(finish, list) {
    const g = new THREE.Group(); const body = frameMat(finish); body.roughness = 0.42;
    const W = 4.7, D = 3.15, T = 0.11;
    const base = new THREE.Mesh(slab(W, D, 0.2, T, 0.02, 20), body); base.rotation.x = -Math.PI / 2; g.add(base);
    const well = new THREE.Mesh(new THREE.ShapeGeometry(rrShape(4.0, 1.56, 0.06), 12), darkMat); well.rotation.x = -Math.PI / 2; well.position.set(0, T / 2 + 0.0012, -0.55); g.add(well);
    const keys = new THREE.Mesh(new THREE.PlaneGeometry(3.94, 1.5), new THREE.MeshStandardMaterial({ map: keysTex, roughness: 0.75, metalness: 0.05 }));
    keys.rotation.x = -Math.PI / 2; keys.position.set(0, T / 2 + 0.002, -0.55); g.add(keys);
    const pad = new THREE.Mesh(new THREE.ShapeGeometry(rrShape(1.75, 1.08, 0.08), 12), new THREE.MeshPhysicalMaterial({ color: finishes[finish].frame, metalness: 0.9, roughness: 0.2, clearcoat: 0.9 }));
    pad.rotation.x = -Math.PI / 2; pad.position.set(0, T / 2 + 0.0015, 0.9); g.add(pad);
    const hinge = new THREE.Group(); hinge.position.set(0, T / 2, -D / 2 + 0.03); g.add(hinge);
    const bar = new THREE.Mesh(new THREE.CylinderGeometry(0.045, 0.045, W - 0.9, 16), darkMat); bar.rotation.z = Math.PI / 2; bar.position.set(0, 0.01, 0.02); hinge.add(bar);
    const LH = 3.05, LD = 0.05;
    const lid = new THREE.Mesh(slab(W, LH, 0.16, LD, 0.012, 20), body); lid.position.set(0, LH / 2, 0); hinge.add(lid);
    const bez = new THREE.Mesh(new THREE.ShapeGeometry(rrShape(W - 0.04, LH - 0.04, 0.14), 20), glassBlack); bez.position.set(0, LH / 2, LD / 2 + 0.0008); hinge.add(bez);
    const sw = W - 0.2, sh = sw / 1.6;
    const scr = screenPair(sw, sh, mask(900, 562, 12), list, 1.6, LD / 2 + 0.0016, hinge, LH / 2 + 0.03);
    const logo = new THREE.Mesh(new THREE.PlaneGeometry(0.62, 0.62), new THREE.MeshPhysicalMaterial({ map: logoTex, transparent: true, alphaMap: mask(128, 128, 36), metalness: 0.9, roughness: 0.22 }));
    logo.rotation.y = Math.PI; logo.position.set(0, LH / 2, -LD / 2 - 0.0012); hinge.add(logo);
    hinge.rotation.x = -0.24;
    g.userData.screen = scr; return g;
  }

  // ---------- staging ----------
  const P = (s) => '/img/' + s + '.webp';
  const phoneShots = ['app/lp-m', 'app/os-world', 'app/sb-home', 'app/nf-main', 'app/cn-home', 'real/nil-ig', 'app/sk-sekiz', 'app/seven-m', 'app/feronya-m'].map(P);
  const deskShots = ['real/nil-site', 'app/seven-d', 'app/feronya-d', 'app/sorbi-d', 'app/ohsame-d', 'app/lp-d', 'real/nil-galeri'].map(P);
  const rot = (arr, k) => arr.slice(k).concat(arr.slice(0, k));
  const plan = [
    { t: 'L', f: 'silver', l: rot(deskShots, 0), p: [1.5, -0.9, -3.4], r: [0.03, -0.3, 0], s: 1.5, m: false },
    { t: 'P', f: 'natural', l: rot(phoneShots, 0), p: [0.1, -0.3, 1.5], r: [0.02, 0.3, -0.03], s: 1.75 },
    { t: 'P', f: 'desert', l: rot(phoneShots, 2), p: [3.2, 0.25, 0.3], r: [0.04, Math.PI - 0.5, -0.05], s: 1.6 },
  ];
  const stage = new THREE.Group(); scene.add(stage);
  const devs = [];
  plan.forEach((d, i) => {
    if (mobile && d.m === false) return;
    const g = d.t === 'L' ? makeLaptop(d.f, d.l) : makePhone(d.f, d.l);
    const holder = new THREE.Group(); holder.add(g); stage.add(holder);
    holder.position.set(...d.p); g.rotation.set(...d.r); holder.scale.setScalar(0.001);
    holder.userData = { base: new THREE.Vector3(...d.p), rot: new THREE.Euler(...d.r), s: d.s, ph: i * 1.7, t0: 0.15 + i * 0.16, g, hov: 0, spinAt: d.t === 'P' ? 5 + i * 5.5 : 1e9 };
    devs.push(holder);
  });

  // gold dust
  const PC = mobile ? 700 : 1600;
  const pos = new Float32Array(PC * 3), spd = new Float32Array(PC);
  for (let i = 0; i < PC; i++) { pos[i * 3] = (Math.random() - 0.5) * 40; pos[i * 3 + 1] = (Math.random() - 0.5) * 20; pos[i * 3 + 2] = (Math.random() - 0.5) * 30 - 4; spd[i] = 0.06 + Math.random() * 0.2; }
  const pg = new THREE.BufferGeometry(); pg.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const dot = C(64, 64, (g) => { const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,236,170,1)'); gr.addColorStop(.35, 'rgba(217,178,76,.5)'); gr.addColorStop(1, 'rgba(217,178,76,0)'); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); });
  const pm = new THREE.PointsMaterial({ size: mobile ? 0.12 : 0.1, map: dot, transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, toneMapped: false });
  scene.add(new THREE.Points(pg, pm));

  // ---------- layout ----------
  let W = 1, H = 1, ox = 0, oy = 0, sc = 1;
  function size() {
    const r = host.getBoundingClientRect(); W = r.width || innerWidth; H = r.height || innerHeight;
    renderer.setSize(W, H, false); camera.aspect = W / H; camera.updateProjectionMatrix();
    if (W >= 1000) { ox = 3.9; oy = 1.5; sc = 1.0; } else if (W >= 760) { ox = 2.75; oy = 0.9; sc = 0.58; } else { ox = -0.8; oy = 5.3; sc = 0.68; }
    stage.position.set(ox, oy, 0); stage.scale.setScalar(sc);
  }
  size(); addEventListener('resize', size);

  // ---------- input ----------
  let mx = 0, my = 0, cx = 0, cy = 0, px = -9, py = -9;
  addEventListener('pointermove', (e) => { mx = e.clientX / innerWidth * 2 - 1; my = e.clientY / innerHeight * 2 - 1;
    const r = host.getBoundingClientRect(); px = (e.clientX - r.left) / r.width * 2 - 1; py = -((e.clientY - r.top) / r.height) * 2 + 1; }, { passive: true });
  const ray = new THREE.Raycaster(), v2 = new THREE.Vector2(); let hovered = null;
  const scrMeshes = devs.map((h) => h.userData.g.userData.screen);
  hero.addEventListener('click', (e) => {
    if (!hovered || e.target.closest('a,button')) return;
    const a = document.createElement('a'); a.href = '/calismalar'; a.setAttribute('data-pt', 'Çalışmalar'); a.style.display = 'none'; document.body.appendChild(a); a.click();
  });

  let visible = true;
  new IntersectionObserver((es) => { visible = es[0].isIntersecting; if (visible) loop(); }).observe(hero);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) loop(); });

  const clock = new THREE.Clock(); let T = 0, running = false; const _q = new THREE.Quaternion(), _e = new THREE.Euler();
  hero.classList.add('h3d-on');
  const ease = (t) => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);
  const eio = (t) => { t = Math.min(1, Math.max(0, t)); return t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };

  function frame() {
    const dt = Math.min(clock.getDelta(), 0.05); T += dt;
    const sp = Math.min(1, Math.max(0, scrollY / (hero.offsetHeight || 1)));
    devs.forEach((h) => {
      const u = h.userData, k = ease((T - u.t0) / 1.8);
      const fl = RM ? 0 : Math.sin(T * 0.55 + u.ph) * 0.14;
      h.position.set(u.base.x, u.base.y + fl - (1 - k) * 3.5, u.base.z + (1 - k) * 2);
      u.hov += ((hovered === h ? 1 : 0) - u.hov) * 0.1;
      h.scale.setScalar(Math.max(0.001, u.s * (0.7 + 0.3 * k) * (1 + u.hov * 0.03)));
      let spin = 0;
      if (!RM && T > u.spinAt) { const q = (T - u.spinAt) / 3.4; if (q >= 1) u.spinAt += 22 + u.ph * 2; else spin = eio(q) * Math.PI * 2; }
      u.g.rotation.set(u.rot.x + (RM ? 0 : Math.sin(T * 0.4 + u.ph) * 0.04), u.rot.y + (RM ? 0 : Math.sin(T * 0.3 + u.ph) * 0.12) + spin, u.rot.z);
    });
    sheens.forEach((o) => { o.g.getWorldQuaternion(_q); _e.setFromQuaternion(_q, 'YXZ'); o.t.offset.set(_e.y * 0.55 + cx * 0.15, _e.x * 0.4 + 0.1); });
    screens.forEach((s) => {
      if (RM) return;
      if (s.fade < 0 && T > s.next) s.fade = 0;
      if (s.fade >= 0) {
        s.fade += dt / 0.9; s.b.opacity = Math.min(1, s.fade);
        if (s.fade >= 1) { s.i = (s.i + 1) % s.list.length; s.a.map = screenTex(s.list[s.i], s.aspect); s.b.opacity = 0;
          s.b.map = screenTex(s.list[(s.i + 1) % s.list.length], s.aspect); s.fade = -1; s.next = T + 5 + Math.random() * 3; }
      }
    });
    const kk = ease(T / 2.4); pm.opacity = 0.8 * kk;
    if (!RM) { const p = pg.attributes.position.array; for (let i = 0; i < PC; i++) { p[i * 3 + 1] += spd[i] * dt; if (p[i * 3 + 1] > 10) p[i * 3 + 1] = -10; } pg.attributes.position.needsUpdate = true; }
    cx += (mx - cx) * 0.045; cy += (my - cy) * 0.045;
    stage.rotation.set(cy * 0.06 + sp * 0.12, cx * 0.16 - sp * 0.35, 0);
    camera.position.set(cx * 0.9, 1.1 - cy * 0.5 + sp * 1.2, (mobile ? 19 : 17.5) - sp * 5 + (1 - kk) * 3);
    target.set(ox * 0.32 + cx * 0.2, oy * 0.2 + sp * 0.5, 0); camera.lookAt(target);
    hovered = null;
    if (!mobile && px > -2) {
      v2.set(px, py); ray.setFromCamera(v2, camera);
      const hit = ray.intersectObjects(scrMeshes, false)[0];
      if (hit) { let o = hit.object; while (o && !devs.includes(o)) o = o.parent; hovered = o || null; }
    }
    hero.classList.toggle('h3d-hov', !!hovered);
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
