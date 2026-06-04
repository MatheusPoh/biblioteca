const API_URL = "";

function carregarLivros() {
    fetch(`/livros`) //${API_URL}
        .then(res => res.json())
        .then(livros => {

            const lista = document.getElementById("lista");
            lista.innerHTML = "";

            livros.forEach(livro => {
                const li = document.createElement("li");
                let status = livro.disponivel ? "Disponível" : "Alugado";

                const texto = document.createElement("span");
                texto.innerText = `${livro.nome} - ${livro.autor} (${status})`;

                const btnAcao = document.createElement("button");

                if (livro.disponivel) {
                    btnAcao.innerText = "Alugar"; //BTN alugar e devolvel livro
                    btnAcao.onclick = () => alugarLivro(livro.id);
                } else {
                    btnAcao.innerText = "Devolver";
                    btnAcao.onclick = () => devolverLivro(livro.id);
                    texto.style.color = "red";
                }

                const btnDelete = document.createElement("button"); 
                btnDelete.innerText = "Deletar"; //BTN deletar livro
                btnDelete.onclick = function () {
                    deletarLivro(livro.id);
                };

                if (!livro.disponivel) { // Se estiver alugado = cor vermelha
                    texto.style.color = "red";
                }

                li.appendChild(texto);
                li.appendChild(btnAcao);
                li.appendChild(btnDelete);
                lista.appendChild(li);
            });
        })
        .catch(error => {
            console.error("Erro ao carregar livros:", error);
        });
}
document.addEventListener("DOMContentLoaded", function () {
    carregarLivros();
});

function cadastrarLivro() {
    const nome = document.getElementById("nomeCadastrar").value;
    const autor = document.getElementById("autorCadastrar").value;

    if (!nome || !autor) {
        alert("Preencha todos os campos!");
        return;
    }

    fetch(`/livros`, { //Envia para API
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ //Converte para JSON
            nome: nome,
            autor: autor
        })
    })

    .then(res => {
        if (!res.ok) {
            return res.json().then(err => { throw err; }); //trata erro 400, 404...
        }
        return res.json();
    })
    .then(data => {
        alert(data.mensagem);

        document.getElementById("nomeCadastrar").value = ""; //Limpa os campos 
        document.getElementById("autorCadastrar").value = "";

        carregarLivros();
    })

    .catch(err => {
        alert(err.erro || "Erro ao cadastrar livro");
    });
}

function deletarLivro(id) {
    
    fetch(`/livros/deletar`, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ id })
    })
    
    .then(res => res.json())
    .then(data => {
        alert(data.mensagem || data.erro); 
        carregarLivros(); 
    })
    .catch(err => {
        console.error(err);
    });
}


function alugarLivro(id) {
    fetch(`/livros/alugar`, {
        method: "PUT",
        headers : {
            "content-Type": "application/json"
        },
        body: JSON.stringify({ id })
    })


    .then(res => res.json())
    .then(data => {
        alert(data.mensagem || data.erro);
        carregarLivros();
    });
}
function devolverLivro(id) {
    fetch(`/livros/devolver`, {
        method: "PUT",
        headers: {
            "content-Type": "application/json"
        },
        body: JSON.stringify({ id })
    })


    .then(res => res.json())
    .then(data => {
        alert(data.mensagem || data.erro);
        carregarLivros();
    });
}