# Gudlft
## Description:
Project 11 OpenClassrooms Path  -  Gudlft  -- Improve a Python web application through testing and debugging

Güdlft is a company that has created a digital platform to coordinate strength competitions. 
Güdlft has set up a team called Regional Outreach to create a lighter (and cheaper) version of 
their current platform for regional organisers. The aim of the application is to streamline the 
management of competitions between clubs. 

The prototype is stored in this [GitHub repository](https://github.com/OpenClassrooms-Student-Center/Python_Testing).
In the issue section of this repository are bugs to fix and features to implement. The second step 
is to create functional and integration tests to make sure the functionality.

To implement unit tests, in branch `modification/server` I add functions to be able to make 
unit tests for a single function. In branch `tests/server` there are several unit tests. These two 
branches are not integrated into `QA` or `main`. 


## Installation:
open terminal
1. clone the repository: `git clone https://github.com/DoriDoro/Gudlft.git`
2. go to folder: `cd Gudlft`
3. install the virtual environment: `python3 -m venv venv`
4. activate the virtual environment: `. venv/bin/activate` on MacOS and Linux and `venv\Script\activate` on Windows
5. install all dependencies with: `pip install -r requirements.txt`
6. run the server:
```
export FLASK_APP=server
export FLASK_ENV=development
flask run
```


## Skills:
- Implement a Python test suite
- Handling errors and exceptions in Python
- Configure a Python environment
- Debug the code of a Python application


## Visualisation:
**1. Home Page** <br>
![home page](README_images/Gudlft_homepage.png)
<br>
<hr>

**2. Dashboard** <br>
![Dashboard](README_images/Gudlft_dashboard.png)
<br>

**3. Show Summary** <br>
![show summary](README_images/Gudlft_show-summary.png)
<br>

**4. successful purchase of places** <br>
![successful purchase](README_images/Gudlft_successful_purchase.png)
<br>

**5. Error when purchase more than 12 places** <br>
![Error 12 places](README_images/Gudlft_Error_more_12.png)
<br>

**6. Error when purchase more places than points available** <br>
![Error more places than points](README_images/Gudlft_Error_much_places.png)
<br>

**7. Error when competition is over** <br>
![Error competition over](README_images/Gudlft_Error_competition_over.png)
<br>
