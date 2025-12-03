from rest_framework import permissions
#2.30----->Custom permissins 
class IsStaffEditorPermission(permissions.DjangoModelPermissions):

     perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
     #So this can be achieved more simply by having (--->views.py line 20).Setting precedence in terms 
     #of access 
    #  def has_permission(self, request, view):
    #       if not request.user.is_staff:
    #            return False
    #       return super().has_permission(request, view)

    #----------------------------------------------

    # def has_permission(self, request, view):
    #     user=request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("products.add_product") :return True#app-name.verb_model_name
    #         if user.has_perm("products.change_product"):return True
    #         if user.has_perm("products.delete_product"):return True
    #         if user.has_perm("products.view_product"):return True
    #         return True
    #     return False

    #3.07---->Moved the permissions.py from products dir  into the api dir to persist it across the system.
    #In this way it can be accessed and used by any view that needs it 