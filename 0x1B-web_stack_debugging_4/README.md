![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Web stakck debugging #4


![the sky is the limit](https://media3.giphy.com/media/HV58tke92RgSLZIB7m/200w.webp?cid=ecf05e47n4bb6h4oal5mlkxrs63o7nadh4l1zi8qnhqtxml3&ep=v1_gifs_search&rid=200w.webp&ct=g)

## About
![the sky is actually not the limit](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/313/frdkCrb.jpg)

Lets test how well our system operates under pressure shall we?
In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends! 

## Install puppet-lint
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```