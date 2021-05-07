function statusChangeCallback(response) {
    console.log(response);
    if (response.status === 'connected') {
        fetchUserDetail();
    } else if (response.status === 'not_authorized') {
        console.log("Please log into this app.")
    } else {
        console.log("Please log into this Facebook.")
    }
}

function fetchUserDetail() {
    FB.api('/me', function (response) {
        console.log(response)
        console.log('Successful login for: ' + response.name);
    });
}

function checkLoginState() {
    FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
    });
}