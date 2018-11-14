package ro.info.wrseg.repository;

import org.springframework.stereotype.Component;
import ro.info.wrseg.exception.UploadException;
import ro.info.wrseg.model.FileUpload;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Component("fileRepository")
public class FileRepository {
    private Path fileStorageLocation;

    public FileRepository() {
        // current relative path
        this.fileStorageLocation = Paths.get("./../assets");
        // previous directory
        this.fileStorageLocation = this.fileStorageLocation.getParent();
        // navigating to assets directory
        this.fileStorageLocation = Paths.get(fileStorageLocation.toString(), "assets");
    }

    public FileUpload save(FileUpload fileUpload) {
        try {
            Path targetLocation = this.fileStorageLocation.resolve(fileUpload.getName() + "." + fileUpload.getExtension());
            Files.copy(fileUpload.getMultipartFile().getInputStream(), targetLocation);
            return fileUpload;
        } catch (IOException ex) {
            throw new UploadException(fileUpload.getName());
        }
    }
}
