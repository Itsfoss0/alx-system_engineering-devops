# Puppet manifest to configure a webserver
# to install nginx and add custom http headers

exec { 'Updated System':
        command  => '/usr/bin/apt-get update',
        provider => 'shell'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['Updated System']
}

file {'/var/www/html/index.html':
  content => 'Hello World!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '7624'
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

exec {'Custom Header':
  command  => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
