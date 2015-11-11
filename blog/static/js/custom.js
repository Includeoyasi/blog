$(document).ready(function(){
            $(".article").hover(function(){
                $(".like").css('color', 'red');
                $(".info i").css('border-radius', '8px').css('background-color', '#ddd');

            }, function(){
                $(".like").css('color', 'black');
                $(".info i").css('background-color', '#fff');
            });

        });