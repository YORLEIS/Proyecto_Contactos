$(document).ready(function () {
    $("form").submit(function (event) {
        var isValid = true;
        
        // Validar campo de identificación
        var cedula = $("#txtCedula").val();
        if (!isValidCedula(cedula)) {
            isValid = false;
            $("#txtCedula").addClass("is-invalid");
            $("#cedulaError").text("N° de identificación debe tener maximo 10 dígitos.");
        } else {
            $("#txtCedula").removeClass("is-invalid");
            $("#cedulaError").text("");
        }
        
        //validar telefono
        var telefono = $("#txtTelefono").val();
        if (!isValidTelefono(telefono)) {
            isValid = false;
            $("#txtTelefono").addClass("is-invalid");
            $("#telefonoError").text("Número de teléfono no válido.");
        } else {
            $("#txtTelefono").removeClass("is-invalid");
            $("#telefonoError").text("");
        }
     
        if (!isValid) {
            event.preventDefault();
        }
    });
});

function isValidCedula(cedula) {
    return cedula.length <=10 && /^\d+$/.test(cedula);
}

function isValidTelefono(telefono) {
    return /^\d{10}$/.test(telefono);
}
