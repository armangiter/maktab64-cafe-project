function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}
function getAllCookie() {
    let ca = document.cookie.split(';');
    return ca
}

function eraseCookie(name) {
    document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}
$('.card_btn').click(function () {
            $.ajax({
                url: "{{ url_for('card') }}",
                type: 'GET',
                success: function (res) {
                    $('#items').html(res['data']);
                }
            });
        })
