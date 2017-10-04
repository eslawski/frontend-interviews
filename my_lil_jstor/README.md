# My Lil' JSTOR

My Lil' JSTOR is a great product we are planning on rolling out to our younger audience. On the site, a user can
purchase coloring books from our collection for a flat rate of $5. The application was started a while ago and 
is in need of a few updates before we can officially launch. Luckily the developers that created the app left us a 
few instructions to get started. Check out the setup steps to see if you can get the app going and 
try to add the new features requested from the product owner. 

## Setup 

* Homebrew
* Install python
* Install pip3?
* pip vs pip3
* Install django


## Tasks

Below are some tasks to complete ahead of the interview. Please feel free to create test cases as necessary. We will go
over the code with you to discuss design choices and ask questions. 

### Something is Broken!

We have several coloring book pages ready for our users, but there appears to be a problem with the page.
Navigate to the homepage and click on the "featured book" to see the problem. We are pretty sure
that all the code that is needed to fix the problem exists in the repo already, so maybe we just aren't
calling it where we should be...

Success Criteria:
* Users are able to see Coloring Book details again

### Likes

We want the ability for users to give feedback about the title by posting a "Like" to a book. 
Users should be allowed to like as many books as they want but we should do our best to limit each session to
like each book only once. We also want to display how many likes a book as on the page.

Success Criteria
* User is able to 'Like' a book 
* User can see how many 'Likes' a book currently has
* User is prevented from re-liking a story if they are using the same browser


### Browse

We need a browse page so all our lil' JSTOR users can see the various coloring books on the site.

Success Criteria
* Users can see all the coloring books we have available to read
* Users can see the image, title and description for each book
* Clicking on a book image or title will go to the book details page


### User Comments

Our users love the coloring books and want to leave comments about how great they are. 
We need to create a form on the coloring book details page to submit a new comment. 
This form requires the name and comment section to be populated, and have an option to supply a rating of 1 to 5.
Users should not be able to submit a comment to the server if the required fields are blank. We would like to print out the 
comments with the submitted fields on the book details page.

Success Criteria
* Users can submit a comment on the book details page
* Name and comment are required before submitted form to server
* Review of 1 - 5 is optional
* We should be able to see old comments on the details page


### Discounts

We would love to offer discounts to our most active users. Currently, each coloring book is $5 and we can discounts offer discounts of
$.25 for every like and $.50 comment. The minimum price we can offer for each book is $2.50. On the book details page we need
to show the updated price to the user. 

Success Criteria
* Discounts are: 
    - $.25 per like
    - $.50 per comment
* Minimum price per book is $2.50
* Updated price is displayed on the page 




