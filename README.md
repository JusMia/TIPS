# TIPS
Source code and data sets for paper 'TIPS: a framework for text summarising with illustrative pictures'

Research on comparing the semantic meaning of texts and images is a new topic with a very high potential for practical applications. One such application that may become very popular in the near future is the representation of longer text passages using illustrative images. To the best of our knowledge, although image-text matching methods have been used to investigate the semantic distance between sentence-image pairs, no method has been proposed yet to generate a set of illustrative pictures to summarise multi sentence texts. In this paper, we propose an algorithm to generate graphical summarising of longer text passages using a set of illustrative pictures (TIPS). TIPS is an algorithm using an appropriately designed voting process that uses results of individual "weak" algorithms to produce a single result. The proposed method includes a summarising algorithm that generates a digest of the input document. Then, a sentence transformer algorithm performs text embedding and a group of CLIP similarity-based algorithms trained on different image embedding find semantic distances between the images in the illustration image database and the input text snippets. This is followed by a voting process that extracts the most matching images to the text from that database. TIPS algorithm allows the integration of the best (highest scored) results of the different recommendation algorithms by diminishing influence of images that are a disjoint part of the recommendations of the component algorithms. Both the TIPS algorithm scheme, the voting process algorithm, and the methodology for evaluating and comparing our algorithm with other image-text matching methods are original achievements presented in this work. Our computations and experiments can be fully replicated as we publish the full source codes of both the TIPS algorithm and the entire evaluation process of our approach.

Read more about Bert package uses https://www.sbert.net/examples/applications/image-search/README.html

Code to Image search https://github.com/UKPLab/sentence-transformers/tree/master/examples/applications/image-search/Image_Search.ipynb

Find out more about CLIP:
https://openai.com/research/ 
https://github.com/openai/CLIP

Original data set:
https://brunel.figshare.com/articles/dataset/4000_stories_with_sentiment_analysis_dataset/7712540
https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/datasets/unsplash-25k-photos.zip
https://public.ukp.informatik.tu-darmstadt.de/reimers/sentence-transformers/datasets/unsplash-25k-photos-embeddings.pkl
