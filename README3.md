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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52013864-4c91-3926-b0b4-792ed15cee82 | 1.80585 | -56.0079 | 2024-12-09 00:58:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fc4b6e1e-a60a-365c-b8e4-3abbb1b1c9b3 | -12.5495 | -57.7395 | 2024-12-09 01:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 12869270-736d-3a1c-8b9e-11f1887e02ac | -4.5429 | -48.0151 | 2024-12-09 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 1d659719-35f3-32e4-8c9c-c0df3666abc9 | -6.9825 | -34.9441 | 2024-12-09 01:00:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| 7093800b-95f0-3f98-a719-1654504fdfe3 | -11.752 | -54.7255 | 2024-12-09 01:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| d3c63d8e-b679-3d64-b06f-67024c2f6494 | -6.9828 | -34.9165 | 2024-12-09 01:00:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| a52e3331-56b0-3a82-a281-3b3148f8d038 | -6.97 | -34.94 | 2024-12-09 01:00:00 | MSG-03 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64bb3978-c119-3168-9117-20bbeea804c1 | -12.7951 | -54.216301 | 2024-12-09 01:09:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e957d580-aaba-3613-8d32-0cbb15744c29 | -4.5612 | -48.015598 | 2024-12-09 01:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa48bc7-bcc2-3ec3-ab0a-33afe0d9251c | -11.7525 | -54.710201 | 2024-12-09 01:09:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5ff338d-cbd0-3d53-b235-d77f6bbd9ac3 | -12.548 | -57.7379 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ead1a0b7-8aa0-3ae7-b5aa-54f7cfd2cde1 | -12.5238 | -57.768501 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e10d8aa1-6ea7-3407-b4ba-e50712fe6915 | -4.0843 | -54.397301 | 2024-12-09 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aedbf5f-2cfc-335a-94d0-3883277b7814 | -12.914 | -55.058102 | 2024-12-09 01:09:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00312fa4-34ff-3ce3-abd2-b6dd76d89fd8 | -13.2649 | -56.828701 | 2024-12-09 01:09:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d464c6b-c70d-30ea-90cf-723892ad3ab4 | -11.8269 | -57.820702 | 2024-12-09 01:09:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5090d791-8ea9-3f21-abfb-84cf6b29b897 | -3.4671 | -53.961899 | 2024-12-09 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8137182e-c920-3946-8e29-c4cee39087d4 | -11.7655 | -54.721901 | 2024-12-09 01:09:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7404f8f7-b35d-3335-a5a3-9d9f813325c7 | -3.4769 | -53.959599 | 2024-12-09 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d729a6d3-fb1b-3ffe-85d2-e50735bcb86f | -11.7557 | -54.724098 | 2024-12-09 01:09:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9474066b-ae81-310e-af0f-ab5e62f5fa88 | -11.8252 | -57.812698 | 2024-12-09 01:09:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba3e369-7f76-3bf9-b183-eff4a53a6f60 | -13.2653 | -51.070599 | 2024-12-09 01:09:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08e5a072-6963-30e7-bd45-02f2ab095171 | -10.8439 | -56.623199 | 2024-12-09 01:09:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89dfa533-ff38-3fdc-bdbf-a35c0ae2f5f3 | -12.5365 | -57.731998 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e6e3b06-0ebc-3249-84f4-4b0ff0d8f698 | -11.7639 | -54.714901 | 2024-12-09 01:09:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4b55fd6-d513-313e-9ffe-7ec3095f011a | -12.5399 | -57.748001 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48e47fe2-c9e5-3fa9-815d-73f106c43425 | -13.2674 | -51.079498 | 2024-12-09 01:09:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b26e4ee-1073-3674-9cd4-856b263b4274 | -11.7541 | -54.717098 | 2024-12-09 01:09:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4654daa-7d38-3471-b67f-4cbe4737693d | -13.2696 | -51.088402 | 2024-12-09 01:09:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 434961e3-824d-3210-92fb-50e13760a7bd | -12.5347 | -57.7239 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37df7b72-5075-32ae-9843-84f43202a697 | -12.5221 | -57.760399 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66310a30-bb59-3cab-a800-fe3188013d91 | -12.9109 | -55.044201 | 2024-12-09 01:09:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52d783b4-5c5d-3cba-9acb-b2563109d5fb | -10.8341 | -56.625401 | 2024-12-09 01:09:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e868aeda-9c59-3242-8ac9-05843079a85a | -12.5336 | -57.7663 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61e4c240-8bf7-3681-9095-76b40f965b7d | -4.5566 | -47.996799 | 2024-12-09 01:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 114a73fe-4996-3f35-9899-321d4b694c0f | -12.5353 | -57.774399 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 996831b4-ad2d-3b94-9e81-088fe930db75 | -12.5382 | -57.740002 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a79dfbe-e47e-35f7-becc-d49c188834be | -12.5463 | -57.7299 | 2024-12-09 01:09:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4568bf00-1984-3229-abf8-7c1313e0e390 | -11.8896 | -54.678398 | 2024-12-09 01:09:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c76fd20e-7ef4-3ec2-8b7a-a9bf140ce47d | -11.888 | -54.671398 | 2024-12-09 01:09:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f2f1f1e-1971-39e6-8224-05a9ded0619f | -4.5515 | -48.018002 | 2024-12-09 01:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e6c94ab-c6cc-3499-92c4-19be99184bbf | -4.5469 | -47.9991 | 2024-12-09 01:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85e4e8e3-968b-3b72-97d6-2888224ea207 | -12.9124 | -55.051102 | 2024-12-09 01:09:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e432f212-3483-3f93-85ab-74e16da613ce | -6.9825 | -34.9441 | 2024-12-09 01:10:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 892750a2-7052-34a4-be62-691abe14e62d | -4.5429 | -48.0151 | 2024-12-09 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 983765ca-918f-35bc-8dcd-5500b5c1f66d | -4.5614 | -48.0141 | 2024-12-09 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8fd589a0-a9da-3a29-825b-6acd583cea81 | -11.752 | -54.7255 | 2024-12-09 01:10:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 4638eee8-c92f-360e-898c-b5830c4542df | -12.5495 | -57.7395 | 2024-12-09 01:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8d390231-5eb5-3004-8233-bcb7447b02c5 | -6.9828 | -34.9165 | 2024-12-09 01:10:00 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| 266c77a7-468d-34c1-9ecc-8b8ee1d9901c | -3.089 | -54.065201 | 2024-12-09 01:11:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07dccb8c-5d3c-3b47-b929-4f0a4b935380 | -1.077 | -62.6408 | 2024-12-09 01:11:00 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b61c96a5-0bc8-3c4b-b7d5-f789b4d1ab66 | -3.0871 | -54.056999 | 2024-12-09 01:11:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d582a3c-b0cf-3c9e-8961-21eeadd4d71e | -3.1086 | -54.060799 | 2024-12-09 01:11:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acf273a1-6622-3966-a974-026c4c4773fc | -1.0746 | -62.630299 | 2024-12-09 01:11:00 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24da1452-903c-3287-b0ed-81810412a5ed | -3.1104 | -54.068901 | 2024-12-09 01:11:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0469ee6b-0c3c-3f11-8cdf-9e7ad1bf5c31 | -12.8576 | -58.224899 | 2024-12-09 01:11:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 759fbfd6-57b4-36c1-a6f7-022a5cf14a32 | -3.0988 | -54.063 | 2024-12-09 01:11:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe3de703-c6a4-3b79-9c38-92708dced0e0 | -3.0792 | -54.067402 | 2024-12-09 01:11:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d961032-4d97-3756-b6c8-2f71a5f78f05 | -2.8858 | -54.256001 | 2024-12-09 01:11:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a08fa1e9-137e-3fec-8fef-4fee45303e8e | -3.0852 | -54.048801 | 2024-12-09 01:11:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d30eca9-6c25-3e9f-af13-1ded7a5f0a00 | -13.2709 | -51.0929 | 2024-12-09 01:20:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 1aa4c6af-4f94-34ce-bee5-90834e194083 | -4.07 | -46.3724 | 2024-12-09 01:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4f2a1d92-7754-3bdd-a291-11320125ac08 | -4.5429 | -48.0151 | 2024-12-09 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 68caf018-08f3-3b0d-b194-d79c4eb4126e | -11.752 | -54.7255 | 2024-12-09 01:20:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 625d07ac-807c-31aa-9d03-584f87e55f4a | -12.5495 | -57.7395 | 2024-12-09 01:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 748daed2-be23-35cc-8cce-cb32ac911610 | -12.5305 | -57.7411 | 2024-12-09 01:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 869dc7c2-3950-3272-9956-b0c23ab52aa4 | -4.5429 | -48.0151 | 2024-12-09 01:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b81ddacc-1285-3c1a-9851-a87c2cc4df7a | -11.752 | -54.7255 | 2024-12-09 01:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0daffc4d-3ba4-3e49-96c1-6856f4c689a7 | -12.5495 | -57.7395 | 2024-12-09 01:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 247508f6-cfd7-32be-9b79-f04d1098e754 | -11.771 | -54.7237 | 2024-12-09 01:30:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 3cd81c8d-6cec-3749-b05d-7e28aa6654da | -13.2709 | -51.0929 | 2024-12-09 01:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 01e886c1-091a-317e-a7b7-573922fa1323 | -11.752 | -54.7255 | 2024-12-09 01:40:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a0e31d18-a1c9-3a43-a3c1-daa8c1474437 | -12.5305 | -57.7411 | 2024-12-09 01:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7836a312-67f0-3d69-aa72-e244f369df0b | -12.5305 | -57.7411 | 2024-12-09 02:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4c030eff-baef-3000-8c57-6f301a0766cb | -3.2351 | -42.4353 | 2024-12-09 02:10:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 82bfebb5-d243-367c-81f4-01d0c863535a | -12.5305 | -57.7411 | 2024-12-09 02:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 15d2c9a8-ef0a-382e-87a6-8a819d8ea636 | -13.2709 | -51.0929 | 2024-12-09 02:10:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 4b8b48e3-9690-3a67-a509-fec606969e72 | -4.0885 | -46.3715 | 2024-12-09 02:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 58bc1d2e-35e6-3771-9f0e-a4404b2be1aa | -13.2709 | -51.0929 | 2024-12-09 02:20:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| bc3f8494-1481-38eb-a064-0b28b02a2285 | -3.2351 | -42.4353 | 2024-12-09 02:20:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| c456a339-a6ea-3494-9a58-96529f893bfb | -4.0885 | -46.3715 | 2024-12-09 02:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fba910d6-669c-34ad-9452-99959e30d28f | -13.2709 | -51.0929 | 2024-12-09 02:30:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| a4a04f53-134b-3b41-9401-436e39fc1415 | -2.1531 | -48.0375 | 2024-12-09 02:30:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| dafd117a-e3f4-3a06-9d55-6cdb19be592c | -12.5305 | -57.7411 | 2024-12-09 02:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 849408a1-eab9-378b-8881-1c6bdfc3f14f | -12.5495 | -57.7395 | 2024-12-09 02:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d95925c7-dbca-3d78-af06-7e814526583c | -12.5305 | -57.7411 | 2024-12-09 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c68e7d4c-a203-3d69-bf2c-fc22f820326f | -12.5495 | -57.7395 | 2024-12-09 03:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a16fb80d-300e-37b6-9089-7ad7bbf25936 | -3.0037 | -53.038 | 2024-12-09 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 680db6f2-fe7d-3ca1-b9aa-359f93712106 | -12.5495 | -57.7395 | 2024-12-09 03:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| bc8cf54e-65f5-3ed4-a19c-642a491980c1 | -2.1531 | -48.0375 | 2024-12-09 03:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6ae9b460-571b-3729-847c-15b76b2b5611 | -13.2709 | -51.0929 | 2024-12-09 03:10:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| bb7322aa-e7d3-3b6e-bab0-9737ce30ddde | -12.5495 | -57.7395 | 2024-12-09 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c6ba4016-05b7-3984-ba1d-8bf506851dd6 | -13.2709 | -51.0929 | 2024-12-09 03:20:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 69786706-0741-3090-89d9-be5ebf90f8be | -12.5305 | -57.7411 | 2024-12-09 03:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9676aed9-d938-3498-97e1-5b9ce0d811be | -5.0718 | -37.71548 | 2024-12-09 03:29:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c5a5677-c081-34ec-9ddc-70bb52e123e0 | -2.99812 | -40.28443 | 2024-12-09 03:29:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5036587c-6f24-3ebc-8cf4-ea0355d035d4 | -3.23403 | -42.42577 | 2024-12-09 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 002b5884-a360-3d95-b478-09145a71c6d7 | -2.99865 | -40.28128 | 2024-12-09 03:29:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 20969794-df2c-3b69-9820-ac5fe0230164 | -4.57812 | -38.55684 | 2024-12-09 03:29:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab2b71e2-53a8-3eb3-98d4-234ae2b06785 | -3.22727 | -42.42942 | 2024-12-09 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README4.md)
