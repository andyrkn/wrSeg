package com.florinvelesca.myapplication;

import android.content.Intent;
import android.media.Image;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Toolbar;

import com.florinvelesca.myapplication.model.FloatSeekBar;

public class TextActivity extends AppCompatActivity {
    public static final String THRESHOLD = "Threshold: ";
    public static final String NOISE = "Noise: ";
    private FloatSeekBar floatSeekBar;
    private SeekBar noiseSeekBar;
    private TextView tesholdTextView;
    private TextView noiseTextView;
    private ImageView textImageView;
    private Uri photoExtra;
    private TextView noPhotoSelected;
    private android.support.v7.widget.Toolbar toolbar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_text);
        linkUi();
        setSeekBarListners();
      if (getIntent().hasExtra("picture")) {
        photoExtra = (Uri)getIntent().getParcelableExtra("picture");
        textImageView.setImageURI(photoExtra);
      }

        if(textImageView.getDrawable() != null){
          noPhotoSelected.setVisibility(TextView.GONE);
        }

    }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    noPhotoSelected.setVisibility(TextView.VISIBLE);
  }

  private void linkUi() {
        floatSeekBar = (FloatSeekBar) findViewById(R.id.seekBar);
        tesholdTextView = findViewById(R.id.threshold_text_view);
        noiseTextView = findViewById(R.id.noise_text_view);
        noiseSeekBar = findViewById(R.id.noiseSeekBar);
        textImageView = findViewById(R.id.text_image_view);
        noPhotoSelected = findViewById(R.id.no_photo_selected);
        setSupportActionBar(toolbar);
    }

    private void setSeekBarListners() {

        floatSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                Float progr = floatSeekBar.getValue();
                String valueDisplayed = THRESHOLD + progr.toString();
                tesholdTextView.setText(valueDisplayed);
                Toast.makeText(TextActivity.this, progr.toString(), Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
        noiseSeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                Integer progr = progress;
                String valueDisplayed = NOISE + progr.toString();
                noiseTextView.setText(valueDisplayed);
                Toast.makeText(TextActivity.this, progr.toString(), Toast.LENGTH_SHORT).show();

            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });

    }
}
