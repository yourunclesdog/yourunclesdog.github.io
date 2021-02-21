from datetime import datetime

now = datetime.now()
print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M")

f = open("posts.html", "r")
makebackup = f.read()
f.close()

f = open("backup.html", "w")
f.write(makebackup)
f.close()

f = open("mobile/posts.html", "r")
makebackup = f.read()
f.close()

f = open("mobile/backup.html", "w")
f.write(makebackup)
f.close()

f = open("posts.html", "r")
empty = 0
startoffile = ""
while empty != 80:
    startoffile = startoffile + f.readline()
    empty = empty + 1
endoffile = f.read()
print(startoffile)
print(endoffile)
f.close()

f = open("mobile/posts.html", "r")
emptym = 0
startoffilem = ""
while emptym != 76:
    startoffilem = startoffilem + f.readline()
    emptym = emptym + 1
endoffilem = f.read()
print(startoffilem)
print(endoffilem)
f.close()


message = input("What would you like to post? ")
imageyn = input("Would you like to post an image y/n ? ")
if imageyn == "y":
    image = input("Provide the file name of the image: ")
    imagepart = ("\n<img class=\"post\" src=\""+image+"\">")
    imagepartm = ("\n<img class=\"post\" src=\"../"+image+"\">")
else:
    imagepart = ("")
    imagepartm = ("")
datetime = ("\n<div>\n<h2>"+ dt_string+"</h2>")
post = ("\n<p>"+message+"</p>\n</div>\n")

f = open("posts.html", "w")
f.write(startoffile+datetime+imagepart+post+endoffile)
f.close()

f = open("mobile/posts.html", "w")
f.write(startoffilem+datetime+imagepartm+post+endoffilem)
f.close()

