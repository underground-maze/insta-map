$(document).ready(function () {

    var $form = $('#add-card-form'),
        fields = ['position', 'email', 'description', 'video'],
        error_class = 'has-error';

    function get_csrf_token(){
        // get csrf_token from backend use ajax
        $.ajax({
            url: $form.attr('action'),
            type: 'GET',
            success: function(response) {
                // insert input into form
                $form.find('#csrf_token').val(response['csrf_token']);
            },
            error: function() {
                console.log(arguments);
            }
        });
    };

    $('#add-card').on('shown.bs.modal', function(){
        get_csrf_token();
    });

    $form.on('submit', function(){
        var $this = $(this);
        var formData = new FormData(this);
        console.log(formData)

        $.ajax({
            url: $this.attr('action'),
            type: 'POST',
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function(response) {
                alert(0);
                console.log(response);
            },
            error: function(response) {
                alert(1);
                if (response.status === 'errors') {
                    fields.forEach(function(index, value) {
                        if (response.errors[value]){
                            $form.find('#' + value).addClass(error_class);
                        }
                    });
                }
            }
        });

        return false;
    });

});
