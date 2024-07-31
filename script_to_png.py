import os
from pdf2image import convert_from_path

def convert_and_delete_pdfs(folder):
    # Проходим по всем файлам в указанной папке
    for filename in os.listdir(folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder, filename)
            # Имя нового PNG файла
            png_path = os.path.join(folder, filename.replace('.pdf', '.png'))
            
            # Конвертация PDF в PNG
            images = convert_from_path(pdf_path)
            for i, image in enumerate(images):
                # Если PDF состоит из нескольких страниц, сохраняем каждую страницу как отдельный файл
                if len(images) > 1:
                    page_path = png_path.replace('.png', f'_page_{i+1}.png')
                    image.save(page_path, 'PNG')
                else:
                    image.save(png_path, 'PNG')
            
            # Удаление исходного PDF файла
            os.remove(pdf_path)
            print(f'Converted and deleted: {filename}')

# Укажите путь к вашей папке
folder_path = './конструкции и теоремы'

# Запуск функции
convert_and_delete_pdfs(folder_path)
