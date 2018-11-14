package ro.info.wrseg.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.BAD_REQUEST, reason = "Invalid file extension")
public class InvalidFileExtensionException extends RuntimeException {
    public InvalidFileExtensionException() {
        this("Invalid file extension");
    }

    public InvalidFileExtensionException(String fileName) {
        super("Invalid file extension when uploading file " + fileName);
    }
}