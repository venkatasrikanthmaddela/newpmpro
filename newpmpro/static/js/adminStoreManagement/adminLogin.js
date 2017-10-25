$(document).ready(function (){
   $("#admin-log-in-form").submit(function e(){
       e.preventDefault();
   });
   $("#adminLoginButton").click(function(){
      var formData = new FormData($("#admin-log-in-form")[0]);
      var userDetails = {"email" : $("#email-id").val(), "password": $("#password").val() };
      var adminLoginCallBacks = {
          "success": function(data){
            window.location.href = "/store";
          },
          "error": function(data){
              console.log(data);
              alert("error");
          }
      };
      window.pmprojectutils.getResponse('POST', '/api/store/admin-login', formData, adminLoginCallBacks, true);
   });
});