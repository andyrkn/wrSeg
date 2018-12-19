package ro.info.wrseg.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import ro.info.wrseg.exception.InvalidFileExtensionException;
import ro.info.wrseg.model.FileUpload;
import ro.info.wrseg.repository.FileRepository;

import java.util.Objects;

import static java.util.UUID.randomUUID;

@Service
public class FileStorageServiceImpl implements FileStorageService {
    private Logger logger = LoggerFactory.getLogger(FileStorageServiceImpl.class);
    private FileRepository fileRepository;

    @Autowired
    public FileStorageServiceImpl(FileRepository fileRepository) {
        this.fileRepository = fileRepository;
    }

    @Override
    public FileUpload save(MultipartFile multipartFile) {
        String fileName = randomUUID().toString();
        String fileExtension;
        try {
            fileExtension = Objects.requireNonNull(multipartFile.getOriginalFilename()).split("\\.")[1];
        } catch (Exception ex) {
            logger.debug("Throwing invalid file extension exception - filename: " + fileName);
            throw new InvalidFileExtensionException(fileName);
        }
        FileUpload fileUpload = new FileUpload(multipartFile, fileName, fileExtension);
        return fileRepository.save(fileUpload);
    }
}
