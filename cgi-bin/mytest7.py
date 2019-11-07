#!/usr/bin/env python3
import cx_Oracle
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<head>")
print("<title>SVG Example</title>")
print("</head>")

print("<body>")

print('<svg width="10cm" height="10cm" viewBox="0 0 16 16">')
print('<rect x="1" y="7" width="5" height="5" fill="red" stroke="black" stroke-width="0.5" />')
print('<circle cx="13" cy="3" r="3" fill="yellow" />')

print('</svg>')

print("</body>")
print("</html>")
