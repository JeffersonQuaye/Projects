'use strict'

const $navbar = document.querySelector('[data-navbar]') 
const $navToggler = document.querySelector('[data-nav-toggler]') 

$navToggler.addEventListener('click', () => $navbar.classList.toggle('active'))



// Header Scroll State

const $header = document.querySelector('[data-header]')

window.addEventListener('scroll', e => {
    $header.classList[window.scrollY > 50 ? 'add' : 'remove']('active')
})


// Favorite Button

const $toggleBtn = document.querySelectorAll("[data-toggle-btn]")

$toggleBtn.forEach($toggleBtn => {
    $toggleBtn.addEventListener('click', () => {
        $toggleBtn.classList.toggle('active')
    })
})