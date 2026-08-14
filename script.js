/* =========================================================
   Shatha Dweikat Website
   Main JavaScript
========================================================= */



/* ================= MOBILE NAVIGATION ================= */


const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");


if(navToggle && navLinks){


    navToggle.addEventListener("click",()=>{


        const opened =
        navLinks.classList.toggle("open");


        navToggle.setAttribute(
            "aria-expanded",
            opened
        );


    });



    navLinks.querySelectorAll("a").forEach(link=>{


        link.addEventListener("click",()=>{


            navLinks.classList.remove("open");


            navToggle.setAttribute(
                "aria-expanded",
                "false"
            );


        });


    });


}








/* ================= CLOSE MENU OUTSIDE ================= */


document.addEventListener(
"click",
(e)=>{


    if(
        navLinks &&
        navToggle &&
        !navLinks.contains(e.target) &&
        !navToggle.contains(e.target)
    ){


        navLinks.classList.remove("open");


        navToggle.setAttribute(
            "aria-expanded",
            "false"
        );


    }


});









/* ================= SCROLL REVEAL ================= */


const revealElements =
document.querySelectorAll(".reveal");



if(
"IntersectionObserver" in window &&
revealElements.length
){


const observer =
new IntersectionObserver(
(entries)=>{


entries.forEach(entry=>{


if(entry.isIntersecting){


entry.target.classList.add(
"in-view"
);



observer.unobserve(
entry.target
);



}


});


},
{
threshold:.15
}
);



revealElements.forEach(el=>{


observer.observe(el);


});



}else{


revealElements.forEach(el=>{


el.classList.add(
"in-view"
);


});


}









/* ================= SMOOTH SCROLL ================= */


document.querySelectorAll(
'a[href^="#"]'
).forEach(anchor=>{


anchor.addEventListener(
"click",
function(e){


const target =
document.querySelector(
this.getAttribute("href")
);



if(target){


e.preventDefault();



target.scrollIntoView({

behavior:"smooth",

block:"start"

});


}



});


});









/* ================= HEADER EFFECT ================= */


const header =
document.querySelector("header");



window.addEventListener(
"scroll",
()=>{


if(!header) return;



if(window.scrollY > 50){


header.style.background =
"rgba(247,241,231,.96)";


header.style.backdropFilter =
"blur(15px)";



}else{


header.style.background =
"transparent";


header.style.backdropFilter =
"none";



}



});









/* ================= BACK TO TOP ================= */


const backToTop =
document.querySelector(".back-to-top");



if(backToTop){



window.addEventListener(
"scroll",
()=>{


if(window.scrollY > 500){


backToTop.classList.add(
"show"
);



}else{


backToTop.classList.remove(
"show"
);



}


});





backToTop.addEventListener(
"click",
(e)=>{


e.preventDefault();



window.scrollTo({

top:0,

behavior:"smooth"

});



});


}

/* ================= DROPDOWN NAVIGATION ================= */
document.querySelectorAll('.nav-dropdown-toggle').forEach(toggle=>{
    toggle.addEventListener('click', event=>{
        event.stopPropagation();
        const item = toggle.closest('.nav-dropdown');
        const isOpen = item.classList.contains('open');
        document.querySelectorAll('.nav-dropdown.open').forEach(openItem=>{
            openItem.classList.remove('open');
            const openToggle = openItem.querySelector('.nav-dropdown-toggle');
            if(openToggle) openToggle.setAttribute('aria-expanded','false');
        });
        if(!isOpen){
            item.classList.add('open');
            toggle.setAttribute('aria-expanded','true');
        }
    });
});
document.querySelectorAll('.dropdown-menu a').forEach(link=>{
    link.addEventListener('click',()=>{
        document.querySelectorAll('.nav-dropdown.open').forEach(item=>item.classList.remove('open'));
        if(navLinks){
            navLinks.classList.remove('open');
            if(navToggle) navToggle.setAttribute('aria-expanded','false');
        }
    });
});
document.addEventListener('click', event=>{
    if(!event.target.closest('.nav-dropdown')){
        document.querySelectorAll('.nav-dropdown.open').forEach(item=>{
            item.classList.remove('open');
            const toggle=item.querySelector('.nav-dropdown-toggle');
            if(toggle) toggle.setAttribute('aria-expanded','false');
        });
    }
});
