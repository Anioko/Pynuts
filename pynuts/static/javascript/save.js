function hashCode(string) {
    var hash = 0;
    if (string.length == 0) return hash;
    for (i = 0; i < string.length; i++) {
        char = string.charCodeAt(i);
        hash = ((hash<<5)-hash)+char;
        hash = hash & hash; // Convert to 32bit integer
    }
    return hash;
}

function save (options) {
    //Params : document, message, author, author_email, ok_callback, error_callback, empty_callback
    options.document = options.document ? options.document : $(document);
    
    // Get all the contenteditable elements
    divs = $(options.document).contents().find('div[contenteditable]');
    span_containers = $(options.document).contents().find('span[contenteditable]');
    
    if (divs.length != 0 && span_containers.length != 0) {
        alert('You have no contenteditable on your document.');
        return false;
    }
    
    var data = [];
    if (divs.length != 0) {
        $.each(divs, function () {
            if($(this).attr('data-hash') != hashCode($(this).html())) {
                data.push({
                    "part": $(this).attr('data-part'),
                    "document_type": $(this).attr('data-document-type'),
                    "document_id": $(this).attr('data-document-id'),
                    "version": $(this).attr('data-document-version'),
                    "content": $(this).html()
                });
            }
            $(this).attr('data-hash', hashCode($(this).html()));
        });
    }
    if (span_containers.length != 0) {
        $.each(span_containers, function () {
            var spans = $(this).find('span[contenteditable]');
            var values = [];
            $.each(spans, function () {
                values.push($(this).html());
            });
            data.push({
                "part": $(this).attr('data-part'),
                "document_type": $(this).attr('data-document-type'),
                "document_id": $(this).attr('data-document-id'),
                "version": $(this).attr('data-document-version'),
                "content": JSON.stringify(values)
            });
        });
    }

    // Check if contents is null
    if (data.length == 0) {
        if (options.unchange_callback) options.unchange_callback();
        return false;
    }

    // Get commit options
    commit_message = options.message ? options.message : null;
    commit_author = options.author ? options.author : null;
    commit_author_email = options.author_email ? options.author_email : null;
    // Make ajax
    $.ajax({
        url: '/_pynuts/update_content',
        data: JSON.stringify({
            'data': data,
            'message': commit_message,
            'author': commit_author,
            'author_email': commit_author_email
        }),
        contentType: 'application/json',
        dataType: 'json',
        type: "POST",
        success: function(response){
            if(response && response.documents) {
                $.each(response.documents, function () {
                    var divs = options.document.contents().find(
                        'div[contenteditable]' +
                        '[data-document-type="' + this.document_type + '"]' +
                        '[data-document-id="' + this.document_id + '"]'
                    );
                    divs.attr('data-document-version', this.version);
                });
                if (options.success_callback) options.success_callback();
            } else {
                if (options.fail_callback) options.fail_callback();
            }
        }
    });
}