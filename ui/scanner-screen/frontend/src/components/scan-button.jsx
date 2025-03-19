import { useState, useEffect } from 'react';
import { Scan, CheckCircle, XCircle } from 'lucide-react';
import { RunRFIDScan } from '../../wailsjs/go/main/App';

export default function GlassyCardScanButton({ className = "" }) {
  const [isScanning, setIsScanning] = useState(false);
  const [notification, setNotification] = useState(null);
  const [showNotification, setShowNotification] = useState(false);
  const [progressWidth, setProgressWidth] = useState(100);

  const buttonClasses = `
    relative group overflow-hidden rounded-md text-3xl
    bg-white/10 backdrop-blur-md border border-white/20
    hover:bg-white/20 hover:border-white/30 active:scale-95
    transition-all duration-300 text-white shadow-lg
    disabled:opacity-50 disabled:cursor-not-allowed 
    ${className}
  `.trim();

  useEffect(() => {
    let timer;
    let progressTimer;
    
    if (showNotification) {
      setProgressWidth(100);
      
      // Update progress bar every 30ms
      progressTimer = setInterval(() => {
        setProgressWidth(prev => Math.max(prev - (100 / 3000 * 30), 0));
      }, 30);
      
      // Hide notification after 3 seconds
      timer = setTimeout(() => {
        setShowNotification(false);
      }, 3000);
    }
    
    return () => {
      clearTimeout(timer);
      clearInterval(progressTimer);
    };
  }, [showNotification]);

// ...existing code...
const scan = async () => {
  setIsScanning(true);
  try {
    const result = await RunRFIDScan();
    if (!result) throw new Error('No scan result received');

    console.log('Scan result:', result);

    // Extract the Python dictionary part
    const dictMatch = result.match(/{.*}/s);
    if (!dictMatch) throw new Error('Invalid scan result format');
    
    // Better conversion from Python dict to JSON
    let jsonStr = dictMatch[0]
      .replace(/'/g, '"')
      .replace(/(\w+):/g, '"$1":')
      .replace(/"(\d+)":/g, '$1:'); // Fix numeric values that got quoted
    
    console.log('Converted JSON string:', jsonStr);
    
    const data = JSON.parse(jsonStr);
    setNotification({
      success: true,
      title: 'Scan Successful',
      data: {
        name: data.Name,
        studentId: data.student_id
      }
    });
    setShowNotification(true);
    
  } catch (error) {
    console.error('Scan error:', error);
    setNotification({
      success: false,
      title: 'Scan Failed',
      message: error.message || error
    });
    setShowNotification(true);
  } finally {
    setIsScanning(false);
  }
};
// ...existing code...

  return (
    <div className="relative">
      <button 
        onClick={scan} 
        className={buttonClasses} 
        disabled={isScanning}
      >
        <div className="absolute inset-0 bg-gradient-to-br from-white/10 to-transparent opacity-50 group-hover:opacity-70 transition-opacity" />
        <div className="absolute -inset-full h-full w-1/2 transform -skew-x-12 bg-gradient-to-r from-transparent to-white/20 opacity-40 group-hover:animate-shine" />
        
        <span className="relative flex items-center justify-center gap-6 py-8 px-12">
          <Scan className="h-16 w-16" />
          <span>{isScanning ? 'Scanning...' : 'Scan Card'}</span>
        </span>
      </button>

      {/* Notification Popup */}
      {showNotification && notification && (
        <div className="absolute top-0 left-0 right-0 -mt-24 mx-auto w-80 bg-black/20 backdrop-blur-md border border-white/20 rounded-lg overflow-hidden shadow-2xl text-white">
          <div className="p-4">
            <div className="flex items-center gap-3 mb-2">
              {notification.success ? (
                <CheckCircle className="h-6 w-6 text-green-500" />
              ) : (
                <XCircle className="h-6 w-6 text-red-500" />
              )}
              <h3 className="text-xl font-semibold">{notification.title}</h3>
            </div>
            
            {notification.success ? (
              <div className="ml-9">
                <p><span className="opacity-70">Name:</span> {notification.data.name}</p>
                <p><span className="opacity-70">Student ID:</span> {notification.data.studentId}</p>
              </div>
            ) : (
              <p className="ml-9 text-red-300">{notification.message}</p>
            )}
          </div>
          
          {/* Progress Bar */}
          <div className="h-1 bg-white/10">
            <div 
              className="h-full bg-white/50" 
              style={{ width: `${progressWidth}%`, transition: 'width 30ms linear' }}
            />
          </div>
        </div>
      )}
    </div>
  );
}
