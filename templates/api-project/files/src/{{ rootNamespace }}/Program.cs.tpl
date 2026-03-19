var builder = WebApplication.CreateBuilder(args);

builder.Services.AddEndpointsApiExplorer();

var app = builder.Build();
var serviceName = app.Configuration["Service:Name"] ?? "{{ serviceName }}";

app.MapGet("/health", () => Results.Ok(new
{
    status = "ok",
    service = serviceName
}));

app.Run();

public partial class Program
{
}
