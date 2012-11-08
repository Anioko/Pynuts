Pynuts is a Flask extension which will simplify your code by creating some generic content, allowing you to:

* implement some basic CRUD (Create, Read, Update and Delete) view functions for administration in a few lines.
* secure your application by easily manage permissions using the request context.
* generate HTML and PDF documents from any instance you created.
* manage different versions of these document with an embedded git repository.
* drastically reduce the amount of code to write.


About Pynuts
------------

* Free software: BSD licensed
* Python 2.6-2.7
* Source code on `Github <https://github.com/Kozea/Pynuts>`_
* `Issue tracker <http://redmine.kozea.fr/projects/pynuts>`_
* `Documentation </docs/>`_
* `Install </docs/Installation/>`_
* Get `in touch <mailto:contact@kozea.fr>`_ with the Pynuts team


Example
-------
Let's compare the code you have to write, without and with Pynuts, to implement a basic view inserting a model instance into database:


Without Pynuts
""""""""""""""

.. code-block:: python
    
    app.route('/employee/add', methods=('GET', 'POST'))
    def add_employee():
        form = EmployeeForm()
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            return redirect(url_for(
                'read_employee', employee_id=employee.employee_id))
        else:
            return render_template(url_for('add_employee'))


With Pynuts
"""""""""""

.. code-block:: python

    @EmployeeView.create_page
    @app.route('/employee/add', methods=('GET', 'POST'))
    def add_employee():
        return EmployeeView().create('create_employee.html.jinja2')
