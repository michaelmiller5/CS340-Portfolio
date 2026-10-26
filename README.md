# CS 340 - Grazioso Salvare Dashboard

This repository contains my Project Two work for CS 340: a full-stack dashboard
for Grazioso Salvare that connects a MongoDB database of Austin Animal Center
outcomes to an interactive Dash web application. It includes the dashboard code
(ProjectTwoDashboard.ipynb), the CRUD Python module (CRUD_Python_Module.py), and
the Project Two README documenting the project.

## How do you write programs that are maintainable, readable, and adaptable?

I keep the different layers of an application separate so each piece can change
without breaking the others. The clearest example is the CRUD Python module from
Project One. It wraps all of the database operations (create, read, update,
delete) in a single AnimalShelter class, so the dashboard never talks to MongoDB
directly. It just calls methods like read(). In Project Two I connected the
dashboard widgets to the database entirely through that module, which kept the
interface code focused on presentation while the database logic stayed in one
place. The advantages were real: when I needed the dashboard to pass in a
username and password, I only had to change the class constructor, not the
dashboard, and the same read() method powered the data table, the pie chart, and
the map. Because the module is self-contained and commented, I could reuse it in
the future for anything that needs this data, such as a command-line reporting
tool, an automated data export, or a different front end built in another
framework.

## How do you approach a problem as a computer scientist?

I start by turning the client's needs into concrete requirements before writing
code. For Grazioso Salvare, I used the dashboard specification and the
rescue-type breed table to define exactly what each filter had to return
(specific breeds, sex, and age ranges), then built the MongoDB queries to match.
This project differed from earlier coursework because it was a full stack built
in stages across several modules rather than one isolated assignment: the
database and user account came first, then the CRUD module, then the data table,
then the charts and filters, and each piece had to work with what came before.
Going forward, strategies I would reuse include building the data-access layer
first and testing it on its own, designing queries directly from a written
requirements table, and adding features incrementally so I can verify each one
works before moving to the next.

## What do computer scientists do, and why does it matter?

Computer scientists build tools that turn raw data into something people can
actually use to make decisions. For Grazioso Salvare, the shelter data on its
own is just thousands of rows that are hard to search through by hand. The
dashboard lets their staff pick a rescue type and immediately see the matching
dogs, where they are located, and the breed breakdown, without writing a single
query. That saves time, reduces errors, and helps the organization identify good
rescue-training candidates faster. Work like this matters because it takes a
slow, manual process and makes it fast and reliable, which frees people to focus
on their actual mission instead of fighting with the data.
