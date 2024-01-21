<h1 align="center"><strong>💲💲💲 Budget Busters: New Year, New Numbers 💲💲💲</strong></h1>

<img src="https://res.cloudinary.com/djdefbnij/image/upload/v1705314715/Hackathons/Screenshot_2024-01-15_at_10.27.38_rc7lor.png" alt="BudgetBustersBanner" width="1200"/>

# SUBMISSION

## Testing

### Code Validation
#### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.
| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FJesseRoss001.github.io%2Fjanhackathonteam11%2Findex.html) | ![screenshot](documentation/html-validation-home.png) | Section lacks header h2-h6 warning |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2FJesseRoss001.github.io%2Fjanhackathonteam11%2Fcontact.html) | ![screenshot](documentation/html-validation-contact.png) | obsolete iframe warnings |


#### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2FJesseRoss001.github.io%2Fjanhackathonteam11) | ![screenshot](documentation/css-validation-style.png) | Pass: No Errors |


#### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.
| File | Screenshot | Notes |
| --- | --- | --- |
| script.js | ![screenshot](documentation/js-validation-script.png) | Unused variables from external files |


#### Python
I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JesseRoss001/janhackathonteam11/main/run.py) | ![screenshot](documentation/py-validation-run.png) | W291 trailing whitespace |


**IMPORTANT**: Django settings.py

The Django settings.py file comes with 4 lines that are quite long, and will throw the `E501 line too long` error.
This is default behavior, but can be fixed by adding `# noqa` to the end of those lines.

Example:

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

**IMPORTANT**: migration and pycache files

You do not have to ever validate files from the `migrations/` or `pycache/` folders!
Ignore these `.py` files, and validate just the files that you've created or modified.

### Browser Compatibility
I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome-home.png) | ![screenshot](documentation/browser-chrome-about.png) | ![screenshot](documentation/browser-chrome-contact.png) | ![screenshot](documentation/browser-chrome-etc.png) | Works as expected |



### Responsiveness
I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile-home.png) | ![screenshot](documentation/responsive-mobile-about.png) | ![screenshot](documentation/responsive-mobile-contact.png) | ![screenshot](documentation/responsive-mobile-etc.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet-home.png) | ![screenshot](documentation/responsive-tablet-about.png) | ![screenshot](documentation/responsive-tablet-contact.png) | ![screenshot](documentation/responsive-tablet-etc.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop-home.png) | ![screenshot](documentation/responsive-desktop-about.png) | ![screenshot](documentation/responsive-desktop-contact.png) | ![screenshot](documentation/responsive-desktop-etc.png) | Works as expected |




## Deployment

<!-- TODO - Add deployed link -->
The live deployed application can be found deployed on [Heroku](https://budgetbuddy2-38958568c907.herokuapp.com/).

### ElephantSQL Database

This project uses [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click **Create New Instance** to start a new database.
- Provide a name (this is commonly the name of the project: janhackathonteam11).
- Select the **Tiny Turtle (Free)** plan.
- You can leave the **Tags** blank.
- Select the **Region** and **Data Center** closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- Optional: *edit your assigned cloud name to something more memorable*.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | cloudinary://423928569512371:Xds6g-KgHTsH_8ayPkb0vci23l4@ddll4c0zo |
| `DATABASE_URL` | postgres://fvnucmpd:fTkWXzsFK1mmwYZ6t7vlNHWNBpJz2DAd@manny.db.elephantsql.com/fvnucmpd |
| `DISABLE_COLLECTSTATIC` | 1 (*this is temporary, and can be removed for the final deployment*) |
| `SECRET_KEY` | 15q8j@52(%vztw)qq!&jnxlf-n%-nq60m9asb1-nv14hx+_q6u |

Heroku needs two additional files in order to deploy properly.

- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!


The project is deployed and can be accessed at [http://your-deployed-link.com](https://budgetbuddy2-38958568c907.herokuapp.com/).

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

Sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "cloudinary://423928569512371:Xds6g-KgHTsH_8ayPkb0vci23l4@ddll4c0zo")
os.environ.setdefault("DATABASE_URL", "postgres://fvnucmpd:fTkWXzsFK1mmwYZ6t7vlNHWNBpJz2DAd@manny.db.elephantsql.com/fvnucmpd")
os.environ.setdefault("SECRET_KEY", "15q8j@52(%vztw)qq!&jnxlf-n%-nq60m9asb1-nv14hx+_q6u")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/JesseRoss001/janhackathonteam11) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/JesseRoss001/janhackathonteam11.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JesseRoss001/janhackathonteam11)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/JesseRoss001/janhackathonteam11)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!


## Criteria

| Criteria                                                                | BudgetBuddy's functionality                                                                                                                                                                                                       |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The project has a creative design that enhances user-experience         | BudgetBuddy has a clean interface and multiple modern components that provide a positive user experience. It is designed to be easy to navigate so that the user can enjoy the different features without getting overwhelmed.    |
| The project is finance related and has a real world use case            | BudgetBuddy is designed to assist users in managing their personal finances by allowing them to set weekly, monthly, and yearly budgets. Users can track expenses and incomes, making it a practical tool for financial planning. |
| The project is Responsive and accessible on different screen sizes      | BudgetBuddy is built with Bootstrap to be fully responsive, ensuring a seamless user experience across devices. This adaptability enhances accessibility and convenience for users managing their finances on-the-go.             |
| The project is well-planned using GitHub Projects or other issue board  | The development of BudgetBuddy was organised using GitHub Projects. This involved detailed issue tracking, feature prioritisation, and progress tracking, ensuring a structured and efficient development process.                |
| The project has a well documented README based on the provided template | The README document for BudgetBuddy is comprehensive and follows the provided template.                                                                                                                                           |

