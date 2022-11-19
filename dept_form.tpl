% rebase('layout.tpl', title='edit hours')

<h1>WXYZ Corp</h1>

<h1>Get Payroll by Department</h1>
<p>
<form action='/getDepartment' method='post'>
<label for='department'>Select Department:</label>
<select name='dept'>
    <option value='advertising'>Advertising</option>
    <option value='environment'>Environment</option>
    <option value='maintenance'>Maintenance</option>
    <option value='shipping'>Shipping</option>
</select>
</p>
<p><input type='submit' value='Submit'></p>