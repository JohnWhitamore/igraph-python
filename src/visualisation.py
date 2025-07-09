import igraph as ig
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
    
class GraphStructure: 
    
    def create_layout(self, stores, products, 
                      store_groups, product_groups,
                      store_to_group, product_to_group):

        # ... initialise the layout as a list
        layout = []
        
        # ... build lookup dictionaries
        store_x = {s: i for i, s in enumerate(stores)}
        product_y = {p: i for i, p in enumerate(products)}
        
        # ... store groups (above stores in the hierarchy)
        for sg in store_groups:
            
            # ... place above the average x-coordinate of its stores
            child_stores = [s for s in stores if store_to_group[s] == sg]
            x = sum(store_x[s] for s in child_stores) / len(child_stores)
            layout.append((x, len(products) + 2))
        
        # ... stores (above product_locations in the hierarchy)
        for s in stores:
            
            layout.append((store_x[s], len(products) + 1))
        
        # ... product groups (left of products)
        for pg in product_groups:
            
            # ... place to the left of the average y-coordinate of its products
            child_products = [p for p in products if product_to_group[p] == pg]
            y = sum(product_y[p] for p in child_products) / len(child_products)
            layout.append((-2, y))  
        
        # ... products (left of product_locations)
        for p in products:
            layout.append((-1, product_y[p]))
        
        # ... product-Locations (grid interior)
        for s in stores:
            for p in products:
                layout.append((store_x[s], product_y[p]))
                
        return layout
        

    def create_figure(self, g, layout, colours, type_to_colour):
        
        # ... plot size
        fig, ax = plt.subplots(figsize=(14, 10))

        # ... igraph plot() function
        ig.plot(
            g,
            layout=layout,
            target=ax,
            vertex_label = g.vs["name"],
            vertex_color=colours,
            vertex_size=20,
            edge_arrow_size=0.5,
            edge_color="gray"
        )

        ax.axis("off")
        
        # ... legend
        legend_handles = [
            mpatches.Patch(color=colour, label=label.replace("_", " ").title())
            for label, colour in type_to_colour.items()
        ]
        
        ax.legend(handles=legend_handles, loc="upper left", frameon=False, fontsize=10)
        
        return fig, ax