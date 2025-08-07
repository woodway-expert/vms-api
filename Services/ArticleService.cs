using Microsoft.EntityFrameworkCore;
using VmsApi.Data;
using VmsApi.Data.Models;

namespace VmsApi.Services;

public class ArticleService : IArticleService
{
    private readonly AppDbContext _context;

    public ArticleService(AppDbContext context)
    {
        _context = context;
    }

    public async Task<IEnumerable<Article>> GetAllArticlesAsync()
    {
        return await _context.Articles
            .Include(a => a.LinkAccountings)
            .ToListAsync();
    }

    public async Task<Article?> GetArticleByIdAsync(int id)
    {
        return await _context.Articles
            .Include(a => a.LinkAccountings)
            .FirstOrDefaultAsync(a => a.ArticleId == id);
    }

    public async Task<Article> CreateArticleAsync(Article article)
    {
        _context.Articles.Add(article);
        await _context.SaveChangesAsync();
        return article;
    }

    public async Task<Article?> UpdateArticleAsync(int id, Article article)
    {
        var existingArticle = await _context.Articles.FindAsync(id);
        if (existingArticle == null)
        {
            return null;
        }

        existingArticle.Name = article.Name;
        existingArticle.NameUa = article.NameUa;
        existingArticle.NameEn = article.NameEn;
        existingArticle.ArticleType = article.ArticleType;

        await _context.SaveChangesAsync();
        return existingArticle;
    }

    public async Task<bool> DeleteArticleAsync(int id)
    {
        var article = await _context.Articles.FindAsync(id);
        if (article == null)
        {
            return false;
        }

        _context.Articles.Remove(article);
        await _context.SaveChangesAsync();
        return true;
    }

    public async Task<IEnumerable<Article>> SearchArticlesAsync(string searchTerm)
    {
        if (string.IsNullOrWhiteSpace(searchTerm))
        {
            return await GetAllArticlesAsync();
        }

        return await _context.Articles
            .Include(a => a.LinkAccountings)
            .Where(a => a.Name.Contains(searchTerm) ||
                       (a.NameUa != null && a.NameUa.Contains(searchTerm)) ||
                       (a.NameEn != null && a.NameEn.Contains(searchTerm)))
            .ToListAsync();
    }
}
