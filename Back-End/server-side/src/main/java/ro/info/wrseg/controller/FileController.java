package ro.info.wrseg.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import ro.info.wrseg.model.FileUpload;
import ro.info.wrseg.service.FileStorageService;
import ro.info.wrseg.service.ProcessedImagesReader;
import ro.info.wrseg.service.ScriptRunnerService;

@RestController
@RequestMapping("/upload-file")
public class FileController {
    private FileStorageService fileStorageService;
    private ScriptRunnerService scriptRunnerService;
    private ProcessedImagesReader processedImagesReader;
    private Logger logger = LoggerFactory.getLogger(FileController.class);

    @Autowired
    FileController(FileStorageService fileStorageService,
                   ScriptRunnerService scriptRunnerService,
                   ProcessedImagesReader processedImagesReader) {
        this.fileStorageService = fileStorageService;
        this.scriptRunnerService = scriptRunnerService;
        this.processedImagesReader = processedImagesReader;
    }

    @CrossOrigin(origins = "*")
    @PostMapping()
    public String uploadFile(@RequestParam("file") MultipartFile multipartFile) {
        FileUpload fileUpload = fileStorageService.save(multipartFile);
        logger.debug("Attempting to run the Python script");
        scriptRunnerService.run(fileUpload.getName());
        logger.debug("Python script has been executed");
        return processedImagesReader.getContent(fileUpload.getName());
    }
}
