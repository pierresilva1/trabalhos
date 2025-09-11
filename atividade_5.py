# -*- coding: utf-8 -*-

class No:
    """
    representa um nó na Árvore AVL.
    cada nó armazena uma chave, referências para os filhos e sua altura.
    """
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1 # a altura de um novo nó (folha) é sempre 1

class ArvoreAVL:
    """
    implementa a estrutura e as operações de uma Árvore AVL.
    """
    def __init__(self):
        self.raiz = None

    # ===============================================================
    # TAREFA 0: MÉTODOS AUXILIARES E ROTAÇÕES
    # ===============================================================

    def obter_altura(self, no):
        if no is None:
            return 0
        return no.altura

    def obter_fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def _atualizar_altura(self, no):
        no.altura = 1 + max(self.obter_altura(no.esquerda),
                            self.obter_altura(no.direita))

    def obter_no_valor_minimo(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def _rotacao_direita(self, no_pivo):
        novo_pai = no_pivo.esquerda
        subarvore_temp = novo_pai.direita

        # rotação
        novo_pai.direita = no_pivo
        no_pivo.esquerda = subarvore_temp

        # atualiza alturas
        self._atualizar_altura(no_pivo)
        self._atualizar_altura(novo_pai)

        return novo_pai

    def _rotacao_esquerda(self, no_pivo):
        novo_pai = no_pivo.direita
        subarvore_temp = novo_pai.esquerda

        # rotação
        novo_pai.esquerda = no_pivo
        no_pivo.direita = subarvore_temp

        # atualiza alturas
        self._atualizar_altura(no_pivo)
        self._atualizar_altura(novo_pai)

        return novo_pai

    # ===============================================================
    # TAREFA 1: INSERÇÃO E DELEÇÃO COM BALANCEAMENTO
    # ===============================================================

    def inserir(self, chave):
        self.raiz = self._inserir_recursivo(self.raiz, chave)

    def _inserir_recursivo(self, no_atual, chave):
        # inserção padrão de BST
        if no_atual is None:
            return No(chave)
        elif chave < no_atual.chave:
            no_atual.esquerda = self._inserir_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._inserir_recursivo(no_atual.direita, chave)
        else:
            raise ValueError("chave duplicada não permitida")

        # atualiza altura
        self._atualizar_altura(no_atual)

        # balanceia
        balance = self.obter_fator_balanceamento(no_atual)

        # caso esquerda-esquerda
        if balance > 1 and chave < no_atual.esquerda.chave:
            return self._rotacao_direita(no_atual)

        # caso direita-direita
        if balance < -1 and chave > no_atual.direita.chave:
            return self._rotacao_esquerda(no_atual)

        # caso esquerda-direita
        if balance > 1 and chave > no_atual.esquerda.chave:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # caso direita-esquerda
        if balance < -1 and chave < no_atual.direita.chave:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def deletar(self, chave):
        self.raiz = self._deletar_recursivo(self.raiz, chave)

    def _deletar_recursivo(self, no_atual, chave):
        if no_atual is None:
            return no_atual

        # busca o nó
        if chave < no_atual.chave:
            no_atual.esquerda = self._deletar_recursivo(no_atual.esquerda, chave)
        elif chave > no_atual.chave:
            no_atual.direita = self._deletar_recursivo(no_atual.direita, chave)
        else:
            # nó encontrado
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            temp = self.obter_no_valor_minimo(no_atual.direita)
            no_atual.chave = temp.chave
            no_atual.direita = self._deletar_recursivo(no_atual.direita, temp.chave)

        # atualiza altura
        self._atualizar_altura(no_atual)

        # balanceia
        balance = self.obter_fator_balanceamento(no_atual)

        # caso esquerda-esquerda
        if balance > 1 and self.obter_fator_balanceamento(no_atual.esquerda) >= 0:
            return self._rotacao_direita(no_atual)

        # caso esquerda-direita
        if balance > 1 and self.obter_fator_balanceamento(no_atual.esquerda) < 0:
            no_atual.esquerda = self._rotacao_esquerda(no_atual.esquerda)
            return self._rotacao_direita(no_atual)

        # caso direita-direita
        if balance < -1 and self.obter_fator_balanceamento(no_atual.direita) <= 0:
            return self._rotacao_esquerda(no_atual)

        # caso direita-esquerda
        if balance < -1 and self.obter_fator_balanceamento(no_atual.direita) > 0:
            no_atual.direita = self._rotacao_direita(no_atual.direita)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    # ===============================================================
    # TAREFA 2 E 3: BUSCAS
    # ===============================================================

    def encontrar_nos_intervalo(self, chave1, chave2):
        resultado = []
        self._encontrar_intervalo_recursivo(self.raiz, chave1, chave2, resultado)
        return resultado

    def _encontrar_intervalo_recursivo(self, no, chave1, chave2, resultado):
        if no is None:
            return
        if chave1 < no.chave:
            self._encontrar_intervalo_recursivo(no.esquerda, chave1, chave2, resultado)
        if chave1 <= no.chave <= chave2:
            resultado.append(no.chave)
        if chave2 > no.chave:
            self._encontrar_intervalo_recursivo(no.direita, chave1, chave2, resultado)

    def obter_profundidade_no(self, chave):
        return self._profundidade_recursiva(self.raiz, chave, 0)

    def _profundidade_recursiva(self, no, chave, nivel):
        if no is None:
            return -1
        if chave == no.chave:
            return nivel
        elif chave < no.chave:
            return self._profundidade_recursiva(no.esquerda, chave, nivel + 1)
        else:
            return self._profundidade_recursiva(no.direita, chave, nivel + 1)

    # método auxiliar para exibir em ordem (para depuração)
    def em_ordem(self):
        resultado = []
        self._em_ordem_recursivo(self.raiz, resultado)
        return resultado

    def _em_ordem_recursivo(self, no, resultado):
        if no:
            self._em_ordem_recursivo(no.esquerda, resultado)
            resultado.append(no.chave)
            self._em_ordem_recursivo(no.direita, resultado)


# --- Bloco de Teste e Demonstração da Atividade AVL ---
if __name__ == "__main__":
    arvore_avl = ArvoreAVL()
    
    print("\n--- ATIVIDADE PRÁTICA: ÁRVORE AVL ---")
    
    print("\n--- 1. Inserindo nós ---")
    chaves_para_inserir = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    try:
        for chave in chaves_para_inserir:
            arvore_avl.inserir(chave)
        print("inserção concluída (sem erros).")
        print("árvore em ordem:", arvore_avl.em_ordem())
    except Exception as e:
        print(f"\nerro durante a inserção: {e}")

    print("\n--- 2. Deletando nós ---")
    try:
        chaves_para_deletar = [10, 11]
        for chave in chaves_para_deletar:
            arvore_avl.deletar(chave)
        print("deleção concluída (sem erros).")
        print("árvore em ordem:", arvore_avl.em_ordem())
    except Exception as e:
        print(f"\nerro durante a deleção: {e}")

    print("\n--- 3. Buscando nós no intervalo [1, 9] ---")
    try:
        nos_no_intervalo = arvore_avl.encontrar_nos_intervalo(1, 9)
        print(f"nós encontrados: {sorted(nos_no_intervalo)}")
    except Exception as e:
        print(f"\nerro durante a busca por intervalo: {e}")

    print("\n--- 4. Calculando profundidade do nó 6 ---")
    try:
        profundidade = arvore_avl.obter_profundidade_no(6)
        if profundidade != -1:
            print(f"o nó 6 está no nível/profundidade: {profundidade}")
        else:
            print("o nó 6 não foi encontrado.")
    except Exception as e:
        print(f"\nerro durante o cálculo de profundidade: {e}")