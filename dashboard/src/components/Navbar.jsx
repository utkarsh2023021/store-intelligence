import { Link }
from "react-router-dom";

import "../styles/navbar.css";

export default function Navbar() {

  return (

    <div
      className="navbar"
    >

      <div
        className="navbar-logo"
      >
        StoreIQ
      </div>

      <Link
        className="nav-link"
        to="/"
      >
        Dashboard
      </Link>

      <Link
        className="nav-link"
        to="/upload"
      >
        Videos
      </Link>

      <Link
        className="nav-link"
        to="/calibration"
      >
        Calibration
      </Link>

      <Link
  className="nav-link"
  to="/processing"
>
  Processing
</Link>

    </div>
  );
}