#fix for nginx

exec {'fix-for-nginx':
  command => 'sed -i "s@usr/share/nginx/html@var/www/html@g" /etc/nginx/sites-available/default',
  path    => '/usr/local/bin/:/bin/',
  before  => Exec['restart-nginx']
}

#Restart nginx
exec {'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
