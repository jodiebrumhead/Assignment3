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
for row in c:
    print(row[0],"-",row[1])
print("<p>",row[0],"-<b>",row[1],"</b>-",row[2],"-",row[3],"</p>")
conn.close()
print("</body>")
print("</html>")
print("Hello World!")
print("This is my first Python script!")
