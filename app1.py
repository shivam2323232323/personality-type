import streamlit as st
from collections import Counter
import random

def main():
    st.title("Personality Type Assessment")
    
    # Step 1: User Name Input
    if "user_name" not in st.session_state:
        st.session_state["user_name"] = None
    
    if st.session_state["user_name"] is None:
        st.session_state["user_name"] = st.text_input("Enter your name to begin:")
        if st.session_state["user_name"]:
            st.experimental_rerun()
        return
    
    st.write(f"Welcome, {st.session_state['user_name']}!")
    
    # Step 2: Personality Traits Selection
    personality_traits = {
        "Red": ["Aggressive", "Ambitious", "Strong-willed", "Goal-oriented", "Pushing", "Problem-solver", "Pioneer", "Decisive", "Innovator", "Impatient", "Controlling", "Convincing", "Performance-oriented", "Powerful", "Results-oriented", "Initiator", "Speed", "Timekeeper", "Intense", "Opinionated", "Straightforward", "Independent"],
        "Yellow": ["Talkative", "Enthusiastic", "Persuasive", "Creative", "Optimistic", "Social", "Spontaneous", "Expressive", "Charming", "Full of vitality", "Self-centered", "Sensitive", "Adaptable", "Inspiring", "Needs attention", "Encouraging", "Communicative", "Flexible", "Open", "Sociable", "Imaginative", "Easygoing"],
        "Green": ["Patient", "Relaxed", "Self-controlled", "Reliable", "Composed", "Loyal", "Modest", "Understanding", "Lengthy", "Stable", "Prudent", "Discreet", "Supportive", "Good listener", "Helpful", "Producer", "Persistent", "Reluctant", "Thoughtful", "Conceals feelings", "Considerate", "Kind"],
        "Blue": ["Conscientious", "Systematic", "Distant", "Correct", "Conventional", "Seems insecure", "Objective", "Structured", "Analytical", "Perfectionist", "Needs time", "Reflecting", "Methodical", "Seeks facts", "Quality-oriented", "Scrutinizes", "Follows rules", "Logical", "Questioning", "Meticulous", "Reserved"]
    }
    
    all_traits = {trait: category for category, traits in personality_traits.items() for trait in traits}
    shuffled_traits = list(all_traits.keys())
    
    if "shuffled_traits" not in st.session_state:
        st.session_state["shuffled_traits"] = random.sample(shuffled_traits, len(shuffled_traits))
    
    st.subheader("Select the traits that best describe you:")
    selected_traits = st.multiselect("Choose your traits", st.session_state["shuffled_traits"], key="selected_traits")
    
    if st.button("Determine Personality Type"):
        category_count = Counter()
        
        for trait in selected_traits:
            category_count[all_traits[trait]] += 1
        
        total_weight = sum(category_count.values())
        personality_percentages = {ptype: (count / total_weight) * 100 for ptype, count in category_count.items()}
        
        st.subheader("Personality Contribution:")
        for ptype, percent in sorted(personality_percentages.items(), key=lambda x: x[1], reverse=True):
            st.write(f"{ptype}: {percent:.1f}%")
    
    st.subheader("Your assessment is saved!")
    st.write("Refresh to assess again or try for someone else.")
    
if __name__ == "__main__":
    main()
