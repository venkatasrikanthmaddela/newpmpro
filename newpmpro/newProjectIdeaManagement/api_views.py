from rest_framework.response import Response
from rest_framework.views import APIView


class SaveProjectIdea(APIView):
    def post(self, request):
        projectTitle = request.data.get("projectTitle")
        request.data.get("projectCategory")
        request.data.get("projectType")
        request.data.get("projectLanguage")
        request.data.get("ieePaper")
        request.data.get("projectAbstract")
        

        return Response({"result": "success"}, 200)