class LinguisticText:
    def __init__(self, url_list, orig_text, prep_text, subr_name):
        self.url_lst = url_list
        self.orig_text = orig_text
        self.prep_text = prep_text
        self.subr_name = subr_name

    def get_links(self, reddit):
        """Get 100 hot links from subreddit"""
        subreddit = reddit.subreddit(self.subr_name)
        submissions = subreddit.hot(limit=100)

        with open(self.url_lst, "w", encoding="utf-8") as f:
            for submission in submissions:
                f.write(submission.permalink)
                f.write("\n")

    def get_text(self, reddit):
        """Get text body and comments from list of links"""
        url = open(self.url_lst).readlines()
        collected_data = open(self.orig_text, "a", encoding="utf-8")
        for i in url:
            self.collecting_main_post(i, collected_data, reddit)

    def collecting_main_post(self, url, collected_data, reddit):
        """"Собирает данные поста: заголовок и текст"""
        post = reddit.submission(url="https://www.reddit.com" + url)
        collected_data.write(post.title)
        collected_data.write("\n\n")
        collected_data.write(post.selftext)
        collected_data.write("\n\n")
        self.collecting_comments(post, collected_data)

    def collecting_comments(self, post, collected_data):
        """Собирает комментарии поста"""
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            collected_data.write(comment.body)
            collected_data.write("\n\n")

    def clean_text(self):
        import re
        """Clean text from punctuation etc etc"""
        emoj = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                          u"\U00002500-\U00002BEF"  # chinese char
                          u"\U00002702-\U000027B0"
                          u"\U000024C2-\U0001F251"
                          u"\U0001f926-\U0001f937"
                          u"\U00010000-\U0010ffff"
                          u"\u2640-\u2642"
                          u"\u2600-\u2B55"
                          u"\u200d"
                          u"\u23cf"
                          u"\u23e9"
                          u"\u231a"
                          u"\ufe0f"  # dingbats
                          u"\u3030"
                          "]+", flags=re.UNICODE)
        f = open(self.orig_text, "r", encoding="utf-8")
        text_ = f.read()

        text_ = self.get_rid_of_links(text_)

        lower_question = input("Do you want to lowercase the text? yes / no ")
        text_ = self.checking_answers(lower_question, "1", text_)

        print("Getting rid of punctuation... ")
        punctuation_question = input("Do you want to get rid of apostrophes as well? yes / no ")
        text_ = self.checking_answers(punctuation_question, "2", text_)

        text_ = re.sub('\n+', ' ', text_)
        text_ = emoj.sub(r'', text_)
        text_ = re.sub("\s{2,}", " ", text_)

        # here's the name of new doc with prepared text
        i = open(self.prep_text, "a", encoding="utf-8")
        i.write(text_)

    def checking_answers(self, answer, note, txt_):
        if answer.lower() == "yes":
            if note == "1":
                return self.lowercase_text(txt_)
            elif note == "2":
                return self.complete_punctuation(txt_)
        elif answer.lower() == "no":
            if note == "1":
                return txt_
            elif note == "2":
                return self.punctuation_excluding_apos(txt_)
        else:
            if note == "1":
                ask = input("Error. Try again. Do you want to lowercase the text? yes / no ")
                if ask == "yes" or ask == "Yes":
                    return self.lowercase_text(txt_)
                else:
                    return txt_
            if note == "2":
                ask = input("Error. Try again. Do you want to get rid of apostrophes? yes / no ")
                if ask == "yes" or ask == "Yes":
                    return self.complete_punctuation(txt_)
                else:
                    return self.punctuation_excluding_apos(txt_)

    def lowercase_text(self, txt_):
        return txt_.lower()

    def complete_punctuation(self, txt_):
        from string import punctuation
        spec_chars = punctuation + '«»\t—…’'
        txt_ = "".join([ch for ch in txt_ if ch not in spec_chars])
        return txt_

    def punctuation_excluding_apos(self, txt_):
        spec_chars = '«»\t—"#$%&()*+,-/:;<=>@[\]^_{|}~'  # !?. ...
        txt_ = "".join([ch for ch in txt_ if ch not in spec_chars])
        return txt_

    def get_rid_of_links(self, txt_):
        import re
        txt_ = re.sub("\d+|(H|h)ttp.+?.+", "", txt_)
        txt_ = re.sub("www.+", "", txt_)
        txt_ = re.sub("!?\[[^\]]*\](\s?)\(.+?\)", "", txt_)
        txt_ = re.sub("r/\w+", "", txt_)
        return txt_

    def stop_words(self):
        from nltk.corpus import stopwords
        stopwords = stopwords.words("english")

    def lemmatization(self, allowed_postags=["NOUN", "ADJ", "VERB", "ADV"]):
        import spacy
        nlp = spacy.load('en_core_web_sm')
        text_out = []
        for text in self.prep_text:
            doc = nlp(text)
            new_text = []
            for token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
            final = " ".join(new_text)
            text_out.append(final)
