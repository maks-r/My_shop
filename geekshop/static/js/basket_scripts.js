window.onload = function() {
    $('.basket_list').on('click', input[type="number"], function(event) {
        s$.ajax({
            url: "/basket/edit/" + event.target.name + "/" + event.terget.value + "/",
            success: function (data) {
                $('.basket_list').html(data);
            },
        });
    });
} 