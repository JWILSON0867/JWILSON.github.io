% rebase('layout.tpl', title='department')

<h3>Department: {{dept}}</h3><br>

<p>
<table class='table'>
<tr>
<th>Emp ID</th>
<th>Name</th>
<th>Wage</th>
<th>Hrs Worked</th>
<th>Weekly Pay</th>
</tr>
% for row in rows:
    <tr align='center'>
    % for col in row:
        <td>{{col}}</td>
    % end
    </tr>
% end
</table>
</p>
<br>