const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});


//....................
document.addEventListener('DOMContentLoaded', function () {
    var flashMessages = document.getElementById('flash-messages');
    if (flashMessages) {
        flashMessages.addEventListener('animationend', function () {
            flashMessages.style.display = 'none';
        });

        setTimeout(function () {
            flashMessages.classList.add('hide');
        }, 5000);
    }
});