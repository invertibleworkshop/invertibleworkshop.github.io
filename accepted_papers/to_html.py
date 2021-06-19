import pandas as pd

papers = pd.read_csv('./accepted_papers/INNF+_2021_paper_status (trimmed).csv', index_col='number')

template = \
"""
            <li value="{}">
              <span class="title"> <a href="{}" target="_blank">{}</a></span>
              <button type="button" class="collapsible">Abstract</button>
              <div class="content">
                {}
              </div>
              <div class="paper">
                <span class="authors">
                    <span>
                      {}
                    </span>
                </span>
              </div>
            </li>
"""
# id, url, title, abstract, authors



for i in range(len(papers)):
    paper = papers.iloc[i]
    print(template.format(paper.name, paper.forum, paper.title, paper.abstract, paper.authors.replace('|', '; ')))




