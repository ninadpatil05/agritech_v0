import os
import glob
import re

html_files = glob.glob('*.html')

head_additions = """
  <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  <meta name="description" content="AgriTech - Smart Crop Detective. AI-powered crop disease detection, soil analysis, and agricultural advice." />
  <meta property="og:title" content="AgriTech - Smart Crop Detective" />
  <meta property="og:description" content="AI-powered crop disease detection and agricultural advice." />
  <meta property="og:type" content="website" />
"""

footer_replacement = """<footer class="site-footer">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; align-items: center; gap: 1rem;">
      <p style="margin: 0;">AgriTech — Smart Crop Detective — intelligent farming for a more resilient tomorrow.</p>
      <div style="display: flex; gap: 1.5rem; font-size: 0.9rem;">
        <a href="/" style="color: var(--muted); text-decoration: none;">Home</a>
        <a href="/contact.html" style="color: var(--muted); text-decoration: none;">Contact Us</a>
        <a href="#" style="color: var(--muted); text-decoration: none;">Privacy Policy</a>
        <a href="#" style="color: var(--muted); text-decoration: none;">Terms of Service</a>
      </div>
    </div>
  </footer>"""

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already added it to prevent duplicates
    if '<link rel="icon"' not in content:
        # Add to head
        content = re.sub(r'(<head>)', r'\1' + head_additions, content, count=1, flags=re.IGNORECASE)
    
    # Replace footer variations
    content = re.sub(r'<footer>[\s\S]*?</footer>', footer_replacement, content, flags=re.IGNORECASE)
    content = re.sub(r'<footer class="site-footer">[\s\S]*?</footer>', footer_replacement, content, flags=re.IGNORECASE)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} HTML files.")
