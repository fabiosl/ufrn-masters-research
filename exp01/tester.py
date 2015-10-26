import random
import string
import time
import MySQLdb
import exp01_config
import urllib2

NUMBER_OF_ATTEMPTS_FOR_EACH_QUERY_LENGTH = 10


fb = MySQLdb.connect(
    host = exp01_config.mysql_host,
    user = exp01_config.mysql_user,
    passwd = exp01_config.mysql_passwd,
    db = exp01_config.mysql_schema
)
# you must create a Cursor object. It will let
#  you execute all the queries you need
fb_cursor = fb.cursor() 


def get_random_string_with_size(query_length):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(query_length))



def search_time_mysql(query_string):
    query_size = len(query_string)
    query_string = ''' "% ''' + query_string + '''% " '''
    start_time = time.time()
    fb_cursor.execute('SELECT COUNT(*) FROM mestrado.post_all_pages_portugal_globo_pt WHERE message like %s' % query_string)
    end_time =  time.time() - start_time
    return end_time


def search_time_elasticsearch(query_string):
    query_size = len(query_string)
    url = exp01_config.elasticsearch_url + "q=message:%s" % query_string
    start_time = time.time()
    urllib2.urlopen(url).read()
    end_time =  time.time() - start_time
    return end_time


mysql_queries = []
elasticsearch_queries = []
for query_length in [250, 150, 100, 50, 30, 20, 10, 5, 2]:
    for attempt in range(NUMBER_OF_ATTEMPTS_FOR_EACH_QUERY_LENGTH):
        query_string = get_random_string_with_size(query_length)
        
        mysql_queries.append((query_length,search_time_mysql(query_string)))
        elasticsearch_queries.append((query_length,search_time_elasticsearch(query_string)))
        print "MySQL Queries: %s" % mysql_queries
        print "ES Queries: %s" % elasticsearch_queries



