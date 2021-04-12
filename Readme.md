# Released ([URL to project](https://anline.pythonanywhere.com/))

_To use the website as seller you have to acess the admin panel_
***you nedd to make a new file named .env in the project main folder &***
***add your gmail and password to the file like this***
```
email=your_email
password=yourpassword
```
& you are ready
***note in settings.py line no 138 there is:
```
STATICFILES_DIRS = [
    BASE_DIR / "ec/static",
]
```
change this to:
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```
***
