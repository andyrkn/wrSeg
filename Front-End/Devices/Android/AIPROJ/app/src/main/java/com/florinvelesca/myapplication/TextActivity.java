package com.florinvelesca.myapplication;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Rect;
import android.graphics.drawable.BitmapDrawable;
import android.media.Image;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.TextView;
import android.widget.Toast;
import android.widget.Toolbar;

import com.florinvelesca.myapplication.model.FloatSeekBar;
import com.google.gson.Gson;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import okhttp3.MediaType;
import okhttp3.MultipartBody;
import okhttp3.OkHttpClient;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;

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

  HttpURLConnection httpUrlConnection = null;
  DataOutputStream request;

  private Gson responseGson = new Gson();
  private ArrayList<Rect> rectList = new ArrayList<>();
  private Bitmap bitmap;


  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_text);
    linkUi();
    setSeekBarListners();
    if (getIntent().hasExtra("picture")) {
      photoExtra = (Uri) getIntent().getParcelableExtra("picture");
      textImageView.setImageURI(photoExtra);
    }

    if (textImageView.getDrawable() != null) {
      noPhotoSelected.setVisibility(TextView.GONE);
    }

    //make request on click
    @SuppressLint("StaticFieldLeak")
    AsyncTask asyncTask = new AsyncTask() {
      @Override
      protected Object doInBackground(Object[] objects) {
        try {
          //create a file to write bitmap data
          File f = new File(getFilesDir(), "temp.jpg");
          f.createNewFile();

          //Convert bitmap to byte array
          bitmap = ((BitmapDrawable) textImageView.getDrawable()).getBitmap();
          ByteArrayOutputStream bos = new ByteArrayOutputStream();
          bitmap.compress(Bitmap.CompressFormat.JPEG, 90 /*ignored for PNG*/, bos);
          byte[] bitmapdata = bos.toByteArray();

          Bitmap test = BitmapFactory.decodeByteArray(bitmapdata, 0, bitmapdata.length);

          //write the bytes in file
          FileOutputStream fos = new FileOutputStream(f);
          fos.write(bitmapdata);
          fos.flush();
          fos.close();

          RequestBody reqFile = RequestBody.create(MediaType.parse("image/*"), f);
          MultipartBody.Part body = MultipartBody.Part.createFormData("file", f.getName(), reqFile);

          OkHttpClient okHttpClient = new OkHttpClient.Builder()
            .connectTimeout(120, TimeUnit.SECONDS)
            .writeTimeout(120, TimeUnit.SECONDS)
            .readTimeout(120, TimeUnit.SECONDS)
            .build();

          Service service = new Retrofit.Builder().client(okHttpClient).baseUrl("http://localhost:8082").build().create(Service.class);
          Call<ResponseBody> req = service.postImage(body);
          req.enqueue(new Callback<ResponseBody>() {
            @Override
            public void onResponse(Call<ResponseBody> call, Response<ResponseBody> response) {
              // Do Something
              try {
                String responseString = response.body().string();

                JSONObject jsonObject = new JSONObject(responseString);
                JSONArray rectanglesArray = jsonObject.getJSONArray("columns");

                ArrayList<String> rectSrings = new ArrayList<>();

                Log.i("JSONARRAY", rectanglesArray.toString());

                for (int i = 0; i < rectanglesArray.length(); i++) {
                  String str = rectanglesArray.getString(i);
                  Pattern p = Pattern.compile("\\d+");
                  Matcher m = p.matcher(str);
                  int[] coord = new int[4];
                  int j = 0;

                  while (m.find()) {
                    coord[j] = Integer.valueOf(m.group());
                    j++;
                  }

                  rectList.add(new Rect(coord[0], coord[1], coord[2], coord[3]));
                }

                Bitmap mutableBitmap = bitmap.copy(Bitmap.Config.ARGB_8888, true);
                Canvas canvas = new Canvas(mutableBitmap);
                Paint paint = new Paint();
                paint.setColor(Color.RED);
                paint.setStyle(Paint.Style.STROKE);
                paint.setStrokeWidth(5f);

                for (Rect rect: rectList) {
                  canvas.drawBitmap(mutableBitmap, 0, 0, null);
                  canvas.drawRect(rect, paint);
                }

                textImageView.setImageBitmap(mutableBitmap);
              } catch (Exception e) {
                e.printStackTrace();
              }
            }

            @Override
            public void onFailure(Call<ResponseBody> call, Throwable t) {
              t.printStackTrace();
            }
          });
        } catch (Exception e) {
          e.printStackTrace();
        }
        return null;
      }
    };

    findViewById(R.id.btnSubmit).setOnClickListener(l -> asyncTask.execute());
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
