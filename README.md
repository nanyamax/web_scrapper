WEBSCRAPPER PROJECT OBJECTIVE
Set up and configure a Scrappy project
Build a functional web scrapper with Scrapy.
Extract data from websites using selectors
store scraped data in a mongoDB database
Test and debug my Scrapy web scraper

Notes
An ITEM is a container that defines the structure of the data that you want to collect

Validation ensures that the data you collect is correct and meets specific rules, preventing bad data from being processed.
Serialization converts the data into a consistent format, making it ready for storage, transmission, or further use.

logging is a fundamental tool used in programming to record important events or actions that happen when a program runs. It is used for understanding what spider is doing at each step.

you can configure logging in ydirectly through constants in settings.py file
it is a good idea to set logging level to DEBUG and write logs to a file,. it allows you retrace your steps in case it ends up failing on a run.
.error(): Logs an error message.
repr(): Provides a detailed, debug-friendly string representation of an object.
Why repr() inside error(): To give a more informative error message that shows the structure and type of the failure object, which is useful for diagnosing issues.
