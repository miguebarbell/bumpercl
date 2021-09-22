// carousel functionality.
console.log('loaded script for carousel.')
const track = document.querySelector('.carousel-track')
const slides = Array.from(track.children)
const nextButton = document.getElementById('next-btn')
console.log(nextButton)
const prevButton = document.getElementById('prev-btn')

for (let i = 0; i < slides.length; i++) {
    slides[i].id = i;

}
let currentImageId = slides.length - 1
nextButton.addEventListener('click', nextImage)
prevButton.addEventListener('click', prevImage)
function nextImage() {
    if (slides.length === 1) {
        return
    }
    if (currentImageId == `${slides.length - 1}`) {
        // console.log('going to the first element.')
        document.getElementById(`${currentImageId}`).style.display = 'none'
        currentImageId = 0
        document.getElementById(currentImageId).style.display = 'flex'
    } else {
        document.getElementById(`${currentImageId + 1}`).style.display = 'flex';
        document.getElementById(`${currentImageId}`).style.display = 'none';
    }
    // console.log('next image')
}
function prevImage() {
    if (slides.length === 1) {
        return
    }
    if (currentImageId === 0) {
        // console.log('going to the last element.')
        currentImageId = slides.length - 1;
        document.getElementById(`${currentImageId}`).style.display = 'flex';
        document.getElementById('0').style.display = 'none'
    } else {
        document.getElementById(`${currentImageId-1}`).style.display = 'flex';
        document.getElementById(`${currentImageId}`).style.display = 'none';
    }
    // console.log('prev image')
}