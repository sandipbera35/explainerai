import httpx
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class OllamaConfig:

    def __init__(
        self,
        model_name: str
    ):

        self.model_name = model_name
        self.base_url = "http://localhost:11434"


class OllamaClient:

    def __init__(
        self,
        config: OllamaConfig
    ):

        self.config = config

    def explain_code(
    
        self,
        prompt: str
    ) -> str:

        url = f"{self.config.base_url}/api/chat"

        # payload = {
        #     "model": self.config.model_name,
        #     "stream": False,
        #     "messages": [
        #         {
        #             "role": "system",
        #             "content": (
        #                 "You are an expert software engineer and "
        #                 "code explanation assistant. "
        #                 "Explain code clearly with examples, "
        #                 "best practices, architecture insights, "
        #                 "and beginner-friendly breakdowns."
        #             )
        #         },
        #         {
        #             "role": "user",
        #             "content": prompt
        #         }
        #     ]
        # }
        payload = {
    "model": self.config.model_name,
    "stream": False,
    "messages": [
        {
            "role": "system",
            "content": (
                "You are an expert software engineer "
                "and code explanation assistant."
            )
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
}

        with httpx.Client() as client:

            response = client.post(
                url,
                json=payload,
                timeout=120
            )

        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            logger.error("HTTP error occurred: %s", e)
            logger.debug("Response content: %s", response.text)
            raise httpx.HTTPStatusError(
                f"Error from Ollama API: {e.response.status_code} - {e.response.text}",
                request=e.request,
                response=e.response
            ) from e

        data = response.json()

        logger.debug("API response: %s", data)

        return data["message"]["content"]
if __name__ == "__main__":
    # Test the OllamaClient with a sample prompt
    config = OllamaConfig(model_name="explainerai")
    client = OllamaClient(config=config)

    sample_prompt = "Explain the purpose of Python decorators."

    try:
        response = client.explain_code(prompt=sample_prompt)
        logger.info("Response from Ollama API: %s", response)
    except Exception as e:
        logger.error("An error occurred: %s", e)