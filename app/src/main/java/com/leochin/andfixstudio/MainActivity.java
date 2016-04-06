package com.leochin.andfixstudio;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "euler";

    private TextView mTestView;
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mTestView = (TextView) findViewById(R.id.tv_test);

        String vmVersion = System.getProperty("java.vm.version");
        mTestView.setText(vmVersion);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        android.os.Process.killProcess(android.os.Process.myPid());
    }

    public void showToast(View v) {
        A.showToast(this);
    }
}
