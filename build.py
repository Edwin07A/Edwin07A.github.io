"""Build the static blog. Upload the generated files without running Python on GitHub."""
from pathlib import Path
from html import escape
import re
import markdown

ROOT = Path(__file__).resolve().parent
raw = (ROOT / "content/micro-factory.md").read_text(encoding="utf-8")
_, front, body = raw.split("---", 2)
meta = dict(line.split(": ", 1) for line in front.strip().splitlines())
body = re.sub(r"^\s*# [^\n]+\n", "", body, count=1)
body = body.replace("../assets/", "assets/")
count = len(re.findall(r"[\u4e00-\u9fff]", body))
minutes = max(1, round(count / 350))
md = markdown.Markdown(extensions=["extra", "toc"], extension_configs={"toc": {"toc_depth": "2-2"}})
article = md.convert(body)
# Stable ASCII anchors are easier to copy and work with the TOC observer in every browser.
for index, item in enumerate(md.toc_tokens):
    previous, current = item["id"], f"section-{index + 1}"
    article = article.replace(f'id="{previous}"', f'id="{current}"')
    md.toc = md.toc.replace(f'href="#{previous}"', f'href="#{current}"')

TITLE = meta["title"]
DESCRIPTION = meta["description"]
TAGS = '<span class="tag">PLC</span><span class="tag">TIA Portal</span><span class="tag">工业安全</span><span class="tag">ISCC</span>'
HEADER = '''<a class="skip-link" href="#main">跳转到正文</a>
<header class="site-header"><div class="wrap header-inner">
<a class="brand" href="index.html" aria-label="phil 的工控手记首页"><span class="brand-mark" aria-hidden="true">&lt;/&gt;</span>工控手记<small>BY PHIL</small></a>
<nav aria-label="主导航"><a href="index.html#posts">文章</a><a class="about-link" href="index.html#about">关于</a><a href="https://github.com/Edwin07A" target="_blank" rel="noopener noreferrer">GitHub ↗</a><button class="theme-toggle" type="button" data-theme-toggle>深色</button></nav>
</div></header>'''
FOOTER = '''<footer class="site-footer"><div class="wrap footer-inner"><span>© 2026 phil · 记录自动化与工业安全的实践</span><a href="https://github.com/Edwin07A" target="_blank" rel="noopener noreferrer">Edwin07A / GitHub ↗</a></div></footer>'''

def page(title, description, content, canonical):
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · phil 的工控手记</title><meta name="description" content="{escape(description, quote=True)}">
<meta name="author" content="phil"><meta name="color-scheme" content="light dark"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:type" content="{'article' if canonical != 'index.html' else 'website'}"><meta property="og:locale" content="zh_CN">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg"><link rel="stylesheet" href="assets/style.css"><script src="assets/site.js" defer></script>
</head><body>{HEADER}{content}{FOOTER}</body></html>'''

index = f'''<main id="main" class="wrap"><section class="hero" aria-labelledby="hero-title"><div>
<div class="eyebrow">PHIL / ENGINEERING NOTES</div><h1 id="hero-title">记录自动化与<br>工业安全的实践</h1>
<p>我是 phil，也叫 Edwin07A。这里记录我的比赛与项目经历，从 PLC 程序、工厂仿真，到数据采集与通信保护。</p>
<a class="intro-link" href="micro-factory.html">阅读第二次 ISCC 参赛记录 <span aria-hidden="true">↗</span></a></div>
<img class="hero-art" src="assets/images/notebook.svg" alt="线条绘制的 PLC、机械臂和受保护通信通道" width="500" height="390"></section>
<section id="posts" aria-labelledby="posts-title"><div class="section-heading"><h2 id="posts-title">比赛与项目</h2><span>01 ARTICLE</span></div>
<a class="post-card" href="micro-factory.html"><img src="assets/images/control-platform.jpg" alt="赛题文档中的微型工厂综合实训装置" width="915" height="686"><div class="post-content"><div class="eyebrow">COMPETITION / ISCC</div><h3>{escape(TITLE)}</h3><p>从工位动作、变量映射到触摸屏控制，记录我负责的程序编写、MES 加解密页面与人脸识别接入。</p><div class="tags">{TAGS}</div><div class="post-bottom"><span>phil · 约 {minutes} 分钟</span><span>阅读全文 ↗</span></div></div></a></section>
<section id="about" class="about" aria-labelledby="about-title"><div><div class="eyebrow">ABOUT THIS BLOG</div><h2 id="about-title">关于这个博客</h2></div><p>把做过的项目整理成能回头查阅的记录：系统怎样连接、程序怎样控制、问题怎样定位，以及哪些地方还值得继续验证。第一篇从第二次参加 ISCC 的微型工厂项目开始。</p></section></main>'''

detail = f'''<div class="reading-progress" aria-hidden="true"></div><main id="main" class="wrap"><header class="article-header"><a class="back-link" href="index.html#posts">← 返回文章列表</a><div class="eyebrow">COMPETITION / ISCC · PROJECT NOTES</div><h1>{escape(TITLE)}</h1><p class="article-deck">从仿真工位到 PLC 程序，再到加密页面与通信准入。这是我的第二次 ISCC 参赛记录。</p><div class="article-meta"><span>作者 phil / Edwin07A</span><span>约 {minutes} 分钟阅读</span><span>比赛复盘初稿</span></div><div class="tags">{TAGS}</div></header>
<div class="article-layout"><article class="article-body" aria-label="比赛复盘正文">{article}<div class="article-end"><a href="index.html#posts">← 回到工控手记</a></div></article><aside class="article-aside" aria-label="文章目录"><p class="aside-label">ON THIS PAGE / 本文目录</p>{md.toc}<div class="aside-bottom"><a href="#main">回到顶部 ↑</a></div></aside></div></main>'''

(ROOT / "index.html").write_text(page("首页", "phil 的个人博客，记录 ISCC 比赛、PLC 自动化与工业安全实践。", index, "index.html"), encoding="utf-8")
(ROOT / "micro-factory.html").write_text(page(TITLE, DESCRIPTION, detail, "micro-factory.html"), encoding="utf-8")
print(f"Built index.html and micro-factory.html; about {count} Chinese characters / {minutes} minutes.")
