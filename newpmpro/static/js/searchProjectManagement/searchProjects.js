/**
 * Created by srikanthmv on 19/7/17.
 */

(function(projectRequestInfo){
    projectRequestInfo.id = "";
    projectRequestInfo.setProjectId = function(projectId){
        projectRequestInfo.id = projectId;
    };
    projectRequestInfo.sendProjectRequest = function(){
        var projectRequestCallBacks = {
            "success": function(){
                alert("success");
                window.location.reload();
            },
            "error": function(data){
                alert(data.responseJSON.result);
                window.location.reload();
            }
        };
        window.pmprojectutils.getResponse("POST", '/api/project/request-for-project', {"projectId":projectRequestInfo.id}, projectRequestCallBacks, false);
    }

})(window.pmprojectutils.projectRequestInfo = window.pmprojectutils.projectRequestInfo || {}, jQuery);

$(document).ready(function() {
    //var table = $('#AllProjectsData').DataTable();
    $('#AllProjectsData').DataTable({
        responsive: true,
        "dom": '<<t>lp>',
        "pagingType": "full_numbers"
    });

    $("#searchProjects").on('keyup click', function(){
        var searchVal = $(this).val();
        $("#AllProjectsData").DataTable().search(searchVal).draw();
    });

    $(".request-for-project").on('click', function()
    {
        window.pmprojectutils.projectRequestInfo.setProjectId($(this).attr("data-id"));
        var userLoginCheck = {
            "success": function(){
                window.pmprojectutils.projectRequestInfo.sendProjectRequest();
            },
            "error": function(){
                $("#loginModalForm").foundation('open');
            }
        };
        window.pmprojectutils.auth.checkUserLogin(userLoginCheck);
    });
});