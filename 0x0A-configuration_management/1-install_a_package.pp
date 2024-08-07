# Install flask package

package { 'werkzeug':
  ensure   => '2.1.1',
  name     => 'werkzeug',
  provider => pip3,
}

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => pip3,
  require  => Package['werkzeug']
}
