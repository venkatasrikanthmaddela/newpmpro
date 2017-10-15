$(document).ready(function(){
    var ArticleEditorOptions, CodeEditorOptions,ArticleEditorQuillObject,CodeEditorQuillObject;
    var articleRelModules = {
        "articleTags" : [],
        "articleCategories" : [],
        "selectedTags": new Array(),
        "selectedCategories" : new Array()
    };
    var modulesRegex = new RegExp("/^[a-zA-Z\s]+$/");
    setUpEditorProperties();
    getCustomTags();

    $("#articleTagsInput").focus(function(){
        $(this).autocomplete({
            source: articleRelModules.articleTags,
            scroll: true
        });
    });

    $("#articleCategoryInput").focus(function(){
       console.log(articleRelModules.articleCategories);
       $(this).autocomplete({
           source: articleRelModules.articleCategories,
           scroll: true

       })
    });

    $("#articleTagsInput").keypress(function(event){
        if(event.which == 13){
            var CurrentVal = $(this).val().toLowerCase();
            if(articleRelModules.selectedTags.indexOf(CurrentVal) === -1 && CurrentVal!="" && CurrentVal!=" " && modulesRegex.test(CurrentVal) == false){
                articleRelModules.selectedTags.push(CurrentVal);
                var trimmedVal = CurrentVal.replace(" ", '');
                var dl = document.getElementById("articleTitleHelpText");
                dl.insertAdjacentHTML('afterend', '<span class="label alert-box primary article-tag" id="'+trimmedVal+'" name="'+CurrentVal+'">'+CurrentVal+'</span>&nbsp;');
                $("#articleTitleHelpText").load(location.href + " #articleTitleHelpText");
                $("#articleTagsInput").val("");
            }
        }
    });

     $("#articleCategoryInput").keypress(function(event){
        if(event.which == 13){
            var CurrentVal = $(this).val().toLowerCase();
            if(articleRelModules.selectedCategories.indexOf(CurrentVal) === -1 && CurrentVal!="" && CurrentVal!=" "){
                articleRelModules.selectedCategories.push(CurrentVal);
                var trimmedVal = CurrentVal.replace(" ", '');
                var dl = document.getElementById("articleTagsHelpText");
                dl.insertAdjacentHTML('afterend', '<span class="label alert-box primary article-category-tag" id="'+trimmedVal+'" name="'+CurrentVal+'">'+CurrentVal+'</span>&nbsp;');
                $("#articleTagsHelpText").load(location.href + " #articleTagsHelpText");
                $("#articleCategoryInput").val("");
            }
        }
    });

    $("body").on("click", '.article-category-tag', function () {
       var selectedVal = $(this).attr("name");
       $(".delete-category").attr("data-category-name", selectedVal);
       $("#categoryRemovalModal").foundation('open');
    });

    $("body").on("click", '.article-tag', function () {
       var selectedVal = $(this).attr("name");
       $(".delete-tag").attr("data-tag-name", selectedVal);
       $("#tagRemovalModal").foundation('open');
    });

    $(".delete-tag").click(function(){
       var deleteVal = $(this).attr("data-tag-name");
       articleRelModules.selectedTags.splice( $.inArray(deleteVal,articleRelModules.selectedTags) ,1 );
       $("#tagRemovalModal").foundation('close');
       var trimmedDelVal = deleteVal.replace(" ", '');
       console.log(trimmedDelVal);
       $("#"+trimmedDelVal).load(location.href + " #"+trimmedDelVal);
       $("#"+trimmedDelVal).remove();
    });

    $(".delete-category").click(function(){
       var deleteVal = $(this).attr("data-category-name");
       articleRelModules.selectedCategories.splice( $.inArray(deleteVal,articleRelModules.selectedCategories) ,1 );
       $("#categoryRemovalModal").foundation('close');
       var trimmedDelVal = deleteVal.replace(" ", '');
       console.log(trimmedDelVal);
       $("#"+trimmedDelVal).load(location.href + " #"+trimmedDelVal);
       $("#"+trimmedDelVal).remove();
    });

    function getCustomTags(){
        var getTagsCallBacks = {
            "success": function(data){
                for(var i=0; i<data.tags.length; i++){
                    articleRelModules.articleTags.push(data.tags[i]);
                }
                for(var j=0; j< data.categories.length; j++){
                    articleRelModules.articleCategories.push(data.categories[j]);
                }
            },
            "error": function(data){

            }
        };
        window.pmprojectutils.getResponse('GET', '/api/article/get-article-rel-modules', {}, getTagsCallBacks, false)
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
        formData.append('tagsList', JSON.stringify(articleRelModules.selectedTags));
        formData.append('categoriesList', JSON.stringify(articleRelModules.selectedCategories));
        console.log(formData);
        //var formData = {
        //    "tags": articleRelModules.selectedTags,
        //    "categories": articleRelModules.selectedCategories
        //};
        var articleReviewCallBacks = {
            "success": function(data){
                $('#articlePostForm')[0].reset();
                $("#articleSuccessModal").foundation('open');
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
