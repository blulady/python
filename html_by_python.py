#https://www.w3schools.com/python/python_file_write.asp
#https://docs.python.org/3/library/webbrowser.html
import webbrowser


#https://www.w3schools.com/python/python_file_write.asp


f = open("htmlbypython.html", "w")
f.write ("\
<html>\
            <body>\
                    <h1>\
                        Stay tuned for our amazing summer sale!\
                    </h1>\
            </body>\
</html>")

f.close()

f = open("htmlbypython.html","r")
print(f.read())

url = 'file:///C:/Users/Sarah/AppData/Local/Programs/Python/Python38-32/htmlbypython.html'
webbrowser.open_new_tab(url)


