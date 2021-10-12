File Reading and Writing Methods
<< Previous Note           Next Note >>
   On this page: open(), file.read(), file.readlines(), file.write(), file.writelines().
Before proceeding, make sure you understand the concepts of file path and CWD. If you run into problems, visit the Common Pitfalls section at the bottom of this page.
Opening and Closing a "File Object"
As seen in Tutorials #12 and #13, file IO (input/output) operations are done through a file data object. It typically proceeds as follows:
Create a file object using the open() function. Along with the file name, specify:
'r' for reading in an existing file (default; can be dropped),
'w' for creating a new file for writing,
'a' for appending new content to an existing file.
Do something with the file object (reading, writing).
Close the file object by calling the .close() method on the file object.
Below, myfile is the file data object we're creating for reading. 'alice.txt' is a pre-existing text file in the same directory as the foo.py script. After the file content is read in, .close() is called on myfile, closing the file object.
myfile = open('alice.txt', 'r')     # Reading. 'r' can be omitted
# ... read from myfile ...
myfile.close()                      # Closing file
foo.py
Below, myfile is opened for writing. In the second instance, the 'a' switch makes sure that the new content is tacked on at the end of the existing text file. Had you used 'w' instead, the original file would have been overwritten.
myfile = open('results.txt', 'w')   # The file is newly created where foo.py is
# ... write to myfile ...
myfile.close()                      # Closing file. VERY IMPORTANT!

myfile = open('results.txt', 'a')   # 'a': appending instead of overwriting.
# ... add text to the file ...
myfile.close()                      # Closing file. DON'T FORGET!
foo.py 
There is one more piece of crucial information: encoding. Some files may have to be read as a particular encoding type, and sometimes you need to write out a file in a specific encoding system. For such cases, the open() statement should include an encoding spcification, with the encoding='xxx' switch:
myfile = open('alice.txt', encoding='utf-8')     # Reading a UTF-8 file; 'r' is omitted


myfile = open('results.txt', 'w', encoding='utf-8')   # File will be written in UTF-8

foo.py
Mostly, you will need 'utf-8' (8-bit Unicode), 'utf-16' (16-bit Unicode), or 'utf-32' (32-bit), but it may be something different, especially if you are dealing with a foreign language text. Here is a full list of encodings.

Reading from a File
OK, we know how to open and close a file object. But what are the actual commands for reading? There are multiple methods.

First off, .read() reads in the entire text content of the file as a single string. Below, the file is read into a variable named marytxt, which ends up being a string-type object. Download mary-short.txt and try out yourself.
      
>>> f = open('mary-short.txt')
>>> marytxt = f.read()             # Using .read()
>>> f.close()
>>> marytxt
'Mary had a little lamb,\nHis fleece was white as snow,\nAnd everywhere that Mary 
went,\nThe lamb was sure to go.\n'
>>> type(marytxt)                  # marytxt is string type
<type 'str'>
>>> len(marytxt)                   # marytxt has 110 characters
110
>>> print(marytxt[0])
M
Next, .readlines() reads in the entire text content of the file as a list of lines, each terminating with a line break. Below, you can see marylines is a list of strings, where each string is a line from mary-short.txt.
      
