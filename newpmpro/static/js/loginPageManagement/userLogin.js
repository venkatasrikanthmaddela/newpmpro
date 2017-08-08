/**
 * Created by srikanthmv on 15/7/17.
 */


$(document).ready(function(){
    $(".register-directly").click(function(){
        var userName = $("#userName").val();
        var emailId = $("#emailId").val();
        var PhoneNumber = $("#mobileNumber").val();
        var password = $("#password").val();
        var isSubscribed = $("#isSubscribed").is(":checked");

        var signUpCallBacks = {
            "success": function(data){
                alert("success");
                window.pmprojectutils.myAccount.setAccountMail(data.email);
                window.pmprojectutils.myAccount.setAccountName(data.name);
                if(window.location.pathname == "/"){
                    window.location.reload();
                }
                if(window.location.pathname == "/search-project"){
                    $("#loginModalForm").foundation('close');
                    if(window.pmprojectutils.projectRequestInfo.id){
                        window.pmprojectutils.projectRequestInfo.sendProjectRequest();
                    }
                    else{
                        window.location.reload();
                    }
                }
                if(window.location.pathname == "/new-project-idea"){
                    window.location.reload();
                }
            },
            "error": function(data){
                console.log(data.responseJSON.error);
                alert(data.responseJSON.error);
            }
        };
        window.pmprojectutils.auth.signup(userName, PhoneNumber, emailId, password, isSubscribed, signUpCallBacks)
    });

    $(".user-login").click(function(){
        var user_email = $("#user-login-email").val();
        var password = $("#user-login-password").val();
        var signInCallBacks = {
            "success": function(){
                if(window.location.pathname == "/"){
                    window.location.reload();
                }
                if(window.location.pathname == "/search-project"){
                    $("#loginModalForm").foundation('close');
                    if(window.pmprojectutils.projectRequestInfo.id){
                        window.pmprojectutils.projectRequestInfo.sendProjectRequest();
                    }
                    else{
                        window.location.reload();
                    }
                }
                if(window.location.pathname == "/new-project-idea"){
                    window.location.reload();
                }
            },
            "error": function(data){
                alert(data.responseJSON.error);
            }
        };
        window.pmprojectutils.auth.logIn(user_email, password, signInCallBacks);
    });
});