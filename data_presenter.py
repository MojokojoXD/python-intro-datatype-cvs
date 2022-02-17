import plotly.graph_objects as go


#Part 2
#Q1
cupcake_file = open('CupcakeInvoices.csv');

for row in cupcake_file:
    print(row);
cupcake_file.seek(0,0);


for row in cupcake_file:
    type = row.split(',');
    print(type[2]);
cupcake_file.seek(0,0);

for row in cupcake_file:
    breakdown = row.rstrip('\n').split(',');
    result = float(breakdown[3])* float(breakdown[4]);
    print(f'{result:.4g}');
cupcake_file.seek(0,0);

total = 0;

for row in cupcake_file:
    breakdown = row.rstrip('\n').split(',');
    result = float(breakdown[3])* float(breakdown[4]);
    total += result;
cupcake_file.seek(0,0);


print(f'{total:.5g}');

total_for_flavor = [0,0,0,]
for row in cupcake_file:
    breakdown = row.rstrip('\n').split(','); 
    result = float(breakdown[3])* float(breakdown[4]);
    if breakdown[2] == 'Chocolate':
        total_for_flavor[0] += result;
    elif breakdown[2] == 'Strawberry':
        total_for_flavor[1] += result;
    else:
        total_for_flavor[2] += result;
    
cupcake_file.seek(0,0);
cupcake_file.close();

fig = go.Figure([go.Bar(x=['Chocolate','Strawberry','Vanilla'], y= total_for_flavor)])


fig.show()