import React from 'react';
import logo from '../../assets/images/uni-logo.png';

const Greeter = () => {
    return (
        <div>
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <div className="text-center">
                            <img src={logo} alt="uni logo" className="img-fluid" style={{width: '300px'}}/>
                            <h1 className="display-4 mt-3">Welcome to the University</h1>
                            <p className="lead">Press The Button to Scan your card </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Greeter;