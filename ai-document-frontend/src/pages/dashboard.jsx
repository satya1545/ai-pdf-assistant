import Navbar from "../components/Navbar";
import UploadCard from "../components/UploadCard";
import DocumentsCard from "../components/DocumentsCard";
import ChatCard from "../components/ChatCard";

function Dashboard() {

    return (

        <div className="min-h-screen bg-gray-100">

            <Navbar />

            <div className="max-w-7xl mx-auto p-8">

                <h1 className="text-4xl font-bold">
                    AI Document Assistant
                </h1>

                <p className="text-gray-600 mt-2">
                    Upload PDFs and chat with your documents using Gemini AI.
                </p>

                <div className="grid lg:grid-cols-2 gap-8 mt-8">

                    <UploadCard />

                    <DocumentsCard />

                </div>

                <div className="mt-8">

                    <ChatCard />

                </div>

            </div>

        </div>

    );

}

export default Dashboard;