//################################################################
//#DNT: MainActivity.java
//#Copyright © 2024 Allison Munn
//#FULL COPYRIGHT NOTICE IS IN README
//################################################################

package com.thenullplayer.dnt;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ProgressBar;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity
{
    ProgressBar button = null;
    TextView text = null;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);

        //set the layout
        setContentView(R.layout.activity_main);

        button = (ProgressBar) findViewById(R.id.progressBar);
        button.setOnClickListener(new ButtonClickListener());

        text = (TextView) findViewById(R.id.textViewLogo);
    }

    @Override
    protected void onRestart()
    {
        super.onRestart();
    }

    @Override
    protected void onStart()
    {
        super.onStart();
    }
    
    @Override
    protected void onResume()
    {
        super.onResume();
    }

    @Override
    protected void onPause()
    {
        super.onPause();
    }

    @Override
    protected void onStop()
    {
        super.onStop();
    }

    @Override
    protected void onDestroy()
    {
        super.onDestroy();

        button.setOnClickListener(null);
        button = null;
    }

    class ButtonClickListener implements View.OnClickListener
    {
        int count = 0;

        public ButtonClickListener()
        {

        }

        public void onClick(View vIn)
        {
            count = count+1;

            if(count == 9)
            {
                count = 0;
                //launch alpha testing activity.
                Intent intent = new Intent();
                intent.setAction("com.thenullplayer.dnt.MAIN");
                startActivity(intent);
            }
        }
    }
}