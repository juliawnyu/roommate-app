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


## Design
Each of the main requirements will correspond to an API endpoint.
