import sqlite3
conn = sqlite3.connect('tanqinba.db')
cursor = conn.cursor()

row = cursor.execute("SELECT * from comment")

f = open('3.txt', 'w', encoding='utf-8')
i = 0
for r in row:
    item = r[4]
    item = item.replace('\n','').replace('\t','').replace(' ','')
    if item != "":
        item = item.replace('###',"\n")
        f.write(item)
        print("%d---------%s" % (i,item))
    i = i+1