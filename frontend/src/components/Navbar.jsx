import { useState } from "react";

const Navbar = () =>{
    
    return(
        <div className="flex justify-between text-white">
            <a href="#" className="flex">
                <img src="data:image/png;base64,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" alt="heart-with-pulse" className="w-8"/><p className="text-xl">Vitabase</p></a>
            <ul className="DESKTOP-MENU hidden lg:flex">
                <li>
                    <a href="#">My Appointments</a>
                </li>
                <li>
                    <a href="#">My Doctors</a>
                </li>
            </ul>
            
        </div>
    )
}

export default Navbar