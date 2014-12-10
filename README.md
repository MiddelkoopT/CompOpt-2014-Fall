CompOpt-2014-Fall
=================

Computational Optimization (IMSE 8001-01) Fall 2014

## Lectures ##

### Week 1 (R) ###
The basics
 * Install basic software (windows 64 bit links)
   * Python (64 bit): https://www.python.org/ftp/python/3.4.1/python-3.4.1.amd64.msi
   * R: http://cran.r-project.org/bin/windows/base/R-3.1.1-win.exe
   * R Studio: http://download1.rstudio.org/RStudio-0.98.1028.exe
   * GitHub for windows: https://github-windows.s3.amazonaws.com/GitHubSetup.exe
   * Notepad++ (optional): http://download.tuxfamily.org/notepadplus/6.6.8/npp.6.6.8.Installer.exe
   * SQLite: http://www.sqlite.org/2014/sqlite-shell-win32-x86-3080600.zip
 * Learn the basics of R:
   * Intractive tutorials: http://tryr.codeschool.com/ https://www.datacamp.com/courses/introduction-to-r
   * Basic tutorial: http://cyclismo.org/tutorial/R/
   * R coding style: http://r-pkgs.had.co.nz/style.html
   * R Markdown: http://rmarkdown.rstudio.com/
   * Offical introduction: http://cran.r-project.org/doc/manuals/R-intro.html
   * Advanced tutorials: http://www.r-tutor.com/

Homework (Due 9/3 before class):
 * Complete R "interactive tutorials", chose which one to complete first at random.  Comlete the "Basic tutorial."  Write a comparison of all three methods and which one worked the best for your learning style and why. When you comlete the interactive tutorials what does each show? Do you get a certificate?  This is Assignment A1_RTutorial on the blackboard system.

### Week 2 (Python) ###
Learn the basics of Python:
 * Interactive tutorials: https://groklearning.com/learn/hoc-epidemic/intro/0/ http://www.codecademy.com/en/tracks/python http://pythontutor.com
 * Read tutorial: https://docs.python.org/3/tutorial/

Homework (Due 9/10 before class):
 * Complete the interactive python tutorials Grok Learning "HOC: Disease Epidemic" and codecademy Python. Which one worked for you?  How did this compare to the R tutorials.  Did you use something else (the python.org tutorial)? If so please elaborate. Did you comlete the entire tutorial to complete the second homework or just portions.  Email your submission as A2_BasicPython.
 * Write a program to read a csv file with two columns (x1 and x2) and write a csv with the following columns: x1, x2, x1+x2, x2-x1. Import the data into R and plot x1 v.s. x2.  Email your submission with the subject A3_PythonCSV

### Week 3 (Project and source management) ###
Github and project workflows.
 * Iteractive tutorial: https://www.codeschool.com/courses/try-git
Git references:
 * Github docs: http://git-scm.com/doc

Project work:
 * Identify your problem and be prepared to discuss in class
 * Identify your data source: generated? benchmark problems? actual data?

Project Assignment:
 * Create a github account and repository for your project.  Email repository URL to instructor.
 * Start programming in Python, begin prgramming your data interfaces: Read/write/generate your sample data in Python.

### Week 4 (TDD/Software Development/Python)
 * Test Driven Development (TDD)
   * "Test Driven Development: By Example," by Kent Beck, 2002. http://www.amazon.com/dp/0321146530
   * Web-based TDD/git (optional): "Test-Driven Development with Python," by Harry Percival, 2014. http://chimera.labs.oreilly.com/books/1234000000754
   * http://www.agiledata.org/essays/tdd.html

### Week 5 (TDD/Project)
 * TDD and Refactoring.
 * Data structures/Classes in Python.

Project Assignment:
  * Use develop/refactor a class and module to import data into Python and use TDD to give some basic statistics about the dataset (number of lines imported, nodes, arcs, etc) and other structural information about the data. Due Wed Oct 1st.

### Week 6 (Data, Databases, and Data Flow)
 * SQLite databases (http://www.sqlite.org/)
   * Download and install to C:\Programs\SQLite: http://www.sqlite.org/2014/sqlite-shell-win32-x86-3080600.zip
 * SQLite in Python (https://docs.python.org/3/library/sqlite3.html)
 * SQLite in R (http://cran.r-project.org/web/packages/RSQLite/index.html)
 * Hashing in Python (https://docs.python.org/3/library/hashlib.html)
 * Problem data strctures
 * Database Design (http://www.tomjewett.com/dbdesign/)
 * Portable Apps (http://portableapps.com/download)

### Week 7 (Orcastration, Optimization)
 * Configparser: https://docs.python.org/3/library/configparser.html
 * Gurobi: http://www.gurobi.com/download/gurobi-optimizer
 * Install Python 3.2 for Gurobi: https://www.python.org/ftp/python/3.2.5/python-3.2.5.amd64.msi
 * Install Gurobi module for Python.
```BatchFile
C:\>cd c:\gurobi563\win64
C:\gurobi563\win64>\Python32\python.exe setup.py install
```

Homework Assignment:
 * Download and install Gurobi.  

### Week 8 (Workflow tools)
 * Pegasus workflow: http://pegasus.isi.edu/
 * Pegasus example: https://github.com/pegasus-isi/Soybean-Workflow

Homework Assignment:
 * Repeate the CSV assignment with R and Python but using SQLite. Due Monday October 13th before class.
 * Solve the following problem in Gurobi using Python. Due Wednesday October 15th before class.
   * max x1 + 2x2 s.t. x1 + x2 <= 40, 2x1 + x2 <= 60 ; x1,x2 >=0 

### Week 9
 * SQLite and experiment and results databases
   * https://github.com/sqlitebrowser/sqlitebrowser/releases/download/v3.3.1/sqlitebrowser-3.3.1-win32.exe
Project Assignment:
 * Determine the results of a your project and create a database to store them in.
 * Generate a hash of a solution.

### Week 10
 * Latex (http://miktex.org/) and TexMaker (http://xm1math.net/texmaker)
   * http://www.xm1math.net/texmaker/texmakerwin32_install.exe 
   * http://mirrors.ctan.org/systems/win32/miktex/setup/basic-miktex-2.9.5105.exe

### Week 11
 * Heuristic Search, A*
   * http://theory.stanford.edu/~amitp/GameProgramming/index.html
   * http://www.redblobgames.com/pathfinding/a-star/introduction.html

## Resources/Notes ##

### Git Workflow
 * https://www.atlassian.com/git/workflows#!workflow-forking
 * https://github.com/dchelimsky/rspec/wiki/Topic-Branches

### Deploymet and DevOps ###
 * The Twelve Factors http://12factor.net/

