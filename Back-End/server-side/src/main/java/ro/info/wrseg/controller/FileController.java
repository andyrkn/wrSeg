package ro.info.wrseg.controller;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import ro.info.wrseg.model.FileUpload;
import ro.info.wrseg.service.FileStorageService;
import ro.info.wrseg.service.ScriptRunnerService;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.Objects;

@RestController
@RequestMapping("/upload-file")
public class FileController {
    private FileStorageService fileStorageService;
    private ScriptRunnerService scriptRunnerService;

    @Autowired
    FileController(FileStorageService fileStorageService, ScriptRunnerService scriptRunnerService) {
        this.fileStorageService = fileStorageService;
        this.scriptRunnerService = scriptRunnerService;
    }

	@CrossOrigin(origins = "*")
    @PostMapping()
    public String uploadFile(@RequestParam("file") MultipartFile multipartFile) throws IOException {
        FileUpload fileUpload = fileStorageService.save(multipartFile);
        scriptRunnerService.run(fileUpload.getName());
        Path path = Paths.get("./../processed-images/" + fileUpload.getName() + ".json");
        byte[] encoded = Files.readAllBytes(path);

        return new String(encoded, StandardCharsets.UTF_8);
    }
}
