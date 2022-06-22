function addGood(e, maxAmount){
    newItem = document.querySelector('#newItem')
    newItem.querySelector('#placeForGood').value = e.target.innerText
    newItem.querySelector('#placeForGood').setAttribute('value', e.target.innerText)
    newItem.querySelector('#needAmount').setAttribute('name', 'id_' + e.target.getAttribute('id'))
    newItem.querySelector('#placeForGood').setAttribute('name', 'id_' + e.target.getAttribute('id'))
    newItem.querySelector('#maxAmount').innerText = '/' + maxAmount
}