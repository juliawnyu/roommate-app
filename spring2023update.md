# Spring 2023 Update
Currently, the project is just a little farther behind the example class project worked on last semester (the game API used during lectures). Most of the features such as database connection and new endpoints have been added.

### 1. Detail what you have already completed in your project. What requirements were met in completing these bits?

MVP featuers completed:
* Simple register page that uses local SQLite3 database (temporary)
* Simple login page that uses local SQLite3 database (temporary)
* User homepage with links to dorm info & quiz
* Endpoints for preference stats (eg: UserCleaningPreferences, UserAnimalPreferences, UserCommonBedtimes, etc)
* Test functions for all endpoints

### 2. Set out your goals for this semester. Please detail what the requirement is that each goals will meet, and how you expect to meet it.

This semester, the team would like the following user journey:
* User registers an account, which is added sucessfully to a database
* User answers a quiz, and these answers are stored to use to roommate match (could be a user with 2 or 3+ similar answers are a match)
* User is able to see a dashboard
* Host the website through a cloud hosting service
* Move database functions to integrate with MongoDB
* Add password encryption for database
* Ultimately we want to provide a seamless experience for the user from registering to finding a roommate match

Stretch features would be:
* A sophisticated-looking UI
* Chat feature with matches (involves some networking)
