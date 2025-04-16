from gymnasium import Environment
from gymnasium.spaces import Sequence, Box, Dict
import numpy as np
from ..common.listings import listings_df, column_name_to_index


class Environment(Environment):
    def __init__(self, current_listing):
        """ Creates an environment
        """
        # The number of components in a listing vector
        n_components = listings_df.to_numpy().shape[1]

        # Set up indices for different vector components
        self.n_beds_index = column_name_to_index['n_beds']
        self.price_index = column_name_to_index['price']
        self.latitude_index = column_name_to_index['latitude']
        self.longitude_index = column_name_to_index['longitude']
        self.offering_type_indices = [key for key in column_name_to_index.keys() if key.startswith('offering_type')]

        # Store the current listing and list of available listings
        self._current_listing = current_listing
        self._available_listings = listings_df.to_numpy()

        # Define the observation space
        self._observation_space = Dict({
            "current_listing": Box(shape=(n_components, ), dtype=float),
            "available_listings": Sequence(Box(shape=(n_components, ), dtype=float), seed=42)
        })

        # Define the action space
        # Each listing is an action that can be taken as well
        self._action_space = Box(shape=(n_components,), dtype=float)

        # Define the rewards
        self._rewards = {
            'click': 5,
            'ignore': -1,
        }


    def _get_obs(self):
        return { "current_listing": self._current_listing, "available_listings": self._available_listings }
    

    def _get_info(self):
        return {}
    

    def reset(self, seed, options):
        # Reset the numpy seed by calling the reset method of the base class
        super().reset(seed=seed)

        # Randomly select a listing and set is as the current listing
        self._current_listing = np.random.choice(self._available_listings)

        # Create and return the new observation and information
        observation = self._get_obs()
        info = self._get_info()

        return observation, info


    def _simulate_user_response(self, suggestion):
        # Ideally, this function would prompt the user to make a decision, but for
        # this assignment, it will only simulate a user making a decision by following
        # the thought process detailed below

        # If the property's offering is not the same, the suggestion will be ignored
        for offering_type_index in self.offering_type_indices:
            if self._current_listing[offering_type_index] != suggestion[offering_type_index]:
                return 'ignore'
        
        # If the number of bedrooms on the suggestion is less than the number of bedrooms
        # on the current listing, we ignore
        if suggestion[self.n_beds_index] < self._current_listing[self.n_beds_index]:
            return 'ignore'
        
        # Define the different price thresholds
        twenty_price_threshold = self._current_listing[self.price_index] * 1.2
        ten_price_threshold = self._current_listing[self.price_index] * 1.1
        zero_price_threshold = self._current_listing[self.price_index]
        
        # If the price of the suggested property is 20% more than the current listing,
        # the suggestion will be ignored
        if suggestion[self.price_index] > twenty_price_threshold:
            return 'ignore'
        
        # If the price of the suggested property is between 10-20% above the current listing
        # the suggestion will be opened only
        if suggestion[self.price_index] > ten_price_threshold and suggestion[self.price_index] <= twenty_price_threshold:
            return 'click_only'
        
        # If the price of the suggested listing is between 0-10% more than the current listing
        # the suggestion be opened and bookmarked only
        if suggestion[self.price_index] > zero_price_threshold and suggestion[3] <= ten_price_threshold:
            return 'click_and_bookmark_only'
        
        # At this point the price of the suggestion is less than or equal to the current listing
        # For this simulation we assume that homes in the same neighbourhood have the same longitude and latitude values

        # If the suggested listing is in the same neighbourhood as the current listing, the user clicks and contacts the
        # owner
        same_latitude = suggestion[self.latitude_index] == self._current_listing[self.latitude_index]
        same_longitude = suggestion[self.longitude_index] == self._current_listing[self.longitude_index]

        if same_latitude and same_longitude:
            return 'click_and_contact_owner_only'
        

        # But if they are not in the same neighbourhood, then the listing will be opened and bookmarked, but in only
        # 50% of the time, will the owner be contacted.
        return 'click_and_bookmark_only' if np.random.random() < 0.5 else 'click_bookmark_and_contact_owner'


    def step(self, action):
        # Prompt the user for action
        response_to_suggestion = self._simulate_user_response(action)

        # If the user didn't ignore the action, then we update the current listing
        # to become the recommended listing
        if action != 'ignore':
            self._current_listing = action

        # Calculate the reward
        reward = self._rewards[response_to_suggestion]

        # Episode never ends
        terminated = False
        truncated = False

        # Get the observation and information
        observation = self._get_obs()
        info = self._get_info

        return observation, reward, terminated, truncated, info
