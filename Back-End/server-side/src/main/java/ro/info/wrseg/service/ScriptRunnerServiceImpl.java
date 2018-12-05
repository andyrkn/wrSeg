package ro.info.wrseg.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;
import ro.info.wrseg.exception.InvalidFileExtensionException;
import ro.info.wrseg.model.FileUpload;
import ro.info.wrseg.repository.FileRepository;

import java.util.Objects;

import static java.util.UUID.randomUUID;

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.file.Paths;
import java.nio.file.Path;

@Service
public class ScriptRunnerServiceImpl implements ScriptRunnerService {
    public void run(String fileName) {
        Path path = Paths.get("./../scripts");
        String pathToScript = path.resolve("script.py").toString();
        System.out.println("Attempting to run " + pathToScript + " " +  fileName);
        try {
            Process p = Runtime.getRuntime().exec("python " + pathToScript + " " + fileName);
            BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String s;
            System.out.println("Here is the standard output of the command:\n");
            StringBuilder content= new StringBuilder();
            while ((s = stdInput.readLine()) != null) {
                content.append(s);
            }
            // if(content.toString()==fileName) {
            //     System.out.println(content.toString());
            // }
            // else {
            //     // throw exception to front
            // }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
