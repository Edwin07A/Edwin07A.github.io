# phil 的工控手记

Edwin07A 的个人博客，首篇文章记录第二次参加全国大学生信息安全与对抗技术竞赛（ISCC）的微型工厂项目。

## 在 GitHub Pages 发布

1. 登录 GitHub，点击右上角 `+` → `New repository`。
2. Repository name 填写 `Edwin07A.github.io`，选择 `Public`，点击 `Create repository`。如果同名仓库已经存在，进入该仓库处理。
3. 新仓库页面点击 `uploading an existing file`；如果已有文件，点击 `Add file` → `Upload files`。
4. 把本目录内的文件和 `assets`、`content` 文件夹拖入上传区。必须让 `index.html` 位于仓库根目录，不要再套一层 `personal-blog` 文件夹。不要直接上传 ZIP。`assets` 必须整文件夹保留层级。
5. 点击 `Commit changes`。提交说明可以填写 `Add personal blog and ISCC write-up`。如有目标分支选项，选主分支。
6. 进入仓库 `Settings` → `Pages`。在 `Build and deployment` 中，Source 选择 `Deploy from a branch`，Branch 选择实际主分支（通常是 `main`），目录选择 `/(root)`，点击 `Save`。
7. 等 GitHub 的 Pages 部署完成。可在 `Actions` 查看部署状态，或回 `Settings` → `Pages` 查看网站链接。
8. 部署成功后的预期地址是 **https://edwin07a.github.io/**。首次部署通常需要几分钟；以 GitHub 的部署状态为准。

网站由静态 HTML、CSS、JavaScript 和本地图片组成，不需要数据库、服务器程序或外部字体服务。首页与文章可以在上传前双击本地 HTML 预览。

## 文件说明

- `index.html`：首页。
- `micro-factory.html`：比赛复盘文章页。
- `content/micro-factory.md`：文章 Markdown 原稿，包含尚待补充的内容边界说明。
- `assets/`：样式、主题与目录交互、图片。
- `build.py`：根据 Markdown 重新生成首页和文章页。
- `.nojekyll`：关闭不需要的 Jekyll 处理。网页本身不依赖它；浏览器上传时看不到隐藏文件也不影响当前页面。

## 修改文章

如果只做少量文字调整，可以直接修改 `micro-factory.html` 中的正文，必要时同步首页摘要。

如果以后希望继续以 Markdown 维护，先安装 Python 和依赖，然后在本目录执行：

```powershell
python -m pip install -r requirements.txt
python build.py
```

修改 `content/micro-factory.md` 后重新构建，再把更新后的 Markdown 和 HTML 上传到仓库。GitHub Pages 不会自动运行本地构建脚本。

文章现为初稿，未填写比赛排名，也没有把规则中的全部防护要求当作已经验证的能力。原始赛题、参考文档、博图工程和可执行程序不在此仓库中；仅使用了标明来源的一张赛题设备照片和重新绘制的示意图。
