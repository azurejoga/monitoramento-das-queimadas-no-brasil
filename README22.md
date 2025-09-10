# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad8418d8-4e6d-3f1c-a87b-14a716361d8a | -6.85698 | -47.91536 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7074ad84-6649-3097-9aa6-e1816136803e | -5.82071 | -43.7251 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bd588c2-c687-38c5-b290-52397df05225 | -9.60745 | -45.7583 | 2025-09-10 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c6ef35-e7f0-3a0b-a21a-96c977b5245a | -5.4841 | -42.65792 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5bbc5563-ffbb-30a2-a7fd-c6eac941807a | -6.29061 | -44.21848 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd1e09ef-7e95-31ed-8956-600af8ccd701 | -6.44344 | -44.07021 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc6eeaa7-3087-3351-9aaf-e842f16f9e3a | -9.31401 | -46.72549 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8c4fed60-99d5-3761-affc-eeab335ee98a | -6.36596 | -44.49517 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3aab0547-ece9-3414-b247-fcb47613dfb3 | -5.93195 | -42.77772 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a999ce96-719c-3ba8-9146-0b9c75b1cd51 | -6.27699 | -44.4774 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 630523c4-1e96-3da0-a05a-4a67b3fcc6c5 | -5.96314 | -45.81173 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7b14731-0971-3ab4-9f5b-0df4b41b1e96 | -5.74226 | -45.25524 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dc030fb-5e9f-3981-afda-5358171f8171 | -5.72387 | -45.41195 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49259438-8fdf-36b7-8df1-50a24914bb09 | -7.77912 | -46.04965 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c512ed80-f15f-3f3c-860f-4220d14d4cbe | -6.39639 | -43.50475 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 221704bf-de24-3cd6-9392-b076a46a0385 | -6.85364 | -47.93523 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba589c9e-1bef-30a9-8107-70314da5b331 | -9.10434 | -46.98359 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84ac8b0d-e9a0-356f-86ed-8ef83321bb53 | -4.48107 | -48.11825 | 2025-09-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| afb35818-188b-35c9-b9a8-3070dfe8f07a | -5.79689 | -51.67617 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c3af7a8-dadc-3a3c-8760-8bfaeec1eea9 | -5.77251 | -45.52999 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57b93566-09e4-3c00-9033-f818afe8b299 | -5.3998 | -43.43853 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4da45d60-1774-3825-9445-eb7811710cba | -6.55894 | -47.4932 | 2025-09-10 04:14:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa8f9f05-8ccc-3b7b-bc01-810201677e8f | -6.16914 | -42.65205 | 2025-09-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d796aab-e177-3aa1-97b4-e4bd1d6d04f4 | -9.05712 | -50.47906 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04e94301-2940-3568-a3ca-6cde4edb5021 | -5.42856 | -43.98814 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8a43124-0e14-30c2-8d3f-245a367471d0 | -7.87067 | -46.0244 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0bd0140-3875-3420-a304-a74362216f99 | -7.07339 | -44.8617 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a30a119d-2a48-302d-aad3-97547768545e | -9.14813 | -46.05336 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e2ccff2-db7d-3f63-a937-0dd093f176b4 | -5.80752 | -45.28873 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bc62fec-d9f5-35f9-a35c-5213b33fcc80 | -5.8917 | -43.9435 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0278323b-b9c0-3232-a7bc-296b91943102 | -9.00926 | -49.52877 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2db777a8-2a1a-35f8-9660-e87baff0d16d | -5.6714 | -43.3544 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fe251b3-854a-33eb-934f-abbc732a1959 | -5.88783 | -43.94648 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 513e02a1-4c81-3a00-947d-60da423a2b69 | -6.44453 | -44.06327 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24efb0cf-c091-305b-ae76-00581bcf47ac | -8.04759 | -48.69284 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1799c4c6-2521-38f9-b085-90f604a24620 | -6.20604 | -43.50251 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 507e31ba-94a5-34cd-88b5-bf5be2dfd3f2 | -8.0255 | -44.50305 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1acbc67c-66bd-3562-b90d-a7e12294564a | -8.28072 | -47.46809 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ba72236-0660-32a5-ac4e-79ee329bfdfa | -9.08399 | -47.06173 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4a44ca3-f0cf-360f-8c18-f0c4cbb1a410 | -8.57629 | -48.95326 | 2025-09-10 04:14:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7403926d-29b6-36f6-9ee8-cc5797fbf97d | -5.91515 | -45.75168 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4e67fe9-bcd5-374b-b0fa-f32987312a75 | -6.44286 | -44.05228 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e45379e3-9c8c-34f6-9856-c7b9171d625f | -6.48041 | -44.00819 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffc11231-abad-30a6-83c4-6d5c9a08bd1b | -5.91966 | -45.81289 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a4234c7-33c0-33f9-829e-0070ac3fa8c3 | -7.78923 | -46.0631 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f6a415a-77ed-3ea0-ae2f-75fbe8d5efc8 | -5.42304 | -42.81077 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1210fbcf-69f6-358d-b14e-8a179b88b7b1 | -5.72515 | -45.60211 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c29663e8-e9be-30ec-bd80-3189db8f5d3b | -5.54888 | -43.0526 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c3f79a-63cb-31f0-bc95-4c0bdadfcd43 | -5.40976 | -43.46132 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e5472bf6-f116-3db7-9e67-896bfe0885d3 | -5.68239 | -43.34905 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d411e3d7-bf6a-3646-8828-cd1b63bfec3b | -6.18068 | -42.6432 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39b6a63c-d3a4-3988-afb4-99d2bd09cd4b | -5.72449 | -45.40814 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e715b7ad-a215-3d34-8b78-9c68b2ff68b9 | -5.78573 | -44.85115 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59b6c3e7-5668-3c4f-997e-96c0eccebaae | -8.16546 | -46.06681 | 2025-09-10 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9d16f54-7bd1-399d-957e-3c0cf6d8d779 | -9.44874 | -46.70208 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb9c9d8b-b1d2-341e-bbdf-bd3f7450c553 | -5.67588 | -43.9092 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28622356-7aa5-30dc-b8be-be3d5d9b3a52 | -5.57254 | -42.90115 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0ee25182-f22a-3d28-ac9c-8c3584c79e12 | -6.2006 | -43.32157 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66d2d7fe-753a-3321-9f93-999101cea085 | -6.25809 | -44.05886 | 2025-09-10 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28f2d930-1126-3977-ac4b-12c8eb729be7 | -5.53867 | -42.65929 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e8218a1f-a8a8-32ed-bf3e-480aed1565da | -7.93873 | -44.85594 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4224b0c8-5faa-30b9-a0bd-6915396de426 | -9.69731 | -46.82402 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2f90916-9d0a-3d97-8bba-8121a917b634 | -7.82091 | -45.12893 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae518976-cf16-32f5-a603-8c12aaf2367f | -5.9331 | -45.81907 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79f4d446-1151-3c7b-8b38-e1c9f8b2de25 | -7.55544 | -44.65616 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e859f00-2d94-386c-b67b-d4da373d04cf | -6.85058 | -47.92957 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 98aa3b41-9359-31cd-b344-7332945e1c57 | -6.35375 | -43.03888 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2081dc2b-522d-3da9-8156-2b81b1d3cf2b | -5.57538 | -42.92628 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fd551753-d87a-36a1-9376-dbe17a9923d3 | -8.07131 | -50.18377 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e1d7f3c-db4c-3b19-881f-3d288fd8bc05 | -5.42419 | -42.82506 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 606e283b-170a-36c8-8776-283bfdce5228 | -8.41772 | -49.12301 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbb5ec26-d0c8-37dc-9b1e-93b1d70ed630 | -7.24484 | -44.46848 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9244695c-82a6-31c8-8520-444320b1b646 | -8.20207 | -44.76347 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34d0b28a-369b-3839-8e3b-9ef24626cd7c | -9.31755 | -46.72607 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8d6d1ced-f51d-3369-9527-986c697e83ed | -7.7055 | -44.84472 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b53a19e-3eea-37a2-bcc2-b236c15760f7 | -5.87801 | -43.44695 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 774edf74-b751-3f63-8fd6-526c13c18364 | -5.53537 | -42.65878 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 10a3606c-b9e8-399b-9bc3-7d57cbbcf2c3 | -9.0592 | -45.75724 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 000c9944-efc8-3639-9794-ad976907bcd0 | -9.07846 | -45.76797 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad9741c7-4b9d-3bcc-9217-976cc984e90f | -9.51845 | -46.54192 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d137d8cc-3dde-3e8f-bd0d-2748c2ec94e0 | -5.89115 | -43.94699 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ada2701b-6c08-32fd-9194-7c80991a1927 | -8.48497 | -47.29816 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2dad9a27-0f26-3469-a484-e3eb71113fc6 | -8.75441 | -47.10123 | 2025-09-10 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bb9fd71-1026-3d90-aaf3-a8fe5098a7f3 | -8.04637 | -48.69999 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 55ab440c-1b51-3380-b4f1-dce5ddef302f | -5.66259 | -43.90714 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b8181ad-2fb0-3347-9f54-46de84408e68 | -6.25758 | -43.41579 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4f49b19a-b69f-3d5a-bbb4-9de394a71b0f | -8.10822 | -44.85779 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e13f1edb-0e4d-363e-913c-bce6547705e0 | -8.34529 | -44.84493 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf263d5d-3e75-3a61-aa30-2aef767052de | -4.72756 | -44.46095 | 2025-09-10 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7889219e-a10f-3f88-8647-b504c2485612 | -6.06345 | -43.13063 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a86ea769-9cb5-3ba8-b121-9d62bc702b6c | -8.5216 | -45.71354 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d271674-7fe9-3f7f-976d-21d1c5419749 | -6.06039 | -43.32775 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92b0472b-18a9-3794-8bc9-a2f035e0ff12 | -5.62237 | -42.8419 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ad47be7-a3ad-3e93-a730-bc2b0e90e80e | -8.85461 | -47.26621 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b12da30-d230-3697-b2d1-0f5db6f58ad2 | -7.71558 | -45.1497 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cca4a0a-d083-3e49-975a-730cee1d7228 | -6.16833 | -43.37651 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23b3ccb6-4a0b-3410-a8c3-f903fbdd3878 | -9.31463 | -46.72229 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 50fe7f06-4854-36c9-b334-5181b10b22ed | -9.14469 | -46.05278 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f692faf-907e-3ce2-8bbc-530e788c20e6 | -5.96926 | -43.70989 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3327ddc5-d884-34c8-b8a5-8ae46f352909 | -5.22321 | -43.69417 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README23.md)
