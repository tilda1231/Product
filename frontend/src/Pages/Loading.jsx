import React from 'react';
import { Oval } from 'react-loader-spinner';
import './Loading.css';

const Loading = () => {
  return (
    <div className="loading-page">
      <h2>Loading...</h2>
      <p>Please wait while we generate your recommendations.</p>
      <Oval
        height={80}
        width={80}
        color="#ffcccb"
        wrapperStyle={{}}
        wrapperClass=""
        visible={true}
        ariaLabel='oval-loading'
        secondaryColor="#ffcccb"
        strokeWidth={2}
        strokeWidthSecondary={2}
      />
    </div>
  );
}

export default Loading;
