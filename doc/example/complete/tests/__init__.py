"""Init file for koztumize tests"""
# -*- coding: utf-8 -*-

import os
import shutil
import pynuts
import sqlite3
from tempfile import mkdtemp
from complete import application
from contextlib import closing

PATH = os.path.dirname(os.path.dirname(__file__))
TEMP_DIR = None
DATABASE = '/tmp/test.db'


def connect_db():
    return sqlite3.connect(DATABASE)


def execute_sql(application, filename, folder=None):
    """Execute a sql file in the sql folder for application.app"""
    path = os.path.join(PATH, 'tests', 'sql', filename)
    with closing(connect_db()) as db:
        with application.open_resource(path) as f:
            db.cursor().executescript(f.read())
        db.commit()


def setup():
    """Setup function for tests."""
    # global variable shouldn't be used but is quite useful here
    # pylint: disable=W0603
    global TEMP_DIR
    TEMP_DIR = mkdtemp()
    if os.path.exists(os.path.join(PATH, 'tests', 'fake_instance')):
        shutil.rmtree(os.path.join(PATH, 'tests', 'fake_instance'))
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    app = pynuts.Pynuts('complete',
        config={'SECRET_KEY': 'Azerty',
                'SQLALCHEMY_DATABASE_URI': 'sqlite:////tmp/test.db',
                'PYNUTS_DOCUMENT_REPOSITORY': os.path.join(
                    PATH, 'tests', 'fake_instance', 'documents.git')})
    application.app = app
    import complete.executable
    execute_sql(application.app, 'database.sql')


def teardown():
    """Remove the temp directory after the tests."""
    if os.path.exists(os.path.join(PATH, 'tests', 'fake_instance')):
        shutil.rmtree(os.path.join(PATH, 'tests', 'fake_instance'))
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    execute_sql(application.app, 'drop_all.sql')


def setup_func():
    execute_sql(application.app, 'insert_data.sql')
    shutil.copytree(
        os.path.join(PATH, 'tests', 'dump', 'instance', 'documents.git'),
        os.path.join(PATH, 'tests', 'fake_instance', 'documents.git'))


def teardown_func():
    execute_sql(application.app, 'truncate_all.sql')
    shutil.rmtree(os.path.join(PATH, 'tests', 'fake_instance'))