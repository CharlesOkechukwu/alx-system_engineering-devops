# Postmortem U+1F3D7 #

During the release of the User management system of the Alx wordpress site at approximately 7:00 pm Greenwich Mean Time(GMT) requests to the server returned a 500 internal server erro instead of a html file which contains the user login page. This made many users unable to login  to thier user accounts within same period.

## Debugging Timeline U+1F41B ##
* Around 7:15pm  Greenwich Mean Time,I recieved a pager notifying mr Bright and myself of an increased read request, we also recieved tickets around 7:20pm grenwich mean time(GMT) notiying us about the 500 internam server error returned by our server.

* I responded to the pager alert around 7:25pm greenwich mean time(GMT), I proceeded in solving the problem, I used ``strace`` and ``termus`` to divide the terminal into two screens. I used one to run the strace, and the other to perform curl requests to the page which returned a ``500 internal server error``.

* I checked that the apache servers were running using ``ps aux`` which confirmed that ``root`` and ``www`` were running properly

* The ``strace`` was ran on the PID of apache which yielded no result, i also proceeded to run ``strace`` on the PID of the www-data process and it yielede a -1 error when tying to access the ``/var/www/html/wp-includes/class-wp-locale.phpp``

* I looked into the wp-settings.php and used pattern matching to located wrong ``.phpp`` extension which i removed in extra p in the extension.

* I now ran a new curl request to the server and a ``200 OK`` signal was returned with the html page of the user management page.

* I now proceeded to write a puppet manifest to automate the above process.

## Root Cause ##
* The error was mainly caused by a mistake during to setting of rules in the ``wp-settings.php`` file which reulted in a typo adding an extra p to the ``.php`` extension

* To fix it I simply corrected the typo in the wp-settings.php file.

## Prevention ##
To prevent such error from occuring further:
* unittests should be carried out on various api endpoints to ensure they are returning the correct status codes.

* Status monitoring should be added to our monitoring packages which would help notify us as the problem is at its early stages to minimize the losses incured due to such error.

* Also with the puppet manifest the respond to such error has been established thus automasting the error correction.

* Automate deployment and configuration of web servers this would now reduce the chances of error when setting up multiple servers.

Hopefully, this error would not occur in this same form again.
