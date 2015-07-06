$(document).ready(function () {

    var $form = $('#add-card-form'),
        fields = ['position', 'email', 'description', 'video'],
        error_class = 'has-error',
        error_template = '<li class="control-label">{msg}</li>',
        error_container_template = 'ul#errors-',
        required_error = 'Обязательное поле.',
        VIDEO_MAX_SIZE = 1024 * 1024 * 1024
        VIDEO_MIN_SIZE = 1024 * 1024 * 10;

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

    function clear_errors(){
        // remove error classes
        $('.' + error_class).removeClass(error_class);
        // clean error messages
        fields.forEach(function(value){
            $form.find(error_container_template + value).empty();
        });
    };

    function insert_errors(errors){
        fields.forEach(function(value) {
            if (errors[value]){
                // set error css class for parent div
                $form.find('#' + value).parent().addClass(error_class);
                // insert errors
                var container = $form.find(error_container_template + value);
                errors[value].forEach(function(error_msg){
                    container.append(error_template.replace('{msg}', error_msg));
                });
            }
        });
    }

    function validate_email(email) {
        var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
        return re.test(email);
    }

    function validate_form(){
        var is_valid = true, errors = {};

        // validate description and position required field
        ['description', 'position'].forEach(function(item){
            var value = $form.find('#' + item).val();
            if (!value.trim()){
                is_valid = false;
                // set required msg error
                errors[item] = [required_error];
            }
        });

        // validate email field
        var value = $form.find('#email').val();
        if (!value.trim()){
            is_valid = false;
            // set required msg error
            errors['email'] = [required_error];
        }

        if (!validate_email(value)){
            is_valid = false;
            // set required msg error
            errors['email'] = ['Введите корректный адрес электронной почты.'];
        }

        // validate video field
        var value = $form.find('#video')[0].files;
        if (!value.length){
            is_valid = false;
            // set required msg error
            errors['video'] = [required_error];
        } else {
            var file = value[0];
            if ((file.size > VIDEO_MAX_SIZE) || (file.size < VIDEO_MIN_SIZE)) {
                errors['video'] = ['Недопустимый размер файла. (min 10 mb, max 1 Gb)'];
            }
            if (file.type.indexOf('video') == -1) {
                errors['video'] = ['Загрузите видео файл.'];
            }
        }

        // insert errors
        insert_errors(errors);
        return is_valid;
    };

    $form.on('submit', function(){
        clear_errors();

        if (!validate_form()) {
            return false;
        }

        var formData = new FormData(this);

        $.ajax({
            url: $form.attr('action'),
            type: 'POST',
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            success: function(response) {
                console.log(response);
            },
            error: function(response) {
                var data = response.responseJSON;
                // set errors for each field in response errors
                if (data.result === 'errors') {
                    insert_errors(data.errors);
                }
            }
        });

        return false;
    });

});
