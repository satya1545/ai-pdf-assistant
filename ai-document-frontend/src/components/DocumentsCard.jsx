import { useEffect, useState } from "react";
import {
    getDocuments,
    deleteDocument
} from "../services/documentService";

function DocumentsCard() {

    const [documents, setDocuments] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetchDocuments();
    }, []);

    const fetchDocuments = async () => {

        try {

            const data = await getDocuments();

            setDocuments(data);

        } catch (error) {

            console.log(error);

        } finally {

            setLoading(false);

        }

    };

    const handleDelete = async (id) => {

        const confirmDelete = window.confirm(
            "Delete this document?"
        );

        if (!confirmDelete) return;

        try {

            await deleteDocument(id);

            setDocuments(
                documents.filter(doc => doc.id !== id)
            );

            alert("Document Deleted");

        } catch (error) {

            console.log(error);

            alert("Delete Failed");

        }

    };

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-bold mb-4">
                My Documents ({documents.length})
            </h2>

            {
                loading ?

                    <p>Loading...</p>

                    :

                    documents.length === 0 ?

                        <p>No documents uploaded.</p>

                        :

                        <div className="space-y-3 max-h-[450px] overflow-y-auto">

                            {

                                documents.map((doc) => (

                                    <div
                                        key={doc.id}
                                        className="border rounded-lg p-4 hover:bg-gray-50"
                                    >

                                        <h3 className="font-semibold text-lg">
                                            📄 {doc.filename}
                                        </h3>

                                        <p className="text-sm text-gray-500">
                                            Chunks : {doc.total_chunks}
                                        </p>

                                        <button
                                            onClick={() => handleDelete(doc.id)}
                                            className="mt-3 bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded"
                                        >
                                            🗑 Delete
                                        </button>

                                    </div>

                                ))

                            }

                        </div>

            }

        </div>

    );

}

export default DocumentsCard;