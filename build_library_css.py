import os
import re

css = """
/* ===== Library Page Rebuild ===== */
.library-hero {
  background: linear-gradient(135deg, var(--green-dark) 0%, var(--green-mid) 100%), radial-gradient(circle at 14px 14px, rgba(255,255,255,0.05) 2px, transparent 2px);
  background-size: 100% 100%, 28px 28px;
  background-blend-mode: overlay;
  padding: 60px 24px;
  text-align: center;
  color: var(--white);
  border-radius: 0 0 var(--radius) var(--radius);
  margin-bottom: 0;
}

.library-hero h1 {
  font-family: 'Sora', var(--font);
  font-size: 28px;
  font-weight: 800;
  margin-bottom: 12px;
}

.library-hero p {
  color: rgba(255,255,255,0.8);
  font-size: 15px;
  margin-bottom: 24px;
}

.library-stats-chips {
  display: flex;
  gap: 12px;
  justify-content: center;
  flex-wrap: wrap;
}

.stat-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  background-color: rgba(255,255,255,0.15);
  backdrop-filter: blur(8px);
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 600;
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}
.dot.red { background-color: var(--red); }
.dot.amber { background-color: var(--yellow); }
.dot.green { background-color: var(--green-light); }

.library-toolbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: var(--white);
  border-bottom: 1px solid var(--border);
  padding: 16px 24px;
  display: flex;
  gap: 16px;
  align-items: center;
  flex-wrap: wrap;
}

.toolbar-search {
  position: relative;
  flex: 1;
  min-width: 240px;
}

.toolbar-search svg {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
}

.toolbar-search .form-input {
  padding-left: 36px;
  height: 42px;
}

.library-toolbar .form-select {
  width: 160px;
  height: 42px;
}

.view-toggle {
  display: flex;
  background-color: var(--bg);
  border-radius: var(--radius-pill);
  padding: 4px;
  border: 1px solid var(--border);
}

.view-btn {
  background: none;
  border: none;
  padding: 6px 12px;
  border-radius: var(--radius-pill);
  cursor: pointer;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
}

.view-btn.active {
  background-color: var(--white);
  color: var(--green-primary);
  box-shadow: var(--shadow-sm);
}

.library-tabs-container {
  padding: 16px 24px;
  background-color: var(--bg);
}

.library-tabs {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
  padding-bottom: 4px;
}
.library-tabs::-webkit-scrollbar {
  display: none;
}

.library-tab {
  white-space: nowrap;
  padding: 8px 16px;
  background-color: var(--white);
  border: 1px solid var(--border);
  border-radius: var(--radius-pill);
  font-size: 13px;
  font-weight: 500;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.2s;
}

.library-tab:hover {
  border-color: var(--green-primary);
  color: var(--green-primary);
}

.library-tab.active {
  background-color: var(--green-primary);
  border-color: var(--green-primary);
  color: var(--white);
}

.results-count {
  padding: 0 24px;
  font-size: 14px;
  color: var(--text-muted);
  margin-bottom: 16px;
}

.library-grid {
  padding: 0 24px 40px;
  display: grid;
  gap: 18px;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
}

.library-grid.list-view {
  grid-template-columns: 1fr;
}

.disease-card {
  background-color: var(--white);
  border-radius: var(--radius);
  border: 1px solid var(--border);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
  cursor: pointer;
}

.disease-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-md);
  border-color: var(--green-primary);
}

.card-thumb {
  height: 110px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 52px;
  filter: drop-shadow(0 4px 6px rgba(0,0,0,0.15));
}

.card-body {
  padding: 16px;
  flex: 1;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.card-crop-tag {
  background-color: var(--green-tint);
  color: var(--green-primary);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
}

.disease-card h3 {
  font-family: 'Sora', var(--font);
  font-size: 15px;
  font-weight: 700;
  margin-bottom: 8px;
  color: var(--text);
}

.disease-card p {
  font-size: 12px;
  color: var(--text-muted);
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  line-height: 1.5;
}

.card-footer {
  padding: 12px 16px;
  background-color: var(--bg);
  border-top: 1px solid var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.severity-indicator {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
  color: var(--text-muted);
  font-weight: 600;
  text-transform: uppercase;
}

.sev-dots {
  display: flex;
  gap: 3px;
}

.sev-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background-color: var(--border);
}

.sev-dot.active-low { background-color: var(--green-mid); }
.sev-dot.active-med { background-color: var(--yellow); }
.sev-dot.active-high { background-color: var(--red); }

.card-link {
  font-size: 12px;
  font-weight: 600;
  color: var(--green-primary);
  display: flex;
  align-items: center;
  gap: 4px;
}

.card-link svg {
  opacity: 0;
  transform: translateX(-4px);
  transition: all 0.2s;
}

.disease-card:hover .card-link svg {
  opacity: 1;
  transform: translateX(0);
}

/* List View Overrides */
.list-view .disease-card {
  flex-direction: row;
  height: 100px;
}

.list-view .card-thumb {
  width: 80px;
  height: 100%;
  font-size: 40px;
}

.list-view .card-body {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 12px 16px;
}

.list-view .card-header {
  margin-bottom: 4px;
  justify-content: flex-start;
  gap: 8px;
}
.list-view .card-header .badge {
  margin-left: auto;
}

.list-view .disease-card h3 {
  margin-bottom: 4px;
}

.list-view .disease-card p {
  -webkit-line-clamp: 1;
}

.list-view .card-footer {
  display: none;
}
.list-view .severity-indicator {
  position: absolute;
  right: 16px;
  bottom: 12px;
}

/* Extended Modal */
#disease-modal .modal {
  max-width: 620px;
  padding: 0;
  overflow: hidden;
}

.modal-thumb {
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 80px;
  filter: drop-shadow(0 8px 16px rgba(0,0,0,0.2));
  position: relative;
}

.modal-close-btn {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(4px);
  border: none;
  color: white;
  font-size: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-body-content {
  padding: 24px;
  max-height: 60vh;
  overflow-y: auto;
}

.modal-header-info {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.modal-header-info h2 {
  font-family: 'Sora', var(--font);
  font-size: 24px;
  margin: 0;
  color: var(--text);
}

.info-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.info-block {
  background-color: var(--bg);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 16px;
}

.info-block.full {
  grid-column: 1 / -1;
}

.info-block h4 {
  font-size: 12px;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 8px;
  letter-spacing: 0.5px;
}

.info-block p {
  font-size: 14px;
  color: var(--text);
  line-height: 1.5;
}

.sev-bar-container {
  height: 6px;
  background-color: var(--border);
  border-radius: 3px;
  margin-top: 8px;
  overflow: hidden;
}

.sev-bar-fill {
  height: 100%;
  border-radius: 3px;
  transition: width 0.5s ease;
}

.sev-bar-fill.low { width: 30%; background-color: var(--green-light); }
.sev-bar-fill.medium { width: 60%; background-color: var(--yellow); }
.sev-bar-fill.high { width: 100%; background-color: var(--red); }

ul.symptom-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
ul.symptom-list li {
  position: relative;
  padding-left: 16px;
  font-size: 13px;
  margin-bottom: 6px;
  color: var(--text);
}
ul.symptom-list li::before {
  content: '›';
  position: absolute;
  left: 0;
  color: var(--green-primary);
  font-weight: bold;
}

ol.treatment-list {
  list-style: none;
  padding: 0;
  margin: 0;
  counter-reset: step;
}
ol.treatment-list li {
  position: relative;
  padding-left: 28px;
  font-size: 13px;
  margin-bottom: 12px;
  color: var(--text);
  line-height: 1.5;
}
ol.treatment-list li::before {
  counter-increment: step;
  content: counter(step);
  position: absolute;
  left: 0;
  top: 0;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: var(--green-tint);
  color: var(--green-primary);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: 700;
}

@media (max-width: 900px) {
  .library-grid {
    padding: 0 16px 40px;
  }
  .library-toolbar, .library-tabs-container {
    padding-left: 16px;
    padding-right: 16px;
  }
  .info-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {
  .library-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .disease-card p {
    display: none;
  }
}

@media (max-width: 400px) {
  .library-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open('static/css/pages.css', 'r', encoding='utf-8') as f:
    pages_css = f.read()

# Remove old library css
# The old library css spans from /* ===== Library Page ===== */ to /* ===== Reports Page ===== */
import re
new_pages_css = re.sub(r'/\* ===== Library Page ===== \*/.*?/\* ===== Reports Page ===== \*/', '/* ===== Reports Page ===== */', pages_css, flags=re.DOTALL)
new_pages_css += css

with open('static/css/pages.css', 'w', encoding='utf-8') as f:
    f.write(new_pages_css)
print("Updated pages.css")
