#!/usr/bin/env python
print "Content-Type: text/html"
print ""
import cgi
form = cgi.FieldStorage()
import csv
try:
    firstName = str(form["fn"].value).replace(" ", "")
except:
    firstName = "null"
else:
    pass

try:
    lastName = str(form["ln"].value).replace(" ", "")
except:
    lastName = "null"
else:
    pass

if firstName == "null" or lastName == "null":
    emptyNames = True
else:
    emptyNames = False

if emptyNames == False:
    with open("nrgAttendance.csv") as csvfile:
        cr = csv.DictReader(csvfile)
        for row in cr:
        #print row
        #print (row['First Name'] + " " + row['Last Name'])
            if row['First Name'].replace(" ", "").lower() == firstName.replace(" ", "").lower() and row['Last Name'].replace(" ", "").lower() == lastName.replace(" ", "").lower():
                dictionary = row
                del dictionary['First Name']
                del dictionary['Last Name']
                
                #Checks amount of date avaliable and how much he/she attended and stores these in a variable
                dateCount = 0
                attendedCount = 0
                for x in dictionary:
                    dateCount = dateCount + 1
                    if dictionary[x].lower() == "x":
                        attendedCount = attendedCount + 1
                percentage = (float(attendedCount) / dateCount) * 100

html_escape_table = {
    "&": "&amp;",
    '"': "\"",
    "'": "\\'",
    ">": "&gt;",
    "<": "&lt;",
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)

def convertDate(inDate):
    if inDate == "Design Day 1" or inDate == "Design Day 2" or inDate == "Kickoff":
        if inDate == "Design Day 1":
            return '2016-01-09'
        if inDate == "Kickoff":
            return '2016-01-09'
        if inDate == "Design Day 2":
            return '2016-01-10'
    else:
        month = inDate[:inDate.find("/")]
        day = inDate[inDate.find("/") + 1:inDate.find("/",inDate.find("/") + 1)]
        year = inDate[inDate.find("/",inDate.find("/") + 1) + 1:]
        if len(month) == 1:
            month = str(0) + month
        if len(day) == 1:
            day = str(0) + day
        return str(year) + "-" + str(month) + "-" + str(day)


print """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Newport Robotics Group Outreach Hours Lookup.">
    <meta name="author" content="Jeremy Zhang">

    <title>NRG Attendance Record Lookup</title>

    <!-- Bootstrap Core CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    
    <!-- Custom CSS -->
    <link href="assets/css/logo-nav.css" rel="stylesheet">
    <link href="assets/css/custom.css" rel="stylesheet">
    
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
    
    <!-- Github Fork -->
    <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.1.1/gh-fork-ribbon.min.css" />
    <!--[if lt IE 9]>
        <link rel="stylesheet" href="http://cdnjs.cloudflare.com/ajax/libs/github-fork-ribbon-css/0.1.1/gh-fork-ribbon.ie.min.css" />
    <![endif]-->
    
    <link href="assets/css/responsive-calendar.css" rel="stylesheet">
    
    <!-- Favicons -->
    <link rel="apple-touch-icon" sizes="57x57" href="assets/icn/apple-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="assets/icn/apple-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="assets/icn/apple-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="assets/icn/apple-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="assets/icn/apple-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="assets/icn/apple-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="assets/icn/apple-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="assets/icn/apple-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="assets/icn/apple-icon-180x180.png">
    <link rel="icon" type="image/png" sizes="192x192"  href="assets/icn/android-icon-192x192.png">
    <link rel="icon" type="image/png" sizes="32x32" href="assets/icn/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="96x96" href="assets/icn/favicon-96x96.png">
    <link rel="icon" type="image/png" sizes="16x16" href="assets/icn/favicon-16x16.png">
    <link rel="manifest" href="assets/icn/manifest.json">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="msapplication-TileImage" content="assets/icn/ms-icon-144x144.png">
    <meta name="theme-color" content="#ffffff">
</head>

<body>
    
    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <!-- Fork Github -->
        <div class="github-fork-ribbon-wrapper right">
            <div class="github-fork-ribbon">
                <a href="https://github.com/EndenDragon/nrgAttendance.cf">View me on GitHub</a>
            </div>
        </div>
        
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <a class="navbar-brand">
                    <img src="assets/img/logo.png" alt="">
                </a>
            </div>
            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li>
                        <a>Newport Robotics Group 948 Attendance</a>
                    </li>
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Content -->
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <a href="http://nrgOutreach.cf/"><button type="button" class="btn btn-warning btn-lg pull-right">Check your outreach hours!</button></a>
                <h1>NRG Attendance Lookup</h1>
                <p>By Jeremy Zhang</p>
                
                <div class="col-md-8">
                <form action="nrgAttendance.py" method="get" id="nameForm">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h3 class="panel-title">Record Lookup</h3>
"""

