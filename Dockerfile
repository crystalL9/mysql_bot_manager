# Sử dụng hình ảnh gốc từ Docker Hub
FROM mysql:latest

# Thiết lập biến môi trường cho MySQL
ENV MYSQL_ROOT_PASSWORD=admin
ENV MYSQL_DATABASE=admin


# Cổng mặc định để truy cập MySQL
EXPOSE 3306
CMD ["mysqld"]