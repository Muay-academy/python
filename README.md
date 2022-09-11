# Docker Python 

สร้างไฟล์ชื่อ Dockerfile ด้วยเอดิเตอร์ vi 
vi Dockerfile

ภายในไฟล์ Dockerfile มีอ้างถึงไฟล์ชื่อ requirements.txt และ run.py

การสร้าง image ชื่อ myhello จากไฟล์ 3 ไฟล์นั้น

docker build -t flask_app_dev .

docker run -p 5000:5000 flask_app_dev

อัปโหลด image (เรียกวิธีการนี้ว่า Publish the image) 