>>> f = open('mary-short.txt')
>>> marylines = f.readlines()      # Using .readlines()
>>> f.close()
>>> marylines
['Mary had a little lamb,\n', 'His fleece was white as snow,\n', 'And everywhere 
that Mary went,\n', 'The lamb was sure to go.\n']
>>> type(marylines)                # marylines is list type
<type 'list'>
>>> len(marylines)                 # marylines has 4 lines
4
>>> print(marylines[0])
Mary had a little lamb,

Lastly, rather than loading the entire file content into memory, you can iterate through the file object line by line using the for ... in loop. This method is more memory-efficient and therefore recommended when dealing with a very large file. Below, bible-kjv.txt is opened, and any line containing smite is printed out. Download bible-kjv.txt and try out yourself.
f = open('bible-kjv.txt')     # This is a big file
for line in f:                # Using 'for ... in' on file object
    if 'smite' in line: 
        print(line,)                # ',' keeps print from adding a line break

f.close()
foo.py

Writing to a File
Writing methods also come in a pair: .write() and .writelines(). Like the corresponding reading methods, .write() handles a single string, while .writelines() handles a list of strings.

Below, .write() writes a single string each time to the designated output file:
       
>>> fout = open('hello.txt', 'w')
>>> fout.write('Hello, world!\n')                # .write(str)
>>> fout.write('My name is Homer.\n')
>>> fout.write("What a beautiful day we're having.\n")
>>> fout.close()
This time, we have tobuy, a list of strings, which .writelines() writes out at once:
     
>>> tobuy = ['milk\n', 'butter\n', 'coffee beans\n', 'arugula\n']
>>> fout = open('grocerylist.txt', 'w')
>>> fout.writelines(tobuy)                      # .writelines(list)
>>> fout.close()
Note that all strings in the examples have the line break '\n' at the end. Without it, all strings will be printed out on the same line, which is what was happening in Tutorial 13. Unlike the print statement which prints out a string on its own new line, writing methods will not tack on a newline character -- you must remember to supply '\n' if you wish a string to occupy its own line.

Common Pitfalls
File I/O is notoriously fraught with stumbling blocks for beginning programmers. Below are the most common ones.

"No such file or directory" error
    
>>> f = open('mary-short.txt')
Traceback (most recent call last):
  File "", line 1, in 
IOError: [Errno 1] No such file or directory: 'mary-short.txt'
You are getting this error because Python failed to locate the file for reading. Make sure you are supplying the correct file path and name. Read first File Path and CWD. Also, refer to this, this and this FAQ.

Issues with encoding
       
>>> f = open('mary-short.txt')    # need encoding='utf-8'
>>> marytxt = f.read()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    marytxt = f.read()
  File "C:\Program Files (x86)\Python35-32\lib\encodings\cp1252.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 36593: character 
maps to <undefined> 
"UnicodeDecodeError" means you have a file encoding issue. Each computer has its own system-wide default encoding, and the file you are trying to open is encoded in something different, most likely some version of Unicode. If this happens, you should specify the encoding using the encoding='xxx' switch while opening the file. If you are not sure which encoding to use, try 'utf-8', 'utf-16', and 'utf-32'.

Entire file content can be read in only ONCE per opening
       
>>> f = open('mary-short.txt')
>>> marytxt = f.read()           # Reads in entire file content
>>> marylines = f.readlines()    # Nothing left to read, returns nothing
>>> f.close()
>>> len(marytxt)
110
>>> len(marylines)     # marylines is empty!
0
Both .read() and .readlines() come with the concept of a cursor. After either command is executed, the cursor moves to the end of the file, leaving nothing more to read in. Therefore, once a file content has been read in, another attempt to read from the file object will produce an empty data object. If for some reason you must read the file content again, you must close and re-open the file.

Only the string type can be written
     
>>> pi = 3.141592
>>> fout = open('math.txt', 'w')
>>> fout.write("Pi's value is ")
>>> fout.write(pi)                # trying to write float, doesn't work
Traceback (most recent call last):
  File "", line 1, in 
TypeError: expected a character buffer object
>>> fout.write(str(pi))          # turn number into string using str()  
>>> 
Writing methods only works with strings: .write() takes a single string, and .writelines() takes a list which contains strings only. Non-string type data must be first coerced into the string type by using the str() function.

Your output file is empty
 
output.txt
This happens to everyone: you write something out, open up the file to view, only to find it empty. In other times, the file content may be incomplete. Curious, isn't it? Well, the cause is simple: YOU FORGOT .close(). Writing out happens in buffers; flushing out the last writing buffer does not happen until you close your file object. ALWAYS REMEMBER TO CLOSE YOUR FILE OBJECT