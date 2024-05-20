# WardrobeWhiz Frontend

This project is the frontend for the WardrobeWhiz intelligent clothing recommendation system. It is built with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the `frontend` directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However, we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

## Directory Structure

- `public/`: Public assets and the HTML template.
- `src/`: Source code for the React application.
  - `Components/`: Reusable components.
    - `Assets/`: Images and other assets.
    - `Hero/`: Hero component.
    - `Items/`: Items component.
    - `Navbar/`: Navbar component.
  - `Context/`: Context providers for global state.
  - `Pages/`: React components for each page.
    - `About.jsx`, `About.css`: About page.
    - `AccessoryDetail.jsx`, `AccessoryDetail.css`: Accessory detail page.
    - `Contact.jsx`, `Contact.css`: Contact page.
    - `Home.jsx`: Home page.
    - `Loading.jsx`, `Loading.css`: Loading page.
    - `Recommendations.jsx`, `Recommendations.css`: Recommendations page.
    - `Trends.jsx`, `Trends.css`: Trends page.
    - `UploadOutfit.jsx`, `UploadOutfit.css`: Upload outfit page.
  - `App.js`, `App.css`: Main application component.
  - `index.js`, `index.css`: Entry point for the React application.
  - `logo.svg`: React logo.
  - `reportWebVitals.js`: Performance metrics.
  - `setupTests.js`: Test setup.
