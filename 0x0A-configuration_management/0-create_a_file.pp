#Create a file in `/tmp/school`

file {'/tmp/school':
ensure  => present,
content => 'I love Puppet',
group   => 'www-data',
owner   => 'www-data',
mode    => '0744'
}
