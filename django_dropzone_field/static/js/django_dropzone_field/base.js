(function ($) {
    $.fn.dropzone = function (options) {
        return this.each(function () {
            return new Dropzone(this, options);
        });
    };


    $(function () {
        $(".dropzone-field").each(function () {
            var el = $(this),
                csrf_token = el.parents("form").find("input[name=csrfmiddlewaretoken]").val();

            $(this).dropzone({
                "clickable": "button",
                "url": "/temporary-upload/",
                "maxFiles": 1,
                "params": {
                    "csrfmiddlewaretoken": csrf_token
                },

                onAddedFile: function(file) {
                    for( var i=0; i<this.files.length - 1; i++ ) {
                        var file = this.files[i];
                        this.removeFile(file);
                    }
                },

                init: function() {
                    this.on("addedfile", this.options.onAddedFile);
                }

            });
        });
    })
})(django.jQuery);