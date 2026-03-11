A simple Flask app for the dashboard (or we can use Next.js as per the plan, but for simplicity in Python, we might use Flask or Streamlit). However, the plan says Next.js with Tailwind. We are to use Firebase SDK for real-time updates. We can create a simple Flask app that serves static files and uses Firebase SDK on the frontend. Alternatively, we can create a separate Next.js project. Since the mission is about the agent, and the dashboard is a separate component, we can create a minimal Flask app for now and then build a more sophisticated one later.

Given the complexity and the fact that we are in Phase 1, let's focus on the agent and the sensors, and set up the Firebase.

We must also note that we are to use Firebase-admin, so we need a service account key. We will assume that we have a service account key file.

We are to structure the code in a way that is robust and follows best practices.

Let's start by creating the Firebase setup.

Note: We are not actually creating the Firebase project via code (that requires human interaction). We will assume the project is created and we have the service account key.

We are to write code that initializes the Firebase app and sets up the Firestore.

We are to create the collections if they don't exist. However, Firestore is schema-less, so we don't need to create collections explicitly. We just need to define the structure of the documents we will store.

We are to design the document structure as per the plan.

We are to create the following collections:
- agent_state
- telemetry_events
- strategy_genomes
- trade_history

We are to create the core agent that will run a loop, fetch data, make decisions, and execute trades.

We are to implement a basic strategy. The plan mentions a target DEX (Uniswap v3 on Polygon). We can start with a simple strategy, like arbitrage between two DEXes, or a simple market making strategy.

However, for Phase 1, we are just setting up the skeleton. We can implement a placeholder strategy that logs and does nothing.

We are to implement error handling and logging.

We are to use environment variables for sensitive information.

Let's create the files step by step.

First, let's create the .env.example file.