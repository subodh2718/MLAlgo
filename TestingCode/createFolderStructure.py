import os

def create_folder_and_readme(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")
    
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write(f"# {os.path.basename(path)}\n\nThis folder contains information about {os.path.basename(path)} in the context of Machine Learning algorithms.")
        print(f"Created README.md in: {path}")
    else:
        print(f"README.md already exists in: {path}")

def create_ml_algorithms_folder_structure():
    structure = {
        "Supervised Learning": [
            "Linear Regression", "Logistic Regression", "Decision Trees",
            "Random Forests", "Support Vector Machines", "Neural Networks"
        ],
        "Unsupervised Learning": [
            "K-Means Clustering", "Hierarchical Clustering", "Principal Component Analysis",
            "Independent Component Analysis", "Autoencoders"
        ],
        "Semi-Supervised Learning": [
            "Self-Training", "Co-Training", "Generative Models"
        ],
        "Reinforcement Learning": {
            "Value-Based Methods": ["Q-Learning", "SARSA"],
            "Policy-Based Methods": ["Policy Gradients", "Actor-Critic"],
            "Model-Based Methods": ["Dyna", "Monte Carlo Tree Search"]
        },
        "Deep Learning": [
            "Convolutional Neural Networks", "Recurrent Neural Networks",
            "Long Short-Term Memory Networks", "Transformers",
            "Generative Adversarial Networks"
        ]
    }

    for category, items in structure.items():
        create_folder_and_readme(category)
        
        if isinstance(items, list):
            for item in items:
                create_folder_and_readme(os.path.join(category, item))
        elif isinstance(items, dict):
            for subcategory, subitems in items.items():
                subcategory_path = os.path.join(category, subcategory)
                create_folder_and_readme(subcategory_path)
                for subitem in subitems:
                    create_folder_and_readme(os.path.join(subcategory_path, subitem))

    print("Machine Learning Algorithms folder structure creation and README.md file addition completed!")

if __name__ == "__main__":
    create_ml_algorithms_folder_structure()