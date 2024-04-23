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


# Solutions

1bi) The PDFs were converted to CSV using the Python script saved under the name "pdf_to_csv.py". The CSVs are under the name purchase_data and redemption_data

1bii) These CSVs were then imported to a MySQL database named dcc_assignment using the Workbench's Table Import Wizard
      After a little bit of manual processing, the data looked like as below:


1c) The required front end was created using HTML, CSS, Flask and Bootstrap

# License
The code in this repository is released under the [MIT license](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt). Read more at the [Open Source Initiative](https://opensource.org/).
