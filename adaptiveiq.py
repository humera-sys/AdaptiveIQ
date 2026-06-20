# ============================================
# AdaptiveIQ - Smart Learning Agent
# A learning buddy that adapts to you
# ============================================

from kaggle_secrets import UserSecretsClient
from google import genai
import time
from datetime import datetime

# get API key safely from secrets
secret = UserSecretsClient()
api_key = secret.get_secret("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# all sessions stored in memory
all_sessions = []

# small pause between calls to avoid hitting limits
def safe_generate(prompt):
    time.sleep(3)
    result = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return result.text

# ── Agent 1: figures out how the student is feeling ──
def check_student_mood(student_input, response_time_seconds):
    prompt = f"""
    A student is learning and gave this response: "{student_input}"
    They took {response_time_seconds} seconds to answer.

    Based on this, decide how the student is feeling right now.
    Choose only one: confused / focused / bored / frustrated

    Reply in this exact format:
    State: [one word]
    Reason: [one short sentence]
    """
    return safe_generate(prompt)

# ── Agent 2: decides what to do next based on mood ──
def decide_next_step(mood, topic):
    prompt = f"""
    A student learning about "{topic}" is currently feeling: {mood}

    Decide what the teacher should do next.
    Choose one action: simplify / encourage / increase_difficulty / suggest_break

    Reply in this exact format:
    Action: [one word]
    Message: [one warm, friendly sentence to say to the student]
    """
    return safe_generate(prompt)

# ── Agent 3: explains the topic based on the action ──
def explain_topic(topic, action):
    prompt = f"""
    A student is learning about "{topic}".
    The recommended action is: {action}

    Write a short, friendly explanation of "{topic}" that fits the action.
    Keep it under 5 sentences. Use simple words. Be encouraging.
    """
    return safe_generate(prompt)

# ── Safety filter: keeps topics appropriate ──
def is_safe_topic(topic):
    banned = ["hack", "weapon", "drug", "violence", "adult"]
    for word in banned:
        if word.lower() in topic.lower():
            print("⚠️ Sorry, that topic isn't available. Please choose an educational topic!")
            return False
    return True

# ── Session tracker: remembers what happened ──
def save_session(topic, session_log):
    session = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "topic": topic,
        "rounds": len(session_log),
        "moods": [entry["mood"].split("\n")[0] for entry in session_log],
        "actions": [entry["action"] for entry in session_log]
    }
    all_sessions.append(session)
    print(f"\n💾 Session saved! Total sessions so far: {len(all_sessions)}")
    return session

def show_history():
    if not all_sessions:
        print("No sessions yet!")
        return
    print("\n📊 Your Learning History:")
    print("=" * 40)
    for s in all_sessions:
        print(f"\n📅 {s['date']}")
        print(f"📖 Topic: {s['topic']}")
        print(f"🔄 Rounds completed: {s['rounds']}")
        print(f"😊 Moods detected: {', '.join(s['moods'])}")
        print(f"🎯 Actions taken: {', '.join(s['actions'])}")

# ── Main session: puts it all together ──
def run_adaptiveiq():
    print("=" * 50)
    print("       Welcome to AdaptiveIQ 🌱")
    print("  Your personal smart learning buddy")
    print("=" * 50)

    topic = input("\nWhat topic are you studying today? ")

    # safety check first
    if not is_safe_topic(topic):
        return

    print(f"\nGreat! Let's learn about {topic} together.\n")

    session_log = []

    for round_num in range(1, 4):
        print(f"\n--- Round {round_num} ---")

        question = safe_generate(
            f"Ask one simple question about {topic} for a student. Just the question, nothing else."
        )
        print(f"\n📝 Question: {question}")

        start = time.time()
        student_answer = input("Your answer: ")
        response_time = round(time.time() - start)

        print("\n🔍 Checking how you're feeling...")
        mood = check_student_mood(student_answer, response_time)
        print(mood)

        print("\n🧭 Adapting to you...")
        next_step = decide_next_step(mood, topic)
        print(next_step)

        action_word = "simplify"
        for line in next_step.split("\n"):
            if line.startswith("Action:"):
                action_word = line.replace("Action:", "").strip()

        print("\n📚 Here's what I want you to know...")
        explanation = explain_topic(topic, action_word)
        print(explanation)

        session_log.append({
            "round": round_num,
            "answer": student_answer,
            "mood": mood,
            "action": action_word
        })

        print("\n" + "-" * 50)

    save_session(topic, session_log)

    print("\n✅ Session Complete!")
    print(f"You completed 3 rounds on: {topic}")
    print("\nYour session summary:\n")
    for entry in session_log:
        lines = entry['mood'].split("\n")
        state = lines[0] if lines else "engaged"
        print(f"  Round {entry['round']}: {state} → AdaptiveIQ chose to {entry['action']}")
    print("\nKeep learning, you're doing amazing! 🌟")

    print("\n")
    show_history()

run_adaptiveiq()
