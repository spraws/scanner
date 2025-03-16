import React from 'react';
import logo from '../../assets/images/uni-logo.png';
import GlassyCardScanButton from '../scan-button';

const Greeter = () => {
    return (
        <div className="flex flex-col items-center justify-center min-h-screen text-center font-poppins">
            {/* Logo at the top */}
            <img src={logo} alt="University Logo" className="w-72 mb-6 drop-shadow-2xl" />
            
            {/* Text content */}
            <h1 className="text-4xl font-semibold">Welcome to Worcester</h1>
            <p className="text-lg mt-2">Press the button below to scan your card</p>
            
            {/* Scan button */}
            <GlassyCardScanButton className="mt-8" onClick={() => alert('Scan button clicked!')} />

        </div>
    );
};

export default Greeter;
