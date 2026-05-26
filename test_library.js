const fs = require('fs');
const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const html = fs.readFileSync('library.html', 'utf8');
const base_css = fs.readFileSync('static/css/base.css', 'utf8');
const pages_css = fs.readFileSync('static/css/pages.css', 'utf8');
const utils_js = fs.readFileSync('static/js/utils.js', 'utf8');

const dom = new JSDOM(html, { runScripts: "dangerously" });
const window = dom.window;
const document = window.document;

// Simulate utils.js
const scriptEl = document.createElement('script');
scriptEl.textContent = utils_js;
document.head.appendChild(scriptEl);

window.onload = () => {
    try {
        console.log("Testing showDisease...");
        window.showDisease('Apple', 'Apple Scab');
        const modal = document.getElementById('disease-modal');
        console.log("Modal classes:", modal.className);
    } catch (e) {
        console.error("Error:", e);
    }
};
