# from newpmpro.models import *
#
#
# class ProjectUtils:
#     def __init__(self):
#
#     def create_project(self, project_title, project_abstract, project_category, project_type, project_framework, project_language, **kwargs):
#         """
#         Returns project-id after successful insert of data
#         :param kwargs:
#         :return:
#         """
#         try:
#             for each_param in [project_title, project_abstract, project_category, project_type, project_framework, project_language]:
#                 if each_param is None:
#                    raise ValueError("Some parameters are missing")
#             for key, value in kwargs.iteritems():
#
#
#             ProjectData.objects.create(projectTitle=project_title, projectCategory=project_category, projectType=project_type,
#                                        projectLanguage=project_language, projectAbstract=project_abstract,
#                                        projectFrameWork=project_framework)
