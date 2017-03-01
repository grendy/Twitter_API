import MySQLdb
import re
import settings
import time




class test:
    def __init__(self):
        # import pdb;pdb.set_trace()
        self.conn = MySQLdb.connect(
            host=settings.host1,
            port=settings.port1,
            user=settings.user,
            passwd=settings.passwd1,
            db=settings.db1)
        self.connect = self.conn
        self.con = MySQLdb.connect(
            host=settings.host,
            port=settings.port,
            user=settings.user,
            passwd=settings.passwd,
            db=settings.db)
        self.connect = self.con

    def parse(self):
        # import pdb;pdb.set_trace()
        malay = self.con.cursor()
        user = self.conn.cursor()
        try:
            # import pdb;pdb.set_trace()
            sql = "select screen_name from twitter_subs_temp"
            user.execute(sql)
            master = user.fetchall()
            itung1 = "select count(*)from twitter_subs_temp"
            user.execute(itung1)
            master_itung = user.fetchall()
            master_itung = str(master_itung).replace(",", "").replace("'", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("L", "")
            # sql1 = "select url from malaysia"
            # malay.execute(sql1)
            # slave = malay.fetchall()
            # itung = "select count(*)from malaysia"
            # malay.execute(itung)
            # slave_itung = malay.fetchall()
            # slave_itung = str(slave_itung).replace(",", "").replace("'", "").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("L", "")
            api = ''
            # import pdb;pdb.set_trace()
            for ulang_master in range(0,int(master_itung)):
                print ulang_master
                a = master[ulang_master]
                ambil_master = str(a).replace(",", "").replace("'", "").replace("(", "").replace(")", "")
                # ambil_master = 'https://www.facebook.com/' + ambil_master
                # import pdb;pdb.set_trace()
                try:
                    masuk_malay = "INSERT INTO `twitter_user`(`screen_name`,`api`) VALUES ('{}','{}') ".format(ambil_master,api)
                    malay.execute(masuk_malay)
                    self.con.commit()
                    print "==========================++++++++++++++================================"
                    print ambil_master
                    print "INSERT SUKSES INTO twitter"
                    print "==========================++++++++++++++================================"

                except:
                    try:
                        masuk_malay = "UPDATE twitter_user SET screen_name = '{}'".format(ambil_master)
                        malay.execute(masuk_malay)
                        malay.execute(masuk_malay)
                        self.con.commit()
                        print "==========================++++++++++++++================================"
                        print ambil_master
                        print "UPDATE SUKSES INTO twitter"
                        print "==========================++++++++++++++================================"
                    except:
                        print "=====================+++++====================="
                        print "DATA ALREADY UP TO DATE"
                        print "=====================+++++====================="
        except:pass
if __name__ == '__main__':
    p = test()
    p.parse()
