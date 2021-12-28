window.addEventListener('scroll',function (){
    let nav = document.querySelector('nav');
    nav.classList.toggle('scroll-active' , window.scrollY > 0);
})