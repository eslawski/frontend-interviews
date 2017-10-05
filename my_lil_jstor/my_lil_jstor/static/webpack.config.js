let ExtractTextPlugin = require("extract-text-webpack-plugin");

const extractSass = new ExtractTextPlugin("[name]");

module.exports = {
    entry: {
        "dist/css/my-lil-jstor.css": "./scss/my-lil-jstor.scss",
        "dist/js/my-lil-jstor.js": "./js/my-lil-jstor.js"
    },
    module: {
        rules: [
            {
                test: /\.s?css$/,
                use: extractSass.extract({
                    use: [{
                        loader: "css-loader",
                        options: {
                            sourceMap: true
                        }
                    }, {
                        loader: "sass-loader",
                        options: {
                            includePaths: [
                                "scss",
                                "node_modules",
                                "node_modules/@ithaka"
                            ],
                            sourceMap: true,
                            outputStyle: "expanded"
                        }
                    }],
                    fallback: "style-loader"
                })
            },
            {
                test: /\.(eot|woff|woff2|ttf|svg|png|jpe?g|gif)(\?\S*)?$/,
                loader: "url-loader?name=./dist/fonts/[hash].[ext]"
            }
        ]
    },
    externals: {
        jquery: "jQuery"
    },
    output: {
        filename: "[name]"
    },
    plugins: [
        extractSass
    ]
};