import json
html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Disease Library - Smart Crop Detective</title>
  <meta name="description" content="Browse all 38 plant diseases across 14 crops. Learn about symptoms and treatments.">
  <meta property="og:title" content="Smart Crop Detective - AI Crop Disease Detection">
  <meta property="og:description" content="Detect crop diseases instantly with AI. Free for Indian farmers.">
  <meta property="og:image" content="/assets/images/og-banner.jpg">
  <meta property="og:type" content="website">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Smart Crop Detective">
  <meta name="twitter:description" content="AI-powered crop disease detection for farmers.">
  <meta name="twitter:image" content="/assets/images/og-banner.jpg">
  <link rel="icon" href="/static/favicon.svg">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/css/base.css">
  <link rel="stylesheet" href="/static/css/components.css">
  <link rel="stylesheet" href="/static/css/pages.css">
  <script src="/static/js/theme.js"></script>
</head>
<body class="auth-protected">
  <!-- Sidebar -->
  <aside class="sidebar" id="sidebar">
    <a href="/dashboard.html" class="sidebar-logo">🌿 Smart Crop Detective</a>
    
    <nav class="sidebar-nav">
      <a href="/dashboard.html" class="sidebar-link">🏠 Dashboard</a>
      <a href="/detect.html" class="sidebar-link">🔬 Detect</a>
      <a href="/weather.html" class="sidebar-link">🌤 Weather</a>
      <a href="/library.html" class="sidebar-link active">📚 Library</a>
      <a href="/reports.html" class="sidebar-link">📋 Reports</a>
      <a href="/profile.html" class="sidebar-link">👤 Profile</a>
    </nav>
    
    <div class="sidebar-user">
      <div class="sidebar-avatar" id="sidebar-avatar">U</div>
      <div class="sidebar-user-info">
        <div class="sidebar-user-name" id="sidebar-name">User</div>
        <div class="sidebar-user-email" id="sidebar-email">user@example.com</div>
        <a href="#" class="sidebar-logout" onclick="handleLogout(event)">Logout</a>
      </div>
    </div>
  </aside>

  <!-- Mobile Nav -->
  <nav class="mobile-nav">
    <div class="mobile-nav-inner">
      <a href="/dashboard.html" class="mobile-nav-link">
        <span>🏠</span>
        <span>Home</span>
      </a>
      <a href="/detect.html" class="mobile-nav-link">
        <span>🔬</span>
        <span>Detect</span>
      </a>
      <a href="/weather.html" class="mobile-nav-link">
        <span>🌤</span>
        <span>Weather</span>
      </a>
      <a href="/library.html" class="mobile-nav-link active">
        <span>📚</span>
        <span>Library</span>
      </a>
      <a href="/profile.html" class="mobile-nav-link">
        <span>👤</span>
        <span>Profile</span>
      </a>
    </div>
  </nav>

  <!-- Main Content -->
  <main class="main-with-sidebar">
    <!-- Hero Banner -->
    <div class="library-hero">
      <h1>📚 Disease Library</h1>
      <p>Complete reference for crop diseases, symptoms & treatments</p>
      <div class="library-stats-chips">
        <div class="stat-chip"><div class="dot red"></div>29 Diseases</div>
        <div class="stat-chip"><div class="dot amber"></div>14 Crops</div>
        <div class="stat-chip"><div class="dot green"></div>9 Healthy variants</div>
      </div>
    </div>

    <!-- Sticky Toolbar -->
    <div class="library-toolbar">
      <div class="toolbar-search">
        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
        <input type="text" class="form-input" id="search-input" placeholder="Search disease or crop...">
      </div>
      <select class="form-select" id="status-filter">
        <option value="">All Status</option>
        <option value="diseased">Diseased</option>
        <option value="healthy">Healthy</option>
      </select>
      <select class="form-select" id="severity-filter">
        <option value="">All Severity</option>
        <option value="high">High</option>
        <option value="medium">Medium</option>
        <option value="low">Low</option>
      </select>
      <div class="view-toggle">
        <button class="view-btn active" id="btn-grid-view" title="Grid View" onclick="setViewMode('grid')">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path></svg>
        </button>
        <button class="view-btn" id="btn-list-view" title="List View" onclick="setViewMode('list')">
          <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path></svg>
        </button>
      </div>
    </div>

    <!-- Crop Tabs -->
    <div class="library-tabs-container">
      <div class="library-tabs" id="crop-tabs">
        <!-- Rendered dynamically -->
      </div>
    </div>

    <!-- Results Count -->
    <div class="results-count" id="results-count">Showing 38 results</div>

    <!-- Grid -->
    <div class="library-grid" id="library-grid">
      <!-- Rendered dynamically -->
    </div>
  </main>

  <!-- Extended Modal -->
  <div class="modal-overlay" id="disease-modal">
    <div class="modal">
      <button class="modal-close-btn" onclick="Modal.hide('disease-modal')">×</button>
      <div class="modal-thumb" id="modal-thumb-bg">
        <span id="modal-thumb-emoji"></span>
      </div>
      <div class="modal-body-content">
        <div class="modal-header-info">
          <div>
            <span class="pill pill-sm" id="modal-crop"></span>
            <span class="badge" id="modal-status"></span>
          </div>
          <h2 id="modal-disease-name"></h2>
        </div>
        
        <div class="info-grid">
          <div class="info-block full">
            <h4>About</h4>
            <p id="modal-description"></p>
          </div>
          <div class="info-block">
            <h4>Severity</h4>
            <p id="modal-severity-label"></p>
            <div class="sev-bar-container">
              <div class="sev-bar-fill" id="modal-severity-bar"></div>
            </div>
          </div>
          <div class="info-block">
            <h4>Spreads Via</h4>
            <p id="modal-spreads-via"></p>
          </div>
          <div class="info-block full">
            <h4>Key Symptoms</h4>
            <ul class="symptom-list" id="modal-symptoms"></ul>
          </div>
          <div class="info-block full">
            <h4>Treatment Steps</h4>
            <ol class="treatment-list" id="modal-treatment"></ol>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-ghost" onclick="Modal.hide('disease-modal')">Close</button>
        <a href="/detect.html" class="btn btn-orange">🔬 Detect This Disease</a>
      </div>
    </div>
  </div>

  <script src="/static/js/api.js"></script>
  <script src="/static/js/auth-guard.js"></script>
  <script src="/static/js/utils.js"></script>
  <script>
    const diseases = [
      { crop: 'Apple', disease: 'Apple Scab', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind and rain splashing', emoji: '🍎', thumbGradient: 'linear-gradient(135deg, #fecaca 0%, #ef4444 100%)', desc: 'A fungal disease causing dark, scabby lesions on leaves and fruit.', symptoms: ['Olive-green spots on leaves', 'Dark, scabby spots on fruit', 'Leaves turning yellow and dropping', 'Fruit deformation'], treatment: ['Prune trees to improve air circulation', 'Remove fallen infected leaves', 'Apply fungicide during bud break', 'Plant resistant varieties'] },
      { crop: 'Apple', disease: 'Black Rot', healthy: false, severity: 'high', cause: 'Fungal', spread: 'Infected debris and rain', emoji: '🍎', thumbGradient: 'linear-gradient(135deg, #b91c1c 0%, #7f1d1d 100%)', desc: 'A fungal disease causing circular leaf spots and fruit rot.', symptoms: ['Frogeye leaf spots', 'Black rotting on fruit', 'Cankers on branches', 'Mummified fruit'], treatment: ['Remove and destroy mummified fruit', 'Prune out dead or diseased wood', 'Apply protective fungicides', 'Ensure good orchard sanitation'] },
      { crop: 'Apple', disease: 'Cedar Apple Rust', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind-blown spores from cedar trees', emoji: '🍎', thumbGradient: 'linear-gradient(135deg, #fed7aa 0%, #ea580c 100%)', desc: 'A fungal disease requiring both cedar and apple trees. Causes orange spots on leaves.', symptoms: ['Yellow/orange spots on upper leaves', 'Tubular structures on leaf undersides', 'Premature leaf drop', 'Small fruit lesions'], treatment: ['Remove nearby cedar trees if possible', 'Apply preventative fungicides in spring', 'Plant rust-resistant apple varieties', 'Prune to improve airflow'] },
      { crop: 'Apple', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🍎', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Vibrant green leaves', 'Firm unblemished fruit', 'Strong branch growth'], treatment: ['Continue regular watering schedule', 'Maintain routine fertilization', 'Monitor for early signs of pests'] },
      
      { crop: 'Blueberry', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🫐', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Deep green healthy foliage', 'Plump firm berries', 'Vigorous new cane growth'], treatment: ['Maintain proper soil pH (4.5-5.5)', 'Ensure consistent moisture', 'Prune annually to encourage new growth'] },
      
      { crop: 'Cherry', disease: 'Powdery Mildew', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind-blown spores', emoji: '🍒', thumbGradient: 'linear-gradient(135deg, #f3f4f6 0%, #9ca3af 100%)', desc: 'A fungal disease creating white powdery coating on leaves. Thrives in dry conditions.', symptoms: ['White powdery spots on leaves', 'Distorted new growth', 'Premature leaf drop', 'Reduced fruit quality'], treatment: ['Apply sulfur or appropriate fungicide', 'Ensure proper spacing for air flow', 'Avoid overhead watering', 'Prune infected shoots'] },
      { crop: 'Cherry', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🍒', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Clear unblemished leaves', 'Firm healthy fruit', 'Strong branch structure'], treatment: ['Continue regular maintenance', 'Monitor during humid periods', 'Apply standard preventative sprays'] },
      
      { crop: 'Corn', disease: 'Cercospora Leaf Spot', healthy: false, severity: 'high', cause: 'Fungal', spread: 'Wind and rain splash', emoji: '🌽', thumbGradient: 'linear-gradient(135deg, #fef08a 0%, #ca8a04 100%)', desc: 'A fungal disease causing gray to tan rectangular lesions on corn leaves.', symptoms: ['Rectangular tan lesions on leaves', 'Lesions restricted by leaf veins', 'Blighting of entire leaves', 'Reduced yield'], treatment: ['Rotate crops with non-hosts', 'Till residue into the soil', 'Apply foliar fungicides early', 'Use resistant hybrids'] },
      { crop: 'Corn', disease: 'Common Rust', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind-blown spores', emoji: '🌽', thumbGradient: 'linear-gradient(135deg, #fdba74 0%, #c2410c 100%)', desc: 'A fungal disease causing small, circular to elongate brown pustules on both leaf surfaces.', symptoms: ['Oval rust-colored pustules', 'Yellow halos around spots', 'Leaves drying out', 'Stunted plant growth'], treatment: ['Plant rust-resistant hybrids', 'Apply fungicides if identified early', 'Monitor fields during cool, humid weather', 'Ensure proper plant spacing'] },
      { crop: 'Corn', disease: 'Northern Leaf Blight', healthy: false, severity: 'high', cause: 'Fungal', spread: 'Crop residue and wind', emoji: '🌽', thumbGradient: 'linear-gradient(135deg, #d1d5db 0%, #4b5563 100%)', desc: 'A fungal disease causing long, elliptical gray-green or tan lesions on corn leaves.', symptoms: ['Cigar-shaped gray-green lesions', 'Lesions turning tan', 'Loss of photosynthetic area', 'Premature plant death'], treatment: ['Use resistant corn hybrids', 'Manage crop residue by tillage', 'Rotate crops annually', 'Apply preventative fungicides'] },
      { crop: 'Corn', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🌽', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Dark green broad leaves', 'Sturdy stalks', 'Well-developed ears'], treatment: ['Maintain optimal nitrogen levels', 'Ensure adequate watering', 'Scout for early pest signs'] },
      
      { crop: 'Grape', disease: 'Black Rot', healthy: false, severity: 'high', cause: 'Fungal', spread: 'Rain splash and mummified fruit', emoji: '🍇', thumbGradient: 'linear-gradient(135deg, #a78bfa 0%, #6d28d9 100%)', desc: 'A fungal disease causing leaf spots and severe rotting of grape berries.', symptoms: ['Small tan leaf spots with dark borders', 'Black lesions on shoots', 'Berries shrivel into hard black mummies', 'Premature fruit drop'], treatment: ['Remove all mummified fruit from vines', 'Prune to open the canopy', 'Apply protective fungicides early', 'Plow in diseased leaves'] },
      { crop: 'Grape', disease: 'Esca (Black Measles)', healthy: false, severity: 'high', cause: 'Fungal', spread: 'Pruning wounds', emoji: '🍇', thumbGradient: 'linear-gradient(135deg, #d8b4fe 0%, #7e22ce 100%)', desc: 'A complex fungal disease causing tiger-stripe patterns on grape leaves.', symptoms: ['Tiger-stripe yellow/red patterns on leaves', 'Dark spotting on berries', 'Sudden vine wilt', 'Wood decay in trunk'], treatment: ['Prune during dry weather', 'Protect pruning wounds with paste', 'Remove severely infected vines', 'Practice good vineyard sanitation'] },
      { crop: 'Grape', disease: 'Leaf Blight', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind and rain', emoji: '🍇', thumbGradient: 'linear-gradient(135deg, #e9d5ff 0%, #9333ea 100%)', desc: 'A fungal disease causing brown lesions that spread rapidly across grape leaves.', symptoms: ['Irregular brown leaf lesions', 'Yellowing around spots', 'Defoliation', 'Reduced vine vigor'], treatment: ['Ensure good canopy management', 'Apply copper-based fungicides', 'Remove fallen leaves in autumn', 'Improve air circulation'] },
      { crop: 'Grape', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🍇', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Vibrant green leaves', 'Plump developing berries', 'Strong vine growth'], treatment: ['Maintain regular pruning', 'Ensure proper trellising', 'Monitor moisture levels'] },
      
      { crop: 'Orange', disease: 'Haunglongbing (Citrus Greening)', healthy: false, severity: 'high', cause: 'Bacterial', spread: 'Asian citrus psyllid', emoji: '🍊', thumbGradient: 'linear-gradient(135deg, #fed7aa 0%, #c2410c 100%)', desc: 'A bacterial disease spread by psyllids causing yellow shoots and bitter fruit.', symptoms: ['Asymmetrical yellow mottling on leaves', 'Lopsided, bitter fruit', 'Premature fruit drop', 'Twig dieback'], treatment: ['Control the psyllid vector with insecticides', 'Remove and destroy infected trees', 'Use certified disease-free nursery stock', 'Enhance tree nutrition'] },
      
      { crop: 'Peach', disease: 'Bacterial Spot', healthy: false, severity: 'high', cause: 'Bacterial', spread: 'Wind-driven rain', emoji: '🍑', thumbGradient: 'linear-gradient(135deg, #fbcfe8 0%, #db2777 100%)', desc: 'A bacterial disease causing small, dark, water-soaked spots on leaves and fruit.', symptoms: ['Small water-soaked leaf spots', 'Shot-hole appearance as spots drop out', 'Deep pits or cracks on fruit', 'Severe defoliation'], treatment: ['Plant resistant peach varieties', 'Apply copper sprays in autumn', 'Maintain tree vigor', 'Avoid high nitrogen fertilizers'] },
      { crop: 'Peach', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🍑', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Lush green foliage', 'Firm smooth fruit', 'Healthy branch structure'], treatment: ['Continue annual pruning', 'Maintain balanced fertilization', 'Water consistently during fruit fill'] },
      
      { crop: 'Pepper', disease: 'Bacterial Spot', healthy: false, severity: 'high', cause: 'Bacterial', spread: 'Rain splash and contaminated seed', emoji: '🫑', thumbGradient: 'linear-gradient(135deg, #fecaca 0%, #dc2626 100%)', desc: 'A bacterial disease causing small, dark, water-soaked spots on leaves and fruit.', symptoms: ['Dark brown spots with yellow halos', 'Scab-like spots on peppers', 'Leaves turning yellow and dropping', 'Sunscald due to defoliation'], treatment: ['Use certified disease-free seeds', 'Apply copper-based bactericides', 'Rotate crops every 2-3 years', 'Avoid overhead irrigation'] },
      { crop: 'Pepper', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🫑', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Deep green leaves', 'Glossy firm peppers', 'Strong upright growth'], treatment: ['Maintain consistent soil moisture', 'Apply balanced fertilizer', 'Support heavy fruiting branches'] },
      
      { crop: 'Potato', disease: 'Early Blight', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind and rain', emoji: '🥔', thumbGradient: 'linear-gradient(135deg, #fde68a 0%, #d97706 100%)', desc: 'A fungal disease causing dark concentric ring patterns (target spots) on older leaves.', symptoms: ['Dark spots with concentric rings', 'Yellowing around lesions', 'Lower leaves die first', 'Dark sunken lesions on tubers'], treatment: ['Apply protectant fungicides', 'Rotate crops with non-solanaceous plants', 'Maintain adequate plant nutrition', 'Destroy infected vines'] },
      { crop: 'Potato', disease: 'Late Blight', healthy: false, severity: 'high', cause: 'Fungal', spread: 'Wind-blown spores in wet weather', emoji: '🥔', thumbGradient: 'linear-gradient(135deg, #9ca3af 0%, #374151 100%)', desc: 'A devastating fungal disease causing water-soaked lesions that rapidly destroy foliage.', symptoms: ['Water-soaked spots on leaves', 'White fungal growth on undersides', 'Rapid browning and shriveling', 'Reddish-brown tuber rot'], treatment: ['Apply specific anti-oomycete fungicides', 'Use certified seed potatoes', 'Destroy cull piles', 'Harvest only in dry conditions'] },
      { crop: 'Potato', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🥔', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Vibrant green canopy', 'Thick healthy stems', 'Good tuber development'], treatment: ['Maintain proper hilling', 'Ensure consistent soil moisture', 'Monitor for Colorado potato beetle'] },
      
      { crop: 'Raspberry', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🍃', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Bright green leaves', 'Strong cane growth', 'Firm berries'], treatment: ['Prune old canes after harvest', 'Trellis for good airflow', 'Maintain regular watering'] },
      
      { crop: 'Soybean', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🟫', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Dark green trifoliate leaves', 'Abundant pod set', 'Strong root nodules'], treatment: ['Ensure adequate phosphorus/potassium', 'Scout for aphids', 'Maintain good weed control'] },
      
      { crop: 'Squash', disease: 'Powdery Mildew', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind-blown spores', emoji: '🎃', thumbGradient: 'linear-gradient(135deg, #e5e7eb 0%, #6b7280 100%)', desc: 'A fungal disease creating white powdery coating on leaves. Thrives in dry conditions.', symptoms: ['White powdery spots on upper leaves', 'Leaves turn yellow and brown', 'Premature vine death', 'Sunscald on fruit'], treatment: ['Plant resistant varieties', 'Apply sulfur or horticultural oils', 'Improve air circulation', 'Avoid excessive nitrogen'] },
      
      { crop: 'Strawberry', disease: 'Leaf Scorch', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Rain splash', emoji: '🍓', thumbGradient: 'linear-gradient(135deg, #fecaca 0%, #b91c1c 100%)', desc: 'A fungal disease causing purple to red spots that develop tan centers on strawberry leaves.', symptoms: ['Irregular purplish spots on leaves', 'Spots coalesce causing leaf death', 'Brown calyxes on fruit', 'Reduced plant vigor'], treatment: ['Remove infected leaves at renovation', 'Apply protective fungicides', 'Ensure good plant spacing', 'Avoid overhead watering'] },
      { crop: 'Strawberry', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🍓', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Bright green trifoliate leaves', 'Firm red berries', 'Vigorous runner production'], treatment: ['Maintain straw mulch', 'Provide 1 inch of water weekly', 'Renovate beds after harvest'] },
      
      { crop: 'Tomato', disease: 'Bacterial Spot', healthy: false, severity: 'high', cause: 'Bacterial', spread: 'Rain splash and contaminated seed', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #fecaca 0%, #dc2626 100%)', desc: 'A bacterial disease causing small, dark, water-soaked spots on leaves and fruit.', symptoms: ['Small dark spots with yellow halos', 'Scabby spots on tomatoes', 'Severe leaf drop', 'Sunscald from canopy loss'], treatment: ['Use certified disease-free seed', 'Apply copper-mancozeb sprays', 'Rotate away from nightshades', 'Avoid overhead irrigation'] },
      { crop: 'Tomato', disease: 'Early Blight', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind and rain', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #fde68a 0%, #d97706 100%)', desc: 'A fungal disease causing dark concentric ring patterns (target spots) on older leaves.', symptoms: ['Concentric ring patterns on lower leaves', 'Yellowing around spots', 'Dark sunken lesions on stems', 'Fruit drop'], treatment: ['Apply protectant fungicides early', 'Mulch to prevent soil splash', 'Stake or cage plants', 'Remove lower infected leaves'] },
      { crop: 'Tomato', disease: 'Late Blight', healthy: false, severity: 'high', cause: 'Fungal', spread: 'Wind-blown spores in wet weather', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #9ca3af 0%, #374151 100%)', desc: 'A devastating fungal disease causing water-soaked lesions that rapidly destroy foliage.', symptoms: ['Large, dark, water-soaked lesions', 'White fuzzy growth on leaf undersides', 'Greasy brown spots on fruit', 'Rapid plant death'], treatment: ['Apply specific anti-oomycete fungicides immediately', 'Destroy infected plants entirely', 'Ensure excellent air circulation', 'Plant resistant varieties'] },
      { crop: 'Tomato', disease: 'Leaf Mold', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind in high humidity', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #bef264 0%, #4d7c0f 100%)', desc: 'A fungal disease causing pale green to yellow spots on upper leaf surfaces.', symptoms: ['Pale green spots on upper leaves', 'Olive-green fuzzy growth on undersides', 'Leaves wither and die', 'Primarily affects greenhouse tomatoes'], treatment: ['Reduce humidity in greenhouses', 'Increase air circulation', 'Apply appropriate fungicides', 'Use resistant varieties'] },
      { crop: 'Tomato', disease: 'Septoria Leaf Spot', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Rain splash', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #fbcfe8 0%, #be185d 100%)', desc: 'A fungal disease causing many small circular spots with dark borders.', symptoms: ['Small circular spots with gray centers', 'Tiny black fruiting bodies in spots', 'Severe yellowing of lower leaves', 'Rapid defoliation'], treatment: ['Apply protectant fungicides', 'Remove infected lower leaves', 'Mulch soil surface', 'Water at the base of plants'] },
      { crop: 'Tomato', disease: 'Spider Mites', healthy: false, severity: 'high', cause: 'Pest', spread: 'Crawling and wind dispersal', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #fed7aa 0%, #c2410c 100%)', desc: 'Tiny arachnids that cause stippling and bronzing of leaves. Thrive in hot, dry conditions.', symptoms: ['Tiny yellow spots (stippling) on leaves', 'Fine webbing on plant parts', 'Leaves turn bronze or yellow', 'Stunted plant growth'], treatment: ['Apply horticultural oils or insecticidal soap', 'Release predatory mites', 'Keep plants well-watered', 'Avoid broad-spectrum insecticides'] },
      { crop: 'Tomato', disease: 'Target Spot', healthy: false, severity: 'medium', cause: 'Fungal', spread: 'Wind and rain', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #fcd34d 0%, #b45309 100%)', desc: 'A fungal disease causing brown circular lesions with concentric rings.', symptoms: ['Brown lesions with concentric rings on leaves', 'Sunken lesions on fruit', 'Premature leaf drop'], treatment: ['Apply targeted fungicides', 'Improve air circulation', 'Rotate crops', 'Destroy crop debris'] },
      { crop: 'Tomato', disease: 'Yellow Leaf Curl Virus', healthy: false, severity: 'high', cause: 'Viral', spread: 'Whiteflies', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #fef08a 0%, #ca8a04 100%)', desc: 'A viral disease spread by whiteflies causing severe leaf curling and yellowing.', symptoms: ['Upward curling of leaf margins', 'Severe yellowing (chlorosis)', 'Stunted plant growth', 'Flower drop and zero fruit set'], treatment: ['Control whitefly populations', 'Use reflective mulches', 'Plant resistant varieties', 'Remove and destroy infected plants immediately'] },
      { crop: 'Tomato', disease: 'Mosaic Virus', healthy: false, severity: 'high', cause: 'Viral', spread: 'Mechanical transmission (hands/tools)', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #d9f99d 0%, #65a30d 100%)', desc: 'A viral disease causing mottled light and dark green patterns on leaves.', symptoms: ['Mottled light/dark green leaves', 'Fern-like leaf distortion', 'Stunted growth', 'Internal fruit browning'], treatment: ['Wash hands and tools thoroughly', 'Do not use tobacco products near plants', 'Remove and destroy infected plants', 'Plant resistant varieties'] },
      { crop: 'Tomato', disease: 'Healthy', healthy: true, severity: 'low', cause: 'None', spread: 'N/A', emoji: '🍅', thumbGradient: 'linear-gradient(135deg, #bbf7d0 0%, #22c55e 100%)', desc: 'No disease detected. The plant appears to be in good health.', symptoms: ['Deep green healthy foliage', 'Strong thick stems', 'Abundant flower and fruit set'], treatment: ['Maintain consistent watering', 'Feed with tomato-specific fertilizer', 'Prune suckers for better airflow'] }
    ];

    const cropEmojis = {
      'Apple': '🍎', 'Blueberry': '🫐', 'Cherry': '🍒', 'Corn': '🌽',
      'Grape': '🍇', 'Orange': '🍊', 'Peach': '🍑', 'Pepper': '🫑',
      'Potato': '🥔', 'Raspberry': '🍃', 'Soybean': '🟫', 'Squash': '🎃',
      'Strawberry': '🍓', 'Tomato': '🍅'
    };

    let currentViewMode = 'grid';
    let currentCropTab = '';

    // Handle logout
    function handleLogout(e) {
      e.preventDefault();
      API.post('/logout', {}).then(() => {
        sessionStorage.removeItem('agritech_user');
        window.location.href = '/index.html';
      });
    }

    // Load user data
    window.addEventListener('userLoaded', function(e) {
      const user = e.detail;
      const name = user.first_name || 'User';
      document.getElementById('sidebar-avatar').textContent = name[0].toUpperCase();
      document.getElementById('sidebar-name').textContent = name;
      document.getElementById('sidebar-email').textContent = user.email;
    });

    function setViewMode(mode) {
      currentViewMode = mode;
      document.getElementById('btn-grid-view').classList.toggle('active', mode === 'grid');
      document.getElementById('btn-list-view').classList.toggle('active', mode === 'list');
      
      const grid = document.getElementById('library-grid');
      if (mode === 'list') {
        grid.classList.add('list-view');
      } else {
        grid.classList.remove('list-view');
      }
    }

    function renderTabs() {
      const tabsContainer = document.getElementById('crop-tabs');
      const crops = Object.keys(cropEmojis).sort();
      
      let html = `<button class="library-tab active" onclick="selectTab('')">All Crops</button>`;
      crops.forEach(crop => {
        html += `<button class="library-tab" onclick="selectTab('${crop}')">${cropEmojis[crop]} ${crop}</button>`;
      });
      tabsContainer.innerHTML = html;
    }

    function selectTab(crop) {
      currentCropTab = crop;
      const tabs = document.querySelectorAll('.library-tab');
      tabs.forEach(tab => {
        if ((crop === '' && tab.textContent === 'All Crops') || tab.textContent.includes(crop)) {
          tab.classList.add('active');
        } else {
          tab.classList.remove('active');
        }
      });
      filterDiseases();
    }

    function renderDiseases(filtered) {
      const grid = document.getElementById('library-grid');
      const count = document.getElementById('results-count');
      
      count.textContent = `Showing ${filtered.length} of ${diseases.length} entries`;
      
      grid.innerHTML = filtered.map(d => {
        const severityClass = {
          'low': 'active-low',
          'medium': 'active-med',
          'high': 'active-high'
        }[d.severity];
        
        return `
        <div class="disease-card" onclick="showDisease('${d.crop}', '${d.disease}')">
          <div class="card-thumb" style="background: ${d.thumbGradient}">
            ${d.emoji}
          </div>
          <div class="card-body">
            <div class="card-header">
              <span class="card-crop-tag">${d.crop}</span>
              <span class="badge ${d.healthy ? 'badge-green' : 'badge-red'}">
                ${d.healthy ? 'Healthy' : 'Diseased'}
              </span>
            </div>
            <h3>${d.disease}</h3>
            <p>${d.desc}</p>
          </div>
          <div class="severity-indicator" style="display: none;"> <!-- For list view right side -->
            <div class="sev-dots">
              <div class="sev-dot active-low"></div>
              <div class="sev-dot ${d.severity === 'medium' || d.severity === 'high' ? 'active-med' : ''}"></div>
              <div class="sev-dot ${d.severity === 'high' ? 'active-high' : ''}"></div>
            </div>
          </div>
          <div class="card-footer">
            <div class="severity-indicator">
              <div class="sev-dots">
                <div class="sev-dot active-low"></div>
                <div class="sev-dot ${d.severity === 'medium' || d.severity === 'high' ? 'active-med' : ''}"></div>
                <div class="sev-dot ${d.severity === 'high' ? 'active-high' : ''}"></div>
              </div>
              <span>${d.severity}</span>
            </div>
            <div class="card-link">
              Details 
              <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </div>
          </div>
        </div>
      `}).join('');
    }

    function filterDiseases() {
      const search = document.getElementById('search-input').value.toLowerCase();
      const status = document.getElementById('status-filter').value;
      const severity = document.getElementById('severity-filter').value;

      let filtered = diseases;

      if (search) {
        filtered = filtered.filter(d => 
          d.crop.toLowerCase().includes(search) || 
          d.disease.toLowerCase().includes(search)
        );
      }

      if (currentCropTab) {
        filtered = filtered.filter(d => d.crop === currentCropTab);
      }

      if (status === 'healthy') {
        filtered = filtered.filter(d => d.healthy);
      } else if (status === 'diseased') {
        filtered = filtered.filter(d => !d.healthy);
      }

      if (severity) {
        filtered = filtered.filter(d => d.severity === severity);
      }

      renderDiseases(filtered);
    }

    function showDisease(cropName, diseaseName) {
      const d = diseases.find(x => x.crop === cropName && x.disease === diseaseName);
      if (!d) return;

      document.getElementById('modal-thumb-bg').style.background = d.thumbGradient;
      document.getElementById('modal-thumb-emoji').textContent = d.emoji;
      
      document.getElementById('modal-crop').textContent = `${d.emoji} ${d.crop}`;
      document.getElementById('modal-disease-name').textContent = d.disease;
      
      const statusEl = document.getElementById('modal-status');
      statusEl.className = `badge ${d.healthy ? 'badge-green' : 'badge-red'}`;
      statusEl.textContent = d.healthy ? 'Healthy' : 'Diseased';
      
      document.getElementById('modal-description').textContent = d.desc;
      
      const sevLabel = document.getElementById('modal-severity-label');
      sevLabel.textContent = d.severity.charAt(0).toUpperCase() + d.severity.slice(1);
      sevLabel.style.color = d.severity === 'high' ? 'var(--red)' : d.severity === 'medium' ? 'var(--yellow)' : 'var(--green-primary)';
      document.getElementById('modal-severity-bar').className = `sev-bar-fill ${d.severity}`;
      
      document.getElementById('modal-spreads-via').textContent = d.spread;
      
      const symList = document.getElementById('modal-symptoms');
      symList.innerHTML = d.symptoms.map(s => `<li>${s}</li>`).join('');
      
      const trList = document.getElementById('modal-treatment');
      trList.innerHTML = d.treatment.map(t => `<li>${t}</li>`).join('');
      
      Modal.show('disease-modal');
    }

    // Event listeners
    document.getElementById('search-input').addEventListener('input', filterDiseases);
    document.getElementById('status-filter').addEventListener('change', filterDiseases);
    document.getElementById('severity-filter').addEventListener('change', filterDiseases);

    // Initial render
    renderTabs();
    renderDiseases(diseases);
  </script>
</body>
</html>"""

with open('library.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Created new library.html")
