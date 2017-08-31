from datetime import datetime
from django.contrib.admin import forms
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django_mysql.models import ListCharField

from newpmpro.baseModels import CustomModel
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(UserManager, BaseUserManager):
    def create_user(self, username, email, password, phone_number, is_staff=False, is_subscribed=False):

        user = self.model(
            email=CustomUserManager.normalize_email(email),
            username=username,
            first_name="",
            last_name="",
            is_staff=is_staff,
            is_active=True,
            mobileNumber=phone_number,
            isSubscribed=is_subscribed
        )
        user.set_password(password)
        user.save()
        return user


class PmUser(AbstractBaseUser, CustomModel, PermissionsMixin):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=25, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=datetime.utcnow())
    last_login = models.DateTimeField(_('last login'), blank=True, default=datetime.utcnow())
    is_staff = models.BooleanField(
        _('staff status'),
        default=False
    )
    is_active = models.BooleanField(
        _('active'),
        default=True
    )
    mobileNumber = models.CharField(max_length=25)
    isSubscribed = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['username', 'mobileNumber']
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def get_short_name(self):
        return self.first_name


auth_models.User = PmUser


class UserSources(CustomModel):
    user = models.ForeignKey(PmUser)
    sources = models.CharField(max_length=25)


class PartnerDetails(CustomModel):
    instituteName = models.CharField(max_length=25)


class ProjectData(CustomModel):
    projectTitle = models.CharField(max_length=25)
    projectCategory = models.CharField(max_length=25)
    projectType = models.CharField(max_length=25)
    projectLanguage = models.CharField(max_length=25)
    ieePaper = models.BooleanField(default=False)
    projectAbstract = models.TextField()
    projectFrameWork = models.CharField(max_length=25)
    projectOwner = models.ForeignKey(PartnerDetails)
    isActive = models.BooleanField(default=True)
    projectStatus = models.CharField(max_length=25, default="PROJECT UPLOADED")


class ProjectIdeas(CustomModel):
    user = models.ForeignKey(PmUser)
    projectInfo = models.ForeignKey(ProjectData)
    projectIdeaStatus = models.CharField(max_length=25, default='IDEA RECEIVED')

    def __str__(self):
        return "user-email : {}, title : {}, category: {}, projectType : {}, Language : {}, Status : {}".\
            format(self.user.email,self.projectLanguage, self.projectIdeaStatus)


class Article(CustomModel):
    title = models.TextField()
    subTitle = models.TextField(default="NA")
    content = models.TextField()
    codePart = models.TextField(default="NA")
    author = models.ForeignKey(PmUser)
    isActive = models.BooleanField(default=True)


class ProjectRequests(CustomModel):
    user = models.ForeignKey(PmUser)
    projectInfo = models.ForeignKey(ProjectData)
    projectRequestStatus = models.CharField(max_length=25, default='REQUESTED')


class Categories(CustomModel):
    articleId = models.ForeignKey(Article)
    name = models.CharField(max_length=256)


class Tags(CustomModel):
    articleId = models.ForeignKey(Article)
    tagName = models.CharField(max_length=256)


class HyperLinks(CustomModel):
    articleId = models.ForeignKey(Article)
    linkName = models.TextField()
    link = models.URLField()


class ArticleFeedBack(CustomModel):
    article = models.ForeignKey(Article, default=None)
    user = models.ForeignKey(PmUser, default=None)
    likeCount = models.IntegerField(default=0)





