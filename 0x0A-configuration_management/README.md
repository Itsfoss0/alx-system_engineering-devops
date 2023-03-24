![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)
  > Configuration Management


![you-are-the-puppet](https://media3.giphy.com/media/NUCunGda7VuN2/200w.webp?cid=ecf05e47hkcr90vsh7hv8bk7qx2aaoog740kqpcm9u4znjjf&rid=200w.webp&ct=g)

## About
Configuration management is the process of defining and maintaining the state of an organization's infrastructure. It involves keeping track of all the systems, applications, and services running within an organization and ensuring that they are all configured and managed in a consistent and repeatable manner.

Configuration management tools, like Puppet, provide a way to automate this process, reducing the need for manual intervention and minimizing the potential for errors.

Puppet is a configuration management tool that allows you to define your infrastructure as code. This means that you can write code to describe how your infrastructure should be configured, and Puppet will automatically enforce that configuration across all the systems it manages.

Puppet uses a client-server architecture, where a Puppet master server controls a fleet of Puppet agents running on managed nodes. The Puppet master server holds the configuration data, while the Puppet agents apply the configurations to the nodes they manage.

If you are new to puppet, the best way  to get started is to dive right in and start experimenting with it. Soon enough, you will be a puppet master (:joy: :joy:)

## Resources

__Read or Watch__
1. [Introduction to configuration management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
2. [Puppet Resource file type](https://www.puppet.com/docs/puppet/5.5/types/file.html)
3. [Puppet's declarative language: Modelling instead of scripting](https://www.puppet.com/blog)
4. [Puppet-lint](http://puppet-lint.com/)
5. [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Note on versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled. 

### Install ```puppet```

```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
You do not need to attempt to upgrade versions. This project is simply a set of tasks to familiarize you with the basic level syntax which is virtually identical in newer versions of Puppet. 

[Puppet 5 docs](https://www.puppet.com/docs/puppet/5.5/puppet_index.html)

### Install puppet-lint
```
$ gem install puppet-lint
```