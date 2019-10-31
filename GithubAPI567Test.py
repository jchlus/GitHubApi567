import unittest
import GithubAPI567

class TestGitHubAPI(unittest.TestCase):

    def testGetRepos(self): 
        self.assertIn('SW-567', GithubAPI567.getRepos('jchlus'))
    def testGetCommits(self): 
        self.assertEqual(GithubAPI567.getCommits('jchlus', 'SW-567'), 3)
    def testGetReposAndCommits(self): 
        self.assertIn('SW-567', GithubAPI567.getReposAndCommits('jchlus'))
        self.assertEqual(GithubAPI567.getReposAndCommits('jchlus')['SW-567'], 3)
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()