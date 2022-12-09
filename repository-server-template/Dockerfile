FROM ubuntu:latest
RUN apt updata && apt upgrade -y && apt install nginx cron git -y && cron start && service nginx start
RUN cd /var/www/html && git clone https://github.com/foolaway/jjvmm-repo.git
RUN echo '*/5 * * * * www-data cd /var/www/html && git clone https://github.com/foolaway/jjvmm-repo.git' >> /etc/crontab