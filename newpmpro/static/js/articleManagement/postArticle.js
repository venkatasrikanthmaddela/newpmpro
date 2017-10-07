$(document).ready(function(){
    var ArticleEditorOptions = {
        debug: 'info',
        placeholder:'Write you article here...',
        theme:'snow'
    };
    var ArticleEditorQuillObject = new Quill('.ArticleEditor', ArticleEditorOptions);
    var CodeEditorOptions = {
        debug:'info',
        placeholder: 'your code goes here..',
        theme:'bubble'
    };
    var CodeEditorQuillObject = new Quill('.CodeEditor', CodeEditorOptions);

    $(".send-article-for-review").click(function(){
        var articleBody = ArticleEditorQuillObject.container.firstChild.innerHTML;
        var articleCodePart = CodeEditorQuillObject.container.firstChild.innerHTML;
        var formData = new FormData($('#articlePostForm')[0]);
        formData.append('articleBody', articleBody);
        formData.append('articleCodePart', articleCodePart);
        console.log(formData);
        var articleReviewCallBacks = {
            "success": function(data){
                alert("success");
            },
            "error": function(data){
                alert("error");
            }
        };
        window.pmprojectutils.getResponse('POST', '/api/article/send-for-review', formData , articleReviewCallBacks, true);
    });
});
