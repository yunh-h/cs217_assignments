document.addEventListener('DOMContentLoaded', function() {
    const addCommentButton = document.getElementById('add-comment-button');
    const commentForm = document.getElementById('comment-form');

    if (addCommentButton && commentForm) {
        addCommentButton.addEventListener('click', function() {
            if (commentForm.style.display === 'none' || commentForm.style.display === '') {
                commentForm.style.display = 'block';
            } else {
                commentForm.style.display = 'none';
            }
        });
    }
});