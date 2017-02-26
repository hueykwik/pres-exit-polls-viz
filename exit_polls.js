function parseRow(d) {
  return { 'state': d.state,
           'year': +d.year,
           'category': d.answer,
           'value': +d.democrat };
}

function ready(data) {
  var defaultOptionName = "ALL";

  var states = d3.nest().key(d => d.state).entries(data);

  d3.select('#states').selectAll('option')
    .data(states, d => d.key)
    .enter()
    .append('option')
    .attr("value", d => d.key)
    .property("selected", function(d) {
      return d.key == defaultOptionName;
    })
    .text(d => d.key);

  d3.select('#states')
    .on("change", function() {
      update(this.value);
    });

  filtered = data.filter(d => (d.state == defaultOptionName));

  var margin = {top: 70, right: 0, bottom: 40, left: 0},
      width = 710 - margin.left - margin.right,
      height = 1300 - margin.top - margin.bottom,

      y_dom = d3.extent(data, d => d.value).reverse()
      x_dom = d3.extent(data, d => d.year)

      y = d3.scale.linear()
          .domain(y_dom)
          .range([0, height]),
      x = d3.scale.linear()
          .domain(x_dom)
          .range([390, 570]),

      // textHeight just sets the minimum needed distance between labels
      layout = d3.layout.slopegraph()(filtered)
          .j('category').y('value').x('year')
          .textHeight((y_dom[0] - y_dom[1]) / height * 14),

      textAlign = m => {
        return (d, i) => i ? 'start' : 'end';
      },
      textMargin = m => {
        return (d, i) => i ? m * 1 : m * -1;
      };

  // Adds the main svg tag, origin is set (margin.left, margin.top)
  var svg = d3.select('#graph').append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
    .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

  // Adds the year labels, 2012 and 2016.
  svg.append('g')
      .attr('class', 'years')
      .selectAll('text').data(x_dom).enter()
    .append('text')
      .attr('x', x)
      .attr('dx', (d, i) => i ? 10 : -10)
      .attr('y', -40)
      .style('text-anchor', textAlign())
      .text(String);

  // Define the line that will be used for each pair below
  var line = d3.svg.line()
      .x(d => x(d.year))
      .y(d => y(d.y));

  function key_func(d) {
    return d.state + "_" + d.year + "_" + d.category + "_" + d.value;
  }

  function pair_key_func(d) {
    return key_func(d[0]) + "_" + key_func(d[1]);
  }

  // Add a group for each pair
  var pairs = svg.append('g')
      .attr('class', 'lines')
      .selectAll('g')
      .data(layout.pairs(), pair_key_func).enter()
    .append('g');

  pairs.append('path')
      .attr('d', line);

  // Adds the labels for each category
  pairs.selectAll('.category')
      .data(d => d).enter()
    .append('text')
      .attr('class', 'category')
      .attr('x', d => x(d.year))
      .attr('dx', textMargin(48))
      .attr('dy', '.32em')
      .attr('y', d => y(d.y))
      .style('text-anchor', textAlign())
      .text(d => d.category);

  // Adds the values for each category
  pairs.selectAll('.value')
      .data(d => d).enter()
    .append('text')
      .attr('class', 'value')
      .attr('x', d => x(d.year))
      .attr('dy', '.32em')
      .attr('dx', textMargin(10))
      .attr('y', d => y(d.y))
      .style('text-anchor', textAlign())
      .text(d => d.value.toFixed(0));

  // Text description
  svg.append('g')
      .attr('class', 'desc')
      .selectAll('text')
      .data(['Why did Democrats lose the 2016 election?',
             'Per CNN exit polls, Clinton performed worse',
             'than Obama in all categories except one.',
             ' ',
             'Check out each state yourself: ',
            ]).enter()
    .append('text')
      .attr('y', (d,i) => i * 20)
      .attr('dy', '-.32em')
      .attr('x', 13)
      .text(String);

  function update(state) {
    filtered = data.filter(d => (d.state == state));

    // Need to convert filtered into a layout, then use
    // layout.pairs() as data.
    var layout = d3.layout.slopegraph()(filtered)
           .j('category').y('value').x('year')
           .textHeight((y_dom[0] - y_dom[1]) / height * 14);

    var pairs = svg.selectAll('.lines')
        .selectAll('g')
      .data(layout.pairs(), pair_key_func);

    pairs.exit().remove();

    pairs = pairs.enter().append('g');

    pairs.append('path')
      .attr('d', line);

    // Adds the labels for each category
    pairs.selectAll('.category')
      .data(d => d).enter()
    .append('text')
      .attr('class', 'category')
      .attr('x', d => x(d.year))
      .attr('dx', textMargin(48))
      .attr('dy', '.32em')
      .attr('y', d => y(d.y))
      .style('text-anchor', textAlign())
      .text(d => d.category);

    // Adds the values for each category
    pairs.selectAll('.value')
        .data(d => d).enter()
      .append('text')
        .attr('class', 'value')
        .attr('x', d => x(d.year))
        .attr('dy', '.32em')
        .attr('dx', textMargin(10))
        .attr('y', d => y(d.y))
        .style('text-anchor', textAlign())
        .text(d => d.value.toFixed(0));
  }
};
