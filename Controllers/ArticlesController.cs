using Microsoft.AspNetCore.Mvc;
using VmsApi.Data.Models;
using VmsApi.Services;

namespace VmsApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class ArticlesController : ControllerBase
{
    private readonly IArticleService _articleService;
    private readonly ILogger<ArticlesController> _logger;

    public ArticlesController(IArticleService articleService, ILogger<ArticlesController> logger)
    {
        _articleService = articleService;
        _logger = logger;
    }

    /// <summary>
    /// Get all articles from the database
    /// </summary>
    /// <returns>List of articles</returns>
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Article>>> GetArticles()
    {
        try
        {
            var articles = await _articleService.GetAllArticlesAsync();
            return Ok(articles);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching articles");
            return StatusCode(500, "Internal server error occurred while fetching articles");
        }
    }

    /// <summary>
    /// Get a specific article by ID
    /// </summary>
    /// <param name="id">Article ID</param>
    /// <returns>Article details</returns>
    [HttpGet("{id}")]
    public async Task<ActionResult<Article>> GetArticle(int id)
    {
        try
        {
            var article = await _articleService.GetArticleByIdAsync(id);
            if (article == null)
            {
                return NotFound($"Article with ID {id} not found");
            }
            return Ok(article);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching article {ArticleId}", id);
            return StatusCode(500, "Internal server error occurred while fetching the article");
        }
    }

    /// <summary>
    /// Create a new article
    /// </summary>
    /// <param name="article">Article to create</param>
    /// <returns>Created article</returns>
    [HttpPost]
    public async Task<ActionResult<Article>> CreateArticle(Article article)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var createdArticle = await _articleService.CreateArticleAsync(article);
            return CreatedAtAction(nameof(GetArticle), new { id = createdArticle.ArticleId }, createdArticle);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while creating article");
            return StatusCode(500, "Internal server error occurred while creating the article");
        }
    }

    /// <summary>
    /// Update an existing article
    /// </summary>
    /// <param name="id">Article ID</param>
    /// <param name="article">Updated article data</param>
    /// <returns>Updated article</returns>
    [HttpPut("{id}")]
    public async Task<ActionResult<Article>> UpdateArticle(int id, Article article)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var updatedArticle = await _articleService.UpdateArticleAsync(id, article);
            if (updatedArticle == null)
            {
                return NotFound($"Article with ID {id} not found");
            }

            return Ok(updatedArticle);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while updating article {ArticleId}", id);
            return StatusCode(500, "Internal server error occurred while updating the article");
        }
    }

    /// <summary>
    /// Delete an article
    /// </summary>
    /// <param name="id">Article ID</param>
    /// <returns>Success result</returns>
    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteArticle(int id)
    {
        try
        {
            var result = await _articleService.DeleteArticleAsync(id);
            if (!result)
            {
                return NotFound($"Article with ID {id} not found");
            }

            return NoContent();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while deleting article {ArticleId}", id);
            return StatusCode(500, "Internal server error occurred while deleting the article");
        }
    }

    /// <summary>
    /// Search articles by name or description
    /// </summary>
    /// <param name="searchTerm">Search term</param>
    /// <returns>List of matching articles</returns>
    [HttpGet("search")]
    public async Task<ActionResult<IEnumerable<Article>>> SearchArticles([FromQuery] string searchTerm = "")
    {
        try
        {
            var articles = await _articleService.SearchArticlesAsync(searchTerm);
            return Ok(articles);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while searching articles with term: {SearchTerm}", searchTerm);
            return StatusCode(500, "Internal server error occurred while searching articles");
        }
    }
}
