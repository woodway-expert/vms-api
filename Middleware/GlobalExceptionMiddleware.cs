using System.Net;
using System.Text.Json;

namespace VmsApi.Middleware;

public class GlobalExceptionMiddleware
{
    private readonly RequestDelegate _next;
    private readonly ILogger<GlobalExceptionMiddleware> _logger;

    public GlobalExceptionMiddleware(RequestDelegate next, ILogger<GlobalExceptionMiddleware> logger)
    {
        _next = next;
        _logger = logger;
    }

    public async Task InvokeAsync(HttpContext context)
    {
        try
        {
            await _next(context);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "An unhandled exception occurred while processing the request");
            await HandleExceptionAsync(context, ex);
        }
    }

    private static async Task HandleExceptionAsync(HttpContext context, Exception exception)
    {
        context.Response.ContentType = "application/json";

        var response = new
        {
            message = "An error occurred while processing your request",
            details = exception.Message
        };

        switch (exception)
        {
            case ArgumentNullException _:
                context.Response.StatusCode = (int)HttpStatusCode.BadRequest;
                response = new { message = "Invalid request data", details = exception.Message };
                break;
            case ArgumentException _:
                context.Response.StatusCode = (int)HttpStatusCode.BadRequest;
                response = new { message = "Invalid argument", details = exception.Message };
                break;
            case UnauthorizedAccessException _:
                context.Response.StatusCode = (int)HttpStatusCode.Unauthorized;
                response = new { message = "Unauthorized access", details = exception.Message };
                break;
            case KeyNotFoundException _:
                context.Response.StatusCode = (int)HttpStatusCode.NotFound;
                response = new { message = "Resource not found", details = exception.Message };
                break;
            default:
                context.Response.StatusCode = (int)HttpStatusCode.InternalServerError;
                response = new { message = "An internal server error occurred", details = "Please contact support if the problem persists" };
                break;
        }

        var jsonResponse = JsonSerializer.Serialize(response, new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase
        });

        await context.Response.WriteAsync(jsonResponse);
    }
}
