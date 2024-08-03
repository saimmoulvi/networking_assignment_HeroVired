## Prerequisites
  - Ensure you have 'nginx' installed on your local machine

## Nginx Configuration
  - The nginx configuration file for awesomeweb is mentioned below
```
server {
    listen 80;
    server_name awesomeweb;

    root /var/www/html/awesomeweb;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}

```

## HTML File
  - index.html file inside awesomeweb directory is mentioned below
```
<!DOCTYPE html>
<html>
<head>
    <title>Congratulations you are seeing awesomeweb server block</title>
</head>
</html>
```

## Steps to be performed:

1. **Install Nginx**:
   
    `sudo apt update`
   
    `sudo apt install nginx`
    

2. **Create HTML Directory:**
   
    `sudo mkdir -p /var/www/html/awesomeweb`
   
    `sudo chown -R $USER:$USER /var/html/awesomeweb`
    

3. **Place index.html inside awesomeweb directory:**
    
    `sudo nano /var/www/html/awesomeweb/index.html`
    

4. **Create and place the above awesomeweb file:**
    
    `sudo nano /etc/nginx/site-available/awesomeweb`
    

5. **Enable the Configuration:**

   `sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/`

6. **Restart Nginx:**   

   `sudo systemctl restart nginx`

7. **Update Hosts file and add the follwing line:**

    `sudo nano /etc/hosts`

    `127.0.0.1 awesomeweb`

8. **Open your browser and mention `http://awesomeweb`**    
    

