package ro.info.wrseg.service;

import org.springframework.stereotype.Service;
import ro.info.wrseg.exception.InvalidFileExtensionException;
import ro.info.wrseg.exception.ProcessingException;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Service
public class ProcessedImagesReaderImpl implements ProcessedImagesReader{
    public String getContent(String fileName) {
        try {
            Path path = Paths.get("./../processed-images/" + fileName + ".json");
            byte[] encoded = Files.readAllBytes(path);
            return new String(encoded, StandardCharsets.UTF_8);
        } catch (IOException e) {
            throw new ProcessingException(fileName);
        }
    }
}
