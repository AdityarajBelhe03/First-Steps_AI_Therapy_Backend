class OpenRouterLlamaScout(BaseChatModel):
    openai_api_key: str
    temperature: float = 0.2
    max_tokens: int = 500
    top_p: float = 0.8
    frequency_penalty: float = 0.4
    presence_penalty: float = 0.3
    model_name: str = "meta-llama/llama-4-scout-17b-16e-instruct"

    @property
    def _llm_type(self) -> str:
        return "openrouter_llama_scout"

    def _generate(self, messages: list[BaseMessage], stop: list[str] | None = None, **kwargs: any) -> ChatResult:
        client = OpenAI(
            api_key=self.openai_api_key,
            base_url="https://openrouter.ai/api/v1"
        )
        openai_messages = []
        for message in messages:
            if isinstance(message, HumanMessage):
                openai_messages.append({"role": "user", "content": message.content})
            elif isinstance(message, AIMessage):
                openai_messages.append({"role": "assistant", "content": message.content})
            else:
                raise ValueError(f"Unsupported message type: {type(message)}")

        response = client.chat.completions.create(
            model=self.model_name,
            messages=openai_messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            stop=stop,
            **kwargs
        )
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=response.choices[0].message.content))])

# 🧠 Initialize LLM
llama_scout_llm = OpenRouterLlamaScout(
    openai_api_key="Put your API Key here"
)
