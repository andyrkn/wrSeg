package ro.info.wrseg.service;

import org.springframework.web.multipart.MultipartFile;
import ro.info.wrseg.model.FileUpload;

public interface FileStorageService {
    FileUpload save(MultipartFile content);
}
