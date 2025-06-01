import os
from anthropic import Anthropic
from typing import List, Dict

class ClaudeAPI:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is required")
        
        self.client = Anthropic(api_key=self.api_key)
        self.model = "claude-3-5-sonnet-20241022"
    
    def send_message(self, message: str, conversation_history: List[Dict] = None) -> str:
        try:
            messages = conversation_history or []
            messages.append({
                "role": "user",
                "content": message
            })
            
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                messages=messages
            )
            
            return response.content[0].text
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_conversation_format(self, user_message: str, assistant_message: str) -> List[Dict]:
        return [
            {"role": "user", "content": user_message},
            {"role": "assistant", "content": assistant_message}
        ]