# Task_List
To run the script, type in the Terminal:
1. "python"
2. "import task_list"
3. The following options are now available:

	a. "task_list.create_db()" - This function create new database of tasks (id, name, deadline, description).
	
	b. "task_list.add('name', 'deadline', 'description')" - This function add new task to the db. Please insert name, deadline and description.
	
	c. "task_list.list()" - This function list all elements from db.
	
	d. "task_list.remove(task_id)" - This function remove task by id. Please insert id number.
	
	e. "task_list.remove_hash(name_hash)" - This function remove task by hash value of name (hash(name) function). Please insert name hash value.
	
	f. "task_list.update(task_id, 'name', 'deadline', 'description')" - This function update task in db. Please insert id number and new name, deadline, description.


For exaple:
1. INPUT: python
   OUTPUT:

2. INPUT: "import task_list"
   OUTPUT:

3. INPUT: task_list.create_db()
   OUTPUT: The database was created successfully

4. INPUT: task_list.add('Running', '02-01-2021', 'Run 10 km')
   OUTPUT:

5. INPUT: task_list.list()
   OUTPUT: Id: 1, Name: running, Deadline: 02-01-2021, Description: Run 10 km

6. INPUT: task_list.update(1, 'running', '03-01-2021', 'Run 15 km') 
   OUTPUT:

7. INPUT: task_list.remove(1)
   OUTPUT: 

8.  INPUT: task_list.remove_hash(3617018932930217536)
   	 OUTPUT: 
