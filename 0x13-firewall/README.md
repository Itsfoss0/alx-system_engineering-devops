![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Firewall

![firewall-image](https://media3.giphy.com/media/RkhMKpIYLT9sukfuXg/200w.webp?cid=ecf05e474t9crl794nus46rjdzrlviax0eil8kwxuu0vt5a7&rid=200w.webp&ct=g)

## About
A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predefined security rules. Its primary purpose is to prevent unauthorized access to a network or a computer system while allowing legitimate traffic to pass through.

Firewalls can be implemented in both hardware and software forms. They can be located at the perimeter of a network or installed on individual computers to provide local protection. Firewalls work by examining data packets and determining whether to allow or block them based on a set of predefined rules.

## Background context
### Your servers without a firewall
![serveres-without-firewall](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

## Resources
__Read or watch__:
1. [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)
2. [Google](https://www.google.com/search?q=ufw+linux)
3. [Youtube](https://www.youtube.com/results?search_query=ufw+firewall+ubuntu)

## More info
As explained in the __web stack debugging guide__ concept page, `telnet` is a very good tool to check if sockets are open with `telnet IP PORT`. For example, if you want to check if port 22 is open on `web-02`:

```
itsfoss@itsfoss$ telnet web-02.iamitsfoss.tech 22
Trying 100.26.156.138...
Connected to web-02.iamitsfoss.tech
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
```
We can see for this example that the connection is successful: Connected to web-02.iamitsfoss.tech. 

Now lest try connecting to port 2222

```
itsfoss@itsfoss$ telnet web-02.iamitsfoss.tech 2222
Trying 100.26.156.138...
^C
itsfoss@itsfoss$
```

We can see that the connection never succeeds, so after some time I just use ctrl+c to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will be originating from web-02 and not from the school’s network, bypassing the firewall.