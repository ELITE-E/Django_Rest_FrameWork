from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_class=[permissions.IsAdminUser,IsStaffEditorPermission]


#3.07----->This allows the permission to persist across the entire application,therefore accessible
#to any view that needs it .