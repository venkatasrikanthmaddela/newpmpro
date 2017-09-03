$(document).ready(function(){
    $(".vote-for-the-article").click(function(){
        articleId = $(this).attr("data-article-id");
        var userCallBacks = {
            "success": function(data){
                console.log(articleId);
                saveArticleVote(articleId);
            },
            "error": function(data){
                $("#loginModalForm").foundation('open');
            }
        };
        pmprojectutils.auth.checkUserLogin(userCallBacks)
    });
    function saveArticleVote(articleId){
        var articleCallbacks = {
            "success": function(data){
                alert(data.message);
                window.location.reload();
            },
            "error" : function(data){
                alert(data.responseJSON.message);
                window.location.reload();
            }
        };
        window.pmprojectutils.getResponse('POST', '/api/article/vote', {"articleId":articleId}, articleCallbacks, false);
    }
    var articleId = "";
});