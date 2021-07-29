# TODO: import necessary libraries
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

# A Binomial class that inherits from the Distribution class. 
class Binomial(Distribution):

    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
    
    #       A binomial distribution is defined by two variables: 
    #           the probability of getting a positive outcome
    #           the number of trials
    
    #       If you know these two values, you can calculate the mean and the standard deviation
    #       
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))

    def __init__(self, prob = .5, size = 20):
        self.p = prob         # stores the probability of the distribution in an instance variable p
        self.n = size         # stores the size of the distribution in an instance variable n
        
        
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
        

    def calculate_mean(self): 
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        self.mean = self.p * self.n
        return self.mean

    
    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev
        
        

    def replace_stats_with_data(self):
        
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """

        """   
        count = 0
        for item in self.data:
            if item == True:
                count += 1
        p = count / len(self.data)
        or
       """        
        
        #update attributes
        self.n = len(self.data)                                     #           updates the n attribute of the binomial distribution
        self.p = 1.0 * sum(self.data)/len(self.data)                #           updates the p value of the binomial distribution by calculating the number of positive trials divided by the total trials
        self.mean = self.calculate_mean()                           #           updates the mean attribute
        self.stdev = self.calculate_stdev()                         #           updates the standard deviation attribute
        
        return self.p, self.n
        

    def plot_bar(self):
        
    
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.bar(x = ['0', '1'], height = [(1 - self.p) * self.n, self.p * self.n])
        plt.title('Bar Chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
    
    
    
    def pdf(self, k):
        

        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        def find_factorial(n):
            factorial = 1
            for i in range (1, n+1):
                factorial  *= i
            return factorial                 
        return (find_factorial(self.n)/(find_factorial(k)*find_factorial(self.n-k)))*((self.p** k)*((1-self.p)**(self.n-k)))              
            
    
    def plot_pdf(self):
        
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        y = []
        for tmp in range(self.n+1):
            x.append(tmp)
            y.append(self.pdf(tmp))
        
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].bar(self.data, density=True)
        axes[0].set_title('Binomial bar plot of Data')
        axes[0].set_xlabel('Number of trials')
        axes[0].set_ylabel('Density')
        
        axes[1].plot(x, y)
        axes[1].set_title('Binomial Distribution')
        axes[1].set_ylabel('Density')
        plt.show()
        
        return x, y
    

    def __add__(self, other):
                           
        # Magic method: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for 
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.
        
        # Hint: When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        # try, except statement will raise an exception if the p values are not equal
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial ()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        return result        

                        
    def __repr__(self):          
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        
        
        # Magic Method:  The method should return a string in the expected format
    
        return 'mean {}, standard deviation {}, p {},n {}'.format(self.mean, self.stdev, self.p, self.n)
