# increase file limit for user holberton

exec {'soft_limit':
  command => 'sed -i "s/holberton soft nofile [0-9]\+/holberton soft nofile 50000/" /etc/security/limits.conf',
  path    => '/bin:/usr/bin:/usr/sbin'
}

exec {'hard_limit':
  command => 'sed -i "s/holberton hard nofile [0-9]\+/holberton hard nofile 50000/" /etc/security/limits.conf',
  path    => '/bin:/usr/bin:/usr/sbin'
}
