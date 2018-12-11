package ro.info.wrseg.service;

import ro.info.wrseg.model.FileUpload;

public interface ScriptRunnerService {
    void run(FileUpload fileUpload);
}
