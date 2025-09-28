console.log('Loading api-requests.js');
const apiRoot = '/api/v1/';

async function showArtisans() {
    const response = await fetch(apiRoot + 'artisans/');
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    // console.log(response);

    const artisans = await response.json()
    // console.log(artisans);

    const newRows = [];
    for (const artisan of artisans) {
        const activeIcon = artisan.is_active ? '<i class="bi bi-check-square-fill"></i>': '<i class="bi bi-square"></i>';
        const deletedIcon = artisan.is_deleted ? '<i class="bi bi-check-square-fill"></i>': '<i class="bi bi-square"></i>';
        const address = artisan.business_address.city;
        // console.log(address);
        const newMarkup = `<tr>
    <td title="oid: ${artisan.oid}">${artisan.given_name} ${artisan.family_name}</td>
    <td>${address}</td>
    <td>${activeIcon}</td>
    <td>${activeIcon}</td>
    <td>
        <button class="btn btn-sm btn-primary" onClick="showArtisan('${artisan.oid}')">
            Show
        </button>
        <button class="btn btn-sm btn-secondary" onClick="editArtisan('${artisan.oid}')">
            Edit
        </button>
    </td>
</tr>`;
        newRows.push(newMarkup);
    }
    tbody = document.getElementById('artisan-items');
    tbody.innerHTML = '';
    for (const row of newRows) {
        tbody.innerHTML += row;
    }
}

window.onload = () => {showArtisans();showPanel('artisan-post');};

function showPanel(panelId) {
    const createButton = document.getElementById('create-button');

    for (panel of ['artisan-get', 'artisan-post', 'artisan-patch']){
        const panelElement = document.getElementById(panel);
        if(panel === panelId){
            panelElement.style.display = 'block';
        }
        else{
            panelElement.style.display = 'none';
        }
    }

    if(panelId === 'artisan-post') {
        createButton.style.display = 'none';
    }
    else {
        createButton.style.display = 'block';
    }
}

async function showArtisan(oid) {
    // console.log('showArtisan("' + oid + '") called');
    const response = await fetch(apiRoot + 'artisans/' + oid + '/');
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }
    // console.log(response);

    const artisans = await response.json();
    const artisan = artisans[0];
    // console.log(artisan);
    // console.log(Object.entries(artisan));

    for(const[key, value] of Object.entries(artisan)) {
        const targetElement = document.getElementById('artisan-' + key);
        // console.log('${key}: ${value}');
        if(targetElement){
            targetElement.innerHTML = '<code>None</code> / <code>null</code>';
            if(value){
                targetElement.innerHTML = value;
            }
        }
    }

    for(const[key, value] of Object.entries(artisan.business_address)) {
        const targetElement = document.getElementById('artisan-business_address-' +key);
        if(targetElement){
            targetElement.innerHTML = '<code>None</code> / <code>null</code>';
            if(value){
                targetElement.innerHTML = value;
            }
        }
    }

    showPanel('artisan-get');
}

async function editArtisan(oid) {
    // console.log('editArtisan("' + oid + '") called');
    const response = await fetch(apiRoot + 'artisans/' + oid + '/');
    if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
    }

    const artisans = await response.json();
    const artisan = artisans[0];
    // console.log(artisan);
    const targetForm = document.querySelector('#artisan-patch');
    // console.log(targetForm);

    for(const[key, value] of Object.entries(artisan)) {
        const targetField = document.getElementById('edit-artisan.' + key)
        if(targetField) {
            targetField.value = value;
        }
    }

    for(const[key, value] of Object.entries(artisan.business_address)) {
        const targetField = document.getElementById('edit-artisan.business_address.' + key)
        if(targetField) {
            targetField.value = value;
        }
    }

    showPanel('artisan-patch');
}

function getFormData(form) {
    const targetForm = document.querySelector(form);
    const formData = new FormData(targetForm);
    return Object.fromEntries(formData.entries());
}

function createArtisanSubmit(form) {
    const formData = getFormData(form);
    const payload = {
        artisan: {
            business_address: {},
        },
    };
    for (const [key, value] of Object.entries(formData)) {
        if(key.startsWith('artisan.business_address')){
            addressKey =
            payload.artisan.business_address[key.slice(25)] = value;
        }
        else if(key.startsWith('artisan.')){
            payload.artisan[key.slice(8)] = value;
        }
    }
    // console.dir(payload);
    apiPost('artisans/', payload.artisan);
}

async function editArtisanSubmit(form) {
    const formData = getFormData(form);
    const payload = {
        artisan: {
            business_address: {},
        },
    };
    for (const [key, value] of Object.entries(formData)) {
        if(key.startsWith('artisan.business_address.')){
            payload.artisan.business_address[key.slice(25)] = value;
        }
        else if(key.startsWith('artisan.')){
            payload.artisan[key.slice(8)] = value;
        }
    }
    console.dir(payload);
    apiPatch('artisans/' + formData.oid, payload.artisan);
    showArtisan(formData.oid);

}

// GET request
function apiGet(path){
    fetch(apiRoot + path)
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // console.log('Data received:', data);
    })
    .catch(error => {
        // console.error('Error fetching data:', error);
    });
}

// POST request
function apiPost(path, data){
    fetch(apiRoot + path, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
    .then(data => {
        // console.log('Data sent successfully:', data);
      })
    .catch(error => {
        // console.error('Error sending data:', error);
      });}

// PATCH request
function apiPatch(path, data){
    // console.log('apiPatch called');
    // console.log(path);
    // console.log(data);
    fetch(apiRoot + path, {
        method: 'PATCH',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
    .then(data => {
        // console.log('Data sent successfully:', data);
      })
    .catch(error => {
        // console.error('Error sending data:', error);
      });}

console.log('Loaded api-requests.js');
