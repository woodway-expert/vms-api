using Microsoft.AspNetCore.Mvc;
using VmsApi.Data.Models;
using VmsApi.Services;

namespace VmsApi.Controllers;

[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    private readonly IOrderService _orderService;
    private readonly ILogger<OrdersController> _logger;

    public OrdersController(IOrderService orderService, ILogger<OrdersController> logger)
    {
        _orderService = orderService;
        _logger = logger;
    }

    /// <summary>
    /// Get all orders from the database
    /// </summary>
    /// <returns>List of orders</returns>
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Order>>> GetOrders()
    {
        try
        {
            var orders = await _orderService.GetAllOrdersAsync();
            return Ok(orders);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching orders");
            return StatusCode(500, "Internal server error occurred while fetching orders");
        }
    }

    /// <summary>
    /// Get a specific order by ID
    /// </summary>
    /// <param name="id">Order ID</param>
    /// <returns>Order details</returns>
    [HttpGet("{id}")]
    public async Task<ActionResult<Order>> GetOrder(Guid id)
    {
        try
        {
            var order = await _orderService.GetOrderByIdAsync(id);
            if (order == null)
            {
                return NotFound($"Order with ID {id} not found");
            }
            return Ok(order);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching order {OrderId}", id);
            return StatusCode(500, "Internal server error occurred while fetching the order");
        }
    }

    /// <summary>
    /// Create a new order
    /// </summary>
    /// <param name="order">Order to create</param>
    /// <returns>Created order</returns>
    [HttpPost]
    public async Task<ActionResult<Order>> CreateOrder(Order order)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var createdOrder = await _orderService.CreateOrderAsync(order);
            return CreatedAtAction(nameof(GetOrder), new { id = createdOrder.OrderId }, createdOrder);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while creating order");
            return StatusCode(500, "Internal server error occurred while creating the order");
        }
    }

    /// <summary>
    /// Update an existing order
    /// </summary>
    /// <param name="id">Order ID</param>
    /// <param name="order">Updated order data</param>
    /// <returns>Updated order</returns>
    [HttpPut("{id}")]
    public async Task<ActionResult<Order>> UpdateOrder(Guid id, Order order)
    {
        try
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var updatedOrder = await _orderService.UpdateOrderAsync(id, order);
            if (updatedOrder == null)
            {
                return NotFound($"Order with ID {id} not found");
            }

            return Ok(updatedOrder);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while updating order {OrderId}", id);
            return StatusCode(500, "Internal server error occurred while updating the order");
        }
    }

    /// <summary>
    /// Delete an order
    /// </summary>
    /// <param name="id">Order ID</param>
    /// <returns>Success result</returns>
    [HttpDelete("{id}")]
    public async Task<IActionResult> DeleteOrder(Guid id)
    {
        try
        {
            var result = await _orderService.DeleteOrderAsync(id);
            if (!result)
            {
                return NotFound($"Order with ID {id} not found");
            }

            return NoContent();
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while deleting order {OrderId}", id);
            return StatusCode(500, "Internal server error occurred while deleting the order");
        }
    }

    /// <summary>
    /// Get orders by customer ID
    /// </summary>
    /// <param name="customerId">Customer ID</param>
    /// <returns>List of orders for the customer</returns>
    [HttpGet("customer/{customerId}")]
    public async Task<ActionResult<IEnumerable<Order>>> GetOrdersByCustomer(int customerId)
    {
        try
        {
            var orders = await _orderService.GetOrdersByCustomerIdAsync(customerId);
            return Ok(orders);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching orders for customer {CustomerId}", customerId);
            return StatusCode(500, "Internal server error occurred while fetching orders");
        }
    }

    /// <summary>
    /// Get orders by date range
    /// </summary>
    /// <param name="startDate">Start date</param>
    /// <param name="endDate">End date</param>
    /// <returns>List of orders within the date range</returns>
    [HttpGet("date-range")]
    public async Task<ActionResult<IEnumerable<Order>>> GetOrdersByDateRange(
        [FromQuery] DateTime startDate,
        [FromQuery] DateTime endDate)
    {
        try
        {
            var orders = await _orderService.GetOrdersByDateRangeAsync(startDate, endDate);
            return Ok(orders);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching orders by date range {StartDate} - {EndDate}", startDate, endDate);
            return StatusCode(500, "Internal server error occurred while fetching orders");
        }
    }

    /// <summary>
    /// Get orders by status
    /// </summary>
    /// <param name="status">Order status</param>
    /// <returns>List of orders with the specified status</returns>
    [HttpGet("status/{status}")]
    public async Task<ActionResult<IEnumerable<Order>>> GetOrdersByStatus(byte status)
    {
        try
        {
            var orders = await _orderService.GetOrdersByStatusAsync(status);
            return Ok(orders);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error occurred while fetching orders by status {Status}", status);
            return StatusCode(500, "Internal server error occurred while fetching orders");
        }
    }
}
