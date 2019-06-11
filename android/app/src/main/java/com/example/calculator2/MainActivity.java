package com.example.calculator2;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    private Button ButtonA, ButtonT, ButtonN, ButtonD,
            Button1, Button2, Button3, ButtonP,
            Button4, Button5, Button6, ButtonM,
            Button7, Button8, Button9, ButtonU,
            ButtonC, Button0, ButtonZ, ButtonE;
    private EditText edit;
    private int a;
    private int where = 0;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toast.makeText(getApplicationContext(), "Calculator", Toast.LENGTH_SHORT).show();
        ButtonA = (Button) findViewById(R.id.buttonA);
        ButtonT = (Button) findViewById(R.id.buttonT);
        ButtonN = (Button) findViewById(R.id.buttonN);
        ButtonD = (Button) findViewById(R.id.buttonD);
        Button1 = (Button) findViewById(R.id.button1);
        Button2 = (Button) findViewById(R.id.button2);
        Button3 = (Button) findViewById(R.id.button3);
        ButtonP = (Button) findViewById(R.id.buttonP);
        Button4 = (Button) findViewById(R.id.button4);
        Button5 = (Button) findViewById(R.id.button5);
        Button6 = (Button) findViewById(R.id.button6);
        ButtonM = (Button) findViewById(R.id.buttonM);
        Button7 = (Button) findViewById(R.id.button7);
        Button8 = (Button) findViewById(R.id.button8);
        Button9 = (Button) findViewById(R.id.button9);
        ButtonU = (Button) findViewById(R.id.buttonU);
        ButtonC = (Button) findViewById(R.id.buttonC);
        Button0 = (Button) findViewById(R.id.button0);
        ButtonZ = (Button) findViewById(R.id.buttonZ);
        ButtonE = (Button) findViewById(R.id.buttonE);
        edit = (EditText) findViewById(R.id.edit1);

        View.OnClickListener cl = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (v == Button)
            }
        }
    }
}