## User Stories



### New Site Users

- As a new visitor, I want to see a demo on how to plan my budget, so that I can understand how the website can help me with my financial planning.
- As a new user, I want to easily find and use the sign-up option, so that I can create an account.
- As a user, I want to browse a variety of financial articles, so that I can learn more about managing my finances.
- As a new site user, I want to be able to create an account, So that I can start setting up my own budget.
- As a registered user, I want to be able to log into my account securely, So that I can access my budgeting information.
- As a new site user, I want to be able to contact the Website, So that I can get in touch with the app.
- As a user, I want to access a FAQ section, so that I can find answers to common questions without having to contact support directly.
- As a user, I want to learn more about the company and its mission, so that I can feel confident in using the website.

### Returning Site Users

- As a returning user, I want to easily log in to my account, so that I can continue managing my budget and accessing personalized content.
- As a returning user, I want to log in and view my dashboard, so that I can quickly see an overview of my financial situation.
- As a returning user, I want to add and categorize my income on the dashboard, so that I can keep track of my earnings and understand where my money comes from.
- As a returning user, I want to record and categorize my expenses, so that I can monitor where my money is going and manage my spending better.
- As a returning user, I want to set financial goals on a weekly, monthly, and yearly basis, so that I can plan my savings and spending according to my short-term and long-term.
- As a returning user, I want to generate reports of my income, expenses, and goal progress, so that I can have a detailed understanding of my financial planing.
- As a user, I want my financial data to be secure and private, So that I can trust the platform with sensitive information.


# ABOUT SUBMISSION

## Intro

Welcome to BudgetBuddy, your go-to companion for financial empowerment! BudgetBuddy is a comprehensive budgeting app designed to assist users in making informed financial decisions, helping them achieve their financial goals with ease and confidence. We created BudgetBuddy to simple the expense and income tracking process. There are tools out there that make something as simple (and important!) as your finances so difficult. BudgetBuddy gives you a straightforward way to keep you on track to your savings goals.

## Goal

The goal section provides a concise summary of the main objective or purpose of the project or software described in this README. It addresses the following aspects:

- ➡️ Problem Statement

  Many existing financial tools complicate the basic yet crucial task of tracking expenses and income. This complexity can hinder users from effectively managing their finances and achieving their savings goals.

- ➡️ Objective(s)

  - To simplify the process of tracking expenses and income, making financial management accessible and straightforward for everyone.
  - To empower users to make informed financial decisions through a user-friendly and comprehensive budgeting tool.
  - To assist users in setting and adhering to their financial goals, whether they're short-term or long-term, personal or household based.
  - To display users' financial data in a clear and concise manner, allowing them to easily identify areas of improvement and make adjustments accordingly.

- ➡️ Target Audience

  BudgetBuddy is designed for individuals seeking a simplified and effective way to manage their personal finances. It's ideal for those who find existing financial tools too complex or cumbersome and are looking for an intuitive solution to track their spending, savings, and financial progress.

- ➡️ Benefits

  - Ease of Use: BudgetBuddy offers a clean, intuitive interface that makes financial tracking effortless.
  - Financial Clarity: Users gain a clear understanding of their financial situation, helping them make better money management decisions.
  - Goal Achievement: By tracking expenses and income, users can more effectively reach their savings and spending goals.
  - Accessibility: BudgetBuddy's responsive design ensures that users can manage their finances anytime, anywhere, across various devices.

## Tech
- [HTML](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [CSS :root variables](https://www.w3schools.com/css/css3_variables.asp) used for reusable styles throughout the site.
- [CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp) used for an enhanced responsive layout.
- [CSS Grid](https://www.w3schools.com/css/css_grid.asp) used for an enhanced responsive layout.
- [JavaScript](https://www.javascript.com) used for user interaction on the site.
- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [GitHub Pages](https://pages.github.com) used for hosting the deployed front-end site.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Codeanywhere](https://codeanywhere.com) used as a cloud-based IDE for development.
- [Bootstrap](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Materialize](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [Flask](https://flask.palletsprojects.com) used as the Python framework for the site.
- [Django](https://www.djangoproject.com) used as the Python framework for the site.
- [MongoDB](https://www.mongodb.com) used as the non-relational database management with Flask.
- [SQLAlchemy](https://www.sqlalchemy.org) used as the relational database management with Flask.
- [ElephantSQL](https://www.elephantsql.com/) used as the relational database management.
- [ElephantSQL](https://www.elephantsql.com) used as the Postgres database.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com) used for online static file storage.

## Credits

- [StartBootstrap Small Business Template](https://startbootstrap.com/theme/small-business) - for the template used to create the foundations of the BudgetBuddy website.
- [Cooolours](https://coolors.co/) - for the colour palette used in the BudgetBuddy website.
- [Adobe XD](https://www.adobe.com/au/products/xd.html) - for the wireframes used to design the BudgetBuddy website.
- [Unsplash](https://unsplash.com/) - for the images used on the About page.
- [ChatGPT](https://chat.openai.com/) - Logo Design: ChatGPT played a crucial role in conceptualizing and creating the logo for our website.
- [ChatGPT](https://chat.openai.com/) The tool also assisted in formalizing and refining the content for our website, ensuring clarity and coherence in our messaging.

