function val(){
        var a = document.getElementById('fn').value
        var b = document.getElementById('sn').value
        sum = parseInt(a) + parseInt(b)
        sub = parseInt(a) - parseInt(b)
        mul = parseInt(a) * parseInt(b)
        div = parseInt(a) / parseInt(b)
        document.getElementById("result").innerText='Addition is '+sum + '\n' + 'Substraction is '+sub +'\n'+'Multiplication is '+ mul +'\n'+ 'Division is '+ div
        //alert('Addition is '+sum + '\n' + 'Substraction is '+sub +'\n'+'Multiplication is '+ mul +'\n'+ 'Division is '+ div)
}

