#.gif done
#.jpg done
#.jpeg done
#.png done
#.pdf done
#.txt done
#.zip
#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
# reference

file = input("input")
file = file.lower()

if ".gif" in file:
    print("image/gif")
elif ".jpg" in file or ".jpeg" in file:
    print("image/jpeg")
elif ".png" in file:
    print("image/png")
elif ".pdf" in file:
    print("application/pdf")
elif ".txt" in file:
    print("text/plain")
elif ".zip" in file:
    print("application/zip")
else:
    print("application/octet-stream")
