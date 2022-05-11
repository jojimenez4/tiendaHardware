
$.getJSON('https://mindicador.cl/api', function(data) {
    var dailyIndicators = data;
    $("<p/>", {
        html: 'Valor dolar $' + dailyIndicators.dolar.valor
    }).appendTo("#dolar");
}).fail(function() {
    console.log('Error al consumir la API!');
});