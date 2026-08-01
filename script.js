// =========================================================
// Shatha Dweikat — Personal Research Platform
// Main JavaScript
// =========================================================



/* =========================
   Mobile Navigation
========================= */


const navToggle = document.getElementById("navToggle");
const navLinks = document.getElementById("navLinks");


function closeMenu(){

    if(!navLinks || !navToggle) return;

    navLinks.classList.remove("open");

    navToggle.setAttribute(
        "aria-expanded",
        "false"
    );

}



if(navToggle && navLinks){


    navToggle.addEventListener("click", () => {


        const isOpen =
        navLinks.classList.toggle("open");


        navToggle.setAttribute(
            "aria-expanded",
            isOpen
        );


    });




    // Close after clicking a link

    navLinks
    .querySelectorAll("a")
    .forEach(link => {


        link.addEventListener(
            "click",
            closeMenu
        );


    });




    // Close when clicking outside


    document.addEventListener(
        "click",
        (event)=>{


            const clickedInside =
            navLinks.contains(event.target)
            ||
            navToggle.contains(event.target);



            if(!clickedInside){

                closeMenu();

            }


        }

    );




    // Escape key closes menu


    document.addEventListener(
        "keydown",
        (event)=>{


            if(event.key === "Escape"){

                closeMenu();

            }


        }

    );


}





/* =========================
   Scroll Reveal Animation
========================= */


const revealElements =
document.querySelectorAll(".reveal");



if(
    "IntersectionObserver" in window
    &&
    revealElements.length
){


    const revealObserver =
    new IntersectionObserver(
        (entries)=>{


            entries.forEach(
                (entry)=>{


                    if(entry.isIntersecting){



                        entry.target.classList.add(
                            "in-view"
                        );



                        revealObserver.unobserve(
                            entry.target
                        );


                    }



                }
            );


        },
        {
            threshold:.15
        }
    );



    revealElements.forEach(
        (element)=>{


            revealObserver.observe(element);


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







/* =========================
   Smooth Navigation Offset
   for fixed Header
========================= */


document
.querySelectorAll('a[href^="#"]')
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



                const headerHeight =
                document.querySelector("header")
                ?.offsetHeight || 0;



                const position =
                target.offsetTop -
                headerHeight;



                window.scrollTo({

                    top:position,

                    behavior:"smooth"

                });


            }


        }

    );


});
