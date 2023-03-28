![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Web server


![web-server](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

## Background context
[![web-server](https://img.youtube.com/vi/AZg4uJkEa-4/0.jpg)](https://youtu.be/AZg4uJkEa-4 "Web Server")


In this project, some of the tasks will be graded on 2 aspects:

- Is your ```web-01``` server configured according to requirements
- Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file ```/tmp/test ```containing the string ```hello world``` and modify the configuration of Nginx to listen on port ```8080``` instead of ```80```, I can use ```emacs``` on my server to create the file and to modify the Nginx configuration file ```/etc/nginx/sites-enabled/```default.

But my answer file would contain:
```
itsfoss@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
itsfoss@ubuntu
```
As you can tell, I am not using ```emacs``` to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the ```root``` user, you do not need to use the ```sudo``` command

A good Sofware Engineer is a [Lazy Sofware Engineer](https://www.techwell.com/techwell-insights/2013/12/why-best-programmers-are-lazy-and-act-dumb)
![lazy-swe](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg)

## Resources
__Read or Watch__:
1. [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
2. [Nginx](https://en.wikipedia.org/wiki/Nginx)
3. [How to configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
4. [Child process concept page](https://intranet.alxswe.com/concepts/110)
5. [Root and subdomains](https://landingi.com/help/domains-vs-subdomains/)
6. [HTTP Request](https://www.tutorialspoint.com/http/http_methods.htm)
7. [HTTP Redirection](https://moz.com/learn/seo/redirection)
8. [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
9. [Log files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)

## References
- [RFC 7231 HTTP/1](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7540 HTTP/2](https://datatracker.ietf.org/doc/html/rfc7540)

## Man or help
- scp
- curl

## Learning objectives
By the end of this project, you are expcted to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/) __Without the help of Google__:

### General
* [X] What is the main role of a web server
* [X] What is a child process
* [X] Why web servers usually have a parent process and child processes
* [X] What are the main HTTP requests

### DNS
* [X] What DNS stands for
* [X] What is DNS main role

### DNS Record Types
DNS Record Types
* [X] ```A```
* [X] ```CNAME```
* [X] ```TXT```
* [X] ```MX```



## Requirements

### General

- Allowed editors: ```vi```, ```vim```, ```emacs```
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A ```README.md ```file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass ```Shellcheck``` (version ```0.3.7```) without any error
- The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- You can’t use ```systemctl``` for restarting a process


## Quiz
[Quizes](./quiz.md)