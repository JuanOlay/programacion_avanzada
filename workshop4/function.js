async function callMessage() {
    try {
        // se agrego el puerto donde corre el backend
        const response = await fetch('http://localhost:3702/hello_ud');
        const data = await response.text();
        document.getElementById('result').textContent = data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// se cambio el nombre de la funcion para que cuadre con el html
async function callTable() {
    try {
        // se agrego el puerto donde corre el backend y se puso una raiz que si exista
        const response = await fetch('http://localhost:3702/get_products');
        const data = await response.json();
        
        let table = '<table>';
        table += '<tr><th>ID</th><th>Name</th><th>Description</th></tr>';
        
        data.forEach(item => {
            table += `<tr><td>${item.id}</td><td>${item.name}</td><td>${item.description}</td></tr>`;
        });
        
        table += '</table>';
        
        document.getElementById('result').innerHTML = table;
    } catch (error) {
        console.error('Error:', error);
    }
}