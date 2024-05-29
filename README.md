
# MiniCPM-V-2_5_docker

This repository contains the core files for setting up and running MiniCPM-V-2_5 using Docker. The project includes:

- `app.py`: The main application file.
- `docker-compose.yml`: Docker Compose configuration file.
- `Dockerfile`: Instructions to build the Docker image.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/15812653950/MiniCPM-V-2_5_docker.git
   cd MiniCPM-V-2_5_docker
   ```

2. Build and run the Docker containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

### Usage

Once the Docker containers are up and running, you can interact with the application through the specified ports and endpoints defined in the `docker-compose.yml` file.

### Files

- `app.py`: This is the main application file that contains the logic of MiniCPM-V-2_5.
- `docker-compose.yml`: Defines the services, networks, and volumes for Docker Compose.
- `Dockerfile`: Contains the instructions to build the Docker image.

---

# MiniCPM-V-2_5_docker

这个仓库包含了使用 Docker 设置和运行 MiniCPM-V-2_5 的核心文件。项目包括：

- `app.py`：主要的应用程序文件。
- `docker-compose.yml`：Docker Compose 配置文件。
- `Dockerfile`：构建 Docker 镜像的指令文件。

## 开始

### 前提条件

- Docker
- Docker Compose

### 安装

1. 克隆仓库：

   ```bash
   git clone https://github.com/15812653950/MiniCPM-V-2_5_docker.git
   cd MiniCPM-V-2_5_docker
   ```

2. 使用 Docker Compose 构建并运行 Docker 容器：

   ```bash
   docker-compose up --build
   ```

### 用法

当 Docker 容器启动并运行后，你可以通过 `docker-compose.yml` 文件中定义的端口和端点与应用程序进行交互。

### 文件

- `app.py`：这是包含 MiniCPM-V-2_5 逻辑的主要应用程序文件。
- `docker-compose.yml`：定义了 Docker Compose 的服务、网络和卷。
- `Dockerfile`：包含构建 Docker 镜像的指令。
