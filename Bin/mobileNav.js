const btnmob = document.getElementsByClassName("btn")
const nav = document.querySelector("nav");
const aza = document.querySelector('ul')

btnmob.addEventListenr('click', () => {
    aza.style.display = "block";
}) 

const green = document.querySelector('h2');

green.style.color = "green";
