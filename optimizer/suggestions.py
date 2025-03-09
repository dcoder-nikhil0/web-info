def optimization_tips(load_time):
    if load_time > 5:
        return [
            "🔴 Slow website! Consider optimizing:",
            "- Minify CSS, JavaScript, and HTML",
            "- Optimize images (use WebP, compress large files)",
            "- Enable browser caching",
            "- Reduce server response time"
        ]
    elif load_time > 2:
        return [
            "🟡 Moderate speed. Some improvements needed:",
            "- Optimize third-party scripts",
            "- Implement lazy loading for images",
            "- Use a Content Delivery Network (CDN)"
        ]
    else:
        return ["🟢 Fast website! No major issues detected."]
