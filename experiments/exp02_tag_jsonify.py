import exp02_util
import mysql_config
import time
import json

fb_cursor = mysql_config.mysql_connection.cursor()
print "Chamando MySQL"
fb_cursor.execute("SELECT id FROM mestrado.post_all_pages_portugal_globo_pt where tags is not null or tags = '' ORDER BY id DESC limit 1")
print "Dei o Execute"
result = fb_cursor.fetchall() 
print "Dei o fetchall	"
if result is ():
	LAST_IMPORTED_POST = 0
else:
	 LAST_IMPORTED_POST = result[0][0]
print " last:  " + str(LAST_IMPORTED_POST)

fb_cursor.execute("SELECT COUNT(*) FROM mestrado.post_all_pages_portugal_globo_pt")
NUMBER_OF_POSTS_ON_DB = fb_cursor.fetchall()[0][0]


query_list = []
while LAST_IMPORTED_POST != NUMBER_OF_POSTS_ON_DB - 1 :
	print "LAST_IMPORTED_POST: " + str(LAST_IMPORTED_POST)

	print "iterando a partir do id: %s " % LAST_IMPORTED_POST
	query_string = "SELECT * FROM mestrado.tags t where post_id > %s ORDER BY POST_ID ASC LIMIT 1000" % str(LAST_IMPORTED_POST)
	fb_cursor.execute(query_string)
	result = fb_cursor.fetchall()

	
	dict_of_tags_to_insert = {}
	for row in result:
		tag_dict = {}
		post_id = row[1]
		if not post_id in dict_of_tags_to_insert.keys() :
			dict_of_tags_to_insert[post_id] = []

		tag_dict["name"] =row[2]
		tag_dict["user"] = row[3]
		dict_of_tags_to_insert[post_id] = dict_of_tags_to_insert[post_id] + [tag_dict]
		LAST_IMPORTED_POST = post_id

	for key in dict_of_tags_to_insert.keys():
		query_list.append("UPDATE post_all_pages_portugal_globo_pt set tags = '%s' where id = %s" % (json.dumps(dict_of_tags_to_insert[key]), key))
		
		
	
	# tags.append(tag_dict)
	# print 
	# print "%s: %s" % (i, json.dumps(tags))
	# print "UPDATE post_all_pages_portugal_globo_pt set tags = %s where post_id = %s" % 
for query in query_list:
	fb_cursor.execute(query)
	mysql_config.mysql_connection.commit()