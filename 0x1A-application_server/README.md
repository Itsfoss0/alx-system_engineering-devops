![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Application Server

## Concepts
For this project, we expect you to look at the following concepts
- [Web server](https://intranet.alxswe.com/concepts/17)
- [Server](https://intranet.alxswe.com/concepts/67)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)


![its application server innit](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230518%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230518T091137Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=edf4a78d6bde9ba0547096743a2609961ef013598b0fc28ca7ba59cb9d7b5bbf)

## Background context
Your web infrastructure is already serving web pages via Nginx that you installed in your [first web stack project](). While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project

## About
An application server is a software framework or container that provides an environment for running and managing web applications. It acts as an intermediary between the web server and the web application, handling the execution of the application's code and managing resources such as concurrency, session management, and security.

Gunicorn (Green Unicorn) is an example of an application server for Python web applications. It serves as a WSGI (Web Server Gateway Interface) HTTP server that runs your Python web application and handles the communication between the web server and your application.
Running your Python web application using Gunicorn instead of running the module directly offers several advantages:

1. __Improved concurrency__: Gunicorn is designed to handle multiple concurrent requests efficiently. It uses a pre-fork worker model, where multiple worker processes are created to handle incoming requests. Each worker operates independently, allowing your application to handle multiple requests simultaneously. This improves the overall performance and responsiveness of your application, especially under high load.

2. __Load balancing__: Gunicorn can be configured to run multiple worker processes, distributing the incoming requests across them. This load balancing helps distribute the workload and prevents any single worker from becoming overwhelmed. It allows your application to scale horizontally and handle increased traffic by utilizing multiple processes.

3. __Worker process management__: Gunicorn manages the worker processes, starting them, and gracefully shutting them down as needed. It monitors worker health and automatically restarts any workers that have become unresponsive or crashed. This helps ensure the stability and reliability of your application, as Gunicorn can handle process failures and keep your application running.

4. __Integration with web servers__: Gunicorn can seamlessly integrate with popular web servers like Nginx. When used together, Nginx acts as a reverse proxy server, forwarding requests to Gunicorn. This setup allows Nginx to handle tasks like serving static files, caching, SSL termination, and load balancing across multiple Gunicorn instances. It provides an additional layer of flexibility and performance optimization for your web application.

5. __Logging and monitoring__: Gunicorn provides detailed logging that can be useful for debugging and monitoring your application. It logs request information, worker status, and any errors or exceptions encountered. This information is essential for identifying and troubleshooting issues in your application.

6. __Configuration options__: Gunicorn offers a wide range of configuration options that allow you to fine-tune its behavior to suit your application's needs. You can adjust the number of worker processes, timeouts, logging settings, and more. These options give you greater control over how Gunicorn handles your application.

## Resources
1. [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
2. [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04) (As mentioned in the video, do not install Gunicorn using `virtualenv`, just install everything globally)
3. [Running gunicorn](https://docs.gunicorn.org/en/latest/run.html)
4. [Be careful the way Flask handles slashes](https://werkzeug.palletsprojects.com/en/0.14.x/routing/) in [route](https://flask.palletsprojects.com/en/1.0.x/api/#flask.Flask.route) - `strict_slashes`
5. [Upstart documentation](https://doc.ubuntu-fr.org/upstart)