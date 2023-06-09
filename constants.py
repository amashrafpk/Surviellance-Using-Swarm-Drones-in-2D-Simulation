"""
    CONSTANTS and tweakable parameters are defined here
"""
class Constants(object):

    # ------------------- MAP PARAMETERS ---------------------
    LENGTH = 50         # Map length
    WIDTH = 50          # Map width
    GEO_FENCE_WIDTH = 3 # Geo-fence width
    IN_AREA=WIDTH-GEO_FENCE_WIDTH

    # -------------------- UAV PARAMETERS --------------------
    NUM_UAVS = 4        # Num of total UAVs
    CONSTANT_VELOCITY = 4 # In meters per second
    W_MAX = 45      # Max heading angle change in degrees
    R_C = 15    # Communication range 
    R_S = 5    # Sensor-perception range
    
    # ----------- WEIGHTS for velocity parameters ------------
    K_O= 0.8    # Obstacle and neighbor avoidance
    K_C= 0.4    # Decentering
    K_S= 0.5    # Selfishness
    K_B= 0.1    # Boundary control
    K_W= 0.8    # Weight for Control input update

    # ---------------- FITNESS FUNCTION PARAM ----------------
    RHO= 0.2
    ALPHA= 0.04 # Weight for distance: UAV <--> point
    BETA= 0.01  # Weight for distance: previous_goal <--> point

    # ---------------- BOUNDARY CONTROL PARAM ----------------
    Q_M= 0.6    # Weight for center of mission area
    Q_B= 0.8    # Weight for nearest boundary point


    # ---------------- THRESHOLD SAFETY DISTANCE -------------
    # Distance threshold for s(z,d) function
    D_O = R_S   # For obstacle avoidance given an emergency situation
    D_N = 2     # For neighbor avoidance given an emergency situation
    D_C = 2*R_S # For decentering term --> neighbor avoidance threshold
                # Decentering value should take approximately 2*R_S (twice the sensor range)
  


    # =======================================================================================================
    #               SIMULATION PARAMETERS (Coverage mode, optimizations, failure simulations...)
    # =======================================================================================================

    TIME_STEP = 0.2 # In seconds
    OBSTACLE_VALUE = -40   # Specific value for marking obstacles in coverage map
    
    
    INTRUDER=True
    # INTRUDER MODE
    # boundary:an intruder appers near the boundry during a random time in simulation
    # ranom:an intruder appers any random position in the plot during a random time in simulation 
    ITR_MODE="boundary"
    
    # Minimum goal distance that must be ensured between agent goal and neighbor goal.
    # Again, this avoids both UAVs moving towards same uncovered areas.
    MIN_GOAL_DIST = R_S
    
    # This parameter will disable the maximum communication radius range. 
    # Therefore, if enabled, all UAVs will have information of all other UAVs coverage areas.
    # Result will be, obviously, more coherent and efficient; but less realistic 
    ALWAYS_COMMUNICATION = False


    # If enabled, drone failures will be simulated by decreasing the number of UAVs at defined iterations.
    SIMULATE_FAILURES = False

    # ---------------- FINAL CONDITION ----------------
    MAX_ITERATIONS = 10000    # Define the maximum iterations for covering area
    MAX_COVERAGE = 95       # Define the maximum coverage percentage
    


    # =======================================================================================================
    #                               PLOTTING AND DRAWING PARAMETERS
    # =======================================================================================================

    
    PLOTS = True                # Global var to disable all plots
    RESULTS_DIR = "results"         # Default directory to store the results
    FILE_NAME = "sim1"         # Default directory to store the results

    # If set to false will leave in blank corresponding plot 
    # (--> Disable for rapid testing: disabling plotting improves performance)
    TRAJECTORY_PLOT = True
    CUMULATIVE_PERCENTAGE = True
    INSTANTANEOUS_PERCENTAGE = True

    COVERAGE_FIRST = False  # True: Plots the coverage map only for the first UAV (red trajectory)
                            # False: Plots global temperature map

                  # Will output a video of the simulation (needs ffmpeg installed)
    
    CIRCLE_SENSOR = True       # Draw the Sensor Radius R_S circle in canvas
    CIRCLE_COMMUNICATION = False    # Draw the Communication Radius R_C circle in canvas


    # =======================================================================================================
    #                                  INITIAL UAVS DISTRIBUTIONS
    # =======================================================================================================

    # --> Only one must be enabled at the same time
    INIT_CIRCUMFERENCE = True     # UAVs circle init at center
    INIT_RANDOM = False           # UAVs random init at center
    INIT_LINE_UP = False           # UAVs init with upwards pointing line formation
    INIT_LINE_DOWN = False          # UAVs init with downwards pointing line formation
    INIT_LINE_INTERCHANGED = False # UAVs init with interchanged line formation
    
    # TODO: Not working
    INIT_CORNER = False             # UAVs init in left corner with random pos around R_S