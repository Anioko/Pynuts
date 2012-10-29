"""Form validators for Pynuts."""
import os
from flask import current_app
from flask.ext.wtf import ValidationError
from flask.ext.uploads import UploadConfiguration, UploadNotAllowed


class AllowedFile(object):
    def __call__(self, form, field):
        """ Check if uploaded file can be saved, according to the rules
            defined by the corresponding UploadSet.

            If no file, raise ValidationError.
            If the file breaks the UploadSet rule, raise UploadNotAllowed.
            Else, save the upload file in a subdirectory named after the
            UploadSet, located in the app instance path.

            Example: a file uploaded via the following UploadField:

            >>> UploadField(label=u'avatar', upload_set=('images', IMAGES), validators=[AllowedFile()])

            will be stored in instance/uploads/images (instance/ being the app instance path).

            raises: ValidationError, UploadNotAllowed
        """
        field.upload_set._config = UploadConfiguration(destination=os.path.join(
            current_app.uploads_default_dest, field.name))
        if not field.has_file():
            raise ValidationError('FileField must not be empty.')
        try:
            field.upload_set.save(field.data)
        except UploadNotAllowed:
            extension = field.data.filename.split('.')[-1]
            field_label = field.label.text
            raise UploadNotAllowed('The %s field does not allow the upload of %s files.' % (
                field_label, extension))


class MaxSize(object):
    """A validator ensuring that uploaded file size is under a specified maximum size.

    :param size: The maximum size to accept, in MB. The default value is 5MB.
    :type size: float, int
    """
    def __init__(self, size=5):
        self.max_size = size

    def __call__(self, form, field):
        """Check if uploaded file is under specified max size."""
        if self.byte_size < self.stream_size(field.data.stream):
            raise UploadNotAllowed(
                'Maximum authorized file size is %.1f MB.' % (self.max_size))

    @property
    def byte_size(self):
        return self.max_size * 1048576

    @staticmethod
    def stream_size(stream):
        """Returns the size (in bytes) of a byte stream.

        :seealso https://groups.google.com/forum/?fromgroups=\
        #!searchin/pocoo-libs/FileStorage/pocoo-libs/n9S53qFqlwo/zwYiBcDwP8gJ
        """
        if hasattr(stream, "getvalue"):
            file_size = len(stream.getvalue())
        else:
            stream.seek(0, 2)
            file_size = stream.tell()
            stream.seek(0)
        return file_size
