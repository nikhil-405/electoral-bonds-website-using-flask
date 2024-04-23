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


      
![1bii_2](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/1db66c6c-cd67-49c9-aee0-78453890d1a4)
![1bii_1](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/a0d6008a-cce3-4105-aa55-f512b795d58d)


1c) The required front end was created using HTML, CSS, Flask and Bootstrap
![Main UI](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/ca1e9c64-6a69-4fed-a2ec-b01d3599a286)

1d) The frontend was connected to the database using Flask, code for the same has been attached in the assignment.py file

1e) All the codes related to 1e have been attached in the "assignment.py" file

I) ![Screenshot 2024-04-23 120208](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/08a875ac-c79a-42ca-8f0f-0977325e639d)

![Screenshot 2024-04-23 120305](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/ab5fd479-dccc-4bcd-a03a-5153a189a5b4)

![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/e8ab5970-4257-437c-9e2e-b47dec9a187b)
The filter criteria is a dropdown menu
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/f55b194c-51fd-4914-8a34-d61f231f1b0c)


II) 
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/da40aa4d-339c-437b-8367-c8d8bf522042)

![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/77ad1678-e841-4ad4-af75-36fb935e1416)
The image below and above are continuous screenshot of the same webpage (idk how to take a scrolling screenshot)
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/1eb7d0b7-d056-449d-ad56-a8a7a6b12179)


III) 
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/c45dfeb0-5719-4de7-889a-0ac905d2011c)
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/46f737d7-cf5a-4260-a712-544883da3929)
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/f21becdf-b835-49ae-9c58-d1ca362031ab)


IV) 
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/08310f2e-cf15-4ed2-a9fc-045e03e964f5)
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/d7ec2f85-7fe3-499c-9826-d57bec744a30)


V) 
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/fdbd7192-9346-4ecd-bfae-a819443d6fc7)
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/f4a005b0-185f-4320-b352-c21fb7bbfff9)


VI)
In order to load the piechart, you can press the total donations button the website's landing page
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/f39a1be9-26af-4480-b393-0c323fc6b743)
![image](https://github.com/nikhil-405/flask_web-dev_assignment/assets/148058602/f6236182-5a9d-4fcc-9333-d91f07854c67)





# License
The code in this repository is released under the [MIT license](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt). Read more at the [Open Source Initiative](https://opensource.org/).
