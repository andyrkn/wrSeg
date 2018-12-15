package ro.info.wrseg.model;

public class FileParameters {
    private Float threshold;
    private Integer noise;
    private Boolean useGauss;
    private Integer maxColumnSeparators;
    private Integer maxSeparators;
    private Float minScale;
    private Integer maxLines;

    public FileParameters(Float threshold,
                          Integer noise,
                          Boolean useGauss,
                          Integer maxColumnSeparators,
                          Integer maxSeparators,
                          Float minScale,
                          Integer maxLines) {
        this.threshold = threshold;
        this.noise = noise;
        this.useGauss = useGauss;
        this.maxColumnSeparators = maxColumnSeparators;
        this.maxSeparators = maxSeparators;
        this.minScale = minScale;
        this.maxLines = maxLines;
    }

    public void setThreshold(Float threshold) {
        this.threshold = threshold;
    }

    public void setNoise(Integer noise) {
        this.noise = noise;
    }

    public void setUseGauss(Boolean useGauss) {
        this.useGauss = useGauss;
    }

    public void setMaxColumnSeparators(Integer maxColumnSeparators) {
        this.maxColumnSeparators = maxColumnSeparators;
    }

    public void setMaxSeparators(Integer maxSeparators) {
        this.maxSeparators = maxSeparators;
    }

    public void setMinScale(Float minScale) {
        this.minScale = minScale;
    }

    public void setMaxLines(Integer maxLines) {
        this.maxLines = maxLines;
    }

    public Float getThreshold() {
        return threshold;
    }

    public Integer getNoise() {
        return noise;
    }

    public Boolean getUseGauss() {
        return useGauss;
    }

    public Integer getMaxColumnSeparators() {
        return maxColumnSeparators;
    }

    public Integer getMaxSeparators() {
        return maxSeparators;
    }

    public Float getMinScale() {
        return minScale;
    }

    public Integer getMaxLines() {
        return maxLines;
    }

    @Override
    public String toString() {
        return "threshold = " + threshold +
                "\nnoise = " + noise +
                "\nuseGauss = " + useGauss +
                "\nmaxColumnSeparators = " + maxColumnSeparators +
                "\nmaxSeparators = " + maxSeparators +
                "\nminScale = " + minScale +
                "\nmaxLines = " + maxLines;
    }
}
