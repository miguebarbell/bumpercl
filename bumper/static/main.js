function checkNotices() {
    if (document.getElementById('notice-title').innerText === '') {
        console.log('Not notice')
    } else {
        console.log('Notice')
        const noticeContainer = document.getElementById('notice-container')
        // const closeButton = document.querySelector('.notice-close')
        noticeContainer.style.display = 'flex'
        noticeContainer.addEventListener('click', () => {
            noticeContainer.style.display = 'none'
        })
    }
}
checkNotices()

function contactForm() {
    const body = document.querySelector('body')
    let divContactForm = document.createElement('div')
    divContactForm.classList.add('freeze')

}