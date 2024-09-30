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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a5ad5ee-699c-334a-9d45-392c9593fc24 | -12.24765 | -50.66529 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dd0b1fa5-dda6-30f4-9812-0988945994f3 | -12.23095 | -50.63972 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91c4c9a9-0ac1-3e56-93f3-92f73e1aac8a | -12.22616 | -50.66925 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96fbb07e-d80c-3989-bfcb-01c62e549963 | -12.22556 | -50.67294 | 2024-09-30 04:32:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e673a6cd-75b5-3aee-824a-635ce78fe0f9 | -14.26057 | -50.97374 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b1dd31e-23c1-36c6-bc12-7e0aa96507f4 | -14.2572 | -50.97317 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86a1b500-bd12-3724-9a43-8fa2ef56d6da | -13.93941 | -50.8786 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2085b124-d84c-3248-9a57-81dff9e53130 | -13.70959 | -50.9542 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44f7bb5b-0636-3335-b539-fa61f56039c5 | -13.70307 | -50.93028 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4598cf7-3c55-3aa1-9475-7854aefe29b2 | -13.70247 | -50.93398 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08631860-dafc-35c5-beb9-1520fcadcbfb | -13.7003 | -50.92601 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8095dcd7-2904-370a-be77-6955ac35525d | -13.69728 | -50.9445 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 966f7f19-5101-3744-b5d8-8ac28527b3b9 | -13.69692 | -50.92543 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2adefda-aa4f-3de4-8a3a-cb836b5ca8f9 | -13.69668 | -50.9482 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58917128-691e-3a08-bd85-c6588412a595 | -13.69355 | -50.92485 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bf91f5c-b199-387f-ab32-78c2c7d89d03 | -13.69017 | -50.92427 | 2024-09-30 04:32:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99c93e00-e8cb-3f18-b3a9-7e46d57d2e40 | -7.86762 | -50.22607 | 2024-09-30 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af758d37-037d-3734-a43f-6ee3b2d36921 | -7.20873 | -51.20218 | 2024-09-30 04:32:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8e79d286-ce27-3051-8041-05a18696f5a5 | -7.2051 | -51.2016 | 2024-09-30 04:32:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d4c11b5-104c-3261-9660-171446ab0186 | -9.31289 | -50.92999 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0202b026-1c8c-3805-b032-28bf0006e32a | -9.30597 | -50.78875 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f39bb56f-18a4-3808-8026-3cc7e1a75245 | -9.30312 | -50.78423 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4a667db-a393-38d2-bd99-2a60ce11e855 | -9.30249 | -50.78815 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3ce0884-d744-3712-b173-0a0efa981a78 | -8.73523 | -51.02403 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54660a41-7ef4-39a6-9035-99f2d883527a | -8.7317 | -51.02341 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91aa83ba-c9ce-3996-8b61-84a9f5354d9e | -8.72819 | -51.02397 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce298c57-f9ed-33b1-aa8c-1ff9dfa19726 | -8.72817 | -51.02283 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49d5323b-2856-3cc0-8736-a0e35ae4660b | -8.72753 | -51.02806 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e80a1402-db64-3c6d-ba76-80979de0d967 | -8.72749 | -51.02691 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a54b43c-78fb-39a6-a6a3-c7195651ddff | -8.72465 | -51.02345 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f8215f4-468e-3cd0-bad3-9a1c45b9df0d | -8.72462 | -51.02231 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0fe0ddb1-4bbe-3461-937c-f106dc1cd11d | -8.69988 | -51.0196 | 2024-09-30 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1bc54da-9c8e-3332-84ae-186670afab8b | -8.0792 | -51.10993 | 2024-09-30 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8d78744-4f1f-3013-bf40-8fce2c858fc8 | -9.90745 | -51.12883 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e8c5948-64c5-3b4a-84f1-1603df4f3134 | -9.90653 | -51.13007 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44a6a947-86c1-3cd5-ab8c-1a1b9841c247 | -9.90589 | -51.13404 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65cbb759-53f6-3bab-94e4-8cd9df9198ae | -9.90395 | -51.12823 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e236d03-6b6b-37ad-b9ad-d9e840ab6be7 | -9.90329 | -51.13219 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db74ea3a-d0d2-3e49-84e6-6eb7c843f794 | -9.90302 | -51.12946 | 2024-09-30 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6221477-8b08-3037-98c6-9f5851c3ca39 | -9.75057 | -50.66241 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1de5c5ab-acd6-3b0a-881b-42dc440b06ee | -9.74996 | -50.66623 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5291c5f-ff7a-30af-ac7a-0a5e3e40e0c0 | -9.74651 | -50.66567 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 004ad8a0-5eeb-3332-80c3-9e1bee3c51fa | -9.74306 | -50.66509 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 319a1419-f2f2-3271-91f4-9fda8973cff9 | -9.73961 | -50.6645 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ea1fb69-9dd2-396f-a172-e8d4db3c4b0e | -9.73899 | -50.66833 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5533441-3800-3d52-9508-ed0a7174594f | -9.73492 | -50.67158 | 2024-09-30 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26a6686d-b8b5-30fb-afd5-8325bef541f7 | -9.61323 | -51.41704 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33c38d02-597f-3581-9209-78b53e00c1d7 | -10.5507 | -51.09169 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1fc4142-b8ef-31b4-a41f-9d97411d2ad8 | -10.54722 | -51.09109 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43b91f5c-76ad-3223-85ff-b3aff773611b | -10.54659 | -51.09498 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01a0ea7d-7c52-34a8-b26d-5b8997e46d78 | -10.54572 | -50.94748 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08ddfc29-84a7-39c8-bf24-3099821c2d58 | -10.54375 | -51.09048 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 255f1c7a-7693-3a9f-a5dd-4f1842a343bd | -10.54312 | -51.09434 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2173f5e-1a45-3a93-8c78-27598b29bf57 | -10.54227 | -50.94688 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 385a1c7e-787c-395b-b609-1a59891345f1 | -10.54027 | -51.08987 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283c21f9-c785-3cf6-994a-89b89e7b40af | -10.53977 | -50.91877 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5787b7df-71a0-3292-997c-0265d4ef0999 | -10.5368 | -51.08925 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13dc2a7b-c719-3026-9162-bdd7a6cde4c7 | -10.53631 | -50.91818 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01117740-0e55-33ff-b20f-e7d7aa5fece2 | -10.53332 | -51.08862 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3436397-c57a-3f56-b6ed-b3f942ea8c22 | -10.5327 | -51.09241 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb0befce-2ed3-34c5-875b-76088671cd5c | -10.52985 | -51.08798 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55321b87-74ec-32e0-a115-8b8187ac4942 | -10.52923 | -51.09176 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 406b4e68-39a2-389b-b55f-9d66de0001ca | -10.52513 | -51.09491 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf0f9ea7-46b6-3db5-82c4-bbf9ab30efbf | -10.52166 | -51.09428 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f8b80621-7821-3f8d-b5b3-f62ce7050d8e | -10.52103 | -51.09812 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 526737ef-d0ff-35f8-9e20-0aa519d9f379 | -10.51844 | -51.11389 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7afbb7e4-2542-35d4-9ad3-a1732ece5607 | -10.51689 | -51.10152 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b8e6987-e595-3eb0-a600-4725de46dbcc | -10.51625 | -51.10543 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3415f57-f29f-3994-839a-985da4170b69 | -10.51495 | -51.11333 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5437327a-97dc-37bf-b447-1e62c09a094b | -10.50954 | -51.1245 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58355c08-4e4b-3a0f-89fd-3459d75a1ab5 | -10.50887 | -51.12854 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 609e8997-be26-3afa-bf7b-6798911ff451 | -10.50408 | -51.13588 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae07feab-1ad4-3bf1-a8c3-83ca99d55122 | -10.47947 | -51.21972 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9460fcf8-f9f0-39ad-add7-04eb4aab81eb | -10.47662 | -51.21518 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b159c43-dcac-361c-a18e-d063cfd157fc | -10.47376 | -51.21074 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2a1848a-7bf2-33dd-9c4a-2ba0a4f355c8 | -10.47311 | -51.21467 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cab7ac7e-b8e9-3aed-8953-f0b85fe43f20 | -10.47091 | -51.20628 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fab58122-347b-34e7-834c-6bfda1af8541 | -10.47024 | -51.21027 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5bd82d4-9170-3ed8-b3a0-183264cc1d10 | -10.46737 | -51.20591 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d075896-4e00-3201-a787-109c49a3d0ce | -10.46449 | -51.20159 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 189fcae8-cf2c-3f07-a871-8dca51608b9c | -10.46292 | -51.18941 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdc85415-e484-3ceb-85ec-f4f5e8dd8835 | -10.46228 | -51.19326 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbc18a64-9e79-3a3d-b808-2f72253aa973 | -10.46163 | -51.19717 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9bebd8e-6340-314a-82eb-db6ef692bf86 | -10.45882 | -50.74942 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c85a3a37-7601-3c7e-bf83-631f1d5a908e | -10.45854 | -50.77277 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 958de101-ad88-34c3-a8a5-869cadc05d90 | -10.4582 | -50.7532 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c6f63907-cf32-3d21-a26a-bb4bf493a56d | -10.45759 | -50.75697 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5ca646c5-464e-39a6-acb5-d6c0a1e7327b | -10.45697 | -50.76073 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fddf19fa-0c71-3193-b93a-bd4fab6daaf0 | -10.45635 | -50.76452 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caf2a089-3a47-3ef0-8b70-a9985ff6a3ed | -10.45573 | -50.76836 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbf7a168-b789-37b6-9011-fac31a1299c5 | -10.4551 | -50.77219 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0f1cd3f-fa2c-3c29-84ef-e7f7fa847885 | -10.45477 | -50.75259 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 997b4d57-8cab-3d3d-a4c4-c40dbbe88a64 | -10.45415 | -50.75637 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90bc3813-3db6-358d-a405-9cf00c3f0f4e | -10.45166 | -50.77162 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4197d586-ffcd-3c6e-b61a-07ba6b32a8c8 | -10.44321 | -50.8016 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d040cfa5-63c2-3626-9431-2bc420f4865c | -10.44259 | -50.8054 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de89fcfd-0d99-3e3c-b326-4c7b5b5aaa85 | -10.44039 | -50.79722 | 2024-09-30 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04fda981-95f5-3a25-b5dc-f7c61fc0897a | -10.83621 | -51.16627 | 2024-09-30 04:32:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce20e778-4df1-3495-822e-913d60c8f616 | -11.97492 | -51.88623 | 2024-09-30 04:32:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a60ceb6-3fee-3211-9e6a-93a7ecd42f4d | -11.97138 | -51.8856 | 2024-09-30 04:32:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README45.md)
