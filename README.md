# 🏥 MediCare - Medical Management Dashboard

A modern, professional, and fully responsive medical management dashboard built with vanilla HTML, CSS, and JavaScript. Designed to work seamlessly with the FastAPI backend for doctors and appointments management.

## ✨ Features

### 👨‍⚕️ **Doctor Dashboard**
- **Sidebar Navigation** with smooth transitions
- **Top Navigation Bar** with search, notifications, and profile
- **Stat Cards** displaying key metrics
- **Interactive Charts** (Line chart & Pie chart)
- **Recent Activity** tracking

### 📅 **Appointments Management**
- **Appointments Table** with filtering and sorting
- **Real-time Status Updates** (Confirmed, Pending, Cancelled, Completed)
- **Add Appointment Modal** with date/time picker
- **Action Buttons** (Confirm, Cancel, Complete)
- **Advanced Filters** by date, status, and patient name

### 👥 **Patient Management**
- **Doctor Cards Grid** display
- **Doctor Information** including specialization and fees
- **Availability Status** (Online/Offline)
- **Responsive Grid** layout

### ⚙️ **System Features**
- **Dark Mode Toggle** with persistent storage
- **Responsive Design** (Mobile, Tablet, Desktop)
- **Toast Notifications** for user feedback
- **Smooth Animations** and transitions
- **Real-time Data Loading**
- **Error Handling** with user-friendly messages

## 📁 Project Structure

```
frontend/
├── index.html           # Main HTML entry point
├── css/
│   ├── main.css        # Core layout & styling
│   ├── components.css  # Tables, forms, modals
│   ├── animations.css  # Page & UI animations
│   └── responsive.css  # Mobile & tablet design
├── js/
│   ├── utils.js        # Utility functions & helpers
│   ├── api.js          # API communication layer
│   ├── charts.js       # Chart.js integration
│   └── app.js          # Main application logic
├── components/         # Reusable component docs
├── pages/              # Page templates docs
├── layouts/            # Layout components docs
├── services/           # Service modules docs
└── assets/             # Images & media files
```

## 🚀 Quick Start

### **1. Prerequisites**
- Node.js (for local server) or any HTTP server
- FastAPI backend running on `http://127.0.0.1:8000`

### **2. Installation**

```bash
# Navigate to frontend directory
cd frontend

# If using http-server (optional)
npm install -g http-server

# Start local server
http-server .
```

### **3. Access the Dashboard**
- Open your browser and go to: `http://localhost:8080` (or your server port)

## 🔗 API Integration

The dashboard communicates with your FastAPI backend at `http://127.0.0.1:8000`.

### **Supported API Endpoints**

#### Doctors
- `GET /doctors` - Get all doctors
- `GET /doctors/{id}` - Get specific doctor
- `GET /doctors/summary` - Get doctor summary
- `GET /doctors/filter` - Filter doctors
- `GET /doctors/search` - Search doctors
- `GET /doctors/sort` - Sort doctors
- `GET /doctors/page` - Paginate doctors
- `GET /doctors/browse` - Browse doctors
- `POST /doctors` - Add new doctor
- `PUT /doctors/{id}` - Update doctor
- `DELETE /doctors/{id}` - Delete doctor

#### Appointments
- `GET /appointments` - Get all appointments
- `GET /appointments/active` - Get active appointments
- `GET /appointments/by-doctor/{id}` - Get appointments by doctor
- `GET /appointments/search` - Search appointments
- `GET /appointments/sort` - Sort appointments
- `GET /appointments/page` - Paginate appointments
- `POST /appointments` - Create appointment
- `POST /appointments/{id}/confirm` - Confirm appointment
- `POST /appointments/{id}/cancel` - Cancel appointment
- `POST /appointments/{id}/complete` - Complete appointment

## 🎨 Customization

### **Color Palette**
Edit the CSS variables in `css/main.css`:

```css
:root {
    --primary: #667eea;
    --primary-dark: #764ba2;
    --secondary: #f093fb;
    --accent-blue: #4facfe;
    --accent-green: #43e97b;
    --success: #10b981;
    --warning: #f59e0b;
    --danger: #ef4444;
}
```

### **Breakpoints**
Responsive breakpoints in `css/responsive.css`:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px
- **Small Mobile**: Below 480px

## 🎯 Key Components

### **Modal System**
```javascript
Modal.open('appointmentModal');
Modal.close('appointmentModal');
Modal.toggle('appointmentModal');
```

