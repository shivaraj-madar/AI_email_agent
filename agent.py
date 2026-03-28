import os
import sys

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import build_resource_service, get_gmail_credentials
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.utils import build_resource_service, get_gmail_credentials
from langchain_community.tools.gmail.utils import build_resource_service, get_gmail_credentials
from langchain_community.tools.gmail import GmailCreateDraft, GmailSendMessage
# 1. FIX ENCODING: Prevents the '0x92' / 'utf-8' crash in your terminal
sys.stdout.reconfigure(encoding='utf-8')


# 1. Setup API Keyimport os
from langchain_groq import ChatGroq
from langchain_community.agent_toolkits import GmailToolkit
from langchain_classic.agents import AgentExecutor, create_structured_chat_agent
from langchain_classic import hub


# 1. Manually check what tools are being loaded
toolkit = GmailToolkit()
all_tools = toolkit.get_tools()

# 2. Print them once just to be 100% sure they are there
print("Available Tools:", [tool.name for tool in all_tools])

# 3. If 'update_gmail_message_labels' or 'create_gmail_label' is missing,
# it's a Scope issue. If they ARE there, the agent is just being lazy.

from dotenv import load_dotenv
load_dotenv() # This loads the key from a hidden .env file

# Now the code looks for the key in your system, not the file
os.environ.get("GROQ_API_KEY")

# Change your SCOPES to this:
SCOPES = ["https://mail.google.com/"]

# 4. INITIALIZE GMAIL (Updated for 2026)
# This will create 'token.json' automatically if it doesn't exist
credentials = get_gmail_credentials(
    client_secrets_file="credentials.json",
    scopes=SCOPES
)
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)
tools = toolkit.get_tools()

print("--- REFRESHED TOOLS LIST ---")
print([tool.name for tool in tools])

# 5. REST OF THE AGENT LOGIC
llm = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)

prompt = hub.pull("hwchase17/structured-chat-agent")

agent = create_structured_chat_agent(llm, tools, prompt)

agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True,
    max_iterations=15   # Increased to allow for multi-step sequences
)

if __name__ == "__main__":
    print("--- Light-Weight Manager Online ---")
    
    # We tell the agent specifically NOT to fetch the full body
    query = """
    1. Use 'search_gmail' to find the 2 most recent unread emails from LinkedIn.
    2. Look ONLY at the 'snippet' and 'subject' provided by the search results. 
    3. Do NOT call 'get_gmail_message' or 'get_gmail_thread' (they are too large).
    4. Summarize the 2 emails based only on those snippets.
    5. If they look like spam, just tell me 'Suggesting Delete' for those IDs.
    """
    
    try:
        agent_executor.invoke({"input": query})
    except Exception as e:
        print(f"Agent Error: {e}")