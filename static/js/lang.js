// ─── Smart Crop Detective · Multilingual Support ──────────────────────────────
// Locales: en (English), hi (Hindi), mr (Marathi)
// Storage key: 'lang'  ← single source of truth, never use 'language'
// ──────────────────────────────────────────────────────────────────────────────

const TRANSLATIONS = {
  en: {
    // ── Navigation ──────────────────────────────────────────────────────────
    nav_home:           'Home',
    nav_detect:         'Detect',
    nav_weather:        'Weather',
    nav_library:        'Library',
    nav_reports:        'Reports',
    nav_profile:        'Profile',
    nav_about:          'About',
    nav_contact:        'Contact',
    nav_login:          'Login',
    nav_signup:         'Sign Up',
    nav_logout:         'Logout',
    nav_toggle_theme:   'Toggle Theme',
    nav_dashboard:      'Dashboard',

    // ── Dashboard ───────────────────────────────────────────────────────────
    dash_greeting:      'Welcome back',
    dash_subtitle:      "Here's your real-time farm telemetry overview",
    dash_quick_scan:    'Quick Scan',
    dash_view_reports:  'View Reports',
    dash_disease_lib:   'Disease Library',
    dash_healthy_crops: 'Healthy Crops',
    dash_diseased_crops:'Diseased Crops',
    dash_vitality_index:'Vitality Telemetry Index',
    dash_optimal:       'Optimal',
    dash_critical:      'Critical',
    dash_moderate:      'Moderate',
    dash_use_location:  'Use My Location',
    dash_recent_scans:  'Recent Scans',
    dash_col_crop:      'Crop',
    dash_col_disease:   'Disease',
    dash_col_date:      'Date',
    dash_col_status:    'Status',
    dash_healthy:       'Healthy',
    dash_diseased:      'Diseased',
    dash_no_scans:      'No scans yet. Upload a leaf photo to get started.',
    dash_total_scans:   'Total Scans',
    dash_diseases_found:'Diseases Found',
    dash_avg_confidence:'Avg Confidence',
    dash_this_week_scans:'This Week Scans',
    dash_vitality_dist: 'Vitality Distribution',
    dash_loading_loc:   'Loading location...',
    dash_no_scans_title:'No Scans Yet',
    dash_no_scans_desc: 'Run your first scan to see your farm health metrics.',
    dash_scans_suffix:  'scans',
    dash_cases_suffix:  'cases',
    dash_no_scans_label:'No Scans',
    dash_excellent:     'Excellent',
    dash_needs_care:    'Needs Care',
    dash_confidence:    'Confidence',
    dash_view_report:   'View full report',
    dash_advisory_tag:  'Agri-Advisory Telemetry',
    dash_loading_tips:  'Loading agricultural advisory tips...',

    reports_title:              'Scan History',
    reports_export:             'Export',
    reports_clear_all:          'Clear All',
    reports_fleet_health:       'Fleet Health Score',
    reports_disease_breakdown:  'Disease Breakdown',
    reports_heatmap_title:      'Scan Frequency Heatmap',
    reports_from:               'From',
    reports_to:                 'To',
    reports_search_disease:     'Search Disease',
    reports_no_history_title:   'Your field journal is empty',
    reports_no_history_desc:    'Every scan you run appears here as a data point. Start building your crop health record.',
    reports_btn_first_scan:     'Run Your First Scan',
    reports_showing_of:         'Showing {showing} of {total} scans',
    reports_delete_title:       'Delete this scan?',
    reports_delete_desc:        'This action cannot be undone.',
    reports_clear_title:        'Clear all history?',
    reports_clear_desc:         'This will permanently delete all your scan history. This action cannot be undone.',
    reports_btn_delete:         'Delete',
    reports_btn_clear:          'Clear All',
    reports_btn_cancel:         'Cancel',
    reports_print:              'Print Report',
    reports_diseased_detections:'Diseased Detections',
    day_mon:                    'Mon',
    day_wed:                    'Wed',
    day_fri:                    'Fri',
    day_sun:                    'Sun',
    reports_less:               'Less',
    reports_more:               'More',
    reports_insight_label:      'Smart Insight',
    reports_all_crops:          'All Crops',
    reports_all_status:         'All',
    reports_search_ph:          'Search disease name...',
    btn_prev:                   'Previous',
    btn_next:                   'Next',

    // ── Detect ──────────────────────────────────────────────────────────────
    detect_title:       'Detect Crop Disease',
    detect_upload:      'Upload a leaf photo',
    detect_analyzing:   'Analyzing with AI...',
    detect_btn_analyze: 'Analyze',
    detect_btn_reset:   'Reset',
    detect_result:      'Detection Result',
    detect_treatment:   'Treatment Steps',
    detect_prevention:  'Prevention Tips',
    detect_confidence:  'Confidence',

    detect_opt_upload:    'Upload Photo',
    detect_opt_camera:    'Take Photo',
    detect_camera_title:  'Use your camera',
    detect_camera_desc:   'Point at the affected leaf and tap capture',
    detect_camera_btn:    'Open Camera',
    detect_camera_hint:   'Opens rear camera on mobile · Works on any phone',

    // ── Auth ────────────────────────────────────────────────────────────────
    auth_welcome_back:  'Welcome back 👋',
    auth_create_acct:   'Create your account',
    auth_email:         'Email',
    auth_password:      'Password',
    auth_first_name:    'First Name',
    auth_last_name:     'Last Name',
    auth_btn_login:     'Login →',
    auth_btn_signup:    'Create Account →',
    auth_forgot_pw:     'Forgot password?',
    auth_no_account:    "Don't have an account?",
    auth_have_account:  'Already have an account?',
    auth_or:            'or',
    auth_ph_email:      'Enter your email',
    auth_ph_password:   'Enter your password',
    auth_ph_firstname:  'First name',
    auth_ph_lastname:   'Last name',

    // ── Profile / Preferences ───────────────────────────────────────────────
    pref_language:      'Language',
    pref_language_desc: 'Interface language',
    pref_theme:         'Theme',
    pref_theme_desc:    'Light or dark interface',
    pref_units:         'Units',
    pref_units_desc:    'Temperature & distance',
    btn_save:           'Save Changes',
    btn_cancel:         'Cancel',

    // ── Library ─────────────────────────────────────────────────────────────
    lib_title:          'Disease Library',
    lib_search_ph:      'Search disease or crop…',

    // ── Weather ─────────────────────────────────────────────────────────────
    weather_title:      'Weather Advisory',
    weather_use_loc:    'Use My Location',

    // ── Toasts / Runtime messages ────────────────────────────────────────────
    toast_lang_saved:   'Language updated',
    toast_theme_saved:  'Theme updated',
    toast_units_saved:  'Units preference saved',
    toast_profile_ok:   'Profile updated successfully!',
    toast_pw_ok:        'Password updated successfully!',
    toast_scan_deleted: 'Scan deleted',
    toast_history_cleared: 'All history cleared',
    toast_csv_ok:       'CSV exported successfully',
    toast_json_ok:      'JSON exported successfully',
    toast_location_ok:  'Weather updated for your location!',
    toast_location_denied: 'Location access denied. Using default city Pune.',
    toast_no_geo:       'Geolocation not supported',
    toast_no_data:      'No data to export',
    toast_no_history:   'No history to clear',
    toast_network_err:  'Network error. Please try again.',
    toast_generic_err:  'Something went wrong. Please try again.',
    toast_acct_created: 'Account created successfully! Please log in.',
    toast_file_size:    'File size must be less than 10MB',
    toast_file_type:    'Please upload a JPEG or PNG image',

    // ── Greeting (time-of-day) ────────────────────────────────────────────────
    greeting_morning:   'Good morning',
    greeting_afternoon: 'Good afternoon',
    greeting_evening:   'Good evening',

    // ── Generic ──────────────────────────────────────────────────────────────
    loading:            'Loading…',

    // ── Security Questions (auth.html signup + forgot-password flow) ─────────────
    security_question_label:    'Security Question',
    security_answer_label:      'Security Answer',
    security_answer_placeholder:'Enter your answer',
    err_select_question:        'Please select a security question',
    q_pet:                      'What was the name of your first pet?',
    q_school:                   'What primary school did you attend?',
    q_city:                     'In which city were you born?',
    q_mother:                   "What is your mother's maiden name?",
    q_teacher:                  'Who was your favourite high school teacher?',
    q_crop:                     'What was the first crop you ever harvested?',

    // ── Forgot Password / Reset Flow ─────────────────────────────────────────────
    forgot_password_title:      'Reset Your Password',
    forgot_step_1_desc:         'Enter your registered email address and we will retrieve your security question.',
    forgot_step_2_desc:         'Answer your security question to verify your identity.',
    forgot_step_3_desc:         'Create a new strong password for your account.',
    forgot_btn_get_question:    'Get Security Question →',
    forgot_btn_verify_answer:   'Verify Answer →',
    forgot_btn_reset:           'Reset Password →',
    forgot_back_to_login:       '← Back to Login',
    reset_new_pw_label:         'New Password',
    reset_confirm_pw_label:     'Confirm Password',
    reset_confirm_ph:           'Confirm your password',
    reset_new_pw_ph:            'Create a new password',
    toast_pw_mismatch:          'Passwords do not match',
    toast_pw_short:             'Password must be at least 8 characters',
    toast_forgot_invalid:       'Incorrect answer. Please try again.',
    toast_forgot_sent:          'Security question retrieved successfully.',
    toast_reset_ok:             'Password reset successfully! Please log in.',
    err_email_required:         'Email is required',
    err_answer_required:        'Please enter your answer',

    // ── Landing Page (index.html) ─────────────────────────────────────────────────
    hero_pill:                  '🌿 AI-Powered Crop Health',
    hero_title_line1:           'Detect Crop Disease',
    hero_title_line2:           'in Seconds',
    hero_title_highlight:       'with AI',
    hero_subtitle:              'Upload a leaf photo and get instant AI diagnosis + treatment advice in English, Hindi, and Marathi. Protect your harvest before it\'s too late.',
    hero_cta_scan:              '🔬 Scan Your Crop',
    hero_cta_how:               'See How It Works ↓',
    hero_trust_free:            'Free',
    hero_trust_noapp:           'No app download',
    hero_trust_anyphone:        'Works on any phone',
    stats_diseases:             'Diseases Detected',
    stats_accuracy:             'Accuracy Rate',
    stats_lang_support:         'Language Support',
    stats_lang_value:           'EN + हिंदी + मराठी',
    features_section_title:     'Everything you need to protect your crops',
    features_section_desc:      'Comprehensive tools powered by AI to help Indian farmers detect diseases early and take action.',
    feature_detect_title:       'AI Disease Detection',
    feature_detect_desc:        'Identifies 38+ crop diseases from a single photo using advanced Gemini Vision AI.',
    feature_detect_link:        'Start scanning →',
    feature_weather_title:      'Weather Advisory',
    feature_weather_desc:       'Irrigation, crop planning, and alerts based on live weather data for your location.',
    feature_weather_link:       'Check weather →',
    feature_lang_title:         'Trilingual Support',
    feature_lang_desc:          'Treatment advice in English, Hindi, and Marathi for farmers across India.',
    feature_lang_link:          'Learn more →',
    feature_history_title:      'Scan History',
    feature_history_desc:       'Track all detections and monitor crop health over time with detailed reports.',
    feature_history_link:       'View reports →',
    how_title:                  'Simple. Fast. Accurate.',
    how_desc:                   'Get crop disease diagnosis in three easy steps.',
    step1_title:                'Upload Photo',
    step1_desc:                 'Take a photo of the affected leaf and upload it',
    step2_title:                'AI Analyzes',
    step2_desc:                 'Gemini Vision AI examines 38+ diseases instantly',
    step3_title:                'Get Treatment',
    step3_desc:                 'Step-by-step treatment + prevention in your language',
    crops_title:                'Supports 14+ crops',
    cta_banner_title:           'Start protecting your crops today — it\'s free',
    cta_banner_btn:             '🔬 Get Started Free →',
    footer_tagline:             'AI-powered crop health for every farmer',
    footer_rights:              '© 2025 Smart Crop Detective',
    footer_made:                'Made with ❤️ for Indian Farmers',

    // ── About Page (about.html) ───────────────────────────────────────────────────
    about_hero_title:           'About Smart Crop Detective',
    about_hero_desc:            'Empowering Indian farmers with AI-powered crop health monitoring. Detect diseases early, get treatment advice in your language, protect your harvest.',
    about_mission_title:        'Our Mission',
    about_problem_label:        'The Problem:',
    about_problem_desc:         'Crop diseases cause billions of dollars in losses annually for Indian farmers. Early detection is crucial, but most farmers lack access to expert diagnosis, leading to crop failure and economic hardship.',
    about_solution_label:       'Our Solution:',
    about_solution_desc:        'Smart Crop Detective uses advanced AI technology to bring instant disease diagnosis to every farmer\'s fingertips. Simply upload a photo of an affected leaf, and our system identifies the disease within seconds.',
    about_impact_label:         'The Impact:',
    about_impact_desc:          'By providing early detection and actionable treatment advice in English, Hindi, and Marathi, we help farmers save their crops, reduce losses, and increase yields.',
    about_tech_title:           'Built with Modern AI',
    about_tech_desc:            'Leveraging cutting-edge technology to deliver accurate and fast results.',
    about_dev_title:            'Meet the Developer',
    about_cta_title:            'Ready to protect your crops?',
    about_cta_btn:              '🔬 Start Scanning Now →',

    // ── Contact Page (contact.html) ───────────────────────────────────────────────
    contact_page_title:         'Get in Touch',
    contact_page_desc:          'Have questions about Smart Crop Detective? Want to report an issue or suggest a feature? We\'d love to hear from you!',
    contact_label_email:        'Email',
    contact_label_location:     'Location',
    contact_label_response:     'Response Time',
    contact_response_val:       'Within 24 hours',
    contact_name_label:         'Name',
    contact_name_ph:            'Your name',
    contact_email_ph:           'Your email address',
    contact_subject_label:      'Subject',
    contact_subject_ph:         'What is this about?',
    contact_message_label:      'Message',
    contact_message_ph:         'Tell us more...',
    contact_btn_send:           'Send Message',
    contact_success_title:      'Message Sent! 🎉',
    contact_success_desc:       'Thank you for reaching out. We\'ll get back to you within 24 hours.',
  },

  hi: {
    nav_home:           'लॉगिन', // Wait, prompt says: nav_home: 'होम', let me make sure I match prompt perfectly!
    nav_home:           'होम',
    nav_detect:         'पहचान',
    nav_weather:        'मौसम',
    nav_library:        'लाइब्रेरी',
    nav_reports:        'रिपोर्ट',
    nav_profile:        'प्रोफ़ाइल',
    nav_about:          'हमारे बारे में',
    nav_contact:        'संपर्क',
    nav_login:          'लॉगिन',
    nav_signup:         'साइन अप',
    nav_logout:         'लॉगआउट',
    nav_toggle_theme:   'थीम बदलें',
    nav_dashboard:      'डैशबोर्ड',

    dash_greeting:      'वापस स्वागत है',
    dash_subtitle:      'आपकी रियल-टाइम फार्म टेलीमेट्री ओवरव्यू',
    dash_quick_scan:    'त्वरित स्कैन',
    dash_view_reports:  'रिपोर्ट देखें',
    dash_disease_lib:   'रोग लाइब्रेरी',
    dash_healthy_crops: 'स्वस्थ फसलें',
    dash_diseased_crops:'रोगग्रस्त फसलें',
    dash_vitality_index:'जीवन शक्ति सूचकांक',
    dash_optimal:       'सर्वोत्तम',
    dash_critical:      'गंभीर',
    dash_moderate:      'मध्यम',
    dash_use_location:  'मेरा स्थान उपयोग करें',
    dash_recent_scans:  'हाल के स्कैन',
    dash_col_crop:      'फसल',
    dash_col_disease:   'रोग',
    dash_col_date:      'तारीख',
    dash_col_status:    'स्थिति',
    dash_healthy:       'स्वस्थ',
    dash_diseased:      'रोगग्रस्त',
    dash_no_scans:      'अभी तक कोई स्कैन नहीं। शुरू करने के लिए पत्ती की फोटो अपलोड करें।',
    dash_total_scans:   'कुल स्कैन',
    dash_diseases_found:'पाए गए रोग',
    dash_avg_confidence:'औसत विश्वास',
    dash_this_week_scans:'इस सप्ताह के स्कैन',
    dash_vitality_dist: 'जीवन शक्ति वितरण',
    dash_loading_loc:   'स्थान लोड हो रहा है...',
    dash_no_scans_title:'अभी तक कोई स्कैन नहीं',
    dash_no_scans_desc: 'अपने खेत के स्वास्थ्य मेट्रिक्स देखने के लिए अपना पहला स्कैन चलाएं।',
    dash_scans_suffix:  'स्कैन',
    dash_cases_suffix:  'मामले',
    dash_no_scans_label:'कोई स्कैन नहीं',
    dash_excellent:     'उत्कृष्ट',
    dash_needs_care:    'देखभाल की आवश्यकता',
    dash_confidence:    'विश्वास',
    dash_view_report:   'पूरी रिपोर्ट देखें',
    dash_advisory_tag:  'कृषि-सलाह टेलीमेट्री',
    dash_loading_tips:  'कृषि सलाहकार युक्तियाँ लोड हो रही हैं...',

    reports_title:              'स्कैन इतिहास',
    reports_export:             'एक्सपोर्ट',
    reports_clear_all:          'सभी हटाएं',
    reports_fleet_health:       'बेड़े का स्वास्थ्य स्कोर',
    reports_disease_breakdown:  'रोग वर्गीकरण',
    reports_heatmap_title:      'स्कैन आवृत्ति हीटमैप',
    reports_from:               'से',
    reports_to:                 'तक',
    reports_search_disease:     'रोग खोजें',
    reports_no_history_title:   'आपका फील्ड जर्नल खाली है',
    reports_no_history_desc:    'आपके द्वारा चलाया जाने वाला प्रत्येक स्कैन यहां एक डेटा बिंदु के रूप में दिखाई देता है। अपना फसल स्वास्थ्य रिकॉर्ड बनाना शुरू करें।',
    reports_btn_first_scan:     'अपना पहला स्कैन चलाएं',
    reports_showing_of:         '{total} स्कैन में से {showing} दिखा रहा है',
    reports_delete_title:       'इस स्कैन को हटाएं?',
    reports_delete_desc:        'यह कार्रवाई पूर्ववत नहीं की जा सकती।',
    reports_clear_title:        'सारा इतिहास साफ़ करें?',
    reports_clear_desc:         'यह आपके सभी स्कैन इतिहास को स्थायी रूप से हटा देगा। यह कार्रवाई पूर्ववत नहीं की जा सकती।',
    reports_btn_delete:         'हटाएं',
    reports_btn_clear:          'साफ़ करें',
    reports_btn_cancel:         'रद्द करें',
    reports_print:              'रिपोर्ट प्रिंट करें',
    reports_diseased_detections:'रोगग्रस्त पहचान',
    day_mon:                    'सोम',
    day_wed:                    'बुध',
    day_fri:                    'शुक्र',
    day_sun:                    'रवि',
    reports_less:               'कम',
    reports_more:               'अधिक',
    reports_insight_label:      'स्मार्ट अंतर्दृष्टि',
    reports_all_crops:          'सभी फसलें',
    reports_all_status:         'सभी',
    reports_search_ph:          'रोग का नाम खोजें...',
    btn_prev:                   'पिछला',
    btn_next:                   'अगला',

    detect_title:       'फसल रोग की पहचान करें',
    detect_upload:      'पत्ती की फोटो अपलोड करें',
    detect_analyzing:   'AI से विश्लेषण हो रहा है...',
    detect_btn_analyze: 'विश्लेषण करें',
    detect_btn_reset:   'रीसेट',
    detect_result:      'पहचान परिणाम',
    detect_treatment:   'उपचार के चरण',
    detect_prevention:  'रोकथाम के उपाय',
    detect_confidence:  'विश्वास',

    detect_opt_upload:    'फोटो अपलोड करें',
    detect_opt_camera:    'फोटो लें',
    detect_camera_title:  'कैमरा उपयोग करें',
    detect_camera_desc:   'प्रभावित पत्ती पर कैमरा लगाएं',
    detect_camera_btn:    'कैमरा खोलें',
    detect_camera_hint:   'मोबाइल पर रियर कैमरा खुलेगा',

    auth_welcome_back:  'वापस स्वागत है 👋',
    auth_create_acct:   'अपना खाता बनाएं',
    auth_email:         'ईमेल',
    auth_password:      'पासवर्ड',
    auth_first_name:    'पहला नाम',
    auth_last_name:     'अंतिम नाम',
    auth_btn_login:     'लॉगिन →',
    auth_btn_signup:    'खाता बनाएं →',
    auth_forgot_pw:     'पासवर्ड भूल गए?',
    auth_no_account:    'खाता नहीं है?',
    auth_have_account:  'पहले से खाता है?',
    auth_or:            'या',
    auth_ph_email:      'अपना ईमेल दर्ज करें',
    auth_ph_password:   'अपना पासवर्ड दर्ज करें',
    auth_ph_firstname:  'पहला नाम',
    auth_ph_lastname:   'अंतिम नाम',

    pref_language:      'भाषा',
    pref_language_desc: 'इंटरफ़ेस भाषा',
    pref_theme:         'थीम',
    pref_theme_desc:    'लाइट या डार्क इंटरफ़ेस',
    pref_units:         'इकाइयाँ',
    pref_units_desc:    'तापमान और दूरी',
    btn_save:           'परिवर्तन सहेजें',
    btn_cancel:         'रद्द करें',

    lib_title:          'रोग लाइब्रेरी',
    lib_search_ph:      'रोग या फसल खोजें…',

    weather_title:      'मौसम सलाह',
    weather_use_loc:    'मेरा स्थान उपयोग करें',

    toast_lang_saved:   'भाषा अपडेट की गई',
    toast_theme_saved:  'थीम अपडेट की गई',
    toast_units_saved:  'इकाई प्राथमिकता सहेजी गई',
    toast_profile_ok:   'प्रोफ़ाइल सफलतापूर्वक अपडेट की गई!',
    toast_pw_ok:        'पासवर्ड सफलतापूर्वक अपडेट किया गया!',
    toast_scan_deleted: 'स्कैन हटाया गया',
    toast_history_cleared: 'सारा इतिहास हटाया गया',
    toast_csv_ok:       'CSV सफलतापूर्वक एक्सपोर्ट किया गया',
    toast_json_ok:      'JSON सफलतापूर्वक एक्सपोर्ट किया गया',
    toast_location_ok:  'आपके स्थान के लिए मौसम अपडेट किया गया!',
    toast_location_denied: 'स्थान एक्सेस अस्वीकृत। डिफ़ॉल्ट शहर पुणे उपयोग हो रहा है।',
    toast_no_geo:       'जियोलोकेशन समर्थित नहीं है',
    toast_no_data:      'एक्सपोर्ट के लिए कोई डेटा नहीं',
    toast_no_history:   'हटाने के लिए कोई इतिहास नहीं',
    toast_network_err:  'नेटवर्क त्रुटि। कृपया पुनः प्रयास करें।',
    toast_generic_err:  'कुछ गलत हुआ। कृपया पुनः प्रयास करें।',
    toast_acct_created: 'खाता सफलतापूर्वक बनाया गया! कृपया लॉगिन करें।',
    toast_file_size:    'फ़ाइल का आकार 10MB से कम होना चाहिए',
    toast_file_type:    'कृपया JPEG या PNG इमेज अपलोड करें',

    greeting_morning:   'सुप्रभात',
    greeting_afternoon: 'नमस्ते',
    greeting_evening:   'शुभ संध्या',

    loading:            'लोड हो रहा है…',

    // ── Security Questions ─────────────
    security_question_label:    'सुरक्षा प्रश्न',
    security_answer_label:      'सुरक्षा उत्तर',
    security_answer_placeholder:'अपना उत्तर दर्ज करें',
    err_select_question:        'कृपया एक सुरक्षा प्रश्न चुनें',
    q_pet:                      'आपके पहले पालतू जानवर का नाम क्या था?',
    q_school:                   'आपने किस प्राथमिक विद्यालय में पढ़ाई की?',
    q_city:                     'आपका जन्म किस शहर में हुआ था?',
    q_mother:                   'आपकी माँ का मायके का नाम क्या है?',
    q_teacher:                  'आपके पसंदीदा हाई स्कूल शिक्षक कौन थे?',
    q_crop:                     'आपने पहली बार कौन सी फसल काटी थी?',

    forgot_password_title:      'पासवर्ड रीसेट करें',
    forgot_step_1_desc:         'अपना पंजीकृत ईमेल पता दर्ज करें और हम आपका सुरक्षा प्रश्न प्राप्त करेंगे।',
    forgot_step_2_desc:         'अपनी पहचान सत्यापित करने के लिए अपने सुरक्षा प्रश्न का उत्तर दें।',
    forgot_step_3_desc:         'अपने खाते के लिए एक नया मजबूत पासवर्ड बनाएं।',
    forgot_btn_get_question:    'सुरक्षा प्रश्न प्राप्त करें →',
    forgot_btn_verify_answer:   'उत्तर सत्यापित करें →',
    forgot_btn_reset:           'पासवर्ड रीसेट करें →',
    forgot_back_to_login:       '← लॉगिन पर वापस जाएं',
    reset_new_pw_label:         'नया पासवर्ड',
    reset_confirm_pw_label:     'पासवर्ड की पुष्टि करें',
    reset_confirm_ph:           'अपना पासवर्ड पुष्टि करें',
    reset_new_pw_ph:            'नया पासवर्ड बनाएं',
    toast_pw_mismatch:          'पासवर्ड मेल नहीं खाते',
    toast_pw_short:             'पासवर्ड कम से कम 8 अक्षरों का होना चाहिए',
    toast_forgot_invalid:       'गलत उत्तर। कृपया पुनः प्रयास करें।',
    toast_forgot_sent:          'सुरक्षा प्रश्न सफलतापूर्वक प्राप्त किया गया।',
    toast_reset_ok:             'पासवर्ड सफलतापूर्वक रीसेट हो गया! कृपया लॉगिन करें।',
    err_email_required:         'ईमेल आवश्यक है',
    err_answer_required:        'कृपया अपना उत्तर दर्ज करें',

    hero_pill:                  '🌿 AI-संचालित फसल स्वास्थ्य',
    hero_title_line1:           'फसल रोग की पहचान करें',
    hero_title_line2:           'सेकंडों में',
    hero_title_highlight:       'AI से',
    hero_subtitle:              'पत्ती की फोटो अपलोड करें और तुरंत AI निदान + उपचार सलाह पाएं — हिंदी, मराठी और अंग्रेजी में। अपनी फसल बचाएं।',
    hero_cta_scan:              '🔬 अपनी फसल स्कैन करें',
    hero_cta_how:               'यह कैसे काम करता है ↓',
    hero_trust_free:            'मुफ्त',
    hero_trust_noapp:           'कोई ऐप डाउनलोड नहीं',
    hero_trust_anyphone:        'किसी भी फोन पर काम करता है',
    stats_diseases:             'पहचाने गए रोग',
    stats_accuracy:             'सटीकता दर',
    stats_lang_support:         'भाषा समर्थन',
    stats_lang_value:           'EN + हिंदी + मराठी',
    features_section_title:     'आपकी फसलों की सुरक्षा के लिए सब कुछ',
    features_section_desc:      'भारतीय किसानों को रोगों का जल्दी पता लगाने और कार्रवाई करने में मदद करने के लिए AI द्वारा संचालित व्यापक उपकरण।',
    feature_detect_title:       'AI रोग पहचान',
    feature_detect_desc:        'उन्नत Gemini Vision AI का उपयोग करके एक ही फोटो से 38+ फसल रोगों की पहचान करता है।',
    feature_detect_link:        'स्कैन शुरू करें →',
    feature_weather_title:      'मौसम सलाह',
    feature_weather_desc:       'आपके स्थान के लिए लाइव मौसम डेटा के आधार पर सिंचाई, फसल योजना और अलर्ट।',
    feature_weather_link:       'मौसम देखें →',
    feature_lang_title:         'त्रिभाषी समर्थन',
    feature_lang_desc:          'भारत भर के किसानों के लिए अंग्रेजी, हिंदी और मराठी में उपचार सलाह।',
    feature_lang_link:          'और जानें →',
    feature_history_title:      'स्कैन इतिहास',
    feature_history_desc:       'विस्तृत रिपोर्ट के साथ समय के साथ सभी पहचानों को ट्रैक करें और फसल स्वास्थ्य की निगरानी करें।',
    feature_history_link:       'रिपोर्ट देखें →',
    how_title:                  'सरल। तेज़। सटीक।',
    how_desc:                   'तीन आसान चरणों में फसल रोग निदान पाएं।',
    step1_title:                'फोटो अपलोड करें',
    step1_desc:                 'प्रभावित पत्ती की फोटो लें और अपलोड करें',
    step2_title:                'AI विश्लेषण करता है',
    step2_desc:                 'Gemini Vision AI तुरंत 38+ रोगों की जांच करता है',
    step3_title:                'उपचार पाएं',
    step3_desc:                 'आपकी भाषा में चरण-दर-चरण उपचार + रोकथाम',
    crops_title:                '14+ फसलों को सपोर्ट करता है',
    cta_banner_title:           'आज ही अपनी फसलों की सुरक्षा शुरू करें — यह मुफ्त है',
    cta_banner_btn:             '🔬 मुफ्त में शुरू करें →',
    footer_tagline:             'हर किसान के लिए AI-संचालित फसल स्वास्थ्य',
    footer_rights:              '© 2025 स्मार्ट क्रॉप डिटेक्टिव',
    footer_made:                '❤️ भारतीय किसानों के लिए बनाया गया',

    about_hero_title:           'स्मार्ट क्रॉप डिटेक्टिव के बारे में',
    about_hero_desc:            'AI-संचालित फसल स्वास्थ्य निगरानी के साथ भारतीय किसानों को सशक्त बनाना। रोगों का जल्दी पता लगाएं, अपनी भाषा में उपचार सलाह पाएं, अपनी फसल बचाएं।',
    about_mission_title:        'हमारा मिशन',
    about_problem_label:        'समस्या:',
    about_problem_desc:         'फसल रोग भारतीय किसानों के लिए सालाना अरबों रुपये का नुकसान करते हैं। जल्दी पहचान महत्वपूर्ण है, लेकिन अधिकांश किसानों को विशेषज्ञ निदान तक पहुंच नहीं है।',
    about_solution_label:       'हमारा समाधान:',
    about_solution_desc:        'स्मार्ट क्रॉप डिटेक्टिव हर किसान की उंगलियों पर तत्काल रोग निदान लाने के लिए उन्नत AI तकनीक का उपयोग करता है।',
    about_impact_label:         'प्रभाव:',
    about_impact_desc:          'अंग्रेजी, हिंदी और मराठी में जल्दी पहचान और कार्रवाई योग्य उपचार सलाह प्रदान करके, हम किसानों को अपनी फसलें बचाने में मदद करते हैं।',
    about_tech_title:           'आधुनिक AI से बना',
    about_tech_desc:            'सटीक और तेज़ परिणाम देने के लिए अत्याधुनिक तकनीक का उपयोग।',
    about_dev_title:            'डेवलपर से मिलें',
    about_cta_title:            'अपनी फसलों की सुरक्षा के लिए तैयार हैं?',
    about_cta_btn:              '🔬 अभी स्कैन शुरू करें →',

    contact_page_title:         'संपर्क करें',
    contact_page_desc:          'स्मार्ट क्रॉप डिटेक्टिव के बारे में प्रश्न हैं? कोई समस्या रिपोर्ट करना चाहते हैं या फ़ीचर सुझाव देना चाहते हैं? हम आपसे सुनना चाहते हैं!',
    contact_label_email:        'ईमेल',
    contact_label_location:     'स्थान',
    contact_label_response:     'प्रतिक्रिया समय',
    contact_response_val:       '24 घंटे के भीतर',
    contact_name_label:         'नाम',
    contact_name_ph:            'आपका नाम',
    contact_email_ph:           'आपका ईमेल पता',
    contact_subject_label:      'विषय',
    contact_subject_ph:         'यह किस बारे में है?',
    contact_message_label:      'संदेश',
    contact_message_ph:         'हमें और बताएं...',
    contact_btn_send:           'संदेश भेजें',
    contact_success_title:      'संदेश भेजा गया! 🎉',
    contact_success_desc:       'हमसे संपर्क करने के लिए धन्यवाद। हम 24 घंटे के भीतर आपसे संपर्क करेंगे।',
  },

  mr: {
    nav_home:           'मुख्यपृष्ठ',
    nav_detect:         'ओळख',
    nav_weather:        'हवामान',
    nav_library:        'ग्रंथालय',
    nav_reports:        'अहवाल',
    nav_profile:        'प्रोफाइल',
    nav_about:          'आमच्याबद्दल',
    nav_contact:        'संपर्क',
    nav_login:          'लॉगिन',
    nav_signup:         'नोंदणी',
    nav_logout:         'लॉगआउट',
    nav_toggle_theme:   'थीम बदला',
    nav_dashboard:      'डॅशबोर्ड',

    dash_greeting:      'पुन्हा स्वागत आहे',
    dash_subtitle:      'तुमच्या शेताचे रीअल-टाइम विहंगावलोकन',
    dash_quick_scan:    'जलद स्कॅन',
    dash_view_reports:  'अहवाल पाहा',
    dash_disease_lib:   'रोग ग्रंथालय',
    dash_healthy_crops: 'निरोगी पिके',
    dash_diseased_crops:'रोगग्रस्त पिके',
    dash_vitality_index:'जीवनशक्ती निर्देशांक',
    dash_optimal:       'उत्कृष्ट',
    dash_critical:      'गंभीर',
    dash_moderate:      'मध्यम',
    dash_use_location:  'माझे स्थान वापरा',
    dash_recent_scans:  'अलीकडील स्कॅन',
    dash_col_crop:      'पीक',
    dash_col_disease:   'रोग',
    dash_col_date:      'तारीख',
    dash_col_status:    'स्थिती',
    dash_healthy:       'निरोगी',
    dash_diseased:      'रोगग्रस्त',
    dash_no_scans:      'अजून कोणतेही स्कॅन नाही. सुरू करण्यासाठी पानाचा फोटो अपलोड करा.',
    dash_total_scans:   'एकूण स्कॅन',
    dash_diseases_found:'आढळलेले रोग',
    dash_avg_confidence:'सरासरी विश्वास',
    dash_this_week_scans:'या आठवड्यातील स्कॅन',
    dash_vitality_dist: 'जीवनशक्ती वितरण',
    dash_loading_loc:   'स्थान लोड होत आहे...',
    dash_no_scans_title:'अजून कोणतेही स्कॅन नाही',
    dash_no_scans_desc: 'तुमच्या शेताचे आरोग्य मेट्रिक्स पाहण्यासाठी तुमचा पहिला स्कॅन करा.',
    dash_scans_suffix:  'स्कॅन',
    dash_cases_suffix:  'केसेस',
    dash_no_scans_label:'कोणतेही स्कॅन नाही',
    dash_excellent:     'उत्कृष्ट',
    dash_needs_care:    'काळजी आवश्यक',
    dash_confidence:    'विश्वास',
    dash_view_report:   'पूर्ण अहवाल पाहा',
    dash_advisory_tag:  'कृषी-सल्ला टेलिमेट्री',
    dash_loading_tips:  'कृषी सल्लागार टिप्स लोड होत आहेत...',

          reports_title:              'स्कॅन इतिहास',
          reports_export:             'निर्यात',
          reports_clear_all:          'सर्व हटवा',
          reports_fleet_health:       'ताफ्याचे आरोग्य गुण',
          reports_disease_breakdown:  'रोगांचे वर्गीकरण',
          reports_heatmap_title:      'स्कॅन वारंवारता हीटमॅप',
          reports_from:               'पासून',
          reports_to:                 'पर्यंत',
          reports_search_disease:     'रोग शोधा',
          reports_no_history_title:   'तुमचे field जर्नल रिकामे आहे', // wait, let's use field directly in Marathi: field is written as field or field (फिल्ड/शेत)
          reports_no_history_title:   'तुमचे फील्ड जर्नल रिकामे आहे',
          reports_no_history_desc:    'तुम्ही चालवलेला प्रत्येक स्कॅन इथे डेटा पॉईंट म्हणून दिसतो. तिथे पीक आरोग्य रेकॉर्ड तयार करण्यास सुरुवात करा.',
          reports_btn_first_scan:     'तुमचा पहिला स्कॅन करा',
          reports_showing_of:         '{total} स्कॅन पैकी {showing} दाखवत आहे',
          reports_delete_title:       'हा स्कॅन हटवायचा?',
          reports_delete_desc:        'ही कृती पूर्ववत केली जाऊ शकत नाही.',
          reports_clear_title:        'सर्व इतिहास हटवायचा?',
          reports_clear_desc:         'यामुळे तुमचा सर्व स्कॅन इतिहास कायमचा हटवला जाईल. ही कृती पूर्ववत केली जाऊ शकत नाही.',
          reports_btn_delete:         'हटवा',
          reports_btn_clear:          'सर्व हटवा',
          reports_btn_cancel:         'रद्द करा',
          reports_print:              'अहवाल मुद्रित करा',
          reports_diseased_detections:'रोगग्रस्त ओळखी',
          day_mon:                    'सोम',
          day_wed:                    'बुध',
          day_fri:                    'शुक्र',
          day_sun:                    'रवि',
          reports_less:               'कमी',
          reports_more:               'जास्त',
          reports_insight_label:      'स्मार्ट अंतर्दृष्टी',
          reports_all_crops:          'सर्व पिके',
          reports_all_status:         'सर्व',
          reports_search_ph:          'रोगाचे नाव शोधा...',
          btn_prev:                   'मागील',
          btn_next:                   'पुढील',

    detect_title:       'पीक रोग ओळखा',
    detect_upload:      'पानाचा फोटो अपलोड करा',
    detect_analyzing:   'AI ने विश्लेषण सुरू आहे...',
    detect_btn_analyze: 'विश्लेषण करा',
    detect_btn_reset:   'रीसेट',
    detect_result:      'ओळख परिणाम',
    detect_treatment:   'उपचार पायऱ्या',
    detect_prevention:  'प्रतिबंध टिप्स',
    detect_confidence:  'विश्वास',

    detect_opt_upload:    'फोटो अपलोड करा',
    detect_opt_camera:    'फोटो घ्या',
    detect_camera_title:  'कॅमेरा वापरा',
    detect_camera_desc:   'बाधित पानावर कॅमेरा धरा',
    detect_camera_btn:    'कॅमेरा उघडा',
    detect_camera_hint:   'मोबाईलवर मागील कॅमेरा उघडेल',

    auth_welcome_back:  'पुन्हा स्वागत आहे 👋',
    auth_create_acct:   'तुमचे खाते तयार करा',
    auth_email:         'ईमेल',
    auth_password:      'संकेतशब्द',
    auth_first_name:    'पहिले नाव',
    auth_last_name:     'आडनाव',
    auth_btn_login:     'लॉगिन →',
    auth_btn_signup:    'खाते तयार करा →',
    auth_forgot_pw:     'संकेतशब्द विसरलात?',
    auth_no_account:    'खाते नाही?',
    auth_have_account:  'आधीच खाते आहे?',
    auth_or:            'किंवा',
    auth_ph_email:      'तुमचा ईमेल प्रविष्ट करा',
    auth_ph_password:   'तुमचा संकेतशब्द प्रविष्ट करा',
    auth_ph_firstname:  'पहिले नाव',
    auth_ph_lastname:   'आडनाव',

    pref_language:      'भाषा',
    pref_language_desc: 'Interface भाषा', // wait, prompt says: pref_language_desc: 'इंटरफेस भाषा', let me make sure I match prompt perfectly!
    pref_language_desc: 'इंटरफेस भाषा',
    pref_theme:         'थीम',
    pref_theme_desc:    'लाइट किंवा डार्क इंटरफेस',
    pref_units:         'एकके',
    pref_units_desc:    'तापमान आणि अंतर',
    btn_save:           'बदल जतन करा',
    btn_cancel:         'रद्द करा',

    lib_title:          'रोग ग्रंथालय',
    lib_search_ph:      'रोग किंवा पीक शोधा…',

    weather_title:      'हवामान सल्ला',
    weather_use_loc:    'माझे स्थान वापरा',

    toast_lang_saved:   'भाषा अद्यतनित केली',
    toast_theme_saved:  'थीम अद्यतनित केली',
    toast_units_saved:  'एकक प्राधान्य जतन केले',
    toast_profile_ok:   'प्रोफाइल यशस्वीरित्या अद्यतनित केली!',
    toast_pw_ok:        'संकेतशब्द यशस्वीरित्या अद्यतनित केला!',
    toast_scan_deleted: 'स्कॅन हटवले',
    toast_history_cleared: 'सर्व इतिहास हटवला',
    toast_csv_ok:       'CSV यशस्वीरित्या निर्यात केले',
    toast_json_ok:      'JSON यशस्वीरित्या निर्यात केले',
    toast_location_ok:  'तुमच्या स्थानासाठी हवामान अद्यतनित केले!',
    toast_location_denied: 'स्थान प्रवेश नाकारला. डीफॉल्ट शहर पुणे वापरत आहे.',
    toast_no_geo:       'जियोलोकेशन समर्थित नाही',
    toast_no_data:      'निर्यात करण्यासाठी डेटा नाही',
    toast_no_history:   'हटवण्यासाठी इतिहास नाही',
    toast_network_err:  'नेटवर्क त्रुटी. कृपया पुन्हा प्रयत्न करा.',
    toast_generic_err:  'काहीतरी चुकले. कृपया पुन्हा प्रयत्न करा.',
    toast_acct_created: 'खाते यशस्वीरित्या तयार केले! कृपया लॉगिन करा.',
    toast_file_size:    'फाइलचा आकार 10MB पेक्षा कमी असणे आवश्यक आहे',
    toast_file_type:    'कृपया JPEG किंवा PNG प्रतिमा अपलोड करा',

    greeting_morning:   'सुप्रभात',
    greeting_afternoon: 'नमस्कार',
    greeting_evening:   'शुभ संध्याकाळ',

    loading:            'लोड होत आहे…',

    // ── Security Questions ─────────────
    security_question_label:    'सुरक्षा प्रश्न',
    security_answer_label:      'सुरक्षा उत्तर',
    security_answer_placeholder:'तुमचे उत्तर प्रविष्ट करा',
    err_select_question:        'कृपया एक सुरक्षा प्रश्न निवडा',
    q_pet:                      'तुमच्या पहिल्या पाळीव प्राण्याचे नाव काय होते?',
    q_school:                   'तुम्ही कोणत्या प्राथमिक शाळेत शिकलात?',
    q_city:                     'तुमचा जन्म कोणत्या शहरात झाला?',
    q_mother:                   'तुमच्या आईचे माहेरचे आडनाव काय आहे?',
    q_teacher:                  'तुमचे आवडते हायस्कूल शिक्षक कोण होते?',
    q_crop:                     'तुम्ही पहिल्यांदा कोणते पीक काढले होते?',

    forgot_password_title:      'संकेतशब्द रीसेट करा',
    forgot_step_1_desc:         'तुमचा नोंदणीकृत ईमेल पत्ता प्रविष्ट करा आणि आम्ही तुमचा सुरक्षा प्रश्न मिळवू.',
    forgot_step_2_desc:         'तुमची ओळख सत्यापित करण्यासाठी तुमच्या सुरक्षा प्रश्नाचे उत्तर द्या.',
    forgot_step_3_desc:         'तुमच्या खात्यासाठी नवीन मजबूत संकेतशब्द तयार करा.',
    forgot_btn_get_question:    'सुरक्षा प्रश्न मिळवा →',
    forgot_btn_verify_answer:   'उत्तर सत्यापित करा →',
    forgot_btn_reset:           'संकेतशब्द रीसेट करा →',
    forgot_back_to_login:       '← लॉगिनवर परत जा',
    reset_new_pw_label:         'नवीन संकेतशब्द',
    reset_confirm_pw_label:     'संकेतशब्द पुष्टी करा',
    reset_confirm_ph:           'तुमचा संकेतशब्द पुष्टी करा',
    reset_new_pw_ph:            'नवीन संकेतशब्द तयार करा',
    toast_pw_mismatch:          'संकेतशब्द जुळत नाहीत',
    toast_pw_short:             'संकेतशब्द किमान 8 अक्षरांचा असणे आवश्यक आहे',
    toast_forgot_invalid:       'चुकीचे उत्तर. कृपया पुन्हा प्रयत्न करा.',
    toast_forgot_sent:          'सुरक्षा प्रश्न यशस्वीरित्या मिळवला.',
    toast_reset_ok:             'संकेतशब्द यशस्वीरित्या रीसेट झाला! कृपया लॉगिन करा.',
    err_email_required:         'ईमेल आवश्यक आहे',
    err_answer_required:        'कृपया तुमचे उत्तर प्रविष्ट करा',

    hero_pill:                  '🌿 AI-चालित पीक आरोग्य',
    hero_title_line1:           'पीक रोग ओळखा',
    hero_title_line2:           'सेकंदात',
    hero_title_highlight:       'AI सह',
    hero_subtitle:              'पानाचा फोटो अपलोड करा आणि तात्काळ AI निदान + उपचार सल्ला मिळवा — मराठी, हिंदी आणि इंग्रजीत. तुमची पिके वाचवा.',
    hero_cta_scan:              '🔬 तुमचे पीक स्कॅन करा',
    hero_cta_how:               'हे कसे कार्य करते ↓',
    hero_trust_free:            'मोफत',
    hero_trust_noapp:           'कोणताही ॲप डाउनलोड नाही',
    hero_trust_anyphone:        'कोणत्याही फोनवर कार्य करते',
    stats_diseases:             'ओळखलेले रोग',
    stats_accuracy:             'अचूकता दर',
    stats_lang_support:         'भाषा समर्थन',
    stats_lang_value:           'EN + हिंदी + मराठी',
    features_section_title:     'तुमच्या पिकांच्या संरक्षणासाठी सर्वकाही',
    features_section_desc:      'भारतीय शेतकऱ्यांना रोग लवकर शोधण्यात आणि कार्यवाही करण्यात मदत करण्यासाठी AI द्वारे चालवलेली सर्वसमावेशक साधने.',
    feature_detect_title:       'AI रोग ओळख',
    feature_detect_desc:        'प्रगत Gemini Vision AI वापरून एकाच फोटोतून 38+ पीक रोग ओळखतो.',
    feature_detect_link:        'स्कॅन सुरू करा →',
    feature_weather_title:      'हवामान सल्ला',
    feature_weather_desc:       'तुमच्या स्थानासाठी थेट हवामान डेटावर आधारित सिंचन, पीक नियोजन आणि सूचना.',
    feature_weather_link:       'हवामान तपासा →',
    feature_lang_title:         'त्रिभाषिक समर्थन',
    feature_lang_desc:          'संपूर्ण भारतातील शेतकऱ्यांसाठी मराठी, हिंदी आणि इंग्रजीत उपचार सल्ला.',
    feature_lang_link:          'अधिक जाणून घ्या →',
    feature_history_title:      'स्कॅन इतिहास',
    feature_history_desc:       'सर्व ओळखी ट्रॅक करा आणि तपशीलवार अहवालांसह कालांतराने पीक आरोग्यावर लक्ष ठेवा.',
    feature_history_link:       'अहवाल पाहा →',
    how_title:                  'सोपे. जलद. अचूक.',
    how_desc:                   'तीन सोप्या चरणांमध्ये पीक रोग निदान मिळवा.',
    step1_title:                'फोटो अपलोड करा',
    step1_desc:                 'प्रभावित पानाचा फोटो घ्या आणि अपलोड करा',
    step2_title:                'AI विश्लेषण करते',
    step2_desc:                 'Gemini Vision AI तात्काळ 38+ रोगांची तपासणी करते',
    step3_title:                'उपचार मिळवा',
    step3_desc:                 'तुमच्या भाषेत पायरी-पायरी उपचार + प्रतिबंध',
    crops_title:                '14+ पिकांना समर्थन',
    cta_banner_title:           'आजच तुमच्या पिकांचे संरक्षण सुरू करा — ते मोफत आहे',
    cta_banner_btn:             '🔬 मोफत सुरू करा →',
    footer_tagline:             'प्रत्येक शेतकऱ्यासाठी AI-चालित पीक आरोग्य',
    footer_rights:              '© 2025 स्मार्ट क्रॉप डिटेक्टिव',
    footer_made:                '❤️ भारतीय शेतकऱ्यांसाठी बनवले',

    about_hero_title:           'स्मार्ट क्रॉप डिटेक्टिव बद्दल',
    about_hero_desc:            'AI-चालित पीक आरोग्य निरीक्षणाने भारतीय शेतकऱ्यांना सक्षम करणे. रोग लवकर शोधा, तुमच्या भाषेत उपचार सल्ला मिळवा, तुमचे पीक वाचवा.',
    about_mission_title:        'आमचे ध्येय',
    about_problem_label:        'समस्या:',
    about_problem_desc:         'पीक रोगांमुळे भारतीय शेतकऱ्यांचे दरवर्षी अब्जावधी रुपयांचे नुकसान होते. लवकर ओळख महत्त्वाची आहे, परंतु बहुतांश शेतकऱ्यांना तज्ज्ञ निदानाचा अभाव आहे.',
    about_solution_label:       'आमचे उपाय:',
    about_solution_desc:        'स्मार्ट क्रॉप डिटेक्टिव प्रत्येक शेतकऱ्याच्या बोटांपर्यंत तात्काळ रोग निदान आणण्यासाठी प्रगत AI तंत्रज्ञान वापरतो.',
    about_impact_label:         'परिणाम:',
    about_impact_desc:          'मराठी, हिंदी आणि इंग्रजीत लवकर ओळख आणि कृती करण्यायोग्य उपचार सल्ला देऊन, आम्ही शेतकऱ्यांना त्यांची पिके वाचवण्यास मदत करतो.',
    about_tech_title:           'आधुनिक AI ने बनवले',
    about_tech_desc:            'अचूक आणि जलद निकाल देण्यासाठी अत्याधुनिक तंत्रज्ञानाचा वापर.',
    about_dev_title:            'विकसकाशी भेटा',
    about_cta_title:            'तुमची पिके संरक्षित करण्यासाठी तयार आहात?',
    about_cta_btn:              '🔬 आता स्कॅन सुरू करा →',

    contact_page_title:         'संपर्क साधा',
    contact_page_desc:          'स्मार्ट क्रॉप डिटेक्टिव बद्दल प्रश्न आहेत? समस्या नोंदवायची आहे किंवा फीचर सुचवायचे आहे? आम्हाला तुमच्याकडून ऐकायला आवडेल!',
    contact_label_email:        'ईमेल',
    contact_label_location:     'स्थान',
    contact_label_response:     'प्रतिसाद वेळ',
    contact_response_val:       '24 तासांच्या आत',
    contact_name_label:         'नाव',
    contact_name_ph:            'तुमचे नाव',
    contact_email_ph:           'तुमचा ईमेल पत्ता',
    contact_subject_label:      'विषय',
    contact_subject_ph:         'हे कशाबद्दल आहे?',
    contact_message_label:      'संदेश',
    contact_message_ph:         'आम्हाला अधिक सांगा...',
    contact_btn_send:           'संदेश पाठवा',
    contact_success_title:      'संदेश पाठवला! 🎉',
    contact_success_desc:       'संपर्क केल्याबद्दल धन्यवाद. आम्ही 24 तासांच्या आत तुमच्याशी संपर्क साधू.',
  },
};

