// create all functionality for the navbar

function showNotice(title, notice) {
    const noticeContainer = document.getElementById('notice-container')
    const noticeTitle = document.getElementById('notice-title')
    const noticeContent = document.getElementById('notice-content')
    const closeButton = document.querySelector('.notice-close')
    noticeContainer.style.display = 'flex'
    noticeTitle.innerText = title
    noticeContent.innerText = notice
    closeButton.addEventListener('click', () => {
        noticeContainer.style.display = 'none'
    })
}
const title = 'Noticia de último momento.'
const notice = 'Llegaron trotadoras nuevas con un tremendo progrma que tiene la capacidad de preparar una maraton en tres meses.'
showNotice(title, notice)
