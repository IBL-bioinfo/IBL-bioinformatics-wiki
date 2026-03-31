// Ensure anchor targets near the bottom of a page can scroll to the viewport top.
// Dynamically adds only the minimum bottom padding needed, then scrolls.
(function () {
    function scrollToHash() {
        var hash = window.location.hash;
        if (!hash) return;
        var id;
        try { id = decodeURIComponent(hash.slice(1)); } catch (e) { return; }
        var target = document.getElementById(id);
        if (!target) return;
        var body = document.querySelector("div.body") || document.body;
        // Reset any previously added padding
        body.style.paddingBottom = "";
        // Use rAF to ensure layout is recalculated without padding
        requestAnimationFrame(function () {
            var targetTop = target.getBoundingClientRect().top + window.pageYOffset;
            var docHeight = Math.max(
                document.body.scrollHeight,
                document.documentElement.scrollHeight
            );
            var needed = targetTop + window.innerHeight - docHeight;
            if (needed > 0) {
                body.style.paddingBottom = needed + "px";
            }
            // Second rAF to ensure padding has taken effect before scrolling
            requestAnimationFrame(function () {
                window.scrollTo(0, target.getBoundingClientRect().top + window.pageYOffset);
            });
        });
    }

    window.addEventListener("hashchange", scrollToHash);
    window.addEventListener("load", function () {
        if (window.location.hash) {
            // Delay to run after the browser's native scroll-to-hash
            setTimeout(scrollToHash, 50);
        }
    });
})();
