# 使用包含 CUDA 的 PyTorch 基础镜像
FROM nvidia/cuda:12.0.0-base-ubuntu20.04
# 设置工作目录
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
# 将当前目录的内容复制到工作目录中
COPY . /app
RUN apt-get update && \
     apt-get install -y python3 python3-pip nvidia-cuda-toolkit
# 安装依赖
#--no-cache-dir
RUN pip install  \
    Pillow==10.1.0 \
    torchvision==0.16.2 \
    transformers==4.40.0 \
    sentencepiece==0.1.99 \
    accelerate==0.30.1 \
    bitsandbytes \
    flask -i https://pypi.tuna.tsinghua.edu.cn/simple
#bitsandbytes==0.43.1
# 暴露端口
EXPOSE 6790

# 运行 app.py
CMD ["python3", "app.py"]