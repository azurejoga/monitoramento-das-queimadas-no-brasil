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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9748838-9867-34c9-b228-ab98e5d3c984 | -8.17118 | -46.50555 | 2025-06-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78b1429d-842b-344d-bece-21cc8daa52db | -10.65606 | -49.36402 | 2025-06-07 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8602df25-e056-34d3-93bb-01d6287a257a | -10.87725 | -49.54962 | 2025-06-07 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea1e4505-5825-34d3-89a4-f52b12e36ca4 | -6.19781 | -48.53854 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 613a7ca5-a15b-38b4-9145-e979f2d0425a | -6.96169 | -42.90889 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 156d0f44-17cc-362a-93a7-7652c358bf6d | -6.0654 | -44.2342 | 2025-06-07 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f34e687-c8ad-3211-b6af-d9c042cde265 | -7.7344 | -44.17591 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2c204b51-38fe-346e-8173-19833e7d6fa3 | -6.96252 | -42.90307 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e4d16a90-055e-376f-8c67-473165542642 | -9.40337 | -48.44156 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 30ec722a-7f65-339a-bbe7-913ede13c9d7 | -11.09103 | -48.46341 | 2025-06-07 04:44:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f8b3489-6706-37b4-b1c4-369973c7143f | -5.64463 | -43.71159 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2fb9068-d3d9-33ce-8fd2-2500ef6c7c1d | -11.02322 | -45.23501 | 2025-06-07 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4350a62-fdbe-3719-a3f0-b21085ded814 | -6.20898 | -55.63593 | 2025-06-07 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707e5eb2-d080-3b74-80a2-ffb68152d857 | -7.35553 | -50.4108 | 2025-06-07 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a0ce26a-e8b5-3ccf-8edf-250ffea5596a | -6.95087 | -42.91309 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e5ae060d-c064-36b4-89b1-e4735b02acca | -7.72975 | -44.17527 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9685804b-bba2-31d4-84f8-d1b67d41e690 | -4.7576 | -45.30696 | 2025-06-07 04:44:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abd82847-ae4e-3f3b-9eeb-438893c3c003 | -10.49627 | -53.66348 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| af580fbc-77b2-3a82-9e18-fb1344720fd9 | -6.94709 | -42.9036 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1af0f0ba-f5b2-3abc-8cce-62f55c59fd1f | -6.23785 | -48.55672 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff4fae27-ae75-3c35-8741-970c6db3be20 | -5.64393 | -43.71642 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c5a7737-6a4b-37b9-84fe-039c6b64c18a | -10.49566 | -53.66719 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2f7fc1b2-73f7-35e4-90a1-bcdd07163ffa | -5.6407 | -43.70595 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c2cb1f1-a7e0-3739-931c-64bfb16e135e | -6.29055 | -48.50007 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7aeacbe-daa8-37d5-9653-8ee292593684 | -7.71718 | -44.1635 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f59781e-18fa-3dcc-8022-f5573d6ab474 | -8.8375 | -49.38667 | 2025-06-07 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3538be8a-ed39-3bf0-ba55-a7454f85234e | -9.36699 | -57.43529 | 2025-06-07 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95cddb85-a6ad-39d7-ba6b-8961c8615414 | -9.40274 | -48.44577 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a730b31-c66b-3fcc-b916-c08449bd9a47 | -7.94701 | -49.76347 | 2025-06-07 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1f0d613b-5bbe-3cf0-9c38-497da2ebb137 | -7.72511 | -44.1746 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6a674f18-fb08-3ad3-b4cc-316d8d66724e | -8.20945 | -48.97997 | 2025-06-07 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9052f96a-ad62-3f88-8805-7242842c1f17 | -7.02491 | -44.59078 | 2025-06-07 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6415daba-7077-3e57-9eb4-fc5ef800e21c | -6.21596 | -44.50674 | 2025-06-07 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf24d2de-069b-3f22-a0cb-0a2eea2f0dea | -10.22514 | -51.64508 | 2025-06-07 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1fe8e50-282b-3995-b06f-9c0ff3b90aa7 | -10.4128 | -53.99931 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f344158b-109c-3515-a7af-aa2b9472b9a2 | -7.02041 | -44.5904 | 2025-06-07 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef141d5d-62a0-3779-a531-6f24dc122016 | -9.06619 | -47.14539 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bfc0aae8-9867-3450-96d3-0572445e9f06 | -7.18361 | -42.82005 | 2025-06-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9603e9fe-c1d0-3d98-8f1d-4b23c4680cd7 | -7.7405 | -44.16634 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ea29b23a-b8be-30dd-86d6-d38bdee9b9a3 | -10.3989 | -47.11349 | 2025-06-07 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e31c5c0e-4584-352a-995a-bcfe0dc8db10 | -6.94587 | -42.80248 | 2025-06-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a0f9ad2-be01-330d-9d85-93da69ef49a9 | -6.21089 | -44.51035 | 2025-06-07 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d93ed30-1d8b-3f8f-ac74-648f0b0888dd | -6.80577 | -41.73817 | 2025-06-07 04:44:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9ef78e5-f816-333c-a707-d0479ead5ed3 | -7.72114 | -44.16906 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6e8248d8-9b6b-3ff0-ad59-667b12483579 | -5.64927 | -43.71234 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30795760-521b-307d-a37b-dbc52d7cf7fa | -8.44907 | -46.48619 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2472314-1001-3431-89f1-f6bde89d460e | -7.20926 | -43.11267 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| edc04816-680e-3efc-80bf-192257977348 | -6.96128 | -42.9118 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b32b1e93-2556-3172-9b54-a2c0271889fe | -7.72322 | -44.15425 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 754aa993-580e-3ea6-b875-dd55694b1462 | -10.63081 | -49.43707 | 2025-06-07 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da174080-8197-362e-a511-a4f3c8f22718 | -8.59141 | -45.87436 | 2025-06-07 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d58adbc2-d395-35ba-a046-6d38f8b8b926 | -8.8735 | -50.18288 | 2025-06-07 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ec1023-3428-3882-a3bc-8c15368d8534 | -7.72579 | -44.16973 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8334763c-3ef6-3b6c-a071-eae4c055e290 | -6.28646 | -48.50353 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e06c2b20-3895-33cb-84c9-8f1976d5049c | -7.1832 | -42.82298 | 2025-06-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4f6866d4-7ca1-3a15-a8cf-debaff69f7e1 | -7.72907 | -44.18012 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e89a27ae-c99b-368e-a3ed-b9ca596e38c1 | -7.7165 | -44.16836 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44cc062e-92d5-3b0e-a9f6-1c1c551abd26 | -6.19432 | -48.53801 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 824a298f-9dc4-37aa-abfb-a6b818afa68f | -6.23265 | -48.5441 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a84e23b-3545-3816-aad4-49ce93e95cc9 | -10.48886 | -53.66609 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc266c97-c34f-38ef-9c59-f1494d48c297 | -6.95128 | -42.91017 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9d51f869-0e1f-39fe-8f14-56530f74df80 | -6.94627 | -42.90942 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0f37ade-ca1d-3ba0-ad0b-3b9f7d82ec7f | -6.95711 | -42.90514 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| ff8ad8a6-8d19-3f66-af6e-691e7cafbc66 | -10.87376 | -49.54909 | 2025-06-07 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59ee697d-58d6-3892-8c97-a22722aa6703 | -8.17568 | -46.50265 | 2025-06-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44b5c152-616a-3205-a4c9-d00a1ddff822 | -8.17168 | -46.5021 | 2025-06-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26d130ec-1cff-3007-9b39-6a8e5627a3bf | -10.49165 | -53.67034 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7825f47-6315-39a4-b263-51e800cc3199 | -8.1762 | -46.49917 | 2025-06-07 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df22bb26-59ea-3220-83ba-e289f7adf43e | -6.24192 | -48.55342 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eb341692-34db-3a9a-8259-b0125b5a4de6 | -6.28995 | -48.50409 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2741864e-b5c4-353e-9c85-6fba87ca4d52 | -6.22508 | -48.57022 | 2025-06-07 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac291dae-f4fe-391f-b0fc-a8f2083c4296 | -9.12891 | -46.87643 | 2025-06-07 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe640a17-aa01-3dbf-ba4c-dc40134f59fe | -9.07469 | -47.14161 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e24c8117-0e1d-35cb-8acb-ae3c7af75b7a | -6.20323 | -43.32753 | 2025-06-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f63e20de-2341-31a5-b2b4-e3465604dda6 | -7.18237 | -42.82887 | 2025-06-07 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4eaef74d-611b-31c5-9815-9eefb2523622 | -8.20886 | -48.98387 | 2025-06-07 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d38e6af7-a3ab-3106-beab-53e10f8c1b6c | -9.404 | -48.43734 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d9213729-0b34-32f8-8929-cefe81b0f9a8 | -11.81577 | -44.26011 | 2025-06-07 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8de0969-eac1-38d5-ac97-672a3002a934 | -7.01977 | -44.59485 | 2025-06-07 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2ba01c6-6107-32d7-8bea-4f6ab5718f47 | -9.07517 | -47.14373 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cbfc2303-bebf-3b40-acf3-32c7bb873b0f | -7.72719 | -44.15981 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 71f04065-e387-3804-b043-fca39e5b7bba | -7.85994 | -47.89805 | 2025-06-07 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0241b0f5-0a09-3e28-99d1-b2274ed40339 | -10.49226 | -53.66664 | 2025-06-07 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81407f5d-180b-3f82-aa0a-335fe229cb91 | -6.95169 | -42.90724 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 0f0efbd4-eb98-34ab-8dc3-4a750ad1723f | -6.2166 | -44.50243 | 2025-06-07 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f8908ae-5ff6-359f-995a-724e519d2ae1 | -5.64694 | -43.59684 | 2025-06-07 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0261e8bf-dd19-341f-82d5-c770e4d9803c | -8.06944 | -46.84438 | 2025-06-07 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1953ea21-7c65-3a05-a8e2-88680b78fcb3 | -5.64141 | -43.70107 | 2025-06-07 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd0af1a7-8dbb-31ff-81a7-3d0bbf0640c5 | -6.60069 | -43.895 | 2025-06-07 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e53b1094-1116-337b-90ba-432e0fe59a2e | -8.31575 | -47.91779 | 2025-06-07 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51e80e24-6330-37c7-b54d-2bbe41e01145 | -9.07931 | -47.13721 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 214e9520-1c69-32c9-94c6-b714dd80e4ba | -9.07007 | -47.14597 | 2025-06-07 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 893b36fd-59a2-306e-9fcf-53b2668d41a1 | -7.73581 | -44.16598 | 2025-06-07 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 16c3c257-9ded-3631-95cd-00d2fb54f4a4 | -9.33305 | -48.51696 | 2025-06-07 04:44:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af159dc0-c080-3566-a41d-94cacc742a1d | -9.5026 | -40.36452 | 2025-06-07 04:44:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 5a6ce70f-76f4-3962-8f5e-34af0ea5ca32 | -6.95587 | -42.91387 | 2025-06-07 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ff1b6c2-9636-3458-bfab-60ac1b23e769 | -5.77606 | -43.61258 | 2025-06-07 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ac70c568-8103-3235-8418-14e1a10ecf9e | -10.64122 | -44.4852 | 2025-06-07 04:44:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba083a47-8271-3302-b77b-f4f0c6b5edca | -9.49566 | -47.39266 | 2025-06-07 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a6095c2-719a-39e9-8982-b8f5c1aad248 | -9.62562 | -48.60137 | 2025-06-07 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
