function loadeEngines() {
    return fetch('http://localhost:8080/view_engines')
        .then(response => response.json())
        .then(data => {
            console.log('Loaded engines:', data);
            return data;
        })
        .catch(error => {
            console.error('Error fetching events:', error);
            return [];
        });
}
