(function(){

    $(document).ready(function(){
       $(".vote-for-the-article").click(function(){
          var userCallBacks = {
            "success": function(data){
                var articleId = $(this).attr("vote-for-the-article");
                saveArticleVote(articleId);
            },
            "error": function(data){

            }
          };
          pmprojectutils.auth.checkUserLogin(userCallBacks)
       });
       function saveArticleVote(articleId){

       }
    });

});