# url_shortener  

https://shorterurlchris.herokuapp.com/  

This is a URL shortener written in Python using Django.  The URLs don't really come out that short given that the host URLs on heroku are pretty long, but you get the idea!

This app uses postgres as the database, and will store the last url you have shortened in an anonymous session, which will display it back on page load either until you shorten a new URL, or the session expires.  

A note: the free Heroku tier I'm using for this app shuts down the server after 30 minutes of activity.  You will see a slow start up time if the app is currently asleep, but it will run quickly after that.

