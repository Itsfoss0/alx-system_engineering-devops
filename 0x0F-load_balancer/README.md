![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Load Balancer

## Concepts
For this project, take a look at the following concepts
1. [Load balancer](https://intranet.alxswe.com/concepts/46)
2. [Web stack debugging](https://intranet.alxswe.com/concepts/68)

![load-balancer](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)


## About
A load balancer is a device or software that distributes network traffic across multiple servers, ensuring that no single server is overwhelmed by too much traffic or requests. The purpose of a load balancer is to optimize resource usage, maximize throughput, minimize response time, and prevent system failures caused by overloading. Load balancers are commonly used in web applications, databases, and other networked systems to improve availability and scalability.

## Background context
You have been given 2 additional servers:

* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
* gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is [redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29) for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Resources
__Read or Watch__:
1. [Introduction to Load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
2. [HTTP header](https://www.techopedia.com/definition/27178/http-header)
3. [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)