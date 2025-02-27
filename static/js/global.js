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





// Experience handling code
$(document).ready(function() {
    // Add jQuery validate plugin if it doesn't exist
    if (typeof $.validator === 'undefined') {
        // Load jQuery validate from CDN
        $.getScript('https://cdnjs.cloudflare.com/ajax/libs/jquery-validate/1.19.5/jquery.validate.min.js', function() {
            setupFormValidation();
        });
    } else {
        setupFormValidation();
    }
  
    function setupFormValidation() {
        //************* AJOUT D'EXPERIENCE ***************//
        $("#btn-add-experience").on('click', function() {
            $('#add-experience-modal').modal('show');
            window.AppliquerMaskSaisie();
        });
  
        //Bouton d'enregistrement de l'expérience
        $("#btn-save-experience").on('click', function() {
          let btn_save_experience = $(this);
          let formulaire = $('#add-experience-form');
          let href = formulaire.attr('action');
      
          $.validator.setDefaults({ ignore: [] });
          
          let formData = new FormData();
          
          let certificatFiles = $('#add-experience-form #certificat_file')[0]?.files;
          let attachmentFiles = $('#add-experience-form #attachment_file')[0]?.files;
      
          if (formulaire.valid()) {
              btn_save_experience.attr('disabled', true);
      
              // Créer la notification avec une référence
              const notification = new Noty({
                  text: gettext('Voulez-vous vraiment créer cette expérience ?'),
                  type: 'warning',
                  layout: 'center',
                  theme: 'custom',
                  timeout: false,
                  buttons: [
                      Noty.button(gettext('OUI'), 'btn btn-primary', function() {
                          notification.close();
                          
                          // Ajouter les fichiers au FormData
                          if (certificatFiles && certificatFiles.length > 0) {
                              formData.append('certificat_file', certificatFiles[0]);
                          }
                          
                          if (attachmentFiles && attachmentFiles.length > 0) {
                              formData.append('attachment_file', attachmentFiles[0]);
                          }
                          
                          // Sérialiser les données du formulaire
                          let data_serialized = formulaire.serialize();
                          $.each(data_serialized.split('&'), function(index, elem) {
                              let vals = elem.split('=');
                              let key = vals[0];
                              let valeur = decodeURIComponent(vals[1].replace(/\+/g, ' '));
                              formData.append(key, valeur);
                          });
      
                          $.ajax({
                              type: 'post',
                              url: href,
                              data: formData,
                              processData: false,
                              contentType: false,
                              success: function(response) {
                                if (response.status == 1) {
                                    resetFields('#' + formulaire.attr('id'));
                                    notifySuccess(response.message, function() {
                                      console.log("Rechargement de la page...");
                                      location.reload();
                                    });
                                    setTimeout(function() {
                                      location.reload();
                                    }, 500);
                                } else {
                                    let errors = JSON.parse(JSON.stringify(response.errors));
                                    let errors_list_to_display = '';
                                    for (field in errors) {
                                        errors_list_to_display += '- ' + ucfirst(field) + ' : ' + errors[field] + '<br/>';
                                    }
                            
                                    $('#add-experience-modal .alert .message').html(errors_list_to_display);
                                    $('#add-experience-modal .alert').fadeTo(2000, 500).slideUp(500, function() {
                                        $(this).slideUp(500);
                                    }).removeClass('alert-success').addClass('alert-warning');
                                    
                                    btn_save_experience.removeAttr('disabled');
                                }
                              },
                            
                              error: function(request, status, error) {
                                  notifyWarning(gettext("Erreur lors de l'enregistrement"));
                                  btn_save_experience.removeAttr('disabled');
                              }
                          });
                      }),
                      Noty.button(gettext('Annuler'), 'btn btn-danger', function() {
                          notification.close();
                          btn_save_experience.removeAttr('disabled');
                      })
                  ]
              });
      
              // Afficher la notification
              notification.show();
      
          } else {
              $('label.error').css({ display: 'none', height: '0px' }).removeClass('error').text('');
      
              let validator = formulaire.validate();
              $.each(validator.errorMap, function(index, value) {
                  console.log('Id: ' + index + ' Message: ' + value);
              });
      
              notifyWarning(gettext('Veuillez renseigner tous les champs obligatoires'));
              btn_save_experience.removeAttr('disabled');
          }
        });
  
        // Handle modal closing - reset form
        $('#add-experience-modal').on('hidden.bs.modal', function() {
            resetFields('#add-experience-form');
            $('#add-experience-form .alert').hide();
            $('#add-experience-form .is-invalid').removeClass('is-invalid');
            $('#add-experience-form .invalid-feedback').text('');
        });
  
        
        //************* EDITION D'EXPERIENCE ***************//
        $(".edit-experience-btn").on('click', function() {
            let experienceId = $(this).data('id');
            let editUrl = $(this).data('href');
            
            console.log('resultat experienceId:', experienceId);
            
            // Update form action URL with the correct ID
            let formAction = $('#edit-experience-form').attr('action');
            formAction = formAction.replace('/0/', `/${experienceId}/`);
            $('#edit-experience-form').attr('action', formAction);
            
            // Récupération des données de l'expérience via l'API
            $.ajax({
                url: editUrl,
                type: 'GET',
                success: function(response) {
                    if (response.status === 1) {
                        let data = response.data;
                        
                        console.log('resultat data:', data);
                        
                        // Remplir le formulaire avec les données existantes
                        $('#edit-experience-id').val(data.id);
                        $('#edit-entreprise').val(data.entreprise);
                        $('#edit-fonction').val(data.fonction);
                        $('#edit-date-debut').val(data.date_debut);
                        $('#edit-location').val(data.location);
                        $('#edit-technologies').val(data.technologies);
                        $('#edit-name').val(data.name);
                        $('#edit-description').val(data.description);
                        
                        // Gérer la date de fin et le checkbox "Poste actuel"
                        if (data.date_fin) {
                            $('#edit-date-fin').val(data.date_fin);
                            $('#edit-en-cours').prop('checked', false);
                            $('#edit-date-fin').prop('disabled', false);
                        } else {
                            $('#edit-date-fin').val('');
                            $('#edit-en-cours').prop('checked', true);
                            $('#edit-date-fin').prop('disabled', true);
                        }
                        
                        // Afficher la modal
                        $('#edit-experience-modal').modal('show');
                    } else {
                        notifyError(response.message || gettext("Erreur lors de la récupération des données"));
                    }
                },
                error: function(xhr, status, error) {
                    notifyError(gettext("Erreur lors de la récupération des données"));
                }
            });
        });

        // Bouton de mise à jour de l'expérience
        $("#btn-update-experience").on('click', function() {
            let btn_update = $(this);
            let formulaire = $('#edit-experience-form');
            let href = formulaire.attr('action');
            
            if (formulaire.valid()) {
                btn_update.attr('disabled', true);
                
                const updateNotification = new Noty({
                    text: gettext('Voulez-vous vraiment mettre à jour cette expérience ?'),
                    type: 'warning',
                    layout: 'center',
                    theme: 'custom',
                    timeout: false,
                    buttons: [
                        Noty.button(gettext('OUI'), 'btn btn-primary', function() {
                            updateNotification.close();
                            
                            let formData = new FormData(formulaire[0]);
                            
                            $.ajax({
                                type: 'post',
                                url: href,
                                data: formData,
                                processData: false,
                                contentType: false,
                                success: function(response) {
                                    if (response.status == 1) {
                                        $('#edit-experience-modal').modal('hide');
                                        notifySuccess(response.message, function() {
                                            location.reload();
                                        });
                                    } else {
                                        let errors = response.errors || {};
                                        let errors_list = '';
                                        
                                        for (field in errors) {
                                            $('#edit-' + field).addClass('is-invalid');
                                            $('#edit-' + field).siblings('.invalid-feedback').text(errors[field]);
                                            errors_list += '- ' + ucfirst(field) + ' : ' + errors[field] + '<br/>';
                                        }
                                        
                                        $('#edit-experience-modal .alert .message').html(errors_list);
                                        $('#edit-experience-modal .alert').show()
                                            .removeClass('alert-success').addClass('alert-warning');
                                        
                                        btn_update.removeAttr('disabled');
                                    }
                                },
                                error: function() {
                                    notifyWarning(gettext("Erreur lors de la mise à jour"));
                                    btn_update.removeAttr('disabled');
                                }
                            });
                        }),
                        Noty.button(gettext('Annuler'), 'btn btn-danger', function() {
                            updateNotification.close();
                            btn_update.removeAttr('disabled');
                        })
                    ]
                });
                
                updateNotification.show();
            } else {
                notifyWarning(gettext('Veuillez renseigner tous les champs obligatoires'));
            }
        });
        // Handle edit modal closing - reset form
        $('#edit-experience-modal').on('hidden.bs.modal', function() {
            $('#edit-experience-form .alert').hide();
            $('#edit-experience-form .is-invalid').removeClass('is-invalid');
            $('#edit-experience-form .invalid-feedback').text('');
        });
  
        //************* SUPPRESSION D'EXPERIENCE ***************//
        $(".delete-experience-btn").on('click', function() {
            let experienceId = $(this).data('id');
            let deleteUrl = $(this).data('href');
            let btn_delete_experience = $(this);

            const deleteNotification = new Noty({
                text: gettext('Voulez-vous vraiment supprimer cette expérience ?'),
                type: 'error',
                layout: 'center',
                theme: 'custom',
                timeout: false,
                buttons: [
                    Noty.button(gettext('OUI'), 'btn btn-danger', function() {
                        deleteNotification.close();
                        btn_delete_experience.attr('disabled', true);

                        // Récupérer le token CSRF depuis le cookie
                        function getCookie(name) {
                            let cookieValue = null;
                            if (document.cookie && document.cookie !== '') {
                                const cookies = document.cookie.split(';');
                                for (let i = 0; i < cookies.length; i++) {
                                    const cookie = cookies[i].trim();
                                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                        break;
                                    }
                                }
                            }
                            return cookieValue;
                        }

                        const csrftoken = getCookie('csrftoken');

                        $.ajax({
                            type: "POST",
                            url: deleteUrl,
                            headers: {
                                'X-CSRFToken': csrftoken
                            },
                            success: function(response) {
                                if (response.status == 1) {
                                    notifySuccess(response.message, function() {
                                        location.reload();
                                    });
                                } else {
                                    notifyWarning(response.message);
                                    btn_delete_experience.removeAttr('disabled');
                                }
                            },
                            error: function(xhr, status, error) {
                                notifyError(gettext("Erreur lors de la suppression"));
                                btn_delete_experience.removeAttr('disabled');
                            }
                        });
                    }),
                    Noty.button(gettext('Annuler'), 'btn btn-secondary', function() {
                        deleteNotification.close();
                    })
                ]
            });

            deleteNotification.show();
        });
        
  
        // Pour le formulaire d'ajout
        $('#en_cours').on('change', function() {
          if ($(this).is(':checked')) {
              $('#date_fin').prop('disabled', true).val('');
              $('<input>').attr({
                  type: 'hidden',
                  name: 'simultaneous_work',
                  value: 'true'
              }).appendTo('#add-experience-form');
          } else {
              $('#date_fin').prop('disabled', false);
              $('#add-experience-form input[name="simultaneous_work"]').remove();
          }
        });
  
        // Gestion du checkbox "Poste actuel" dans le formulaire d'édition
        $('#edit-en-cours').on('change', function() {
            if ($(this).is(':checked')) {
                $('#edit-date-fin').prop('disabled', true).val('');
            } else {
                $('#edit-date-fin').prop('disabled', false);
            }
        });
  
        // Validation using jQuery Validate plugin
        $('#add-experience-form').validate({
            errorPlacement: function(error, element) {
                element.siblings('.invalid-feedback').text(error.text());
            },
            highlight: function(element) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function(element) {
                $(element).removeClass('is-invalid');
            },
            rules: {
                name: "required",
                fonction: "required",
                entreprise: "required",
                location: "required",
                date_debut: "required",
                description: "required"
            },
            messages: {
                name: gettext("Ce champ est obligatoire"),
                fonction: gettext("Ce champ est obligatoire"),
                entreprise: gettext("Ce champ est obligatoire"),
                location: gettext("Ce champ est obligatoire"),
                date_debut: gettext("Ce champ est obligatoire"),
                description: gettext("Ce champ est obligatoire")
            }
        });
        
        // Validation pour le formulaire d'édition
        $('#edit-experience-form').validate({
            errorPlacement: function(error, element) {
                element.siblings('.invalid-feedback').text(error.text());
            },
            highlight: function(element) {
                $(element).addClass('is-invalid');
            },
            unhighlight: function(element) {
                $(element).removeClass('is-invalid');
            },
            rules: {
                name: "required",
                fonction: "required",
                entreprise: "required",
                date_debut: "required",
                description: "required"
            },
            messages: {
                name: gettext("Ce champ est obligatoire"),
                fonction: gettext("Ce champ est obligatoire"),
                entreprise: gettext("Ce champ est obligatoire"),
                date_debut: gettext("Ce champ est obligatoire"),
                description: gettext("Ce champ est obligatoire")
            }
        });
    }
});