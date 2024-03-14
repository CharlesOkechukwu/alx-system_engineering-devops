# increase the amount of traffic Nginx server can handle

exec {'increase limit':
  command => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 3000\"/' /etc/default/nginx",
  path    => '/usr/bin:/usr/sbin:/bin'
}

# restart
exec {'nrestart':
  command => '/usr/sbin/service nginx restart',
  require => Exec['increase limit']
}
