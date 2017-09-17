$(document).ready(function(){
    var ArticleEditorOptions = {
        debug: 'info',
        placeholder:'Write you article here...',
        theme:'snow'
    };
    var ArticleEditorQuillObject = new Quill('.ArticleEditor', ArticleEditorOptions);

    var toolbarOptions = ['code'];
    var CodeEditorOptions = {
        debug:'info',
        placeholder: 'your code goes here..',
        theme:'snow'
    };
    var CodeEditorQuillObject = new Quill('.CodeEditor', CodeEditorOptions);

    $(".send-article-for-review").click(function(){
        var title = $("#ArticleTitle").val();
        var subTitle = $("#ArticleSubTitle").val();
        var articleBody = CodeEditorQuillObject.container.firstChild.innerHTML;
        var articleCodePart = CodeEditorQuillObject.container.firstChild.innerHTML;
        //var formData = new FormData($('#articlePostForm')[0]);
        var formData = {
            "articleTitle":title,
            "articleSubTitle":subTitle,
            "articleBody":articleBody,
            "articleCodePart":articleCodePart
        };
        var articleReviewCallBacks = {
            "success": function(data){
                alert("success");
            },
            "error": function(data){
                alert("error");
            }
        };
        window.pmprojectutils.getResponse('POST', '/api/article/send-for-review', {"articleData":formData}, articleReviewCallBacks, false);
    });
});
