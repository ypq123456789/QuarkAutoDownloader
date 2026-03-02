# -*- coding: utf-8 -*-
"""
自动更新检查器 - 从 GitHub Releases 获取最新版本

功能:
  - 检查 GitHub 最新 Release 版本
  - 与当前版本比较
  - 提供下载链接
"""
import os
import re
import json
import requests
import subprocess
import tempfile
import threading
from packaging import version as pkg_version

# ═══════════════════════════════════════════
# 配置区 - 发布前修改这里
# ═══════════════════════════════════════════
CURRENT_VERSION = "1.0.1"
GITHUB_OWNER = "ypq123456789"
GITHUB_REPO = "quark-auto-save-downloader"
GITHUB_REPO_URL = f"https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}"
GITHUB_API_URL = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/releases/latest"
# ═══════════════════════════════════════════


def get_current_version():
    """获取当前版本号"""
    return CURRENT_VERSION


def check_update(timeout=10):
    """
    检查 GitHub 最新版本
    返回 dict:
      - has_update: bool
      - current_version: str
      - latest_version: str
      - release_name: str
      - release_notes: str  (Markdown 格式的发布说明)
      - download_url: str   (EXE 下载直链)
      - html_url: str       (Release 页面链接)
      - published_at: str
      - error: str | None
    """
    result = {
        "has_update": False,
        "current_version": CURRENT_VERSION,
        "latest_version": "",
        "release_name": "",
        "release_notes": "",
        "download_url": "",
        "html_url": "",
        "published_at": "",
        "error": None,
    }

    try:
        headers = {"Accept": "application/vnd.github.v3+json"}
        resp = requests.get(GITHUB_API_URL, headers=headers, timeout=timeout)

        if resp.status_code == 404:
            result["error"] = "仓库未找到或暂无发布版本"
            return result

        resp.raise_for_status()
        data = resp.json()

        tag = data.get("tag_name", "")
        # 去掉 v 前缀: "v1.0.1" -> "1.0.1"
        latest_ver = re.sub(r"^v", "", tag)

        result["latest_version"] = latest_ver
        result["release_name"] = data.get("name", tag)
        result["release_notes"] = data.get("body", "")
        result["html_url"] = data.get("html_url", "")
        result["published_at"] = data.get("published_at", "")

        # 查找 EXE 资源
        for asset in data.get("assets", []):
            name = asset.get("name", "")
            if name.lower().endswith(".exe"):
                result["download_url"] = asset.get("browser_download_url", "")
                break

        # 比较版本
        try:
            if latest_ver and pkg_version.parse(latest_ver) > pkg_version.parse(CURRENT_VERSION):
                result["has_update"] = True
        except Exception:
            # 简单字符串比较作为后备
            if latest_ver and latest_ver != CURRENT_VERSION:
                result["has_update"] = True

    except requests.exceptions.Timeout:
        result["error"] = "检查更新超时，请稍后重试"
    except requests.exceptions.ConnectionError:
        result["error"] = "无法连接到 GitHub，请检查网络"
    except Exception as e:
        result["error"] = f"检查更新失败: {str(e)}"

    return result


def check_update_async(callback):
    """
    异步检查更新 (在后台线程执行，结果通过 callback 返回)
    callback(result_dict) 会在后台线程中调用
    """
    def _worker():
        result = check_update()
        callback(result)

    t = threading.Thread(target=_worker, daemon=True)
    t.start()
    return t


def download_update(download_url, progress_callback=None, timeout=300):
    """
    下载更新文件到临时目录
    progress_callback(downloaded_bytes, total_bytes) 可选
    返回: (success, file_path_or_error)
    """
    try:
        resp = requests.get(download_url, stream=True, timeout=timeout)
        resp.raise_for_status()

        total = int(resp.headers.get("content-length", 0))
        # 保存到临时目录
        tmp_dir = tempfile.mkdtemp(prefix="quark_update_")
        filename = download_url.split("/")[-1] or "update.exe"
        tmp_path = os.path.join(tmp_dir, filename)

        downloaded = 0
        with open(tmp_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if progress_callback:
                        progress_callback(downloaded, total)

        return True, tmp_path

    except Exception as e:
        return False, str(e)


def open_release_page():
    """在默认浏览器中打开 Release 页面"""
    import webbrowser
    webbrowser.open(f"{GITHUB_REPO_URL}/releases/latest")


def open_github_page():
    """在默认浏览器中打开 GitHub 仓库"""
    import webbrowser
    webbrowser.open(GITHUB_REPO_URL)
