function process_response(formularios){
    form_select = document.getElementById('tabela');
    form_select.innerHTML = '';

    formularios.forEach(function(formularios){
        var tr = document.createElement("tr");
        tr.setAttribute('class','linha_coluna');
        tr.setAttribute('onclick',"window.location='http://127.0.0.1:8000/media/" + formularios.fields.arquivo + "'");
        var th = document.createElement("th");
        th.setAttribute('scope','row')
        var a = document.createElement("a");
        a.setAttribute('href',"http://127.0.0.1:8000/media/" + formularios.fields.arquivo)
        a.setAttribute('class','link')
        a.innerHTML = formularios.fields.nome
        var td1 = document.createElement("td");
        td1.innerHTML = formularios.fields.descricao
        var td2 = document.createElement("td");
        var data = formularios.fields.data_publicacao
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
            console.log(depart_id)
            process_response(result);
            $("#mensagem").text("Formulários carregados");
        }
    });
}