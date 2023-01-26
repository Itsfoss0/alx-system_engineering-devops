![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
> loops, conditions and log parsing in Bash

## Intro
Bash is a powerful command-line tool that can be used to automate various tasks, including looping through a set of commands and parsing log files. Loops are used to execute a command or set of commands repeatedly, and conditions are used to control the flow of the loop. The for loop is used to iterate over a list of items, and the while loop is used to repeatedly execute a command until a certain condition is met. Log parsing is the process of extracting useful information from log files using various commands and techniques. Bash provides a variety of commands and tools for parsing log files, such as ```grep```, ```sed```, and ``awk``, which can be used to search for and extract specific information from log files. These features can be used to automate log parsing tasks, making it easy to extract important data and insights from log files. In this context, we will be discussing how to use loops and conditions in Bash to automate tasks and parse log files effectively. 

Stay hooked as we dive right in :)
> Why was the awk command feeling so awk-ward? It had just split with its log file!

> What did the grep command say to the log file? "You're matching my expectations!"

## Resources
Read or also watch
1. [Loops sample](https://tldp.org/LDP/Bash-Beginners-Guide/html/sect_09_01.html)
2. [Variable assignment and arithemetic](https://tldp.org/LDP/abs/html/ops.html)
3. [Comparison operator](https://tldp.org/LDP/abs/html/comparison-ops.html)
4. [File test operator](https://tldp.org/LDP/abs/html/fto.html)
5. [Make your script portable](https://www.cyberciti.biz/tips/finding-bash-perl-python-portably-using-env.html)

## Man / Help

- env
- cut
- for
- while
- until
- if

## Learning objectives
After going through the above resources, you should be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) the following concepts __without the help of Google__

* [ ] How to create SSH keys
* [ ] What is the advantage of using ```#!/usr/bin/env bash``` over ```#!/bin/bash```
* [X] How to use ```while```, ```until``` and ```for``` loops
* [X] How to use ```if```, ```else```, ```elif``` and ```case``` condition statements
* [X] How to use the ```cut``` command
* [X] What are files and other comparison operators, and how to use them

## Requirements
### General 
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md at the root of the project folder
- All your Bash script files must be executable
- You are not allowed to use ```awk```
- Your Bash script must pass ```Shellcheck``` (version 0.7.0) without any error
- The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## More info
### Shellcheck
[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. ```Shellcheck``` is your friend! __All your Bash scripts must pass ```Shellcheck``` without any error or you will not get any points on the task__.

Shellcheck is available on the school’s computers. If you want to use it on your own computer, here is how to [install it](https://github.com/koalaman/shellcheck#installing).

Example:

Not passing ```shellcheck```

![not-passing-shellcheck](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/Vxotqyj.png)

Passing ```shellcheck```

![passing-shellcheck](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/251/ubHWxDU.png)

For every feedback, Shellcheck will provide a code that you can use to get more information about the issue, for example for code ```SC2034```, you can browse https://github.com/koalaman/shellcheck/wiki/SC2034.