if emptyNames == False:
    print """<div class="pull-right" style="position: relative; top: -20px;"><a href="nrgAttendance.py"><button type="button" class="btn btn-danger btn-xs">Clear</button></a></div>"""

print """
            </div>
                        <div class="panel-body">
                            <div class="input-group input-group-lg">
                                <span class="input-group-addon" id="sizing-addon1"><span class="glyphicon glyphicon-user" aria-hidden="true"></span></span>
                                <input type="text" class="form-control" placeholder="First Name" aria-describedby="sizing-addon1" name="fn" id="fn" data-provide="typeahead" autocomplete="off" required>
                                <input type="text" class="form-control" placeholder="Last Name" aria-describedby="sizing-addon1" name="ln" id="ln" data-provide="typeahead" autocomplete="off" required>
                                <span class="input-group-addon">
                                    <button class="btn btn-default btn-large" type="button submit" value="Submit">Submit <span class="glyphicon glyphicon-ok" aria-hidden="true"></span></button>
                                </span>
                            </div>
                        </div>
"""

if emptyNames == False:
    print """
                                <div class="well well-sm">
                                <center><p style="color: #333;"><b>"""
    print str(form["fn"].value).replace(" ", "") + " " + str(form["ln"].value).replace(" ", "")+"'s"
    print """Attendance Record</b><br></p></center>
                                
                                <!-- Responsive calendar - START -->
                                  <div class="responsive-calendar" style="color: black;">
                                  <div class="controls">
                                      <a class="pull-left" data-go="prev"><div class="btn btn-primary btn-lg">Prev</div></a>
                                      <h4><span data-head-month></span> <span data-head-year></span></h4>
                                      <a class="pull-right" data-go="next"><div class="btn btn-primary btn-lg">Next</div></a>
                                  </div><hr/>
                                  <div class="day-headers">
                                    <div class="day header">Sun</div>
                                    <div class="day header">Mon</div>
                                    <div class="day header">Tue</div>
                                    <div class="day header">Wed</div>
                                    <div class="day header">Thu</div>
                                    <div class="day header">Fri</div>
                                    <div class="day header">Sat</div>
                                  </div>
                                  <div class="days" data-group="days">
                                  </div>
                                </div>
                                <!-- Responsive calendar - END -->
                                <p style="color: darkgrey;"><i>Dates that are highlighted are the ones you have attended.</i></p>
                                <hr>
                                <h4 style="color: black;"><strong>Percentage of attendance: """
    
    try:
        print percentage
        nonExistant = False
    except:
        print """<div class="alert alert-danger" role="alert">Name lookup failed! Make sure you had typed it correctly. Else if this problem keeps happening, please contact Catherine or Jeremy.</div>"""
        nonExistant = True
    else:
        pass
    print """%</strong></h4>
                             </div>
    """
