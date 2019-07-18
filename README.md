# Project Logs Analysis


## Overview
The aim of the project is to create a reporting tool using python which can fetch reports from a large database of news website. The news database is a PostgreSQL database with schema containing three tables: articles, authors and log. By using this three tables we should get the relational reports which tells about popular three articles of all time, popular article authors and days with more than 1% of requests which lead to errors.

## Prerequisites
* [Python](https://www.python.org/downloads/)-To connect to PostgreSQl database and send queries.
* [Vagrant](https://www.vagrantup.com/downloads.html) - A virtual environment builder and manager.
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads) - An open source virtualiztion product.
* [Git](https://git-scm.com/downloads) - An open source version control system.

## Getting news data
[newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)->This `newsdata.sql` file should be placed in the vagrant directory,which will be shared with your virtual machine.

## Setting up the project
> In order to run this project logs analysis, you must have Vagrant and VirtualBox set up on your pc(To install, Click on each tool in prerequisites).

Download and clone from github [FSWDN program virtual machine](https://github.com/udacity/fullstack-nanodegree-vm) for instructions and installation process of virtual machine.  

```
#Clone the git repository into a directory using a bash terminal
git clone https://github.com/adinarayanaraju5/project_logs_analysis.git

#Once the project has been setup, navigate into the project directory with Vagrant file
cd /project_logs_analysis

#To Start the virtual machine
vagrant up

#Connection to the virtual machine
vagrant ssh

#Navigate to the folder where the host and guest files are shared
cd /vagrant

#Apply PostgreSQL to create news database
psql -d news -f newsdata.sql
```
## Running the project
```
#Once the project has been setup, navigate into the project directory on your pc
cd /project_logs_analysis

#Then, run the following command
vagrant ssh

#Navigate to the folder shared between the host and virtual machine
cd /vagrant

#Run projectlog.py
python projectlog.py
```

## Output of the project -> Logs Analysis
```
1. What are the most popular three articles of all time?
        Candidate is jerk, alleges rival - 338647 views
        Bears love berries, alleges bear - 253801 views
        Bad things gone, say good people - 170098 views
2. Who are the most popular article authors of all time?
        Ursula La Multa - 507594 views
        Rudolf von Treppenwitz - 423457 views
        Anonymous Contributor - 170098 views
        Markoff Chaney - 84557 views
3. On which days did more than 1% of requests lead to errors?
        JUL 17, 2016 - 2.3% error
```
## Resource Links
* [Udacity full stack web development nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
* [host git repository](https://github.com/adinarayanaraju5/project_logs_analysis.git)
