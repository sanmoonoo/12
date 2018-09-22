import memcache

#创建memcached链接

m = memcache.Client(['127.0.0.1:11211'],debug=True)

#在memchche中添加数据
#set如果没有的话添加,如果有的话覆盖
#add 如果没有添加,有的话报错
#replace 如果没有报错,如果有覆盖

#key,val,time
m.set('name','zhangsan',time=200)

print(m.get('name'))
m.delete('name')
print(m.get('name'))
