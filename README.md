# To-Do App

A small task-tracking web app made with Django. Create tasks, see them all on one page, update their details, tick them off when they're done, and remove them when they're no longer needed. Everything is saved in a local SQLite database, so there is nothing extra to set up.

## What It Can Do

- Show every task in a table with its title, description, completion checkbox, status text, creation date, and action buttons
- Create a task with a title and a description
- Edit the title and description of an existing task
- Delete a task
- Mark a task as done or pending by clicking its checkbox (the page saves it automatically)
- Display a "No Task Yet" message when there are no tasks

## Built With

- Python 3 and Django 6.1
- SQLite (the default Django database)
- Django templates for the HTML pages
- Plain CSS, with no front-end frameworks

## Project Structure

```
manage.py                     # Django command-line utility
db.sqlite3                    # SQLite database (stores the tasks)

todo_project/                 # Django project (configuration)
├── __init__.py
├── settings.py               # Project settings
├── urls.py                   # Root URL config (admin + includes todo_app.urls)
├── wsgi.py                   # WSGI entry point
└── asgi.py                   # ASGI entry point

todo_app/                     # Django app (the actual to-do logic)
├── __init__.py
├── admin.py                  # (empty) admin registrations
├── apps.py                   # App config (TodoAppConfig)
├── models.py                 # todo_table model
├── views.py                  # home, add, edit, delete, complete views
├── urls.py                   # App-level routes
├── tests.py                  # (empty) tests
└── migrations/
    ├── __init__.py
    └── 0001_initial.py       # Creates the todo_table table

templates/
├── home.html                 # Task list page
├── add_task.html             # Add-task form
├── edit_task.html            # Edit-task form
└── navbar.html               # Shared header, included in other pages

static/css/
├── home.css                  # Styles for the task list
├── add_task.css              # Styles for add/edit forms
└── navbar.css                # Styles for the header
```

All of these sit inside `Assignment_to_do/todo_project/`, the folder that contains `manage.py`.

## How the Code Works

### The model

The app stores its data in one model, `todo_table`, defined in `todo_app/models.py`:

| Field         | Type                               | Purpose                                  |
|---------------|------------------------------------|------------------------------------------|
| `Title`       | `CharField(max_length=50)`         | Short name of the task                   |
| `Description` | `CharField(max_length=100)`        | More detail about the task               |
| `Done`        | `BooleanField(default=False)`      | `True` once the task is completed        |
| `Created`     | `DateTimeField(auto_now_add=True)` | Filled in automatically when created     |

### The routes

All routes are declared in `todo_app/urls.py`. The project's main `urls.py` also exposes Django's built-in `/admin/` page.

| Path               | View             | URL name         | What it does                          |
|--------------------|------------------|------------------|---------------------------------------|
| `/`                | `home`           | `home`           | Lists all tasks                       |
| `/add/`            | `add_task`       | `add_task`       | Shows the form and saves a new task   |
| `/edit/<id>/`      | `edit_task`      | `edit_task`      | Shows the form and updates a task     |
| `/delete/<id>/`    | `delete_task`    | `delete_task`    | Deletes a task                        |
| `/complete/<id>/`  | `task_completed` | `task_completed` | Sets a task as done or not done       |

### The views

The functions in `todo_app/views.py` behave as follows:

- **`home`** loads every task from the database and passes them to `home.html`.
- **`add_task`** displays an empty form for a normal visit. When the form is submitted, it creates a new task and sends the user back to the home page.
- **`edit_task`** finds the task by its ID and fills the form with its current values. On submit, it saves the changes only if both the title and the description are filled in, then returns to the home page.
- **`delete_task`** removes the chosen task and returns to the home page.
- **`task_completed`** accepts a POST request from the checkbox form. A ticked checkbox sets `Done` to `True`, and an unticked one sets it to `False`. Then it returns to the home page.

### The pages and styles

- `navbar.html` holds the "To-Do App" heading and the **Add Task** button. The other pages include it at the top.
- `home.html` loops through the tasks and draws one table row for each. Every row has Edit and Delete buttons and a checkbox inside a small form that submits itself whenever the checkbox changes.
- `add_task.html` and `edit_task.html` are the two form pages, and both are styled by `add_task.css`.
- In `settings.py`, `templates/` is registered as the template folder (`TEMPLATES["DIRS"]`) and `static/` as the static files folder (`STATICFILES_DIRS`).

## Running the Project on a Mac

You'll need Python 3 installed. Check with `python3 --version`. If it's missing, install it with `brew install python` or from [python.org](https://www.python.org/downloads/macos/).

1. **Open Terminal and go to the project folder** (the one that contains `manage.py`). Change the path to wherever you unzipped the files:

   ```bash
   cd ~/Downloads/Assignment_to_do/todo_project
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   If the zip already contains a `venv` folder that doesn't work, delete it with `rm -rf venv` and run the commands above again.

3. **Install Django:**

   ```bash
   pip install django
   ```

4. **Set up the database.** The migration file is already included, so you only need to run:

   ```bash
   python manage.py migrate
   ```

5. **Start the server:**

   ```bash
   python manage.py runserver
   ```

6. **Open the app** at <http://127.0.0.1:8000/>. Press `Control + C` in Terminal to stop the server, and run `deactivate` to leave the virtual environment.

If port 8000 is busy, use another one, for example `python manage.py runserver 8080`.

## Notes

- `DEBUG = True` and the default `SECRET_KEY` are meant for local use only. Change them before putting the app online.
- The time zone in `settings.py` is set to `Asia/kolkata`.
- Deleting works through a normal link (a GET request), so a stricter version would use a POST form.
- In `edit_task.html`, the title input's `value` isn't wrapped in quotes, so a title with spaces can appear cut off in the edit form. Adding quotes around `{{ task_data.Title }}` fixes this.