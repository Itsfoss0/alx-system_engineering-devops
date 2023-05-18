#!/usr/bin/env puppet
# Allow the user `holberton`  to login and
# open files without any errors

exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  provider => 'shell'
}

# make some tweaks on the soft file limit
exec { 'increase-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
  provider => 'shell'
}