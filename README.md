# DeepFit - AI-Powered Fitness Assessment System
## Sports Authority of India (SAI) - Digital Fitness Evaluation Platform

```text
DeepFit_Documentation.pdf - available in the Repository Files section.
```
## 🎯 Project Overview

DeepFit is an advanced AI-powered fitness assessment platform developed for the Sports Authority of India (SAI) to revolutionize athlete screening and fitness evaluation. Using cutting-edge computer vision and machine learning technologies, the system eliminates the need for expensive equipment and manual measurements, providing accurate, real-time fitness assessments through a simple webcam.

This innovative solution addresses SAI's challenge of conducting large-scale fitness assessments across India by enabling remote, automated evaluation of athletes' physical capabilities. The system provides instant body measurements (height, weight, BMI) and tracks exercise performance (situps, dumbbell curls, vertical jumps) with AI-powered form analysis, making talent identification and fitness monitoring accessible, efficient, and scalable.

**Problem Statement:** Traditional fitness assessments require expensive equipment, trained personnel, and physical presence, making it difficult for SAI to evaluate thousands of aspiring athletes across remote areas of India.

**Solution:** DeepFit uses AI and computer vision to transform any smartphone or laptop camera into a professional fitness assessment tool, enabling SAI to conduct nationwide talent hunts and fitness evaluations remotely, accurately, and cost-effectively.

<img width="1920" height="922" alt="Screenshot 2025-09-18 130234" src="https://github.com/user-attachments/assets/b960c0aa-2986-4696-b0a6-5ae9a174c346" />

<img width="1920" height="930" alt="Screenshot 2025-09-17 181657" src="https://github.com/user-attachments/assets/085edf66-3097-4294-b754-fbc0eb3aa8ce" />

<img width="1398" height="913" alt="Screenshot 2025-09-18 132747" src="https://github.com/user-attachments/assets/d560f4af-3e57-41b4-ad03-21271e7e6a3d" />



### Key Features

- **📏 Height & Weight Estimation**: AI-based body measurement using single camera
- **💪 Exercise Tracking**: Real-time tracking of Situps, Dumbbell Curls, and Vertical Jumps
- **📊 Performance Analytics**: Comprehensive fitness dashboards and progress tracking
- **🎯 Dynamic Benchmarks**: Personalized fitness goals based on athlete data
- **👤 User Management**: Secure authentication with profile management
- **🏆 Leaderboard**: Competitive rankings based on performance metrics

## 🏗️ System Architecture

### Technology Stack

**Backend:**
- Flask (Python Web Framework)
- MongoDB Atlas (Cloud Database)
- MediaPipe (Pose Detection)
- OpenCV (Computer Vision)
- PyTorch (Deep Learning)
- Scikit-learn (Machine Learning)

**Frontend:**
- HTML5, CSS3, JavaScript
- Responsive Design
- Real-time Video Processing

**AI/ML Components:**
- MiDaS (Depth Estimation)
- MediaPipe Holistic (Pose Detection)
- Random Forest (Weight Prediction)
- YOLO (Object Detection - Optional)

## 📁 Project Structure

