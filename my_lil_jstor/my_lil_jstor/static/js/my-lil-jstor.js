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
});
