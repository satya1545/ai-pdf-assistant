import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

function Login() {

    const navigate = useNavigate();

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const loginUser = async () => {

        try {

            const formData = new URLSearchParams();

            formData.append("username", email);
            formData.append("password", password);

            const response = await api.post(
                "/auth/login",
                formData,
                {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                }
            );

            localStorage.setItem(
                "token",
                response.data.access_token
            );
 

            navigate("/dashboard");

        } catch (error) {

            console.log(error);

            alert("Invalid Email or Password");

        }

    };

    return (

        <div className="min-h-screen bg-slate-100 flex items-center justify-center">

            <div className="bg-white shadow-lg rounded-xl p-8 w-full max-w-md">

                <h1 className="text-3xl font-bold text-center text-blue-600">
                    AI Document Assistant
                </h1>

                <p className="text-center text-gray-500 mt-2 mb-8">
                    Welcome Back
                </p>

                <div className="mb-4">

                    <label className="block mb-2">
                        Email
                    </label>

                    <input
                        type="email"
                        placeholder="Enter Email"
                        className="w-full border rounded-lg p-3"
                        value={email}
                        onChange={(e) =>
                            setEmail(e.target.value)
                        }
                    />

                </div>

                <div className="mb-6">

                    <label className="block mb-2">
                        Password
                    </label>

                    <input
                        type="password"
                        placeholder="Enter Password"
                        className="w-full border rounded-lg p-3"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                    />

                </div>

                <button
                    onClick={loginUser}
                    className="w-full bg-blue-600 text-white rounded-lg py-3 hover:bg-blue-700"
                >
                    Login
                </button>

            </div>

        </div>

    );

}

export default Login;