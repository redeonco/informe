function process_response(formularios){
    form_select = document.getElementById('tabela');
    form_select.innerHTML = '';
    getUrl = window.location.host + "/media/"

    formularios.forEach(function(formularios){
        var tr = document.createElement("tr");
        tr.setAttribute('class','linha_coluna');
        tr.setAttribute('onclick',"window.location='http://" + getUrl + formularios.fields.arquivo + "'");
        var th = document.createElement("th");
        th.setAttribute('scope','row')
        var a = document.createElement("a");
        a.setAttribute('href',"http://" + getUrl + formularios.fields.arquivo)
        a.setAttribute('class','link')
        a.innerHTML = formularios.fields.nome
        var td1 = document.createElement("td");
        td1.innerHTML = formularios.fields.descricao
        var td2 = document.createElement("td");
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
        var data = new Date(formularios.fields.data_publicacao).toLocaleString('pt-br', options);
        td2.innerHTML = data

        form_select.appendChild(tr);
        tr.appendChild(th);
        th.appendChild(a)
        tr.appendChild(td1);
        tr.appendChild(td2);
    });
}

function filtraFormularios(id){
    depart_id = document.getElementById("departamentos").value;
    $.ajax({
        type: 'GET',
        url: '/filtra_formularios/',
        data: {
            outro_param: depart_id
        },
        success: function(result){
            process_response(result);
            $("#mensagem").text("Formulários carregados");
        }
    });
}

function process_response2(pops){
    pop_select = document.getElementById('tabela');
    pop_select.innerHTML = '';
    getUrl = window.location.host + "/media/"

    pops.forEach(function(pops){
        var tr = document.createElement("tr");
        tr.setAttribute('class','linha_coluna');
        tr.setAttribute('onclick',"window.location='http://" + getUrl + pops.fields.arquivo + "'");
        var th = document.createElement("th");
        th.setAttribute('scope','row')
        var a = document.createElement("a");
        a.setAttribute('href',"http://" + getUrl + pops.fields.arquivo)
        a.setAttribute('class','link')
        a.innerHTML = pops.fields.nome
        var td1 = document.createElement("td");
        td1.innerHTML = pops.fields.descricao
        var td2 = document.createElement("td");
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
        var data = new Date(pops.fields.data_publicacao).toLocaleString('pt-br', options);
        td2.innerHTML = data

        pop_select.appendChild(tr);
        tr.appendChild(th);
        th.appendChild(a)
        tr.appendChild(td1);
        tr.appendChild(td2);
    });
}

function filtraPop(id){
    depart_id = document.getElementById("departamentos").value;
    $.ajax({
        type: 'GET',
        url: '/filtra_pop/',
        data: {
            outro_param: depart_id
        },
        success: function(result){
            console.log(depart_id)
            process_response2(result);
            $("#mensagem").text("POPs carregados");
        }
    });
}


function process_response3(alvaras){
    alvaras_select = document.getElementById('tabela');
    alvaras_select.innerHTML = '';
    getUrl = window.location.host + "/media/"
    console.log(getUrl)

    alvaras.forEach(function(alvaras){
        var tr = document.createElement("tr");
        tr.setAttribute('class','linha_coluna');
        tr.setAttribute('onclick',"window.location='http://" + getUrl + alvaras.fields.arquivo + "'");
        var th = document.createElement("th");
        th.setAttribute('scope','row')
        var a = document.createElement("a");
        a.setAttribute('href', "http://" + getUrl + alvaras.fields.arquivo)
        a.setAttribute('class','link')
        a.innerHTML = alvaras.fields.nome
        var td1 = document.createElement("td");
        td1.innerHTML = alvaras.fields.descricao
        var td2 = document.createElement("td");
        var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
        var data_vigencia = new Date(alvaras.fields.data_vigencia).toLocaleString('pt-br', options);
        console.log(alvaras.fields.data_vigencia)
        td2.innerHTML = data_vigencia
        var td3 = document.createElement("td");
        var data_publicacao = new Date(alvaras.fields.data_publicacao).toLocaleString('pt-br', options);
        console.log(alvaras.fields.data_publicacao)
        td3.innerHTML = data_publicacao

        alvaras_select.appendChild(tr);
        tr.appendChild(th);
        th.appendChild(a)
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td3);
    });
}

function filtraFilial(id){
    filial_id = document.getElementById("filial").value;
    $.ajax({
        type: 'GET',
        url: '/filtra_filial/',
        data: {
            outro_param: filial_id
        },
        success: function(result){
            console.log(filial_id)
            process_response3(result);
            $("#mensagem").text("POPs carregados");
        }
    });
}