const data = [
{
    "_id" : "scatter_plot",
    "viz_type" : 32.0
},
{
    "_id" : "big_number",
    "viz_type" : 1070.0
},
{
    "_id" : "map_pinned",
    "viz_type" : 41.0
},
{
    "_id" : "Pareto",
    "viz_type" : 260.0
},
{
    "_id" : "stack bar and line",
    "viz_type" : 464.0
},
{
    "_id" : "table",
    "viz_type" : 15630.0
},
{
    "_id" : "bar",
    "viz_type" : 2288.0
},
{
    "_id" : "pivot",
    "viz_type" : 5307.0
},
{
    "_id" : "Bar",
    "viz_type" : 482.0
},
{
    "_id" : "Table",
    "viz_type" : 32438.0
},
{
    "_id" : "stack bar",
    "viz_type" : 1422.0
},
{
    "_id" : "Text",
    "viz_type" : 2410.0
},
{
    "_id" : "Line",
    "viz_type" : 562.0
},
{
    "_id" : "Map",
    "viz_type" : 15.0
},
{
    "_id" : "map_filled",
    "viz_type" : 80.0
},
{
    "_id" : "Stack Bar",
    "viz_type" : 154.0
},
{
    "_id" : "bar and line",
    "viz_type" : 1523.0
},
{
    "_id" : "tree_table",
    "viz_type" : 715.0
},
{
    "_id" : "heatmap",
    "viz_type" : 368.0
},
{
    "_id" : "Bar And Line",
    "viz_type" : 234.0
}]

const total = data.reduce((prev, item) => {

    prev = prev + item.viz_type

    return prev
}, 0)

const percents = data.map((item) => {

    item.percent = item.viz_type / total

    return item
})



console.log(percents)

