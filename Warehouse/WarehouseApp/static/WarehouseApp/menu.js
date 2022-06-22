function showMenu(event){
    if (event.target.tagName === 'P'){
        parent = event.target.parentNode.parentNode
        if (parent.classList.contains('active')){
            parent.classList.remove('active')
        }
        else{
            parent.classList.add('active')
        }
    }
    else{
        parent = event.target.parentNode
        if (parent.classList.contains('active')){
            parent.classList.remove('active')
        }
        else{
            parent.classList.add('active')
        }
    }
}