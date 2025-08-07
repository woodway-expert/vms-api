using VmsApi.Data.Models;

namespace VmsApi.Services;

public interface IArticleService
{
    Task<IEnumerable<Article>> GetAllArticlesAsync();
    Task<Article?> GetArticleByIdAsync(int id);
    Task<Article> CreateArticleAsync(Article article);
    Task<Article?> UpdateArticleAsync(int id, Article article);
    Task<bool> DeleteArticleAsync(int id);
    Task<IEnumerable<Article>> SearchArticlesAsync(string searchTerm);
}
