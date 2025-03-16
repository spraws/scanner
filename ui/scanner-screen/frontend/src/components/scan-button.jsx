"use client"

import { Scan } from 'lucide-react';
import { invoke } from '@wails/runtime'; // Import the Wails runtime invoke method

export default function GlassyCardScanButton({ className = "", onClick }) {
  // Combine default classes with any custom classes
  const buttonClasses = `
    relative group overflow-hidden rounded-md px-4 py-2
    bg-white/10 backdrop-blur-md border border-white/20
    hover:bg-white/20 hover:border-white/30 active:scale-[0.98]
    transition-all duration-300 text-white shadow-lg
    ${className}
  `.trim()

  // Function that will be triggered when the button is clicked
  const handleScan = async () => {
    try {
      // Call the Go function that runs the Python script
      const response = await invoke('RunRFIDScan'); // Calls the Go function exposed by Wails
      alert(`RFID Scan Result:\n${response}`); // Display the result from the script
    } catch (error) {
      alert(`Error: ${error}`); // Handle any error that occurs during the scan
    }
  }

  return (
    <button onClick={handleScan} className={buttonClasses}>
      {/* Gradient overlay */}
      <div className="absolute inset-0 bg-gradient-to-br from-white/10 to-transparent opacity-50 group-hover:opacity-70 transition-opacity" />

      {/* Shine effect */}
      <div className="absolute -inset-full h-full w-1/2 block transform -skew-x-12 bg-gradient-to-r from-transparent to-white/20 opacity-40 group-hover:animate-shine" />

      {/* Button content */}
      <span className="relative flex items-center justify-center gap-2">
        <Scan className="h-5 w-5" />
        <span>Scan Card</span>
      </span>
    </button>
  )
}
