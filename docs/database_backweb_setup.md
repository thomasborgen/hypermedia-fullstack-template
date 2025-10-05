env variables.
```sh
POSTGRES_BACKWEB_USER="postgres_backweb"
POSTGRES_BACKWEB_DB="backweb"
POSTGRES_BACKWEB_PASSWORD="local"
BACKWEB_SECRET_KEY="supersecret"
```

1. Create database with Adminer

call the database `backweb`

2. Create a new user with adminer in normal sql:

> Remember to change the password. and store the password in bitwarden

```sql
CREATE USER postgres_backweb WITH PASSWORD '<changeme>';ALTER DATABASE backweb OWNER TO postgres_backweb;
```

Or Create new user with `psql` through `docker` and set it as owner of backweb

```sh
docker exec -u postgres server-db-1 psql -c "CREATE USER postgres_backweb WITH PASSWORD '<changeme>';ALTER DATABASE backweb OWNER TO postgres_backweb;"
```

If you made a mistake and need to delete the user:

```sh
docker exec -u postgres server-db-1 psql -c 'DROP USER postgres_backweb;ALTER DATABASE backweb OWNER TO postgres_backweb;'
```

3. Add environment variables to github actions vars and secrets.

vars:

```sh
POSTGRES_BACKWEB_USER="postgres_backweb"
POSTGRES_BACKWEB_DB="backweb"
```

secrets:

> Use backweb password you put in bitwarden. Remember to put the secret_key in bitwarden.

```sh
POSTGRES_BACKWEB_PASSWORD="local"
BACKWEB_SECRET_KEY="supersecret"
```

```sh
POSTGRES_BACKWEB_PASSWORD_STAGING="local"
BACKWEB_SECRET_KEY_STAGING="supersecret"
```

4. Deploy backweb by deploying the code to the environment.
