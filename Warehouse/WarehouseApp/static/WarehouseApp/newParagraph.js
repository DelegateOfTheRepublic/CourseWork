function addNewParagraph(e){
    newItem = document.querySelector('#newItem')
    if (newItem != null){
        goodName = newItem.querySelector('#placeForGood').innerText
        goodAmount = newItem.querySelector('#needAmount').value
        if (goodName != 'Товар не выбран' && (!isNaN(Number(goodAmount)) && goodAmount != '')){
            if (newItem.querySelector('#maxAmount') != null){
                if (Number(goodAmount) <= Number(newItem.querySelector('#maxAmount').innerText.split('/')[1])){
                    items = document.querySelector('#items')
                    fieldset = document.createElement('fieldset')
                    legend = document.createElement('legend')
                    label = document.createElement('label')
                    input = document.createElement('input')
                    placeForGood = document.createElement('input')
                    span = document.createElement('span')
        
                    fieldset.setAttribute('id', 'newItem')
                    fieldset.setAttribute('class', "border-2 color_b4 rounded-lg p-1 h-fit")
                    fieldset.setAttribute('title', "Для добавления, нажмите на любой товар из соотв. списка выше")
        
                    placeForGood.setAttribute('type', "text")
                    placeForGood.setAttribute('id', "placeForGood")
                    placeForGood.setAttribute('name', "None")
                    placeForGood.setAttribute('class', 'outline-none')
                    placeForGood.setAttribute('style', 'width: 100%')
                    placeForGood.setAttribute('readonly', 'readonly')
                    placeForGood.value = "Товар не выбран"
        
                    span.setAttribute('id', 'maxAmount')
                    span.innerText = '/'
        
                    label.setAttribute('for', "needAmount")
                    label.innerText = "Необходимое количество:"
                    
                    newItem.querySelector('#needAmount').style.color = 'black'
                    input.setAttribute('id', "needAmount")
                    input.setAttribute('class', "h-fit w-12 outline-none")
                    input.setAttribute('type', "text")
                    input.setAttribute('placeholder', "enter")
                    input.setAttribute('onkeypress', 'removeError(event)')
                    input.setAttribute('onblur', "removeError(event)")
        
                    legend.append(placeForGood)
                    fieldset.append(legend)
                    fieldset.append(label)
                    fieldset.append(input)
                    fieldset.append(span)
        
                    items.append(fieldset)
                    newItem.removeAttribute('id')
                }
                else{
                    newItem.querySelector('#needAmount').style.color = 'red'
                }
            }else{
                items = document.querySelector('#items')
                fieldset = document.createElement('fieldset')
                legend = document.createElement('legend')
                label = document.createElement('label')
                input = document.createElement('input')
                placeForGood = document.createElement('input')
    
                fieldset.setAttribute('id', 'newItem')
                fieldset.setAttribute('class', "border-2 color_b4 rounded-lg p-1 h-fit")
                fieldset.setAttribute('title', "Для добавления, нажмите на любой товар из соотв. списка выше")
    
                placeForGood.setAttribute('type', "text")
                placeForGood.setAttribute('id', "placeForGood")
                placeForGood.setAttribute('name', "None")
                placeForGood.setAttribute('class', 'outline-none')
                placeForGood.setAttribute('style', 'width: 100%')
                placeForGood.setAttribute('readonly', 'readonly')
                placeForGood.value = "Товар не выбран"
    
                label.setAttribute('for', "needAmount")
                label.innerText = "Необходимое количество:"
                
                input.setAttribute('id', "needAmount")
                input.setAttribute('class', "h-fit w-12 outline-none")
                input.setAttribute('type', "text")
                input.setAttribute('placeholder', "enter")
    
                legend.append(placeForGood)
                fieldset.append(legend)
                fieldset.append(label)
                fieldset.append(input)
    
                items.append(fieldset)
                newItem.removeAttribute('id')
            }
        }
    }
}

function removeError(event){
    needAmountInput = event.target
    if (needAmountInput.parentNode.querySelector('#maxAmount').innerText.split('/').length != 0){
        maxAmount = Number(needAmountInput.parentNode.querySelector('#maxAmount').innerText.split('/')[1])
        needAmount = Number(needAmountInput.value)

        if (needAmount > maxAmount){
            needAmountInput.style.color = 'red'
        }
        else{
            needAmountInput.style.color = 'black'
        }
    }
    else{
        needAmountInput.style.color = 'red'
    }
}