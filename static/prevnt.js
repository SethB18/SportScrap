// Detect Developer Tools Open State
let devToolsOpen = false;

function detectDevTools() {
    const element = new Image();
    Object.defineProperty(element, 'id', {
        get: function () {
            devToolsOpen = true;
            setTimeout(() => {
                devToolsOpen = false;
                window.location.href = 'about:black'; // Redirect when tools are closed
            }, 100); // Redirect after dev tools are detected
        }
    });

    console.log('%c ', element);
}

// Run Detection
setInterval(detectDevTools, 500);

// Disable Right-Click
document.addEventListener('contextmenu', function (e) {
    e.preventDefault();
});

// Disable Common Key Combinations
document.addEventListener('keydown', function (e) {
    if (e.key === 'F12' || e.keyCode === 123 || (e.ctrlKey && e.shiftKey && ['I', 'J', 'C'].includes(e.key)) || (e.ctrlKey && e.key === 'U')) {
        e.preventDefault();
    }
});
