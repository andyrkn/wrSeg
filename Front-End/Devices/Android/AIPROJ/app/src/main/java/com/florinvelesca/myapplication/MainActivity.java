package com.florinvelesca.myapplication;

import android.content.Intent;
import android.net.Uri;
import android.os.ResultReceiver;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

public class MainActivity extends AppCompatActivity {
  ImageView imageUpload;
  Button uploadButton;
  Button scanButton;
  Uri selectedImage;
  private static final int RESULT_LOAD_IMAGE = 1;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    linkUi();

    uploadButton.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View v) {
        System.out.println("Tag Button");
        Intent galeryIntent = new Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
        startActivityForResult(galeryIntent, RESULT_LOAD_IMAGE);

      }
    });

    scanButton.setOnClickListener(new View.OnClickListener() {
      @Override
      public void onClick(View v) {
        Intent nextActivity = new Intent(MainActivity.this, TextActivity.class);
        nextActivity.putExtra("picture",selectedImage);
        startActivity(nextActivity);
      }
    });

  }

  private void linkUi() {
    scanButton = findViewById(R.id.scan_button);
    uploadButton = findViewById(R.id.upload_button);
    imageUpload = findViewById(R.id.image_view);
  }

  @Override
  protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode == RESULT_LOAD_IMAGE && resultCode == RESULT_OK && data != null) {
      selectedImage = data.getData();
      imageUpload.setImageURI(selectedImage);
    }
  }
}
