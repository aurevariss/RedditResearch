import praw
from tasks import text_class
from config import parse_config
config = parse_config('skz')

def main():
    reddit = praw.Reddit(user_agent=True, client_id=config["client_id"], client_secret=config["client_secret"], username=config["username"])

    # Create class object
    text_obj = text_class.LinguisticText(url_list=config["url_list"], orig_text=config["original_text"], prep_text=config["prepared_text"], subr_name=config["subreddit_name"])

    # Get all info: links, post text, post comments
    # text_obj.get_links(reddit)
    text_obj.get_text(reddit)

    # Cleaning the text
    text_obj.clean_text()

if __name__ == "__main__":
    main()