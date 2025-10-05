# Backup / Dump db

```sh
docker exec -t server-db-1 pg_dumpall -c -U postgres > dump_`date +%Y-%m-%d"_"%H_%M_%S`.sql
```

# Drop db

```sh
docker exec -it server-db-1 psql -U postgres -d postgres -c "DROP DATABASE app;"
```
# Create db

```sh
docker exec -it server-db-1 psql -U postgres -d postgres -c "CREATE DATABASE app;"
```

# Restore db

```sh
cat dump_2025-03-21_18_28_18.sql | docker exec -i server-db-1 psql -U postgres
```
