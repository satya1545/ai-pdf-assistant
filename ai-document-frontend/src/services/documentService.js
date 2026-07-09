import api from "./api";

const token = () => localStorage.getItem("token");

export const getDocuments = async () => {

    const response = await api.get("/documents", {
        headers: {
            Authorization: `Bearer ${token()}`
        }
    });

    return response.data;
};

export const deleteDocument = async (documentId) => {

    const response = await api.delete(
        `/documents/${documentId}`,
        {
            headers: {
                Authorization: `Bearer ${token()}`
            }
        }
    );

    return response.data;
};