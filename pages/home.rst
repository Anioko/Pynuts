Pynuts is a BSD licensed Flask extension which will simplify your code by creating some generic content.

It allows you to:

* implement some basic CRUD (Create, Read, Update and Delete) view functions for administration in a few lines.
* secure your application by easily manage permissions using the request context.
* handle HTML and PDF documents with git, you can store anything you want for any instance you created. Of course, you can use all the features that git provides and do what you want with your documents, that’s why Pynuts is a powerful tool for developpers.
* drastically reduce the amount of code to write.

Example
-------
Let's compare the code you have to write, without and with Pynuts, to implement a basic view inserting a model instance into database:


Without Pynuts
""""""""""""""

.. code-block:: python
    
    print "Hello world"


With Pynuts
"""""""""""

.. code-block:: python

    @EmployeeView.create_page
    @app.route('/employee/add', methods=('GET', 'POST'))
    def add_employee():
        return EmployeeView().create('create_employee.html.jinja2')


* Free software: BSD licensed
* Python 2.6-2.7
* Source code and issue tracker: on `Github <https://github.com/Kozea/Pynuts>`_
* `Documentation <http://packages.python.org/Pynuts/>`_
* `Install <http://packages.python.org/Pynuts/Installation.html>`_
* Get `in touch <mailto:contact@kozea.fr>`_