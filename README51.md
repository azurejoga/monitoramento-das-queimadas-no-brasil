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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f31e808b-e623-3e09-a98e-88c400f9593b | -17.14117 | -45.78789 | 2025-10-08 04:19:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30b8b78b-95df-32bf-bc7e-2a5d85ea5757 | -15.26072 | -46.33398 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d1f8e6f-3b77-33fe-b15d-eeb459965404 | -15.38056 | -46.28273 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27767e0b-fb23-30ed-9543-8f9fdd39307d | -15.30604 | -46.16141 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3552646-fba3-33af-a6c7-63adbf7bb487 | -19.33371 | -46.04137 | 2025-10-08 04:19:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab5d2605-5ab0-3a97-b7db-b17f0e77599f | -13.38949 | -47.56685 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c4ca1ae-86ac-32d9-bb6c-225d1e7d30de | -13.75039 | -45.75475 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 417caf83-fe9a-38c8-9a8d-33d6d4c07f17 | -14.71259 | -46.07593 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3db96e37-9d95-33d7-9485-fddc57a6eb44 | -13.72695 | -45.66568 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 040fa88d-f080-3747-a27b-49e641d07896 | -20.12167 | -44.41671 | 2025-10-08 04:19:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3434425a-77b2-3c2f-ab70-6042e1e90aa1 | -14.1472 | -43.17245 | 2025-10-08 04:19:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a725f0e-701c-32b7-94ff-7c04666000ff | -19.98629 | -44.24122 | 2025-10-08 04:19:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c2a536aa-5a95-34fd-b2ff-c26d0d94f0b1 | -19.88 | -44.30558 | 2025-10-08 04:19:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba25c7c2-b03e-3f63-bd60-e65eba08db48 | -14.7979 | -41.63327 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 93995597-f889-3567-a9c3-0890ccc7f6d4 | -19.30672 | -43.16643 | 2025-10-08 04:19:00 | NPP-375D | SÃO SEBASTIÃO DO RIO PRETO | MINAS GERAIS | Brasil | 3164803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 69a6da8d-0526-39b6-a75a-a80fd486f12c | -18.02954 | -44.94616 | 2025-10-08 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b866a7f9-e64f-3f09-a436-0eafa673d8f6 | -16.58395 | -46.55612 | 2025-10-08 04:19:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57be4880-51d1-36d6-9868-95484e9f9340 | -15.58842 | -44.50897 | 2025-10-08 04:19:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce94bc3-d2dd-3123-8356-76be20e650d7 | -13.3026 | -48.02781 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61422a4e-0462-3707-89cf-50aebaec162d | -7.81396 | -44.14012 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55979d48-53fc-3f6d-abbc-38cca3cdb88a | -15.26131 | -46.33034 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b81c213-ee85-3003-9e5b-42cb8f63219a | -8.23036 | -44.18129 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db7ab7f4-b597-3f33-b5b0-5cdb7b178eef | -15.31885 | -46.16742 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 741d6240-6632-34b2-8fed-f38cec48ca6d | -13.72783 | -45.70278 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce9c5a12-1f58-3a70-8789-7d384338368f | -15.98969 | -50.95168 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0d9bd8b-4fd8-3ba8-88af-7db39bbf9b23 | -13.73277 | -45.71471 | 2025-10-08 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f868695-f291-3cfc-a908-309580439a7e | -8.22868 | -44.19183 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2b78b5a-a950-3d04-861a-81a226da92f4 | -13.80222 | -45.80783 | 2025-10-08 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdebc8f9-2c9f-3ac1-8de4-5da0121cd509 | -14.69673 | -46.0812 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00e6e9dd-01ad-341b-913b-460cfe471084 | -9.08841 | -47.96585 | 2025-10-08 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 34200a54-e2b9-3827-b6c9-9465b35f9662 | -17.13699 | -43.46292 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57158566-4119-3408-a573-a97b15a8944d | -17.16237 | -56.59896 | 2025-10-08 04:19:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2d676650-c79f-3494-8b3c-b1563ea7951e | -15.99245 | -50.95996 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0691f761-ba83-3df7-8ebf-7f16d208196a | -20.19341 | -43.94991 | 2025-10-08 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 639651bc-e5c2-352f-b6b3-a462a66cc168 | -15.24705 | -46.35413 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7364a2b9-a3db-3d5f-9787-0d872c891d00 | -15.06463 | -49.48622 | 2025-10-08 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fecbe486-f41f-3bde-bf01-93c67d175dbe | -14.74624 | -47.8562 | 2025-10-08 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3b37f0-442e-3b59-bfdf-2db95700c7f5 | -19.59988 | -44.64818 | 2025-10-08 04:19:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c6b6a65-9a32-388c-bc60-bbd1c109e86a | -7.79103 | -44.21926 | 2025-10-08 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5dba8f47-86fa-341b-8778-968103e0f572 | -9.1745 | -46.92503 | 2025-10-08 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76a2267f-a84d-31af-b45c-99ff6f57b6b1 | -9.08689 | -47.9629 | 2025-10-08 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09c00718-0195-3940-8b68-f53153d901b0 | -17.93157 | -57.51189 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 05354d5c-ac92-394a-a894-fa6b0c314fa1 | -18.05591 | -57.52715 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cf8a4822-48b3-3448-a484-cef978236836 | -15.76243 | -48.72548 | 2025-10-08 04:19:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 02549f94-74f3-3944-bf10-03ab1185c726 | -17.96437 | -57.5064 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2fd32e4e-eba9-37b1-9d25-5bb1897a0ef1 | -9.16889 | -46.17887 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 258a765d-5a38-3511-99c2-279fcbed9b33 | -14.94015 | -46.79478 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7ec6aea2-7f12-3dbd-92b4-83274830e06a | -18.07948 | -44.45033 | 2025-10-08 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e949fa5-80bc-33de-8005-1665456778e2 | -17.97035 | -57.50962 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dd73e895-31b8-343e-8923-4f34c8aa8233 | -8.22815 | -44.17373 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c664cb6-1739-38ff-a69c-5033170debd7 | -16.06197 | -47.77361 | 2025-10-08 04:19:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de4150f3-5010-3410-8054-8f53023b05ed | -9.18973 | -47.79675 | 2025-10-08 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bc4b400a-8537-3500-8e04-24fe2934da82 | -18.05029 | -57.55205 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6f910393-d270-30d6-b455-6cdfc858fb3b | -8.69131 | -47.02615 | 2025-10-08 04:19:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| abe90458-a242-3af0-8d24-9044536a689f | -19.514 | -44.07568 | 2025-10-08 04:19:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3da917fb-7763-341f-8093-37835f4795c7 | -13.37432 | -47.55828 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 727114db-68c1-3442-b6fb-f31170f00874 | -14.71437 | -46.06502 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41b28344-16c6-311a-a29d-306cb51d0dc3 | -15.99316 | -50.9561 | 2025-10-08 04:19:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f881d304-92ee-3397-b223-e84a405cebda | -8.2337 | -44.18184 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 429ff7ae-76f8-32f8-94d0-b48439c32e98 | -20.08912 | -44.20382 | 2025-10-08 04:19:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4ee4b0e2-6165-3b12-a775-e5bc6c6aa54b | -7.54693 | -47.1948 | 2025-10-08 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42949919-7788-3f59-ab82-f32454663576 | -14.79547 | -46.07516 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c56c650b-ce98-3d56-9ab5-09126384c7f6 | -18.05185 | -57.54105 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ad8c8e8d-b051-3d05-a0fc-c645a684645f | -21.04003 | -45.6762 | 2025-10-08 04:19:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0839cd13-241e-3576-9686-f405bcabcb88 | -15.56503 | -43.84366 | 2025-10-08 04:19:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b04959d9-c764-36c7-b9dc-004d62225258 | -8.51968 | -46.286 | 2025-10-08 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4f143f16-bdd9-33ba-abd8-aa50829c3121 | -15.25438 | -46.35163 | 2025-10-08 04:19:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59c92d86-f5ee-3d13-bcc1-7dbc47437300 | -15.29181 | -56.92502 | 2025-10-08 04:19:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e6fe327-445a-35f6-bf16-d2c3764e26cb | -14.95532 | -46.80895 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 666f511b-03d4-3d7a-83d9-6d706f2627d2 | -18.35662 | -43.58424 | 2025-10-08 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51c91851-33e5-33bb-afab-64928ccdb145 | -15.86292 | -44.82799 | 2025-10-08 04:19:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8112c39-3062-3b79-ba04-9c1b7d1de6cb | -20.1211 | -44.42057 | 2025-10-08 04:19:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fa97ef7c-f5a4-3a07-b534-d4a24a71c658 | -17.82647 | -57.64124 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 9e55413a-5b0f-3d2d-a6f0-8d9799c38714 | -14.9224 | -46.79605 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faa9ce78-7f4c-37ae-a2f7-e2ba801d1f7f | -18.02466 | -57.52116 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 832ef18e-83fa-3ebb-a42e-933758ad1132 | -18.01783 | -57.52346 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 96f09eba-40f0-3902-a33a-5a3d0b3cf56e | -7.80218 | -44.21382 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 323685d3-3516-3851-8df5-68c1224c6163 | -18.05436 | -57.53403 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 3eee790c-54b6-32ef-a916-4f5d841594b3 | -14.52814 | -46.64444 | 2025-10-08 04:19:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7550d4f4-db76-37e0-b313-945415efde9a | -18.1343 | -40.25422 | 2025-10-08 04:19:00 | NPP-375D | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a24e1210-d510-39d1-b9eb-325a40fd99da | -14.55931 | -47.00011 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 667bdce0-2eb0-382a-b796-f749b9dc579e | -8.22032 | -44.20129 | 2025-10-08 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d935d8f7-9af1-34f6-a779-d6c917633ed0 | -17.14161 | -43.45566 | 2025-10-08 04:19:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c77ef0b7-0256-3a13-b055-580473e467d0 | -15.76997 | -46.25487 | 2025-10-08 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be4b0b61-3b35-3ed6-8317-9dc8668f3d44 | -17.56433 | -46.06433 | 2025-10-08 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79117032-28a2-3611-9e4b-40821cc3e6f4 | -17.9406 | -57.5284 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9f70b92f-f40c-3db9-b148-a4cb343cec53 | -15.06829 | -46.65445 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 994b4db2-c335-32ec-9954-8bd87889032c | -14.70621 | -46.08656 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71e453fd-7a25-396f-8495-7a32bc04081e | -8.15643 | -50.16528 | 2025-10-08 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f55dbf0c-0544-3b9a-bf7e-87ee04a48736 | -17.83109 | -57.64935 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| 867329fa-f078-30a5-993f-439507ce19a6 | -19.40139 | -44.3922 | 2025-10-08 04:19:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d8deb6c-b054-34d0-8ad8-c04dfd994d2c | -17.9996 | -57.49182 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 231f5d5e-24b5-3f1b-8680-29f33bd25a25 | -15.75578 | -48.74227 | 2025-10-08 04:19:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a73358a6-ae75-34d2-be10-52e40b116c8d | -18.01684 | -57.55656 | 2025-10-08 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a81489d7-7ff2-3f19-918e-872422007f14 | -13.46833 | -47.71978 | 2025-10-08 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c9202c7-effb-3f95-8cf5-b94e08b9af9d | -18.18698 | -46.21168 | 2025-10-08 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f2614f7-ae5d-3475-907c-2aa491168521 | -14.71021 | -46.0905 | 2025-10-08 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| df394b9a-7e0e-3442-9f3c-ce15cb951722 | -14.36698 | -47.73006 | 2025-10-08 04:19:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31d18ada-a8a9-348d-be9b-014b6e0f3f18 | -16.33339 | -47.0566 | 2025-10-08 04:19:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d9b9903-4674-3880-a507-ef0369c7eb06 | -15.08462 | -46.61895 | 2025-10-08 04:19:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README52.md)
