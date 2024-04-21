This is the readme file for the repository.

# Setting up the website locally
* Install all the required packages and download the entire repository locally.

* Then, import the CSVs into MySQL databases. Go to the "assignment.py" file and enter your MySQL credentials into MySQL.connector (Ensure that the database and the tables are under the correct name)

* Run the assignment.py file, you will receive the link to a locally hosted website. Open the link in any web browser, and you will be up and running.


# Documenting the process
* The Problem_Statement.pdf file has links to the PDFs that contain the data

* After the PDF was converted to CSV (using PyMuPDF library's getTable), the tables were loaded into a MySQL database using MySQL workbench's table import wizard.

* In MySQL, a bit of manual processing was done, like changing the attribute names and their datatypes.

* After this, the data was ready to work with.

* A basic frontend for the website was created using HTML and CSS.

* The front end and the back end of the website were integrated using the Flask library for Python.

* ChartJS was used to display the graphs on the website.

# License
The code in this repository is released under the [MIT license](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt). Read more at the [Open Source Initiative](https://opensource.org/).