### **Toast Notifications**
```javascript
Toast.success('Operation successful');
Toast.error('Something went wrong');
Toast.warning('Please check your input');
Toast.info('Information message');
```

### **API Calls**
```javascript
// Get all doctors
const doctors = await API.getDoctors();

// Get appointments
const appointments = await API.getAppointments();

// Create appointment
await API.createAppointment({
    patient_name: 'John Doe',
    doctor_id: 1,
    date: '2024-03-20',
    reason: 'Checkup'
});
```

### **Theme Toggle**
```javascript
Theme.dark();   // Enable dark mode
Theme.light();  // Enable light mode
Theme.toggle(); // Toggle theme
```

## 📊 Charts Integration

The dashboard uses **Chart.js** for data visualization:

- **Appointments Chart** (Line chart for weekly data)
- **Status Chart** (Doughnut chart for appointment status)

Charts are automatically initialized on page load and can be updated dynamically.

## 🛡️ Error Handling

All API calls include error handling with user-friendly toast notifications:
- Network errors
- Server errors (4xx, 5xx)
- Validation errors
- Timeout errors

## 🔒 Security Features

- XSS Protection via DOM manipulation
- CSRF token ready (can be implemented)
- Input validation
- Secure local storage for settings
- HTTPS ready configuration

## 📱 Responsive Design

The dashboard is fully responsive with:
- **Mobile-first** design approach
- **Flexible layouts** using CSS Grid & Flexbox
- **Touch-friendly** buttons and controls
- **Optimized** performance for all devices
- **Adaptive** navigation for mobile

## ⚡ Performance Optimizations

- Minimal dependencies (only Chart.js)
- Efficient DOM manipulation
- Debounced search and filter operations
- Lazy loading for data
- CSS animations with GPU acceleration
- Optimized images and assets

## 🌙 Dark Mode

- One-click dark mode toggle
- Persistent settings using localStorage
- Smooth theme transitions
- All components support both themes

## 🎬 Animations

- **Page Transitions** (fade, slide)
- **Card Hover Effects** (scale, shadow)
- **Button Ripple Effects**
- **Modal Animations** (slide-up, fade)
- **Loading States** (skeleton, spinner)
- **Smooth Scrolling**

## 🌍 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## 📝 Local Storage

The dashboard uses localStorage for:
- Dark mode preference
- User settings
- Recent searches
- Session data

## 🔧 Development Tips

### **Adding New Page**
1. Add HTML in `index.html`
2. Add route in `setupNavigation()`
3. Create load function like `loadPageData()`
4. Add CSS as needed

### **Adding New API Call**
1. Add method in `js/api.js`
2. Include error handling
3. Add toast notification
4. Use in `js/app.js`

### **Styling Components**
1. Add CSS to appropriate file (`main.css`, `components.css`, etc.)
2. Use CSS variables for consistency
3. Ensure mobile responsiveness
4. Test dark mode

## 💡 Tips & Tricks

### **Filter Appointments**
Filters work in real-time and can be combined:
```
Date + Status + Patient Name = Powerful filtering
```

### **Export Data**
Convert tables to CSV for export (feature ready for implementation)

### **Notifications**
Notification bell shows count of pending items

### **Performance Debugging**
Check console for performance logs:
```javascript
console.log('📊 Chart Manager initialized');
console.log('🔗 API initialized');
```

## 🐛 Troubleshooting

### **Backend not connecting**
- Verify FastAPI is running on `http://127.0.0.1:8000`
- Check CORS settings in backend
- Verify API endpoints are correct

### **Charts not rendering**
- Check Chart.js is loaded from CDN
- Verify canvas elements exist in HTML
- Check browser console for errors

### **Dark mode not working**
- Clear browser cache
- Check localStorage is enabled
- Verify CSS variable support

### **Mobile menu stuck**
- Clear session storage
- Hard refresh page (Ctrl+Shift+R)
- Check viewport meta tag

## 📞 Support & Contributions

For issues or improvements:
1. Check the code comments
2. Review API documentation
3. Test with sample data
4. Check browser console for errors

## 📄 License

MediCare Dashboard © 2024. All rights reserved for healthcare use.

## 🎉 Version History

- **v1.0.0** - Initial release with full features
  - Complete dashboard UI
  - Appointment management
  - Doctor management
  - Dark mode support
  - Responsive design
  - API integration

---

**Built with ❤️ for modern healthcare management**

For more info or customization, refer to the inline code documentation and CSS variable definitions.