// ─── Locale → Intl locale code map ────────────────────────────────────────────
const LOCALE_MAP = { en: 'en-IN', hi: 'hi-IN', mr: 'mr-IN' };

const Lang = {
  STORAGE_KEY: 'lang',
  SUPPORTED:   ['en', 'hi', 'mr'],

  // ── Public API ──────────────────────────────────────────────────────────────

  get() {
    const v = localStorage.getItem(this.STORAGE_KEY);
    return this.SUPPORTED.includes(v) ? v : 'en';
  },

  set(lang) {
    if (!this.SUPPORTED.includes(lang)) lang = 'en';
    localStorage.setItem(this.STORAGE_KEY, lang);
    this._apply(lang);
    this._syncSelects(lang);
    this._updateHtmlLang(lang);
    this._notifyNav(lang);
    window.dispatchEvent(new CustomEvent('langchange', { detail: { lang } }));
  },

  /** Translate a key, with English fallback, then the key itself as last resort. */
  t(key) {
    const lang = this.get();
    return (TRANSLATIONS[lang]?.[key])
        ?? (TRANSLATIONS.en?.[key])
        ?? key;
  },

  /** Return the correct Intl locale string for the active language. */
  locale() {
    return LOCALE_MAP[this.get()] || 'en-IN';
  },

  // ── Internal ────────────────────────────────────────────────────────────────

  _apply(lang) {
    // Text content
    document.querySelectorAll('[data-i18n]').forEach(el => {
      el.textContent = TRANSLATIONS[lang]?.[el.dataset.i18n]
                    ?? TRANSLATIONS.en?.[el.dataset.i18n]
                    ?? el.dataset.i18n;
    });
    // Placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      el.placeholder = TRANSLATIONS[lang]?.[el.dataset.i18nPlaceholder]
                    ?? TRANSLATIONS.en?.[el.dataset.i18nPlaceholder]
                    ?? '';
    });
    // Titles (tooltips)
    document.querySelectorAll('[data-i18n-title]').forEach(el => {
      el.title = TRANSLATIONS[lang]?.[el.dataset.i18nTitle]
              ?? TRANSLATIONS.en?.[el.dataset.i18nTitle]
              ?? '';
    });
    // aria-labels
    document.querySelectorAll('[data-i18n-aria]').forEach(el => {
      el.setAttribute('aria-label',
        TRANSLATIONS[lang]?.[el.dataset.i18nAria]
        ?? TRANSLATIONS.en?.[el.dataset.i18nAria]
        ?? '');
    });

    // Handle data-custom-i18n (textContent — used in auth.html security questions, forgot-password)
    document.querySelectorAll('[data-custom-i18n]').forEach(el => {
      const key = el.dataset.customI18n;
      el.textContent = TRANSLATIONS[lang]?.[key]
                   ?? TRANSLATIONS.en?.[key]
                   ?? el.textContent;
    });

    // Handle data-custom-i18n-placeholder
    document.querySelectorAll('[data-custom-i18n-placeholder]').forEach(el => {
      const key = el.dataset.customI18nPlaceholder;
      el.placeholder = TRANSLATIONS[lang]?.[key]
                    ?? TRANSLATIONS.en?.[key]
                    ?? el.placeholder;
    });

    // Handle <option> elements with data-custom-i18n (preserve value attribute)
    document.querySelectorAll('option[data-custom-i18n]').forEach(el => {
      const key = el.dataset.customI18n;
      el.textContent = TRANSLATIONS[lang]?.[key]
                   ?? TRANSLATIONS.en?.[key]
                   ?? el.textContent;
    });
  },

  _syncSelects(lang) {
    document.querySelectorAll('#langSelect, [data-lang-select]').forEach(sel => {
      sel.value = lang;
    });
    // Old button-toggle pattern in detect.html
    document.querySelectorAll('[data-lang]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
  },

  _updateHtmlLang(lang) {
    document.documentElement.setAttribute('lang', lang);
  },

  _notifyNav(lang) {
    if (window.NavComponent?.setLang) NavComponent.setLang(lang);
  },

  /** Re-translate newly injected DOM nodes automatically. */
  _observe() {
    new MutationObserver(muts => {
      for (const m of muts) {
        for (const n of m.addedNodes) {
          if (n.nodeType === 1 && (
            n.matches?.('[data-i18n],[data-i18n-placeholder],[data-i18n-title],[data-i18n-aria],[data-custom-i18n],[data-custom-i18n-placeholder]') ||
            n.querySelector?.('[data-i18n],[data-i18n-placeholder],[data-i18n-title],[data-i18n-aria],[data-custom-i18n],[data-custom-i18n-placeholder]')
          )) {
            this._apply(this.get());
            return;
          }
        }
      }
    }).observe(document.body, { childList: true, subtree: true });
  },

  /** One-time migration: move old 'language' key → 'lang'. */
  _migrateLegacyKey() {
    const legacy = localStorage.getItem('language');
    if (legacy && !localStorage.getItem(this.STORAGE_KEY)) {
      localStorage.setItem(this.STORAGE_KEY, this.SUPPORTED.includes(legacy) ? legacy : 'en');
    }
    localStorage.removeItem('language'); // clean up regardless
  },

  init() {
    this._migrateLegacyKey();
    // Auto-detect browser language for first-time visitors
    if (!localStorage.getItem(this.STORAGE_KEY)) {
      const browserLang = (navigator.language || navigator.userLanguage || 'en').split('-')[0].toLowerCase();
      const detected = this.SUPPORTED.includes(browserLang) ? browserLang : 'en';
      localStorage.setItem(this.STORAGE_KEY, detected);
    }
    const lang = this.get();
    this._apply(lang);
    this._syncSelects(lang);
    this._updateHtmlLang(lang);
    this._observe();

    // Wire all langSelect dropdowns present at init time
    document.querySelectorAll('#langSelect, [data-lang-select]').forEach(sel => {
      sel.addEventListener('change', e => {
        this.set(e.target.value);
        if (window.Toast) Toast.success(this.t('toast_lang_saved'));
      });
    });

    // Wire old button-toggle pattern (detect.html)
    document.querySelectorAll('.language-toggle button').forEach(btn => {
      btn.addEventListener('click', () => this.set(btn.dataset.lang));
    });
  },
};

window.Lang = Lang;
document.addEventListener('DOMContentLoaded', () => Lang.init());
