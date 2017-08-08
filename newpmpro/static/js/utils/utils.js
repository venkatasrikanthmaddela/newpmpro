/**
 * Created by srikanthmv on 15/7/17.
 */

( function (pmprojectutils, $) {
    pmprojectutils.baseurl = '';
    pmprojectutils.getCookie = function (name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };

    pmprojectutils.setNewCSRFToken = function () {
        var updatedToken = pmprojectutils.getCookie('csrftoken');
        $('form .csrfToken').each(function (index, value) {
            $(this).val(updatedToken);
        });
    };

    pmprojectutils.getResponse = function (reqType, path, sendData, callbacks ,isFormData) {

        isFormData = isFormData || false ;
        var response = {
            type: reqType,
            url: pmprojectutils.baseurl + path,
            //data: JSON.stringify(sendData),
            headers: {
                "X-CSRFToken": pmprojectutils.getCookie('csrftoken')
            },

            contentType: 'application/json'
        };
//        if (reqType != "GET") {
        if(isFormData){
            response["contentType"] = false;
            response["processData"] = false;
            response["data"] = sendData;
        }
        else{
            response["dataType"] = "json";
            response["data"] = JSON.stringify(sendData)
        }
//        }

        if (callbacks != undefined) {
            if (callbacks["success"]) {
                response["success"] = function (data, textStatus, jqXHR) {
                    callbacks["success"](data, textStatus, jqXHR);
                };
            }
            if (callbacks["error"]) {
                response["error"] = function (data, textStatus, jqXHR) {
                    callbacks["error"](data, textStatus, jqXHR);
                };
            }
        }
        $.ajax(response);
    };

}(window.pmprojectutils = window.pmprojectutils || {}, jQuery) );


(function(auth, $){

    auth.signup = function(name, phoneNumber, emailId, password, isSubscribed, callbacks){
        var signUpObj = {
            "name": name,
            "email": emailId,
            "phoneNumber":phoneNumber,
            "password":password,
            "isSubscribed":isSubscribed
        };
        window.pmprojectutils.getResponse("POST", "/account/api/signup/direct", signUpObj, callbacks, false);

    };
    auth.logIn = function(username, password, callBacks){
        var loginObj = {
            "email": username,
            "password": password
        };
        window.pmprojectutils.getResponse("POST", "/account/api/login", loginObj, callBacks)
    };
    auth.logout = function (callbacks) {
        window.pmprojectutils.getResponse("POST", "/account/api/logout", {}, callbacks);
    };
    auth.checkUserLogin = function(callbacks){
        window.pmprojectutils.getResponse("GET", "/account/api/is-user-logged-in", {}, callbacks);
    }

}(window.pmprojectutils.auth = window.pmprojectutils.auth || {}, jQuery));

( function (myAccount, $) {
    myAccount.accountName = "";
    myAccount.accountMail = "";
    myAccount.setAccountName = function (userName) {
        myAccount.accountName = userName;
    };
    myAccount.setAccountMail = function (email) {
        myAccount.accountMail = email;
    };

}(window.pmprojectutils.myAccount = window.pmprojectutils.myAccount || {}, jQuery));


function checklogin(){
    if(window.pmprojectutils.myAccount.accountMail){
        return true;
    }
    else{
        return false;
    }
}