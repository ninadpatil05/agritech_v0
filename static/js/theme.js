/**
 * Theme Manager — Smart Crop Detective
 * Runs synchronously in <head> to prevent flash of wrong theme.
 */
(function () {
    'use strict';

    var KEY = 'theme'; // same key used by profile preferences
    var HTML = document.documentElement;

    function resolve() {
        var saved = localStorage.getItem(KEY);
        if (saved === 'dark' || saved === 'light') return saved;
        // 'system' or null → follow OS
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }

    function apply(theme) {
        if (theme === 'system') {
            // Clear override, follow OS
            localStorage.setItem(KEY, 'system');
            theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        } else {
            localStorage.setItem(KEY, theme);
        }
        HTML.setAttribute('data-theme', theme);
        _syncBtns(theme);
    }

    function toggle() {
        var next = (HTML.getAttribute('data-theme') || 'light') === 'dark' ? 'light' : 'dark';
        apply(next);
        return next;
    }

    function _syncBtns(theme) {
        var btns = document.querySelectorAll('[data-theme-toggle]');
        for (var i = 0; i < btns.length; i++) {
            var icon = btns[i].querySelector('.tt-icon');
            if (icon) icon.textContent = theme === 'dark' ? '☀️' : '🌙';
            btns[i].title = theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
        }
    }

    // ── Apply immediately (before first paint) ─────────────────
    apply(resolve());

    // ── React to OS-level changes ───────────────────────────────
    try {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function (e) {
            if (localStorage.getItem(KEY) === 'system' || !localStorage.getItem(KEY)) {
                HTML.setAttribute('data-theme', e.matches ? 'dark' : 'light');
                _syncBtns(e.matches ? 'dark' : 'light');
            }
        });
    } catch (_) {}

    // ── Re-sync buttons after DOM is ready (nav may not exist yet) ──
    function syncWhenReady() {
        _syncBtns(HTML.getAttribute('data-theme') || 'light');
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', syncWhenReady);
    } else {
        syncWhenReady();
    }

    // ── Public API ──────────────────────────────────────────────
    window.ThemeManager = {
        toggle: toggle,
        apply: apply,
        current: function () { return HTML.getAttribute('data-theme') || 'light'; },
        syncBtns: function () { _syncBtns(HTML.getAttribute('data-theme') || 'light'); }
    };
})();
