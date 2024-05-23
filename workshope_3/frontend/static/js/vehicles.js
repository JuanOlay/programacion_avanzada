function loadeEngines() {
    return fetch('http://localhost:8080/view_vehicles')
        .then(response => response.json())
        .then(data => {
            console.log('Loaded vehicles:', data);
            return data;
        })
        .catch(error => {
            console.error('Error fetching vehicles:', error);
            return [];
        });
}
