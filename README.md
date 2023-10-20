# dummy Flask project with MongoDB

folder structure

```
app/
  __init__.py - app factory function which - connects to db, registers api/v1 blueprint, & returns the app instance
  api/
    v1/
      __init__.py - registers blueprints of the following modules
      knowledge/
        controller.py
        helpers.py (if needed)
        routes.py
      llm/
        controller.py
        helpers.py (if needed)
        routes.py
      webhooks/
        controller.py
        helpers.py (if needed)
        routes.py
      ...
  constants/
    knowledge_file.py
    ...
  helpers/
    apify.py
    ...
  models/
    knowlede_file.py
    ...
  utils/
    db.py - to connect to mongodb
    validation.py
    ...
runner.py - runs the app
```
