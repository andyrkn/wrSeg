package ro.info.wrseg.service;

import ro.info.wrseg.model.FileParameters;
import ro.info.wrseg.model.FileUpload;

public interface ScriptRunnerService {
    void run(FileUpload fileUpload, FileParameters fileParameters);
}
