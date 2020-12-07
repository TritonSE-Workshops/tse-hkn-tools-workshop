# Internship Tools Workshop

**A joint collaboration between TSE and HKN @ UCSD.**

In this workshop, we covered the following tools:

* Confluence/Jira
* Docker
* MongoDB
* Python 3+

In this activity, we'll be building an application that uses all four of those tools.
This application will be a simple CLI-based note-taking application. More details below.

## Setup

All you will need for this exercise is:

* Docker
* Docker Compose (usually shipped with Docker)

First, clone this repository.

```
git clone https://github.com/TritonSE/tse-hkn-tools-workshop
```

Then, using Docker Compose, build and run the development environment.

```
docker-compose up
```

At this point, you will need to open a new shell. Navigate back to the
repository directory. In order to run the program, use:

```
docker exec -it workshop_notes python notes
```

This will connect to one of the containers started by Docker Compose
and run the note-taking application. The other container is responsible
for running a containizered version of MongoDB.

## Jira

TODO: Provide a link here

## Activity

In this activity, you will be implementing the function `delete_note`
in the file **notes/commands.py**. This enable the user to be able
to delete notes from the command line.

If you have time, I would encourage you to go a step beyond and
try to implement a command to edit existing notes! This may require
editing the file **notes/cli.py** as well.

The application is using the PyMongo driver. Documentation can
be found at https://pymongo.readthedocs.io/en/stable/. There is
plenty of documentation available on StackOverflow too.

Good luck!
