from pathlib import Path

path = Path('index.html')
s = path.read_text(encoding='utf-8')


def replace_once(old, new, label):
    global s
    count = s.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly 1 match, found {count}')
    s = s.replace(old, new, 1)

replace_once(
    '<meta content="Gulf Coast Code Works builds practical custom software, web applications, workflow automation, reporting and QA/QC systems for real-world operations, including ReportFlow Pro." name="description"/>',
    '<meta content="Gulf Coast Code Works builds practical custom software, web applications, workflow automation, reporting and QA/QC systems, plus custom 3D design and print-ready product files for real-world operations." name="description"/>',
    'meta description'
)

replace_once(
    '.services-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:9px}',
    '.services-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:9px}',
    'home service grid columns'
)

css = r'''


/* ===== CUSTOM 3D DESIGN CAPABILITY ===== */
:root{--three-d-image:url("assets/3d-fleur-de-lis-concept.webp")}
.three-d-service{grid-column:1/-1;padding:0;overflow:hidden;display:grid;grid-template-columns:minmax(280px,.88fr) minmax(0,1.12fr);align-items:stretch}
.three-d-art{min-height:430px;background-image:linear-gradient(180deg,rgba(6,20,29,.05),rgba(6,20,29,.18)),var(--three-d-image);background-size:cover;background-position:center 48%;position:relative}
.three-d-art:after{content:'Concept Design';position:absolute;left:14px;bottom:14px;padding:6px 9px;border-radius:999px;background:rgba(7,31,46,.88);color:#f8e5b8;font-size:9px;font-weight:800;letter-spacing:.11em;text-transform:uppercase;border:1px solid rgba(247,229,188,.22)}
.three-d-copy{padding:28px;display:flex;flex-direction:column;justify-content:center}
.three-d-copy h3{font-family:'Cormorant Garamond',serif;font-size:40px;line-height:1.02;margin:2px 0 10px;color:#15344a}
.three-d-copy p{margin:0 0 14px;color:#425460;line-height:1.6}
.three-d-copy ul{columns:2;column-gap:28px;margin:8px 0 17px;padding-left:18px}
.three-d-copy li{break-inside:avoid;margin-bottom:7px}
.three-d-tags{display:flex;gap:7px;flex-wrap:wrap;margin:4px 0 12px}
.three-d-tags span{padding:5px 8px;border-radius:5px;background:#f5f1ea;border:1px solid rgba(16,52,73,.10);font-size:11px;color:#345467;font-weight:700}
.three-d-note{font-size:12px;color:#64747e;margin-top:9px;line-height:1.45}
.three-d-concept{grid-column:1/-1;padding:0;overflow:hidden;display:grid;grid-template-columns:minmax(280px,.85fr) minmax(0,1.15fr);align-items:stretch}
.three-d-concept .three-d-art{min-height:390px}
.three-d-concept-copy{padding:26px;display:flex;flex-direction:column;justify-content:center}
.three-d-concept-copy h3{font-family:'Cormorant Garamond',serif;font-size:38px;line-height:1.02;margin:2px 0 8px;color:#15344a}
.three-d-concept-copy p{margin:0 0 12px;color:#425460;line-height:1.6}
@media(max-width:900px){.three-d-service,.three-d-concept{grid-template-columns:1fr}.three-d-art,.three-d-concept .three-d-art{min-height:360px}.three-d-copy ul{columns:1}}
@media(max-width:560px){.three-d-art,.three-d-concept .three-d-art{min-height:310px}.three-d-copy,.three-d-concept-copy{padding:20px}.three-d-copy h3,.three-d-concept-copy h3{font-size:34px}}
'''
if 'CUSTOM 3D DESIGN CAPABILITY' in s:
    raise RuntimeError('3D CSS already present')
replace_once('\n</style>', css + '\n</style>', '3D CSS insertion')

replace_once(
    'Custom software, web applications, and digital tools built for the way real businesses operate — from the field to the office.</p>',
    'Custom software, web applications, digital tools, and custom 3D product design built for the way real businesses and creators operate — from the field to the office to the workbench.</p>',
    'home hero copy'
)

