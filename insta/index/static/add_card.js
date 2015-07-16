$(document).ready(function () {

    var $main_menu = $('#main-menu'),
        $form = $('#add-card-form'),
        $progress = $('div.progress-bar'),
        fields = ['position', 'email', 'description', 'video', 'captcha'],
        error_class = 'has-error',
        error_template = '<li class="control-label">{msg}</li>',
        error_container_template = 'ul#errors-',
        required_error = 'Обязательное поле.',
        VIDEO_MAX_SIZE = 1024 * 1024 * 512,
        VIDEO_MIN_SIZE = 1024 * 1024 * 1,
        video_size = 0;

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

    function get_main_menu(){

        // get main_menu from backend use ajax
        $.ajax({
            url: '/anonymous',
            type: 'GET',
            success: function(response) {
                if (response.result === 'anonymous'){
                    $main_menu.html(''
                        // vk login btn
                        +   '<li>'
                        +       '<p class="navbar-btn">'
                        +           '<a href="/login" class="btn btn-sm btn-social btn-vk ">'
                        +               '<i class="fa fa-vk"></i> Войти через Вконтакте'
                        +           '</a>'
                        +       '</p>'
                        +   '</li>'
                    );
                } else if (response.result === 'authenticated'){
                    $main_menu.html(''
                        // create new card btn
                        +   '<li>'
                        +       '<a role="button" id="add-card-link">Совершить открытие</a>'
                        +   '</li>'
                        // vk logout btn
                        +   '<li>'
                        +       '<p class="navbar-btn">'
                        +           '<a href="/logout" class="btn btn-sm btn-social btn-vk ">'
                        +               '<i class="fa fa-vk"></i> Выйти'
                        +           '</a>'
                        +       '</p>'
                        +   '</li>'
                    );
                    $('#add-card-link').click(function(){
                        $('#add-card').modal('show');
                    });
                }
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
                $form.find(error_container_template + value).parent().addClass(error_class);
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
            video_size = file.size;
            if ((video_size > VIDEO_MAX_SIZE) || (video_size < VIDEO_MIN_SIZE)) {
                errors['video'] = ['Недопустимый размер файла. (min 1 mb, max 512 Mb)'];
            }
            if (file.type.indexOf('video') == -1) {
                errors['video'] = ['Загрузите видео файл.'];
            }
        }

        // validate re captcha
        var value = grecaptcha.getResponse();
        if (!value.trim()){
            is_valid = false;
            // set required msg error
            errors['captcha'] = [required_error];
        }

        // insert errors
        insert_errors(errors);
        return is_valid;
    };

    function progress_handling_function(e){
        if(e.lengthComputable){
            var percent = e.loaded / e.total * 100;
            $progress.attr('aria-valuenow', e.loaded);
            $progress.attr('style', 'width: {pc}%'.replace('{pc}', percent));
        }
    }

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
            xhr: function() {
                var myXhr = $.ajaxSettings.xhr();
                if(myXhr.upload){
                    myXhr.upload.addEventListener('progress', progress_handling_function, false);
                }
                return myXhr;
            },
            success: function(response) {
                $parent = $form.parent()
                $parent.empty();
                $parent.html(''
                    + '<div class="alert alert-info">'
                    +     '<p>'
                    +         '<strong>Поздравляем</strong>, ваше открытие принято. '
                    +         'После подтверждения модератором оно будет опубликовано! '
                    +         '<strong>Спасибо</strong>, что исследуете мир вместе с нами.'
                    +     '</p>'
                    + '</div>');
            },
            error: function(response) {
                var data = response.responseJSON;
                // set errors for each field in response errors
                if (data.result === 'errors') {
                    insert_errors(data.errors);
                }
            },
            beforeSend: function(){
                $form.find('button[type="submit"]').attr('disabled', true);
                // update progress bar
                $progress.attr('aria-valuenow', 0);
                $progress.attr('aria-valuemax', video_size);
                $progress.attr('style', 'width: 0%');
            },
            complete: function(){
                $form.find('button[type="submit"]').attr('disabled', false);
            }
        });

        return false;
    });

    get_main_menu();

});
