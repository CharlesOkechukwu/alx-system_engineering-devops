# install dependencies for flask
package { 'python3':
  ensure => '3.8.10'
}

# pip install
package { 'python3-pip':
  ensure => present
}
# flask install
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
# werkzeug install
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
