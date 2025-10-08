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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2be357d2-22f8-3fef-aad8-7a9386d3bf79 | -6.7184 | -44.8092 | 2025-10-08 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a839868d-99d5-3355-87d8-2d18c7cb0a2e | -4.62377 | -47.41807 | 2025-10-08 03:47:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3365d6d3-5f0f-317e-9315-64fe7a9f71c7 | -7.73038 | -42.40638 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 429159f5-b42a-3314-ba71-791fcc4d76b2 | -4.50169 | -46.36613 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b1d46b88-520d-3116-a16b-18115e160200 | -5.61518 | -43.94062 | 2025-10-08 03:47:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a55a9dba-d0be-341e-a84f-0e93f9a6ffd7 | -7.82084 | -44.14227 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| cd40ae0e-4d34-31a7-a4ef-9f7933fdc468 | -4.50475 | -46.36814 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16720d07-993d-3fe1-b4e3-d62dc2e7249e | -7.81601 | -44.14259 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fbd33ba8-d798-31f2-b425-712ac907471a | -7.47724 | -43.127 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9bded670-6d01-3545-abbf-f7d8adfc54b5 | -7.44051 | -43.1474 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6cf756fc-4ae4-334d-bbe6-47c33b02d476 | -7.78484 | -44.21463 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7001b760-7da1-32cc-a8de-ce1413aac42e | -5.16534 | -46.22795 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dc74eef-0db5-354d-af6b-fb5e78691807 | -7.45635 | -43.04359 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 27e0fdcc-4fc7-3f62-bb80-7c2266cd3b5d | -7.02972 | -42.87438 | 2025-10-08 03:47:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 78802702-cdf8-37a7-a2dd-f1a7bab7a3e5 | -5.45573 | -45.87154 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f3bc085-a7c8-3075-b8a2-3d99f37ef719 | -4.05148 | -47.50372 | 2025-10-08 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72d2718f-7c5e-3c95-8751-ae72af29fe7d | -4.87328 | -46.82434 | 2025-10-08 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b7842ee-40fc-3838-84c0-0ee0841e2162 | -7.80798 | -44.24186 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c6ef2bc-a4a1-3631-9c9b-39ebdbee9076 | -7.44783 | -43.14332 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a793e1d2-f177-3667-949b-d599d48a5d13 | -7.7882 | -42.40942 | 2025-10-08 03:47:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aea7c678-c7f2-3533-8847-0510ec43862d | -4.94658 | -45.78999 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6435a73-cf4b-30ef-8ba5-580fec9c5fa0 | -5.16597 | -46.22441 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4cd8258-b65d-3481-b604-91e12ce72dd7 | -7.80892 | -44.1829 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89a45e75-5ec9-373d-8a5f-bb5f43901b31 | -5.71918 | -44.6598 | 2025-10-08 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ab54cb7-9cfc-368f-ac16-952c2b4c9008 | -7.24393 | -39.17962 | 2025-10-08 03:47:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5bcef14-504f-3673-9512-bcdcc4873ab9 | -5.59107 | -45.84187 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99abd993-c155-3429-b071-c92ea03962bc | -5.77678 | -45.74042 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e3de6ec-62fc-3845-926e-0c1a520a85be | -5.86844 | -44.30445 | 2025-10-08 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2661a8ba-662d-3a0f-81ef-23ac14b13512 | -7.79002 | -44.20927 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d64e9749-a8cc-3753-9a89-5e63a112c35f | -7.68887 | -42.40344 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e6b3b65f-d39f-3748-9bee-662d43880541 | -5.8306 | -44.97143 | 2025-10-08 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e611df0-c455-3c18-8a3c-4932e3fdd760 | -7.44207 | -43.15094 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0097f3c2-907a-31b3-b7d6-54feb490655b | -4.49907 | -46.36746 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8ba1f43f-7135-3d61-b7c2-6a339080ed0d | -5.82221 | -46.74681 | 2025-10-08 03:47:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 371952ed-939b-3d31-847a-4ba73f89b8c4 | -5.71039 | -45.68447 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a686ca48-bd12-3944-9fce-0f889cca37de | -5.74267 | -44.40562 | 2025-10-08 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f00175a-272b-356f-877c-bb0dcc66e058 | -6.25601 | -45.04541 | 2025-10-08 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fa0946b-6e15-34fd-bb94-c33e262bcba7 | -7.80883 | -44.23704 | 2025-10-08 03:47:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80034fe6-81a4-35bd-af59-f7d8d9b2f721 | -5.1428 | -44.95971 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1725a6f8-8c6e-37ba-a785-d36d69803599 | -5.36288 | -44.44527 | 2025-10-08 03:47:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d467b38-7871-3e50-bfde-8918419afcf1 | -7.43757 | -43.13843 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b6d240b-3882-3e4f-b90d-c352356f2149 | -7.67939 | -42.40969 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 06cb08ad-0a6d-3ca1-8ed5-e9f594f96265 | -7.1563 | -39.31078 | 2025-10-08 03:47:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6ae75aa6-1402-3cef-b442-e993d3e326eb | -7.69486 | -42.39303 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 280be9cb-6684-3dd6-a611-5c539790e0a4 | -8.84578 | -36.5717 | 2025-10-08 03:47:00 | NOAA-21 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 423900f6-92b2-3b81-af57-a68da2c9cd6e | -7.5228 | -44.09114 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c178de8-8fa6-3db2-b24a-64b87a0fa838 | -7.00636 | -42.88303 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 450af9b7-ff77-36b8-809a-ecca3446925a | -7.31687 | -39.25373 | 2025-10-08 03:47:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2fbb67d3-6b3f-3bf3-bce3-b2dddcebdab2 | -4.94805 | -45.59316 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26778a66-5c52-3d12-9589-c32ba8b1aa61 | -3.58128 | -49.44231 | 2025-10-08 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2eb375b1-dba4-3e3d-a0a0-bc43ce1b8f46 | -7.69549 | -42.38935 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3122f261-3743-331e-bdb6-c69671a68dc2 | -7.51699 | -42.71939 | 2025-10-08 03:47:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c9a8e4db-2d48-355f-9ce5-81732c096628 | -6.99987 | -42.86954 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d6ba7f09-c8e3-301a-8cd9-e70cd9eddb49 | -4.69068 | -46.47072 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1dc8c56d-35e6-39f8-9294-daa51c631ea1 | -7.68003 | -42.40596 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ee8ab6b-4693-320b-b497-6be83a5f92ef | -4.49411 | -46.36277 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd6ad186-a7fd-39de-815f-5065c6d6faeb | -6.65396 | -41.98913 | 2025-10-08 03:47:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 05c4e043-7c0a-3a10-8cac-052f15eb1094 | -5.71568 | -45.68524 | 2025-10-08 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a080679-3763-393b-8548-54a407f3f17b | -6.24126 | -35.08234 | 2025-10-08 03:47:00 | NOAA-21 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 03d6b12a-bb69-32e0-97a2-b6ccec07efdc | -7.79652 | -44.20171 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 505fc1ee-600f-31e9-acfa-5bc9b670663d | -7.35537 | -43.85937 | 2025-10-08 03:47:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e1098d8b-433f-36b5-921c-f43b772ff84d | -7.77413 | -44.19415 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7be9db1-ec0b-39e1-b6e5-21a41879c4f9 | -4.47855 | -49.71554 | 2025-10-08 03:47:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a75e4c2b-c9fc-3187-bd52-d26e16148e9a | -7.35373 | -43.86882 | 2025-10-08 03:47:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3c41da87-abf2-38a1-8f81-7f46d8cc1c4a | -7.731 | -42.40273 | 2025-10-08 03:47:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 630f1ef2-f834-343b-a4c8-4d8f8477f0d3 | -4.95335 | -45.59414 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54665430-cbd4-36f8-83a3-4eb7b0933075 | -6.64344 | -43.80011 | 2025-10-08 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f5918c4e-a900-39a4-83ea-2dceb4d485aa | -7.8168 | -44.13791 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81a3f54d-8aba-3aa6-9d57-573868494f04 | -7.47499 | -43.08866 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 23ebc7ab-daae-3d15-8478-4228074bc15a | -7.82056 | -44.17065 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 42bace8b-1d07-3994-bf6d-b4a9429310e3 | -4.91424 | -48.02187 | 2025-10-08 03:47:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f18775f4-0352-38a1-93ab-4ad5d5aa7ce3 | -7.40865 | -45.17378 | 2025-10-08 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1602e281-9ec2-3a50-b585-a78d2affda19 | -4.69146 | -45.84346 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cf2899e6-06d2-35da-9948-f32dc0217196 | -4.49803 | -46.35352 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3da08788-fa95-3725-95f7-12407ddee2fb | -5.8311 | -44.96857 | 2025-10-08 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1514a1d-d104-34ba-be3a-1c701f6f76b8 | -4.69466 | -45.83685 | 2025-10-08 03:47:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7ef12f06-ef46-327f-9fd0-d74cc3d2fe6d | -4.68277 | -49.49473 | 2025-10-08 03:47:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3e125d82-dd93-39fc-8cbb-69fdd56c87cc | -7.78917 | -44.21402 | 2025-10-08 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4246d799-c8d8-37b7-ac37-48e05a0978eb | -7.47787 | -43.09759 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 24052d00-2528-33c5-9506-fe09df078c10 | -7.39584 | -45.18891 | 2025-10-08 03:47:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ea8c919-1334-3fec-9e04-c49d6be8e740 | -4.50114 | -46.35571 | 2025-10-08 03:47:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 730152b8-e56e-3c35-99a2-fdb3f2ef0feb | -5.90175 | -44.56513 | 2025-10-08 03:47:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1cbf6f44-ef11-3855-8562-730cfb9eec4b | -4.85975 | -45.79541 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25c58fa2-0ab6-3a87-b813-29849c143246 | -5.70575 | -44.2188 | 2025-10-08 03:47:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d1bb4b23-4faa-313d-a999-4653f08d5df7 | -5.3936 | -45.20563 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83b5ec1c-3208-3580-bc60-3696ccd3794e | -7.44065 | -43.13366 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 51bddaf3-c658-3747-8765-9814e558619c | -7.45 | -43.13086 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 75f293bb-c50d-31f4-8cc9-226383094cb0 | -6.40938 | -43.47685 | 2025-10-08 03:47:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1c2efff-990a-30d7-9a8c-78568bbfffbc | -5.1423 | -44.9627 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6179c98a-6546-3bbc-826b-61c805c315bf | -5.13561 | -44.9714 | 2025-10-08 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a48a53e-094e-3aa0-b4b3-1ba9e56fa011 | -6.74302 | -34.96317 | 2025-10-08 03:47:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30772e76-a5e8-36ec-b63f-5e0a2cc3357a | -7.67536 | -42.58097 | 2025-10-08 03:47:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c43b8a63-61d8-36f1-a20a-766778a015d1 | -7.51348 | -42.71486 | 2025-10-08 03:47:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64c10bbc-28c0-332b-adb0-728be64306fd | -5.16067 | -46.92165 | 2025-10-08 03:47:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d089718-6729-3706-9d82-888f80612d73 | -5.16524 | -46.22961 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a67194a-835a-302e-b87f-0fd09c4f6787 | -7.79547 | -42.61372 | 2025-10-08 03:47:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7f1d0b9-436a-3b21-82b7-d8e2f6ef8641 | -4.85522 | -45.7575 | 2025-10-08 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b1cf96c-31ef-3df1-95d3-370af70354d5 | -7.45069 | -43.15237 | 2025-10-08 03:47:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 49d1a59c-566e-3d1a-bddf-611d24cd07b2 | -7.01198 | -42.87566 | 2025-10-08 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 3326e139-6659-3e0d-928f-549294bfdd92 | -5.01007 | -44.08167 | 2025-10-08 03:47:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README17.md)
