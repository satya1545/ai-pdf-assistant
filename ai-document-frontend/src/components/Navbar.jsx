import { useNavigate } from "react-router-dom";

function Navbar() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.removeItem("token");

        navigate("/");

    };

    return (

        <nav className="bg-white shadow">

            <div className="max-w-7xl mx-auto px-8 py-4 flex justify-between items-center">

                <h1 className="text-2xl font-bold text-blue-600">
                    AI Document Assistant
                </h1>

                <button
                    onClick={logout}
                    className="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg"
                >
                    Logout
                </button>

            </div>

        </nav>

    );

}

export default Navbar;