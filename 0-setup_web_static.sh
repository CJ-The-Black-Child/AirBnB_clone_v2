#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_Static

echo -e "\e[1;32m START\e[0m"

# Update packages and install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m Packages updated and Nginx installed\e[0m"
echo

# Configure firewall to allow Nginx HTTP connections
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Allowed incoming Nginx HTTP connectiosn\e[0m"
echo

# Create directories
directories=("/data/web_static/releases/test" "/data/web_static/shared")
for dir in "${directories[@]}"; do
	if [ ! -d "$dir" ]; then
		sudo mkdir -p "$dir"
		sudo chown -R ubuntu:ubuntu "$dir"
	fi
done
echo -e "\e[1;32m Directories created\e[0m"
echo

# Add a test HTML file
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >  /data/web_static/releases/test/index.html
echo -e "\e[1;32m Test HTML file added\e[0m"
echo

# Prevent overwriting the current symlink
if [ -d "/data/web_static/current" ]; then
	echo "Path /data/web_static/current exists, removing..."
	sudo rm -rf /data/web_static/current
fi
echo -e "\e[1;32m Prevented symlink overwrite\e[0m"
echo

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR  ubuntu:ubuntu /data
echo -e "\e[1;32m Symbolic link created and ownership set \e[0m"
echo

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_config_line="location /hbnb_static/ {
	alias /data/web_static/current/;
}"
sudo sed -E -i "/location \/ {/a $nginx_config_line" "$nginx_config"
echo -e "\e[1;32m Nginx configuration updated\e[0m"
echo

# Restart now
sudo service nginx restart
echo -e "\e[1;32m Nginx restarted\e[0m"

echo -e "\e[1;32m Setup completed successfully\e[0m"
