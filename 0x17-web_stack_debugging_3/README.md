![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Web stack monitoring #3

![six-stages-of-debuging](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png)

## Background Context
When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.

The web stack you are debugging today is a Wordpress website running on a LAMP stack.

## Requeirements
### General

- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
Y- our Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4

## More Info
Install puppet-lint
```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```