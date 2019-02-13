# Welcome to Bangazon
<div style="text-align:center">
<h1 style="font-weight: bold">Bangazon</h1>
<img src="images/bangazonIcon.png" width="200"/>
</div>

<h2 style="font-weight: bold">E-commerce Site</h2>

<h3>This a a client facing Bangazon e-commerce website. After registering users can browse through
products other users have posted. They can also add items of their own to sell. Items can be view by
category, or searched by keyword.</h3>

<h2 style="font-weight: bold;"> Technologies Used
<h3>Development Languages and Libraries</h3>

<img src="images/python.png"/>______<img src="images/django.jpeg"/>______<img src="images/dbbrowser.png"/>______<img src="images/html5.jpg"/>______<img src="./images/css3.jpg"/>

<h1></h1>
<h3>Development Tools</h3>

<img src="images/lucid.png"/>______<img src="images/slack.png"/>______<img src="images/vs.png"/>______<img src="images/github.jpg"/>


<h2>Instructions for Installing Bangazon</h2>

<h4> You will need to have command line tools installed for your computer to use terminal commands.
</h4>

  * Mac users - Open your terminal and type

    ```sh
    git --version
    ```

  * Linux/Windows users, please vist the [Git page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and follow the instructions for setup

<h4>You will now need to configure your git account. In the terminal window, type</h4>

  ```sh
  git config –global user.name “You Name”
  git config –global user.email “Your Email”
  ```

#### Create a new directory to store the files in. Type this into your terminal window.

  ```sh
  mkdir Bangazon
  cd Bangazon
  git clone https://github.com/garrulous-gobies/Bangazon_1
  ```

#### If you do not have Python version 3 installed on your machine, visit the [Python Download Page](https://www.python.org/downloads/) or to install with command line,

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install python
pip install django
```

#### Now you need to migrate the models into your local folder:
```sh
python manage.py makemigrations
python manage.py migrate
```


#### You can now populate the data by running

```sh
chmod +x django_data.sh
./django_data.sh Bangazon seeder
```

#### You can now run the program by typing:

```sh
python manage.py runserver 8080
```

<h1 style="text-align:center; font-weight: bold;">Congratulations! You are now experiencing Bangazon!

<h2 style="font-weight:bold;text-align:center" > Main functionality of Bangazon</h2>

1. When user clicks Employees in the navigation bar, a list will appear showing all employees.
1. When user clicks Departments in the navigation bar, a list will appear showing all departments.
1. When user clicks on the department's name, the department's details will appear on a new page, showing the budget and the employees in the department.
1. When the user clicks See All Departments, the list of departments will appear.
1. When the user clicks Edit Department, a form pre-populated with the department information will apear.
1. When the user clicks Submit, the department is edited with the information in the input fields, and the list of all departments will be shown.
1. When the user clicks Add a New Department, a form to add a new department is shown.
1. When the user clicks Submit, the department is saved to the database with the information in the input fields, and the list of all departments will be shown.
1. When user clicks Computers in the navigation bar, a list will appear showing all computers.
1. When user clicks Add Computer button, a form appears allowing a user to add a computer and assign it to an employee.
1. From the Computers main page a user can click on a computer to view a computer's details
1. From the Computer Details page, a user can delete a computer if it has never been assigned to an employee and a user can decomission a computer if it is not currently assigned.
1. When user clicks Training Programs in the navigation bar, a list will appear showing all future training programs.
1. When user clicks a specific Training Program while on the Training Programs page, details will appear displaying the Title, Description, Start Date, End Date, Max Enrollment, and Employees that are scheduled to attend.
1. When user is on a specific Training Program page and user clicks Edit Training, a form will appear with the current details displaying the Title, Description, Start Date, End Date, and Max Enrollment with a Save button and a Cancel Edits button.
1. When user clicks Save while on the Edit Training Programs page, the form will be checked for validation and the database will be updated with new information. The user will then be redirected to the main Training Page.
1. When user clicks Cancel Edits while on the Edit Training Programs page, the user will then be redirected to the main Training Page.
1. When user is on a specific Training Program page and user clicks Delete Training, the training will be removed from the database and the user will be redirected to the main Training Program page.
1. When user clicks Past Training Programs while on the Training Programs page, a list will appear showing all past training programs.
1. When user clicks a specific Training Program while on the Past Training Programs page, details will appear displaying the Title, Description, Start Date, End Date, Max Enrollment, and Employees that attended.


<h2 style="text-align: center">Entity Relationship Diagrams</h2>

<img src="images/ERD.png" />

<h2 style="text-align: center; font-weight: bold"> Visual Feature List</h2>

<h3 style="text-align: center">To help you along, here is a visualization of the features, and behaviors of the application to get you started.</h3>

## Viewing the employee list and adding a new employee
![new computer gif](https://github.com/garrulous-gobies/Bangazon_1/blob/nl-readme-gifs/images/employees.gif)

### Viewing the department list and adding a new department
![new departments gif](https://github.com/garrulous-gobies/Bangazon_1/blob/nl-readme-gifs/images/newdepartment.gif)

### Viewing the training programs list and adding a new training program
![new training gif](https://github.com/garrulous-gobies/Bangazon_1/blob/nl-readme-gifs/images/newtraining.gif)

### Editing an existing training programs. Past programs may not be edited.
![edit training gif](https://github.com/garrulous-gobies/Bangazon_1/blob/nl-readme-gifs/images/edittraining.gif)

### Viewing the computer list and adding a new computer
![new computer gif](https://github.com/garrulous-gobies/Bangazon_1/blob/nl-readme-gifs/images/newcomputer.gif)


