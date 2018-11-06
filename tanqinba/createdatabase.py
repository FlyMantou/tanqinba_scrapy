import sqlite3
conn = sqlite3.connect('tanqinba.db')
cursor = conn.cursor()


cursor.execute('create table tanqinba (id INTEGER primary key AUTOINCREMENT, piano_url varchar(20),'
     'piano_name varchar(20),piano_des varchar(800),piano_singer varchar(20),'
    'piano_seeNum INTEGER,piano_collectNum INTEGER,piano_hard INTEGER,'
    'piano_uploadUser varchar(20),piano_uploadTime varchar(20),piano_comment varchar(255))')

cursor.execute('create table comment (id INTEGER primary key AUTOINCREMENT, score_id INTEGER,'
               'comment_user varchar(20),comment_date varchar(255),comment_content varchar(20))')

cursor.close()