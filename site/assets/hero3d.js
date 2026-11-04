// Laurus 3D showcase: a slowly orbiting ring of real work screens in a gold-dust field.
import * as THREE from './three-0170.min.js';

const host = document.querySelector('.h3d');
const hero = host && host.closest('.hero3');
if (host && hero) start();

function start() {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const mobile = innerWidth < 760;
  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
  } catch (e) { return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, mobile ? 1.5 : 1.75));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  host.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x0b120e, 18, 38);
  const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 80);
  const target = new THREE.Vector3(0, 0, 0);

  // rounded-corner alpha masks
  function mask(w, h, r) {
    const c = document.createElement('canvas'); c.width = w; c.height = h;
    const g = c.getContext('2d'); g.fillStyle = '#000'; g.fillRect(0, 0, w, h); g.fillStyle = '#fff';
    g.beginPath(); g.roundRect(2, 2, w - 4, h - 4, r); g.fill();
    const t = new THREE.CanvasTexture(c); return t;
  }
  const mD = mask(512, 320, 22), mP = mask(220, 476, 34);

  const V = (window.__H3D_IMGS || []);
  const loader = new THREE.TextureLoader();
  const ring = new THREE.Group();
  ring.rotation.z = -0.16; ring.rotation.x = 0.3;
  scene.add(ring);

  const R = mobile ? 5.2 : 7.2;
  const items = [];
  const n = V.length;
  V.forEach((it, i) => {
    const phone = it.k === 'p';
    const w = phone ? 1.7 : 4.3, h = phone ? 3.65 : 2.69;
    const tex = loader.load(it.src, t => { t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; });
    const mat = new THREE.MeshBasicMaterial({ map: tex, alphaMap: phone ? mP : mD, transparent: true, opacity: 0, fog: true });
    const mesh = new THREE.Mesh(new THREE.PlaneGeometry(w, h), mat);
    const glow = new THREE.Mesh(new THREE.PlaneGeometry(w * 1.06, h * 1.06),
      new THREE.MeshBasicMaterial({ color: 0xd9b24c, alphaMap: phone ? mP : mD, transparent: true, opacity: 0, blending: THREE.AdditiveBlending, depthWrite: false }));
    glow.position.z = -0.02;
    const holder = new THREE.Group(); holder.add(glow); holder.add(mesh);
    const a = (i / n) * Math.PI * 2;
    const y = (i % 2 ? 1 : -1) * (phone ? 0.35 : 0.95) + (i % 3 - 1) * 0.25;
    const rr = R + (phone ? 0.5 : -0.2);
    holder.position.set(Math.sin(a) * rr, y, Math.cos(a) * rr);
    holder.userData = { a, rr, y, href: it.href, t0: i * 0.07, mesh, glow, hover: 0 };
    ring.add(holder); items.push(holder);
  });

  // gold dust
  const PC = mobile ? 900 : 2000;
  const pos = new Float32Array(PC * 3), spd = new Float32Array(PC);
  for (let i = 0; i < PC; i++) {
    pos[i * 3] = (Math.random() - 0.5) * 34; pos[i * 3 + 1] = (Math.random() - 0.5) * 18; pos[i * 3 + 2] = (Math.random() - 0.5) * 30;
    spd[i] = 0.08 + Math.random() * 0.22;
  }
  const pg = new THREE.BufferGeometry(); pg.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  const dot = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const g = c.getContext('2d');
    const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(255,236,170,1)'); gr.addColorStop(.35, 'rgba(217,178,76,.55)'); gr.addColorStop(1, 'rgba(217,178,76,0)');
    g.fillStyle = gr; g.fillRect(0, 0, 64, 64); return new THREE.CanvasTexture(c); })();
  const pm = new THREE.PointsMaterial({ size: mobile ? 0.11 : 0.09, map: dot, transparent: true, opacity: 0, depthWrite: false, blending: THREE.AdditiveBlending, color: 0xffffff });
  const dust = new THREE.Points(pg, pm); scene.add(dust);

  // orbit lines
  const orbits = new THREE.Group(); scene.add(orbits);
  [R + 1.6, R + 2.6, R - 1.2].forEach((r, k) => {
    const pts = []; for (let i = 0; i <= 160; i++) { const a = i / 160 * Math.PI * 2; pts.push(new THREE.Vector3(Math.sin(a) * r, 0, Math.cos(a) * r)); }
    const l = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), new THREE.LineBasicMaterial({ color: 0xd9b24c, transparent: true, opacity: 0, fog: true }));
    l.rotation.x = 0.1 + k * 0.07; l.rotation.z = -0.12 + k * 0.05; l.userData.o = [0.22, 0.12, 0.08][k]; orbits.add(l);
  });

  // layout
  let W = 1, H = 1, ox = 0, oy = 0;
  function size() {
    const r = host.getBoundingClientRect(); W = r.width || innerWidth; H = r.height || innerHeight;
    renderer.setSize(W, H, false); camera.aspect = W / H; camera.updateProjectionMatrix();
    ox = W >= 1000 ? 10.2 : (W >= 760 ? 6 : 0); oy = W >= 760 ? -0.3 : 5.2;
    ring.position.set(ox, oy, 0); orbits.position.set(ox, oy, 0);
  }
  size(); addEventListener('resize', size);

  // input
  let mx = 0, my = 0, cx = 0, cy = 0, px = -9, py = -9;
  addEventListener('pointermove', e => { mx = e.clientX / innerWidth * 2 - 1; my = e.clientY / innerHeight * 2 - 1;
    const r = host.getBoundingClientRect(); px = (e.clientX - r.left) / r.width * 2 - 1; py = -((e.clientY - r.top) / r.height) * 2 + 1; }, { passive: true });
  const ray = new THREE.Raycaster(); const v2 = new THREE.Vector2(); let hovered = null;
  hero.addEventListener('click', e => {
    if (!hovered || e.target.closest('a,button')) return;
    const a = document.createElement('a'); a.href = hovered.userData.href; a.setAttribute('data-pt', 'Çalışmalar'); a.style.display = 'none';
    document.body.appendChild(a); a.click();
  });

  // visibility
  let visible = true;
  new IntersectionObserver(es => { visible = es[0].isIntersecting; if (visible) loop(); }, { threshold: 0 }).observe(hero);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) loop(); });

  const clock = new THREE.Clock(); let T = 0, running = false;
  hero.classList.add('h3d-on');
  const ease = t => 1 - Math.pow(1 - Math.min(1, Math.max(0, t)), 3);

  function frame() {
    const dt = Math.min(clock.getDelta(), 0.05); T += dt;
    const sp = Math.min(1, Math.max(0, scrollY / (hero.offsetHeight || 1)));
    // entrance
    items.forEach(h => {
      const u = h.userData, k = ease((T - u.t0) / 1.6);
      u.mesh.material.opacity = k;
      const z = (1 - k) * 6;
      h.position.set(Math.sin(u.a) * (u.rr + z), u.y + (1 - k) * -1.2, Math.cos(u.a) * (u.rr + z));
      h.lookAt(camera.position); h.rotateY(Math.sin(u.a + ring.rotation.y) * 0.45);
      u.hover += ((hovered === h ? 1 : 0) - u.hover) * 0.12;
      u.glow.material.opacity = (0.07 + u.hover * 0.35) * k;
      const s = 1 + u.hover * 0.06; h.scale.set(s, s, s);
    });
    const kk = ease(T / 2.2);
    pm.opacity = 0.85 * kk;
    orbits.children.forEach(l => { l.material.opacity = l.userData.o * kk; });
    if (!RM) {
      ring.rotation.y += dt * 0.07 * (1 + sp * 2.5);
      orbits.rotation.y -= dt * 0.03;
      const p = pg.attributes.position.array;
      for (let i = 0; i < PC; i++) { p[i * 3 + 1] += spd[i] * dt; if (p[i * 3 + 1] > 9) p[i * 3 + 1] = -9; }
      pg.attributes.position.needsUpdate = true;
    }
    cx += (mx - cx) * 0.04; cy += (my - cy) * 0.04;
    camera.position.set(cx * 1.6, 1.2 - cy * 0.8 + sp * 1.5, (mobile ? 19 : 23) - sp * 7 + (1 - kk) * 4);
    target.set(ox * 0.18 + cx * 0.3, oy * 0.55 + sp * 0.6, 0);
    camera.lookAt(target);
    // hover pick
    hovered = null;
    if (!mobile && px > -2) {
      v2.set(px, py); ray.setFromCamera(v2, camera);
      const hit = ray.intersectObjects(items.map(h => h.userData.mesh), false)[0];
      if (hit && hit.object.material.opacity > 0.8) hovered = hit.object.parent;
    }
    hero.classList.toggle('h3d-hov', !!hovered);
    host.style.opacity = String(1 - sp * 0.75);
    renderer.render(scene, camera);
  }
  function loop() {
    if (running) return; running = true;
    clock.getDelta();
    (function tick() {
      if (!visible || document.hidden) { running = false; return; }
      frame();
      if (RM && T > 2.5) { running = false; return; }
      requestAnimationFrame(tick);
    })();
  }
  loop();
}
