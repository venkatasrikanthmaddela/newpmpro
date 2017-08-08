from rest_framework.response import Response
from rest_framework.views import APIView

from newpmpro.models import ProjectRequests, PmUser, ProjectData


class RequestForProject(APIView):
    def post(self, request):
        try:
            project_id = request.data.get("projectId")
            user_email = request.user.email
            requested_projects = ProjectRequests.objects.filter(user__email=user_email).values_list('projectInfo__id', flat=True)
            if long(project_id) in requested_projects:
                return Response({"result": "You have already Requested for this project"}, 500)
            else:
                project_request = ProjectRequests.objects.create(user=PmUser.objects.get(email=user_email),
                                               projectInfo=ProjectData.objects.get(id=project_id),
                                               projectRequestStatus="REQUESTED")
                project_request.save()
                return Response({"result": "success"}, 200)
        except:
            return Response({"result": "something went wrong. please try again"}, 500)
