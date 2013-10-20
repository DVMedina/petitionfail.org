#!/usr/bin/env python2.7
# coding:utf8
import os,bottle
from bottle import request, route, run, default_app, error, template, view
from bottle import install 
from bottle_sqlite import SQLitePlugin
from bottle import static_file
import sqlite3

install(SQLitePlugin(dbfile='/home/pluto/petitionfail.org/data.db'))

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/home/pluto/petitionfail.org/bootstrap')

@route('/')
def main():
    conn = sqlite3.connect('/home/pluto/petitionfail.org/data.db')
    c = conn.cursor()
    result = c.execute('select * from url order by id desc limit 10').fetchall()
    #result = c.execute('select * from data order by id desc').fetchall()
    c.close()
    return template('content',rows=result)

@route('/url')
def sub(db):
    conn = sqlite3.connect('/home/pluto/petitionfail.org/data.db')
    c = conn.cursor()
    result = c.execute('select * from url order by id desc limit 10').fetchall()
    c.close()
    return template('webref',rows=result)

@route('/report')
def sub():
    tip= ''
    return template('quicksub',tip=tip)

'''
6LdnjeUSAAAAAC_INOLxcxUDoAwsLGEcJmgyjDPd
http://bottlepy.org/docs/dev-cn/tutorial.html#request-data
https://developers.google.com/recaptcha/docs/verify
http://stackoverflow.com/questions/1440239/how-to-use-python-plugin-recaptcha-client-for-validation
http://captchas.net/sample/python/
http://www.ibm.com/developerworks/cn/linux/l-python-mechanize-beautiful-soup/
http://www.crummy.com/software/BeautifulSoup/bs4/doc/
'''

'''
http://zoomq.qiniudn.com/ZQScrapBook/ZqFLOSS/data/20101018141708/
http://www.cnblogs.com/yd1227/archive/2009/09/28/1575877.html
'''
from recaptcha.client import captcha
def bs4_gettitle(url):
    from bs4 import BeautifulSoup
    import urllib
    req = urllib.urlopen(url).read()
    webpage = BeautifulSoup(req)
    charset = webpage.original_encoding
    if charset == 'gbk' or charset=='gb2312' or charset =='windows-1252':
        webpage = BeautifulSoup( req,from_encoding="gb18030")
    else:
        webpage = BeautifulSoup(req,from_encoding="utf-8")
    return webpage.title.string

def gettitle(url):
    from BeautifulSoup import BeautifulSoup
    import urllib
    req = urllib.urlopen(url).read()
    webpage = BeautifulSoup(req)
    charset = webpage.originalEncoding
    if charset == 'gbk' or charset=='gb2312' or charset =='windows-1252':
        webpage = BeautifulSoup( req,fromEncoding="gb18030")
    else:
        webpage = BeautifulSoup(req,fromEncoding="utf-8")
    return webpage.title.string


@route('/report',method='POST')
def do_url():
    remoteip = request.environ.get('REMOTE_ADDR')
    try :
        url = request.forms.get("url")
        if  not (request.forms.get('recaptcha_challenge_field') and request.forms.get('recaptcha_response_field')):
            return template('quicksub',tip='请重输验证码')
        title = gettitle(url)
    except:
        return template('quicksub',tip='请重输网址')


    response = captcha.submit(
        request.forms.get('recaptcha_challenge_field'),
        request.forms.get('recaptcha_response_field'),
        '6LdnjeUSAAAAAC_INOLxcxUDoAwsLGEcJmgyjDPd',
        remoteip
    )
    if not response.is_valid:
        return template('quicksub',tip='验证码有误，请重新提交！')
    else :
        conn = sqlite3.connect('/home/pluto/petitionfail.org/data.db')
        c = conn.cursor()
        c.execute("insert into url (url,title,ip) values(?,?,?)",(url,title,remoteip))
        conn.commit()
        c.close()
        # sendmail
        from subprocess import call
        import os
        os.system('''/home/pluto/petitionfail.org/web2email.py -u petitionfail.org -p pf5201314 -f petitionfail.org@gmail.com -r petitionfail@googlegroups.com '''+url)
#        execmd=''' -u petitionfail.org -p pf5201314 -f petitionfail.org@gmail.com -r petitionfail@googlegroups.com ''',url
#        call([ '/home/pluto/petitionfail.org/web2email.py',execmd ])
        return template('quicksub',tip='提交成功！')

@error(404)
def error404(error):
    return template('404')

class StripPathMiddleware(object):
  def __init__(self, app):
    self.app = app
  def __call__(self, e, h):
    e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
    return self.app(e,h)

if __name__ == "__main__":
    # Interactive mode
    run(app=myapp)
    
else:
    # Mod WSGI launch
    bottle.debug(True)
    os.chdir(os.path.dirname(__file__))
    application = StripPathMiddleware(default_app())

