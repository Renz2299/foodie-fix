# Foodie Fix - *Milestone Project 3*

**Find the final project here:**

A back end web application that allows users to browse a directory of recipes as well as add their own recipes.

![The Foodie Fix application shown across multiple displays](foodie_fix/static/img/readme_imgs/renders_final.png)

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [User Experience](#user-experience)
3. [Design Choices](#design-choices)
4. [Database Planning](#database-planning)
5. [Project Management](#project-management)
6. [Site Development & Features](#site-development--features)
    * [Universal Site Elements](#universal-site-elements)
    * [Landing Page]()
    * [Home Page]()
    * [My Recipes Page]()
    * [Recipe Page]()
    * [Account Page]()
7. [Credits & Acknowledgements](#credits--acknowledgements)

---

## Project Overview
Foodie Fix is a back end web application intended to help users find cooking inspiration and add their own recipes to a digital cookbook as well as allow other users to view their recipes. The application consits of five main pages: The Landing page, where users are first directed and encouraged to register or login; the Home page, which is the recipe directory showing all recipes added to the application from any users; the My Recipes page, which is individual to each user showing them their profile and the recipes they have added to the application; the Recipe pages, where the users can read and follow along with a recipe and; the Account page, where users can view and edit their account details.

---

## User Experience

### Project Goals
The primary goal of the application is to provide a helpful tool where users can browse existing recipes as well as add and edit their own recipes. Foodie Fix has two key target audience:
- People looking for cooking inspiration and new recipes to try.
- People wanting to store their recipes digitally for themselves and others to see.

These target audiences aren't exclusive and some users may want to use Foodie Fix for both purposes.

### Persona One

**User:** Sarah, 36

Sarah is a Data Analyst based in Surrey. Her and her husband have two young children, together they enjoy exploring the outdoors and taking their dog for walks in the woods.

**Sarah's Goals:**
- Find new recipes for family meals.
- Publish her own recipes so they are easy to access in the future.

**How the site helps Sarah:**
- Allows her to find new recipes created by other users.
- Provides her with a digital cookbook where she can publish her own recipes.

### Persona Two

**User:** Oscar, 52

Oscar is a Carpenter based in Newport, he enjoys spending time with his wife and family, albeit fleeting now that his three children are grown up.

**Oscar's Goals:**
- Publish his own recipes for his family and friends to try themselves.
- Find new recipes to try at his next family dinner party.

**How the site helps Oscar:**
- Allows him to publish his own recipes for others to find and try.
- Provides a directory of recipes for him to browse and try.

### Wireframes

Below are the first wireframes for the site, initially, the site consisted of just three pages, a main recipe directory page, the page for users to view their own recipes and an account page where users can review their details.

Following testing of these wireframes to understand how a user would navigate the site it was found that more pages were needed to ensure the purpose of the site was fully conveyed to users and it wa easy for users to follow.

**Home Page**

![Initial wireframes of the Foodie Fix Home page](foodie_fix/static/img/readme_imgs/wireframes_mk1_01.png)

**My Recipes Page**

![Initial wireframes of the Foodie Fix My Recipes page](foodie_fix/static/img/readme_imgs/wireframes_mk1_02.png)

**Account Page**

![Initial wireframes of the Foodie Fix Account page](foodie_fix/static/img/readme_imgs/wireframes_mk1_03.png)

---

## Design Choices

### Colours

From looking at current cooking brands, orange and reds appears to be recurring colours due to their resemblance of food, specifically fruits. I wanted this site to be more vibrant, therefore I used Adobe Colour to test out brighter tones of orange and red until I came the colour scheme shown below.

![The final colour scheme (deep fuscia, white, deep orange, mustard & pale yellow)](foodie_fix/static/img/readme_imgs/colour_scheme_final.png)

This colour scheme was tested using Adobe's accessibility tools to check the contrast ratio of different colour combinations.

White was tested on all four coloured background to see if it would be a suitable text colour throughout the site. It was found that white text only worked on the deep orange and fuscia. The deep fuscia was tested on the pale yellow and would work as a suitable text colour.

![White tested on pale yellow background](foodie_fix/static/img/readme_imgs/colour_check_1.png)

![White tested on mustard background](foodie_fix/static/img/readme_imgs/colour_check_2.png)

![White tested on deep orange background](foodie_fix/static/img/readme_imgs/colour_check_3.png)

![White tested on deep fuscia background](foodie_fix/static/img/readme_imgs/colour_check_4.png)

![Deep fuscia tested on pale yellow background](foodie_fix/static/img/readme_imgs/colour_check_5.png)

Here are the final colour assignments that were later implemented into the wireframes:
- Deep Fuscia #BF0D38 - Button Background & Header Text
- White #FFFFFF - Text (only on Deep Fuscia & Deep Orange)
- Deep Orange #DF6D00 - Header & Footer Background
- Mustard #F99B02 - Hovers & Clicked Links
- Pale Yellow #F7B76C - Card Backgrounds
- Black #000000 - Text (only when white or deep fuscia caanot be used)

### Typography

The chosen fonts for this application are Google Fonts: Marvel, Nunito & Carme.

Marvel will be used for the navbar and logo, only in uppercase.

![Marvel font in bold 700](foodie_fix/static/img/readme_imgs/marvel_font.png)

Nunito will be used for headers and buttons.

![Nunito font in extra bold 800](foodie_fix/static/img/readme_imgs/nunito_font.png)

Carme will be used for paragraph text.

![Carme font in regular 400](foodie_fix/static/img/readme_imgs/carme_font.png)

### Hi-Fi Wireframes

The initial wireframes were developed upon to ensure the purpose of the site was fully conveyed to the users. Some additions were also made to aid in planning the site and figuring out the journey a user would take through the site, these included the landing page allowing users to register or login as well as an individual recipe page.

**Landing Page**

The landing page consists of a main header image and title followed by options for the user to register or login. Below this is a grid of a the latest recipes added to the site, however the user currently cannot see more details about the recipe because they are not logged in.

![Developed wireframes of the Foodie Fix Landing page](foodie_fix/static/img/readme_imgs/wireframes_mk2-04.png)

**Home Page**

The home page is where a user is directed upon registering or logging into the site. It consists of a header image and title followed by the same grid of latest recipes, however this time the button allowing the user to view the recipe is now present as they are logged in.

![Developed wireframes of the Foodie Fix Home page](foodie_fix/static/img/readme_imgs/wireframes_mk2-05.png)

**My Recipes Page**

The my recipes page is where the user can view their profile, add recipes to the site and view the recipes they have already added to the site.

![Developed wireframes of the Foodie Fix My Recipes page](foodie_fix/static/img/readme_imgs/wireframes_mk2-06.png)

**Recipe Page**

The recipe page is where a user is directed upon clicking for more details on a recipe. If they created the recipe there will also be an edit and delete button at the bottom of the recipe page. If they did not create the recipe, then this button will not be present and they can only view the recipe.

![Developed wireframes of the Foodie Fix Recipe page](foodie_fix/static/img/readme_imgs/wireframes_mk2-07.png)

**Account Page**

The account page shows the users details that they would've filled out upon registering. Underneath is the option for the user to edit or delete their details.

![Developed wireframes of the Foodie Fix Account page](foodie_fix/static/img/readme_imgs/wireframes_mk2-08.png)

Here is a list of aspirational features that would be nice to include in the application, however not necessary and will only be implemented if time allows:
- Filter the main database of recipes by cuisine or meal.
- Allow users to review other recipes.
- Show the total number of recipes as user has created on their profile.
- Allow other users to navigate to a creators profile.
- A site specific 404 page to keep the users on the site even in the event of an error.

---

## Database Planning

SQL will be used in this project to create a relational database system containing the details needed for the application. One of the drawbacks of SQL is that once a database has been created and the fields have been filled with data, it is quite frustrating to edit or add new fields. Therefore, before creating any database functionality, the tables that would be needed for this project were planned out to hopefully prevent a frustrating and time-consuming update later on in the project.

Below is a visualisation of the tables needed for the minimum viable application, this consists of a user table where users information from registration will be stored, and a recipes table where all the information relating to recipes will be stored. Each table has a primary key of id and the foreign key between the two tables is the user.name and recipes.created_by.

![A relational user table and recipes table](foodie_fix/static/img/readme_imgs/db_plan_1.png)

If throughout the project there is time to include any of the aspirational features mentioned in [Hi-Fi Wireframes](#hi-fi-wireframes), this is the visualisation showing the tables that will be needed. The recipes table has now got cuisine and meal fields so the database can be filtered based on those fields, and the reviews table has been added. All three tables have their own primary key of id, the foreign key between users and recipes has remained the same however the user.name is also the foreign key used in the reviews table and to link the recipes and reviews table, the recipe_id becomes the foreign key.

![A relational user table, recipes table and reviews table](foodie_fix/static/img/readme_imgs/db_plan_2.png)



---

## Project Management

---

## Site Development & Features

---

## Pre-Deployment Testing

---

## Deployment

---

## Post-Deployment Testing

---

## Credits & Acknowledgement