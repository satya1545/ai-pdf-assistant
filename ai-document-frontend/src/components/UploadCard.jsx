import { useState } from "react";
import api from "../services/api";

function UploadCard() {

    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);

    const uploadPDF = async () => {

        console.log(file);

        if (!file) {
            alert("Please select a PDF.");
            return;
        }

        const formData = new FormData();

        formData.append("file", file);

        try {

            const token = localStorage.getItem("token");

            const response = await api.post(
                "/upload/pdf",
                formData,
                {
                    headers: {
                        Authorization: `Bearer ${token}`
                    }
                }
            );

            alert(response.data.message);

        } catch (error) {

            console.log(error);

            console.log(error.response);

            if (error.response) {
                console.log(error.response.data);
            }

            alert("Upload Failed");

        }

    };

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-bold mb-4">
                Upload PDF
            </h2>

            <input
                type="file"
                accept=".pdf"
                onChange={(e) => {

                    const selectedFile = e.target.files[0];

                    console.log(selectedFile);

                    setFile(selectedFile);

                }}
            />

            <button
            onClick={uploadPDF}
            disabled={loading}
            className="w-full bg-blue-600 text-white rounded-lg py-2 hover:bg-blue-700"
        >

            {loading ? "Uploading..." : "📤 Upload PDF"}

            </button>

        </div>

    );

}

export default UploadCard;