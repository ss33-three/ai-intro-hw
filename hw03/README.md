# HW03 人脸识别系统

## 项目结构

## 功能说明
- 基于 **face_recognition** 库实现**人脸检测**
- 基于 **Streamlit** 提供可视化网页界面
- 支持上传图片 → 自动识别人脸位置 → 展示人脸框
- 可扩展为 1:N 人脸识别（将已知人脸放入 known_faces 目录）

## 环境依赖
- face_recognition
- streamlit
- dlib
- opencv-python
- numpy

## 运行方式
1. 安装依赖
   pip install -r requirements.txt
2. 启动项目
   streamlit run app.py
3. 
3. 访问网页
打开浏览器访问：
http://localhost:8501/
4. 
## 人脸库使用（可选扩展）
将需要识别的人脸图片放入 `known_faces/` 文件夹，即可扩展为人脸识别功能。