print """
                    </div>
                </form>
                </div>
                <div class="col-md-4">
                    <div class="panel panel-default" style="color: #333;">
                        <div class="panel-heading">
                            <h3 class="panel-title">Friendly Attendance Reminder</h3>
                        </div>
                        <div class="panel-body">
                            <p>In order to be considered "active" in NRG948, one must maintain a 67% attendance record. In addition, participating in Kickoff and Design Days is also required to attend competition, especially if you need a carpool to get there.</p>
                            <br />
                            <p>Important Dates to Know~</p>
                            <ul>
                              <li>Kickoff - 1/9/2016</li>
                              <li>Design Day 1 - 1/9/2016</li>
                              <li>Design Day 2 - 1/10/2016</li>
                            </ul>
                            <br />
                            <strong>Please note that the attendance record may not always be up to date. If you have any concerns whatsoever regarding your attendance, please contact <a href="http://www.google.com/recaptcha/mailhide/d?k=01fyJ02hhRlJ2wpXPt6vUO9Q==&amp;c=-CuFxqD7ke3K1FbvTscm_ZcPs8lFMjvyCXC_8leIWX4=" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k\07501fyJ02hhRlJ2wpXPt6vUO9Q\75\75\46c\75-CuFxqD7ke3K1FbvTscm_ZcPs8lFMjvyCXC_8leIWX4\075', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">Catherine Shea</a>. Otherwise, if there are issues with the website itself, please contact <a href="http://www.google.com/recaptcha/mailhide/d?k=01RIMdNVOxm2VAq0S11ck4rQ==&amp;c=FcLtQqSHKRW6hOb0I51FKzPVpTFZGQeUC25IpgtfTE8=" onclick="window.open('http://www.google.com/recaptcha/mailhide/d?k\07501RIMdNVOxm2VAq0S11ck4rQ\75\75\46c\75FcLtQqSHKRW6hOb0I51FKzPVpTFZGQeUC25IpgtfTE8\075', '', 'toolbar=0,scrollbars=0,location=0,statusbar=0,menubar=0,resizable=0,width=500,height=300'); return false;" title="Reveal this e-mail address">Jeremy Zhang</a>. Thank you.</strong>
                        </div>
                    </div>
                </div>
                    <p class="pull-right" style="color: yellow;">&copy; 2015<script>new Date().getFullYear()>2010&&document.write("-"+new Date().getFullYear());</script>, by Jeremy Zhang.</p>
            </div>
        </div>
    </div>
    <!-- /.container -->

    <!-- jQuery -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    
    <!-- Bootstrap Core JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-3-typeahead/4.0.0/bootstrap3-typeahead.js"></script>
    
    <!-- Responsive Calendar -->
    <script src="assets/js/responsive-calendar.js"></script>
"""

if emptyNames == False and nonExistant == False:
    print """
        <!-- Calendar Data -->
    <script type="text/javascript">
      $(document).ready(function () {
        $(".responsive-calendar").responsiveCalendar({
          startFromSunday: true,
          events: {""",
    for key in dictionary:
        if dictionary[key] == "x":
            print '"' + convertDate(key) + '":{},',

    print """
            }
        });
      });
    </script>
    """

print """
    <!-- First Names typeahead -->
    <script>
        var jsonString = '[""",
fnList = []
fnJSON = ""

with open("nrgAttendance.csv") as csvfile:
        cr = csv.DictReader(csvfile)
        for row in cr:
            if fnList.count(row['First Name']) == 0:
                fnList.append(row['First Name'])
for fn in fnList:
    fnJSON = fnJSON + '''{"label":"''' + html_escape(fn) + '''"},'''
print fnJSON[0:len(fnJSON) - 1],

print """]';
         
        var jsonObj = $.parseJSON(jsonString);
        var sourceArr = [];
         
        for (var i = 0; i < jsonObj.length; i++) {
           sourceArr.push(jsonObj[i].label);
        }
         
        $("#fn").typeahead({
           source: sourceArr
        });
    </script>
    
    <!-- Last Names typeahead -->
    <script>
        var jsonString = '[""",

lnList = []
lnJSON = ""

with open("nrgAttendance.csv") as csvfile:
        cr = csv.DictReader(csvfile)
        for row in cr:
            if lnList.count(row['Last Name']) == 0:
                lnList.append(row['Last Name'])
for ln in lnList:
    lnJSON = lnJSON + '''{"label":"''' + html_escape(ln) + '''"},'''
print lnJSON[0:len(lnJSON) - 1],

print """]';
         
        var jsonObj = $.parseJSON(jsonString);
        var sourceArr = [];
         
        for (var i = 0; i < jsonObj.length; i++) {
           sourceArr.push(jsonObj[i].label);
        }
         
        $("#ln").typeahead({
           source: sourceArr
        });
    </script>
    
</body>

</html>
"""