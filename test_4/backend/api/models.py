from django.db import models

class RelatorioCadop(models.Model):
    registro_ans = models.IntegerField(primary_key=True, verbose_name="Registro ANS")
    cnpj = models.CharField(max_length=20, verbose_name="CNPJ")
    razao_social = models.CharField(max_length=255, verbose_name="Razão Social")
    nome_fantasia = models.CharField(max_length=255, verbose_name="Nome Fantasia", blank=True, null=True)
    modalidade = models.CharField(max_length=255, verbose_name="Modalidade")
    logradouro = models.CharField(max_length=255, verbose_name="Logradouro")
    numero = models.CharField(max_length=255, verbose_name="Número", blank=True, null=True)
    complemento = models.CharField(max_length=255, verbose_name="Complemento", blank=True, null=True)
    bairro = models.CharField(max_length=255, verbose_name="Bairro")
    cidade = models.CharField(max_length=255, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    ddd = models.CharField(max_length=2, verbose_name="DDD", blank=True, null=True)
    telefone = models.CharField(max_length=20, verbose_name="Telefone", blank=True, null=True)
    fax = models.CharField(max_length=20, verbose_name="Fax", blank=True, null=True)
    endereco_eletronico = models.CharField(max_length=255, verbose_name="Endereço Eletrônico", blank=True, null=True)
    representante = models.CharField(max_length=255, verbose_name="Representante", blank=True, null=True)
    cargo_representante = models.CharField(max_length=255, verbose_name="Cargo Representante", blank=True, null=True)
    regiao_de_comercializacao = models.CharField(max_length=255, verbose_name="Região de Comercialização", blank=True, null=True)
    data_registro_ans = models.CharField(max_length=10, verbose_name="Data Registro ANS")

    class Meta:
        verbose_name = "Relatório Cadop"
        verbose_name_plural = "Relatórios Cadop"
        db_table = 'relatorio_cadop'

    def __str__(self):
        return f"{self.registro_ans} - {self.razao_social}"

class DemonstracoesContabeis(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(verbose_name="Data")
    reg_ans = models.ForeignKey(
        RelatorioCadop,
        on_delete=models.CASCADE,
        db_column='reg_ans',
        verbose_name="Registro ANS"
    )
    cd_conta_contabil = models.IntegerField(verbose_name="Código Conta Contábil")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    vl_saldo_inicial = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Valor Saldo Inicial"
    )
    vl_saldo_final = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="Valor Saldo Final"
    )

    class Meta:
        verbose_name = "Demonstração Contábil"
        verbose_name_plural = "Demonstrações Contábeis"
        db_table = 'demonstracoes_contabeis'

    def __str__(self):
        return f"{self.reg_ans.registro_ans} - {self.descricao} ({self.data})"