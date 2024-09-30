function changeUsernameHeader(){
    var username;
    var loginUsername;
    var search;

    search = new URLSearchParams(window.location.search)

    loginUsername = search.get('login');
    console.log(loginUsername);
    // username = loginUsername.toString;
    document.getElementById("usernameHeader").innerText = "Olá, " + loginUsername + "!";
}

function resetEditPerfilForm(){
    document.getElementById("editPerfilForm").reset();
}

function resetSenhaForm(){
    document.getElementById("redefinirSenha").reset();
}

function toggleFilterDropdown(){
    var element = document.getElementById("dropdownFilter");
    var hidden = element.getAttribute("hidden");

    console.log("whats wrong?");

    if (hidden) {
       element.removeAttribute("hidden");
    } else {
       element.setAttribute("hidden", "hidden");
    }
}

function cadastroNovoProjeto(){
    //redireciona pra listaProjeto e abre o popup da IA com link pra pag da IA
    console.log("oi");
    nameProjeto = document.getElementById("nome-projeto").value;
    dataContrato = document.getElementById("data-final").value;
    console.log(nameProjeto);
    console.log(dataContrato);

    if(nameProjeto !== "" && dataContrato !== ""){
        console.log("diff");
        window.location.href = '/listaProjetos.html';
    }

}

function hidePopupIA(){
    const popover = document.getElementById("popupIA");
    const hideBtn = document.getElementById("hideBtn");


    popover.popover = "manual";

    hideBtn.popoverTargetElement = popover;
    hideBtn.popoverTargetAction = "hide";

    console.log("ue");
}

