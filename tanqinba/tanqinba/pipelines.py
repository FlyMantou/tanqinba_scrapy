# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
conn = sqlite3.connect('tanqinba.db')
cursor = conn.cursor()
class TanqinbaPipeline(object):

    #def __init__(self):
        #cursor.execute('create table tanqinba (id INTEGER primary key AUTOINCREMENT, piano_url varchar(20),'
                     # 'piano_name varchar(20),piano_des varchar(800),piano_singer varchar(20),'
                      #'piano_seeNum varchar(20),piano_collectNum varchar(20),piano_hard varchar(20),'
                      #'piano_uploadUser varchar(20),piano_uploadTime varchar(20))')

    def process_item(self, item, spider):

        print(item)
        print('正在保存信息至数据库')
        sql = '''
            insert into tanqinba 
            (piano_url, piano_name,piano_des,piano_singer,piano_seeNum,piano_collectNum,piano_hard,piano_uploadUser,piano_uploadTime) 
            values 
            (:pi_url, :pi_name,:pi_des,:pi_singer,:pi_seeNum,:pi_collectNum,:pi_hard,:pi_uploadUser,:pi_uploadTime)
            '''
        cursor.execute(sql,{'pi_url':item['url'],'pi_name':item['name'],'pi_des':item['des'],'pi_singer':item['singer'],'pi_seeNum':item['seeNum'],'pi_collectNum':item['collectNum'],'pi_hard':item['hard'],'pi_uploadUser':item['user'],'pi_uploadTime':item['time']})

        conn.commit()

