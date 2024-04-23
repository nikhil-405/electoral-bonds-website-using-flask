import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from flask import Flask, render_template, request
from flask import Flask
from flask_mysqldb import MySQL



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'nikhil'
app.config['MYSQL_DB'] = 'dcc_assignment'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search_query']

        conn = mysql.connection
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM purchase_data WHERE bond_number = %s", (search_query,))
        # cursor.execute("DESC purchase_data")
        search_results = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        # print(column_names)
        cursor.close()
        # print(search_results)
        return render_template("search_results.html", search_results=search_results, search_query=search_query, column_names = column_names)
    
    else:
        return render_template("search.html")


@app.route('/filter', methods=['GET', 'POST'])
def filter():
    if request.method == 'POST':
        filter_criteria = request.form['filter_criteria']
        filter_value = request.form['filter_value']

        if filter_criteria in ["party_name", "ac_no", "pay_branch", "pay_teller", "date_of_encashment"]:
            table_name = "redemption_data"
        else:
            table_name = "purchase_data"

        sql_query = f"SELECT * FROM {table_name} WHERE {filter_criteria} = %s"
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(sql_query, (filter_value,))
        filtered_data = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        cursor.close()

        return render_template('filtered_data.html', filtered_data=filtered_data, column_names = column_names)

    else:
        return render_template("filter.html")


@app.route('/submit-filter', methods=['POST'])
def submit_filter():
    if request.method == 'POST':
        filter_criteria = request.form['filter_criteria']
        filter_value = request.form['filter_value']

        if filter_criteria in ["party_name", "ac_no", "pay_branch", "pay_teller", "date_of_encashment"]:
            table_name = "redemption_data"
        else:
            table_name = "purchase_data"

        sql_query = f"SELECT * FROM {table_name} WHERE {filter_criteria} = %s"
        conn = mysql.connection
        cursor = conn.cursor()
        cursor.execute(sql_query, (filter_value,))
        filtered_data = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        cursor.close()

        return render_template('filter_results.html', filtered_data=filtered_data, column_names = column_names)

    else:
        return render_template("filter.html")


# 1e2
@app.route('/bond', methods=['GET', 'POST'])
def bond():
    
    if request.method == 'POST':
        person_name = request.form['person_name']

        cur = mysql.connection.cursor()
        cur.execute("SELECT YEAR(date_of_purchase) AS year, COUNT(*) AS num_bonds, SUM(denominations) AS total_value "
                    "FROM purchase_data "
                    "WHERE name_of_the_purchaser = %s "
                    "GROUP BY YEAR(date_of_purchase)", (person_name,))
        results = cur.fetchall()
        print(results)
        cur.close()


        df = pd.DataFrame(results, columns=['Year', 'Number of Bonds', 'Total Value'])
        # print(df)

        years = [result[0] for result in results]
        num_bonds = [result[1] for result in results]
        total_value = [result[2] for result in results]

        return render_template('bond_results.html', person_name=person_name,
                               years=years, num_bonds=num_bonds, total_value=total_value)

    else:  
        return render_template("bond.html")
        
# 1e3
@app.route('/party-bonds', methods=['GET', 'POST'])
def party_bonds():
    if request.method == 'POST':
        party_name = request.form['party_name']

        cur = mysql.connection.cursor()
        cur.execute("SELECT YEAR(date_of_encashment) AS year, COUNT(*) AS num_bonds, SUM(denominations) AS total_value "
                    "FROM redemption_data "
                    "WHERE party_name = %s "
                    "GROUP BY YEAR(date_of_encashment)", (party_name,))
        results = cur.fetchall()

        cur.close()


        df = pd.DataFrame(results, columns=['Year', 'Number of Bonds', 'Total Value'])
        # print(df)

        years = [result[0] for result in results]
        num_bonds = [result[1] for result in results]
        total_value = [result[2] for result in results]

        return render_template('party_bonds_result.html', party_name=party_name,
                               years=years, num_bonds=num_bonds, total_value=total_value)
    else:   
        return render_template("party_bonds.html")


# 1e4
# Just complete the results template
@app.route('/party-donations', methods=['GET', 'POST'])
def party_donations_info():
    if request.method == 'POST':
        party_name = request.form['party_name']

        cur = mysql.connection.cursor()
        cur.execute("SELECT p.name_of_the_purchaser, SUM(p.denominations) AS total_amount "
                    "FROM purchase_data AS p "
                    "JOIN redemption_data AS r " 
                    "ON p.bond_number = r.bond_number "
                    "WHERE r.party_name = %s "
                    "GROUP BY r.party_name, p.name_of_the_purchaser", (party_name,))
        results = cur.fetchall()
        print(results)
        cur.close()


        df = pd.DataFrame(results, columns=["Company", "Donation to party"])
        # print(df)

        company = [result[0] for result in results]
        donation = [result[1] for result in results]
        donation = [float(donation) for donation in donation]
        total = sum(donation)
        # print(company, donation, total)

        return render_template('party_donations_result.html', company = company, party_name = party_name, donation = donation, total = total)
    else:   
        return render_template("party_donations.html")

# 1e5
@app.route('/company-donations', methods=['GET', 'POST'])
def company_donations_info():
    if request.method == 'POST':
        company_name = request.form['company_name']

        cur = mysql.connection.cursor()
        cur.execute("SELECT r.party_name, SUM(p.denominations)"
                    "FROM purchase_data as p "
                    "JOIN redemption_data as r "
                    "ON p.bond_number = r.bond_number "
                    "WHERE p.name_of_the_purchaser = %s "
                    "GROUP BY r.party_name", (company_name,))
        results = cur.fetchall()

        cur.close()


        df = pd.DataFrame(results, columns=["Party", "Donation by Comapny"])
        # print(df)

        parties = [result[0] for result in results]
        donation = [result[1] for result in results]
        total = sum(donation)

        return render_template('company_donations_result.html', parties = parties, donation = donation, total = total, company_name = company_name)
    else:   
        return render_template("company_donations.html")

# 1e6
@app.route('/total-donations', methods=['GET', 'POST'])
def total_donations():
    cur = mysql.connection.cursor()
    cur.execute("SELECT party_name, SUM(denominations) "
                "FROM redemption_data "
                "GROUP BY party_name")
    results = cur.fetchall()

    party_name = [result[0] for result in results]
    total_donation = [result[1] for result in results]
    print(len(party_name))
    print(len(total_donation))
    return render_template("total_donations_result.html", party_name = party_name, total_donation = total_donation)



if __name__ == "__main__":
    app.run(debug = True)