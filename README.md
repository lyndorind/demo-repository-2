# Demo Repository API

A small FastAPI application with one endpoint that echoes a message.

## Run the application

Install the project dependencies with [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Start the development server:

```bash
uv run fastapi dev
```

The API is available at `http://127.0.0.1:8000`. FastAPI's interactive documentation is available at `http://127.0.0.1:8000/docs`.

## Use the echo endpoint

Send a message in the URL:

```bash
curl http://127.0.0.1:8000/echo/hello
```

The response is:

```json
{"message":"hello"}
```

To run the application without the development auto-reloader:

```bash
uv run fastapi run
```

## Configure PostgreSQL

Set `DATABASE_URL` to a SQLAlchemy PostgreSQL connection URL:

```bash
export DATABASE_URL="postgresql+psycopg://postgres:postgres@localhost:5432/tasks"
```

The default is the same connection string above. The application creates the `tasks` table at startup.

## Manage tasks

List tasks:

```bash
curl http://127.0.0.1:8000/tasks
```

Create a task:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Write documentation"}'
```

Delete a task by ID:

```bash
curl -X DELETE http://127.0.0.1:8000/tasks/1
```