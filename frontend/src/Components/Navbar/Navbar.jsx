import React,{ useState } from 'react'
import './Navbar.css'
import logo from '../Assets/logo.png'
import { Link } from 'react-router-dom'

const Navbar = () => {

    const [menu, setMenu] = useState("home");

  return (
    <div className ='navbar'>
    <div className = 'nav-logo'>
      <img src={logo} alt='logo' />
    </div>
    <ul className="nav-menu">
        <li onClick={()=> {setMenu("home")}}><Link style={{textDecoration: 'none'}} to='/'>Home</Link>{menu==="home"?<hr/>:<></>}</li>
        <li onClick={()=> {setMenu("trends")}}><Link style={{textDecoration: 'none'}} to='/trends'>Trends</Link>{menu==="trends"?<hr/>:<></>}</li>
        <li onClick={()=> {setMenu("contact")}}><Link style={{textDecoration: 'none'}} to='/contact'>Contact</Link>{menu==="contact"?<hr/>:<></>}</li>
        <li onClick={()=> {setMenu("about")}}><Link style={{textDecoration: 'none'}} to='/about'>About</Link>{menu==="about"?<hr/>:<></>}</li>
    </ul>

    </div>
  )
}

export default Navbar