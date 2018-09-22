class Role(object):
    VISITOR = 1
    COMMON_USER = 2
    VIP_USER=4
    VVIP_USER = 8
    SUPER_VIP = 16

class user(object):
    def __init__(self,name,role):
        self.name =name
        self.role = role

def Vvip(user,)