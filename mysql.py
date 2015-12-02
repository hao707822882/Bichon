__author__ = 'Administrator'

import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='mysql', port=3306)
    cur = conn.cursor()
    cur.execute('SELECT * FROM user')
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
