import memcache

mc = memcache.Client(['127.0.0.1:11211'],debug=True)

mc.set('foo','bar')

print(mc.get("foo"))

mc.replace('foo','')