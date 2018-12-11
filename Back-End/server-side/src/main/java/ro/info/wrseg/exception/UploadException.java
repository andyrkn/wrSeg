package ro.info.wrseg.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.BAD_REQUEST, reason = "Error in uploading image")
public class UploadException extends RuntimeException {
    public UploadException() {
        this("Error in uploading image");
    }

    public UploadException(String fileName) {
        super("Could not upload file with name " + fileName);
    }
}