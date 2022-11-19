% rebase('layout.tpl', title='edit hours')

<h2>WXYZ Corp</h2>

<h1 style="padding-bottom:2%">Enter emp_id and Hours Worked</h1>

<form action="/editHours" method="post">
    <p><input type="text" name="eid" placeholder="emp_id" style="margin-right:2%"><label for="emp_id" style="">employee ID</label></p>
    <br>
    <p><input type="text" name="hrs" placeholder="hours" style="margin-right:2%"><label for="hours">Enter hrs worked</label></p><br>
    <br>
    <input type="submit" value="Submit">

</form>
