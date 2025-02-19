# AirBnB clone web server setup and configuration

# Update packages and install Nginx
exec { 'update_and_install_nginx':
command     => 'apt-get -y update && apt-get -y install nginx',
path        => '/usr/bin',
environment => ['DEBIAN_FRONTEND=noninteractive'],
require     => Package['nginx'],
logoutput   => true,
}

# Create /data directory
file { '/data':
ensure => 'directory',
owner  => 'ubuntu',
group  => 'ubuntu',
mode   => '0755',
}

# Create /data/web_static/releases directory
file { '/data/web_static/releases':
ensure => 'directory',
owner  => 'ubuntu',
group  => 'ubuntu',
mode   => '0755',
}

# Add a test HTML file
file { '/data/web_static/releases/test/index.html':
ensure  => 'file',
content => '<h1> welcome to www.congojunior.tech</h1>\n',
owner   => 'ubuntu',
group   => 'ubuntu',
mode    => '0644',
require => File['/data/web_static/releases/test'],
}

# Configure firewall to allow Nginx HTTP connections
exec { 'allow_nginx_http':
command => 'ufw allow "Nginx HTTP"',
path    => '/usr/bin',
require => Exec['update_and_install_nginx'],
}

# Create directories

$directories = ['/data/web_static/release/test', '/data/web_static/shared']
file { $directories:
ensure  => 'directory',
}

# Prevent overwriting the current symlink
file { '/data/web_static/current':
ensure => 'link',
target =>'/data/web_static/releases/test',
owner  => 'ubuntu',
group  => 'ubuntu',
force  => true,
before => File['/etc/nginx/sites-available/default'],
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
ensure  => 'file',
require => Package['nginx'],
}

# Restart Nginx
service {'nginx':
ensure    => 'running',
enable    => true,
subscribe => File[ '/etc/nginx/sites-available/default' ],
}
