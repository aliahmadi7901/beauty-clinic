function comment(comment_id) {
    $("#parent").val(comment_id)
    document.getElementById("comment_form").scrollIntoView({behavior: 'smooth'})
}
