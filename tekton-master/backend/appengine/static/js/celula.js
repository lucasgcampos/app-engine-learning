/**
 * Created by lucas on 28/10/14.
 */
$(document).ready(function() {

    // Oculta
    var $celulaForm = $('#celula-form');
    $celulaForm.hide();


    // Mostra e esconde o form
    $('#mostrar-form-btn').click(function () {
       $celulaForm.slideToggle();
    });

    // Input
    var $nomeInput = $('#nomeInput');
    var $areaInput = $('#areaInput');
    var $enderecoInput = $('#enderecoInput');

    // Mensagem de erro
    var $helpNomeSpan = $('#help-nome');
    var $helpAreaSpan = $('#help-area');
    var $helpEnderecoSpan = $('#help-endereco');

    // Fundo de erro
    var $nomeDiv = $('#nomeDiv');
    var $areaDiv = $('#areaDiv');
    var $enderecoDiv = $('#enderecoDiv');

    var $ajaxGif = $('#ajax-gif');
    $ajaxGif.hide();
    var $salvarBtn = $('#salvar-btn');


    $.get('/celulas/rest').success(function (celulas) {
        for (var i = 0; i < celulas.length; i += 1) {
            adicionarLinha(celulas[i]);
        }
    });



    $salvarBtn.click(function() {
        var celula = {
            nome : $nomeInput.val(),
            area : $areaInput.val(),
            endereco : $enderecoInput.val()
        };

        $ajaxGif.slideDown();
        $salvarBtn.hide();

        var promessa = $.post('/celulas/rest/save', celula);

        promessa.success(function(celula_do_servidor) {
            $nomeInput.val("");
            $helpNomeSpan.text("");
            $nomeDiv.removeClass('has-error');

            $areaInput.val("");
            $helpAreaSpan.text("");
            $areaDiv.removeClass('has-error');

            $enderecoInput.val("");
            $helpEnderecoSpan.text("");
            $enderecoDiv.removeClass('has-error');

            $celulaForm.fadeOut();
            adicionarLinha(celula_do_servidor);
        });


        promessa.error(function(erros) {
            console.log(erros);
            if(erros.responseJSON != null && erros.responseJSON.nome != null) {
                $nomeDiv.addClass('has-error');
                $helpNomeSpan.text(erros.responseJSON.nome);
            } else {
                $nomeDiv.removeClass('has-error');
                $helpNomeSpan.text("");
            }

            if(erros.responseJSON != null && erros.responseJSON.area != null) {
                $areaDiv.addClass('has-error');
                $helpAreaSpan.text(erros.responseJSON.area);
            } else {
                $areaDiv.removeClass('has-error');
                $helpAreaSpan.text("");
            }

            if(erros.responseJSON != null && erros.responseJSON.endereco != null) {
                $enderecoDiv.addClass('has-error');
                $helpEnderecoSpan.text(erros.responseJSON.endereco);
            } else {
                $enderecoDiv.removeClass('has-error');
                $helpEnderecoSpan.text("");
            }
        });

        promessa.always(function () {
           $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        });
    });

    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha = function(celula) {
        var linha = '<tr id="row' + celula.id + '">' +
            '<td>' + celula.nome + '</td>' +
            '<td>' + celula.area + '</td>' +
            '<td>' + celula.endereco + '</td>' +
            '<td><button id="ex' + celula.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button><td>' +
            '</tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#row' + celula.id);
+
+        $linhaHtml.hide();
+        $linhaHtml.fadeIn();

        $('#ex' + celula.id).click(function () {
            $linhaHtml.fadeOut();
            $.post('/celulas/rest/delete', {'celula_id': celula.id}).success(function () {
                $linhaHtml.remove();
            }).error(function () {
                alert('Ocorreu um problema ao tentar excluir este registro, atualize a página e tente novamente.');
                $linhaHtml.fadeIn();
            });
        });


    }


});