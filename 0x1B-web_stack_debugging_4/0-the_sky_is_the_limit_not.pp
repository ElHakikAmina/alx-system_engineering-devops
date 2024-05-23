# Increases the amount of traffic an Nginx server can handle.

# Increase the UNLIMIT of the default file
exec { 'update unlimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  provider    => 'shell'
}

# Restart Nginx
-> exec { 'nginx-restart':
  command => 'service nginx restart',
  provider    => 'shell'
}
