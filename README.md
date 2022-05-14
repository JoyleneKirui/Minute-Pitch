# Minute-Pitch



## Author - Joylene Kirui

This is a Python Flask application that allows users to submit their one minute pitches and other users to vote on them and leave comments of their feedback on them. 

## Description

This is a Flask application that allows users to pi 1 minute to actually say something meaningful!</br> #Pitch in a minuteusers to vote on them and leave comments of their feedback on them. The pitches are organized by category. 

#### Prerequisites
Basic HTML, CSS

## Setup/Installation Requirements

```
#flask
$ pip install flask

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

```
1.Download and install Git ($ sudo apt install git-all)
  Clone this [github repo] (https://github.com/JoyleneKirui/Minute-Pitch.git)
2. Install python($ sudo apt-get install python3.8)
3. On terminal for linux or command prompt for windows;
  * Change directory to working directory
  * Run $ chmod +x start.sh
  * Run the application: $ ./start.sh

```

### Deployment environment
* Heroku

### How To Access the Site
Live link: https://Minute-Pitch.herokuapp.com/


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Displays pitches and pitches categories. | **Select Pitches Category** | view pitches in category |
| Dispay Register form | **Register** | Redirected to Registration Page |
| Display login form | **Login** | Redirect to home page |
| Display Account Information | **Click Update** |  Update Profile Page |



## TDD

`$ python3 manage.py test`


## User Story
* A user can see the pitches other people have posted. 
* A user can be signed in and leave a comment
* A user can vote on the pitch they liked and give it a downvote or upvote.
* A user will receive a welcoming email once they sign up.
* A user can view the pitches they have created in their profile page 
* A user can comment on the different pitches and leave feedback 
* A user can submit a pitch in any category. 
* A user can view the different categories.

### Technology & Tools
* Python
* Flask
* HTML
* CSS
* Bootstrap

## Known Bugs
There are no known bugs

## License

> [MIT License](license) this application's source code is free to be used for any open source projects

> Copyright (c) 2022 **Joylene Kirui**



## Authors information
* [LinkedIn](https://www.linkedin.com/in/Joylene-Kirui)
