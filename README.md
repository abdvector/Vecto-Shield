# Vecto Shield: Intelligent Autonomous Vector Control System


![Release](https://img.shields.io/badge/Release-v1.0.0-007ec6?style=flat) ![Streamlit](https://img.shields.io/badge/Streamlit-Ready-ff4b4b?style=flat) ![Python](https://img.shields.io/badge/Python-3.9%2B-007ec6?style=flat) ![License](https://img.shields.io/badge/License-MIT-97ca00?style=flat)

**Vecto Shield** is a proactive "Predict & Prevent" enterprise-grade system designed to combat vector-borne diseases (like Dengue and Malaria) in urban environments. By bridging the gap between technological capability and social equity, this system transitions municipal operations from inefficient *Reactive Logistics* (chasing cases after an outbreak) to intelligent *Predictive Logistics*.

---

##  The Project
Vecto Shield integrates **Satellite Meteorology, Machine Learning, and Swarm Intelligence** into a unified autonomous framework:
1. **Predictive Engine (AI)**: A Random Forest Regressor analyzes micro-climatic precursors (temperature, humidity, rainfall) to predict outbreaks with a **14-day biological lead time**.
2. **Action Engine (Swarm Robotics)**: If critical risk is detected, a Multi-Squadron **Particle Swarm Optimization (PSO)** algorithm mathematically calculates the most efficient flight paths for drone fleets to neutralize high-risk breeding clusters.

##  Why It Matters
Current municipal strategies rely on blind "Blanket Fogging" only *after* clinical cases reach hospitals. This results in wasted resources and preventable mortality. 
Vecto Shield introduces a **"Gatekeeper Architecture"**:
- **Socio-Economic Impact**: By grounding drone fleets during low-risk climatic windows, municipalities can reduce fuel and operational expenditures (OPEX) by **up to 60%**.
- **Equitable Health**: Ensures marginalized, high-density communities receive immediate, precision-targeted protection before an outbreak spreads.

---

## System Workflow
The application is deployed via a highly interactive, 3-tier Streamlit Dashboard:

1. **Tab 1: Predicted Hotspots**: Displays a Live Risk Heatmap of the city. (Currently illustrating **Patna City** as an example deployment). Highlights current weather conditions and the Top 5 high-risk clusters.
2. **Tab 2: Drone Operations**: A real-time visual simulation of the PSO metaheuristic. Watch autonomous drone squadrons optimize their flight paths and converge on infected clusters using minimal fuel.
3. **Tab 3: Analytics Dashboard**: Deep-dive epidemiological data including:
   - **Model Accuracy**: Actual vs Predicted case scatter plots.
   - **Vector Ecology**: Visual proof of the biological 14-Day Extrinsic Incubation Period (EIP) lag between rainfall spikes and outbreaks.
   - **The "Kill Zone"**: A heatmap defining the exact temperature/humidity conditions where breeding accelerates exponentially.

---

## How to Get Started

### Prerequisites
- Python 3.9+
- `pip` package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/vecto-shield.git
   cd vecto-shield
   ```
2. Install dependencies:
   ```bash
   pip install streamlit pandas numpy plotly pydeck scikit-learn
   ```
3. Run the Dashboard:
   ```bash
   streamlit run app.py
   ```
4. Open the provided `localhost` URL in your web browser.

---

##  Assumptions & Technical Constraints
- **Simulation Scope**: The current UI visually simulates Patna City. The GPS coordinates for the map center and drone base station are hardcoded for this illustrative purpose.
- **Drone Physics**: The Swarm Simulator assumes a flat 2D geographic plane for velocity calculations (altitude is abstracted).
- **Data Availability**: The AI assumes historical epidemiological ground truth is accurately reported by municipal hospitals without heavy data skew.

## Key Findings
- **High Accuracy**: The Random Forest model achieved an $R^2$ accuracy exceeding 0.95 on unseen test data.
- **Biological Validation**: The AI successfully learned and captured the 14-day Extrinsic Incubation Period (EIP) natively, without explicit hardcoding.
- **Swarm Efficiency**: The niching strategy in the PSO algorithm effectively solved the Vehicle Routing Problem (VRP), preventing premature convergence and ensuring all target hotspots are covered.

##  Scalability & Expansion 🌐
Vecto Shield is inherently modular and **highly scalable**. 
While currently illustrating Patna, the system can be instantly expanded to **any municipality globally**. 
- **Ease of Scaling**: Simply replace the `.csv` files in the `/Data` directory with local NASA POWER API weather data and local hospital records. The Machine Learning model dynamically retrains itself to learn the specific micro-climatic nuances of the new geography.
- **Future Expansion**: The backend can easily be expanded to integrate live IoT weather sensors, traffic routing for ground-based trucks, or computer vision for analyzing drone camera feeds.
