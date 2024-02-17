require('dotenv').config();
const express = require("express");
const cors = require("cors");
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const fs = require('fs');
const https = require("https");
const cookieParser = require('cookie-parser')


const app = express();

const PORT = 8002;
const sslServer = https.createServer({
    key: fs.readFileSync('cert/key.pem'),
    cert:fs.readFileSync('cert/certificate.pem')
}, app)
app.use(cors());
app.options('*', cors()) // include before other routes
app.use(cookieParser())
app.use(express());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.urlencoded({ extended: true }));
let users = require('./db/users');
let dados = require('./db/dados');

function escreve(fich, db) {
    fs.writeFile(fich, JSON.stringify(db, null, 4), 'utf8', err => {
        if (err) {
            console.log(`Error writing file: ${err}`)
        } else {
            console.log('Escreveu no ficheiro ' + fich); // Sucesso
        }
    })
}

function existeUser(nome) {
    for (utilizador of users)
        if (utilizador.username === nome) {
            return true;
        }
    return false;
}
//
// Registo de um novo utilizador
app.post("/registar", (req, res) => {
    const username = req.body.username;
    if (!existeUser(username)) {
        const newUser = {
            username: username,
            password: req.body.password,
            tipo: 0
        }
        if (newUser.password.length < 5) {
            return res.status(400).send({
                msg: 'Password deve ter 5 ou mais caracteres'
            });
        }
        users.push(newUser);
        escreve("./db/users.json", users);
        return res.status(201).send({
            msg: `Criado utilizador ${username}`
        });
    } else {
        return res.status(409).send({
            msg: 'Utilizador já existe'
        });
    }
});

// Login
app.post("/login", (req, res) => {
    const nome = req.body.username;
    const senha = req.body.password;
    for (utilizador of users) {
        if (utilizador.username === nome)
        if (utilizador.password === senha) {
        token = jwt.sign(utilizador, process.env.SECRET);
        res.cookie("token", token, {httpOnly: true, maxAge: 3600000, secure: true});// create a cookie with the token
        return res.status(201).json({
            auth: true,
})
}   else {
    return res.status(401).json({ msg: "Password inválida!" })
}
}
    return res.status(404).json({ msg: "Utilizador não encontrado!" })
});

function validarToken(token) {
    try {
        return jwt.verify(token, process.env.SECRET);
    } catch (err) {
        return false;
    }
}

// Acesso à informação somente se autorizado
app.get("/listarDados", (req, res) => {
    const decoded = validarToken(req.header('token'));
    if (!decoded) {
        return res.status(401).json({ msg: "Utilizador não autenticado ou não autorizado!" });
    }
    const nome = decoded.username;
    if (dados) {
        res.status(200).json(dados);
    } else {
        res.status(404).json({ msg: "Dados não encontrados!" });
    }
});


app.get("/logout", (req, res) => {
    res.clearCookie("token");
    return res.status(200).json({ auth: false });
});

app.delete('/remover/:id', (req, res) => {
    // get the id from the request
    const id = req.params.id;
    // read the json file
    const data = JSON.parse(fs.readFileSync('db/dados.json', 'utf8'));
    // find the index of the item in the array
    const index = data.findIndex(item => item.id === Number(id));
    // check
    if (index === -1) {
        res.status(404).json({ error: "Item not found" });
        return;
    }
    // remove the item from the array
    data.splice(index, 1);
    // write the updated data back to the json file
    fs.writeFileSync('db/dados.json', JSON.stringify(data));
    // send a response to the client
    res.status(200).json({ msg: "Item removed successfully" });
});

app.get("/checkAuth", (req, res) => {
    const token = req.cookies.token;
    if (!token) {
        return res.status(200).json({ auth: false });
    }
    try {
        const decoded = jwt.verify(token, process.env.SECRET);
        return res.status(200).json({ auth: true });
    } catch (err) {
        return res.status(200).json({ auth: false });
    }
});

app.use(express.static('public'));
sslServer.listen(8002, () => {
    console.log('Server listening on port 8002');
});

app.use((req, res, next) => {
    req.secure ? next() : res.redirect('https://' + req.headers.host + req.url)
})

async function getPublicAPI() {
    const axios = require("axios");
    let result = [];

    const options = {
        method: 'GET',
        url: 'https://bloomberg-market-and-financial-news.p.rapidapi.com/stories/detail',
        params: {internalID: 'QFY0Y6T0AFB501'},
        headers: {
          'X-RapidAPI-Key': '61b5165e89msh8b57b6f78a81529p1d4212jsn9398f7c2cd49',
          'X-RapidAPI-Host': 'bloomberg-market-and-financial-news.p.rapidapi.com'
        }
    };

    await axios.request(options).then(function (response) {
        //console.log(response.data);
        result = response;
    }).catch(function (error) {
        console.error(error);
    })
    return result;
}
// Acesso à API pública sem autenticação
app.get("/APIpublica", (req, res) => {
    getPublicAPI().then(function (dados) {
        console.log(dados.data);
        if (dados) {
            res.status(200).json(dados.data);
        } else {
            res.status(404).json({ msg: "Dados não encontrados!" });
        }
    })
});
app.get("/items", (req, res) => {
    // read the json file
    const data = JSON.parse(fs.readFileSync('db/dados.json', 'utf8'));
    // send the data as a response to the client
    res.status(200).json(data);
});

function findNextId(data) {
    nextId = Math.max(...data.map(item => item.id), 0);
    return ++nextId;
}

app.post('/inserir', async (req, res) => {
    try {
        let data = JSON.parse(await fs.promises.readFile('db/dados.json'))
        const newItem = req.body;
        newItem.id = findNextId(data);
        data.push(newItem);
        await fs.promises.writeFile('db/dados.json', JSON.stringify(data));
        res.status(201).json(newItem);
    } catch(err) {
        console.error(err);
        res.status(500).send(err);
        }
        });

   