# The Fuzzy Duck|- Resturant stie
---
Welcome to the Fuzzy Ducks resturant site. The Fuzzy Duck is a small resturant with ten tables of two and we can seat parties up to 12 people.
On our site you can view our menu, navigate to our social media, leave a review comment with a picture and create and manage your reservations.
To leave comments and make reservations an account is needed. Anyone can create an account with a few clicks.

## Featues
--- 
### Existing Features

#### Base Template
The base templates consist of sections that are shown on all pages. The sections are navigation, message area and footer.

- Navigation
    - The navigation bar consist of 5 menu options when the user is logged out. When the user is logged in the "Register" option disappers
    - When the screen width is smaller than 990pixels the menu converts to a button in the top right coner
    - The nav section the user is on change color and get an underline to clearly show the user where on the site the user is.
    - The Navbar is shown on all pages and provides an easy and clear way to navigate through the site and therfore binging value to the user.
![nav bar log out]( static {%%}
- Messagess
    - Messages is displayed when the user take certain actions. Examples of such actions are creating, editing, deleting reservations, creating comments. Error messages are also displayed here.
    - Messages are displayed beneath the navbar. Error messages in red and confirmations in green
    - Messages help notify the user of errors and succesfull actions taken
![confim message](/bookings/static/bookings/images/confirmation_message.png)
- Main content
    - Content from other pages are prresented here so the base can emain the same
- Footer
    - Here links to our social media is presented with clear symbols of each platform. The links open in a new to provide a good user experience
    - our phone number is also presented here if customers want to call us with a reservation
![footer](/bookings/static/bookings/images/footer.png)

#### Landing Page

- The landing page image
    - Here the user is presented with a picture of our resturant bar to give the user an instant idea of what typ of site the user has visited
    - The image has a fixed position with a scroll effect to give an additional design boost
![hero image](/bookings/static/bookings/images/hero_img.png)
- Comment section

    - Leave a Comment
     - Here the user can leave a review comment
     - If there are no comments the user sees a message to leave the first comment
     - If the user is not logged in two links are pesented to either signup or login to be able to leave a comment
     - The user must fill in the text field of max 400 charcters, this field is required
     - The user can also give a review score between 1-5 stars with a default value of 3 stars
     - There is also an optional function to upload a picture from the users visit. If no image is uploaded a default picture is added
     - When the comment is submitted the user get a message saying that the comment is saved and awaitin approval from the resturant

    - View existing comments
        - Beneath the leave comment section the user can scroll through other visitors comments
        - The window where the comments are presented is scrollable to avoid a long list on the main page
    - Approve comments
        - Before a comment is published an admin user must approve it from the admin page to avoid inappopriate comments being published
![logout](/bookings/static/bookings/images/comment_logged_out.png)
![comments](/bookings/static/bookings/images/comments.png)
![empty comment](/bookings/static/bookings/images/comments_empty.png) 
#### Menu
- Menu
    - In this section a pdf file is loaded so the user can see what food and beveragges are offered in our resturant

#### Book a Table
- Book a Table
    - Here the user can create, view, edit and delete reservations
    - The "Create a reservation" button opens a window with input fields so the required info can be entered
        - First name: is required and has a max length of 80 characters
        - Last name: is required and has a max lengt of 80 chaacters
        - Email: is required and must have the correct format and be less than 254 characters
        - Number of guests: is required but has a default value of 2
        - Date & Time: is required and has date time picker to make is easy for the user to provide the corect format.
            - validators:
                - User can´t pick a date before present time.
                - User can´t pick a date before or after opening hours with the last time for reservations are at 21.59 o'clock
                - If to many reservations are placed during a specefic time a error shows that there are no available tables at that time
    - View reservations
        - Here the user can see reservations that are made and approved by the resturant
        - The resrevation card shows information about the resevation such as date and number of people
        - If there are no reservations the user sees a text that says there are no reservations at the moment
    - Edit a reservation
        - The edit reservation page opens if the user presses the "edit" button and a pre populated window appers with all the details of the reservation
        - The user can change the information and press update or cancel when the new information is entered
    - Delete a reservation
        - The user can press the "Delete" button to delete a reservation. Before the reservation gets deleted a warning message is shown asking the user if they are sure

    
![no reservation](/bookings/static/bookings/images/no_reservation.png)
![Create reservation](/bookings/static/bookings/images/create_reservation.png)
![view reservations](/bookings/static/bookings/images/reservations.png)
![edit reserrvation](/bookings/static/bookings/images/edit_reservation.png)
![Delete resevation](/bookings/static/bookings/images/delete_reservation.png)

#### Register
- If the user do not have an account one can be created here. Either press the "Register" link in the nav bar or in the link on the signup page
    - The fields Username and password are required and the field e-mail is optional. The password must we written in to two fields to asure that the correct password is entered.
#### Log in / Log out 
- In the navbar the user can see either login or logout depending the log in state. This clearly shows if the user is logged in or not
- The login page requires the user to enter username and password
- The user can also check the box "Rememer me" to have the user stay loged in
- If the user presses signout the signout page is presented as an extra step before being loged out.
![sinup page](/bookings/static/bookings/images/signup.png)
![sing in page](/bookings/static/bookings/images/signin.png)
![sign out page](/bookings/static/bookings/bookings/images/signout.png)

#### Admin site
- Here an admin user can log in to manage comments and reservations
- Both comments and reservations must be approved by an admin user before published on site
- Custom list columns and actions are added so the admin user can approve/disapprove and delete multible rows at the same time. As well as et a good ovelook of all rows

![admin comments ](/bookings/static/bookings/images/admin_comments.png)
![admin resevations](/bookings/static/bookings/images/admin_reservations.png)

#### Model Methods
- Automatic calculations of tables needed for reservation
- Automatic calculation of end time or reservation
- Status for both comments reservations are set to unapproved by default

### Features Left to Implement
- An email confirmation sent to the user when a reservation is finalized
- Ability to pick tables in different sizes
- Calendar that shows available time slots for reservations

## Testing
---
The site has been both manually tested and with some automated tests. How the site works is desribed in each section in the README file.
- Manual Testing
    - Creating comments
        - Error message is shown if the text field is left blank
        - The comment does not show until approved by an admin user
        - A default picture is added if the user does not uppload an image
        - A picture can be uploaded
        - A message is shown when comment is submitted
    - Creating a resservation
        - Error message is shown if any field without default value is left blank
        - Error message is shown if email form has the wrong format
        - The reservation is not shown before it has been approved by an admin user
        - A message is shown when the form is added successfully 
        - A message is shown when the form is added with a error
        - A specific error is shown in the form if a date is picked before/after opening hours
        - A specific error is shown in the form if a date is picked present time
        - A specific error is shown in the form if there is there are no available tables in that time slot
    - Editing a reservation
        - Edit button takes user to edit page
        - All values are pre populated
        - Update and cancel buttons work
        - Successfully submitted change shows an allert message
        - Wrongfully added changes gives a generic error message
    - Deleting a Reservation
        - Delete button shows a warning modal
        - Delete button in modal successfully delete reservation
        - Cancel button in modal closes modal
    - Links in navbar works
    - Links in footer works and opens in a new window
    - The login / register links in comment/Book a table page works (if user is not logged in)

- Automated testing
    - Comment form is tested in test_forms, and that required and not required fields pass test
    - Views testing
        - Testing that requires loggin
            - Edit reservation gives a 200 response and use the corect template
            - Add eservation gives a 200 response
            - Delete reservation works
            - Add comment contains an updated object and redirects to the corect site
        - Test that do not require user to be logged in
            - Menu page gives a 200 response
            - The index page uses the corect template and gives a 200 response
            - The view reservation page uses the corect template and gives a 200 response


### Validator Testing
- HTML using https://validator.w3.org/
    - edit.html with no errors 
    - index.html only errors from django template vars
    - my_bookings.html only errors from django variables
- CSS using https://jigsaw.w3.org/
    - style.css no errors found

- Python using https://infoheap.com/python-lint-online/
    - admin.py no errors
    - forms.py no errors
    - models.py no errors
    - test_forms.py no errors
    - test_views.py error on f'string' 
    - views.py no errors

    - settings.py no errors
    - urls.py no errors

### Unfixed Bugs
- More automated testing would be better. more advanced tests that could test all validators as well as model methods
- No specific error messages are shown when editing reservations. Just a message that something went wrong but not what validation error was activated
- In test_forms the test tried for ReservationForm is ok even if fields are missing values. There fore that test was deleted

### Fixed Bugs
 - Date and time field was not pre populated when pressing edit reservation
    - Fix: I erased the custom date time format attribute on that form field and that fixed it
 - Reservation between opening hours did not work
    - Fix: i changed the character place on the split string method from 11:12 to 11:13
- Function to avoid double reservations did not work
    Fix: I used a filte method to query reservatio times that collided but it did not seam to work so I made a for loop compare already done reservations with the reservation in the form. If the dates collided the loop ssubtracted the tables needed for that reservation with the resturants total number of tables fo two people.
## Deployment
---
- Create app on heroku
    - Create heroku account or sign in
    - Click create new app in the top right corner
    - Give app a name and choose location nearest to you
    
- Attach the database
    - Click resources tab
    - Search for postgres and add heroku postgres

- Prepare your enviroment and settings.py
    - Click settings tab
    - Click reveal config vars
    - Copy adress to database
    - Add secret key variable from project
    - Create an env.py file
    - Add env.py file to gitignore
    - Create enviroment variables for database and secret key 
    - Attache heroku database as default in settings.py 
    - Add heroku app name in Allowed hosts ['bookings2022ci.herokuapp.com', 'localhost']
    - Create a procfile with content: web: gunicorn django_bookings.wsgi

- Get static and media files stored on cloudinary
    - Login/Register a Cloudinary account
    - Go to dashboard and copy API Enviroment variable
    - Add Cloudinary url to env.py (Delete prefix Cloudinary_url=)
    - Copy Cloudinary url in config vars in heroku settings
    - Add Config vars DISABLE_COLLECTSTATIC 1
    - Add Cloudinary_storage and Cloudinary to Installed apps in settings.py
    - Add these lines of code to settings.py
        - STATIC_URL = '/bookings/static/'

        - STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
        - STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
        - STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

        - MEDIA_URL = '/media/'
        - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    - Add TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') to settings.py
    - In TEMPLATTES  in settinggs.py add [TEMPLATES_DIR] to Dirs: field

- Deployment on Heroku
    - Click deployment tab
    - Connect github account
    - Search for repository
    - Click deploy branch

- Final deployment
    - DEBUG flag must be set to false in settings.py
    - Add X_FRAME_OPTIONS = 'SAMEORIGIN' to settings.py
    - Remove Disablestatic config var
    - Click deploy branch in deploy menu.

    
## Credits
---
 
### Borrowed code
- Rendering alert messges:
    - https://ordinarycoders.com/blog/article/django-messages-framework
- How to make nav link active with bootstrap so usesr could see where on the site is active
    - https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap
-  How to style froms with bootstap:
    - https://www.youtube.com/watch?v=6-XXvUENY_8


### Content

- The site is styled with bootstrap and css

- The icons are taken fom https://fontawesome.com

- Here are a list of articles, sites and people that has heleped me during the project
    - How to limit an integer field:
        https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    - How to make nav link active with bootstrap so usesr could see where on the site is active
        - https://stackoverflow.com/questions/25044370/make-clicked-tab-active-in-bootstrap
    - How to style froms with bootstap:
        https://www.youtube.com/watch?v=6-XXvUENY_8
    - How to combine a post request with a user:
        - https://www.youtube.com/watch?v=zJWhizYFKP0&t=343s
    - How to add actions and list objects to admin site:
        - https://www.youtube.com/watch?v=nR-12YbcXPw
    - How to render a pdf file:
        - https://www.csestack.org/render-open-pdf-file-django/
    - How to log in a user in a test case before rrunning test:
        - https://micropyramid.com/blog/django-unit-test-cases-with-forms-and-views/ and also CI support

### Media
- Pictures on site are taken from https://www.pexels.com/sv-se/
- The menu was taken from https://www.sample.net/graphics/restaurant-menu-templates/#

## Mockups
---
![mockup landing page](/bookings/static/bookings/images/mockup_landing.png)
![mockup resevations page](/bookings/static/bookings/images/mockup_reservation.png)

## User Stories

All user stories can be followed in the git repositoy for all major functionality