<div align="center">

# 🚀 夸克网盘自动下载器

**自动监测夸克网盘分享链接更新，发现新文件自动下载到本地**

[![Release](https://img.shields.io/github/v/release/ypq123456789/quark-auto-save-downloader?style=for-the-badge&color=blue)](https://github.com/ypq123456789/quark-auto-save-downloader/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/ypq123456789/quark-auto-save-downloader/total?style=for-the-badge&color=green)](https://github.com/ypq123456789/quark-auto-save-downloader/releases)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)](https://github.com/ypq123456789/quark-auto-save-downloader/releases)

<img src="https://raw.githubusercontent.com/ypq123456789/quark-auto-save-downloader/main/screenshots/main.png" width="700" alt="主界面截图">

</div>

---

## ✨ 功能特点

- 🔍 **自动监测** — 定时检查分享链接，发现新文件自动下载
- ⚡ **多线程下载** — 8 线程并发分片下载，充分利用带宽
- 📊 **实时进度** — 下载速度、进度条、剩余时间一目了然
- 🔔 **系统通知** — 新文件下载完成后弹出 Windows 通知
- 📅 **智能管理** — 文件按日期+任务名命名，过期自动清理
- 🔄 **远程同步** — 支持从远程 URL 自动同步任务配置
- ⚙️ **兼容配置** — 完全兼容 [quark-auto-save](https://github.com/ypq123456789/quark-auto-save) 原项目配置格式
- 🔒 **最小化到托盘** — 关闭窗口自动最小化，后台静默运行
- 🆕 **自动更新** — 启动时自动检查新版本，一键下载更新

## 📥 下载安装

### 方式一：直接下载 EXE（推荐）

前往 [Releases 页面](https://github.com/ypq123456789/quark-auto-save-downloader/releases/latest) 下载最新版 `夸克网盘自动下载器.exe`。

> 💡 无需安装 Python 环境，双击即可运行！

### 方式二：从源码运行

```bash
git clone https://github.com/ypq123456789/quark-auto-save-downloader.git
cd quark-auto-save-downloader
pip install -r requirements.txt
python main.py
```

## 🚀 快速开始

### 1. 获取 Cookie

1. 打开浏览器，访问 [pan.quark.cn](https://pan.quark.cn) 并登录
2. 按 `F12` 打开开发者工具
3. 切换到 `Network`（网络）标签
4. 随便点击一个请求，在 `Request Headers` 中找到 `Cookie` 字段
5. 复制完整的 Cookie 值

### 2. 配置软件

1. 双击运行 `夸克网盘自动下载器.exe`
2. 进入 **⚙️ 设置** 页面
3. 粘贴 Cookie，点击「验证 Cookie」
4. 设置下载目录和检查间隔
5. 点击「保存设置」

### 3. 添加任务

进入 **📋 任务管理** 页面：
- 点击「添加任务」，填写任务名和夸克网盘分享链接
- 或点击「从配置文件导入」，直接导入原项目的 `quark_config.json`

### 4. 开始监测

进入 **📡 监控面板**，点击「启动监测」即可！

## 📋 文件命名规则

下载的文件统一保存在下载根目录，命名格式：

```
日期-任务名称-原文件名
```

例如：
```
2026-03-01-7光阴之外-11_4K@BeeWeb.mp4
2026-03-01-追更剧场-某某剧EP01.mp4
```

每天自动清理前一天的文件，保持目录整洁。

## 🔧 兼容性

完全兼容 [quark-auto-save](https://github.com/ypq123456789/quark-auto-save) 项目的配置文件格式：

- ✅ `quark_config.json` 直接导入
- ✅ Cookie 格式兼容（单个/多个/换行分隔）
- ✅ 任务字段完全兼容（taskname, shareurl, pattern, runweek, enddate 等）
- ✅ magic_regex 魔法正则兼容
- ✅ Docker 导出的配置可直接使用

## 💰 授权说明

| 版本 | 功能 | 价格 |
|------|------|------|
| **试用版** | 完整功能，7 天免费体验 | 免费 |
| **永久版** | 无限期使用，永久更新 | 付费获取激活码 |

> 试用期结束后，您仍可查看任务列表和设置，但无法启动监测下载功能。

获取激活码请联系开发者。

## 📷 软件截图

<details>
<summary>点击查看更多截图</summary>

### 监控面板
实时显示监测状态、下载进度、速度和日志。

### 任务管理
管理所有追更任务，支持添加、编辑、删除和批量导入。

### 设置页面
配置 Cookie、下载目录、检查间隔、远程配置同步。

### 关于 & 更新
查看版本信息、检查更新、管理授权。

</details>

## ❓ 常见问题

<details>
<summary><b>Q: 下载速度很慢怎么办？</b></summary>

夸克网盘对非会员有下载限速（约 100-200 KB/s）。软件已使用 8 线程并发下载来最大化利用带宽，但总速度仍受限于夸克的限制策略。

如果您是夸克会员，速度会明显更快。
</details>

<details>
<summary><b>Q: Cookie 多久会过期？</b></summary>

通常 30 天左右。过期后需要重新在浏览器中获取并更新。
</details>

<details>
<summary><b>Q: 支持 Mac / Linux 吗？</b></summary>

目前仅支持 Windows。如需其他平台，可以从源码运行（需安装 Python 和 PyQt6）。
</details>

<details>
<summary><b>Q: 如何从 Docker 版迁移？</b></summary>

1. 从 Docker 容器中导出配置：`docker cp 容器名:/app/data/quark_config.json ./`
2. 在软件中点击「从配置文件导入」选择该文件即可
</details>

## 📝 更新日志

### v1.0.0 (2026-03-01)
- 🎉 首个正式版本发布
- 自动监测分享链接更新并下载
- 8 线程并发分片下载
- 实时下载进度与速度显示
- 系统托盘后台运行
- 完全兼容 quark-auto-save 配置
- 按日期自动清理过期文件
- 授权系统（7 天免费试用）
- 自动检查更新

## 🙏 致谢

- [quark-auto-save](https://github.com/ypq123456789/quark-auto-save) — 原始项目
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) — GUI 框架
- [PyInstaller](https://pyinstaller.org/) — EXE 打包

---

<div align="center">
<sub>Made with ❤️ for Quark Cloud Drive users</sub>
</div>
