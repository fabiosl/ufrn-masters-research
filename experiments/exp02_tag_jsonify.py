import exp02_util
import mysql_config
import time


fb_cursor = mysql_config.mysql_connection.cursor()
fb_cursor.execute("SELECT id FROM mestrado.post_all_pages_portugal_globo_pt where tags is not null ORDER BY id DESC")
result = fb_cursor.fetchall() 
if result is ():
	LAST_IMPORTED_POST = 0
else:
	 LAST_IMPORTED_POST = result[0][0]


fb_cursor.execute("SELECT COUNT(*) FROM mestrado.post_all_pages_portugal_globo_pt")
NUMBER_OF_POSTS_ON_DB = fb_cursor.fetchall()[0][0]



while LAST_IMPORTED_POST < 200: # NUMBER_OF_POSTS_ON_DB:
	print LAST_IMPORTED_POST
	print NUMBER_OF_POSTS_ON_DB
	print "LAST_IMPORTED_POST < NUMBER_OF_POSTS_ON_DB? " + str(LAST_IMPORTED_POST < NUMBER_OF_POSTS_ON_DB)

	print "iterando a partir do id: %s " % LAST_IMPORTED_POST
	query_string = "SELECT * FROM mestrado.tags t where post_id > %s ORDER BY POST_ID ASC LIMIT 1000" % str(LAST_IMPORTED_POST)
	fb_cursor.execute(query_string)
	result = fb_cursor.fetchall()

	# 1 -> [{"name": "bla", "user":"ble"}]
	# tags = {}
	
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
	print dict_of_tags_to_insert
	
		# tags.append(tag_dict)
	# print 
	# print "%s: %s" % (i, json.dumps(tags))
	# print "UPDATE post_all_pages_portugal_globo_pt set tags = %s where post_id = %s" % 