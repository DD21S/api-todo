# ToDo

API to manage tasks and reminders. Made with FastAPI, super fast and well documented thanks to OpenAPI. Use SQLAlchemy like ORM and Pydantic for models.

## Quickstart

First of all, clone this repo.

```
git clone https://github.com/DD21S/api-todo.git
```

Create a file with the name ``.env`` and set the environment variables. In this way:

```
USER_DATABASE=username
PASSWORD_DATABASE=123456789
HOST_DATABASE=localhost
NAME_DATABASE=todo
```

Then, you install the requirements.

```
pip install -r requirements.txt
```

Run the API:

```
uvicorn main:app --reload
```

Ready, now your API is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create and activate one with these commands:

```
python3 -m venv venv
source venv/bin/activate
```

## Routes

| **METHOD**  | **ROUTE**                | **FUNCTIONALITY**              |
| ----------- | ------------------------ | ------------------------------ |
| **GET**     | /tasks                   | Displays all tasks             |
| **POST**    | /tasks                   | Create a new task              |
| **GET**     | /tasks/{task_id}         | Get a task                     |
| **PUT**     | /tasks/{task_id}         | Update a task                  |
| **DELETE**  | /tasks/{task_id}         | Delete a task                  |
| **PATCH**   | /tasks/{task_id}         | Change status of the task      | 
