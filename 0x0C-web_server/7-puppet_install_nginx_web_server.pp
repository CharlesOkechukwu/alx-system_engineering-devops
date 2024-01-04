# for the installation of nginx and configuration of nginx server
exec { 'update':
  command => '/usr/bin/apt-get -y update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update']
}

file { 'index.html':
  ensure  => 'present',
  path    => '/var/www/html/index.html',
  content => 'Hello World!'
}

exec { 'restart':
  command => '/usr/bin/service nginx restart',
  require => Package['ngix']
}

file_line { 'set redirection':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  notify  => Exec['restart'],
  require => Package['nginx']
}
