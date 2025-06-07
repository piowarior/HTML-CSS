document.addEventListener("DOMContentLoaded", function () {
    let currentIndex = 0;
    const images = document.querySelectorAll(".slider img");
    const totalImages = images.length;
    
    function changeImage() {
        images.forEach((img, index) => {
            img.style.opacity = index === currentIndex ? "1" : "0";
        });
        currentIndex = (currentIndex + 1) % totalImages;
    }
    
    setInterval(changeImage, 3000);
});
