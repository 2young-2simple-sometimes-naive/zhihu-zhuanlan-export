#!/usr/bin/env python

#install:
#pip install -U zhihu_oauth
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
from zhihu_oauth import ZhihuClient

client = ZhihuClient()
#client.login_in_terminal('-----$$$EMAIL$$$-----', '-----$$$PASSWORD$$$-----')
#client.save_token('token.pkl')

#"""
client.load_token('token.pkl')
outfile = "已订阅专栏.xml"
with open(outfile, 'w', encoding='utf-8') as output:
    output.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    output.write("<opml version=\"1.0\">\n")
    output.write("	<body>\n")

    me = client.me()
    columns = me.following_columns
    for column in columns:
        url = 'https://zhuanlan.zhihu.com/' + u"{}".format(column.id)
        name = u"{}".format(column.title)
        print(column.title  )
        #print(name"{}".format'utf-8', 'ignore'))
        output.write("		<outline text=\"" + name + "\" title=\"" + name + "\" type=\"rss\" xmlUrl=\"" + url + "\" htmlUrl=\"" + url + "\"/>" + '\n')
    output.write("	</body>\n")
    output.write("</opml>")
#"""
