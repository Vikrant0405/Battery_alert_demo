# Battery Alert Demo

A Python program that monitors battery status and sends notifications when the battery is fully charged or running low. It provides both visual notifications and voice alerts to remind users about charging status.

## Features

- **Battery Monitoring**: Continuously monitors battery percentage and charging status
- **High Battery Alert**: Notifies when battery reaches 80% or higher while charging
- **Low Battery Alert**: Notifies when battery falls below 20% regardless of charger connection
- **Visual Notifications**: Sends system notifications using plyer library
- **Voice Alerts**: Uses text-to-speech (pyttsx3) to announce battery status
- **Charger Status Detection**: Tells whether charger is connected or not when battery is low

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Required Python packages:
  - `psutil` - For battery sensor information
  - `plyer` - For system notifications
  - `pyttsx3` - For text-to-speech functionality

## Installation

1. **Clone the repository**
   
```
bash
   git clone https://github.com/Vikrant0405/Battery_alert_demo.git
   cd Battery_alert_demo
   
```

2. **Install Python dependencies**
   
```
bash
   pip install psutil plyer pyttsx3
   
```

## Usage

1. **Run the program**
   
```
bash
   python battery.py
   
```

2. **How it works**:
   - The program continuously monitors your battery status
   
   - **High Battery Alert** (Battery >= 80% AND charger plugged in):
     - Displays: "🔋 Battery Full - Battery is fully charged. Please unplug the charger!"
     - Voice: "Battery is fully charged. Please unplug the charger!"
   
   - **Low Battery Alert** (Battery < 20%):
     - If charger IS connected: "Battery is low at X percent. Please plug in the charger, it is connected!"
     - If charger is NOT connected: "Battery is low at X percent. Please connect the charger!"

## Configuration

You can modify the battery thresholds in the code:

```
python
# High battery threshold
if battery.percent >= 80 and battery.power_plugged:

# Low battery threshold
elif battery.percent < 20:
```

Change `80` or `20` to your desired threshold percentages.

## Project Structure

```
Battery_alert_demo/
├── battery.py       # Main application file
└── README.md       # Project documentation
```

## Technology Stack

- **Language**: Python
- **Battery Monitoring**: psutil
- **Notifications**: plyer
- **Text-to-Speech**: pyttsx3

## Code Explanation

### Main Components:

1. **Battery Monitoring**:
   
```
python
   battery = psutil.sensors_battery()
   
```
   Gets current battery percentage and charging status.

2. **High Battery Condition**:
   
```
python
   if battery.percent >= 80 and battery.power_plugged:
   
```
 when battery >=   Triggers alert 80% AND charger is connected.

3. **Low Battery Condition**:
   
```
python
   elif battery.percent < 20:
       if battery.power_plugged:
           # Charger is connected but battery is low
       else:
           # Charger is not connected
   
```
   Triggers alert when battery < 20%, with different messages based on charger status.

4. **Visual Notification**:
   
```
python
   notification.notify(
       title="🔋 Low Battery",
       message=f"Battery is at {battery.percent}%. Please connect the charger!",
       timeout=5
   )
   
```

5. **Voice Alert**:
   
```
python
   speak.say(f"Battery is low at {battery.percent} percent. Please connect the charger!")
   speak.runAndWait()
   
```

## License

This project is for educational purposes.
