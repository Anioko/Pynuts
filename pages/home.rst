========
 Pynuts
========

Pynuts is a Flask extension which will simplify your code by creating some generic content.

It allows you to:

* implement some basic CRUD (Create, Read, Update and Delete) view functions for administration in a few lines.
* secure your application by easily manage permissions using the request context.
* handle HTML and PDF documents with git, you can store anything you want for any instance you created. Of course, you can use all the features that git provides and do what you want with your documents, that’s why Pynuts is a powerful tool for developpers.
* drastically reduce the amount of code to write.

Let's compare the code you would have to write without and with Pynuts to implement a basic view to add a model instance in database:

.. table::

    +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+
    | Without Pynuts:                                                     |  With Pynuts:                                                                       |
    +=====================================================================+=====================================================================================+
    | .. sourcecode:: python                                              | .. sourcecode:: python                                                              |
    |                                                                     |                                                                                     |
    |                                                                     |     @EmployeeView.create_page                                                       |
    |    @app.route('/employee/add', methods=('GET', 'POST'))             |     @app.route('/employee/add', methods=('GET', 'POST'))                            |
    |    def add_employee():                                              |     def add_employee():                                                             |
    |        form = EmployeeForm()                                        |         return EmployeeView().create('create_employee.html.jinja2')                 |
    |        if form.validate_on_submit():                                |                                                                                     |
    |            employee = Employee()                                    |                                                                                     |
    |            form.populate_obj(employee)                              |                                                                                     |
    |            db.session.add(employee)                                 |                                                                                     |
    |            db.session.commit()                                      |                                                                                     |
    |            return redirect(url_for(                                 |                                                                                     |
    |                'read_employee', employee_id=employee.employee_id))  |                                                                                     |
    |        else:                                                        |                                                                                     |
    |            return render_template(url_for('add_employee'))          |                                                                                     |
    |                                                                     |                                                                                     |
    +---------------------------------------------------------------------+-------------------------------------------------------------------------------------+


* Free software: BSD licensed
* Python 2.6-2.7
* Source code and issue tracker: on `Github <https://github.com/Kozea/Pynuts>`_
* `Documentation <http://packages.python.org/Pynuts/>`_
* `Install <http://packages.python.org/Pynuts/Installation.html>`_
* Get `in touch <mailto:contact@kozea.fr>`_