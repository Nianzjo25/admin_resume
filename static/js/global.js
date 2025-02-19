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

// Ajouter les styles personnalisés pour Noty
const notyCustomStyles = `
    .noty_theme__custom {
        border-radius: 4px;
        margin: 10px 0;
        padding: 0;
        background-color: white;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        position: relative;
    }

    .noty_theme__custom::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        border-radius: 4px 0 0 4px;
    }

    .noty_theme__custom.noty_type__success::before {
        background-color: #28a745;
    }

    .noty_theme__custom.noty_type__warning::before {
        background-color: #ffc107;
    }

    .noty_theme__custom.noty_type__error::before {
        background-color: #dc3545;
    }

    .noty_theme__custom .noty_body {
        padding: 15px 20px;
        font-size: 14px;
        color: #333;
    }

    .noty_theme__custom .noty_buttons {
        padding: 10px;
        border-top: 1px solid #eee;
        text-align: right;
    }

    .noty_theme__custom .btn {
        margin-left: 5px;
        border-radius: 3px;
        font-size: 13px;
    }
`;

// Ajouter les styles au document
const styleElement = document.createElement('style');
styleElement.textContent = notyCustomStyles;
document.head.appendChild(styleElement);

function notifySuccess(message, fnCallback) {
    if (my_noty) {
        my_noty.close();
    }
    
    my_noty = new Noty({
        text: message,
        type: 'success',
        layout: 'topRight',
        theme: 'custom',
        timeout: 5000,
        progressBar: true,
        buttons: [
            Noty.button('OK', 'btn btn-success', function () {
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
        layout: 'topRight',
        theme: 'custom',
        timeout: 5000,
        progressBar: true,
        buttons: [
            Noty.button('OK', 'btn btn-warning', function () {
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
        layout: 'topRight',
        theme: 'custom',
        timeout: 5000,
        progressBar: true,
        buttons: [
            Noty.button('OK', 'btn btn-danger', function () {
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