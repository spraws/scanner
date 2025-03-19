import { useState } from 'react';
import { Scan } from 'lucide-react';
import { RunRFIDScan } from '../../wailsjs/go/main/App';

export default function GlassyCardScanButton({ className = "", onClick }) {
  const [isScanning, setIsScanning] = useState(false);

  const buttonClasses = `
    relative group overflow-hidden rounded-md px-6 py-3 text-2xl
    bg-white/10 backdrop-blur-md border border-white/20
    hover:bg-white/20 hover:border-white/30 active:scale-[0.98]
    transition-all duration-300 text-white shadow-lg
    ${className}
  `.trim();

  async function scan() {
    setIsScanning(true);
    try {
      const result = await RunRFIDScan();
      if (!result) {
        throw new Error('No scan result received');
      }
      console.log('Scan result:', result);

      try {
        const data = JSON.parse(result);
        alert(`Scan successful!\nName: ${data.Name}\nStudent ID: ${data.student_id}`);
      } catch {
        alert(`Scan successful: ${result}`);
      }
    } catch (error) {
      console.error('Scan error:', error);
      alert(`Scan failed: ${error.message}`);
    } finally {
      setIsScanning(false);
    }
  }

  return (
    <button onClick={scan} className={buttonClasses} disabled={isScanning}>
      <div className="absolute inset-0 bg-gradient-to-br from-white/10 to-transparent opacity-50 group-hover:opacity-70 transition-opacity" />
      <div className="absolute -inset-full h-full w-1/2 block transform -skew-x-12 bg-gradient-to-r from-transparent to-white/20 opacity-40 group-hover:animate-shine" />
      <span className="relative flex items-center justify-center gap-3">
        <Scan className="h-12 w-12" />
        <span>{isScanning ? 'Scanning...' : 'Scan Card'}</span>
      </span>
    </button>
  );
}
