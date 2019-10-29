$(function ($) {
    $('#id_dt_nasc').mask("99/99/9999");
    $('#id_email').addClass('form-control');
    //$('#id_old_password').addClass('form-control');
    //$('#id_new_password1').addClass('form-control');
    //$('#id_new_password2').addClass('form-control');
    if ($("form").length){
        $("form").submit(function(){
            $("#btn_confirma").attr("disabled", "disabled").html("Enviando...");
        })
    }
}); // end ready