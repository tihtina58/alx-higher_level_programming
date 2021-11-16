Databases
What are databases?
First, what are databases for?

Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology re using is stateless or stateful, you will need to persist your data somewhere. s what databases are for.

Then, why not store your data in flat files, as you did in Relational databases, done  project? A solid database is expected to be acid, which means it guarantees:

Atomicity: transactions are atomic, which means if a transaction fails, the result will be like it never happened.
Consistency: you can define rules for your data, and expect that the data abides by the rules, or else the transaction fails.
Isolation: run two operations at the same time, and you can expect that the result is as though they were ran one after the other. s not the case with the JSON file storage you built: if 2 insert operations are done at the same time, the later one will fetch an outdated collection of users because the earlier one is not finished yet, and therefore overwrite the file without the change that the earlier operation made, totally ignoring that it ever happened.
Durability: unplug your server at any time, boot it back up, and it t lose any data.
Also, a solid database will provide strong performance (because I/O is your bottleneck and databases are I/O, so their performance makes a whole lot more of a difference than the performance of your s code) and scalability (inserting one user in a collection of 5 users should take about the same time as inserting one user in a collection of 5 billion users).

ACID is a cool acronym! CRUD is another cool one
You will definitely run into the concept  operations. s just a fancy way to refer to the 4 operations that can be performed on the data itself:

Create some data;
Read some data;
Update some data;
Destroy some data.
Obviously, a database should allow all four. Yes, s it.

2+ kinds of databases
When people talk about databases, re usually referring to relational databases (such as PostgreSQL, MySQL, 
Engineers that are comfortable with SQL are very respected in the industry, even more so in this age where data has gotten so valuable. To be honest, the fact that I aced the SQL challenge on my Apple interview is probably a huge reason for me to have gotten the job; it turns out the initial role was a lot about manipulating data.
The fear of SQL explains a lot why non-relational databases got , a bit like if it was a statement, a complain. Non-relational databases push a lot the button of not having to use SQL.
Modern full-fledged frameworks contain tools that are called ORMs, and one of their roles is to abstract away SQL queries (which is good for day-to-day ease of use, but can turn out very dangerous). ll cover ORMs more later, but s worth noting that you do find back-end engineers in the industry who work with relational databases, but never write a line of SQL, which makes them a lot less valuable on a project.
For a beginner, keep in mind that s syntax is a bit hard to wrap your head around, so maybe you should follow a tutorial first. Please t try to memorize the SQL syntax. ve used SQL extensively in very advanced cases, on systems with hundreds of millions of records, and I still go on Google each time I need to compose a SQL query.
Some terminology around relational databases
One good thing about relational databases is that whether re PostgreSQL, MySQL, Oracle, or other, ve managed to be pretty consistent across brands. Therefore, not only are their versions of SQL pretty decently similar (at least for CRUD operations), but the terminology re using are mostly the same.

Say you need to store users. To do that, you create a table that is .

Your users have 3 pieces of information to store: , , and . Those are called columns, and they all have types, like integer for , varchar(32)  (a string of variable length, but maximum 32), and char(32) (a string of exactly 32 characters, which is the case for all text encrypted with the md5 algorithm, for instance). The available types may vary heavily from one  to the other.

Now, s add a user in the database with SQL:

INSERT INTO users (login, password) VALUES ('rudy', '01234567890123456789012345678901');
This adds a row in the table (sometimes also refered to as a record, or more rarely, a tuple).

Why are they  databases?
Historically, the initial reason was that tables used to be  (they gather a lot of datas that  to each other, since they follow the same structure). However, tables are now tables, and the  has now been recycled for another use.

A relation as used today is something that ties two records together, most often across different tables. For instance, say you have a blog, and you have 2 tables:

posts, with the fields id, title and body
comments, with the fields id and body
In both tables,  fields are primary keys, because they uniquely identify the row that they belong to (if you give me the post of id , re sure to be getting only one post).

But how do you know that a given comment is attached to a given post. Well, you add a postid field to the comments table, containing the id of the post you with to attach it to. The postid field is called a foreign key, uniquely identifying s table primary key.

Now that you have that, you can easily identify, from a comment, which post it is attached to; but you can also easily identify, from a post, which comments are attached to it. Just fetch the comments whose post_id field contain the id of the post you had in mind. The fact that you can do that is what is called a relation.

Once you have your relation, you can do pretty advanced things. For instance, you can join tables together while querying them, which will allow you to search the comments whose posts were published within the last , for instance (well, provided the posts table has a published_at column of type date, for instance).

Note: you can have a relation between rows of the same table, for instance, a user that is  of another one, a comment that is  of another one, replya sponsorthe monthfor anotheryou4say idthe relationterm relatedare relationscalled relationalcalled letbranddatabase loginfor idthe passwordtheir logintheir idtheir userscalled theytheytheyIdonSQLitWeNoSQLcalled Oracle, theythatItCRUDof applicationdidnThatwrongthe Thatyouyou