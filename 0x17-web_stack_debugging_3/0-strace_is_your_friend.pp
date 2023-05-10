#!/usr/bin/env puppet
# fix internal server error
exec { 'web stack deubging':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path     => '/usr/local/bin/:/bin/',
  provider => 'shell'
}