# Makefile for building Matcha-TTS wheel

# 项目元数据
PACKAGE_NAME=cosyvoice-tts

# Python 解释器
PYTHON=python3

# 打包输出目录
DIST_DIR=dist

# 默认目标：构建 wheel
all: build

# 清除编译和打包生成的文件
clean:
	rm -rf build/ $(DIST_DIR)/ *.egg-info
	find . -type f -name "*.so" -delete
	find . -type f -name "*.c" -delete
	find . -type f -name "*.cpp" -delete
	find . -type f -name "*.pyd" -delete

# 安装打包工具（仅需一次）
init:
	$(PYTHON) -m pip install --upgrade pip setuptools wheel build numpy

# 打包为 .whl 文件
build: clean
	$(PYTHON) -m build

# 安装本地生成的 .whl 文件
install:
	pip install $(DIST_DIR)/$(PACKAGE_NAME)*.whl

# 发布到正式 PyPI
upload:
	twine upload $(DIST_DIR)/*

.PHONY: all clean init build install upload
