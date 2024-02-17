
// const { urlencoded } = require("body-parser");
let itemIndex = 0;
async function loginEnviar() {
    document.getElementById("divLogin").style.display = "block";
    document.getElementById("legenda").innerText = "Login";
    document.getElementById("btnLogin").style.display = "inline";
    document.getElementById("btnRegistar").style.display = "none";
    const nome = document.getElementById("username").value;
    const senha = document.getElementById("password").value;
    const user = {
        username: nome,
        password: senha,
    };
    const resposta = await makeRequest("https://localhost:8002/login", {
        method: "POST",
        body: JSON.stringify(user),
        headers: { "Content-type": "application/json; charset=UTF-8" },
    });
    json = await resposta.json();
    switch (resposta.status) {
        case 201:
            {
                // login ok
                document.getElementById("divLogin").style.display = "none";
                document.getElementById("divListar").style.display = "block";
                document.getElementById("btnListar").style.display = "none";
                document.getElementById("pMsg").innerHTML = "";
                document.getElementById("login").style.display = "none";
                document.getElementById("logout").style.display = "inline";
                document.getElementById("btnLogin").style.display = "inline";
                document.getElementById("btnRegistar").style.display = "none";
                document.getElementById("registar").style.display = "none";
                document.getElementById("API").style.display = "inline";
                document.getElementById("cart-button").style.display = "inline";

                if (user.username == "admin" && user.password == "admin") {
                    document.getElementById("remover").style.display = "inline";
                    document.getElementById("inserir").style.display = "inline";
                }
                
                document.getElementById("legenda").innerText = "Autenticar";
                localStorage.setItem("token", json.token);
                break;
            }
        case 401:
            {
                // Password errada
                document.getElementById("pMsg").innerHTML = json.msg;
                break;
            }
        case 404:
            {
                // Utilizador não encontrado
                console.log(json.msg);
                document.getElementById("pMsg").innerHTML = json.msg;
                break;
            }
    }
}

async function logout() {
    const response = await fetch("/logout", {
        method: "GET",
        credentials: "include"
    });
    const data = await response.json();
    if (data.auth === false) {
    document.getElementById("logout").style.display = "none";
    document.getElementById("login").style.display = "inline";
    document.getElementById("btnListar").style.display = "none";
    document.getElementById("registar").style.display = "inline";
    document.getElementById("remover").style.display = "none";
    document.getElementById("inserir").style.display = "none";
    document.getElementById("divListar").innerHTML = "";
    document.getElementById("pMsg").innerHTML = "";
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    document.getElementById("API").style.display = "none";
    document.getElementById("cart-button").style.display = "none";
    localStorage.removeItem("token");  
    }
    
}

function login() {
    document.getElementById("divLogin").style.display = "block";
    document.getElementById("legenda").innerText = "Login";
    document.getElementById("btnLogin").style.display = "inline";
    document.getElementById("btnRegistar").style.display = "none";
}

function registar() {
    document.getElementById("divLogin").style.display = "block";
    document.getElementById("legenda").innerText = "Registar";
    document.getElementById("btnLogin").style.display = "none";
    document.getElementById("btnRegistar").style.display = "inline";
}


async function registarEnviar() {
    const nome = document.getElementById("username").value;
    const senha = document.getElementById("password").value;
    const user = {
        username: nome,
        password: senha,
    };
    const resposta = await makeRequest("https://localhost:8002/registar", {
        method: "POST",
        body: JSON.stringify(user),
        headers: { "Content-type": "application/json; charset=UTF-8" },
    });
    json = await resposta.json();
    switch (resposta.status) {
        case 409:
            {
                // Utilizador já existe
                document.getElementById("pMsg").innerHTML = json.msg;
                break;
            }
        case 400:
            {
                // Password inaceitável
                document.getElementById("pMsg").innerHTML = json.msg;
                break;
            }
        case 201:
            {
                // Utilizador registado
                document.getElementById("pMsg").innerHTML = json.msg;
                break;
            }
    }
}

