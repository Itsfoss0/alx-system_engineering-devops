# Configuring the SSH client using puppet 

file {'/.ssh/school':
  ensure => present,
  content => 'Host *
    HostName 54.146.84.110
    SeverAliveInterval 120
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
  owner => 'itsfoss', 
  group => 'itsfoss',
  mode => '0744'
}
