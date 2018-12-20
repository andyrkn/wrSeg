package ro.info.wrseg.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.repository.query.Param;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import ro.info.wrseg.model.FileParameters;
import ro.info.wrseg.model.FileUpload;
import ro.info.wrseg.service.FileStorageService;
import ro.info.wrseg.service.ProcessedImagesReader;
import ro.info.wrseg.service.ScriptRunnerService;

@RestController
@RequestMapping("/upload-file")
public class FileController {
    private Logger logger = LoggerFactory.getLogger(FileController.class);
    private FileStorageService fileStorageService;
    private ScriptRunnerService scriptRunnerService;
    private ProcessedImagesReader processedImagesReader;

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
    public String uploadFile(@RequestParam("file") MultipartFile multipartFile,
                             @RequestParam(value = "threshold", required = false) Float threshold,
                             @RequestParam(value = "noise", required = false) Integer noise,
                             @RequestParam(value = "usegauss", required = false) Boolean useGauss,
                             @RequestParam(value = "maxcolseps", required = false) Integer maxColumnSeparators,
                             @RequestParam(value = "maxseps", required = false) Integer maxSeparators,
                             @RequestParam(value = "minscale", required = false) Float minScale,
                             @RequestParam(value = "maxlines", required = false) Integer maxLines) {
        FileUpload fileUpload = fileStorageService.save(multipartFile);
        FileParameters fileParameters = new FileParameters(
                threshold,
                noise,
                useGauss,
                maxColumnSeparators,
                maxSeparators,
                minScale,
                maxLines);
        logger.debug("Received the following parameters:\n" + fileParameters);
        scriptRunnerService.run(fileUpload, fileParameters);
        logger.debug("AI Layer (Python script) has been executed");
        return processedImagesReader.getContent(fileUpload.getName());
    }
}
