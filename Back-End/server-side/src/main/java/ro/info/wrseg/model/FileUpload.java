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

    //    public byte[] getBytes() {
//        if (bytes == null) {
//            bytes = new byte[]{};
//        }
//        return bytes.clone();
//    }
//
//    public void setBytes(byte[] bytes) {
//        if (bytes != null) {
//            this.bytes = bytes;
//        } else {
//            this.bytes = new byte[]{};
//        }
//    }


    public MultipartFile getMultipartFile() {
        return multipartFile;
    }

    public void setMultipartFile(MultipartFile multipartFile) {
        this.multipartFile = multipartFile;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
}
