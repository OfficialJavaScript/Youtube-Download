document.addEventListener('DOMContentLoaded', function() {
    const progressBar = document.querySelector('.progress-bar');
    const previewContainer = document.getElementById('preview-container');
    const previewImage = document.getElementById('preview-image');
    
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const videoUrl = document.getElementById('video_url').value;
        progressBar.style.width = '0%';
        previewContainer.style.display = 'none';

        fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ video_url: videoUrl }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                previewImage.src = data.thumbnail_url;
                previewContainer.style.display = 'block';
            }
        });
    });
});
