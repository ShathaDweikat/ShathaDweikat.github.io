/* =========================================================
   Shatha Dweikat — Website Interactions
========================================================= */


/* =========================
   Mobile Navigation
========================= */

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







/* =========================
   Scroll Reveal Animation
========================= */


const revealElements =
document.querySelectorAll(".reveal");



if (
    "IntersectionObserver" in window &&
    revealElements.length
){


    const observer =
    new IntersectionObserver(
        entries => {


            entries.forEach(entry => {


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
            threshold:0.15
        }
    );




    revealElements.forEach(element => {


        observer.observe(element);


    });



}else{


    revealElements.forEach(element => {


        element.classList.add(
            "in-view"
        );


    });


}







/* =========================
   Smooth Anchor Offset
   (for fixed header)
========================= */


document
.querySelectorAll('a[href^="#"]')
.forEach(anchor => {


    anchor.addEventListener(
        "click",
        function(e){


            const target =
            document.querySelector(
                this.getAttribute("href")
            );


            if(target){


                e.preventDefault();



                const headerHeight =
                document.querySelector("header")
                ?.offsetHeight || 0;



                const position =
                target.offsetTop - headerHeight;



                window.scrollTo({

                    top:position,

                    behavior:"smooth"

                });


            }


        }
    );


});







/* =========================
   Profile Floating Effect
========================= */


const profileImage =
document.querySelector(".profile-image");



if(profileImage){


    window.addEventListener(
        "mousemove",
        (e)=>{


            const x =
            (window.innerWidth / 2 - e.clientX)
            / 60;



            const y =
            (window.innerHeight / 2 - e.clientY)
            / 80;



            profileImage.style.transform =
            `
            translate(${x}px,${y}px)
            `;


        }
    );


}
