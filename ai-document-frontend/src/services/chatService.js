
import api from "./api";

export const askQuestion = async (question) => {

    const response = await api.get(
        "/chat/",
        {
            params: {
                question
            }
        }
    );

    return response.data;

};