replace_once(
    '<div class="service-tile"><div class="service-code">SYSTEM</div><b>Consulting &amp;</b><span>System Design</span></div>\n</div>',
    '<div class="service-tile"><div class="service-code">SYSTEM</div><b>Consulting &amp;</b><span>System Design</span></div>\n<div class="service-tile"><div class="service-code">3D</div><b>Custom 3D</b><span>Printable Design</span></div>\n</div>',
    'home 3D service tile'
)

replace_once(
    '<div class="page-hero"><div class="wrap"><div class="eyebrow">Services</div><h1>Software built around your business.</h1><p>I focus on practical tools that help teams organize work, collect information, reduce manual effort and operate more efficiently.</p></div></div>',
    '<div class="page-hero"><div class="wrap"><div class="eyebrow">Services</div><h1>Software and custom design built around your idea.</h1><p>I build practical digital tools for business operations and custom 3D product concepts that can move from an idea, logo, sketch, or measurements toward a print-ready file.</p></div></div>',
    'services hero'
)

services_last = '<div class="panel"><h3>Consulting &amp; System Design</h3><p>Not every company knows exactly what needs to be built. I can help define the problem, shape the workflow and design the right solution.</p></div>'
services_feature = r'''<div class="panel three-d-service">
  <div class="three-d-art" role="img" aria-label="Original fleur-de-lis 3D printable decor concept"></div>
  <div class="three-d-copy">
    <div class="product-kicker">New Capability • Custom 3D Design</div>
    <h3>Turn an idea into a print-ready 3D product.</h3>
    <p>Start with a description, logo, sketch, dimensions, or reference images. I can develop the concept into controlled 3D geometry, refine it for additive manufacturing, and deliver files that are ready for a slicer and final print review.</p>
    <div class="three-d-tags"><span>STL / OBJ</span><span>Logo-to-3D</span><span>Custom Decor</span><span>Branded Products</span><span>Functional Concepts</span></div>
    <ul>
      <li>Branded desk plaques, signs, emblems and display pieces</li>
      <li>Original Gulf Coast and Louisiana-inspired decor</li>
      <li>Decorative and LED-tealight holders</li>
      <li>Organizers, stands, holders and shop accessories</li>
      <li>Custom concepts from measurements or sketches</li>
      <li>Print-ready files with geometry reviewed before delivery</li>
    </ul>
    <div class="product-actions"><a class="btn primary small" data-page="contact" data-contact-prefill="I want to discuss a custom 3D design / printable product. My idea is: " href="#">Start a 3D Design →</a></div>
    <div class="three-d-note">Physical printing can be quoted separately when available. Final material, size and print method are confirmed before production.</div>
  </div>
</div>'''
replace_once(services_last, services_last + '\n' + services_feature, 'services 3D feature')

portfolio_anchor = '<div class="panel"><div class="project" style="grid-template-columns:1fr"><div class="shot" style="min-height:240px"><img alt="Stack Test Pro screenshots"'
if s.count(portfolio_anchor) != 1:
    raise RuntimeError(f'portfolio anchor: expected 1 match, found {s.count(portfolio_anchor)}')
portfolio_feature = r'''<div class="panel three-d-concept">
  <div class="three-d-art" role="img" aria-label="Fleur-de-lis Gulf Coast decorative 3D product concept"></div>
  <div class="three-d-concept-copy">
    <div class="product-kicker">3D Product Concept • Gulf Coast Collection</div>
    <h3>Custom Fleur-de-Lis Decor</h3>
    <p>An original Louisiana-inspired product concept created to show what custom 3D design can become: branded decor, display pieces, holders, gifts, and one-off products shaped around a client idea rather than pulled from a generic catalog.</p>
    <div class="chips"><span class="chip">Original Concept</span><span class="chip">3D Printable</span><span class="chip">Louisiana Decor</span><span class="chip">Custom Product Design</span></div>
    <div class="product-note"><b>Concept stage:</b> The visual shown is a design direction. Before delivery, the geometry is rebuilt or refined for the target printer, material, scale, wall thickness, clearances and stability.</div>
    <div class="product-actions"><a class="btn primary small" data-page="contact" data-contact-prefill="I have a custom 3D product idea. I want something similar in spirit to the Gulf Coast / fleur-de-lis concept, but customized for: " href="#">Ask About Custom 3D Design →</a></div>
  </div>
</div>

'''
s = s.replace(portfolio_anchor, portfolio_feature + portfolio_anchor, 1)

