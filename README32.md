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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02da5c34-cc86-3158-b0d1-017a111fcf3e | -3.28275 | -50.62349 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a5a00f1-65ac-3794-97bb-9d29afc081c7 | -3.10592 | -50.36352 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ccae99bc-67a4-3572-8995-cd499e398d01 | -2.97636 | -53.29175 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 32d6d21e-a479-3079-9864-39fcf9c04550 | -4.23077 | -45.77455 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a4353d2-51a2-3b32-8339-46a367dc885e | -3.28194 | -43.61323 | 2024-11-29 04:04:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14cf9d64-2838-344e-8658-0a2542754412 | -5.47975 | -42.06887 | 2024-11-29 04:04:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 948ae2ca-5ef4-3c9b-ab49-f27d5de08612 | -4.67978 | -42.3806 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6349b5ee-b58c-31fe-a06f-1957ef1c5d12 | -0.27395 | -51.63451 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53647ce8-eddf-349c-a03b-25273f0ed431 | -3.26257 | -45.37588 | 2024-11-29 04:04:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fee55d92-0b53-36c8-aa7a-7c649b01cecd | -3.85596 | -50.15232 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec9fc0e9-7adf-36a5-be92-9927cdb7da5d | -3.64424 | -49.39769 | 2024-11-29 04:04:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f951b51b-03c9-3acd-954b-b32eae6e184e | -3.25095 | -53.63811 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d2d016e9-ecb7-3868-b936-2879233db13b | -2.60261 | -46.83449 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67f25bd1-f821-33d0-9beb-73bf38014d67 | -1.59221 | -52.28817 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 01384606-b68e-3a87-9877-226762630ea7 | -2.86685 | -46.84385 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5f23bb8-af58-3136-bd88-44ef2a66fb30 | -3.71085 | -47.14472 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52e8d1be-3479-32a7-8724-6b892f5fd53f | -5.86563 | -42.75825 | 2024-11-29 04:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 75067353-6a6a-3722-92d5-47700d01b5b3 | -3.95482 | -46.72822 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76c21dd-57d4-3627-91b7-286971188759 | -1.32595 | -51.92532 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d2ee062-f42f-32b5-a374-ee189edffd85 | -0.27596 | -51.63673 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d182a4b0-d9e4-3246-a376-771b59225d25 | -4.3381 | -50.7727 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f27e884d-8d44-312f-946e-b2c15311abee | -5.04068 | -43.61949 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2f6880cc-d21a-3695-bdb5-32865a922c9f | -2.3133 | -51.96238 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18a1ddde-90ab-3720-944c-d52dea669718 | -3.93425 | -46.72048 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44409deb-5915-36e4-967d-da7f5712927f | -2.55904 | -46.41164 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba845d9b-7992-3e0d-92d7-028aafa8dae2 | -3.18401 | -50.30257 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb02f0d9-55d2-33bc-927d-feb28aa06631 | -3.46557 | -50.54312 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 642961d9-9c28-3ca7-b486-35452dc9cc9d | -3.19174 | -46.5702 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a10e7ca-bf7f-3c66-bf20-4c382d78aa6c | -1.63233 | -46.33422 | 2024-11-29 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f54248b9-7009-33b3-8b94-51be580f590b | -3.97677 | -46.72744 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fcac986-50a7-3620-ae5f-445573b88470 | -3.03102 | -48.50233 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 413e7112-ecda-35c9-b9a8-f36399382c93 | -2.33035 | -46.87289 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 822112a9-868d-3eab-8302-c54a231e5e85 | -4.51468 | -42.0715 | 2024-11-29 04:04:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf7339c7-05ea-3e31-8dec-87e4d1e88a7b | -2.57743 | -50.00079 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8561b1f2-4a2f-3f5d-a172-67f85fcc0f36 | -1.33378 | -51.93373 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2c8ec02-ee90-3d7c-9b22-df5d4f374914 | -3.25095 | -50.41009 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db77fabf-2d4e-3a45-865b-476c6fbb1981 | -3.49339 | -53.80015 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3cec868f-69a6-31b8-8162-8bd3ba695288 | -3.47485 | -49.92657 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b6ed2fe-156a-3274-8ce9-db3588a9bedb | -2.72645 | -54.14085 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a8a714b-4026-3aa9-81f1-2fcf082668e7 | -3.49602 | -50.46551 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d201f940-ec63-3b01-beaf-f4ac73eaa997 | -1.61524 | -53.88145 | 2024-11-29 04:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ea407fb1-8206-3d11-ab56-1279f4f6c2d3 | -2.87993 | -46.84604 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86b4b1bc-98de-3dcc-978a-07990c691abb | -3.16931 | -48.43713 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81aff696-7a04-33f2-b3c3-5b6c98247347 | -2.95453 | -48.33886 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56c3bcea-7dc7-301d-bcf0-da37d9bc1d67 | -3.61228 | -44.80299 | 2024-11-29 04:04:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0780c0a-2b8c-351f-8195-e37b5de0e2f8 | -1.16245 | -53.67445 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b835e5c-0c81-332c-8af5-f1eea7d84e20 | -3.79054 | -50.13237 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8afa339e-5e75-315c-b9e5-bc4188bd20f9 | -2.95968 | -53.72211 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00330166-5625-31e2-8d9a-2358d5be0a4c | -0.99613 | -51.72326 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5053c96b-3bac-31f8-ad1a-e337c01b4fd5 | -2.36172 | -48.54626 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30434495-f85f-3373-9b53-73f94b6125ec | -4.3955 | -47.23272 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 524a7996-943d-38bc-8cee-a3bef6156298 | -1.68373 | -52.45889 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9303fd88-fd20-355b-9ec5-6cbd0e246b5e | -4.73095 | -40.24241 | 2024-11-29 04:04:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f44c8f87-9e8a-37a8-9bd0-f2af2e528c04 | -3.80532 | -44.04675 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22d51185-3b68-3d30-9ff9-3b1091df5714 | -5.11369 | -45.48685 | 2024-11-29 04:04:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a970fcee-1993-3c40-9c13-0cb3d49d45fa | -1.52769 | -51.61935 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d15b9391-87ad-3dde-85e6-7f65778c4a28 | -2.29602 | -51.98935 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6b5d965-d601-3346-bf70-2bf65b8b3592 | -4.51134 | -42.07097 | 2024-11-29 04:04:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69ef001b-0ace-3906-bba3-deb200091ffc | -2.83742 | -46.80468 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 88db5826-d56d-3c27-9c95-cc93e161297c | -3.72634 | -49.87532 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bc7ee73-08e2-319d-90f9-c6b277d9c3ee | -5.7195 | -43.83981 | 2024-11-29 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 382ba11e-8c46-3c8e-bff3-27c5db1fda04 | -1.18838 | -51.77541 | 2024-11-29 04:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f063614a-932d-39bf-ae17-9839d9ee826a | -1.31016 | -51.96062 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f21879ca-938f-3bbc-aea1-e6dc126b7ac9 | -4.39631 | -41.70102 | 2024-11-29 04:04:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0f8b6528-dec8-3a1d-903b-1ac331dce2a2 | -3.93689 | -46.70448 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d0cf334-c492-3f8d-9a4e-68da8a1de75f | -4.66634 | -42.37846 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 968bb549-e624-3b63-8db4-3eb873528b8f | -3.49911 | -53.80753 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af0edd8f-b816-378a-b735-8440c81b38d7 | -2.86648 | -46.87408 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59db8cb1-4e4a-3b12-a0b7-8d980e971bb4 | -5.27768 | -45.12659 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69480dc2-5bf4-313a-bab1-acaad8c0060a | -1.5867 | -52.28187 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7bfe7907-19da-3ddb-8fe9-c37038f19114 | -3.20059 | -46.59633 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2808b4b-569c-3cf8-9ae9-000d012ca6aa | -3.26477 | -49.89524 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b117c612-b67b-35aa-a343-5a7a7d00c4a2 | -3.32245 | -46.7026 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34810af5-c0f9-3a27-b99d-15c2a8f7e4ed | -3.64474 | -49.39465 | 2024-11-29 04:04:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a48b669-db7a-3598-947c-26564a3a9eb9 | -3.24443 | -53.64657 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a0b64b7-a072-3dff-a425-b01171c289fc | -3.94792 | -46.69041 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f1f6a43-a8a0-37a1-b0a0-a67afa413c47 | -3.4971 | -50.46136 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8d75004-56b9-3b88-93d0-336a1b517b11 | -6.18602 | -43.95921 | 2024-11-29 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fae4afb-40d0-3eeb-8d05-b553ddfdfa8f | -1.71319 | -52.76845 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 92be64df-05b8-3210-b04c-4b2b7166fcd3 | -1.93986 | -52.96054 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77f85390-197a-32e6-b528-3136c33ad1bf | -6.06379 | -44.15168 | 2024-11-29 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fc01f74-2d35-33a8-8697-10b0615ee175 | -3.61642 | -49.85674 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc9a0eed-425a-32b4-a773-efbd515e0a4e | -3.72299 | -50.19042 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b10ceba1-4f85-349a-a554-4f54871fcd4c | -1.91834 | -52.88631 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8b41d53-4ab0-32f0-95f5-487ce9b4805e | -2.65134 | -48.78503 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 638640ca-55b8-361e-91a6-827f09c619d5 | -3.46662 | -50.54292 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec360abb-c0cb-3222-bcdb-cdf4e06c4835 | -2.20233 | -52.1033 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84e5fdaf-04c6-33a5-990f-212a0931d351 | -5.18435 | -44.34585 | 2024-11-29 04:04:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00432fd9-0625-317a-a0d0-3021c282e9ca | -3.17503 | -46.30005 | 2024-11-29 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ed439b9-1d46-3dd5-8a03-6630b0bd8288 | -3.41569 | -50.16615 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90f0ffad-677b-3d94-a288-3072af9538ea | -5.27555 | -45.45107 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4886c80a-d60e-3c13-b5c2-500a2ed87b6e | -4.16878 | -48.62141 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82fcd587-bd95-380f-8bbf-8b012892024c | -3.28465 | -50.61223 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95a22334-00e6-3fa1-bd69-e4f32cdf1035 | -5.86678 | -42.75107 | 2024-11-29 04:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2ad2570b-5681-342e-8e34-cb791d855245 | 0.9898 | -50.27343 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29dcfa50-6c4f-3930-a320-0e9a09e2f0bc | -2.85388 | -45.54734 | 2024-11-29 04:04:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a286d090-4339-37fb-bc9d-eb2af0c7d85e | -4.78438 | -44.40799 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f19603cc-f023-3b53-9e25-13043c55264c | -5.62952 | -44.53285 | 2024-11-29 04:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44f6f65c-dbbd-35cc-ade4-e6beed78b315 | -4.45053 | -43.99875 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85dac5e5-091e-3b44-86d7-3e5c9f25ffef | -3.22181 | -54.17995 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README33.md)
