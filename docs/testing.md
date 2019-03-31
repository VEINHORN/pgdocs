# Testing

If you want to run specific test in module, run below command:

```shell
python -m unittest tests.test_profile
```

That command will be run `test_profile.py` file from `tests` module.

For testing specific class run:

```shell
python -m unittest tests.test_profile.TestProfile
```

Type below command to run all tests from `tests` folder:

```shell
python -m unittest discover -s tests
```
