/* =========================================================
   Shatha Dweikat Website
   Main JavaScript
========================================================= */


/* ================= MOBILE NAVIGATION ================= */


const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");


if (navToggle && navLinks) {


    navToggle.addEventListener("click", () => {


        const opened = navLinks.classList.toggle("open");


        navToggle.setAttribute(
            "aria-expanded",
            opened
        );


    });



    navLinks.querySelectorAll("a").forEach(link => {


        link.addEventListener("click", () => {


            navLinks.classList.remove("open");


            navToggle.setAttribute(
                "aria-expanded",
                "false"
            );


        });


    });


}







/* ================= SCROLL REVEAL ================= */


const revealElements =
document.querySelectorAll(".reveal");



if (
    "IntersectionObserver" in window &&
    revealElements.length
){


    const revealObserver =
    new IntersectionObserver(
        entries => {


            entries.forEach(entry => {


                if(entry.isIntersecting){


                    entry.target.classList.add(
                        "in-view"
                    );


                    revealObserver.unobserve(
                        entry.target
                    );


                }


            });


        },
        {
            threshold:.15
        }
    );



    revealElements.forEach(element => {


        revealObserver.observe(element);


    });



}else{


    revealElements.forEach(element=>{


        element.classList.add(
            "in-view"
        );


    });


}







/* ================= CLOSE MENU WHEN CLICK OUTSIDE ================= */


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


        }
    );


});








/* ================= HEADER EFFECT ================= */


const header =
document.querySelector("header");



window.addEventListener(
"scroll",
()=>{


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
