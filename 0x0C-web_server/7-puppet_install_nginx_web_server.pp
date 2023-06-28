#A puppet manifest to install nginx
#queried on port 80

exec {'apt-get update':
     command => '/usr/bin/sudo apt-get -y update'
}

package {'nginx':
ensure => installed,
 require => Exec['apt-get update']
}



exec {'write-to-file':
     command => "/usr/bin/echo 'Hello World!' | /var/www/html/index.html > /dev/null"
}




$new_rule = "\\\n\tlocation = /redirect_me {\n\t\t return 301 https://github.com/Abasay;\n\t}\n"

exec {'backup':
command => '/usr/bin/sudo cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bakup',
require => Exec['write-to-file']
}

exec {"$new_rule":
command => "/usr/bin/sudo sed -i '53i $NEW_RULE' /etc/nginx/sites-available/default",
require => Exec['backup'],
}

exec {'restart':
command => '/usr/bin/sudo nginx restart',
require => Exec['$new_rule']
}