(() => {
  const button = document.querySelector('[data-theme-toggle]');
  const applyTheme = (theme) => {
    document.documentElement.dataset.theme = theme;
    if (button) {
      const dark = theme === 'dark';
      button.textContent = dark ? '浅色' : '深色';
      button.setAttribute('aria-label', dark ? '切换浅色主题' : '切换深色主题');
      button.setAttribute('aria-pressed', String(dark));
    }
  };
  let saved;
  try { saved = localStorage.getItem('field-notes-theme'); } catch {}
  applyTheme(saved === 'dark' || saved === 'light' ? saved :
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
  button?.addEventListener('click', () => {
    const theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    applyTheme(theme);
    try { localStorage.setItem('field-notes-theme', theme); } catch {}
  });
  const progress = document.querySelector('.reading-progress');
  if (progress) {
    const update = () => {
      const distance = document.documentElement.scrollHeight - window.innerHeight;
      progress.style.transform = `scaleX(${distance > 0 ? Math.min(1, window.scrollY / distance) : 0})`;
    };
    addEventListener('scroll', update, { passive: true });
    addEventListener('resize', update);
    update();
  }
  if ('IntersectionObserver' in window) {
    const links = [...document.querySelectorAll('.toc a')];
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) if (entry.isIntersecting) {
        links.forEach(link => {
          const current = link.hash === '#' + entry.target.id;
          link.classList.toggle('active', current);
          if (current) link.setAttribute('aria-current', 'location');
          else link.removeAttribute('aria-current');
        });
      }
    }, { rootMargin: '-12% 0px -72% 0px' });
    document.querySelectorAll('.article-body h2').forEach(heading => observer.observe(heading));
  }
})();
