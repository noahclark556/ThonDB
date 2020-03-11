# ThonDB

<h2>Python based database framework</h2>

Same concept as SQL, obviously less advanced but allows creation of databases and tables within those databases, etc. <br/>
Query commands are simple, but are listed when "help" is typed into the query console.<br/>
You will be prompted to create a database, it well then be automatically saved with the extension .tdb to the databases directory.
Also remember that typing 'stop()' into the console when executing queries will break out of the query. <br/>

Logic behind this is relatively simple, it utilizes lists, dictionaries, tuple unpacking, string manipulation<br/>
etc. to retrieve and update data within a database file. ThonDB formats the query as "TABLE|COL:ROW|COL:ROW" and so on.<br/>
Due to the selective formatting of this framework, as of now, information that is put in to a table containing ":" and "|" <br/>
will obviously cause problems. I'll get around to fixing that when the skeleton of the whole thing is finished. <br/>
This has the capability to be used as a package in other projects, but it would take some time to get used to the usage of some of the
methods and error handling, which I built directly into the console, forgetting the fact that outside of my project, the console
would most likely not be used. But within the ReadReturn object class, the usage is not hard to understand, so using this as a
standalone package is definitely possible. TO RUN: just run 'Main.py' with python <br/>
<br/>
<center><h1>QUERY COMMANDS</h1></center>
<br/>
<table>
  <tr>
      <td>Command</td>
      <td>Usage</td>
      <td>Ex.</td>
  </tr>
  <tr>
      <td>getRawRows.{FORMAT}</td>
      <td>FORMAT is either 'raw' or 'pairs' Returns all table data</td>
      <td>getRawRows.pairs</td>
  <tr/>
  <tr>
      <td>getSpecific.{COLUMN}.{ROW}</td>
      <td>COLUMN is column name, ROW is row number - Returns data of that specific item</td>
      <td>getSpecific.name.3</td>
  <tr/>
  <tr>
      <td>getSize</td>
      <td>Returns size of currently selected table</td>
      <td>getSize</td>
  <tr/>
  <tr>
      <td>selectTable.{TABLE_NAME}</td>
      <td>Allows selection of different table to be manipulated</td>
      <td>selectTable.users</td>
  <tr/>
  <tr>
      <td>deleteRow.{COLUMN}.{VALUE}</td>
      <td>Delete row from selected table where column={COLUMN} and value={VALUE}</td>
      <td>deleteRow.name.jeff</td>
  <tr/>
  <tr>
      <td>insert</td>
      <td>Allows insertion into currently selected table</td>
      <td>insert</td>
  <tr/>
  <tr>
      <td>newTable</td>
      <td>Allows creation of new table</td>
      <td>newTable</td>
  <tr/>

</table>
