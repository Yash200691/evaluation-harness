from unittest.mock import MagicMock, patch

from agent.llm_client import LLMClient


def test_generate_text_response(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "fake-api-key")
    monkeypatch.setenv("MODEL_NAME_A", "test-model")

    # Replace the real Groq client with a mock
    with patch("agent.llm_client.Groq") as mock_groq:
        # Create the fake assistant message
        expected_message = MagicMock()
        expected_message.content = "I found three laptops."

        # Create a fake Groq response
        fake_response = MagicMock()
        fake_response.choices[0].message = expected_message

        # Configure the mock client to return our fake response
        mock_groq.return_value.chat.completions.create.return_value = (
            fake_response
        )

        # Initialize LLMClient; it receives the mocked Groq client
        llm = LLMClient()

        messages = [
            {
                "role": "user",
                "content": "Find laptops under ₹60,000."
            }
        ]

        # Call the method under test
        result = llm.generate(messages)

        # Verify the returned message
        assert result.content == "I found three laptops."

        # Verify the API method was called correctly
        llm.client.chat.completions.create.assert_called_once_with(
            model="test-model",
            messages=messages,
            tools=None
        )

def test_generate_tool_call(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "fake-api-key")
    monkeypatch.setenv("MODEL_NAME_A", "test-model")

    with patch("agent.llm_client.Groq") as mock_groq:
        # Simulate a tool call from the LLM
        tool_call = MagicMock()
        tool_call.id = "call_123"
        tool_call.function.name = "search_products"
        tool_call.function.arguments = (
            '{"category": "laptop", "max_price": 60000}'
        )

        expected_message = MagicMock()
        expected_message.content = None
        expected_message.tool_calls = [tool_call]

        # Simulate the Groq response
        fake_response = MagicMock()
        fake_response.choices[0].message = expected_message

        mock_groq.return_value.chat.completions.create.return_value = (
            fake_response
        )

        llm = LLMClient()

        messages = [
            {
                "role": "user",
                "content": "Find laptops under ₹60,000."
            }
        ]

        tools = [
            {
                "type": "function",
                "function": {
                    "name": "search_products",
                    "description": "Search the product catalog",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "category": {"type": "string"},
                            "max_price": {"type": "number"}
                        }
                    }
                }
            }
        ]

        result = llm.generate(messages, tools)

        # Verify the returned tool call
        assert result.tool_calls[0].function.name == "search_products"
        assert result.tool_calls[0].id == "call_123"

        # Verify the arguments passed to Groq
        llm.client.chat.completions.create.assert_called_once_with(
            model="test-model",
            messages=messages,
            tools=tools,
        )