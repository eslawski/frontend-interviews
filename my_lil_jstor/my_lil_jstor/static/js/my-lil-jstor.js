// Please include or add javascript to this file
import $ from "jquery";

// Array that keeps track of all the book a user has already liked this "session"
let likedBooks = [];

$( document ).ready(function() {

    /**
     * Function that is called when the like button is clicked for a coloring book.
     * An ajax request is made to the server to process the like. If successful, update
     * the UI to reflect the new like.
     * @param bookId
     */
    window.likeClicked = function(bookId) {
        if(likedBooks.indexOf(bookId) !== -1) {
            return; // Do not let the user like a book more than once
        }

        ajaxWithMask({
            url: 'like',
            type: 'post',
            data: {
                bookId: bookId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            onSuccess: function(data) {
                let likeButton = $(".like-button");
                likeButton.removeClass("fa-heart-o");
                likeButton.addClass("fa-heart");
                $(".like-count").html(data.likes);
                likedBooks.push(bookId)
            },
            onError: function(data) {
                alert('Unable to process like');
            }
        });
    };

    /**
     * Adds a comment obtained from the server to the comments section.
     * TODO: Instead of loading comments in the original page request for coloring book details
     * TODO: maybe consider loading the comments in a separate ajax request after the fact.
     * TODO: That way the comments can can be added all in one place (instead of in both javascript
     * TODO: and html) This would make implementing the 'star rating' component much easier as it can
     * TODO: be created and maintained in javascript.
     */
    function addComment(response) {
        let comment = response.comment;
        let media = $("<div>", {"class": "media comment"});
        let mediaBody = $("<div>", {"class": "media-body"});
        let h5 = $("<h5>", {"class": "mt-0"});

        mediaBody.append(h5.append(comment.user)).append(comment.comment);
        media.append(mediaBody);
        $(".comments-section").prepend(media);
        $('#comment-text-field').val("");
        $('#user-text-field').val("");
    }

    /**
     * Handles the submission of the comments form for a coloring book. If the
     * comment post was successful then add it to the comments section of the
     * currently displayed book.
     */
    $('#comment-form').submit(function() { // catch the form's submit event
        ajaxWithMask({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            onSuccess: addComment,
            onError: function(response) {
                alert("Unable to add comment");
            }
        });
        return false;
    });

    /**
     * Makes an ajax request while also masking the screen to prevent user interaction
     * @param ajaxRequest Object that contains various pieces of information for how to
     *          fulfill the ajax request.
     */
    function ajaxWithMask(ajaxRequest) {
        let mask = $('<div>', {"class": "modal-mask"});
        $("body").append(mask);
        $.ajax({
            data: ajaxRequest.data,
            type: ajaxRequest.type,
            url: ajaxRequest.url,
            success: function(response) {
                mask.remove();
                ajaxRequest.onSuccess(response);
            },
            error: function(response) {
                mask.remove();
                ajaxRequest.onError(response)
            }
        });
    }
});
