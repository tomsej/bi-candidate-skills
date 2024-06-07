# Python Test

This test is used to test your basic Python knowledge. Do not worry if you do not know how to solve everything!

## Prepare

- We suppose you have your Python and some IDE (e.g. VSCode) installed.
- Install `requirements.txt`:
```
pip install -r requirements.txt
```
- install `api_holidays` in interactive mode:
```
pip install -e .
```
- test that everything is working by running:

```
api-holidays 
```
- test that pytest is running:
```
pytest
```

## Assignment

1. Currently the script is only `printing` results into stdout. Write result into file `{year}.json`.

2. Allow `year` parametrization. In original script the year is hard-coded. Allow parametrization from terminal. So I can run e.g. `api-holidays -y 2020` and will download and store list of holidays for year 2020.

3. Write some tests. Please use `pytest` for that. You can mock http call or test original api endpoint.

Create new branch e.g. `novakj` (user surname + first letter of your name - e.g. Jan Novák => `novakj`) and push this branch to git.

Test should take **<1 hour**.

**Good luck!!**