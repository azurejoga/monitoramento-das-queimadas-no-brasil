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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4f9f6b5-fb11-3973-8105-a86fa3305c11 | -4.03265 | -43.24897 | 2024-09-26 13:06:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 469fb6be-5795-36bc-8e0e-daf98c8dd2eb | -6.08218 | -43.68238 | 2024-09-26 13:06:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6e11e724-e9fb-3b2f-9d1e-869dcd18ecd8 | -5.62676 | -43.69289 | 2024-09-26 13:06:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 25fce821-b497-3745-be9c-54c1963a6a61 | -2.72122 | -46.73617 | 2024-09-26 13:06:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 10be1fa1-6766-3bcd-afc7-a2502d7921c3 | -2.71825 | -46.72503 | 2024-09-26 13:06:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ba6b4e3f-9437-3bba-acb9-64dadf36f955 | -2.19065 | -46.98668 | 2024-09-26 13:06:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 8681db31-85d8-30a4-89f4-eed1a106171c | -2.18849 | -47.00182 | 2024-09-26 13:06:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fd5a1750-0672-3ae8-9e9a-ead666721c73 | -4.10925 | -46.78438 | 2024-09-26 13:06:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 2790c0b5-0018-31a3-b671-80f1239a7341 | -4.10694 | -46.80145 | 2024-09-26 13:06:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 271.2 |
| 16bb1984-ba2b-38df-b2ed-c0930d665157 | -4.10464 | -46.81838 | 2024-09-26 13:06:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| ba7f9c66-c6a4-3978-852e-6f9b07be623a | -10.032 | -53.5065 | 2024-09-26 13:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 5e75c189-164b-3858-b624-127f3b08bad5 | -10.6456 | -45.8407 | 2024-09-26 13:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 652db835-9de3-3540-a181-1bd2174ef060 | -10.8348 | -45.907 | 2024-09-26 13:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 18ee950b-10c9-32d1-ad86-82dc06db846c | -10.8352 | -45.8843 | 2024-09-26 13:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.0 |
| db7c2506-cecc-31f3-94d5-8f1006c402c5 | -10.8525 | -51.1581 | 2024-09-26 13:06:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| bf932b63-9809-30c2-8e10-efe0d3e69093 | -11.1545 | -46.1597 | 2024-09-26 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2f33b646-a21c-30ef-b044-3e0266aa1b8c | -11.1354 | -46.1623 | 2024-09-26 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 6f57745b-323d-3982-a792-449f04e2f402 | -11.1542 | -46.1824 | 2024-09-26 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d11a2800-bee4-3f26-9eaa-281724ee67d9 | -11.212 | -51.1627 | 2024-09-26 13:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| be86c68f-9796-354f-af15-8afbeedef987 | -11.2123 | -51.1415 | 2024-09-26 13:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3dae8b63-9d25-3839-a153-602aac9e4580 | -11.4789 | -47.3082 | 2024-09-26 13:06:11 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| d258cdbe-2bc2-3143-9702-7f5bd5a4dec3 | -11.6988 | -47.8576 | 2024-09-26 13:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ec064d9a-bcb4-3fa9-b7fa-f0cb8e33aa71 | -11.7179 | -47.8551 | 2024-09-26 13:06:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 99392214-50ef-3ba6-b0cc-5a0e4f0e5b41 | -11.8613 | -49.6327 | 2024-09-26 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 65727f4e-5874-3dc6-810a-1036878b2d74 | -11.8419 | -49.6567 | 2024-09-26 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 72a6f99e-a666-3c4b-b603-3994bda313da | -11.8616 | -49.611 | 2024-09-26 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 83e0ee04-5310-330e-b3b7-7c7bd1b79932 | -11.8422 | -49.635 | 2024-09-26 13:06:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| a1f5a1db-a62b-3824-aadd-9ae0da941269 | -11.9365 | -47.3367 | 2024-09-26 13:06:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 700ef0a6-d9ba-3b0c-9fed-f664d2b7124a | -12.1802 | -42.4064 | 2024-09-26 13:06:14 | GOES-16 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 96.0 |
| fbfe2348-d429-3fa2-ac3c-f2383f8e213e | -12.2175 | -45.5074 | 2024-09-26 13:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 456.8 |
| d48db70f-c8b7-3bbd-bae0-f3266f609578 | -12.2367 | -45.5045 | 2024-09-26 13:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| db1c5d3a-4844-3867-8e7e-8a0717d794d1 | -12.2857 | -50.5294 | 2024-09-26 13:06:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| eaebb9df-1181-31c9-84bb-5b85baba4fdb | -12.4835 | -48.9224 | 2024-09-26 13:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 83f6fd10-031b-333e-9196-8f0354860af1 | -12.5026 | -48.9198 | 2024-09-26 13:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 157.8 |
| f9259d66-4520-3a2f-9bf8-d3e4eae9be75 | -12.5464 | -53.5147 | 2024-09-26 13:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 143d6469-4711-39d9-a0c9-40123ee186b0 | -12.7158 | -45.569 | 2024-09-26 13:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 9ace2e14-d6d5-3a18-a841-e56c553e3836 | -12.8102 | -51.1716 | 2024-09-26 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 2a2f2226-23b6-3952-85ca-1f94ab9da646 | -12.8297 | -51.1479 | 2024-09-26 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 378.2 |
| 0d88d045-cd07-30c1-b212-8df47ced01f4 | -12.7914 | -51.1525 | 2024-09-26 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 389.3 |
| 4f3e1245-2a01-31e9-a5c5-4c47ca47756d | -12.9516 | -45.3242 | 2024-09-26 13:06:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a09a631c-63c5-3440-90da-c8462c330b47 | -12.8106 | -51.1502 | 2024-09-26 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 512.9 |
| 590b9163-440d-3d51-93fa-592557005be9 | -12.8855 | -51.2477 | 2024-09-26 13:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e4c03a41-f8e9-393b-ba4c-c18a700dff78 | -13.1963 | -45.6308 | 2024-09-26 13:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 6bb156ac-e1e7-3933-8c71-740ea9ce7d4f | -13.1796 | -45.4952 | 2024-09-26 13:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 418.9 |
| 0b8936fb-d31d-33de-94f5-9a340739d183 | -13.1603 | -45.4983 | 2024-09-26 13:06:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| e1493226-1afb-3b65-83bf-b4e4c026078b | -13.1967 | -45.6077 | 2024-09-26 13:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3afc7619-2d16-337d-b659-04cb338fac2a | -13.2985 | -46.3247 | 2024-09-26 13:06:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 3a37f6bc-720b-3844-92b8-56809663d326 | -13.3179 | -46.3216 | 2024-09-26 13:06:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 73944cfe-3be0-3e2e-8eb0-a1f78397e240 | -14.57 | -45.7205 | 2024-09-26 13:06:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| d01060ac-eb43-33c0-b932-1cc90d20307c | -14.5705 | -45.6973 | 2024-09-26 13:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| a3a7bc0b-2bf8-386b-802a-ba1023df95d0 | -14.571 | -45.674 | 2024-09-26 13:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 897b9cc9-ed43-3898-9208-4a300bb8cdc3 | -15.6998 | -41.0835 | 2024-09-26 13:06:33 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 287.7 |
| 4f9d025f-ac89-31c3-a82d-8459ba5a1937 | -17.8068 | -43.2338 | 2024-09-26 13:06:45 | GOES-16 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 43952254-5c45-314d-9ee1-10e981c0a335 | -17.9929 | -44.4514 | 2024-09-26 13:06:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 7bc4206d-65f8-3f37-89f2-5255f0948217 | -18.9102 | -49.1674 | 2024-09-26 13:06:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.8 |
| f6af28d7-7a99-311d-ba17-5cf9472db00b | -21.2733 | -51.0061 | 2024-09-26 13:07:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 546.6 |
| 79c8eddb-fb73-38a6-a717-bb4dd2d0cec4 | -21.9374 | -48.5688 | 2024-09-26 13:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 1f3c970a-7dfe-38d2-9ab0-5a780d5bed94 | -21.9583 | -48.5638 | 2024-09-26 13:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 250.5 |
| 2b429333-1ccc-33dd-865b-16a28d3adbc1 | -21.9576 | -48.5873 | 2024-09-26 13:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 7519a028-4e53-316d-adbb-e4219dd1614b | -21.9381 | -48.5453 | 2024-09-26 13:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 59d71e2a-923c-3059-8d65-4d37aed26e58 | -22.2243 | -48.6625 | 2024-09-26 13:07:09 | GOES-16 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 339.3 |
| 262f0876-7bf1-3b1f-b14f-995598ad33b5 | -6.73406 | -48.64793 | 2024-09-26 13:08:00 | TERRA_M-T | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6d3c1e2b-66a5-3364-8ca4-ed883dd9264e | -7.58766 | -49.19811 | 2024-09-26 13:08:00 | TERRA_M-T | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f712cf1f-5e15-32e9-b639-e3b81fda957c | -7.58597 | -49.21044 | 2024-09-26 13:08:00 | TERRA_M-T | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0cd720eb-813f-3a9e-98f8-643f039d5599 | -8.75384 | -49.76859 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a63fbbc0-ad09-3cc5-bd8e-c62d47dec72e | -11.85593 | -49.61219 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a80dcccd-d9dd-3f9f-89a7-5bab5b4176e5 | -6.11653 | -50.96401 | 2024-09-26 13:08:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 167261e3-f505-3f06-8042-87fd3630bdb2 | -6.11449 | -51.11127 | 2024-09-26 13:08:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 19f695cf-d01f-3c61-937a-3d06740fd742 | -6.11315 | -51.12075 | 2024-09-26 13:08:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 264bc1ae-45d4-340e-9c9c-839070f44dc9 | -6.11246 | -50.99294 | 2024-09-26 13:08:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 548ba2d7-f3e3-3b56-9f17-4ed60b18932a | -9.3305 | -50.724 | 2024-09-26 13:08:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 41bcdad5-7a83-341f-b55c-1bf1201bcb36 | -9.32898 | -50.73538 | 2024-09-26 13:08:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5ae10464-2b08-319f-a40d-3cbe0b5d4022 | -9.32695 | -50.7289 | 2024-09-26 13:08:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 20209a3b-641a-379b-8ab0-77503e78d8a9 | -9.14004 | -51.52087 | 2024-09-26 13:08:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| fa62b1c3-e6dd-35fc-b69e-308efb48ebb3 | -9.13868 | -51.53074 | 2024-09-26 13:08:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5c37576b-e0e1-314c-9003-a22c77ffaf4a | -8.04183 | -50.42411 | 2024-09-26 13:08:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| b4c8d969-ecb5-3928-bd54-e1a49e13ce1d | -8.04028 | -50.4353 | 2024-09-26 13:08:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 191e85bd-c39b-3c3c-93f8-660d04545e93 | -9.42474 | -51.45753 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| f1e21360-889a-38dc-a6e0-a7ecafbea766 | -9.42338 | -51.46751 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 179.7 |
| a5f20d91-97b5-3191-a55c-91eb0344eada | -9.422 | -51.47754 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ee052fef-296e-364a-94f5-c875ef0501a8 | -9.41539 | -51.45636 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1348af90-0e02-3a86-8735-1a87adb55d27 | -9.41402 | -51.46636 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 24de0b80-5489-36ff-a9c0-f9ee09d840ab | -10.61358 | -51.11535 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| f5483d08-cda8-31c9-9548-203ccde7cd6d | -10.61212 | -51.12606 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1aa24b77-b5a0-3f97-8ca1-05e6bece7552 | -10.50706 | -51.15007 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 3f41e946-02d7-3ceb-a556-8cb0ee7a4759 | -10.4777 | -50.76247 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 24f3d0b7-39b9-34c2-a4f7-826f29f351c8 | -10.46633 | -50.7725 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 1475b1e4-5a38-3818-ad52-880e51f1b8a2 | -10.46486 | -50.78341 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 36273057-2526-3722-99ba-b6e8d084340f | -11.21388 | -51.1413 | 2024-09-26 13:08:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 9b267d24-e0f8-32f8-b420-2241f8ad9a2d | -11.21244 | -51.15216 | 2024-09-26 13:08:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a9182298-356f-349e-9ad2-d254c7981f51 | -11.211 | -51.163 | 2024-09-26 13:08:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 78a11056-83cb-303d-bd29-2112c6638507 | -11.06046 | -51.42235 | 2024-09-26 13:08:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1ae17361-6f0f-3baa-82d7-22f32fe42c23 | -11.05901 | -51.4328 | 2024-09-26 13:08:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 826a9e63-cc43-3f08-a917-7fd3411a2700 | -8.90963 | -52.76814 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d46ea24d-d161-3350-bf1f-a1d7d13e335f | -8.7347 | -52.05414 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f8431d6c-f7c8-3d10-8dcf-4e605335b02d | -8.72562 | -52.05298 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 75289be5-6546-3988-a00e-69bffb77bb03 | -8.66641 | -53.17773 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 120528a1-f63b-30da-b796-655c516e71f7 | -8.66512 | -53.18665 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| aa3e1a89-9ffa-3d8f-86ec-f24cd92d4cf4 | -8.65767 | -53.11281 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6deeaf1d-846f-32e9-a207-eca3eb2020e3 | -8.65625 | -53.18539 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |


[Clique aqui para ver as próximas entradas](README181.md)
