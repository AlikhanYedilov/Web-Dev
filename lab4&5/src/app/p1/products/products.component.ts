// products.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent {
  categories = ['All', 'Fresh Fruits', 'Organic Vegetables', 'Leafy Greens', 'Seasonal Berries'];
  selected = 'All';

  searchQuery = '';
  filteredCategories = this.categories;

  products = [
    { id: 1, category: 'Fresh Fruits', name: 'Apple', description: 'Crisp and juicy red apples.', rating: 4.8, likes: 0, image: 'apple.jpg', link: 'https://en.wikipedia.org/wiki/Apple' },
    { id: 2, category: 'Fresh Fruits', name: 'Banana', description: 'Sweet and ripe bananas.', rating: 4.6, likes: 0, image: 'banana.jpg', link: 'https://en.wikipedia.org/wiki/Banana' },
    { id: 3, category: 'Fresh Fruits', name: 'Orange', description: 'Citrusy and tangy oranges.', rating: 4.7, likes: 0, image: 'orange.jpg', link: 'https://en.wikipedia.org/wiki/Orange_(fruit)' },
    { id: 4, category: 'Fresh Fruits', name: 'Pineapple', description: 'Tropical and refreshing.', rating: 4.5, likes: 0, image: 'pineapple.jpg', link: 'https://en.wikipedia.org/wiki/Pineapple' },
    { id: 5, category: 'Fresh Fruits', name: 'Mango', description: 'Sweet and juicy mangoes.', rating: 4.9, likes: 0, image: 'mango.jpg', link: 'https://en.wikipedia.org/wiki/Mango' },
    { id: 6, category: 'Organic Vegetables', name: 'Carrot', description: 'Crunchy and sweet organic carrots.', rating: 4.7, likes: 0, image: 'carrot.jpg', link: 'https://en.wikipedia.org/wiki/Carrot' },
    { id: 7, category: 'Organic Vegetables', name: 'Broccoli', description: 'Fresh and nutritious.', rating: 4.5, likes: 0, image: 'broccoli.jpg', link: 'https://en.wikipedia.org/wiki/Broccoli' },
    { id: 8, category: 'Organic Vegetables', name: 'Potato', description: 'Versatile organic potatoes.', rating: 4.4, likes: 0, image: 'potato.jpg', link: 'https://en.wikipedia.org/wiki/Potato' },
    { id: 9, category: 'Organic Vegetables', name: 'Onion', description: 'Strong and flavorful.', rating: 4.3, likes: 0, image: 'onion.jpg', link: 'https://en.wikipedia.org/wiki/Onion' },
    { id: 10, category: 'Organic Vegetables', name: 'Tomato', description: 'Juicy and fresh.', rating: 4.6, likes: 0, image: 'tomato.jpg', link: 'https://en.wikipedia.org/wiki/Tomato' },
    { id: 11, category: 'Leafy Greens', name: 'Spinach', description: 'Iron-rich leafy greens.', rating: 4.8, likes: 0, image: 'spinach.jpg', link: 'https://en.wikipedia.org/wiki/Spinach' },
    { id: 12, category: 'Leafy Greens', name: 'Lettuce', description: 'Fresh and crispy.', rating: 4.5, likes: 0, image: 'lettuce.jpg', link: 'https://en.wikipedia.org/wiki/Lettuce' },
    { id: 13, category: 'Leafy Greens', name: 'Kale', description: 'Nutrient-packed superfood.', rating: 4.7, likes: 0, image: 'kale.jpg', link: 'https://en.wikipedia.org/wiki/Kale' },
    { id: 14, category: 'Leafy Greens', name: 'Arugula', description: 'Peppery and flavorful.', rating: 4.6, likes: 0, image: 'arugula.jpg', link: 'https://en.wikipedia.org/wiki/Eruca_vesicaria' },
    { id: 15, category: 'Leafy Greens', name: 'Swiss Chard', description: 'Colorful and healthy.', rating: 4.4, likes: 0, image: 'swiss_chard.jpg', link: 'https://en.wikipedia.org/wiki/Chard' },
    { id: 16, category: 'Seasonal Berries', name: 'Strawberry', description: 'Sweet and juicy.', rating: 4.9, likes: 0, image: 'strawberry.jpg', link: 'https://en.wikipedia.org/wiki/Strawberry' },
    { id: 17, category: 'Seasonal Berries', name: 'Blueberry', description: 'Rich in antioxidants.', rating: 4.8, likes: 0, image: 'blueberry.jpg', link: 'https://en.wikipedia.org/wiki/Blueberry' },
    { id: 18, category: 'Seasonal Berries', name: 'Raspberry', description: 'Tart and flavorful.', rating: 4.7, likes: 0, image: 'raspberry.jpg', link: 'https://en.wikipedia.org/wiki/Raspberry' },
    { id: 19, category: 'Seasonal Berries', name: 'Blackberry', description: 'Juicy and rich.', rating: 4.6, likes: 0, image: 'blackberry.jpg', link: 'https://en.wikipedia.org/wiki/Blackberry' },
    { id: 20, category: 'Seasonal Berries', name: 'Cranberry', description: 'Tart and healthy.', rating: 4.4, likes: 0, image: 'cranberry.jpg', link: 'https://en.wikipedia.org/wiki/Cranberry' },
  ];

  filterCategories() {
    this.filteredCategories = this.categories.filter((category) =>
      category.toLowerCase().includes(this.searchQuery.toLowerCase())
    );
  }

  getFilteredProducts() {
    return this.products.filter((product) => {
      const matchesCategory = this.selected === 'All' || product.category === this.selected;
      const matchesSearch = product.name.toLowerCase().includes(this.searchQuery.toLowerCase());
      return matchesCategory && matchesSearch;
    });
  }

  selectCategory(event: any) {
    this.selected = event?.target?.value || 'All';
  }

  clearFilters() {
    this.selected = 'All';
    this.searchQuery = '';
    this.filteredCategories = this.categories;
  }

  removeProduct(id: number) {
    this.products = this.products.filter((product) => product.id !== id);
  }

  likeProduct(id: number) {
    this.products = this.products.map((product) =>
      product.id === id ? { ...product, likes: product.likes + 1 } : product
    );
  }

  shareProduct(link: string, platform: string) {
    const encodedLink = encodeURIComponent(link);
    const platformUrls: Record<string, string> = {
      whatsapp: `https://api.whatsapp.com/send?text=${encodedLink}`,
      telegram: `https://t.me/share/url?url=${encodedLink}`,
    };
    const shareUrl = platformUrls[platform.toLowerCase()];
    if (shareUrl) {
      window.open(shareUrl, '_blank');
    } else {
      console.error('Unsupported platform for sharing');
    }
  }
}
