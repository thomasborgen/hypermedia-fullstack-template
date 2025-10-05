# Setup

To install dependencies use (uv)[https://docs.astral.sh/uv/getting-started/installation/]

```sh
uv sync
```

We also use `ruff` for formatting, so make sure that runs in your IDE on save.


## Concept of an App

An app is something that has a link in the menu and solves a problem. Good examples are: Receive, Pick, Transfer.

All apps have a folder int he `/server/{here}` folder.

All apps have their own `router.py` that handles all http trafic to the endpoints of the app.

### Schema

> Schema are the classes for transporting data in a typed way.

Most of the times the classes in the `schema.py` are used as a base for the Database Models.

However, sometimes we use it as a dataclass for endpoints or structured data transfer in between services/functions.

### Models

> Models are classes that represent the database schema.

We use SQLModel as an ORM. SQLModel is built ontop of `pydantic` and `SQLAlchemy` and joins the two worlds in one model. By doing this our database model can inherit from the base models.


### Views

> Views are html pages that are directly navigatable to by url.

All apps have a `views` folder with at least an `index.py`.

### Partials

> Partials are html snippets that endpoints can respond with when there is no navigation.

Partials are good for updating parts of the page with new data. For example you add a new order line to the orders. The create new orderline POST endpoint can then respond with a partial that inserts itself into an order line table with htmx.

Some apps have their own database models. They s
