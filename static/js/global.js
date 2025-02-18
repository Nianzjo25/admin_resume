function resetFields(formulaire) {

    //$(formulaire + " input[type=text]:not(.notreset)").val("");
    $(formulaire + " input:not(.notreset)").val("");
    $(formulaire + " input[type=number]:not(.notreset)").val("");
    $(formulaire + " input[type=date]:not(.notreset)").val("");
    $(formulaire + " input[type=email]:not(.notreset)").val("");
    $(formulaire + " select:not(.notreset)").prop('selectedIndex', 0);

}



function AppliquerMaskSaisie() {

    $('.money_field_avec_virgule').inputmask({
        alias: 'numeric',
        groupSeparator: ' ',
        autoGroup: true,
        digits: 2,
        digitsOptional: false,
        prefix: '',
        rightAlign: false,
        allowMinus: false,
        placeholder: '0',
        removeMaskOnSubmit: true
    });

    $('.money_field_only_positive').inputmask({
        alias: 'numeric',
        groupSeparator: ' ',
        autoGroup: true,
        digits: 0,
        digitsOptional: false,
        prefix: '',
        rightAlign: false,
        allowMinus: false,
        placeholder: '',
        removeMaskOnSubmit: true
    });

    $('.float_field_only_positive').inputmask({
        alias: 'numeric',
        groupSeparator: '',
        autoGroup: true,
        digits: 2,
        digitsOptional: true,
        prefix: '',
        rightAlign: false,
        allowMinus: false,
        placeholder: '0.00',
        removeMaskOnSubmit: true,
        onBeforePaste: function (pastedValue) {
            // Convertir la valeur collée en format numérique
            return pastedValue.replace(',', '.'); // Remplacer la virgule par un point si nécessaire
        }
    });


    //appliquer le mask de saisie sur les champs montant
    Inputmask("currency", {
        prefix: "",
        groupSeparator: " ",//désactiver pour
        alias: "numeric",
        digits: 0,// nombre de caractère après la virgule
        onKeyDown: function (event) {
            var key = event.keyCode || event.charCode;

            // Empêcher la saisie du signe négatif
            if (key === 189 || key === 109) { // Les codes 189 et 109 correspondent au signe moins (-)
                event.preventDefault();
                return false;
            }
        }
    }).mask('.money_field');

    Inputmask("currency", {
        prefix: "",
        groupSeparator: " ",//désactiver pour
        alias: "numeric",
        digits: 0,// nombre de caractère après la virgule
        onKeyDown: function (event) {
            var key = event.keyCode || event.charCode;

            // Empêcher la saisie du signe négatif
            if (key === 189 || key === 109) { // Les codes 189 et 109 correspondent au signe moins (-)
                event.preventDefault();
                return false;
            }
        }
    }).mask('.total_autres_taxes');

    //appliquer le mask de saisie sur les champs montant
    Inputmask("currency", {
        prefix: "",
        groupSeparator: " ",//désactiver pour
        alias: "numeric",
        digits: 0,// nombre de caractère après la virgule
        onKeyDown: function (event) {
            var key = event.keyCode || event.charCode;

            // Empêcher la saisie du signe négatif
            /*
            if (key === 189 || key === 109) { // Les codes 189 et 109 correspondent au signe moins (-)
                event.preventDefault();
                return false;
            }
            */
        }
    }).mask('.money_field_negative');

    /*
    new Cleave('.money_field', {
        numeral: true,
        numeralThousandsGroupStyle: 'thousand'
        //delimiter: ' ',
    });
    alert("cleve init");


    if ($('.money_field').length > 0) {

       AutoNumeric.multiple('.money_field', {
          currencySymbol: '',
          digitGroupSeparator: ' ',
          decimalCharacter: '.',
          decimalPlaces: 0
        });

    }
    */

}
AppliquerMaskSaisie();



var my_noty;//variale global pour pouvoir le fermer de popup de l'extérieur
function notifySuccess(message, fnCallback) {
    if (my_noty) {
        my_noty.close();
    }
    
    my_noty = new Noty({
        text: message,
        type: 'success',
        layout: 'center',
        theme: 'bootstrap-v4',
        timeout: false,
        modal: true,
        buttons: [
            Noty.button('OK', 'btn btn-primary', function () {
                if (typeof fnCallback === 'function') fnCallback();
                my_noty.close();
            })
        ]
    }).show();
}

function notifyWarning(message, fnCallback) {
    if (typeof Noty === "undefined") {
        console.error("Erreur : Noty.js n'est pas chargé !");
        return;
    }

    if (my_noty) {
        my_noty.close();
    }

    my_noty = new Noty({
        text: message,
        type: 'warning',
        layout: 'center',
        theme: 'bootstrap-v4',
        timeout: false,
        modal: true,
        buttons: [
            Noty.button('OK', 'btn btn-primary', function () {
                if (typeof fnCallback === 'function') fnCallback();
                my_noty.close();
            })
        ]
    }).show();
}


function notifyError(message, fnCallback) {
    if (my_noty) {
        my_noty.close();
    }
    
    my_noty = new Noty({
        text: message,
        type: 'error',
        layout: 'center',
        theme: 'bootstrap-v4',
        timeout: false,
        modal: true,
        buttons: [
            Noty.button('OK', 'btn btn-primary', function () {
                if (typeof fnCallback === 'function') fnCallback();
                my_noty.close();
            })
        ]
    }).show();
}


function addInputAlphaNumValidation(inputSelector, errorId) {
    var previousValue = ""; // Déclarer previousValue en dehors de la fonction
    $(inputSelector).on("input", function () {
        var inputValue = $(this).val();
        // var alphanumericRegex = /^[a-zA-Z0-9]*$/;
        var alphanumericRegex = /^[a-zA-Z0-9\/\-_]*$/;
        var errorMessage = $("#" + errorId);

        if (!alphanumericRegex.test(inputValue)) {
            errorMessage.css("display", "block");
            $(this).val(previousValue);
            setTimeout(function () {
                errorMessage.css("display", "none");
            }, 5000);
        } else {
            previousValue = inputValue;
            errorMessage.css("display", "none");
        }
    });
}

$(document).ready(function () {
    addInputAlphaNumValidation(".alpha_num_input", "error-message");
});