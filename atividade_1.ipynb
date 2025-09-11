{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Construindo árvore fixa...\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'Digraph' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 75\u001b[39m\n\u001b[32m     73\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mConstruindo árvore fixa...\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m     74\u001b[39m fixed_tree = build_fixed_tree()\n\u001b[32m---> \u001b[39m\u001b[32m75\u001b[39m \u001b[43mdraw_tree\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfixed_tree\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mtree_fixa\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[32m     77\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mConstruindo árvore randômica...\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m     78\u001b[39m expr_random = generate_random_expression()\n",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[5]\u001b[39m\u001b[32m, line 8\u001b[39m, in \u001b[36mdraw_tree\u001b[39m\u001b[34m(node, filename)\u001b[39m\n\u001b[32m      7\u001b[39m \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34mdraw_tree\u001b[39m(node, filename=\u001b[33m\"\u001b[39m\u001b[33mtree\u001b[39m\u001b[33m\"\u001b[39m):\n\u001b[32m----> \u001b[39m\u001b[32m8\u001b[39m     dot = \u001b[43mDigraph\u001b[49m(comment=\u001b[33m\"\u001b[39m\u001b[33mÁrvore de Expressão\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m     10\u001b[39m     \u001b[38;5;28;01mdef\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34madd_nodes_edges\u001b[39m(node, parent=\u001b[38;5;28;01mNone\u001b[39;00m):\n\u001b[32m     11\u001b[39m         \u001b[38;5;28;01mif\u001b[39;00m node \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[31mNameError\u001b[39m: name 'Digraph' is not defined"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self, value, left=None, right=None):\n",
    "        self.value = value\n",
    "        self.left = left\n",
    "        self.right = right\n",
    "\n",
    "def draw_tree(node, filename=\"tree\"):\n",
    "    dot = Digraph(comment=\"Árvore de Expressão\")\n",
    "    \n",
    "    def add_nodes_edges(node, parent=None):\n",
    "        if node is None:\n",
    "            return\n",
    "        dot.node(str(id(node)), str(node.value))\n",
    "        if parent:\n",
    "            dot.edge(str(id(parent)), str(id(node)))\n",
    "        add_nodes_edges(node.left, node)\n",
    "        add_nodes_edges(node.right, node)\n",
    "\n",
    "    add_nodes_edges(node)\n",
    "    dot.render(filename, format=\"png\", cleanup=True)\n",
    "    print(f\"Árvore gerada: {filename}.png\")\n",
    "\n",
    "def build_fixed_tree():\n",
    "    left = Node(\"*\", Node(\"+\", Node(7), Node(3)), Node(\"-\", Node(5), Node(2)))\n",
    "    right = Node(\"*\", Node(10), Node(20))\n",
    "    root = Node(\"/\", left, right)\n",
    "    return root\n",
    "\n",
    "def generate_random_expression():\n",
    "    \"\"\"Gera uma expressão mais simples para garantir o parsing\"\"\"\n",
    "    operadores = [\"+\", \"-\", \"*\"]\n",
    "    operandos = [str(random.randint(1, 9)) for _ in range(3)]\n",
    "    \n",
    "    return f\"({operandos[0]} {random.choice(operadores)} {operandos[1]}) {random.choice(operadores)} {operandos[2]}\"\n",
    "\n",
    "def build_tree_from_expression(expr: str):\n",
    "    \"\"\"Parser melhorado para expressões simples\"\"\"\n",
    "    expr = expr.strip()\n",
    "    if expr.startswith('(') and expr.endswith(')'):\n",
    "        expr = expr[1:-1].strip()\n",
    "    \n",
    "    depth = 0\n",
    "    for i, char in enumerate(expr):\n",
    "        if char == '(':\n",
    "            depth += 1\n",
    "        elif char == ')':\n",
    "            depth -= 1\n",
    "        elif depth == 0 and char in ['+', '-', '*', '/']:\n",
    "\n",
    "            left_expr = expr[:i].strip()\n",
    "            right_expr = expr[i+1:].strip()\n",
    "            \n",
    "            if left_expr.startswith('(') and left_expr.endswith(')'):\n",
    "                left_expr = left_expr[1:-1].strip()\n",
    "            \n",
    "            node = Node(char)\n",
    "            \n",
    "            if any(op in left_expr for op in ['+', '-', '*', '/']):\n",
    "                node.left = build_tree_from_expression(left_expr)\n",
    "            else:\n",
    "                node.left = Node(left_expr)\n",
    "            \n",
    "            if any(op in right_expr for op in ['+', '-', '*', '/']):\n",
    "                node.right = build_tree_from_expression(right_expr)\n",
    "            else:\n",
    "                node.right = Node(right_expr)\n",
    "            \n",
    "            return node\n",
    "\n",
    "    return Node(expr)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(\"Construindo árvore fixa...\")\n",
    "    fixed_tree = build_fixed_tree()\n",
    "    draw_tree(fixed_tree, \"tree_fixa\")\n",
    "\n",
    "    print(\"Construindo árvore randômica...\")\n",
    "    expr_random = generate_random_expression()\n",
    "    print(\"Expressão gerada:\", expr_random)\n",
    "    \n",
    "    try:\n",
    "        random_tree = build_tree_from_expression(expr_random)\n",
    "        draw_tree(random_tree, \"tree_randomica\")\n",
    "    except Exception as e:\n",
    "        print(f\"Erro ao processar expressão: {e}\")\n",
    "        print(\"Gerando expressão alternativa...\")\n",
    "\n",
    "        simple_expr = \"3 + 4 * 2\"\n",
    "        random_tree = build_tree_from_expression(simple_expr)\n",
    "        draw_tree(random_tree, \"tree_randomica\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.11.4 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "5238573367df39f7286bb46f9ff5f08f63a01a80960060ce41e3c79b190280fa"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
