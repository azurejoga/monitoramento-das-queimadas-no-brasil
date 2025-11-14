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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14fb7ad8-39b5-3fd5-acd9-5d8cc4ccbd80 | -6.87844 | -47.24379 | 2025-11-14 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d0e38a3-fe70-392b-8a7c-d546fc6354f1 | -4.71357 | -42.94312 | 2025-11-14 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d1a9e993-3e94-3270-8ce5-b927ca7b4151 | -3.31078 | -49.15949 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9b81885-7953-3c90-b4e9-24af1bc0a24f | -1.37413 | -52.53119 | 2025-11-14 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9b3da65-5327-3510-bbdd-2d7e3354ef72 | -1.65797 | -54.27398 | 2025-11-14 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ff7ba80-e545-3819-8617-bf4d9a0e66c4 | -5.49099 | -47.69962 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9fede8a-0d59-33a4-af4d-0482d2fcd62e | -6.24018 | -46.24217 | 2025-11-14 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af624ae9-fa8b-3726-8522-dbf76fbaedd1 | -7.35265 | -43.36498 | 2025-11-14 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e86533b5-3466-3746-ad84-3a8818b726fb | -3.81772 | -44.24368 | 2025-11-14 04:44:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddedeea6-0f87-3bb5-854c-16fe4871ff1a | -5.85616 | -47.49012 | 2025-11-14 04:44:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 859053b9-5a09-3ddf-a34d-47243882898c | -2.97639 | -47.78838 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1683d2f4-0d3f-3845-b9a5-9290536b62ed | -3.2098 | -51.69176 | 2025-11-14 04:44:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 630d5627-77f9-3e8f-9cc8-bc99e1565cbe | -6.48086 | -39.34991 | 2025-11-14 04:44:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2dbd825b-9bc2-3905-b8c7-c068151b00d1 | -3.36001 | -48.40206 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2824e334-32ea-317f-aaec-4f01041c6f29 | -3.71588 | -54.03899 | 2025-11-14 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3286be10-c1b2-30b2-b014-1c0d13987c81 | -6.07247 | -41.57829 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2bb2b47f-0b35-39db-b50b-64248771194f | -4.10249 | -48.02076 | 2025-11-14 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6e7aa6c7-6d4a-3a37-b231-da2d8d6f38b2 | -3.91305 | -50.03869 | 2025-11-14 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c63c392-c911-3b0c-9f02-9f0b2081580b | -2.09032 | -47.98388 | 2025-11-14 04:44:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c5dd9a8-855f-35ef-8d51-51bc7fde664f | -4.64173 | -47.95103 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04869cef-9f2c-304c-a6c6-b1964bd1d9da | -2.72685 | -49.56602 | 2025-11-14 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fae445d-bb33-3e57-a749-30937b278059 | -4.4469 | -50.72594 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ce11d43-e578-37e6-a3a4-9f141bb14067 | -4.59765 | -46.53659 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 322faf27-3831-38e7-ab06-fe36d23897d9 | -4.61284 | -43.38479 | 2025-11-14 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e8e35b25-9a19-3c17-8487-96e595d6f3c7 | -2.38078 | -48.67817 | 2025-11-14 04:44:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 837cfb0a-bbd2-3a97-a591-eb1b9200edd3 | -6.9014 | -42.09011 | 2025-11-14 04:44:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9a765cfc-6a89-3de0-829e-26d8e20215f6 | -7.16998 | -38.45647 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 933bda74-6730-3f06-89a5-3856d7429153 | -2.28026 | -53.64504 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0715494c-4c18-34f1-8289-9a674abfacd8 | -5.25139 | -46.17944 | 2025-11-14 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47675755-f357-342d-85dc-796d9d9ad173 | -3.1986 | -51.37429 | 2025-11-14 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 200c75e2-b464-3815-8f0d-af3647d71c64 | -2.79975 | -52.97167 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be9c8f68-8738-38ba-8b73-5468a4e7c90c | -5.49158 | -50.45641 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9b2fcfe-0843-373b-998e-8c9082eb5a22 | -2.96052 | -45.76175 | 2025-11-14 04:44:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d91b0666-e3db-3385-b0fe-46e373bf3815 | -2.90149 | -48.06232 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 697bba9c-3afc-3bb0-b03d-dbbb2a4a17c2 | -1.49726 | -47.80641 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aae0bf3c-e84b-35d2-8be9-233a9833854e | -2.63206 | -47.30269 | 2025-11-14 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43f09884-4df3-36cc-a867-fcd160c248e8 | -2.28097 | -53.64069 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d9f7dfb-d067-3c6c-92fa-1b299da5b303 | -5.49726 | -41.91074 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce92c0aa-9a0d-316e-914a-4dca1fc7ca04 | -2.48472 | -54.12519 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5527a6c6-27e3-3cda-acad-24f1bdd7ee64 | -5.02486 | -41.10049 | 2025-11-14 04:44:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7194e591-43c0-3eb1-8b3b-d5ed4376a6b2 | -3.30076 | -50.10822 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fae58280-8517-3963-9520-65343036e031 | -2.65515 | -46.99778 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d0db16b-f875-3dfa-baf7-c5fae7cf8a25 | -3.01163 | -49.44003 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d9efce4-0848-32d0-a4b7-67a2759d29ea | -4.98699 | -43.88947 | 2025-11-14 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec8c5be6-6677-330b-aad0-6c2318b684bc | -6.15962 | -48.05248 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4fe9b9c-d1e0-3454-a75a-2d36ae1ce81f | -6.88184 | -42.85535 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1dd1aed6-0f57-3e8f-a5ec-4ddb9fb98580 | -4.53295 | -46.40064 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ab82d38-cf96-3ee9-8ad5-aa3b7c84dad3 | -6.07086 | -41.57813 | 2025-11-14 04:44:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c8e340b1-76aa-3164-b9de-4c92582fe2f5 | -1.90639 | -52.61976 | 2025-11-14 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fcc65b5b-ff36-3d39-9768-d6cf958a755f | -5.89016 | -42.75068 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 45adf70f-6d39-3101-807f-599bee92bfce | -3.07939 | -53.10249 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3000d6a7-10bf-3805-8bd1-dbe2fe61f592 | -5.41926 | -43.26096 | 2025-11-14 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6009d71b-1d5c-3bcc-9777-34bfb58cf99c | -4.1071 | -50.05827 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e2042c9-8d8d-33d6-8289-e7f63a7297e4 | -5.34519 | -46.76149 | 2025-11-14 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7278a2aa-2000-3a7d-a103-18ce5ba2f698 | -2.23765 | -46.07486 | 2025-11-14 04:44:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e870cb94-563d-3c39-9c0d-d72e35f6fcea | -4.93169 | -48.54913 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d563993-0248-369b-bcaf-edab4723ecab | -1.83058 | -53.79973 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 053a51a9-76dc-3f30-81b4-7df15b7dc3ea | -2.85248 | -53.00351 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d95b5a4c-9303-3080-9498-88f06373e3cd | -3.79759 | -52.01132 | 2025-11-14 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c27cb1fb-911e-364a-b1c5-83c9c7f7c050 | -6.09612 | -41.60737 | 2025-11-14 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e806f1d5-4678-34fa-9349-1402342f9991 | -4.71083 | -40.81408 | 2025-11-14 04:44:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5873f0a1-d734-319d-a0dc-09bbc0639b13 | -4.10379 | -50.05775 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a220c81-8fe2-3dfa-8d44-bdee4b0d4a15 | -3.2529 | -43.29235 | 2025-11-14 04:44:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8e4960c-86b6-336b-8b7f-db26f67d694b | -1.84033 | -53.79461 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12dfd76e-af66-3be9-b00e-d785a703dd60 | -3.76104 | -47.74754 | 2025-11-14 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27fbcba5-8c0b-30dd-be7b-00db7c1b78ea | -5.7495 | -49.26213 | 2025-11-14 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0cfcbde-dcd4-37e3-ae4e-05e16859bfe3 | -4.75162 | -48.82755 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2fa59c2-4f34-315f-a1e2-4a175567fbd1 | -4.64526 | -47.95151 | 2025-11-14 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 515e0f77-ed77-391e-a8cc-ddb8e6fafe50 | -4.97729 | -48.36115 | 2025-11-14 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d64b9c95-da9c-32bb-8635-22adf685c226 | -4.73104 | -46.72909 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e9f556d-f020-3cfd-a528-8f9ab6e9f83f | -3.74614 | -44.27553 | 2025-11-14 04:44:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56d1812f-6d9c-308f-bc5c-912ecc172354 | -3.35716 | -48.39783 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c8499c5-bfa4-3afa-825c-ab97e16f9674 | -5.52977 | -41.75542 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 46a46203-9633-3fd5-939a-19b12467dd7f | -3.42739 | -50.1671 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b0950bd-7800-3988-9591-0a949b4ded24 | -4.45568 | -45.82222 | 2025-11-14 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd7e868f-d75a-346b-94fa-c68aff8bda79 | -5.57171 | -47.10248 | 2025-11-14 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6cea3050-e690-3e71-b565-1f2ddd125c52 | -5.52398 | -41.75798 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ed1bd642-2df2-386a-8ea6-205b37f4a916 | -4.33384 | -50.81701 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d16ab41-2a84-3f9e-9521-e3eeb532e96e | -2.74994 | -49.52704 | 2025-11-14 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e396486-dc58-3453-90c7-e1a1dd4bfed8 | -4.75049 | -46.39398 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2959f09b-8fa7-38c8-88b3-89eec989de03 | -5.53367 | -43.68058 | 2025-11-14 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26f095e3-ce09-321e-878f-4cfeb13457c4 | -3.41537 | -53.53272 | 2025-11-14 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62fb8a4c-9c9b-3e0a-8dd8-6455b11a6e8f | -3.08184 | -49.27569 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9963df3-8c70-3718-ae1b-bc08b99841c1 | -6.88144 | -42.85823 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44087a3b-7fa1-3697-ac0a-b59d97f7c985 | -5.39885 | -48.31673 | 2025-11-14 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d54154a4-0c23-3389-885f-c2ba3656e6f7 | -5.33402 | -43.03595 | 2025-11-14 04:44:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e176a329-f7d6-374e-b345-fe97e8242534 | -4.98054 | -49.60186 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 541930c0-a3fb-34d6-9174-d8a62334759b | -7.15355 | -44.97449 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c221ea61-e13d-337a-afe8-00c8cece173c | -6.99388 | -42.78167 | 2025-11-14 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ee12b8a2-799e-3e0f-9ec0-df9820f6798f | -6.47826 | -39.34736 | 2025-11-14 04:44:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b172d416-7362-3f42-94f0-501f884919be | -3.53128 | -44.84699 | 2025-11-14 04:44:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d72d14c-0441-3fa9-91ea-f3b7c4ccc4e8 | -2.47132 | -45.1884 | 2025-11-14 04:44:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4a490690-8035-3d3d-8e58-6a22864cb27e | -3.32342 | -52.08243 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c20281f-a59d-3476-80f4-c9cc2d16ea1a | -3.47973 | -45.64722 | 2025-11-14 04:44:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3db23529-9d02-3985-982f-3e50dafbd218 | -2.93984 | -49.35748 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1e32f87d-4344-3ab1-81ea-1b04e620fdf5 | -6.10852 | -41.5977 | 2025-11-14 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ac2aafaa-9c07-34c7-b944-d78a026b7db8 | -5.03687 | -49.78372 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aaca9fb-dc52-3eb9-8983-165ebc053878 | -4.11703 | -50.05982 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49e67e53-af82-321a-9fae-44cd57b86df8 | -2.33314 | -55.69088 | 2025-11-14 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c9b0fb8-17a1-3e1a-8a0a-545064f15b41 | -7.46038 | -42.57999 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README42.md)
