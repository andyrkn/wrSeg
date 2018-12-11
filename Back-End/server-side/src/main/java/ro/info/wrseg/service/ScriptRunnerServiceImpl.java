package ro.info.wrseg.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import ro.info.wrseg.controller.FileController;
import ro.info.wrseg.model.FileUpload;

import java.io.BufferedReader;
import java.io.File;
import java.io.InputStreamReader;
import java.nio.file.Path;
import java.nio.file.Paths;

@Service
public class ScriptRunnerServiceImpl implements ScriptRunnerService {
    private final String PATH_TO_SCRIPTS = "./../scripts";
    private final String SCRIPT_NAME = "script.py";
    private Logger logger = LoggerFactory.getLogger(FileController.class);

    public void run(FileUpload fileUpload) {
        Path path = Paths.get(PATH_TO_SCRIPTS);
        String pathToScript = path.resolve(SCRIPT_NAME).toString();
        logger.debug("Attempting to run AI Layer (Python script) - pathToScript: " + pathToScript);
        try {
            String[] cmd = {
                    "python",
                    pathToScript,
                    fileUpload.getName() + "." + fileUpload.getExtension()
            };
            File file = new File("./../scripts");
            Process scriptPyProcess = Runtime.getRuntime().exec(cmd, null, file);
            logger.debug("Running script process: " + scriptPyProcess + " ...");
            scriptPyProcess.waitFor();
            BufferedReader ScriptStandardOutput = new BufferedReader(new InputStreamReader(scriptPyProcess.getInputStream()));
            StringBuilder content = new StringBuilder();
            String line;
            while ((line = ScriptStandardOutput.readLine()) != null) {
                content.append(line);
            }
            logger.debug("[AI LAYER] The STANDARD OUTPUT of the Python script:\n\n" + content + "\n");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
