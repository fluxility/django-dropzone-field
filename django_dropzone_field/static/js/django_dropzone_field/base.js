(function ($) {
    $.fn.dropzone = function (options) {
        return this.each(function () {
            return new Dropzone(this, options);
        });
    };


    $(function () {
        $(".dropzone-field").each(function () {
            var el = $(this),
                csrf_token = el.parents("form").find("input[name=csrfmiddlewaretoken]").val(),
                input_field = el.prev(),
                earlier_upload = el.find(".dz-earlier-upload"),
                clickable = el.find("button")[0];

            $(this).dropzone({
                "clickable": clickable,
                "url": "/temporary-upload/",
                "maxFiles": 1,
                "params": {
                    "csrfmiddlewaretoken": csrf_token
                },

                /**
                 * On adding new file, remove old ones
                 * @param file
                 */
                onAddedFile: function(file) {
                    for( var i=0; i<this.files.length - 1; i++ ) {
                        var file = this.files[i];
                        this.removeFile(file);
                    }

                    earlier_upload.remove();
                },

                /**
                 * Update file reference
                 * @param file
                 */
                onComplete: function(file) {
                    var file_reference = file.xhr.response;
                    input_field.val(file_reference);
                },

                init: function() {
                    this.on("addedfile", this.options.onAddedFile);
                    this.on("complete", this.options.onComplete);
                }

            });
        });
    })
})(django.jQuery);