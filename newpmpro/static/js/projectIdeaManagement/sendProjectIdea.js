/**
 * Created by srikanthmv on 16/7/17.
 */

$(document).ready(function(){
    $(".send-project-idea").click(function(){
        formId = $(this).attr("data-form-id");
        var userLoginCheck = {
            "success": function(){
                sendProjectIdea(this);
            },
            "error": function(){
                $("#loginModalForm").foundation('open');
            }
        };
        window.pmprojectutils.auth.checkUserLogin(userLoginCheck);
    });

    function sendProjectIdea(currentElement){
        var formData = new FormData($("#"+formId)[0]);
        formData.append("projectAbstract", $("#projectAbstract").val());
        var projectIdeaCallBacks = {
            "success": function(data){
                alert("success")
            },
            "error": function(data){
                alert("error")
            }
        };
        window.pmprojectutils.getResponse('POST','api/idea/send-project-idea',formData,projectIdeaCallBacks, true)
    }
});

var formId = "";