const showMenu = (toogleId, navbarId, bodyId) => {
    const toogle = document.getElementById(toogleId)
    navbar = document.getElementById(navbarId)
    bodypadding = document.getElementById(bodyId)

    if (toogle && navbar) {
        toogle.addEventListener('click', () => {
            navbar.classList.toggle('expander')

            bodypadding.classList.toggle('body-pd')
        })
    }

}
showMenu('nav-toggle', 'navbar', 'body-pd')