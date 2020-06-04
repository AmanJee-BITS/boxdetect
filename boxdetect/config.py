# parameters
min_w, max_w = (40, 50)
min_h, max_h = (50, 60)
wh_ratio_range = (0.65, 0.1)
scaling_factors = [0.5, 0.7]
padding = 1

# drawing rectangles
thickness = 2

# image enhancement
dilation_kernel = (2, 2)
dilation_iterations = 2

# rectangles grouping
group_size_range = (2, 100)  # minimum number of rectangles in a group, >2 - will ignore groups with single rect  # NOQA E501
vertical_max_distance = min_h * 0.3  # in pixels
# multiplier to be used with mean width of all the rectangles detected
# e.g. for multiplier of 4 the maximum distance between boxes to be grouped together will be:  # NOQA E501
# max_horizontal_distance = np.mean(all_rect_widths) * 4
horizontal_max_distance_multiplier = 4
