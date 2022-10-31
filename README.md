# The Fuzzy Duck|- Resturant stie
---
Welcome to the Fuzzy Ducks resturant site. The Fuzzy Duck is a small resturant with ten tables of two and we can seat parties up to 12 people.
On our site you acn view our menu, navigate to our social media, leave a review comment with a picture and create and manage your rreservations.
To leave comments and make reservations an account is needed. Anyone can create an account with a few clicks.

## Featues
--- 
### Existing Features

#### Base Template
The base templates consist of sections that are shown on all pages. The sections are navigation, messagearea and footer.

- Navigation
    - The navigation bar consist of 5 menu options when the user is logged out. When the user is logged in the "Regisster" option disapers
    - When the screen width is smaller than 990pixels the menu converts to a button in the top right coner
    - The nav option the user is on change color and get an underline to clearly show the user where on the site the user is.
    - The Navbar is shown on all pages and provides an easy and clear way to navigate through the site and therfore binging value to the user.
![pictuer of message](/bookings/static/images/nav_bar_logged_out.png)
- Messagess
    - Messages is displayed when the user take certain actions. Examples of such actions are creating, editing, deleting reservations, creating comments. Error messages are also displayed here.
    - Messages are displayed beneath the navbar. Error messages in read and confirmations in green
    - Messages help notify the user of errors and succesfull actions taken
![pictuer of message](/bookings/static/images/confirmation_message.png)
- Main content
    - Content from other pages are prresented here so the base can emain the same
- Footer
    - Here links to our social media is presented with clear symbols of each platform. The links open in a new to provide a good user experience
    - our phonenumer is also presented here if customers want to call us with a reservation
![pictuer of message](/bookings/static/images/footer.png)

#### Landing Page

- The landing page image
    - Here is the user pesented with a picture of our resturant bar to give the user an instant idea of what typ of site the user has visited
    - The image has a fixed position with a scroll effect to give an additional design boost
![pictuer of message](/bookings/static/images/hero_img.png)
- Comment section

    - Leave a Comment
     - Here the user can leave a review comment
     - If there are no comments the user sees a message to leave the first comment
     - If the user is not logged in two links are pesented to either signup or login to be able to leave a comment
     - The user must fill in the text field of max 400 charcters, this field is required
     - The user can also give a review score between 1-5 stars with a default value of 3 stars
     - There is also an optional function to upload a picture from the users visit
     - When the comment is submitted the user get a message saying that the comment is saved an awaitin approval from the resturant

    - View existing comments
        - Beneath the leave comment section the user can scroll through other visitors comments
        - The window where the comments are presented is scollable to avoid a long list on the main page
    - Approve comments
        - Before a comment is published an admin user must approve it fom the admin page to avoid inappopriate comments being published
![pictuer of message](/bookings/static/images/comment_logged_out.png)
![pictuer of message](/bookings/static/images/comments.png)
![pictuer of message](/bookings/static/images/comments_empty.png) 
#### Menu
- Menu
    - In thsi section a pdf file is loaded so the user can see what food and beveragges are offered in our resturant

#### Book a Table
- Book a Table
    - Here the user can create, view, edit and delete reservations
    - The "Create a reservation" button opens a window with input fields so the required ino can be entered
        - First name: is required and has a max length of 80 characters
        - Last name: is required and has a max lengt of 80 chaacters
        - Email: is required and must have the correct format and be less than 254 characters
        - Number of guests: is required but has a default value of 2
        - Date & Time: is equired and has date time picker to make is easy for the user to provide the corect format.
            - validators:
                - User can´t pick a date before present time.
                - User can´t pick a date before or after opening hours with the last time for reservations are at 21.59 o'clock
                - If to many reservations are placed during a specefic time a error shows that there are no available tables at that time
    - View reservations
        - Here the user can see reservations that are made and approved by the resturant
        - The resrevation card shows information about the resevation such as date and number of people
        - If there are no reservations the user sees a text that says there are no reservations at the moment
    - Edit a reservation
        - The edit reservation page opens if the user presses the "edit" button and a pr populated widow appers with all the details of the reservation
        - The user can change the information and press update or cancel when the new information is entered
    - Delete a reservation
        - The user can press the "Delete" button to delete a reservation. Before the reservation gets deleted a warning message is shown asking the user if they are sure

    
![no reservation](/bookings/static/images/no_reservation.png)
![Create reservation](/bookings/static/images/create_reservation.png)
![view reservations](/bookings/static/images/reservations.png)
![edit reserrvation](/bookings/static/images/edit_reservation.png)
![Delete resevation](/bookings/static/images/delete_reservation.png)

#### Register
- If the user do not have an account one can be reated here. Either press the "Register" link in the nav bar or in the link on the signup page
    - The fields Username and password are required and the field e-mail is optional. The password must we written in to two fields to asure that the correct password is entered.
#### Log in / Log out 
- In the navbar the user can see either see login or logout depending the log in state. This clearly shows if the user is logged in or not
- The login page requires the user to enter username and password
- The user can also check the box "Rememer me" to have the user stay loged in
- If the user presses signout the signout page is presented as an extra step before being loged out.
![sinup page](/bookings/static/images/signup.png)
![sing in page](/bookings/static/images/signin.png)
![sign out page](/bookings/static/images/signout.png)

#### Admin site
- Here an admin user can log in to manage comments and reservations
- Both comments and reservations must be approved by an admin user before published on site
- Custom list columns and actions are added so the admin user can approve/disapprove and delete multible rows at the same time. As well as et a good ovelook of all rows

![admin comments ](/bookings/static/images/admin_comments.png)
![admin resevations](/bookings/static/images/admin_reservations.png)


### Features Left to Implement
- An email confirmation sent to the user when a reservation is finalized
- Ability to pick tables in different sizes
- Calendar that shows available time slots for reservations

## Testing
---

### Validator Testing
- HTML

- CSS

- Python

### Unfixed Bugs
- More automated testing would be better. more advanced tests that could test all validators as well as model methods
- No specific error messages are shown when editin reservations. Just a message that something went wrong but not what validator was activated
### Fixed Bugs

## Deployment
---
## Credits
---
### Content

### Media

## Mockups
---
## Use stories
---