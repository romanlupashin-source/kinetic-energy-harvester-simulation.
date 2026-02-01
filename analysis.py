import numpy as np
import matplotlib.pyplot as plt

def generate_bio_simulation():
    # 1. Simulate Bio-Data (e.g., Stem Cell signal intensity)
    # Generating 100 data points with a baseline of 200
    ys = 200 + np.random.randn(100)
    x = [x for x in range(len(ys))]

    # 2. Create Visualization
    fig = plt.figure(figsize=(10, 6), facecolor='w')
    
    # Plot the signal line
    plt.plot(x, ys, '-', label='Signal Intensity', color='#2c3e50')
    
    # Highlight areas above threshold (simulating stress markers)
    threshold = 201.5
    plt.fill_between(x, ys, threshold, where=(ys > threshold), 
                     facecolor='#e74c3c', alpha=0.6, label='High Stress Marker')
    
    plt.title("Stem Cell Aging Marker Simulation", fontsize=14)
    plt.xlabel("Time (ms)")
    plt.ylabel("Signal Intensity (a.u.)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # 3. Save the result
    output_filename = "simulation_result.png"
    plt.savefig(output_filename)
    print(f"✅ Simulation complete. Chart saved to {output_filename}")
    plt.close(fig)

if __name__ == "__main__":
    generate_bio_simulation()
