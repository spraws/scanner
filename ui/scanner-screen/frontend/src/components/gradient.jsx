import { useEffect, useRef } from 'react';
import Granim from 'granim';

const GradientBackground = () => {
    const canvasRef = useRef(null);

    useEffect(() => {
        const granimInstance = new Granim({
            element: canvasRef.current,
            name: 'granim',
            opacity: [1, 1],
            states: {
                "default-state": {
                    gradients: [
                        ['#007dba', '#59cbe8'],
                        ['#0087ff', '#ede8d0']
                    ]
                }
            }
        });

        // Cleanup on component unmount
        return () => {
            granimInstance.destroy();
        };
    }, []);

    return (
        <canvas 
            ref={canvasRef}
            style={{
                position: 'fixed',
                width: '100%',
                height: '100%',
                top: 0,
                left: 0,
                zIndex: -1
            }}
        />
    );
};

export default GradientBackground;