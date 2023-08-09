# Puppet manifest to fix why apache is returning 500 error

exec { 'fix the php extension issue':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}