const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const container_signup = document.querySelector(".container-signup");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
  setTimeout(function(){location.replace('/accounts/signup/')}, 1700);
});

sign_in_btn.addEventListener("click", () => {
  container_signup.classList.add("sign-up-mode");
});