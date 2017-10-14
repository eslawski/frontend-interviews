// Please include or add javascript to this file
import $ from "jquery";

// Array that keeps track of all the book a user has already liked this "session"
let likedBooks = [];

$( document ).ready(function() {
    window.likeClicked = function(bookId) {

        if(likedBooks.indexOf(bookId) !== -1) {
            return; // Do not let the user like a book more than once
        }

        $.ajax({
            url: 'like',
            type: 'post',
            data: {
                bookId: bookId,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(data) {
                let likeButton = $(".like-button");
                likeButton.removeClass("fa-heart-o");
                likeButton.addClass("fa-heart");
                $(".like-count").html(data.likes);
                likedBooks.push(bookId)
            },
            failure: function(data) {
                alert('Got an error');
            }
        });
    };

    $('#comment-form').submit(function() { // catch the form's submit event
        $.ajax({ // create an AJAX call...
            data: $(this).serialize(), // get the form data
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function(response) { // on success..
                let comment = response.comment;
                let media = $("<div>", {"class": "media comment"});
                let mediaBody = $("<div>", {"class": "media-body"});
                let h5 = $("<h5>", {"class": "mt-0"});

                mediaBody.append(h5.append(comment.user)).append(comment.comment);
                media.append(mediaBody);
                $(".comments-section").prepend(media);
                $('#comment-text-field').val("");
                $('#user-text-field').val("");
            },
            error: function(e, x, r) { // on error..

            }
        });
        return false;
    });
});
