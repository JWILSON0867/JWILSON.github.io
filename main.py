import sqlite3
from bottle import route, run, template, request

@route('/', method='GET')
def index():
    return template('login')

@route('/VbD', method=['GET', 'Post'])
def getDep():
    dept = request.form.get("dept")
    conn = sqlite3.connect('payroll.db')
    cur = conn.cursor()

    sql = '''SELECT pay_data.emp_id, emp_name, wage, hrs_worked FROM employees JOIN pay_data WHERE pay_data.emp_id = employees.emp_id AND employees.department = ?'''
    cur.execute(sql, (dept,))
    rows = cur.fetchall()
    cur.close()

    hrs = 0
    wage = 0

    if rows:

        datalist = []
        for row in rows:
            eid, name, wage, hrs = row
            if hrs <= 40:
                payout = wage * hrs
            else:
                ot_pay = (hrs - 40) * wage * 1.5
                payout = (wage * 40) + ot_pay

            emp = (eid, name, wage, hrs, payout)
            datalist.append(emp)

        data = {'rows': datalist, 'dept': dept}

        return template('show_department', data)

    else:
        data = {'msg': 'An error accurred connecting to the database'}
        return template('status', data)

@route('/EED', method=['GET', 'Post'])
def editEmp():
    if request.method == 'GET':
        return template('edit_hours')
    else:
        hrs = request.forms.get('hrs')
        eid = request.forms.get('eid')

        try:
            conn = sqlite3.connect('payroll.db')
            cur = conn.cursor()

            sql_1 = '''SELECT emp_id, emp_name, department FROM employees WHERE emp_id = ?'''
            cur.execute(sql_1, (eid,))
            result = cur.fetchone()

            emp_id = result[0]
            emp_name = result[1]
            dept = result[2]

            sql_2 = '''UPDATE pay_data SET hrs_worked = ? WHERE emp_id = ?'''
            cur.execute(sql_2, (hrs, eid))
            if result:
                conn.commit()
                cur.close()
                return template('editSuccess', {'emp_id': emp_id, 'emp_name': emp_name, 'dept': dept, 'hrs': hrs})
        except:

            data = {'msg': 'Employee not found!!'}
            return template('status', data)

        finally:
            cur.close()

    run(host='localhost', port=8080, debug=True)