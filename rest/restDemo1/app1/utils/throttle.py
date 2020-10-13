from rest_framework.throttling import BaseThrottle,SimpleRateThrottle
import time


class VisitThrottle(SimpleRateThrottle):
    scope = 'Luffy'

    def get_cache_key(self, request, view):
        return self.get_ident(request)

class UserThrottle(SimpleRateThrottle):
    scope = 'LuffyUser'

    def get_cache_key(self, request, view):
        return request.user.username

'''
VISIT_RECORD = {}

class VisitThrottle(BaseThrottle):
    
    # 60s内只能访问3次
    # 可以存到数据库，redis
    
    def __init__(self):
        self.history = None

    def allow_request(self,request,view):
        # 1.获取用户ip
        # remote_addr = request.META.get('REMOTE_ADDR')
        remote_addr = self.get_ident(request)
        print(remote_addr)
        ctime = time.time()
        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime,]
            return True
        history = VISIT_RECORD.get(remote_addr)
        self.history = history
        while history and history[-1] < ctime - 60:
            history.pop()

        if len(history) < 3:
            history.insert(0,ctime)
            return True

        return False  # False 访问频率太高，被限制

    def wait(self):
        # 需要等待多少秒
        ctime = time.time()
        second = 60 - (ctime - self.history[-1])
        return second
    
'''