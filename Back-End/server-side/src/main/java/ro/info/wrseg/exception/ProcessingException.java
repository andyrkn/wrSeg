package ro.info.wrseg.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(value = HttpStatus.BAD_REQUEST, reason = "Processing error")
public class ProcessingException extends RuntimeException {
    public ProcessingException() {
        this("Processing error");
    }

    public ProcessingException(String fileName) {
        super("Processing error - " + fileName);
    }
}