<div align="center">

# 🚀 夸克网盘自动下载器

**自动监测夸克网盘分享链接更新，发现新文件自动下载到本地**

[![Release](https://img.shields.io/github/v/release/ypq123456789/quark-auto-save-downloader?style=for-the-badge&color=blue)](https://github.com/ypq123456789/quark-auto-save-downloader/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/ypq123456789/quark-auto-save-downloader/total?style=for-the-badge&color=green)](https://github.com/ypq123456789/quark-auto-save-downloader/releases)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)](https://github.com/ypq123456789/quark-auto-save-downloader/releases)

<img src="https://raw.githubusercontent.com/ypq123456789/quark-auto-save-downloader/main/screenshots/监控面板.png" width="700" alt="监控面板截图">

</div>

---

## ✨ 功能特点

- 🔍 **自动监测** — 定时检查分享链接，发现新文件自动下载
- ⚡ **多线程下载** — 8 线程并发分片下载，充分利用带宽
- 📊 **实时进度** — 下载速度、进度条、剩余时间一目了然
- 🔔 **系统通知** — 新文件下载完成后弹出 Windows 通知，点击通知打开下载文件夹
- 📅 **智能管理** — 文件按日期+任务名命名，过期自动清理
- 🔄 **远程同步** — 支持从远程 URL 自动同步任务配置
- ⚙️ **兼容配置** — 支持导入 [quark-auto-save (QAS)](https://github.com/Cp0204/quark-auto-save) 的配置文件，迁移零成本
- 🔒 **最小化到托盘** — 关闭窗口自动最小化，后台静默运行
- 🆕 **自动更新** — 启动时自动检查新版本，一键下载更新

---

## 📥 下载安装

前往 [Releases 页面](https://github.com/ypq123456789/quark-auto-save-downloader/releases/latest) 下载最新版 `夸克网盘自动下载器.exe`，双击即可运行，**无需安装任何环境**。

> 💡 建议将 exe 文件放在一个**单独的文件夹**中运行，程序会在同目录下生成 `config.json` 配置文件。

---

## � 软件截图

| 监控面板 | 任务管理 |
|----------|----------|
| ![监控面板](https://raw.githubusercontent.com/ypq123456789/quark-auto-save-downloader/main/screenshots/监控面板.png) | ![任务管理](https://raw.githubusercontent.com/ypq123456789/quark-auto-save-downloader/main/screenshots/任务管理.png) |

| 设置 | 关于 |
|------|------|
| ![设置](https://raw.githubusercontent.com/ypq123456789/quark-auto-save-downloader/main/screenshots/设置.png) | ![关于](https://raw.githubusercontent.com/ypq123456789/quark-auto-save-downloader/main/screenshots/关于.png) |

---

## �🚀 快速开始

### 第一步：获取 Cookie

Cookie 是程序访问你夸克网盘账号的凭证，获取方法：

1. 打开浏览器，访问 [pan.quark.cn](https://pan.quark.cn) 并**登录账号**
2. 按 `F12` 打开开发者工具
3. 切换到 **`Network`（网络）** 标签
4. 在页面上随便点击一下，等左侧出现请求列表
5. 点击任意一条请求，在右侧找到 **`Request Headers`** → **`Cookie`** 字段
6. 复制完整的 Cookie 值（很长，全部复制）

### 第二步：填写 Cookie 并验证

1. 打开软件，进入 **⚙️ 设置** 页面
2. 将 Cookie 粘贴到「账号设置」输入框
3. 点击「**验证 Cookie**」，显示绑定的账号名即为成功

### 第三步：添加监测任务

进入 **📋 任务管理** 页面，点击「**添加任务**」，填写任务名和分享链接，点「确定」保存。

### 第四步：启动监测

进入 **📡 监控面板**，点击「**启动监测**」，程序立即开始第一次检测，之后按设置的间隔自动运行。

---

## ⚙️ 配置项详解

### 账号设置

| 配置项 | 说明 |
|--------|------|
| **Cookie** | 夸克网盘账号的登录凭证，用于下载文件。Cookie 通常 30 天左右过期，过期后需重新获取并更新 |
| **验证 Cookie** | 点击后连接夸克服务器验证 Cookie 有效性，并显示绑定的账号昵称 |

### 下载设置

| 配置项 | 说明 |
|--------|------|
| **下载目录** | 文件下载到本地的保存位置。点击「浏览...」选择文件夹，或直接输入路径 |
| **检查间隔** | 每隔多少秒检查一次所有任务是否有新文件。默认 300 秒（5 分钟），建议不低于 60 秒，避免请求过于频繁 |
| **自动启动** | 程序打开后自动开始监测，无需手动点「启动监测」 |
| **开机自启** | Windows 开机时自动启动本程序，适合长期追更使用 |
| **系统通知** | 新文件下载完成后弹出 Windows 右下角通知。**点击通知可直接打开下载文件夹** |

### 任务配置项详解

点击「添加任务」或双击任务进入编辑时，有以下配置项：

#### 基本配置

| 配置项 | 说明 |
|--------|------|
| **任务名称** | 任务的标识名，会出现在下载文件名中（格式：`日期-任务名-文件名`） |
| **分享链接** | 夸克网盘分享页面的 URL，格式如 `https://pan.quark.cn/s/xxxxxxxxxx` |
| **更新星期** | 勾选哪几天运行此任务。例如只勾「周五周六周日」适合只在周末更新的剧集。**全不勾选等同于每天都运行** |

#### 进阶配置（点击「▶ 进阶选项」展开）

| 配置项 | 说明 | 示例 |
|--------|------|------|
| **截止日期** | 超过此日期后停止检测该任务，适合有结束日期的连载内容。格式 `YYYY-MM-DD`，留空表示永不停止 | `2026-06-30` |
| **文件过滤（正则）** | 只下载文件名匹配此正则表达式的文件，留空则下载全部文件 | `.*\.(mp4\|mkv)` 只下载视频文件 |
| **更新子目录** | 分享链接有多层文件夹时，指定只监测某个子目录的文件名，支持部分匹配 | 填 `1080p` 只处理名为「1080p」的子目录 |
| **重命名替换** | 下载后对文件名做正则替换，格式为 `匹配Pattern\|替换内容`，支持捕获组 `\1\2\3` | `S01E(\d+).*\.mp4\|第\1集.mp4` |
| **网盘路径** | 兼容 QAS 的字段，用于指定网盘转存路径，本软件直接下载到本地时**可留空** | `/我的追更/某某剧` |

### 配置导入与远程同步

| 功能 | 说明 |
|------|------|
| **导入本地配置文件** | 从本地选择 `config.json` 或 `quark_config.json` 导入任务列表（支持 QAS 格式） |
| **从剪贴板导入 JSON** | 将配置 JSON 内容复制到剪贴板后点击，直接粘贴导入 |
| **启用远程配置定期同步** | 勾选后定期从「远程地址」拉取配置，实现远程更新任务列表 |
| **远程地址** | 配置文件的直链 URL，需能直接返回 JSON 内容（如 GitHub Raw 链接） |
| **同步间隔** | 多久同步一次远程配置，默认 3600 秒（1 小时） |
| **立即同步远程配置** | 手动触发一次远程同步，不等待定时器 |

---

## 📋 文件命名规则

下载文件统一保存在下载目录下，命名格式：

```
日期-任务名称-原文件名
```

例如：
```
2026-03-01-追光者-EP01_1080P.mp4
2026-03-02-追光者-EP02_1080P.mp4
2026-03-02-某纪录片-第1集.mp4
```

程序每天自动清理**前一天**的文件，只保留最新下载的内容，避免占用过多磁盘空间。

---

## 🔄 从 QAS 项目迁移

如果你是 [quark-auto-save (QAS)](https://github.com/Cp0204/quark-auto-save) 项目的用户，可以一键导入任务配置，无需重新录入：

### 导出 QAS 配置

**Docker 部署的用户：**
```bash
docker cp 容器名:/app/data/quark_config.json ./quark_config.json
```

**本地部署的用户：**  
直接找到 QAS 项目目录下的 `quark_config.json` 文件。

### 导入到本软件

1. 打开本软件，进入 **⚙️ 设置** 页面
2. 找到「**配置导入与远程同步**」区域
3. 点击「**📂 导入本地配置文件**」，选择刚才导出的 `quark_config.json`
4. 任务列表自动导入完成 ✅

> ⚠️ **注意**：本软件配置格式在 QAS 基础上扩展了更多字段（本地下载路径、运行星期等），本软件导出的配置**不能**反向导入 QAS。

---

## ❓ 常见问题

<details>
<summary><b>Q: 下载速度很慢怎么办？</b></summary>

夸克网盘对非会员有下载限速（约 100-200 KB/s）。软件已使用 8 线程并发下载最大化利用带宽，但总速度仍受限于夸克的限速策略。

如果想提升速度，推荐去**闲鱼**购买 88VIP 夸克会员（约 5 元/年），非高峰期基本不限速，性价比极高。
</details>

<details>
<summary><b>Q: Cookie 过期了怎么办？</b></summary>

Cookie 通常 30 天左右过期。过期后软件日志会提示验证失败，重新在浏览器复制最新 Cookie，粘贴到设置页保存即可。
</details>

<details>
<summary><b>Q: 文件过滤（正则）怎么写？</b></summary>

只有文件名匹配正则的文件才会被下载：

- 只下载 mp4/mkv：`.*\.(mp4|mkv)`
- 只下载含「1080p」的文件：`1080p`
- 只下载第 1-9 集：`EP0[1-9]`

留空则下载分享链接中的**全部文件**。
</details>

<details>
<summary><b>Q: 更新子目录怎么用？</b></summary>

当分享链接里有多个子文件夹（如「1080p」「4K」「花絮」），只想下载其中某个文件夹时使用。填入文件夹名关键词即可，支持部分匹配。填 `1080p` 则只处理名为「1080p」的子目录。留空则处理根目录下所有文件。
</details>

<details>
<summary><b>Q: 程序关闭后还在运行吗？</b></summary>

点击「×」关闭窗口时，程序会**最小化到系统托盘**（任务栏右下角），继续后台运行。右键托盘图标 → 选择「退出」可彻底关闭。
</details>

<details>
<summary><b>Q: 如何从 QAS (quark-auto-save) 迁移？</b></summary>

详见上方「从 QAS 项目迁移」章节。简单来说：导出 `quark_config.json` → 在本软件设置页点击「导入本地配置文件」即可。
</details>

<details>
<summary><b>Q: 支持 Mac / Linux 吗？</b></summary>

目前仅支持 Windows。
</details>

---

## 📝 更新日志

### v1.0.0 (2026-03-01)
- 🎉 首个正式版本发布
- 自动监测分享链接更新并下载到本地
- 8 线程并发分片下载，实时进度与速度显示
- 系统托盘后台运行，点击通知打开下载文件夹
- 支持导入 [quark-auto-save (QAS)](https://github.com/Cp0204/quark-auto-save) 配置文件
- 按日期自动清理过期文件
- 启动自动检查更新

---

## 🙏 致谢

- [quark-auto-save (QAS)](https://github.com/Cp0204/quark-auto-save) — 配置格式参考，本软件支持导入其配置文件
- [PyQt6](https://www.riverbankcomputing.com/software/pyqt/) — GUI 框架

---

<div align="center">
<sub>Made with ❤️ for Quark Cloud Drive users</sub>
</div>
