# nrgAttendance.cf

**By Jeremy Zhang - [http://nrgAttendance.cf](http://nrgAttendance.cf/)**

Newport Robotics Group (NRG948) Attendance Site

Make any changes/fixes that are needed and submit a pull-request! Thank you for your contribution! :)

## Files

**Significant files and their purpose**

* index.html - Static HTML file redirecting to nrgAttendance.py, incase the 301 redirect from `.htaccess` fails.
* nrgAttendance.py - Python CGI file. Takes the name, process the `nrgAttendance.csv` file, and display the output. The python file is a standalone. If no parameters are given, it will show the barebones, otherwise, it either shows an error, or processes the request.
* nrgAttendance.csv - User data to be processed.
* /assets - Javascript, CSS, imgs, & more!

## URL Format

Url format example for nrgOutreach.py to process: `http://nrgAttendance.cf/nrgAttendance.py?fn=Jeremy&ln=Zhang`

* First Name (fn): Jeremy
* Last Name (ln): Zhang