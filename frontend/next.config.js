module.exports = {
    async redirects() {
        return [{source: "/", destination: "/Home", permanent: true}]
    },
    async rewrites() {
        return [
            {
                source: "/api/:path*",
                destination: "http://localhost:8080/api/:path*"
            }
        ]
    }
}
