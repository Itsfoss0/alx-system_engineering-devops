![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > shell variable expansion

## Intro
Have you ever found yourself writing a shell script and wanting to incorporate the value of a variable into a command or string? Or maybe you've wanted to manipulate the value of a variable before using it in your script. If so, then you'll want to learn about shell variable expansion. Lets take a deep dive into this powerful feature of the shell and explore some of the various ways you can use it to make your scripts more flexible and efficient

## Resources
Read or watch. 
1. [Expansions](http://linuxcommand.org/lc3_lts0080.php)
2. [Shell arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
3. [Variables](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html)
4. [Shell init files](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
5. [The alias command](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_01.html)
6. [Technical writting](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2021/6/9112669886fd446a2aa3113c31319d1f468dc160.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230107%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230107T205221Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c01637fc9adee4b178a6e71b5628c99b434f6f79f3aca4137a3331f94b85dccc)

## Man or Help
* ```printenv```
* ```set```
* ```unset```
* ```export```
* ```alias```
* ```unalias```
* ```.```
* ```source```
* ```printf```


## Learning objectives
By the end of this project, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/?fbclid=IwAR2K5_BGPVo0QjJXkOIIqNsqcXK4lTskPWJvA0asKQIGtCPWaQBdKmj1Ztg) __Without the help of google__ the following concepts

### General
* [X] What happens when you type $ ```ls -l *.txt```

### Shell intialization files
* [X] What are the ```/etc/profile``` file and the ``` /etc/profile.d``` directory
* [X] What is the ```~/.bashrc``` file

### Variables
* [X] What is the difference between a local and a global variable
* [X] What is a reserved variable
* [X] How to create, update and delete shell variables
* [X] What are the roles of the following reserved variables: ```HOME```, ```PATH```, ```PS1```
* [X] What are special parameters
* [X] What is the special parameter ```$??```

### Expansions
* [X] What is expansion and how to use them
* [X] What is the difference between single and double quotes and how to use them properly
* [X] How to do command substitution with ```$()``` and backticks

### Shell Arithmetic
* [X] How to perform arithmetic operations with the shell

### The ```alias``` command

* [X] How to create an alias
* [X] How to list aliases
* [X] How to temporarily disable an alias

### Other help pages
* [X] How to execute commands from a file in the current shell

### More info
Read your ``` /etc/profile```, ```/etc/inputrc ```and ```~/.bashrc ``` files.

Look at some files in the ```/etc/profile.d``` directory.

Note: You do not have to learn about ```awk```, ```tar```, ```bzip2```, ```date```, ```scp```, ```ulimit```, ```umask```, or shell scripting, yet.

## Quizes
[Quiz](./quiz.md)