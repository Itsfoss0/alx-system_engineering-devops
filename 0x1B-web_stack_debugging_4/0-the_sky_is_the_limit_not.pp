#!/usr/bin/env puppet

# patch up our nginx webserver to handle
# a large number of requests
exec { 'fix nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# restart Nginx service (nginx.service)
-> exec { 'nginx-restart':
  command => 'sudo service nginx restart',
  path    => '/etc/init.d/'
}