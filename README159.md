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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 519e5099-d1e0-38a2-a0b9-c52cafe73814 | -12.2329 | -44.6728 | 2026-10-10 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 1c9e7947-6576-3da0-bb37-c88d6fa58b22 | -8.7075 | -44.9086 | 2026-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 9e3412c6-5652-3c7f-92b6-3a67605b8c9f | -11.057 | -44.0092 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 97e96fde-5316-34e2-9284-3fbba56ccf25 | -11.47 | -43.3824 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| a897e326-eaca-388d-95c4-3ff043d1e855 | -11.0335 | -45.4016 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 63fa677d-1f23-3b16-b1f2-72db22a9082a | -11.2068 | -45.3091 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 2361f436-1c85-3a20-906a-d4d375373f26 | -9.0829 | -45.0957 | 2026-10-10 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1c31335f-dad9-3c09-91e4-a9fbbaccc89c | -11.7772 | -45.4806 | 2026-10-10 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 5b1c3ffe-c87b-3ef7-aa33-af54c30d030e | -10.9957 | -45.3839 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 1de943a8-e679-380d-b88f-5c80a8c180a0 | -10.9953 | -45.4068 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 6a9567b3-cd21-3e0d-951e-65d41cbb8aa7 | -11.8307 | -43.5866 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 81c8a766-122e-3f03-bfb5-5e2143179697 | -11.0379 | -44.012 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 351.8 |
| 6c34ee86-7108-3ffb-b258-255e69e9b889 | -11.987 | -43.4433 | 2026-10-10 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 75046a30-b249-3c55-a332-af2954f4d2e5 | -11.1873 | -45.3347 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 2d4be41e-dd9d-3f14-b7ec-31d36a542970 | 1.6754 | -55.6266 | 2026-10-10 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 51e97c6b-e023-37f3-af29-b77698495a84 | -11.5985 | -43.6935 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| dabe585b-a4d6-31ed-954c-5401e20a1f0b | -9.9211 | -44.7662 | 2026-10-10 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 7f475b90-870e-3488-a45a-fd0c2066eaf0 | -13.1827 | -54.3571 | 2026-10-10 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| d72def95-584a-3096-ba1e-630895edc72e | -14.9763 | -41.6703 | 2026-10-10 14:10:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 51f92d29-b740-3ffa-9cfb-be6400b4db42 | -10.8909 | -44.8001 | 2026-10-10 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d688106e-35eb-31bf-bf71-e2a3072ed9f7 | -10.4147 | -47.2846 | 2026-10-10 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 851bfc2a-4793-3cbc-8b9d-79f5b7fba24c | -9.9208 | -44.7893 | 2026-10-10 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 32b8bf3b-aa16-35b7-9735-0209da62d13b | 2.727 | -60.2586 | 2026-10-10 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 136.7 |
| a7f2702a-2828-3e77-8431-99c6c64c71d7 | -9.9381 | -44.9022 | 2026-10-10 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| cbb03c70-e53c-35bd-842d-b33c31ce2a92 | -12.8513 | -50.9957 | 2026-10-10 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 63d6196e-d9ee-3c24-8fbf-10ea929f5ba8 | -9.8795 | -50.5131 | 2026-10-10 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 299d30e5-8ad9-3dc3-8487-1895330ae8c0 | -11.0144 | -45.4042 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.3 |
| a4450199-274e-3b97-9d92-58ed313b7266 | -17.4581 | -45.0511 | 2026-10-10 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8d5968a5-a745-3dcb-9886-fe3bba23ea41 | -11.0187 | -44.0148 | 2026-10-10 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 133.6 |
| b1c557ab-3588-39d6-aa7e-97282f0f5dc4 | -12.1861 | -48.4124 | 2026-10-10 14:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d14ae077-8f15-3a77-8983-d746e5ca1698 | -12.0699 | -47.3632 | 2026-10-10 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| ba3450f5-688a-3324-82d3-69dd684dc1cd | -10.2317 | -46.8382 | 2026-10-10 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 624ab7fb-9064-341a-b209-dcc6f33e0a71 | -8.9116 | -45.1833 | 2026-10-10 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| a1c08712-219b-353a-8906-d076d99ee913 | -17.4568 | -45.0988 | 2026-10-10 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 1575eae3-0bbe-3b83-8190-f63e2eb49a38 | -11.8495 | -43.6072 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| a368a995-5d4b-3285-b579-293adbd29730 | -12.0646 | -43.4071 | 2026-10-10 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| f5edc69e-c9c5-3e6e-a9a4-0079ef68df01 | -15.0233 | -41.362 | 2026-10-10 14:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 117.9 |
| e2657ae5-0e7d-340c-86bb-0bf1ced14198 | -10.9579 | -45.3661 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2ff3a3f7-6223-3fa1-a6e1-fc601c4a0d07 | -11.6002 | -43.5989 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| afa38957-01a2-3bdd-9a9a-2a03477b0bc3 | -10.9097 | -44.8206 | 2026-10-10 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 066c0f30-5eec-354f-b674-adc8935b2e70 | -12.0063 | -43.4402 | 2026-10-10 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 278.6 |
| 04c78b04-322a-30ce-95cc-6fc32d77b63c | -12.0265 | -43.3895 | 2026-10-10 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 4f826fa9-f662-3302-afc0-1239d39893ca | -1.4487 | -48.9739 | 2026-10-10 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b91d1d64-7191-371e-88c5-f62b48769d70 | -11.3823 | -54.0434 | 2026-10-10 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| efa90931-0a24-33ef-b701-8c0c7c3c5106 | -11.5797 | -43.6728 | 2026-10-10 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| a5c920d1-05d7-39f1-b3e6-8789459eb948 | -10.9388 | -45.3687 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.7 |
| d87c2a50-1f13-34ba-85ac-1b2c2b0f4a7c | -11.1876 | -45.3117 | 2026-10-10 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| f6195802-e96b-361a-a49b-f712235495c5 | -1.64 | -54.44 | 2026-10-10 14:15:00 | MSG-03 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c8bfa6-af2b-390a-8dd6-07855fcb09a7 | -11.06 | -45.48 | 2026-10-10 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa973425-a641-3002-b2c9-a35745c7b769 | -11.05 | -45.43 | 2026-10-10 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6db9246e-c515-3119-8327-a6b70b5c5a30 | -1.64 | -54.38 | 2026-10-10 14:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a25ec7d-73bf-34bb-977d-07ace06b558d | -12.7072 | -43.0611 | 2026-10-10 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 273.6 |
| 2e1e3f6b-9814-3b24-81e4-3ffc7ea53ffb | -17.4568 | -45.0988 | 2026-10-10 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 06f4efe9-0272-3429-bf86-896dec6f0e6b | -9.9211 | -44.7662 | 2026-10-10 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 291.5 |
| d2608527-e0fc-3718-9659-db86c65cfe33 | -11.8787 | -47.3668 | 2026-10-10 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 7ca7a4dc-5c8b-39f6-88ab-8bc035e63a6e | -8.9778 | -45.8797 | 2026-10-10 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 57ce5a62-347b-346f-97f0-93946af91a8c | -12.4646 | -51.2982 | 2026-10-10 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 8a73e124-6b98-3437-8d28-738476199f09 | -10.4724 | -47.2333 | 2026-10-10 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 94838433-5e2c-3ce8-8d62-ccfc5127b883 | -13.1827 | -54.3571 | 2026-10-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d3dbecda-0a4e-3d33-bdf8-cfef238f5e28 | -16.6457 | -40.5501 | 2026-10-10 14:20:00 | GOES-19 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| 53fcbba8-1d60-3b22-930c-587e85c0c96e | -9.9395 | -44.81 | 2026-10-10 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 032963b5-70c8-3ba4-a437-14345e738232 | -9.9384 | -44.8791 | 2026-10-10 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 4a4bb4f0-83a9-3369-9b7d-64c5d5c3491b | -12.0063 | -43.4402 | 2026-10-10 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 346.5 |
| 5e7c61a3-213e-34c2-a2a7-2be64a2887a5 | -12.8303 | -44.6239 | 2026-10-10 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 386.8 |
| d3611d8b-5f5f-336a-bc88-d2e67d22fc82 | -11.3823 | -54.0434 | 2026-10-10 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 2898ff50-0592-37ca-9bb0-b97241fb1819 | -8.9311 | -45.1355 | 2026-10-10 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 01bd345f-2efe-3ce9-ade5-216ec80a0dfd | -1.1992 | -55.6712 | 2026-10-10 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b87f19b0-08ac-3e37-8fc6-666170680a89 | -10.2486 | -49.6851 | 2026-10-10 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 7d994d03-2bbd-3fc8-8f98-7d6ae1ca2664 | -9.9381 | -44.9022 | 2026-10-10 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 50ccc871-a666-31a6-94df-834c15b37e67 | -1.1094 | -54.1601 | 2026-10-10 14:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 03a4b67c-ff4c-3268-8a9b-0ba51a71c9a7 | -9.9208 | -44.7893 | 2026-10-10 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 6d9f0425-d3de-3f85-b127-02d869c8e162 | -11.2083 | -45.217 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 03f2e472-fb52-351e-9a71-2239c8a54c55 | -10.9953 | -45.4068 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 7329efab-4479-3a29-a334-32c258940eea | -3.234 | -42.6473 | 2026-10-10 14:20:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 765505be-dafb-3acb-b7e5-3285d72efca6 | -11.6951 | -43.655 | 2026-10-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f0615733-4c97-3ac9-8cd3-dc73186a1208 | -12.6873 | -43.0884 | 2026-10-10 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 223.4 |
| 9aeb560f-6894-3ab4-8bbd-c9ccc2dfc960 | -10.9579 | -45.3661 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.7 |
| 6fd3047f-60dd-3ebe-aeff-96374479c486 | -4.2965 | -43.0149 | 2026-10-10 14:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| cda14fb1-fc59-3bc2-a483-830479d97a7f | -11.1197 | -45.9602 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 5bd42f13-b1f7-3fce-ab2b-afc1a25f89c1 | -13.1636 | -54.3591 | 2026-10-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| d2ad697a-92dc-3067-b42c-8ff6d1eb3788 | -13.2018 | -54.3551 | 2026-10-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| d35579fc-b4e4-3750-b27f-a48afd49af2d | -8.0766 | -45.6112 | 2026-10-10 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| fa7920e2-9298-3981-9fda-3dfe8ac28158 | -10.454 | -47.191 | 2026-10-10 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 964fee1c-8e28-317c-a06a-b852a9cd61db | -11.0374 | -44.0355 | 2026-10-10 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 3cbeff21-c18c-3dbd-b687-a07059b4fc34 | -1.4487 | -48.9739 | 2026-10-10 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6d31e3b7-797a-38fd-a129-6a7321121d01 | -11.7772 | -45.4806 | 2026-10-10 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| c86a9bdd-b6e6-36e7-a91b-de813d22ad09 | -11.8692 | -43.5805 | 2026-10-10 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2ce777f8-d658-3360-bed2-27610f05d30d | -11.987 | -43.4433 | 2026-10-10 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 340.7 |
| e7f5d230-0dc1-3622-baad-252469591d67 | -12.0256 | -43.4371 | 2026-10-10 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 5007e003-b15e-3e16-86a4-7cf5d769ef88 | -1.4755 | -54.6363 | 2026-10-10 14:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 138d0c22-93f7-363f-8622-62f5decaa8f6 | -17.4581 | -45.0511 | 2026-10-10 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 129.4 |
| e75ec7a9-50d4-3d19-a329-7433ca49859b | -1.4671 | -48.995 | 2026-10-10 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5bb90877-5ada-32e0-966d-2cbec8b98e19 | -12.7067 | -43.0851 | 2026-10-10 14:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 297.6 |
| 3c2c361e-d230-36e8-b862-30fdc4a28c85 | -11.014 | -45.4272 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a757efff-8c4a-307e-9d99-e98a52af0c4a | -12.4837 | -51.2959 | 2026-10-10 14:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 8b8e3130-5789-3fc7-ab3e-863cf9efa4e1 | -13.1639 | -54.3385 | 2026-10-10 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| de19c3cf-c6f5-364d-a971-e59dc3dd0c35 | -10.9575 | -45.389 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| d9e29f9a-6115-3be3-88f3-a573373c7619 | -10.4144 | -47.3069 | 2026-10-10 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| bb14b4e9-22b9-3d90-817a-2f3a53e6bb9b | -11.0741 | -44.1237 | 2026-10-10 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3d6446d1-18ef-389f-be35-56cb7d52dd0a | -10.9388 | -45.3687 | 2026-10-10 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 295.5 |


[Clique aqui para ver as próximas entradas](README160.md)
