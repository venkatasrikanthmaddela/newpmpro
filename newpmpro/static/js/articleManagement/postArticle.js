$(document).ready(function(){
    var ArticleEditorOptions, CodeEditorOptions,ArticleEditorQuillObject,CodeEditorQuillObject;
    var articleTags = [];
    var selectedTags = [];
    setUpEditorProperties();
    getCustomTags();

    $("#articleTagsInput").focus(function(){
        $(this).autocomplete({
            source: articleTags,
            scroll: true
        });
    });

    $("#articleTagsInput").keypress(function(event){
        if(event.which == 13){
            var CurrentVal = $(this).val();
            if(selectedTags.indexOf(CurrentVal) === -1){
                selectedTags.push($(this).val());
                var dl = document.getElementById("articleTitleHelpText");
                dl.insertAdjacentHTML('afterend', '<span class="label primary">'+CurrentVal+'</span>&nbsp;');
                $("#articleTitleHelpText").load(location.href + " #articleTitleHelpText");
            }
        }
    });

    function getCustomTags(){
        var getTagsCallBacks = {
            "success": function(data){
                for(var i=0; i<data.tags.length; i++){
                    articleTags.push(data.tags[i]);
                }
            },
            "error": function(data){

            }
        };
        window.pmprojectutils.getResponse('GET', '/api/article/get-tags', {}, getTagsCallBacks, false)
    }

    //$("#articleTagsInput").focus(function(){
    //    console.log(articleTags);
    //    $(this).autocomplete("search");
    //});

    $(".send-article-for-review").click(function(){
        var articleBody = ArticleEditorQuillObject.container.firstChild.innerHTML;
        var articleCodePart = CodeEditorQuillObject.container.firstChild.innerHTML;
        var formData = new FormData($('#articlePostForm')[0]);
        formData.append('articleBody', articleBody);
        formData.append('articleCodePart', articleCodePart);
        console.log(formData);
        var articleReviewCallBacks = {
            "success": function(data){
                $('#articlePostForm')[0].reset();
                $("#articleSuccessModal").foundation('open');
                //window.location.href = "/articles/article-success";
            },
            "error": function(data){
                alert("error");
            }
        };
        window.pmprojectutils.getResponse('POST', '/api/article/send-for-review', formData , articleReviewCallBacks, true);
    });

    function setUpEditorProperties(){
        ArticleEditorOptions = {
            debug: 'info',
            placeholder:'Write you article here...',
            theme:'snow'
        };
        ArticleEditorQuillObject = new Quill('.article-editor', ArticleEditorOptions);
        CodeEditorOptions = {
            debug:'info',
            placeholder: 'your code goes here..',
            theme:'bubble'
        };
        CodeEditorQuillObject = new Quill('.code-editor', CodeEditorOptions);
    }
});
