# Software Engineering Final Project - Fall 2021  
#### Contributors:
- Deepak Putta
- Jose Ramirez Fuentes
- Jaason Raudales
- Charles Read
- Keylin Sanchez
- Joseph Shatti
#### InCollege is a python-based command line utility that is designed to allow college students to create personal accounts, search and apply for jobs, and connect with other students, much like LinkedIn. The intention was to design a minimum viable product to spark interest of potential investors and get them to commit funding for future versions of the software.
#### This program was developed over a ten-week period, with stories and bugs tracked through Jira. Each week, members were assigned a new scrum role. Each contributer took on the role of scrum master, tester, and developer at different points in the development process. A branch protection rule was implemented for the main branch, which required each pull request to be reviewed by a minimum of two members before merging branches. This facilitated the collaboration process, by ensuring that all team members had any changes made to the code reviewed by others.
## Application Structure
     .
     |-- api-inputs/
     |-- api-outputs/
     |-- src/
     |  |-- db/
     |  |  |-- *** Table creation SQL script and python script ***
     |  |-- utils/
     |  |  |-- *** Handle interactions with the database ***
     |  |-- *** python files for each menu ***
     |-- test/
     |  |-- *** python files to test each menu ***
     |-- *** Database file ***
## Application Features
### Launch
    Jacob had dreamed about working at Southwest Airlines for as long as he can remember. He applied and interviewed for internships and full-time jobs to no avail…

          MENU
    n - Create new account
    l - Login
    f - Find a friend
    s - Play a video of success story
    t - Training
    i - InCollege Important Links
    u - Usefull links
    q - Quit
    
    Please make a choice from the menu:
### Student accounts
    Please input a unique username and password
    Username: Jose
    First name: Jose
    Last name: Ramirez
    Password: **hidden**
    Do you want to be a plus member? It will cost $10 each month (y/n) y
####
    Username: Jose
    Password: **hidden**

    You have successfully logged in
    Please don't forget to create a profile
    Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!

    1 - View/Edit Profile
    2 - Job/Internship Search
    3 - Find Someone You Know
    4 - Messages
    5 - Learn a New Skill
    6 - InCollege Important links
    7 - InCollege Learning
    8 - Log Out

    Please make a choice from the menu:

### Profiles
    No profile setup

    0 - Go back

    1 - Edit profile

    Select an option from the menu: 1

    Enter title: Student
    Enter major: Comp Sci
    Enter university name: USF
    Enter about: Ready to work!

    1 - Add experience
    2 - Add education
    3 - Go back

    Please make a choice from the menu:
####
    Jose Ramirez
    Title:         Student
    Major:         Comp Sci
    University:    USF
    About:         Ready to work!
    Experiences:
    None
    Education:
    None
### Jobs
    1 - Post a job
    2 - Apply for a job
    3 - Delete a job
    4 - Go back

    Please make a choice from the menu:
### Messages
    Messages

    0 - Go back

    1 - Jose
    2 - Joseph
    3 - Joshua
    4 - Start new conversation

    Select an option from the menu:
####
    Conversation with Joshua

    From you at 11/21/21 08:57:51 PM: Hi!
    From Joshua at 11/21/21 08:57:51 PM: Hi back!

    0 - Go back

    1 - Write Message
    2 - Delete Conversation

    Select an option from the menu:
### Important Links
    InCollege Important Links

    0 - Go back

    1 - About
    2 - Copyright Notice
    3 - Accessibility
    4 - User Agreement
    5 - Privacy Policy
    6 - Cookie Policy
    7 - Copyright Policy
    8 - Brand Policy
    9 - Languages

    Select an option from the menu:
### Learning
    1 - Networking
    2 - Time Management
    3 - Public Speaking
    4 - Agile and Scrum
    5 - Leadership
    6 - Go Back

    Please make a choice from the menu:
### InCollege Learning
    InCollege Learning

    0 - Go back

    1 - (Completed) How to use In College learning
    2 - (Not Completed) Train the trainer
    3 - (Not Completed) Gamification of learning
    4 - (Not Completed) Understanding the Architectural Design Process
    5 - (Not Completed) Project Management Simplified
    6 - (Not Completed) How to use In College learning

    Select an option from the menu:
