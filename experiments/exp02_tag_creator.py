# Seeds Tags table

import mysql_config
import random
import exp02_util

fb_cursor = mysql_config.mysql_connection.cursor()
fb_cursor.execute("SELECT COUNT(*) FROM mestrado.post_all_pages_portugal_globo_pt")

NUMBER_OF_POSTS_ON_DB = fb_cursor.fetchall()[0][0]

def generate_tags_for_post(post_id):
	number_of_tags_for_this_post = random.choice(range(0,8)) #random between 1 and 5
	result = []
	for i in range(number_of_tags_for_this_post):
		result.append((post_id, exp02_util.random_tag_name(), exp02_util.random_tag_user()))
	return result


string =  "INSERT INTO mestrado.tags(post_id, tag_name, tag_user) values "

values = []

for post_id in range(0, NUMBER_OF_POSTS_ON_DB):
	values += generate_tags_for_post(post_id)

	if len(values) >= 50000:
		print "Inserindo..."
		insert_query = string + ", ".join(str(t) for t in values)
		fb_cursor.execute(insert_query)
		mysql_config.mysql_connection.commit()

		values = []

