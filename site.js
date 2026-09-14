
(function(){
  const btn=document.querySelector('.menu-btn'); const nav=document.querySelector('.navlinks');
  if(btn&&nav){btn.addEventListener('click',()=>{nav.classList.toggle('open');btn.setAttribute('aria-expanded',nav.classList.contains('open')?'true':'false')});}
  document.querySelectorAll('.navlinks a').forEach(a=>a.addEventListener('click',()=>nav&&nav.classList.remove('open')));
})();
