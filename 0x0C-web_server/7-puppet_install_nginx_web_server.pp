# puppet manifest to configure the web server
exec { 'dist update':
        command  => '/usr/bin/apt-get update',
        provider => 'shell'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['dist update']
}

file {'/var/www/html/index.html':
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '7624'
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
