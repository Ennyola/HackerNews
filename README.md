# HackerNews
A cron job implemented in django that syncs the db with data gotten from an API every 5 minutes.



- Create a virtual Environment using virtualenv or pipenv

- cd into the root directory of the project (The same directory where you can see manage.py and requirements.txt)

- Use the command "pip install -r requirements.txt" to install all dependencies

- Run the server using "python manage.py runserver"

-Navigate to http://127.0.0.1:8000/ to view the index page.

- The detail page is on http://127.0.0.1:8000/item/<int:id>/(It can be also be accessed by clicking on the comments hyperlink on each item listed on the index page)

- Navigate through the API route which can be found here http://127.0.0.1:8000/api/

- The Job scheduler runs automatically in the background When you start the server. No explicit command is needed for it. Make sure you have stable internet connection for it to successfully add items to the DB. A log of what item is saved to the DB would be displayed on your terminal as they are being saved.

-Two Applications are created inside the django project called "api" and "news". The "api" application houses all logic related to the API and the "news" application houses all logic relating to how the news are displayed on the webpage.

- The Job folder holds the Job scheduler logic. The Job scheduler runs automatically when the server is started by modifying the ready method in news/apps.py

The following routes can be found in the application
http://127.0.0.1:8000/ - The index page

http://127.0.0.1:8000/item/<int:id>/ - The details page

http://127.0.0.1:8000/job/ - The job page. The News have been filtered to only display items with a type "job"

http://127.0.0.1:8000/ask/ - The ASK HN page. The News have been filtered to only display items in the ASK HN category

http://127.0.0.1:8000/show/ - The SHOW HN page. The News have been filtered to only display items in the SHOW HN category



The api routes are as follows 
GET http://127.0.0.1:8000/api/news/ (To fetch all items/news)

GET http://127.0.0.1:8000/api/news/?by=&by__iexact=&title=&title__iexact=&title__icontains=&type=&type__iexact= 
(To filter through all news. A list of all filters that can be specified is listed and explained below)

POST http://127.0.0.1:8000/api/news/ (To add a new item to the database)

GET http://127.0.0.1:8000/api/news/id/ (To fetch a single Item)

PUT http://127.0.0.1:8000/api/news/id/ (To update a single Item)
DELETE http://127.0.0.1:8000/api/news/id/ (To Delete a single Item)


The following filters can be specified In the API
 -"by" : To filter using the username of the item's author(case sensitive)

 -"by__iexact" : To filter using the username of the item's author(case insensitive)

 -"title" - To filter through the item's title(case sensitive)

 - "title__iexact" : To filter through the item's title(case insensitive)

 - "title__icontains": To filter through using a substring in the title(case insensitive)

 "type" - To filter through types (case sensitive)

 "type__iexact" - To filter through types (case insensitive)
 