# Roommate App Project
Julia Westphal, Bianca Macias, Kang in Park, Chinedu Nnorom


An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.


## Problem Overview
This app intends to improve upon the roommate-matching process that is currently implemented within NYU. 

There are a few basic questions that students are asked as they decide who they would be most compatible with as a roommate including time they go to sleep and wake up, how clean or messy they keep their space, and whether or not they're comfortable with guests, noise, etc. Having a roommate that fits in well with your lifestyle is super important, as they are someone you will be living with for almost an entire year. There is also a lot of anxiety when it comes to roommate matching as you never meet them (unless you connect with them prior by email) until move-in day. We propose a different, more interactive solution.


## Proposed Solution
Our proposed solution is a roommate-matching app that will help NYU students find compatible roommates. While NYU already has a simple preference survey before matching roommates, the process is very vague and users have no agency over who they are matched with. Our roommate-matching app will allow users to create a profile, take a preference quiz, and be presented with personalized roommate recommendations which they can choose to connect with or continue browsing for more potential matches. Our quiz will be far more in depth than the current survey provided by NYU, to ensure the perfect match is reached. 


## Requirements
### The MVP of our app would include the following:

* Simple user log-in and profile creation
* Simple user quiz to begin roommate match process (by simple, we mean multiple choice answers and no type user input)
* Personalized roommate recommendations based on preference quiz
* Simple profile page for users
* Function to connect with compatible matches (1:1 chat?)
* Post experience survey to allow feedback on what could be improved

## Basic Survey
* What time do you usually go to bed?
* How often do you have guests over?
* Are you alright with sharing basic apartment supplies? (toiletries, cleaning supplies, kitchen supplies, etc)
* Are you often at your dorm during the day?
* Do you often clean?

## Additions 
### If MVP is produced:
* Allowing other school into our app or the greater nyc area
* More in depth roommate questionaire which allows user to write in preferences
*  More detailed user profiles

## Optional Feature
* Tabs for each NYU dorm with mini descriptions and pcitures of rooms
* Virtual/video tours (not sure how difficult this is, could prob at least get videos of Clark and Othmer)



## Design
Each of the main requirements will correspond to an API endpoint.


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
