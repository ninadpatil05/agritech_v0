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
            n.matches?.('[data-i18n],[data-i18n-placeholder],[data-i18n-title],[data-i18n-aria]') ||
            n.querySelector?.('[data-i18n],[data-i18n-placeholder],[data-i18n-title],[data-i18n-aria]')
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
