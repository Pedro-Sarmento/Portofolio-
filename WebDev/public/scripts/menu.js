function clearPage() {
    // Função para limpar página
}

function loadHome(){
    document.getElementById("divListar").innerHTML = "";
    const welcome = document.getElementsByClassName('welcome')[0];
    const cards = document.getElementsByClassName('cards')[0];
    const about = document.getElementsByClassName('about')[0];
    const reviews = document.getElementsByClassName('reviews')[0];
    welcome.style.visibility = "visible";
    cards.style.visibility = "visible"; 
    about.style.display = "none"; 
    reviews.style.display = "none";  

}

function loadProducts() {
    const welcome = document.getElementsByClassName('welcome')[0];
    const cards = document.getElementsByClassName('cards')[0];
    const about = document.getElementsByClassName('about')[0];
    const reviews = document.getElementsByClassName('reviews')[0];
    welcome.style.visibility = "hidden";
    cards.style.visibility = "hidden"; 
    about.style.display = "none"; 
    reviews.style.display = "none";  
}

function loadAbout() {
    document.getElementById("divListar").innerHTML = "";
    const welcome = document.getElementsByClassName('welcome')[0];
    const cards = document.getElementsByClassName('cards')[0];
    const about = document.getElementsByClassName('about')[0];
    const reviews = document.getElementsByClassName('reviews')[0];
    welcome.style.visibility = "visible";
    cards.style.visibility = "hidden"; 
    about.style.display = "inline";    
    reviews.style.display = "none";  
}

function loadReviews() {
    document.getElementById("divListar").innerHTML = "";
    const welcome = document.getElementsByClassName('welcome')[0];
    const cards = document.getElementsByClassName('cards')[0];
    const about = document.getElementsByClassName('about')[0];
    const reviews = document.getElementsByClassName('reviews')[0];
    welcome.style.visibility = "visible";
    cards.style.visibility = "hidden"; 
    about.style.display = "none"; 
    reviews.style.display = "inline"; 
}

function loadAPI() {
    document.getElementById("divListar").innerHTML = "";
    const welcome = document.getElementsByClassName('welcome')[0];
    const cards = document.getElementsByClassName('cards')[0];
    const about = document.getElementsByClassName('about')[0];
    const reviews = document.getElementsByClassName('reviews')[0];
    welcome.style.visibility = "hidden";
    cards.style.visibility = "hidden"; 
    about.style.display = "none"; 
    reviews.style.display = "none"; 
}
    



