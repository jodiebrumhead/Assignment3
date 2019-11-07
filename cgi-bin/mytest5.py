#!/usr/bin/env python3
import cx_Oracle
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<head>")
print("<title>The Crop Report</title>")
print("</head>")

print("<body>")
print("<h2>This is a text title</h2>")
conn = cx_Oracle.connect("student/train@geosgen")
c = conn.cursor()
c.execute("SELECT * FROM GISTEACH.CROPS")
print("<table style=\"width:100%;border:1px solid black\">")
print("<tr><th>","Reference","</th><th>","Veg","</th></tr>")
#print("<table>")
for row in c:
    print("<tr><td>",row[0],"</td>","-","<td>",row[1],"</td></tr>")
#print("<p>",row[0],"-<b>",row[1],"</b>-",row[2],"-",row[3],"</p>")
print("</table>")
conn.close()
print("</body>")
print("</html>")
print('<svg width="100" height="100">')
print('<circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />')
print('<rect x="1" y="1" width="14" height="14" stroke="green" />')
print("</svg>")
