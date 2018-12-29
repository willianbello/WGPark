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