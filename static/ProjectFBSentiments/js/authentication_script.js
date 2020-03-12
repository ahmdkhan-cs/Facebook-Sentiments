$('document').ready(function(){
    $('.js--authenticating-pages').addClass('animated fadeIn');

    // Signup validation
    $('[name=signup] #submit').on('click', function(){
        if($('[name=signup] [name=username]').val() == ""){
            $('[name=signup] #validusername').text("Enter username");
            $('[name=signup] [name=username]').addClass('input-style-error');
            return false;
        }
    });

    $('[name=signup] #submit').on('click', function(){
        if($('[name=signup] [name=email]').val() == ""){
            $('[name=signup] #validemail').text("Enter email");
            $('[name=signup] [name=email]').addClass('input-style-error');
            return false;
        }
    });

    $('[name=signup] #submit').on('click', function(){
        if($('[name=signup] [name=password1]').val() == ""){
            $('[name=signup] #validpassword1').text("Enter password");
            $('[name=signup] [name=password1]').addClass('input-style-error');
            return false;
        }
    });

    $('[name=signup] #submit').on('click', function(){
        if($('[name=signup] [name=password2]').val() != $('[name=signup] [name=password1]').val()){
            $('[name=signup] #validpassword2').text("Password doesnt match");
            $('[name=signup] [name=password2]').addClass('input-style-error');
            return false;
        }
    });


    // Login validation

    
    $('[name=login] #submit').on('click', function(){
        if($('[name=login] [name=username]').val() == ""){
            $('[name=login] #validusername').text("Enter email");
            $('[name=login] [name=username]').addClass('input-style-error');
            return false;
        }
    });

    $('[name=login] #submit').on('click', function(){
        if($('[name=login] [name=password]').val() == ""){
            $('[name=login] #validpassword').text("Enter password");
            $('[name=login] [name=password]').addClass('input-style-error');
            return false;
        }
    });


});
