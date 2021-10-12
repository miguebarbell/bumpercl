const body = document.querySelector('body');
function deployCart() {
    console.log('deploy cart')
    // freeze the body
    const freezer = document.createElement('div')
    freezer.classList.add('freezer');
    body.appendChild(freezer)
    const cartDiv = document.createElement('div')
    cartDiv.classList.add('cart-container')

    // add div with element
    // check the qty
    // save it to the internal storage
    // create a close button that put everything to the normality
}