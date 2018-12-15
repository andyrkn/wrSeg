package ro.info.wrseg.model;

public class FileParameters {
    private float threshold;
    private int noise;
    private boolean useGauss;
    private int maxColumnSeparators;
    private int maxSeparators;
    private float minScale;
    private int maxLines;

    public FileParameters(float threshold,
                          int noise,
                          boolean useGauss,
                          int maxColumnSeparators,
                          int maxSeparators,
                          float minScale,
                          int maxLines) {
        this.threshold = threshold;
        this.noise = noise;
        this.useGauss = useGauss;
        this.maxColumnSeparators = maxColumnSeparators;
        this.maxSeparators = maxSeparators;
        this.minScale = minScale;
        this.maxLines = maxLines;
    }

    public void setThreshold(float threshold) {
        this.threshold = threshold;
    }

    public void setNoise(int noise) {
        this.noise = noise;
    }

    public void setUseGauss(boolean useGauss) {
        this.useGauss = useGauss;
    }

    public void setMaxColumnSeparators(int maxColumnSeparators) {
        this.maxColumnSeparators = maxColumnSeparators;
    }

    public void setMaxSeparators(int maxSeparators) {
        this.maxSeparators = maxSeparators;
    }

    public void setMinScale(float minScale) {
        this.minScale = minScale;
    }

    public void setMaxLines(int maxLines) {
        this.maxLines = maxLines;
    }

    public float getThreshold() {
        return threshold;
    }

    public int getNoise() {
        return noise;
    }

    public boolean isUseGauss() {
        return useGauss;
    }

    public int getMaxColumnSeparators() {
        return maxColumnSeparators;
    }

    public int getMaxSeparators() {
        return maxSeparators;
    }

    public float getMinScale() {
        return minScale;
    }

    public int getMaxLines() {
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
