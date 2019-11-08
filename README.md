# CHILDREN OF ZAMBIA - Code Institute Milestone Project 4
Built by **_Cecilia Barriga_**

For this project I decided to create something new, rather than following the suggested projects.
I went with a NGOn known as 'Children of Zambia'. I created the logo myself, with help of Tailor Brands website, and changing the colors myself.

I created this site with HTML, CSS, JavaScript and Python using Django. The main focus of the site, is to get donations from user in order to help the children with education. 
I also created a News page where users can read about any news happening with the children. 


## UX
This application is intended for use by all, but mainly people that want to donate money to an NGO that helps Children in Zambia with their education, and at the end this will also help to reduce poverty. 


## WireFrames
Below are the wireframes for the project.

About Us/Index:
![Index](https://user-images.githubusercontent.com/42648801/63551020-4bab4e80-c534-11e9-956f-4ab752959eae.png)

Children:
![meal](https://user-images.githubusercontent.com/42648801/63551091-78f7fc80-c534-11e9-8853-2f7cb90215d0.png)

News:
![login](https://user-images.githubusercontent.com/42648801/63551112-857c5500-c534-11e9-8d46-f9e7589e83c3.png)

Cart:
![My Recipe](https://user-images.githubusercontent.com/42648801/63551130-9200ad80-c534-11e9-9111-146c27ba3db6.png)

Checkout:
![recipe](https://user-images.githubusercontent.com/42648801/63551149-9fb63300-c534-11e9-8cd2-c5d571d62531.png)

For add and edit recipe are also the same, with difference of the buttons:
![add recipe](https://user-images.githubusercontent.com/42648801/63551160-a8a70480-c534-11e9-9762-23b7b49c514c.png)


## Layout
I used Bootstrap for this website.


## Features
The following section describes the front-end features in this project.

- Navbar - Consists of the NGO logo which returns the user to the "Index" page. There is also links to the "Children", "News" "Login", "Register", "My orders", "Logout" and "Cart". The navbar will appear on all pages.
- Index - The home page on giving the users information regarding the NGO, Issues and Education.
- Children - It display all the Children that we have currently in the program, so people can choose also to which child they wish to donate
- News: Post from the NGO (Superuser) with news of the children, or the organization.
- My orders - Users can see all the donations they have done.
- Login: User can login with his/her credentials
- Register: User can register.
- Logout: logs our the user and redirect him to index page.
- Cart - User can see the number of children they decided to donate to.
- Forgot Password Link - users recieve an email allowing them to reset their password.
- Contact form - There is a contact form in the footer for users to contact the NGO.
- Social Media links: Provides users with links to the website social media pages (Links direct to social media pages for this project as this is not a real business and there are no "Children of Zambia" accounts).


## Technologies Used
- Cloud 9 IDE : This project used Cloud 9, an online integrated development environment, to construct the code end to end.
- Bootstrap: This project used Bootstrap, a library of website themes. 
- Python: This whole proyect is done with Django. This project uses Python, an interpreted high-level programming language for general-purpose programming and used to write the logic of this game, which is included within .py files.
- HTML: This project uses HTML, the standard mark-up language used to build website layout, which is included within the .html files.
- CSS: This project uses CSS, a style sheet language, used to add styling to a website. The custom.css file was added to this project, to add additional styling on top of the Bootstrap template.
- JavaScript: This project uses JavaScript, an object-oriented programming language used to create interactive effects within web browsers. JavaScript within this project was included with the Bootstrap template.
- Chrome Dev Tools: This project uses Chrome Dev Tools, a set of web developer tools, to continuously test and inspect that the web pages are rendering as intended within the browser.
- GitHub: This project uses GitHub, a web hosting service, for version control and final project backup.
- Heroku: This project uses Heroku, a web hosting service that supports Python applications, for final project deployment.
- Font Awesome: This project uses Font Awesome, vector icons and social logos on the website.
- Stripe: This project uses Stripe in order to accept the payments/donations.

## Testing
- Manual Testing: I retrieve a lot of issues while texting.

Trying every single thing: login, send forgotten password, add post, edit/delete poster (as superuser), contact form, payment form, add to cart, checkout.


- Responsive Testing

The app was tested on different devices and also using the Google Chrome inspect feature to test for repsonsiveness and any errors that occurred. 


## Deployment
The following section describes the process to deploy this project to Heroku.

- Ensure all required technologies are installed locally, as per the requirements.txt file.
- Via Terminal, login to Heroku, using 'heroku login' command. 
- Push project to Heroku, using 'push -u heroku master' command.
- Create scale, using 'heroku ps:scale web=1' command.
- Login to Heroku and select newly created app.
- Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
- From 'More' menu on the top right, select 'Restart all dynos'.

You can see it here: [https://ngo-ces.herokuapp.com/](url)


## Bugs and Struggles
I found several issues and I struggle with many things:
- In the payment form all users were displaying in the full name field.
- I could not display messages of success or error for sending the contact form
- The payment was not passing correctly
- I could not display the orderitemlist in "my orders"
- Following the auth code from Code Institute there was an issue with the password_reset


## Acknowledegments
- Content: The information regarding the situation in Zambia is coming from UNICEF
- Media: The photos used in this site were obtained from pixabay and unsplash.
- Acknowledgements: Big thank you to the tutors for all your help and patience, as I have many things breaking and you were extra patiente with me.
