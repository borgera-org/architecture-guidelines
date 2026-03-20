FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

COPY ["Directory.Build.props", "./"]
COPY ["src/Billing.Api/Billing.Api.csproj", "src/Billing.Api/"]

RUN dotnet restore "src/Billing.Api/Billing.Api.csproj"

COPY . .

RUN dotnet publish "src/Billing.Api/Billing.Api.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS final
WORKDIR /app

COPY --from=build /app/publish .

EXPOSE 8080

ENV ASPNETCORE_URLS=http://+:8080

ENTRYPOINT ["dotnet", "Billing.Api.dll"]
