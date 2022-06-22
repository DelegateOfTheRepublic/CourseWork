function find(e){
    if (e.keyCode == 13){
        itemName = e.target.value.trim();
        itemsList = document.querySelector('#itemsList');
        itemsListChildren = itemsList.children
        for (let id = 0; id < itemsListChildren.length; id++){
            item = itemsListChildren[id]
            if (item.querySelector('p').innerText != itemName){
                item.style.display = 'none';
            }
        }
        e.preventDefault();
    }
    else if (e.button == 0){
        itemName = e.target.parentNode.querySelector('#search').value.trim();
        itemsList = document.querySelector('#itemsList');
        itemsListChildren = itemsList.children
        for (let id = 0; id < itemsListChildren.length; id++){
            item = itemsListChildren[id]
            if (item.querySelector('p').innerText != itemName){
                item.style.display = 'none';
            }
        }
        e.preventDefault();
    }
}

function clearSearch(e){
    e.target.parentNode.querySelector('#search').value = "";
    itemsList = document.querySelector('#itemsList');
    itemsListChildren = itemsList.children
    for (let id = 0; id < itemsListChildren.length; id++){
        item = itemsListChildren[id]
        if (item.style.display === 'none'){
            item.style.display = '';
        }
    }
}