```
HeightAndWeightCalculator/
│
├── Backend/                          # Backend application
│   ├── models/                       # ML models
│   │   ├── weight_rf_model.pkl      # Weight prediction model
│   │   ├── weight_scaler.pkl        # Feature scaler
│   │   └── yolov8n.pt               # YOLO model (optional)
│   │
│   ├── logs/                         # Application logs
│   ├── uploads/                      # User uploaded files
│   ├── measurements/                 # Measurement data
│   ├── jump_data/                    # Vertical jump data
│   ├── validation_results/           # Validation reports
│   │
│   ├── .env                          # Environment configuration
│   ├── app.py                        # Main Flask application
│   ├── db_config.py                  # Database configuration
│   ├── dynamic_benchmarks.py         # Benchmark system
│   │
│   ├── situp_blueprint.py            # Situp exercise module
│   ├── dumbbell_blueprint.py         # Dumbbell exercise module
│   ├── vertical_jump_blueprint.py    # Vertical jump module
│   ├── advanced_jump_detector.py     # Advanced jump detection
│   │
│   ├── integrated_system.py          # Height/Weight estimation
│   ├── enhanced_ui.py                # UI components
│   ├── session_manager.py            # Session management
│   ├── error_logger.py               # Logging system
│   └── train_model.py                # Model training script
│
├── Frontend/                         # Frontend application
│   ├── templates/                    # HTML templates
│   │   ├── index.html               # Home page
│   │   ├── login.html               # Login page
│   │   ├── signup.html              # Registration page
│   │   ├── dashboard.html           # User dashboard
│   │   ├── performance_dashboard.html # Performance metrics
│   │   ├── Best_Results.html        # Leaderboard
│   │   ├── index_situp.html         # Situp interface
│   │   ├── index_dumbbell.html      # Dumbbell interface
│   │   ├── index_verticaljump.html  # Vertical jump interface
│   │   └── errors/                  # Error pages
│   │
│   └── static/                       # Static assets
│       ├── css/                      # Stylesheets
│       ├── js/                       # JavaScript files
│       └── images/                   # Images
│
├── Datasets/                         # Training data
│   ├── AthleteData.csv              # Athlete benchmark data
│   └── training_data.csv            # Exercise training data
│
└── requirements.txt                  # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account
- Webcam/Camera
- 4GB RAM minimum
- Windows/Linux/macOS

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd HeightAndWeightCalculator
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure MongoDB Atlas

1. Create MongoDB Atlas account at https://cloud.mongodb.com/
2. Create a new cluster named `sih2573`
3. Get your connection string
4. Create `.env` file in `Backend/` folder:

```env
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority
DB_NAME=sih2573
```

### Step 4: Initialize Database

The application will automatically create these collections:
- `users` - User accounts
- `situps` - Situp exercise data
- `DumbBell` - Dumbbell exercise data
- `Vertical_Jump` - Vertical jump data
- `Height and Weight` - Body measurements
- `Final_Estimated_Height_and_Weight` - Final estimates
- `Qualified_Results` - Leaderboard data
- `exercise_sessions` - Session tracking
- `exercise_results` - Exercise results
- `height_videos` - Video uploads
- `measurements` - Additional measurements

### Step 5: Run Application

```bash
cd Backend
python app.py
```

Access the application at: `http://localhost:5000`

## 📖 User Guide

### 1. Registration & Login

1. Navigate to `http://localhost:5000`
2. Click "Sign Up" to create account
3. Fill in details and capture profile photo
4. Login with credentials

### 2. Height & Weight Measurement

1. Go to Dashboard → Height & Weight
2. Stand 2-3 meters from camera
3. Ensure full body is visible
4. System will auto-measure when stable
5. Press 'S' to save measurement
6. Press 'F' for final estimate

**Controls:**
- `S` - Save measurement
- `F` - Final estimate
- `R` - Reset
- `C` - Toggle auto-save
- `K` - Recalibrate camera
- `Q` - Quit

### 3. Exercise Tracking

#### Situps
1. Go to Dashboard → Situps
2. Click "Start Camera"
3. Lie down with full body visible
4. Perform situps (3-minute timer)
5. Click "Stop" when done
6. View results in display page

#### Dumbbell Curls
1. Go to Dashboard → Dumbbell Curls
2. Click "Start Camera"
3. Stand with arms visible
4. Perform curls with both arms
5. System tracks reps and estimates weight
6. Click "Stop" when done

#### Vertical Jump
1. Go to Dashboard → Vertical Jump
2. Click "Start Camera"
3. Stand in frame for calibration
4. Perform vertical jumps
5. System measures jump height
6. Click "Stop" when done

### 4. Performance Dashboard

- View all exercise results
- Compare with benchmarks
- Track progress over time
- See personalized goals

### 5. Leaderboard

- View top performers
- Compare your rankings
- Filter by exercise type
- See detailed statistics

## 🔧 Configuration

### Camera Settings

Edit in respective blueprint files:
```python
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv2.CAP_PROP_FPS, 30)
```

### Exercise Durations

Edit in blueprint files:
```python
SITUP_DURATION = 180  # 3 minutes
```

### Benchmark System

Modify `Datasets/AthleteData.csv` to update benchmark data:
```csv
Age,Gender,Height_cm,Weight_kg,Situps_per_min,Vertical_Jump_cm,Dumbbell_Curl_per_min
25,M,175,70,30,65,25
```

## 🧪 API Endpoints

### Authentication
- `POST /login` - User login
- `POST /signup` - User registration
- `GET /logout` - User logout

### Measurements
- `POST /upload_exercise_video` - Upload exercise video
- `GET /height_weight_system` - Start height/weight measurement
- `GET /performance_dashboard` - View performance metrics

### Exercise APIs
- `GET /situp/start_camera` - Start situp tracking
- `GET /situp/stop_camera` - Stop situp tracking
- `GET /situp/get_stats` - Get current stats
- `POST /api/submit_situp_result` - Submit results

