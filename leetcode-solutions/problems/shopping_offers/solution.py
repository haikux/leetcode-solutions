class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        return self.final_amount(price, special, needs, {})
        
    
    def final_amount(self, price, special, needs, map):
        # First check if the offer is already computed (Memoization) for the 
        # required need
        if tuple(needs) in map:
            return map[tuple(needs)] 

        min_amount = 0
        # Process the base case amount, without including any offers
        for i, item in enumerate(needs):
            min_amount += item * price[i] 
        
        # Now compute the price including the offers
        for offer in special:
            # Check if the offer satisfies the need
            need_rem = self.is_offer_valid(needs, offer)
            if all(i>=0 for i in need_rem):
                min_amount = min(min_amount, offer[-1] + self.final_amount(price, special, need_rem, map))
        map[tuple(needs)] = min_amount

        return min_amount
    
    def is_offer_valid(self, needs, offer):
        result = []
        print(needs)
        print(offer)
        for i, n in enumerate(needs):
            result.append(n-offer[i]) 
        return result


        