replace_once(
    '<div class="page-hero"><div class="wrap"><div class="eyebrow">How It Works</div><h1>A straightforward process.</h1><p>You do not need to show up with technical specs. Start with the problem, and we work from there.</p></div></div>',
    '<div class="page-hero"><div class="wrap"><div class="eyebrow">How It Works</div><h1>A straightforward process.</h1><p>You do not need to show up with technical specs or a finished CAD model. Start with the problem or the idea, and we work from there.</p></div></div>',
    'process hero'
)
replace_once(
    '<div class="panel"><h3>2. Define the workflow.</h3><p>We map out how the work is actually being done today and what a better process should look like.</p></div>',
    '<div class="panel"><h3>2. Define the workflow or design.</h3><p>For software, we map how the work is done today. For 3D projects, we define the shape, dimensions, use case, printer constraints and what the finished product needs to do.</p></div>',
    'process step 2'
)
replace_once(
    '<div class="panel"><h3>3. Build the right tool.</h3><p>Instead of forcing your company into generic software, I build a solution around the way your operation works.</p></div>',
    '<div class="panel"><h3>3. Build the right solution.</h3><p>That may be a custom application, an automation workflow, a reporting system, or a print-ready 3D model built around the actual requirement.</p></div>',
    'process step 3'
)

replace_once(
    '<div class="page-hero"><div class="wrap"><div class="eyebrow">Contact</div><h1>What’s slowing your business down?</h1><p>Tell me what keeps getting missed, repeated, delayed or manually tracked. We can work backward from the problem and decide what kind of tool actually makes sense.</p></div></div>',
    '<div class="page-hero"><div class="wrap"><div class="eyebrow">Contact</div><h1>What are you trying to solve or create?</h1><p>Tell me what keeps getting missed, repeated or manually tracked — or show me the custom product idea you want to turn into a 3D design. We can work backward from the need and decide the right way to build it.</p></div></div>',
    'contact hero'
)
replace_once(
    '<aside class="contact-card"><div class="eyebrow" style="color:#bdd0d5">Gulf Coast Code Works</div><h2>Let’s build something useful.</h2><p>Start with the business problem. The technical solution comes second.</p>',
    '<aside class="contact-card"><div class="eyebrow" style="color:#bdd0d5">Gulf Coast Code Works</div><h2>Let’s build something useful.</h2><p>Start with the business problem or the product idea. The technical solution comes second.</p>',
    'contact card'
)
replace_once(
    '<div class="field"><label for="problem">What problem are you trying to solve?</label><textarea id="problem" name="problem" placeholder="Tell me what you\'re doing today, what\'s frustrating, and what you\'d like to work better." required=""></textarea></div>',
    '<div class="field"><label for="problem">What problem are you trying to solve or what do you want to create?</label><textarea id="problem" name="problem" placeholder="Tell me what you\'re doing today, what\'s frustrating, or describe the custom software / 3D product you want to build." required=""></textarea></div>',
    'contact form question'
)
replace_once(
    '<footer class="footer"><div class="wrap"><span>© 2026 Gulf Coast Code Works. All rights reserved.</span><span>Software • Web • Apps • Automation</span></div></footer>',
    '<footer class="footer"><div class="wrap"><span>© 2026 Gulf Coast Code Works. All rights reserved.</span><span>Software • Web • Apps • Automation • 3D Design</span></div></footer>',
    'footer'
)

path.write_text(s, encoding='utf-8')
print('Applied custom 3D design website update.')
