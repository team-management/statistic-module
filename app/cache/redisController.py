import redis

redis_conn = {}

def createRedisConnection():
    """[Generates a redis client ]
    """ 
    global redis_conn
    pool = redis.ConnectionPool(host="redis-dev")
    #redis_conn = redis.Redis(connection_pool=pool) 
    #for docker-compose test
    redis_conn = redis.Redis( connection_pool=pool) 
    redis.Redis(host)
    return

def getKeyValue(key):
    """Retrieves key value from redis database
    
    Arguments:
        key {[string]} -- [key]
        
    """
    if not redis_conn:
        createRedisConnection()
    value = redis_conn.get(key)
    if value is None:
        raise Exception("There is not any entry with key '" + key + "'")
    return value.decode('utf-8')

def setKeyValue(key, value, override):
    """Sets a key value pair in redis database
    
    Arguments:
        key {[string]} -- [key]
        
    """
    if redis_conn is None:
        createRedisConnection()
    
    checkValue = redis_conn.get(key)

    if checkValue is not None and override is False:
        raise Exception("The key-value pair already exists")
    if checkValue is not None and override is True:
        #TODO: Console log de que el valor ha sido sobreescrito
        return redis_conn.set(key, value.encode('utf-8'))
    
    else:
        return redis_conn.set(key, value.encode('utf-8'))



def test():
    #print(setKeyValue("test", "foo"))
    print(getKeyValue("foo").decode("utf-8"))
    return

#test()