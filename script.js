/* =========================================================
   Shatha Dweikat Website
   Main JavaScript
========================================================= */


/* ================= LUCIDE ICONS ================= */


if(window.lucide){

    lucide.createIcons();

}



/* ================= MOBILE NAVIGATION ================= */


const navToggle =
document.getElementById("navToggle");


const navLinks =
document.getElementById("navLinks");



if(navToggle && navLinks){


navToggle.addEventListener(
"click",
()=>{


const opened =
navLinks.classList.toggle("open");


navToggle.setAttribute(
"aria-expanded",
opened
);


});



navLinks.querySelectorAll("a")
.forEach(link=>{


link.addEventListener(
"click",
()=>{


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
(event)=>{


if(
navLinks &&
navToggle &&
!navLinks.contains(event.target) &&
!navToggle.contains(event.target)

){


navLinks.classList.remove("open");


navToggle.setAttribute(
"aria-expanded",
"false"
);


}


});







/* ================= SMOOTH SCROLL ================= */


document.querySelectorAll(
'a[href^="#"]'
)
.forEach(anchor=>{


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



revealElements.forEach(
element=>{

observer.observe(element);

}
);



}else{


revealElements.forEach(
element=>{

element.classList.add(
"in-view"
);

}
);


}







/* ================= BACK TO TOP ================= */


const backTop =
document.querySelector(".back-to-top");



if(backTop){



window.addEventListener(
"scroll",
()=>{


if(window.scrollY > 500){


backTop.style.opacity="1";

backTop.style.pointerEvents="auto";


}else{


backTop.style.opacity="0";

backTop.style.pointerEvents="none";


}


});



backTop.style.opacity="0";

backTop.style.pointerEvents="none";


}







/* ================= HEADER EFFECT ================= */


const header =
document.querySelector("header");



window.addEventListener(
"scroll",
()=>{


if(window.scrollY > 50){


header.style.background =
"rgba(247,241,231,.95)";


header.style.backdropFilter =
"blur(15px)";


}else{


header.style.background =
"transparent";


header.style.backdropFilter =
"none";


}


});
