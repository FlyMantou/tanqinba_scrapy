# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
conn = sqlite3.connect('tanqinba.db')
cursor = conn.cursor()
class TanqinbaPipeline(object):



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

        sql2 = '''
            insert into comment 
            (score_id, comment_user,comment_date,comment_content) 
            values 
            (:co_id, :co_user,:co_date,:co_content)
            '''

        row = cursor.execute("SELECT * from tanqinba WHERE piano_url=:piano_url",{'piano_url':item['url']})
        id = 0
        for r in row:
            id = r[0]
        cursor.execute(sql2,{'co_id':id,'co_user':item['commentUser'],'co_date':item['commentDate'],'co_content':item['commentContent']})
        conn.commit()

