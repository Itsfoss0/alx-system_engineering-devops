#!/usr/bin/env puppet
# Allow the user `holberton`  to login and
# open files without any errors

exec { 'changing-security-limits':
  command  => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path     => '/usr/local/bin/:/bin/'
}

# increament soft file limits holberton
exec { 'increament-security-limits-for-holberton-user':
  command  => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf'
  path     => '/usr/local/bin/:/bin/',
}