- `GET /dumbbell/start_camera` - Start dumbbell tracking
- `GET /dumbbell/stop_camera` - Stop dumbbell tracking
- `GET /dumbbell/get_stats` - Get current stats
- `POST /api/submit_dumbbell_result` - Submit results

- `GET /vertical_jump/start_camera` - Start jump tracking
- `GET /vertical_jump/stop_camera` - Stop jump tracking
- `GET /vertical_jump/get_stats` - Get current stats
- `POST /api/submit_vertical_jump_result` - Submit results

### Benchmarks
- `GET /api/dynamic_benchmarks?email=<email>` - Get personalized benchmarks
- `POST /api/match_athlete` - Find matching athlete profile

### Leaderboard
- `GET /api/best_results` - Get leaderboard data
- `POST /api/save_qualified_results` - Save to leaderboard

## 🔐 Security Features

- Password hashing with bcrypt
- Session management with secure cookies
- CORS protection
- Input validation
- SQL injection prevention (NoSQL)
- XSS protection

## 📊 Data Models

### User Schema
```javascript
{
  name: String,
  age: Number,
  gender: String,
  place: String,
  phone: String,
  email: String (unique),
  password: Binary (hashed),
  photo: String (base64),
  created_at: DateTime
}
```

### Exercise Result Schema
```javascript
{
  user_email: String,
  reps_completed: Number,
  form_quality: Number,
  timer_time: String,
  submission_time: DateTime,
  created_at: DateTime
}
```

### Height & Weight Schema
```javascript
{
  user_email: String,
  height_cm: Number,
  weight_kg: Number,
  confidence_score: Number,
  uncertainty_height: Number,
  uncertainty_weight: Number,
  timestamp: DateTime,
  bmi: Number
}
```

## 🎓 AI/ML Models

### 1. Height Estimation
- **Method**: MediaPipe Pose + Depth Estimation
- **Accuracy**: ±2-3 cm
- **Input**: Single RGB image
- **Output**: Height in cm

### 2. Weight Estimation
- **Model**: Random Forest Regressor
- **Features**: Body proportions, height, anthropometric ratios
- **Accuracy**: ±3-5 kg
- **Training Data**: 1000+ samples

### 3. Exercise Detection
- **Situps**: Angle-based detection (shoulder-hip-knee)
- **Dumbbell**: Elbow angle tracking
- **Vertical Jump**: Pose tracking + height calculation

### 4. Benchmark Matching
- **Algorithm**: K-Nearest Neighbors
- **Features**: Age, gender, height, weight
- **Dataset**: AthleteData.csv

## 🐛 Troubleshooting

### Camera Not Working
```bash
# Check camera access
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"
```

### MongoDB Connection Failed
1. Check `.env` file exists in `Backend/` folder
2. Verify MongoDB URI is correct
3. Check network connectivity
4. Whitelist IP in MongoDB Atlas (0.0.0.0/0 for testing)

### Module Not Found
```bash
pip install -r requirements.txt --upgrade
```

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)
```

## 📈 Performance Optimization

- Use GPU for PyTorch models (if available)
- Reduce camera resolution for faster processing
- Enable model caching
- Use connection pooling for MongoDB
- Implement lazy loading for ML models

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is developed for educational purposes.

## 👥 Team

Developed for Smart India Hackathon 2024
**Problem Statement by:** Sports Authority of India (SAI)
**Category:** Smart Education & Sports
**Solution:** AI-powered contactless fitness assessment system

## 📞 Support

For issues and questions:
- Check troubleshooting section
- Review console logs
- Verify MongoDB Atlas connection
- Ensure all dependencies are installed

## 🔄 Version History

- **v1.0.0** - Initial release with core features
- **v1.1.0** - Added MongoDB Atlas integration
- **v1.2.0** - Enhanced exercise tracking
- **v1.3.0** - Added dynamic benchmarks
- **v1.4.0** - Performance dashboard improvements

## 🎯 Future Enhancements

- [ ] Mobile app integration
- [ ] Multi-user video sessions
- [ ] Advanced analytics with ML insights
- [ ] Social features and challenges
- [ ] Integration with fitness wearables
- [ ] Nutrition tracking
- [ ] AI-powered form correction
- [ ] Voice commands

## 📚 References

- MediaPipe: https://google.github.io/mediapipe/
- OpenCV: https://opencv.org/
- Flask: https://flask.palletsprojects.com/
- MongoDB: https://www.mongodb.com/

---


