package eu.romka.romka_test;

import java.io.IOException;
import java.io.OutputStream;
import java.util.Set;
import java.util.UUID;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothSocket;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class Romka_testActivity extends Activity {
    /** Called when the activity is first created. */
	
	BluetoothDevice bt_device;
	BluetoothSocket mmSocket = null;
	OutputStream mmOutStream;
	Boolean isConnected = false;
	
	private static BluetoothAdapter mBluetoothAdapter = null;
	
	public TextView txt1 = null;
	
	//*
	public void btSendData(int Command, TextView txt1) {
		String tmp = String.format("%d", Command);
		if(isConnected) {			
        	txt1.setText(tmp);
        	try {
        		//String tmp = "1";
        		byte tmp2 = (byte) Command;
        		mmOutStream.write(tmp2);
        		tmp2 = (byte) 255;
        		mmOutStream.write(tmp2);
        		txt1.setText("sent " + tmp);
            } catch (IOException e) {
            	txt1.setText("sent " + tmp + " error [3]");
            }
    	} else {
    		txt1.setText("not connected " + tmp);
    	}
    }
    //*/
	
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        final TextView txt1 = (TextView) findViewById(R.id.text1);

        
        
        // BT        
        
        String tmp_text = "";
        String mac_address = "";
        
        
        
           
        // Interface
        
        
        final Button button1 = (Button) findViewById(R.id.button1);                    
        button1.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(1, txt1);
            }
        });
        
        final Button button2 = (Button) findViewById(R.id.button2);
        button2.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(4, txt1);
            }
        });
        
        final Button button3 = (Button) findViewById(R.id.button3);
        button3.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(7, txt1);
            }
        });
        
        final Button button4 = (Button) findViewById(R.id.button4);
        button4.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(2, txt1);
            }
        });
        
        final Button button5 = (Button) findViewById(R.id.button5);
        button5.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(5, txt1);
            }
        });
        
        final Button button6 = (Button) findViewById(R.id.button6);
        button6.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(8, txt1);
            }
        });
        
        final Button button7 = (Button) findViewById(R.id.button7);
        button7.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(3, txt1);
            }
        });
        
        final Button button8 = (Button) findViewById(R.id.button8);
        button8.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(6, txt1);
            }
        });
        
        final Button button9 = (Button) findViewById(R.id.button9);
        button9.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(9, txt1);
            }
        });
        
        final Button button10 = (Button) findViewById(R.id.button10);                    
        button10.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	if(isConnected) {
	            	txt1.setText("try to close bt conn");
	            	try {
	            		//stop
	            		byte tmp2 = (byte) 5; 
	            		mmOutStream.write(tmp2);
	            		mmOutStream.close();
	            		isConnected = false;
	                } catch (IOException e) {
	                	txt1.setText("colse conn error [4]");
	                }
            	} else {
            		txt1.setText("not connected (close)");
            	}
            }
        });
        
        final Button connect_button = (Button) findViewById(R.id.button11);                    
        connect_button.setOnClickListener(new View.OnClickListener() {
        	
        	String tmp_text = "";
        	
            public void onClick(View v) {
                // Perform action on click
            	txt1.setText("Connecting...");
            	if(!isConnected) {
	            	mBluetoothAdapter = BluetoothAdapter.getDefaultAdapter();
	                if (mBluetoothAdapter == null) {
	                //if (1 == 2) {
	                    // Device does not support Bluetooth
	                	txt1.setText("No BT found");
	                } else {
	                	txt1.setText("Connecting... BT found");
	                	if (!mBluetoothAdapter.isEnabled()) {
	                		txt1.setText("Connecting... BT not enabled");
	                	    Intent enableBtIntent = new Intent(BluetoothAdapter.ACTION_REQUEST_ENABLE);
	                	    startActivityForResult(enableBtIntent, 1);
	                	}
	                	
	                	Set<BluetoothDevice> pairedDevices = mBluetoothAdapter.getBondedDevices();
	                	// If there are paired devices
	                	if (pairedDevices.size() > 0) {
	                	    // Loop through paired devices
	                		
	                	    for (BluetoothDevice device : pairedDevices) {
	                	        // Add the name and address to an array adapter to show in a ListView
	                	        //mArrayAdapter.add(device.getName() + "\n" + device.getAddress());
	                	    	tmp_text += "<" + device.getName() + ">\n" + device.getAddress() + "\n";
	                	    	txt1.setText(tmp_text);
	                	    	
	                	    	/*
	                	    	if(device.getName().toString() == "linvor") {
	                	    		mac_address = device.getAddress();
	                	    		bt_device = device;
	                	    		
	                	    		tmp_text = txt1.getText().toString();
	                        	    tmp_text += "\n Selected mac address = " + mac_address + "; bt_name = " + bt_device.getName();
	                        	    //tmp_text += "\n Selected mac address = " + mac_address;
	                        	    txt1.setText(tmp_text);
	                	    	} else {
	                	    		tmp_text = txt1.getText().toString();
	                        	    tmp_text += "-\n";
	                        	    txt1.setText(tmp_text);
	                	    	}
	                	    	//*/
	                	    	
	                	    	bt_device = device;
	                	    }
	                	    
	        	    		tmp_text = txt1.getText().toString();
	                	    tmp_text += "\n Selected mac address = " + bt_device.getAddress() + "; bt_name = " + bt_device.getName();
	                	    txt1.setText(tmp_text);
	                	    
	                	    
	                	    
	                	    //BluetoothDevice mmDevice = null;
	                	    
	                	    //*
	                	    try {
	                	    	mmSocket = bt_device.createRfcommSocketToServiceRecord(UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"));
	                	    	//mmSocket = bt_device.createRfcommSocketToServiceRecord(UUID.fromString("1"));
	                	    	tmp_text = txt1.getText().toString();
	                	    	tmp_text += "\nsocket created [1]";
	                	    	txt1.setText(tmp_text);
	                	    	//bt_device.createRfcommSocketToServiceRecord(UUID.fromString("fa87c0d0-afac-11de-8a39-0800200c9a66"));
	                	    } catch (IOException connectException) {
	                	    	txt1.setText("Error connection to BT");
	                	    }
	                	    
	                	    //mBluetoothAdapter.cancelDiscovery();
	                	    
	                	    try {
	                            // Connect the device through the socket. This will block
	                            // until it succeeds or throws an exception
	                            mmSocket.connect();
	                        } catch (IOException connectException) {
	                            // Unable to connect; close the socket and get out
	                            try {
	                                mmSocket.close();
	                                tmp_text = txt1.getText().toString();
	                    	    	tmp_text += "\nconnection error [2]";
	                    	    	txt1.setText(tmp_text);
	                            } catch (IOException closeException) { }
	                            return;
	                        }
	                	    
	                	    
	                	    try {
	                	    	mmOutStream = mmSocket.getOutputStream();
	                	    	tmp_text = txt1.getText().toString();
	                	    	tmp_text += "\nstream created [3]";
	                	    	
	                	    	txt1.setText(tmp_text);
	                	    	isConnected = true;
	                	    	
	                	    }  catch (IOException connectException) {
	                	    	txt1.setText("Error creating output stream");
	                	    }
	                	}
	                	else {
	                		txt1.setText("Connecting... Paired device == 0 :((");
	                	}
	                }    
            	}
            	else {
            		txt1.setText("Already connected");
            	}
            }
        });
        
        final Button rot_left = (Button) findViewById(R.id.button12);
        rot_left.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(1, txt1);
            	btSendData(9, txt1);
            }
        });
        
        final Button rot_right = (Button) findViewById(R.id.button13);
        rot_right.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(3, txt1);
            	btSendData(7, txt1);
            }
        });
        
        final Button cam_left = (Button) findViewById(R.id.button14);
        cam_left.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(10, txt1);
            }
        });
        
        final Button cam_right = (Button) findViewById(R.id.button15);
        cam_right.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(11, txt1);
            }
        });
        
        final Button cam_up = (Button) findViewById(R.id.button16);
        cam_up.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(12, txt1);
            }
        });
        
        final Button cam_down = (Button) findViewById(R.id.button17);
        cam_down.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                // Perform action on click
            	btSendData(13, txt1);
            }
        });
    }
    
    @Override
    public void onDestroy() {
    	super.onDestroy();
    	
    	try {
    		String tmp = "5";
    		byte[] tmp2 = tmp.getBytes(); 
    		mmOutStream.write(tmp2);
    		mmOutStream.close();
    		isConnected = false;
        } catch (IOException e) {}
    }
}