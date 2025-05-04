$(document).ready(function() {
    console.log("Cantidad de .form-select:", $(".form-select").length);
    let htmlSeleccion = '<option selected>Tema</option>';
    $(".form-select").eq(1).append(htmlSeleccion);
});