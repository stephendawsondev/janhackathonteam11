You can find the live deployed application on [Heroku](https://budgetbuddy2-38958568c907.herokuapp.com/). This link will take you to the live version of your project.

### ElephantSQL Database

This project relies on [ElephantSQL](https://www.elephantsql.com) for the PostgreSQL Database. To set up your own Postgres Database, follow these steps:

1. Click on **Create New Instance** to start a new database.
2. Provide a name, which is often the name of the project (e.g., "janhackathonteam11").
3. Choose the **Tiny Turtle (Free)** plan.
4. Leave the **Tags** field blank.
5. Select the **Region** and **Data Center** closest to your location.
6. Once created, click on the new database name to access the database URL and Password.

### Cloudinary API

This project utilizes the [Cloudinary API](https://cloudinary.com) to store media assets online because Heroku doesn't persist this type of data. To obtain your Cloudinary API key, follow these steps:

1. Create an account on Cloudinary and log in.
2. For your *Primary interest*, select *Programmable Media for image and video API*.
3. Optionally, edit your assigned cloud name to something more memorable.
4. On your Cloudinary Dashboard, copy your **API Environment Variable**.
5. Ensure you remove the `CLOUDINARY_URL=` as part of the API **value**; this is the actual **key**.

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that allows developers to build, run, and operate applications entirely in the cloud. Follow these deployment steps after setting up your Heroku account:

1. In your Heroku Dashboard, select **New** in the top-right corner and choose **Create new app** from the dropdown menu.
2. Provide a unique app name, choose a region closest to you (EU or USA), and select **Create App**.
3. In the new app's **Settings**, click **Reveal Config Vars** and set your environment variables as follows:

   | Key                  | Value                                                                                                                                                  |
   | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | `CLOUDINARY_URL`     | cloudinary://423928569512371:Xds6g-KgHTsH_8ayPkb0vci23l4@ddll4c0zo                                                                                    |
   | `DATABASE_URL`       | postgres://fvnucmpd:fTkWXzsFK1mmwYZ6t7vlNHWNBpJz2DAd@manny.db.elephantsql.com/fvnucmpd                                                             |
   | `DISABLE_COLLECTSTATIC` | 1 (*temporary, can be removed for the final deployment*)                                                                                                |
   | `SECRET_KEY`         | 15q8j@52(%vztw)qq!&jnxlf-n%-nq60m9asb1-nv14hx+_q6u                                                                                                   |

4. Heroku requires two additional files for proper deployment: `requirements.txt` and `Procfile`. Install this project's **requirements** with:

   ```bash
   pip3 install -r requirements.txt
   ```

   If you have your own installed packages, update the requirements file using:

   ```bash
   pip3 freeze --local > requirements.txt
   ```

5. Create a **Procfile** with the following command:

   ```bash
   echo web: gunicorn app_name.wsgi > Procfile
   ```

   Replace **app_name** with your primary Django app's name, the folder where settings.py is located.

6. To connect your GitHub repository to the app, you can either choose **Automatic Deployment** from the Heroku app or use the Terminal/CLI:

   - Connect to Heroku: `heroku login -i`
   - Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
   - After standard Git `add`, `commit`, and `push` to GitHub, deploy to Heroku with:

     ```bash
     git push heroku main
     ```

Your project should now be connected and deployed to Heroku.

You can access the deployed project at [http://your-deployed-link.com](https://budgetbuddy2-38958568c907.herokuapp.com/).

### Local Deployment

This project can be cloned or forked to create a local copy on your system.

For either method, you'll need to install any necessary packages from the *requirements.txt* file:

```bash
pip3 install -r requirements.txt
```

Create a new file called `env.py` at the root-level and include the same environment variables from the Heroku deployment steps. Here's a sample `env.py` file:

```python
import os

os.environ.setdefault("CLOUDINARY_URL", "cloudinary://423928569512371:Xds6g-KgHTsH_8ayPkb0vci23l4@ddll4c0zo")
os.environ.setdefault("DATABASE_URL", "postgres://fvnucmpd:fTkWXzsFK1mmwYZ6t7vlNHWNBpJz2DAd@manny.db.elephantsql.com/fvnucmpd")
os.environ.setdefault("SECRET_KEY", "15q8j@52(%vztw)qq!&jnxlf-n%-nq60m9asb1-nv14hx+_q6u")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, you can run it locally by following these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (if applicable): `python3 manage.py loaddata file-name.json` (repeat for each file)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

#### Cloning

To clone the repository, follow these steps:

1. Go to the [GitHub repository](https://github.com/JesseRoss001/janhackathonteam11).
2. Locate the "Code" button above the list of files and click it.
3. Select your preferred cloning method (HTTPS, SSH, or GitHub CLI) and click the copy button to copy the URL to your clipboard.
4. Open Git Bash or Terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:

   ```bash
   git clone https://github.com/JesseRoss001/janhackathonteam11.git
   ```

7. Press Enter to create your local clone.

If you are using Gitpod, you can create your own workspace using this repository by clicking the "Open in Gitpod" button. Note that you need to have the Gitpod browser extension installed for direct project opening in Gitpod.

#### Forking

Forking the GitHub Repository creates a copy of the original repository on your GitHub account. It allows you to view and make changes without affecting the original owner's repository. Here's how to fork this repository:

1. Log in to GitHub and visit the [GitHub Repository](https://github.com/JesseRoss001/janhackathonteam11).
2. Above the "Settings" button on the repository's menu, locate the "Fork" button.
3. Click the "Fork" button.
4. You should now have a copy of the original repository in your GitHub account.
