# Difference between data and json?
- JSON is coming form an external database that is made public which is made available to us by an API link. 
    - it can be an object, a list of objects, objects that contain list. 
- JSON comes in many formats, in reality, its reading from a database but it is a link that is specific that all that link is going to pull that database information. 
- So no visualness to it or anything like that. 

https://dojo.navyladyveteran.com/
# This is a django based API. if it is an api where is the json data?

Django REST framework
Log in
Api Root

GET 
json
api
OPTIONS
Api Root
The default basic root view for DefaultRouter

GET /
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "characters": "https://dojo.navyladyveteran.com/characters/", - this is the JSON data 
    "squishies": "https://dojo.navyladyveteran.com/squishies/" - - this is the JSON data 
}

# Answer: At this link the data is simply 2 links to the actual api routes 

# ASSUMING WE HAVE ALREADY MADE IT SO OUR APPLICATION CAN SEE THE JSON DATA FROM THIS LINK HOW WOULD WE USE IT? HOW WOULD WE DISPLAY THE JSON DATA THAT WE ARE NOW PULLING BACK?

# Answer: Use jinja and a for loop on our html and display what we want like: its like we are pulling our actual own data from our database 
{% for character in characters %}
 <h2>{{character.name}}</h2>
{% endfor %}


# What is an API Key?
- Its the developer of the API's way of restricting who can use the API data. 
- if the key is not part of hte url, typically an error is returned. 
- how do we know this website https://dojo.navyladyveteran.com/characters/ doesnt not have an API key? 
    - because we can all access it


# Most of the time, the difference between using a key and not using  a key is?
- the amount of times  you're allow to send a request to the API. There's a limit alot of times to ones without the api keys

# The purpose of API's is why reinvent the wheel? When there's already a database out there, why dont you use public and available to use. 

# APIS access data publicly so you don't have to make your own database and save it yourself. Storage is precious. 
- since they are public apis, you do not want to many people going to that link at one time, it will crash the servers down. 





YOU WILL NEED TO INSTALL THE FOLLOWING PACKAGES TO RUN THIS APP AS IS flask flask-bcrypt pymysql requests flask-cors

https://api.github.com/users/dojo24 https://api.github.com/users/dojo24/followers

https://dojo.navyladyveteran.com/ https://dojo.navyladyveteran.com/characters/ https://dojo.navyladyveteran.com/squishies/

https://api.openweathermap.org/data/2.5/weather?lat=41.06&lon=-76.24&appid= https://api.openweathermap.org/geo/1.0/direct?q=Berwick,18603&limit=5&appid=

https://app.peardeck.com/student/ttcyuundb

https://github.com/public-apis/public-apis







# For spotipy APIs you need ot install pipenv install spotipy as a package 
    - in terminal type pipenv install spotipy (this way you can import spotipy)