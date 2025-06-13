function Watch(name){
    if(name!='Not GameId'){
        path = `https://www.song27.com/iframe/ch.php?ch=${name}`
        document.getElementById('responsive-iframe').setAttribute('src',path)
    }
}

function adjustIframeHeight() {
    const iframe = document.getElementById('responsive-iframe');
    const aspectRatio = 16 / 9;
    const width = iframe.offsetWidth;
    const height = width / aspectRatio;
    iframe.style.height = height + 'px';
}

window.addEventListener('load', adjustIframeHeight);
window.addEventListener('resize', adjustIframeHeight);
