
====================================
Alpha Griffin Python Starter Project
====================================

Starting point for a Python project.


Starting a Project
------------------

You can use this repository as a starting point for any Alpha Griffin Python project. Here's an example of one way to accomplish this with GitHub:

1. Start a new repository on GitHub but **do not initialize** as you will be pushing an existing repository (a clone of pyproject). For this example we'll name it *my_new_thing*.
2. ``git clone http://github.com/AlphaGriffin/pyproject my_new_thing``
3. ``cd my_new_thing``
4. ``git remote remove origin``
5. ``git remote add origin http://github.com/AlphaGriffin/my_new_thing``
6. ``git push -u origin master``

Now your clone of pyproject lives at the new GitHub address and pushes will go there by default.

**Recommended**

With this extra step you can easily pull and merge again in the future from this master *pyproject* repository:

7. ``git remote add pyproject http://github.com/AlphaGriffin/pyproject``

Using ``git pull pyproject`` you can pull and merge the latest from *pyproject* at any time.



Initial Commit
--------------

There's a few things you'll want to do for first commit:

1. Rename the default project source folder: ``git mv ag/pyproject ag/my_new_thing``
2. Update variables in ``setup.py``
3. Update project name in ``.gitignore`` (look for *pyproject*.egg-info)


Installing
----------

To install this project to the local system: ``python setup.py install``

