# Strange behaviour with sub apps

```
poetry install
poetry run pytest tests
```
```
FAILED tests/test_app.py::test_read_sub - RuntimeError: Caught handled exception, but response already started.
```