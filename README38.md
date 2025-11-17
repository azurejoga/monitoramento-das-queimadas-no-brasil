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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7af1c3b-313e-3c18-95d6-1698308d5b47 | -11.04208 | -45.07491 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 973b8e9f-389d-3ebf-a598-1c6c6e099332 | -11.93935 | -43.84832 | 2025-11-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59f30020-79b2-3226-850e-a2d02d584cc9 | -10.63761 | -51.76333 | 2025-11-17 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e721fce9-5b37-3b12-9bf2-f114b96549b9 | -10.51437 | -58.58066 | 2025-11-17 04:40:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bf81afc-ec61-3cd9-a9a7-61fa4054a8ff | -11.67893 | -44.7224 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d35cf3e3-17ab-37de-a75b-8df50b48beae | -10.79177 | -47.64389 | 2025-11-17 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8bdcafd-2062-3744-8ea7-f0a40b148c47 | -9.99314 | -44.7627 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a3cba01-4452-3533-b3ae-51fe22addfcb | -12.80237 | -46.43198 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cde42988-ff2e-333e-a2b5-5f9e26d2da50 | -10.94679 | -48.70238 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 910af364-8eac-3690-986b-1084cd6093e0 | -9.65134 | -43.90422 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c727d910-1646-3377-841d-b74ce30a8972 | -9.80497 | -48.56208 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95a859f8-bf3a-3573-9318-4a67405e19c6 | -12.19832 | -54.26917 | 2025-11-17 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2d1f0ba-e67e-39c8-b58a-22a6f011376c | -12.8641 | -46.03323 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cb0b578-da27-3365-bcff-5f5f22631154 | -11.96902 | -44.29683 | 2025-11-17 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 274d26b9-255b-321c-b4b8-b69d32fa299d | -10.51491 | -58.57779 | 2025-11-17 04:40:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4774c59-c073-390c-8038-ae780ae37c38 | -8.73594 | -48.32082 | 2025-11-17 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2868ce81-4728-3229-bbec-07f0bac33f03 | -9.32245 | -49.69305 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f214c364-af12-38ef-a6b8-b81d3aa17526 | -9.57907 | -49.11173 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 520c1c25-0f6f-348f-8c58-8f16ac56ca0f | -10.53486 | -47.91805 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0d90b37-fd44-3ea0-a9b6-5cf2664b2fc4 | -12.84732 | -46.01365 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f34ab241-d1fe-3596-845d-efeb63dee531 | -12.88876 | -46.4603 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc5763df-b563-3a3e-88bf-a16f7720ffbc | -11.81115 | -45.30906 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ea191bad-5de4-3b5e-b76a-4508746d95f0 | -10.10394 | -44.77373 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfe1f9d1-e483-30f7-8473-f1d742d3728f | -11.86069 | -45.22132 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a955e4d-e6fe-34db-8a87-7e4d278cc370 | -12.88493 | -46.45967 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdd07ba4-e52e-3c21-b841-42e781b6eb8c | -11.73305 | -49.84616 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d355ce9-a3ce-31bf-8b52-7d055d9bff0b | -14.78192 | -52.44963 | 2025-11-17 04:40:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65be783d-9801-3bb7-9cb5-25dd2e38ec70 | -9.72083 | -43.95958 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f58fc9d2-1d00-3d94-864b-45ffe7b97bed | -9.83509 | -44.60798 | 2025-11-17 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ceb6bf9-f2a2-30f6-af92-594b2457594b | -12.89012 | -46.45067 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69dfc59d-4e8e-3af5-837e-05849cebfa9b | -12.70061 | -46.77938 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13faa9d4-7e54-3332-8dcf-4e5fffd5d262 | -9.85857 | -44.18649 | 2025-11-17 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 879aeec9-5c77-3428-94fc-2789b5ce4be8 | -9.98851 | -44.76578 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 316d8f6a-997e-319c-9462-fcdf8df01ac2 | -11.16017 | -44.03626 | 2025-11-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd852168-4fd3-3d29-9600-f2fe81581736 | -11.46867 | -48.02919 | 2025-11-17 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd7b4a92-013d-3e51-a05e-038c66b807fc | -10.17318 | -44.53348 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40573490-9b37-3923-ad61-9fccaddbc290 | -10.91623 | -49.41163 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8bb7b321-f5ba-3e45-9e6f-c488483f3d91 | -11.16305 | -49.44322 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d559e03-c7f7-3484-8102-bf120f8c5b3d | -9.65452 | -43.91322 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| abf556a6-9386-3170-a718-6298ffe2135e | -12.80154 | -46.39515 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d937c5a6-c752-3b01-b893-3d0ae6c05af7 | -9.6551 | -43.90902 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5da6acfd-e3fd-3982-9d79-9191031ccbdf | -9.80159 | -48.56157 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ea485a7-36d5-3450-921b-a63175c0996e | -11.05585 | -45.15482 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa289941-aa67-35e6-a5ee-f195d41b9f16 | -11.66995 | -44.72517 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36c96fff-e7b5-3218-88e6-d465e65da170 | -12.85759 | -46.02174 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ad25426-8590-340c-9b13-d145162cb647 | -12.61826 | -48.44831 | 2025-11-17 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86cad343-066b-3e40-a473-a7b8d92d03fe | -12.40411 | -47.54674 | 2025-11-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f86bcc82-2e8d-3318-8298-c6d9f479ccce | -9.87139 | -44.18816 | 2025-11-17 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 610ad5be-cca5-3430-86f4-96049888b499 | -12.80943 | -46.43781 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a984734-a368-3b40-93f2-9a80bc067e3e | -10.85334 | -46.74601 | 2025-11-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e1bfb72-028c-3a14-b43c-b2a3b1aef3cc | -10.92364 | -48.69489 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 114f1dd7-7aff-3391-9279-0fc83d9ca85b | -9.71104 | -43.96672 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 201fe510-f44e-326b-9370-0c873f701633 | -12.80624 | -46.43239 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c227b252-e040-3de1-9cca-b22bfb9ac084 | -11.7051 | -48.86233 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5a2c7db4-cf67-323a-8d25-fa601a7d06b5 | -10.53759 | -47.91079 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 62c7a685-22f2-3e28-b7c3-e2f34d2bbca6 | -10.55688 | -44.8234 | 2025-11-17 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b0d78a4-2712-3b6e-ae6a-2ad9a24a4a5b | -10.1864 | -44.49924 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 659d9d5c-841b-38e9-b4ed-ea61d9c45100 | -11.05994 | -45.15527 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62ff2a06-a458-3156-b149-8ad09beda4a3 | -9.57852 | -49.11527 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6117971-ec48-3d57-82bd-68f5baa360a4 | -12.10007 | -53.27687 | 2025-11-17 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1986117-4a14-33f6-9377-0febfe955ac4 | -11.34378 | -48.90525 | 2025-11-17 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9498d60-0205-3e13-9514-20777c2b4636 | -11.91991 | -49.86876 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 840bb719-a9f2-3a0c-ada6-dbb77c5936fd | -13.81798 | -44.46006 | 2025-11-17 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1d5cca6-05b1-30f0-b8aa-721de09e99e8 | -11.70281 | -48.85439 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b3ae9e43-bd7e-3d75-891e-eb11dd2e8774 | -10.88382 | -44.63438 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f03cab26-355e-332e-a1b7-de1a6c85060a | -10.66378 | -49.37244 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 85e62451-15d3-382a-9434-01eb578f00b9 | -10.79125 | -47.6451 | 2025-11-17 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 575b56a5-3743-3cc7-95de-5500dee40a3c | -10.1554 | -44.50689 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b95ec6a9-7cd8-348e-a44e-0942e6d8a328 | -9.80214 | -48.55791 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f359d14-f986-3f1d-9f0c-86dba926e29b | -8.87071 | -50.18715 | 2025-11-17 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3cd5bb9f-cc2f-333f-b9d6-dee33b7f1100 | -12.80292 | -46.44075 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7b5b87b7-6c3d-3b85-befd-777114cdd2a9 | -11.70226 | -48.8581 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e299627-c2d7-315d-beed-34ce7ea4a703 | -12.21111 | -49.63319 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6320caa-92e8-3785-906e-364c8b5a25f1 | -11.71244 | -48.85967 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 464e84be-bd67-3869-ba5f-580c2247921b | -9.75172 | -43.95953 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 880ff6e1-db44-35de-be88-90bf072b7ee0 | -10.96786 | -44.52735 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38336642-85e5-3b1a-a119-bd363cb8ae26 | -12.88944 | -46.45551 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ee1940e-ab7b-337b-935a-90903b875984 | -15.86481 | -45.66395 | 2025-11-17 04:40:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f36b7203-67f3-398c-9301-6c5098026228 | -11.15917 | -49.44626 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26d3aef1-399b-36ca-8192-e283840576b9 | -11.70565 | -48.85863 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 808c64b2-1dbd-33e4-a008-240159388f91 | -11.80659 | -45.31209 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bc62965d-172b-33bb-99ee-31a07a7b164b | -11.62259 | -43.90362 | 2025-11-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 485aa38a-5f65-3e06-a296-0a37b1a0cc93 | -8.82865 | -47.36383 | 2025-11-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27c54879-1f4c-3045-8c37-9aecc63ee802 | -9.15592 | -47.5906 | 2025-11-17 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13d70eb5-0f1a-3755-b083-0a441c0efc2e | -10.537 | -47.91473 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 214eca56-2eab-37b6-b878-e247d9c203e7 | -11.41025 | -43.32051 | 2025-11-17 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea8a09fe-6464-3141-aedd-cfa2929a5474 | -13.322 | -47.37682 | 2025-11-17 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 392cfa50-3ae8-31f2-9b17-4df636cc14d3 | -10.9547 | -48.69602 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd40881-f9bd-391c-8d4e-a67f726005f8 | -12.80752 | -46.43608 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f368a049-7fc6-3f08-bd62-690bd7e3cb3d | -9.05224 | -46.00498 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4777d9b-d2c5-3a8e-b103-86c0042a663d | -12.81452 | -46.38698 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 368e1a4d-7923-3f44-b582-63b1d4b8470b | -9.65944 | -43.90961 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5493a5a7-e8a6-345f-8d08-ad0b8268a669 | -10.71233 | -44.50341 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00690606-59bd-3eb4-8b60-b480a8145299 | -10.66596 | -49.35822 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68ce8cd9-4fe6-32ce-958c-f16bf2f1175f | -10.52522 | -45.38237 | 2025-11-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75e8a383-d3c3-3cca-9bee-5f71bffe7990 | -12.86349 | -46.41628 | 2025-11-17 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b24c3189-3547-318f-93e8-a289c43ce4b4 | -9.81518 | -48.58607 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0480e72a-d26d-3e39-abf6-cd309610b011 | -12.00049 | -38.16582 | 2025-11-17 04:40:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 515c2638-700b-3cd3-a130-ffde10c12513 | -13.26764 | -47.31056 | 2025-11-17 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 943f5f82-32ff-36e5-84ee-e359feeb0ed1 | -10.13067 | -49.15077 | 2025-11-17 04:40:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README39.md)
