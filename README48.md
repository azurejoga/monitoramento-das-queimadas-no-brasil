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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9634718e-db3b-3373-8243-7f3f3e1d3a22 | -17.5882 | -57.4711 | 2024-11-16 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 11d82e31-e3f8-3842-904c-0a9ba7d78675 | -15.9028 | -59.254 | 2024-11-16 04:50:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| ca489d48-7f27-3b91-9000-acfa8caeb509 | -3.7394 | -45.6523 | 2024-11-16 04:50:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 565cbee1-c322-3062-8d33-0d9f62f779fc | -15.9025 | -59.2741 | 2024-11-16 04:50:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3c40a31d-64eb-3c88-906f-3123112af4fc | -15.9219 | -59.2722 | 2024-11-16 04:50:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5c34210a-aff5-31f9-8ac2-2c6ffd53cdaa | -17.235 | -57.4516 | 2024-11-16 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 3ce64272-a0a9-3c03-8362-21912b3bdc33 | -2.2299 | -53.6219 | 2024-11-16 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 359868af-2c9e-388d-a215-831128de1aaf | -16.958 | -57.6269 | 2024-11-16 04:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 01a5c985-78d5-3001-b0c0-d99e9f1e5310 | -17.5675 | -57.5351 | 2024-11-16 04:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 6ac11138-b985-34eb-a472-c72699ba43f4 | -2.2299 | -53.6018 | 2024-11-16 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| af55b98b-65d6-32a4-89f1-c652c8fe3ff0 | -4.23812 | -48.34906 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0306468-2464-373e-8557-39c175519943 | -5.90616 | -46.23182 | 2024-11-16 04:50:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 63c38ba5-577b-3fbb-96d4-b8f7e06719bc | -3.56185 | -50.25151 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 812f9cb3-30d7-357d-b227-139969ad1544 | -4.61727 | -45.34615 | 2024-11-16 04:50:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6e293f1-967f-3ebf-be52-0f9717e7739c | -3.95871 | -50.02037 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b578073-ad6d-3191-ac6c-159c7300d3ab | -4.15022 | -50.76859 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27306d2d-1232-3097-88db-61951897276a | -3.3922 | -51.57323 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75228151-7626-3eed-8435-c2844ecbe614 | -3.56412 | -50.23695 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7386c25-48f5-3ac7-a9a7-8a171444d044 | -4.37769 | -48.56644 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6e67bef-cd70-30dd-9321-57ea68619a9e | -5.95158 | -44.46426 | 2024-11-16 04:50:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f8c46fd-7a9b-3731-b064-d1dacbd52e7f | -4.55545 | -45.76091 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5483a35-03ac-36dd-a34d-5565c07792a3 | -3.56355 | -50.24061 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bf348e9-1f98-3551-bd71-2460f4ae7b7c | -6.40899 | -47.51763 | 2024-11-16 04:50:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 699aa499-b1fa-37d7-8bd5-60e73c7f4651 | -3.69919 | -50.20117 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32d6da5f-447f-3640-a83e-ded96e478359 | -3.5692 | -50.24894 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e11efee-9a94-39ea-b3e9-b861cc09bdb9 | -5.6582 | -45.20234 | 2024-11-16 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37c337cd-7e09-3138-971c-9107a6591650 | -3.56406 | -51.64616 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea35cc99-9d59-342b-a4a6-bfd883e6fe73 | -3.56637 | -50.2448 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd962406-4157-3992-b8bd-a22c1141fd15 | -6.16928 | -41.17025 | 2024-11-16 04:50:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c846606-77d5-3e2e-8266-3794ddc8ec58 | -3.92718 | -52.25543 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 170459a4-cd83-39e8-9186-1ef071753855 | -4.27857 | -48.20839 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 102f9e88-ef83-3c22-98fa-cbbad685e912 | -4.22154 | -50.67633 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5466c47-9c08-3261-b9de-fcfbdd649125 | -6.02079 | -48.03811 | 2024-11-16 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5acc7e3a-9d34-3613-b13c-f3fd1cdde7a6 | -4.13471 | -49.36316 | 2024-11-16 04:50:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d2a4f29-c361-3906-844a-b914701960fb | -3.42775 | -51.67038 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 374b2ecc-0083-3c0d-a1ef-29ad3c90515c | -3.96615 | -49.99474 | 2024-11-16 04:50:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eed34c70-5b3e-3109-acf1-08ad00d45151 | -3.55845 | -50.25101 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee95acab-7d1b-32cc-b6a9-19bf2fdedc3a | -3.53636 | -50.45868 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10d43be7-5217-327d-95e9-b7341054b46d | -4.10558 | -46.87418 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7603b52-313f-33cd-ae4f-830aef4d0376 | -4.77817 | -50.92267 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20091819-7dca-3c7d-b499-bf74c916fee9 | -4.98862 | -44.32326 | 2024-11-16 04:50:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4b2dee3f-c0f4-3d04-983e-9a37d1d1a842 | -10.66611 | -44.49617 | 2024-11-16 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bce8f0a9-f966-3c02-8994-01b954c13c7a | -3.56524 | -50.25203 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23271fa5-43e5-36a9-9fa6-1155b311fc3a | -6.66442 | -47.88036 | 2024-11-16 04:50:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a055c5af-7e59-3234-b08d-1f0503ac9661 | -4.95344 | -44.72829 | 2024-11-16 04:50:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1719b2ad-a4a3-3901-a719-32de09123d16 | -4.36901 | -45.62556 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e503a43-8932-3bff-aaa6-2903a8736e58 | -6.02468 | -48.03866 | 2024-11-16 04:50:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f95ec64e-eec6-360c-977e-739b8dcf02f8 | -3.89053 | -50.25586 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b98d487d-9cb2-3f39-aa11-7ac245f2acce | -5.33102 | -40.90197 | 2024-11-16 04:50:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1399eed6-4c43-34c2-ac13-05ea959fb956 | -6.43863 | -47.86336 | 2024-11-16 04:50:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2d69645-1209-32bc-9330-89d64c5cb7e0 | -2.96701 | -53.87781 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9a7a37e-32ea-348b-8b39-f0bc3dd5c923 | -3.74072 | -50.18506 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8546e37d-1628-39e0-bbad-ef9828bbe2cb | -3.87728 | -52.26928 | 2024-11-16 04:50:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 911e9be2-a3ea-3260-bb8f-a28b3bc73e0a | -4.21894 | -46.813 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ff86882-5b5a-3b9a-bbed-7eb2a289b1bd | -4.51277 | -50.19822 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a25fcf00-9cfe-3bf2-847c-f56a7750e913 | -7.49874 | -47.35811 | 2024-11-16 04:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2fb43b1-3ca3-3868-9d0b-bacbd16f13b6 | -4.37077 | -48.08385 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87a646a2-8fff-3623-9297-0a572d2b2dc8 | -3.59955 | -50.35007 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 791f47fa-7e9c-3eb9-9f6f-b257f51da420 | -4.37725 | -45.63137 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4cd694a-8897-3437-a1b9-a9281086866d | -4.29524 | -48.09856 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0786b0d-d7e0-33f9-9c12-aa183aa2c688 | -4.37389 | -48.08894 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6cb5791f-1130-3f28-9dd1-d450f25407ed | -8.28161 | -45.9693 | 2024-11-16 04:50:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 455422b6-9b7c-3a0a-b071-78b6068806f9 | -4.50935 | -50.1977 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14b3c68a-6eac-343e-8bfc-bd94452650c5 | -3.74128 | -50.18139 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28d09933-069c-38ba-83e5-755a221865fc | -7.20499 | -47.69916 | 2024-11-16 04:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af22178a-0d65-350e-90ea-c8a8a6e1d3b2 | -5.97195 | -42.16365 | 2024-11-16 04:50:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4085bcc2-0824-3919-aa76-8fdb2ed82a4a | -4.10503 | -46.87776 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64ed7016-788c-36c5-b788-56da6bf7f1f2 | -4.377 | -48.57088 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5676b724-1631-30bb-bea4-d46cf6f1f403 | -6.16993 | -41.16553 | 2024-11-16 04:50:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 22cfb05b-ade0-3756-b029-7af7473608b4 | -3.69536 | -50.11414 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c70eaaa-7d66-3220-b886-3b8aef2d9127 | -4.36457 | -45.62476 | 2024-11-16 04:50:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02d16d91-c1f6-3937-85ee-8987c7bf7514 | -4.37936 | -50.71549 | 2024-11-16 04:50:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae7e5127-b072-38e2-8792-58937473a361 | -3.56298 | -50.24427 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18bbb9f9-d585-34f8-8681-772895400e46 | -6.16309 | -41.16948 | 2024-11-16 04:50:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc2dcc0a-4d6f-3947-9139-8826095e9f01 | -3.56105 | -51.55752 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d11caf80-787c-3194-bd87-fb6ae9ce9d65 | -3.46228 | -51.62291 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 761b79ce-2790-30b5-bf76-4493f31fc11b | -3.55299 | -49.92577 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60b5f31d-a909-38d6-8d86-39342bdc8b97 | -3.56016 | -50.24007 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7ff142-59bb-32fe-ba3c-d6c5c8148b54 | -4.37263 | -48.57476 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff850219-bc0b-3881-bc07-303cc66b0976 | -3.46282 | -51.61947 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 643a1244-87a5-3c9b-b3e3-e3eb7160b943 | -3.56241 | -50.2479 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58dc2e1e-060a-3ec3-a745-f303cc39d708 | -4.21838 | -46.81663 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 186d8acb-f48b-3716-9591-36549dff2931 | -10.83551 | -44.46284 | 2024-11-16 04:50:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a220083-0f7d-3f9f-886f-b5e9ea9a87c9 | -3.78055 | -50.10822 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 176d16ee-a958-3019-9a4c-79a65d5b6f29 | -4.2225 | -46.81709 | 2024-11-16 04:50:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1190ed99-8fe7-3725-8c15-dc9f3053bba4 | -10.54044 | -44.67735 | 2024-11-16 04:50:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7f1f170-3ccb-3ae2-810a-99e5efc8d62f | -4.29454 | -48.10316 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfa42972-0dbb-33c0-bb1c-e3ee74f77f65 | -4.99355 | -44.32396 | 2024-11-16 04:50:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ee503105-eff5-3dcf-9bef-918eaaac3b15 | -3.58516 | -50.53211 | 2024-11-16 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eafdaf84-d81a-3ab0-8f76-bd8611ec1de8 | -7.2494 | -46.78341 | 2024-11-16 04:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2848d98f-21cb-317a-9836-edc2555a7574 | -4.30552 | -45.9883 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e91f5ad-d439-3cb1-9260-a28e660e1780 | -4.95396 | -44.72521 | 2024-11-16 04:50:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4aac70c3-b23b-32aa-84cd-2716fb998efd | -5.79072 | -48.15703 | 2024-11-16 04:50:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f9b101e-569c-3ad0-acf4-e78e3e0d7035 | -4.37009 | -48.08841 | 2024-11-16 04:50:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ce5396e-d254-331a-8062-72d339c6e845 | -3.22829 | -53.62346 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 746f0345-9a38-3c35-b6f8-51f7eaf48981 | -3.56076 | -51.64565 | 2024-11-16 04:50:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e83e01e-5185-3207-ad15-eb4b01cd53ae | -3.2576 | -53.68052 | 2024-11-16 04:50:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76c0785-d05c-3f93-97c2-41da2b4676aa | -5.75113 | -49.46042 | 2024-11-16 04:50:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 453a5670-0f8a-3b39-b253-561764a872fd | -4.35517 | -45.86648 | 2024-11-16 04:50:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe4a4e8-c5b7-39ac-a2fa-f184237e67ea | -7.25149 | -46.78721 | 2024-11-16 04:50:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README49.md)
