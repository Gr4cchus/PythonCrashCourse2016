from user import User
from admin import Admin, Privileges

admin0 = Admin('john', 'doe')
admin0.privileges.show_privileges()
