package ro.info.wrseg.model;

import org.springframework.web.multipart.MultipartFile;

public class FileUpload {
    private MultipartFile multipartFile;
    private String name;
    private String extension;

    public FileUpload() {
    }

    public FileUpload(MultipartFile multipartFile, String name, String extension) {
        this.multipartFile = multipartFile;
        this.name = name;
        this.extension = extension;
    }

    public void setMultipartFile(MultipartFile multipartFile) {
        this.multipartFile = multipartFile;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }

    public MultipartFile getMultipartFile() {
        return multipartFile;
    }

    public String getName() {
        return name;
    }

    public String getExtension() {
        return extension;
    }
}
