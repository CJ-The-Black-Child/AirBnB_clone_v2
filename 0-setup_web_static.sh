#!/usr/bin/env bash
# Sets up the web servers for the deployment of web_Static

echo -e "\e[1;32m START\e[Om"

# Update packages and install Nginx
sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;32m Packages updated and Nginx installed\e[Om"
echo

# Configure firewall to allow Nginx HTTP connections
sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;32m Allowed incoming Nginx HTTP connectiosn\e[Om"
echo

# Create directories
directories=("/data/web_static/releases/test" "/data/web_static/shared")
for dir in "${directories[@]}"; do
	sudo mkdir -p "$dir"
done
echo -e "\e[1;32m Directories created\e[Om"
echo

# Add a test HTML file
echo "<h1> welcome to www.congojunior.tech</h1>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
echo -e "\e[1;32m Test HTML file added\e[Om"
echo

# Prevent overwriting the current symlink
if [ -d "/data/web_static/current" ]; then
	echo "Path /data/web_static/current exists, removing..."
	sudo rm -rf /data/web_static/current
fi
echo -e "\e[1;32m Prevented symlink overwrite\e[Om"
echo

# Create a symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR  ubuntu:ubuntu /data
echo -e "\e[1;32m Symbolic link created and ownership set \e[Om"
echo

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
nginx_config_line="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "381$nginx_config_line" "$nginx_config"
echo -e "\e[1;32m Nginx configuration updated\e[Om"
echo

# Restart now
sudo service nginx restart
echo -e "\e[1;32m Nginx restarted\e[Om"

echo -e "\e[1;32m Setup completed successfully\e[Om"