async function listar() {
    document.getElementById("divListar").innerHTML = "";
    const resposta = await makeRequest("https://localhost:8002/items", {
        method: "GET",
        headers: {
            token: localStorage.getItem("token"),
            "Content-type": "application/json; charset=UTF-8",
        },
    });

    dados = await resposta.json();
    switch (resposta.status) {
        case 200:
            {
            const tableCSS = document.createElement("table");
            tableCSS.classList.add("my-table");
            
            if (document.getElementsByClassName("my-table").length == 0) {
                // create table element
                const table = document.createElement("table");
                table.classList.add('my-table'); //  if you want to set a class to the table
                // create name row
                const nameRow = table.insertRow();
                // create image row
                const imgRow = table.insertRow();

                const pricerow = table.insertRow()
    
                // Iterate through the data
                if (dados.length <= 8){
                    for (let i = 0; i < dados.length; i++) {
                        //create the name cell
                        const nameCell = nameRow.insertCell();
                        nameCell.innerHTML = dados[i].nome;
                        
                        //create the image cell
                        const imgCell = imgRow.insertCell();
                        const imgContainer = document.createElement("div");
                        
                        const img = document.createElement("img");
                        img.src = dados[i].url;
                        img.style.width = '200px';
                        imgContainer.appendChild(img);
                        imgContainer.style.display = "block";
                        
                        //price cell
                        const pricecell = pricerow.insertCell()
                        pricecell.innerHTML = dados[i].preco + "€";
                        //create the new button
                        const newButton = document.createElement("button");
                        newButton.innerHTML = "Comprar";
                        newButton.classList.add("my-new-button-class");
                        newButton.setAttribute("id", dados[i].id);
                        imgContainer.appendChild(newButton);
                        newButton.onclick = () => addToCart({name: dados[i].nome, quantity: 1, price: Number(dados[i].preco)});
                        imgCell.appendChild(imgContainer);
                    }
                } else {
                    const nameRow2= table.insertRow();
                    // create image row
                    const imgRow2 = table.insertRow();
                    const pricerow2 = table.insertRow();

                    for (let i = 0; i < 9; i++) {
                        //create the name cell
                        const nameCell = nameRow.insertCell();
                        nameCell.innerHTML = dados[i].nome;
                        
                        //create the image cell
                        const imgCell = imgRow.insertCell();
                        const imgContainer = document.createElement("div");
                        
                        const img = document.createElement("img");
                        img.src = dados[i].url;
                        img.style.width = '200px';
                        imgContainer.appendChild(img);
                        imgContainer.style.display = "block";
                        
                        //price cell
                        const pricecell = pricerow.insertCell()
                        pricecell.innerHTML = dados[i].preco + "€";

                        //create the new button
                        const newButton = document.createElement("button");
                        newButton.innerHTML = "Comprar";
                        newButton.classList.add("my-new-button-class");
                        newButton.setAttribute("id", dados[i].id);
                        imgContainer.appendChild(newButton);
                        newButton.onclick = () => addToCart({name: dados[i].nome, quantity: 1, price: Number(dados[i].preco)});
                        imgCell.appendChild(imgContainer);
                    }
                    
                    for (let i = 9; i < dados.length; i++) {
                        
                        //create the name cell
                        const nameCell = nameRow2.insertCell();
                        nameCell.innerHTML = dados[i].nome;
                        
                        //create the image cell
                        const imgCell = imgRow2.insertCell();
                        const imgContainer = document.createElement("div");
                        
                        const img = document.createElement("img");
                        img.src = dados[i].url;
                        img.style.width = '200px';
                        imgContainer.appendChild(img);
                        imgContainer.style.display = "block";
                        
                        //price cell
                        const pricecell2 = pricerow2.insertCell();
                        pricecell2.innerHTML = dados[i].preco + "€";

                        //create the new button
                        const newButton = document.createElement("button");
                        newButton.innerHTML = "Comprar";
                        newButton.classList.add("my-new-button-class");
                        newButton.setAttribute("id", dados[i].id);
                        imgContainer.appendChild(newButton);
                        newButton.onclick = () => addToCart({name: dados[i].nome, quantity: 1, price: Number(dados[i].preco)});
                        imgCell.appendChild(imgContainer);
                    }
                }
                // append the table to the div
                document.getElementById("divListar").appendChild(table);
                //add a box around the table
                document.getElementById("divListar").style.border = "1px solid gray";
                document.getElementById("pMsg").innerHTML = "";
                break;
                }
            }
        case 401:
            {
                // Utilizador não autenticado ou não autorizado
                document.getElementById("pMsg").innerHTML = dados.msg;
                break;
            }
        case 404:
            {
                // Dados não encontrados
                document.getElementById("pMsg").innerHTML = dados.msg;
                break;
            }
    }
}

function addToCart(item) {
    // Get the cart items tbody
    var cartItems = document.getElementById("cart-items");
  
    // Create a new row for the item
    var row = cartItems.insertRow();
  
    // Insert the item name into the first cell
    var nameCell = row.insertCell(0);
    nameCell.innerHTML = item.name;
  
    // Insert the item quantity into the second cell
    var quantityCell = row.insertCell(1);
    quantityCell.innerHTML = item.quantity;
  
    // Insert the item price into the third cell
    var priceCell = row.insertCell(2);
    priceCell.innerHTML = item.price;
  
    //create the remove button
    var buttonCell = row.insertCell(3);
    var removeButton = document.createElement("button");
    removeButton.innerHTML = "Remove";
    removeButton.setAttribute("data-index", itemIndex);
    removeButton.addEventListener("click", removeFromCart);
    buttonCell.appendChild(removeButton);
    itemIndex += 1;
    // Update the total price
    updateTotal();
    var expires = "";
    var date = new Date();
    date.setTime(date.getTime() + (30*24*60*60*1000));
    expires = "; expires=" + date.toUTCString();
    if(document.cookie==""){
        document.cookie ="Name = "+ item.name +";"+ expires + "; path=/"
    }else{
        document.cookie +="\/"+item.name+"";
    }
}

