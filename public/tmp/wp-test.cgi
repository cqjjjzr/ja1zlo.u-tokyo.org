#!/usr/bin/python
# -*- coding: euc-jp -*-
 
import site
import cgi
import os
 
print "content-type: text/html\n\n"

print '<html>'
print '<body>'

# formで送信される方法を取得して出力してみる
if os.environ['REQUEST_METHOD'] == 'POST':
	print 'POST'
elif os.environ['REQUEST_METHOD'] == 'GET':
	print 'GET'
 
print '<br/>'
 
# 入力された値を出力する
form = cgi.FieldStorage()
if form.has_key('msg'):
	print '<h2>' + form['msg'].value + '</h2>'
 
print '<body>'
print '</html>'
