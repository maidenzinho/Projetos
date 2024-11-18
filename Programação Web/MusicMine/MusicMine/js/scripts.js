document.getElementById('login-form')?.addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('api/users.php?action=login', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    if (data.status === 'success') {
        window.location.href = 'index.php';
    } else {
        alert(data.message);
    }
});

document.getElementById('register-form')?.addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('api/users.php', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    if (data.status === 'success') {
        alert('User registered successfully!');
        window.location.href = 'login.php';
    }
});

document.getElementById('add-music-form')?.addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('api/songs.php', {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    if (data.status === 'success') {
        alert('Music added successfully!');
        this.reset();
    }
});

async function fetchSongs() {
    const response = await fetch('api/songs.php');
    const songs = await response.json();
    const songList = document.getElementById('music-list');
    songList.innerHTML = '';
    songs.forEach(song => {
        const songItem = document.createElement('div');
        songItem.innerHTML = `<h3>${song.title}</h3><p>${song.artist}</p><iframe src="${song.youtube_url}" width="300" height="200" frameborder="0" allowfullscreen></iframe>`;
        songList.appendChild(songItem);
    });
}

fetchSongs();
