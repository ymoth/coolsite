### Installing..

Первым делом установим python3.10
https://www.python.org/downloads/release/python-3100/ <br>
После успешной установки, установим нужный нам модули, пропишем в консоль Win+R -> cmd ->

```
python -m pip install pillow
python -m pip install django
python -m pip install django-recaptcha
```

__После успешной установки, запускаем сам сервер__

```cmd
python manage.py runserver
```

***
Ответ от сервера

```
Django version 4.1.6, using settings 'coolsite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Пример:
![image](https://user-images.githubusercontent.com/69197682/221411888-55946ca5-959f-4b48-b9ab-3adb649673ca.png)

Веб-сайтик, построенный на Django. Авторизованная модельнизация на ООП.
![image](https://user-images.githubusercontent.com/69197682/221411843-63159332-55f4-43da-b079-dcb2038d2f03.png)
