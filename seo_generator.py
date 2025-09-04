import os
import requests
import ssl
import certifi
from dotenv import load_dotenv

def generate_seo_content(keyword):
    """
    Generate SEO content (currently using mock data)
    
    Args:
        keyword (str): The target keyword for SEO content
        
    Returns:
        dict: Dictionary containing generated SEO content
    """
    # Mock response for testing
    return {
        'status': 'success',
        'keyword': keyword,
        'title': f'Best {keyword} Guide | Your Brand',
        'meta_description': f'Learn everything about {keyword} with our comprehensive guide. Discover tips, tricks, and best practices.',
        'content': f"""
        <h1>Ultimate Guide to {keyword}</h1>
        <p>Welcome to our comprehensive guide about {keyword}. In this article, we'll cover everything you need to know.</p>
        
        <h2>What is {keyword}?</h2>
        <p>{keyword} is an important concept that many people are interested in learning more about. Key aspects include:</p>
        <ul>
            <li><strong>Definition</strong>: A clear explanation of what {keyword} entails</li>
            <li><strong>Core Components</strong>: The fundamental elements that make up {keyword}</li>
            <li><strong>Common Uses</strong>: Where and how {keyword} is typically applied</li>
            <li><strong>Benefits</strong>: The advantages of understanding {keyword}</li>
        </ul>
        
        <h2>Why is {keyword} Important?</h2>
        <p>Understanding {keyword} can help you achieve better results in your field. Consider these key points:</p>
        <ul>
            <li><strong>Career Advancement</strong>: Mastering {keyword} can open up new opportunities</li>
            <li><strong>Problem-Solving</strong>: Apply {keyword} to overcome common challenges</li>
            <li><strong>Efficiency</strong>: Streamline your workflow with {keyword} best practices</li>
            <li><strong>Industry Relevance</strong>: Stay current with {keyword} trends and developments</li>
        </ul>
        
        <h2>Getting Started with {keyword}</h2>
        <p>Here's a step-by-step guide to begin working with {keyword}:</p>
        <ol>
            <li><strong>Research the Basics</strong>: Build a solid foundation of {keyword} knowledge</li>
            <li><strong>Find Reliable Resources</strong>: Identify trustworthy sources about {keyword}</li>
            <li><strong>Practical Application</strong>: Implement {keyword} in real-world scenarios</li>
            <li><strong>Continuous Learning</strong>: Stay updated with the latest {keyword} trends</li>
            <li><strong>Join Communities</strong>: Connect with other {keyword} enthusiasts</li>
        </ol>
        
        <h2>Pro Tips for {keyword} Success</h2>
        <ul>
            <li>✅ Start with the fundamentals before advancing to complex topics</li>
            <li>✅ Practice regularly to reinforce your understanding</li>
            <li>✅ Document your learning journey with {keyword}</li>
            <li>✅ Seek feedback from experienced professionals</li>
            <li>✅ Stay patient and persistent in your learning</li>
        </ul>
        
        <h2>Conclusion</h2>
        <p>By following this comprehensive guide, you should now have a solid understanding of {keyword}. Remember:</p>
        <ul>
            <li>Consistent practice is key to mastering {keyword}</li>
            <li>Stay curious and keep exploring new aspects of {keyword}</li>
            <li>Apply what you learn to real-world situations</li>
            <li>Share your knowledge with others in the {keyword} community</li>
        </ul>
        """
    }
    
    try:
        # Create a custom session with certificate verification
        session = requests.Session()
        session.verify = certifi.where()  # Use certifi's certificate bundle
        
        # Add retry mechanism
        retry_strategy = requests.adapters.HTTPAdapter(
            max_retries=3,
            status_forcelist=[500, 502, 503, 504]
        )
        session.mount('https://', retry_strategy)
        
        # Make the API request with proper SSL verification
        response = session.post(
            'https://api.grok.ai/v1/generate',
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        
        # Process and return the response
        response_data = response.json()
        return {
            'status': 'success',
            'keyword': keyword,
            'content': response_data.get('content', f'This is sample SEO content for "{keyword}". The actual Grok API integration needs to be properly configured with the correct endpoint and authentication.'),
            'meta_description': response_data.get('meta_description', f'Learn all about {keyword} with our comprehensive guide.'),
            'title': response_data.get('title', f'Best {keyword} Guide | Your Brand')
        }
        
    except requests.exceptions.SSLError as e:
        # Provide more detailed SSL error information
        ssl_context = ssl.create_default_context()
        ssl_context.load_verify_locations(cafile=certifi.where())
        raise Exception(f"SSL verification failed. This might be due to network restrictions or proxy settings. Details: {str(e)}")
    except requests.exceptions.RequestException as e:
        # Provide a more helpful error message
        if 'Max retries exceeded' in str(e):
            raise Exception("Could not connect to the Grok API. Please check your internet connection and try again.")
        raise Exception(f"Error calling Grok API: {str(e)}")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")
