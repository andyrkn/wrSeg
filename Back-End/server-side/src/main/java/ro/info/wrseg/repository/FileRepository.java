package ro.info.wrseg.repository;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.info.wrseg.exception.UploadException;
import ro.info.wrseg.model.FileUpload;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Component("fileRepository")
public class FileRepository {
    private Logger logger = LoggerFactory.getLogger(FileRepository.class);
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
            final String JPG_EXTENSION = "jpg";
            Path targetLocation = this.fileStorageLocation.resolve(fileUpload.getName() + "." + JPG_EXTENSION);
            logger.debug("Attempting to save the file " + fileUpload.getName()
                    + " in the following target location: " + targetLocation.toString());
            Files.copy(fileUpload.getMultipartFile().getInputStream(), targetLocation);
            fileUpload.setExtension(JPG_EXTENSION);
            return fileUpload;
        } catch (IOException ex) {
            logger.debug("Throwing upload exception - filename: " + fileUpload);
            throw new UploadException(fileUpload.getName());
        }
    }
}
