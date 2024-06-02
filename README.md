# cloud-project
## config server aws:
### cài đặt python, cài pip
Sử dụng pip để install flask, flask_al...
### filename:
tạo file runweb.service với nội dung:
[Unit]
Description=Gunicorn instance target
After=network.target
[Service]
User=ec2-user
Group=www-data
WorkingDirectory=/home/ec2-user/cloud-project
ExecStart=/home/ec2-user/cloud-project/venv/bin/gunicorn -w 4 -b 0.0.0.0:80 home:app
Restart=always
[Install]
WantedBy=multi-user.target

### chạy lệnh sau để khởi động service vừa tạo:
sudo systemctl enable runweb.service
sudo systemctl start runweb.service

## thiết lập VPC
tạo 2 AZ, mỗi vùng 2 subnet 1 public và 1 private
tạo nat gateway đi kèm
associate các nhóm subnet lại

## thiết lập ec2
tạo cấu hình t1.micro, sử dụng subnet public 2 của zone số 2 (us-east-1b)
chọn đúng vpc chứa 2 subnet đã tạo bên trên, đồng thời chỉ định Network Security Group tương ứng.

## thiết lập RDS
Sử dụng 2 database Primary và Secondary, đặt trong 2 vùng subnet private đảm bảo bảo mật
thiết đặt Security group chỉ cho phép máy chủ nằm trong Ec2 được kết nối

## thiết lập load balancing và auto scaling group
tạo target group
tạo load balancing
cài đặt ngưỡng cho auto scaling, min 2, desired 2, max 4
