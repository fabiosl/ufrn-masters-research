import exp02_util
import mysql_config
import time

fb_cursor = mysql_config.mysql_connection.cursor()
print "After indexes creation: "
for i in range(50):
	string = "SELECT COUNT(*) FROM mestrado.tags where tag_user=\"%s\" and tag_name=\"%s\"" % (exp02_util.random_tag_user(), exp02_util.random_tag_name())
	start_time = time.time()
	fb_cursor.execute(string)
	end_time =  time.time() - start_time
	print string + ": " + str(end_time) + " segundos."

# fabiosl@macpro ~/workspace/ufrn-masters-research/experiments (master) $ python exp02_mysql_query_analyzer.py 
# Before indexes creation: 
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Aaron" and tag_name="that": 4.36646914482 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adriana" and tag_name="by": 4.17953705788 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Addie" and tag_name="state": 4.15578484535 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelaide" and tag_name="generated": 4.26236796379 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abbie" and tag_name="by": 4.29976797104 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agnus" and tag_name="instances": 4.16232895851 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrianna" and tag_name="are": 4.16953802109 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrianne" and tag_name="instantiate": 4.16423201561 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agnes" and tag_name="overlap": 4.29492998123 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abigail" and tag_name="different": 4.17712306976 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustina" and tag_name="method": 4.22342896461 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Aaron" and tag_name="creating": 4.11923789978 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adriane" and tag_name="thread": 4.17500519753 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustin" and tag_name="that": 4.15130090714 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adena" and tag_name="a": 4.24540901184 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelaide" and tag_name="module": 4.19979906082 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adeline" and tag_name="the": 4.18936109543 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agatha" and tag_name="for": 4.20446705818 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrianna" and tag_name="bound": 4.16348409653 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adriane" and tag_name="the": 4.19786405563 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agnes" and tag_name="multithreaded": 4.2379899025 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Ahmed" and tag_name="functions": 4.141477108 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abbie" and tag_name="useful": 4.15231204033 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abe" and tag_name="own": 4.13311886787 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adaline" and tag_name="share": 4.16168403625 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustina" and tag_name="to": 4.19956302643 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrienne" and tag_name="functions": 4.16526889801 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Ahmad" and tag_name="that": 4.16510391235 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abby" and tag_name="dont": 4.91354990005 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adah" and tag_name="to": 4.37314915657 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abby" and tag_name="own": 4.19593310356 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abraham" and tag_name="by": 4.19499993324 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Ada" and tag_name="own": 4.15051102638 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adriene" and tag_name="programs": 4.13018703461 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelaide" and tag_name="method": 4.15579915047 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adaline" and tag_name="useful": 4.13608503342 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abdul" and tag_name="class": 4.1275601387 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abe" and tag_name="module": 4.14355111122 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adolph" and tag_name="functions": 4.14006209373 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adele" and tag_name="that": 4.19601798058 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustina" and tag_name="seen": 4.11279678345 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelle" and tag_name="using": 4.1818459034 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adeline" and tag_name="This": 4.15157008171 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Aaron" and tag_name="the": 4.22977995872 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelia" and tag_name="share": 4.15000104904 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agatha" and tag_name="generated": 4.14664101601 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Addie" and tag_name="each": 4.17273402214 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adan" and tag_name="Random": 4.14763307571 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Afton" and tag_name="hidden": 4.13704395294 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adele" and tag_name="the": 4.20750379562 segundos.


# Executing:
# ALTER TABLE `mestrado`.`tags` 
# ADD INDEX `tag_name` (`tag_name` ASC),
# ADD INDEX `tag_user` (`tag_user` ASC),
# ADD INDEX `name_user` (`tag_name` ASC, `tag_user` ASC);

# SQL script was successfully applied to the database.



# fabiosl@macpro ~/workspace/ufrn-masters-research/experiments (master) $ python exp02_mysql_query_analyzer.py 
# After indexes creation: 
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Addie" and tag_name="to": 0.234026193619 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adan" and tag_name="random.Random": 0.281204938889 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustina" and tag_name="of": 0.254233837128 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adam" and tag_name="thread": 0.245181083679 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adriana" and tag_name="is": 0.316114187241 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abraham" and tag_name="dont": 0.307112932205 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adam" and tag_name="method": 0.24186706543 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abigail" and tag_name="generated": 0.234393119812 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abby" and tag_name="are": 0.342766046524 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agueda" and tag_name="the": 0.236221075058 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustina" and tag_name="dont": 0.278964042664 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustin" and tag_name="thread": 0.311532020569 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Aaron" and tag_name="using": 0.302842140198 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adela" and tag_name="a": 0.234228849411 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agnus" and tag_name="hidden": 0.232814073563 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrienne" and tag_name="generated": 0.239733934402 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Aaron" and tag_name="each": 0.262207984924 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelle" and tag_name="the": 0.242733001709 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agatha" and tag_name="dont": 0.232794046402 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Afton" and tag_name="get": 0.235485076904 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agustin" and tag_name="and": 0.232353925705 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrian" and tag_name="actually": 0.237640857697 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abbie" and tag_name="instances": 0.238816976547 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Ada" and tag_name="sequences": 0.27033996582 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adah" and tag_name="hidden": 0.234536170959 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abram" and tag_name="multithreaded": 0.235674858093 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adan" and tag_name="each": 0.23263502121 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adolph" and tag_name="for": 0.234091043472 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adriana" and tag_name="likely": 0.236845970154 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelia" and tag_name="the": 0.234643936157 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelia" and tag_name="class": 0.23179101944 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Ahmad" and tag_name="functions": 0.307506084442 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrien" and tag_name="the": 0.235261917114 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adell" and tag_name="that": 0.273354053497 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agatha" and tag_name="it": 0.24489402771 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adolfo" and tag_name="to": 0.232158899307 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adam" and tag_name="that": 0.264044046402 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adria" and tag_name="that": 0.247316122055 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Abe" and tag_name="are": 0.231909990311 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adrienne" and tag_name="creating": 0.316083908081 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adolph" and tag_name="by": 0.309193849564 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Addie" and tag_name="class": 0.232991933823 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adell" and tag_name="is": 0.235455036163 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agnus" and tag_name="for": 0.232788085938 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adelle" and tag_name="a": 0.232937812805 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adria" and tag_name="this": 0.233861923218 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Agnes" and tag_name="the": 0.234441995621 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adela" and tag_name="of": 0.258213043213 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adriene" and tag_name="Random": 0.239457130432 segundos.
# SELECT COUNT(*) FROM mestrado.tags where tag_user="Adela" and tag_name="generated": 0.248536109924 segundos.
