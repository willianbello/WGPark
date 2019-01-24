
$(document).ready(function() {

    var link = $('#linkHistorico');
    var subir = $('#botaoSubir');

    $(link).click(function() {

        var seletor = $(this).attr("href");
        console.log(seletor);
        var posicao = $(seletor).offset().top;
        $("html, body").animate({
            scrollTop: posicao - 50
        }, 1500);

    });

    $(subir).click(function() {
        $("html, body").animate({
            scrollTop: 0
        }, 700);
    });

    $(window).scroll(function() {
        var minhaPosicao = $(this).scrollTop();
        if (minhaPosicao >= 400) {
            subir.fadeIn()
        } else {
            subir.fadeOut();
        }
    });
});

function iniciar() {
    setInterval(mostrarData, 1000);
}

function mostrarData() {

    var data = new Date();

    var dia = data.getDate(); // 1-31
    var mes = data.getMonth(); // 0-11 (zero=janeiro)
    var ano4 = data.getFullYear(); // 4 dígitos

    var hora = data.getHours(); // 0-23
    var min = data.getMinutes(); // 0-59
    var seg = data.getSeconds(); // 0-59

    if (hora < 10) hora = "0" + hora
    if (min < 10) min = "0" + min
    if (seg < 10) seg = "0" + seg

    var str_data = dia + '/' + (mes + 1) + '/' + ano4;
    var str_hora = hora + ':' + min + ':' + seg;

    document.getElementById('dia').value = str_data;
    document.getElementById('hora').value = str_hora;
    document.getElementById('horario').value = str_hora;
}