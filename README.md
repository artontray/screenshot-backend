# Note

To enhance your reading experience of this documentation, we recommend not using the dark mode of Github, as it may display images with distorted colors that do not accurately reflect reality.

# Purpose of this project

In today's digital world, we often struggle to locate important resources when we need them the most. Thankfully, we have a helpful tool called a screenshot, which enables us to capture and preserve a screen image of vital information or instant snapshots of a situation. If you have ever searched for an old email with critical address details, you can relate to the challenge of finding specific screenshots of this event from a massive collection of files with generic names on Desktop location. Sometimes, we may need to capture evidence of a non-working service or keep a record of changes made to a system. However, locating the right screenshot from hundreds of files can be time-consuming and frustrating. 



There have been many instances where I have needed an application that allows me to search for a specific screenshot using keywords. That is precisely what the Screenshot Organizer app does, and it is the focus of this document that I will be presenting.

Personal Note :

When editing a README file for a project, I always have a section called "Fixed bugs" where I'm supposed to list any bugs I encountered during the development of the app and explain how I solved them. However, it can be frustrating to recall a specific bug I had without the accompanying screenshots. That's an other reason I decided to developp this app, specifically for capturing these bugs and organize them. This way, I can easily find them later and save time searching through my desktop.


Analys of the main problem:

- Difficulty locating specific screenshots: With the abundance of digital features available, finding a particular screenshot from a vast collection of files with generic names can be challenging and time-consuming.

- Inefficient management of digital assets: The process of scrolling through hundreds of files to locate the right screenshot is not only frustrating but also inefficient. A dedicated app like Screenshot Organizer can help users better manage their digital assets and streamline their workflow.



This project was developed in order to demonstrate 
some ability to :
- code in Python
- deal with boostrap React
- manipulate REST Framework
- understand API
- build an App with Back-End and Front-end developpement
- code with ReactJS

[Check this out](>)

# Screenshot Organizer

Screenshots are a fascinating phenomenon in the digital age. They capture a stolen moment in time that only you can see on your computer screen, making it a unique piece of digital art. The ability to share this image with the rest of the world is a powerful concept that has the potential to inspire, provoke thought, or even make someone smile.

In a world where we are constantly bombarded with information, a screenshot can capture a specific moment that resonates with us in a personal way. It can evoke a range of emotions and stir up memories that we may have forgotten. It's a visual snapshot of our digital lives that we can choose to keep private or share with others.

The act of taking a screenshot is a form of creative expression, capturing an instant in time that can never be replicated. It's a reflection of who we are and the world we inhabit, offering a glimpse into our digital experiences.

So, whether it's a funny meme, a touching message from a loved one, or an inspirational quote, a screenshot has the power to bring people together and create a shared experience. It's a testament to the power of technology and a such of unique ways in which it allows us to connect and express ourselves.

# Contents

* [Database Schema](<#database-schema>)
* [Technologies Used](<#technologies-used>)
     * [Modules](<#modules>)
     * [Languages](<#languages>)
     * [Libraries](<#libraries>)
     * [Frameworks](<#frameworks>)
     * [Platforms](<#platforms>)
     * [Services](<#services>)
     * [Resources](<#resources>)
* [Testing](#testing)
     * [APITestCase](#Aapitestcase)
     * [Manual Testing](#manual-testing)
     * [URL Testing](#url-testing)
     * [CRUD Testing](#crud-testing)
     * [Validator Testing](#validator-testing)
* [Bugs](<#bugs>)
    * [Fixed](<#fixed>)
    * [Unfixed](<#unfixed>)
* [Project Setup](<#project-setup>)
* [Deployment](<#deployment>)
    * [Set up JSON web tokens](<#set-up-json-web-tokens>)
    * [API for deployment to Heroku](<#api-for-deployment-to-heroku>)
    * [Deploy to Heroku](<#deploy-to-heroku>)
    * [extra environment variables](<#extra-environment-variables>)
* [Credits](<#credits>)
* [Media](<#media>)


# Database Schema

The database for this project is composed by :

- User : To store a new user's username and password.
- Profiles : to register User's Profile (avatar, description etc..)
- Screenshot_public : to store a post with a screenshot, content, title , image.
- Scrennshot_private : to store a post with a private screenshot : content, image, title, category (see below)
- Category : to store all the different categories of private screenshots (emails, jobs, entertainement, flights, meetings, social media etc...)
- Comment : to store all the comment connected to a public screenshot
- followers : to store all the followers and followings id of user so we known who is following who
- likes : to store all the likes register to public screenshots

To accomplish this, I had to develop a database table model to streamline the application's functionality. I used [Visual Studio Code](https://code.visualstudio.com/) to generate the following :

![DASHBOARD](media/readme-files/TABLE_SCREENSHOT_ORGANIZER.png)

[Back to top](<#contents>)


# Testing










veed for gif image
Bitmoji.com for images
