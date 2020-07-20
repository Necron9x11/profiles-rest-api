# Profiles REST AP*

Profiles REST API course code

# Setting Up the Class Environment

For detailed build instructions refer back to the class. This is a summary and steps to fire it back up once it has been built

### Requirements

**NOTE:** _**The class only has instructions for Winblowz and Mac.**_

- A code editor/IDE
    The Instructor uses [`Atom`](https://atom.io/). It is a preferecen thing. So far at least the class has not required any Atom specific plugin functionality. (I have used JetBrains ['Pycharm IDE`](https://www.jetbrains.com/pycharm/))
- Hashi Corop's [`Vagrant`](https://www.vagrantup.com/)
- [Git](https://git-scm.com/downloads)
- -Oracle's [`Virtualbox`](https://www.virtualbox.org/)


### Restarting once you are setup

1. Launch a terminal and open two tabs in it. (If using Pycharm you can simply open two terminal session in the Pycharm interface.)
2. Browse to your project's directory (~/Code/Classes/PythonDjangoRestBeginner)
3. Launch your editor/IDE. 
4. From the class proiject main directory launch the `VirtualBox` instance with `Vagrant` instance. 
   ```bash
   $ vagrant up
   ```
5. Switch to a second terminal window and access the `Vagrant` box once it launches. 
   ```bash
   $ vagrant ssh
   ```
6. Once inside the `Vagrant` instance load up the `Python Virtual Environment`.
   ```bash
   $ source /home/vagrant/venv/bin/activate
   ``` 

7. Inside the `Vagrant` instance switch to the directory sync'd with your host machine. 
   ```bash
   $ cd /vagrant
   ```
8. Now launch the Django Development Web Server
   ```bash
   $ python manage.py runserver 0.0.0.0:8000
   ```
9. Not get in your ID and go to work!


