import pandas as pd

data = {
    'workout': [
        'Cardio', 'Strength Training', 'Yoga', 'HIIT', 'Pilates', 'CrossFit', 'Swimming', 
        'Cycling', 'Running', 'Boxing', 'Dance', 'Stretching', 'Rowing', 'Jump Rope',
        'Walking', 'Climbing', 'Bodyweight Exercises', 'Resistance Band Training', 'Aerobics', 'Powerlifting'
    ],
    'min_fitness_level': [
        3, 5, 2, 6, 4, 7, 3, 5, 4, 6, 3, 1, 5, 4, 1, 7, 2, 3, 3, 8
    ],  # Fitness level 1-10
    'requires_equipment': [
        False, True, False, True, True, True, True, True, False, True, False, False, True, False, 
        False, True, False, True, False, True
    ],
    'duration': [
        30, 45, 60, 20, 50, 60, 45, 60, 30, 60, 45, 15, 30, 15, 30, 60, 25, 40, 30, 90
    ],  # Duration in minutes
    'intensity': [
        'Moderate', 'High', 'Low', 'High', 'Moderate', 'High', 'Moderate', 'High', 'High', 'High', 
        'Moderate', 'Low', 'Moderate', 'High', 'Low', 'High', 'Moderate', 'Moderate', 'Moderate', 'High'
    ],
    'goal': [
        'Endurance', 'Strength', 'Flexibility', 'Endurance', 'Flexibility', 'Strength', 'Endurance',
        'Endurance', 'Endurance', 'Strength', 'Endurance', 'Flexibility', 'Endurance', 'Endurance', 
        'Endurance', 'Strength', 'Strength', 'Strength', 'Endurance', 'Strength'
    ],
    'calories_burned': [
        300, 600, 200, 800, 400, 700, 500, 600, 400, 700, 350, 150, 400, 200, 200, 600, 250, 500, 400, 1000
    ]
}

df = pd.DataFrame(data)


def recommend_workout(df, user_input):
    user_goal = user_input['goal'].capitalize()
    
    matching_workouts = df[
        (df['min_fitness_level'] <= user_input['fitness_level']) &
        (df['requires_equipment'] == user_input['has_equipment']) &
        (df['duration'] <= user_input['available_time']) &
        (df['goal'] == user_goal)
    ]

    if not matching_workouts.empty:
        print("\nBased on your input, the recommended workouts are:\n")
        print(matching_workouts[['workout', 'duration', 'intensity', 'calories_burned']])
    else:
        print("No workouts match your current requirements. Please adjust your input or goals.")

user_input = {
    'fitness_level': int(input("Enter your fitness level (1-10): ")),
    'has_equipment': input("Do you have access to gym equipment? (yes/no): ").lower() == 'yes',
    'available_time': int(input("Enter available workout time in minutes: ")),
    'goal': input("What is your fitness goal? (Endurance/Strength/Flexibility): ")
}

recommend_workout(df, user_input)
#df=pd.DataFrame(recommend_workout)