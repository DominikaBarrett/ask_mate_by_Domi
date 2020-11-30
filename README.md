Story
Last week you created a pretty good site from scratch. It already has some features but it's a bit difficult to maintain due to the fact that we store data in csv files and we also need some more features to make it more usable and more appealing to users.

The management decided to move further as users requested new features like ability to comment on answers and tag questions (and here is the issue with csv files as well). There are several other feature requests which you can find in the user stories.

As last week the management is handing out a prioritized list of new user stories that you should add to the unfinished stories from last week on your product backlog. Try to estimate these new stories as well and based on the estimations decide how many your team can finish until the demo. As the order is important, you should choose from the beginning of the list as much as you can.

What are you going to learn?
how to use psycopg2 to connect to a PostgreSQL database from Python,
SQL basic commands (SELECT, UPDATE, DELETE, INSERT)
CSS basics
how to work according to the Scrum framework,
how to create a sprint plan.
Tasks
As you will work in a new repository but you need the code from the previous sprint, add the ask-mate-2 repository as a new remote to the previous sprint's repository, then pull (merge) and push your changes into it.

There is a merge commit in the project's repository that contains code from the previous sprint
Make the application use a database instead of CSV files.

The application uses a PostgreSQL database instead of CSV files
The application respects the PSQL_USER_NAME, PSQL_PASSWORD, PSQL_HOST and PSQL_DB_NAME environment variables
The database structure (tables) is the same as in the provided SQL file (sample_data/askmatepart2-sample-data.sql)
Allow the user to add comments to a question.

There is a /question/<question_id>/new-comment page
The page is linked from the question's page
There is a form with message field, and issues POST requests
After submitting, you are redirected back to the question detail page, and the new comment appears together with submission time
Allow the user to add comments to an answer.

There is a /answer/<answer_id>/new-comment page
The page is linked from the question's page, next to or below the answer
There is a form with message field, and issues POST requests
After submitting, you are redirected back to the question detail page, and the new comment appears together with submission time
Implement searching in questions and answers. (Hint: Passing data from browser)

There is a search box and "Search" button on the main page
When you write something and press the button, you see a results list of questions (same data as in the list page)
The results list contains questions for which the title or description contain the searched phrase
The results list also contains questions which have answers for which the message contains the searched phrase
The results list has the following URL: /search?q=<search phrase>
Allow the user to edit the posted answers.

There is a /answer/<answer_id>/edit page
The page is linked from the answer's page
There is a form with a message field, and issues a POST request
The field is pre-filled with existing answer's data
After submitting, you are redirected back to the question detail page, and the answer is updated
Allow the user to edit comments.

The page URL is /comment/<comment_id>/edit
There is a link to the edit page next to each comment
The page contains a POST form with a message field
The field pre-filled with current comment message
After submitting, you are redirected back to question detail page, and the new comment appears
The submission time is updated
There is a message that says "Edited <number_of_editions> times." next to or below the comment
Allow the user to delete comments.

There is a recycle bin icon next to the comment
Clicking the icon asks the user to confirm the deletion
The deletion itself is implemented by the /comments/<comment_id>/delete endpoint (which does not ask for confirmation anymore)
After deleting, you are redirected back to question detail page, and the comment is not showed anymore
Display latest 5 questions on the main page (/).

The main page (/) displays the latest 5 submitted questions
The main page contains a link to all of the questions (/list)
Implement sorting for the question list. [If you did this user story in the previous sprint, now you only have to rewrite it to use SQL]

The question list can be sorted by title, submission time, message, number of views, and number of votes
You can choose the direction: ascending or descending
The order is passed as query string parameters, for example /list?order_by=title&order_direction=desc
Add tags to questions.

The tags are displayed on the question detail page
There is an "add tag" link which leads to the page for adding a tag
The page for adding a tag has the URL /question/<question_id>/new-tag
The page allows to either choose from existing tags, or define a new one.
Highlight the search phrase in the search results.

On the search results page, the searched phrase should be highlighted
If the phrase is found in an answer, the answer is also displayed (slightly indented)
The search phrase is also highlighted in the answers
Allow the user to delete tags from questions

There is an X link next to each tag
Clicking that link deletes the tag and reloads the question page
The deletion is implemented as /question/<question_id>/tag/<tag_id>/delete endpoint
General requirements
None

Hints
It's important that if the database table has a timestamp column then you cannot insert a UNIX timestamp value directly into that table, you should use:
either strings in the following format '1999-01-08 04:05:06',
or if you use psycopg2 and the datetime module, you can pass a datetime object to the SQL query as parameter (details in the background materials: Date/Time handling in psycopg2)
Pay attention on the order of inserting data into the tables, because you may violate foreign key constraints (that means e.g. if you insert data into the question_tag before you insert into the tag table the corresponding tag id you want to refer to then it won't exist yet)!
You can import the sample data file into psql with the \i command or run it via the Database tool in PyCharm.
Some user stories may require to deal with CSS as well, but do not deal with CSS too much. It's more important that you write proper queries, have a working connection with psycopg2, have a clean Python code than create an amazingly beautiful web application (although if you have time, of course it's not forbidden to do so 😃).
Data models
All data should be persisted in a PostgreSQL database in the following tables (you can ignore data in the not implemented fields):

AskMate data model part 2

question table
id: A unique identifier for the question
submission_time: The date and time when the question was posted
view_number: How many times this question was displayed in the single question view
vote_number: The sum of votes this question has received
title: The title of the question
message: The question text
image: the path to the image for this question

answer table
id: A unique identifier for the answer
submission_time: The date and time when the answer was posted
vote_number: The sum of votes this answer has received
question_id: The id of the question this answer belongs to
message: The answer text
image: The path to the image for this answer

tag table
id: A unique identifier for the tag
name: The name of the tag

question_tag table
question_id: The id of the question the tag belongs to
tag_id: The id of the tag belongs to the question

comment table
id: A unique identifier for the comment
question_id: The id of the question this comment belongs to (if the comment belongs to an answer, the value of this field should be NULL)
answer_id: The id of the answer this comment belongs to (if the comment belongs to a question, the value of this field should be NULL)
message: The comment text
submission_time: The date and time the comment was posted or updated
edited_number:: How many times this comment was edited

Database and sample data
To init the database use the sample_data/askmatepart2-sample-data.sql file in your repository.

Starting your project
Background materials
Git
Working with the git remote command
Merge vs rebase
Mastering git
SQL
Installing and setting up PostgreSQL
Installing psycopg2
Best practices for Python/Psycopg/Postgres
Setting up a database connection in PyCharm
Date/Time handling in psycopg2
PostgreSQL documentation page on Queries
PostgreSQL documentation page Data Manipulation
Database glossary
Agile/SCRUM
Agile project management
Planning poker
Web basics (Flask/Jinja/HTML/CSS)
Flask/Jinja Tips & Tricks
Passing data from browser
Collection of web resources
Pip and VirtualEnv
A web-framework for Python: Flask
Flask documentation (the Quickstart gives a good overview)
Jinja2 documentation
