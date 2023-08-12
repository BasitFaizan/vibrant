let preloader = document.querySelector('.preloader')

window.addEventListener('load',()=>{
    setTimeout(()=>{

        preloader.style.display = 'none';
    })
})

// nav
let hamburger = document.querySelector('.hamburger')
let navlink = document.querySelector('.navlink')

hamburger.addEventListener('click',()=>{
    console.log('hello');
    navlink.classList.toggle('active')
})