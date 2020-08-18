# TwitterBot
A twitter bot that likes posts given hashtags and follows users given usernames and the hashtags they use.

Built using Python 3.7 and the libraries tweepy and  tkinter, this provides a GUI for inputting either hashtags or usernames from the user. 
Using the hashtags input the bot crawls throught the web searching for those hashtags and likes the tweets with those hashtags and follows users tweeting about those hashtags.
Using the usernames input the bot searches for those usernames and follows them.

python gui.py  <-- runs the tkinter GUI, inputs hashtags and usernames from the user till the window is closed. 
python test.py <-- inputs the values of hashtags and usernames from the user through the command line or uses inbuilt values of hashtags and usernames.


The results are displayed in the app.log file.