async function cookietest(){
    var cart = document.cookie.split(';')[0].split("=")[1].split("/");
    clearCookies();
    const response = await makeRequest('https://localhost:8002/items/', {
            method: "GET",
            headers: { "Content-type": "application/json; charset=UTF-8" },
        })
    json= await response.json()
    await cart.forEach( async name => { 
        
        json.forEach(item =>{
        if(name == item["nome"]){
            name = item["nome"]
            price = item["preco"]
            quantity = 1
            addToCart({name: name, quantity:quantity, price:Number(price)})
            }
        })
    });
}
function clearCookies(){
    var allCookies = document.cookie.split(';');
    for (var i = 0; i < allCookies.length; i++)
        document.cookie = allCookies[i] + "=;expires="
        + new Date(0).toUTCString();
    document.getElementById("cart-items").innerHTML = "";
    
}
// Remove an item from the cart
function removeFromCart(event) {
    // Get the cart items tbody
    var cartItems = document.getElementById("cart-items");
    let index = event.target.getAttribute("data-index");
    // check if index is valid before removing
    console.log(index)
    console.log(cartItems.rows.length)
    if (index <= cartItems.rows.length) {
        // Remove the row at the specified index
        cartItems.deleteRow(index);
        // Update the item index
        for (var i = 0; i < cartItems.rows.length; i++) {
            cartItems.rows[i].cells[3].setAttribute("data-index", i);
        }
        // Update the total price
        updateTotal();
        itemIndex -=1;
    }
}

// Update the total price
function updateTotal() {
    // Get the cart items tbody
    var cartItems = document.getElementById("cart-items");
  
    // Initialize the total price
    var total = 0;
  
    // Iterate through the cart items
    for (var i = 0; i < cartItems.rows.length; i++) {
        // Get theitem quantity and price
        var quantity = parseFloat(cartItems.rows[i].cells[1].innerHTML);
        var price = parseFloat(cartItems.rows[i].cells[2].innerHTML);
    
        // Add the item price to the total
        total += quantity * price;
      }
  
    // Get the total price div
    var totalPrice = document.getElementById("cart-total");
  
    // Set the total price
    totalPrice.innerHTML = "Total: €" + total;
}


function ShowCart(){
    var cartButton = document.getElementById("cart-button");

// Get the cart sidebar
var cartSidebar = document.getElementById("cart");

// Add a click event listener to the cart button
cartButton.addEventListener("click", function() {
  // toggle the "open" class on the cart sidebar
  cartSidebar.classList.toggle("open");
});
}

async function remover() {
    let id = prompt("ID?");
    // Pass the id as a parameter
    const resposta = await makeRequest(`https://localhost:8002/remover/${id}`, {
        method: "DELETE",
        headers: {
            token: localStorage.getItem("token"),
            "Content-type": "application/json; charset=UTF-8",
        },
    });
    json = await resposta.json();
    if (resposta.status === 200) {
        console.log(json.msg);
    } else {
        console.log(json.error);
    }
    listar();
}

async function insert() {
    let name = prompt("Nome do item a inserir?")
    let url = prompt("Url da imagem a utilizar?")
    let price = prompt("Preço do Item que quer adicionar?")
    const resposta = await makeRequest(`https://localhost:8002/inserir`, {
        method: "POST",
        headers: { "Content-type": "application/json; charset=UTF-8" },
        body: JSON.stringify({ nome: name, url: url, preco: price}),
    });
    const data = await resposta.json();
    if (resposta.status === 201) {
        console.log(`New item added with ID: ${data.id}`);
        listar();
    } else {
        console.log(data.error);
    }
}

async function API() {
    const resposta = await makeRequest("https://localhost:8002/APIpublica", {
        method: "GET",
        headers: {
            // token: localStorage.getItem("token"),
            "Content-type": "application/json; charset=UTF-8",
        },
    });
    dados = await resposta.json();
    console.log(dados)
    switch (resposta.status) {
        case 200:
            {
                // obteve os dados
                let lista = "";
                lista += '<h2>' + dados.title + '</h2>';
                lista += '<h3>' + 'ContentTags' + '</h3>';
                for (dado of dados.contentTags) {
                    lista += "dados ->" + JSON.stringify(dado.id) + "<br>" + "type-> "+ JSON.stringify(dado.type) + "<br><hr>";
                }
                document.getElementById("divListar").innerHTML = lista;
                document.getElementById("pMsg").innerHTML = "";
                break;
            }
        case 401:
            {
                // Utilizador não autenticado ou não autorizado
                document.getElementById("pMsg").innerHTML = dados.msg;
                break;
            }
        case 404:
            {
                // Dados não encontrados
                document.getElementById("pMsg").innerHTML = dados.msg;
                break;
            }
    }
}

async function makeRequest(url, options) {
    try {
        const response = await fetch(url, options);
        return response;
    } catch (err) {
        console.log(err);
    }
}