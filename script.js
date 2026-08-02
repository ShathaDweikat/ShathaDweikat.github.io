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
