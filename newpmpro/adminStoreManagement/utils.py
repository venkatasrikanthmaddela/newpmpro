from articleManagement.models import ArticleRequests
from newpmpro.models import PmUser, ProjectIdeas


def get_defaults_for_dashboard():
    default_statistics = dict(userCount=0, articleRequests=0, newProjectIdeas=0)
    try:
        default_statistics["userCount"] = PmUser.objects.all().count()
        default_statistics["articleRequests"] = ArticleRequests.objects.filter(requestStatus='REQUESTED').count()
        default_statistics["newProjectIdeas"] = ProjectIdeas.objects.filter(projectIdeaStatus='IDEA RECEIVED').count()
    except:
        "error"
    return default_statistics
