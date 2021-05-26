Alexander Jimenez

I am writing this just to explain some of the code I have written.

First and foremost, I did not regularly commit my code or preserve any commit history because I did not realize that was a requirement until it was too late, and I figured as long as I provide valid, clean code at the end, 
it would be easy to track my progress through my functions. I am aware that this is a good way to check and understand how I work through my code from start to finish, however I am more than willing to go through my code and explain 
my thought process throughout the entire procedure.
If there are any mistakes or if anything causes confusion, feel free to reach out to me and I can explain any part of my code.

#Import Agenda File
The import_agenda.py file is executed by typing "python3 import_agenda.py agenda.xls" for example. 
If successful, the terminal will print out "Database has now been created!".

#Lookup Agenda File
The lookup_agenda.py file will import the database created in import_agenda.py. From there, it takes in arguments from the command line.
For example, "python3 lookup_agenda.py speakers Carl A. Waldspurger" will print out the information about the sessions and subsessions that include that speaker.
This program supports looking up speakers even if there are multiple speakers for an event.
This program also supports providing the information of subsessions belonging to the sessions that were selected from the given query.
