// carousel functionality.
console.log('loaded script for carousel.')
const images = document.querySelectorAll('.image-detail')
for (let i = 0; i < images.length; i++) {
    images[i].style.display = 'none'
    images[i].id = i
}
const nextButton = document.getElementById('next-btn')
const prevButton = document.getElementById('prev-btn')

let currentImageId = 0
images[currentImageId].style.display = 'flex'
nextButton.addEventListener('click', nextImage)
prevButton.addEventListener('click', prevImage)
function nextImage() {
    if (images.length === 1) {
        return
    }
    if (currentImageId == `${images.length - 1}`) {
        document.getElementById(`${currentImageId}`).style.display = 'none'
        currentImageId = 0
        document.getElementById(currentImageId).style.display = 'flex'
        // console.log(`current image: ${currentImageId}`)
    } else {
        document.getElementById(`${currentImageId}`).style.display = 'none';
        currentImageId += 1
        document.getElementById(`${currentImageId}`).style.display = 'flex';
        // console.log(`current image: ${currentImageId}`)
    }
}
function prevImage() {
    if (images.length === 1) {
        return
    }
    if (currentImageId === 0) {
        // console.log('first item')
        document.getElementById('0').style.display = 'none'
        currentImageId = images.length - 1;
        document.getElementById(`${currentImageId}`).style.display = 'flex';
        // console.log(`current image: ${currentImageId}`)
    } else {
        document.getElementById(`${currentImageId}`).style.display = 'none';
        currentImageId -= 1
        document.getElementById(`${currentImageId}`).style.display = 'flex';
        // console.log(`current image: ${currentImageId}`)
    }
}