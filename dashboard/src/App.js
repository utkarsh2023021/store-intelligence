import {
  BrowserRouter,
  Routes,
  Route
}
from "react-router-dom";

import Navbar
from "./components/Navbar";

import ZoneCalibration
from "./pages/ZoneCalibration";

import Dashboard
from "./pages/Dashboard";

import VideoUpload
from "./pages/VideoUpload";

import Processing
from "./pages/Processing";

function App() {

  return (

    <BrowserRouter>

      <Navbar />

      <Routes>

        <Route
          path="/"
          element={
            <Dashboard />
          }
        />

        <Route
          path="/calibration"
          element={
            <ZoneCalibration />
          }
        />

        <Route
          path="/upload"
          element={
            <VideoUpload />
          }
        />

        <Route
  path="/processing"
  element={
    <Processing />
  }
/>

      </Routes>

    </BrowserRouter>
  );
}

export default App;