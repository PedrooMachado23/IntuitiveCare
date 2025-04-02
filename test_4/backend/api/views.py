from django.http import HttpResponse, JsonResponse
from api.models import DemonstracoesContabeis
from django.views.decorators.http import require_http_methods
from django.db.models import F, Sum, Count, FloatField, Q
from django.db.models.functions import Cast, Round
from datetime import date
from django.db import connection

#Executa a query dos dados do último trimestre de 2024
@require_http_methods(['GET'])
def query_trimestre(request):
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT cad.razao_social,
                dem.descricao as descr,
                COUNT(*) as ocorrencias,
                ROUND(SUM(dem.vl_saldo_final - dem.vl_saldo_inicial)::numeric, 2) as resultado_periodo
            FROM public.relatorio_cadop as cad
            JOIN public.demonstracoes_contabeis as dem
                ON cad.registro_ans = dem.reg_ans
            WHERE lower(dem.descricao) LIKE lower('%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO%')
                AND dem.data BETWEEN '2024-10-01' AND '2024-12-31'
            GROUP BY cad.razao_social, descr
            ORDER BY resultado_periodo ASC
            LIMIT 10;
            """
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        
        return JsonResponse(results, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

#Executa a query dos dados do ano inteiro de 2024
@require_http_methods(['GET'])
def query_ano(request):
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT cad.razao_social,
                dem.descricao as descr,
                COUNT(*) as ocorrencias,
                ROUND(SUM(dem.vl_saldo_final - dem.vl_saldo_inicial)::numeric, 2) as resultado_periodo
            FROM public.relatorio_cadop as cad
            JOIN public.demonstracoes_contabeis as dem
                ON cad.registro_ans = dem.reg_ans
            WHERE lower(dem.descricao) LIKE lower('%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO%')
                AND dem.data BETWEEN '2024-01-01' AND '2024-12-31'
            GROUP BY cad.razao_social, descr
            ORDER BY resultado_periodo ASC
            LIMIT 10;
            """
            cursor.execute(query)
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        
        return JsonResponse(results, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

#Busca registros por nome_social
@require_http_methods(['GET'])
def search_by_razao_social(request):
    
    razao_social = request.GET.get('razao_social', '').strip()
    
    if not razao_social:
        return JsonResponse({'error': 'Parâmetro razao_social é obrigatório'}, status=400)
    
    try:
        with connection.cursor() as cursor:
            query = """
            SELECT *
            FROM public.relatorio_cadop
            WHERE lower(razao_social) LIKE lower(%s)
            ORDER BY razao_social
            LIMIT 10;
            """
            cursor.execute(query, [f'%{razao_social}%'])
            
            columns = [col[0] for col in cursor.description]
            results = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        
        return JsonResponse(results, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)