
(function(){
  const btn=document.querySelector('.menu-btn'); const nav=document.querySelector('.navlinks');
  if(btn&&nav){btn.addEventListener('click',()=>{nav.classList.toggle('open');btn.setAttribute('aria-expanded',nav.classList.contains('open')?'true':'false')});}
  document.querySelectorAll('.navlinks a').forEach(a=>a.addEventListener('click',()=>nav&&nav.classList.remove('open')));
  const form=document.getElementById('contactForm');
  if(form){form.addEventListener('submit',function(e){e.preventDefault(); const fd=new FormData(form); const subject='Gulf Coast Code Works inquiry — '+(fd.get('company')||fd.get('name')||'New project'); const body=['Name: '+(fd.get('name')||''),'Email: '+(fd.get('email')||''),'Company: '+(fd.get('company')||''),'Project type: '+(fd.get('project')||''),'','Problem / idea:',''+(fd.get('message')||'')].join('\n'); location.href='mailto:gulfcoastcodeworks@gmail.com?subject='+encodeURIComponent(subject)+'&body='+encodeURIComponent(body);});}
})();
