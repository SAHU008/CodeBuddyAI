
import ast
import streamlit as st

st.set_page_config(
    page_title="CodeBuddy AI",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #121b32);
    color: #f1f5f9;
}
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}
.hero {
    padding: 28px;
    border-radius: 18px;
    background: linear-gradient(120deg, #173b68, #312e81);
    border: 1px solid #45638d;
    margin-bottom: 24px;
}
.hero h1 {
    color: white;
    font-size: 2.6rem;
}
.hero p {
    color: #dbeafe;
    font-size: 1.05rem;
}
div.stButton > button {
    background: #38bdf8;
    color: #07111f;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    padding: 0.65rem 1.2rem;
}
div.stButton > button:hover {
    background: #7dd3fc;
    color: #07111f;
}
.tip {
    background: #172554;
    border-left: 4px solid #38bdf8;
    padding: 14px;
    border-radius: 8px;
    margin-top: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("💻 CodeBuddy AI")
    st.caption("Your coding companion")
    st.divider()
    st.markdown("### 🧰 Tools")
    st.write("🐍 Python Syntax Checker")
    st.write("💡 Error Explanations")
    st.write("📘 Beginner Tips")
    st.divider()
    st.caption("Version 2.0 | Learning project")

# ---------- HEADER ----------
st.markdown("""
<div class="hero">
    <h1>💻 CodeBuddy AI</h1>
    <p>Your beginner-friendly Python coding assistant.</p>
    <p>Write code, check syntax, and learn from your mistakes.</p>
</div>
""", unsafe_allow_html=True)

# ---------- CODE INPUT ----------
left, right = st.columns([3, 2])

with left:
    st.subheader("⌨️ Python Code Editor")
    code = st.text_area(
        "Write or paste your Python code",
        height=280,
        placeholder='def greet():\n    print("Hello, developer!")',
        key="code_input"
    )

    check_clicked = st.button(
        "🔍 Check My Code",
        type="primary",
        use_container_width=True
    )

with right:
    st.subheader("📚 Quick Tips")
    st.markdown("""
    <div class="tip">
    <b>Tip 1</b><br>
    Use a colon (:) after if, for, while, and function definitions.
    </div>
    <div class="tip">
    <b>Tip 2</b><br>
    Keep indentation consistent. Python uses indentation to define blocks.
    </div>
    <div class="tip">
    <b>Tip 3</b><br>
    Match your opening and closing brackets and quotation marks.
    </div>
    """, unsafe_allow_html=True)

    st.info("This tool checks Python syntax. It does not execute submitted code.")

# ---------- ERROR EXPLANATIONS ----------
def explain_error(error):
    message = error.msg.lower()

    if "expected ':'" in message:
        return (
            "A colon is missing at the end of a statement.",
            "Add : after statements such as if, for, while, or def."
        )

    if "was never closed" in message:
        return (
            "A bracket or parenthesis was opened but not closed.",
            "Check that every (, [, or { has a matching closing symbol."
        )

    if "unexpected indent" in message:
        return (
            "A line has indentation where Python does not expect it.",
            "Remove unnecessary spaces at the start of the line."
        )

    if "unindent does not match" in message:
        return (
            "The indentation does not match the surrounding code.",
            "Use consistent indentation, preferably four spaces per level."
        )

    if "unterminated string literal" in message:
        return (
            "A text string may be missing its closing quotation mark.",
            "Check that every opening quote has a matching closing quote."
        )

    if "invalid syntax" in message:
        return (
            "Python found invalid syntax near the reported line.",
            "Check operators, colons, parentheses, quotation marks, and spelling."
        )

    return (
        "Python could not parse this code.",
        "Review the reported line and check the syntax around it."
    )

# ---------- RESULTS ----------
if check_clicked:
    st.divider()
    st.subheader("📊 Code Analysis")

    if not code.strip():
        st.warning("Please enter some Python code before checking.")

    else:
        try:
            ast.parse(code)
            st.success("✅ No Python syntax errors found!")
            st.markdown("### 🎉 Great work!")
            st.write(
                "Your code passed the syntax check. "
                "Remember, syntax correctness does not guarantee "
                "that your program will run without errors."
            )

        except SyntaxError as error:
            title, suggestion = explain_error(error)

            st.error("❌ Syntax error detected")
            st.write(f"**Problem:** {title}")
            st.write(f"**Python message:** {error.msg}")

            if error.lineno is not None:
                st.write(f"**Line number:** {error.lineno}")

            st.markdown("### 💡 How to fix it")
            st.write(suggestion)

            st.caption(
                "CodeBuddy AI provides basic syntax guidance. "
                "Always review suggested fixes before using them."
            )

st.divider()
st.caption("Made with Python and Streamlit | CodeBuddy AI")
