
from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    message = "必须是SVIP才能访问"
    def has_permission(self,request,view):
        if request.user.user_type != 1:
            return False
        return True