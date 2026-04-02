// Persist the sidebar scroll position across page navigations.
// div.sphinxsidebar is the fixed overflow:auto container in Alabaster.
(function () {
    var KEY = "sphinxSidebarScrollTop";

    function getSidebar() {
        return document.querySelector("div.sphinxsidebar");
    }

    // Restore saved position after the browser has finished its own layout/scroll.
    window.addEventListener("load", function () {
        var saved = sessionStorage.getItem(KEY);
        if (saved === null) return;
        // Two nested rAFs: first lets the browser apply its own scroll restoration,
        // second runs after layout is fully painted so our value wins.
        requestAnimationFrame(function () {
            requestAnimationFrame(function () {
                var sidebar = getSidebar();
                if (sidebar) sidebar.scrollTop = parseInt(saved, 10);
            });
        });
    });

    // Save position before leaving the page.
    window.addEventListener("pagehide", function () {
        var sidebar = getSidebar();
        if (sidebar) sessionStorage.setItem(KEY, sidebar.scrollTop);
    });
})();
