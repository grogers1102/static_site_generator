import os
import shutil
from block import markdown_to_html_node
from htmlnode import *
from extract_markdown import extract_title

def copy_dir_to_other(source_dir, target_dir):
   try:
      if not os.path.isdir(target_dir):
         os.mkdir(target_dir)
      print(source_dir)
      print(target_dir)
      if os.listdir(target_dir):
         print("Cleaning target directory")
         shutil.rmtree(target_dir)
         os.mkdir(target_dir)
      source_content = os.listdir(source_dir)
      print(source_content)
      for file in source_content:
         print(f"Checking {file}")
         file_path = os.path.join(source_dir, file)
         print(file_path)
         if os.path.isfile(file_path):
            print("Attempting to copy")
            shutil.copy(file_path, target_dir)
            print(f"{file} copied to {target_dir}")
         elif os.path.isdir(file_path):
            print(f"{file} is a directory")
            copy_dir_to_other(file_path, f"{target_dir}/{file}")
   except Exception as e:
      print(f'Error: {e}')

def generate_page(from_path, template_path, dest_path):
   print("Generating page from {from_path} to {dest_path} using {template_path}")
   with open(from_path, "r") as f:
      markdown_content = f.read()
   with open(template_path, "r") as f:
      template_content = f.read()
   html_node: ParentNode = markdown_to_html_node(markdown_content)
   html_content: str = html_node.to_html()
   title = extract_title(markdown_content)
   html_file = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
   if not os.path.isdir(os.path.dirname(dest_path)):
      os.makedirs(os.path.dirname(dest_path))
   with open(dest_path, "w") as f:
      f.write(html_file)


def main():
   copy_dir_to_other("./static", "./public")
   generate_page("content/index.md", "template.html", "public/index.html")
main()