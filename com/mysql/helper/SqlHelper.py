# --coding:utf-8--
from _mysql_exceptions import Error
from com.common.BaseLoggingObj import BaseLoggingObj
from com.common.BaseLoggingObj import logger
from com.mysql.MySqlConfig import MySqlConfig
import MySQLdb
import MySQLdb.cursors


class SqlHelper(BaseLoggingObj):
    @staticmethod
    def __fetchAll(cursor):
        data = cursor.fetchall()
        return data

    @staticmethod
    def __excute(cursor, command):
        if command == None:
            return []
        data = []
        for sql in command:
            cursor.execute(sql)
            d = SqlHelper.__fetchAll(cursor)
            data.append(d)
        return data

    '''
        config默认是MySqlConfig，可通过构造参数传入
    '''

    def __init__(self, config=MySqlConfig):
        BaseLoggingObj.__init__(self)

        self.hostName = config.hostName
        self.name = config.name
        self.db = config.db
        self.password = config.password
        self.charset = config.charset

    def doInternal(self, action, commond):
        data = None
        db = MySQLdb.connect(host=self.hostName, user=self.name, passwd=self.password, db=self.db,
                             cursorclass=MySQLdb.cursors.DictCursor, charset=self.charset)
        cursor = db.cursor()
        data = action(cursor, commond)
        db.commit()
        db.close()
        if data is not None:
            return data

    @staticmethod
    def getCon(host="127.0.0.1", user="root", passwd="123456", charset="utf8"):
        return MySQLdb.connect(host=host, user=user, passwd=passwd,
                               cursorclass=MySQLdb.cursors.DictCursor, charset=charset)

    def do(self, sql):
        try:
            self.doInternal(SqlHelper.__excute, sql)
            return True
        except Error, e:
            self.logging.error("insert error %s", e)
            return False

    @logger
    def insert(self, *sql):
        return self.do(sql)

    @logger
    def delete(self, *sql):
        return self.do(sql)

    @logger
    def update(self, *sql):
        return self.do(sql)

    @logger
    def select(self, *sql):
        return self.doInternal(SqlHelper.__excute, sql)
