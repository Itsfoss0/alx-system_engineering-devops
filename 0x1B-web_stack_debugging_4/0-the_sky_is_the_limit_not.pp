#!/usr/bin/env puppet

# patch up our nginx webserver to handle
# a large number of requests
exec { 'Fix nginx':
  provider => 'shell',
  command => 'sed -i "s/15/4096/" /etc/default/nginx'
}

#restart the service (nginx.service)

exec { 'restart nginx':
  command => 'sudo service nginx restart',
  provider => 'shell',
  path    => '/etc/init.d/'
}