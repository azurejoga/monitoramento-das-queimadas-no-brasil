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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f72571ec-f50b-3326-a2e2-47b89441dc78 | -3.17577 | -49.45474 | 2026-10-10 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 63be80e5-0db2-38b7-9e49-270d8aa8f6a2 | -6.32418 | -55.33975 | 2026-10-10 12:00:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c53a1315-05ce-36a4-aff1-5c402723324d | -2.51131 | -48.35957 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1683b6f8-dbf2-35db-b854-f5d8dd91a0d1 | -3.0488 | -54.14472 | 2026-10-10 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8186beeb-1589-3d31-a4ca-02d51c0a89ac | -3.17975 | -50.59444 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9d8bbd68-ed44-30df-9a2a-be64a0601863 | -9.798 | -49.67212 | 2026-10-10 12:00:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8983ca42-4558-3ad3-83d4-373588135925 | -12.37995 | -46.56202 | 2026-10-10 12:00:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 75a8aca6-65b4-3931-b9b3-37af378a2c2e | -3.16342 | -50.58327 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7a4ba739-995f-3955-8a84-1ed7e1cafb9b | -6.43729 | -55.27256 | 2026-10-10 12:00:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| e5ed2c65-e9cc-325d-b772-11e6d68f4f15 | -3.25928 | -50.43278 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| d216d7f0-51fa-3b27-936b-259e6356f7ce | -3.26809 | -54.68966 | 2026-10-10 12:00:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 6934f177-1d6d-3095-8b89-1666ba8e98cc | -5.79232 | -53.80304 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2117b701-a58a-326a-afcf-1d73276f8628 | -9.94513 | -44.87996 | 2026-10-10 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a5197ce7-86bf-3c05-8e03-a5c63dc050c9 | -6.37127 | -55.16831 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7f0ffcfd-2f2a-3792-99df-865f50a09f51 | -2.51421 | -48.33939 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 228.1 |
| 2c342e92-6694-34a1-9209-1285dec5802f | -3.30575 | -54.0002 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fd681428-df36-3911-b5ff-4d489591e0b4 | -3.39142 | -50.21513 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1adbc8c9-2b41-360c-82d2-ec7a8a530f46 | -4.40369 | -49.77518 | 2026-10-10 12:00:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 473a5875-71a3-3e6e-9988-08a62473bc82 | -1.62699 | -54.4227 | 2026-10-10 12:00:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 61971957-21ab-3efe-8304-ed7e1c9cda37 | -3.22568 | -49.43008 | 2026-10-10 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| e27875b3-dabe-3dfd-a311-cdf7dc8788c9 | -6.1077 | -52.70469 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f7467207-308f-32d3-9a1d-f77d1f51c6b5 | -9.27326 | -47.40027 | 2026-10-10 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 74ce711b-71f7-3289-933f-3986a29f9cf1 | -11.66273 | -46.78801 | 2026-10-10 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| d13c8b4a-7d19-327a-9b2b-3c494dd5ae25 | -3.31566 | -54.00163 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| cd68d9d4-2f4f-3e43-9a04-2ade01e0f0b5 | -3.20474 | -53.85429 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 6bfa5311-4b43-3f5a-9114-cc12a85d51da | -9.11548 | -45.82796 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| bf7e6273-6270-3040-9d10-89047860546a | -8.9769 | -45.87521 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 8d0123cb-d2ff-3094-bb0a-c5b3c82f88ca | -8.98204 | -47.53965 | 2026-10-10 12:00:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5e0cc574-6e2d-39d9-b9a3-9e81126edc7a | -4.10291 | -54.02102 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ad87f2fb-8436-3ead-88b8-7050c9057828 | -1.88857 | -54.67755 | 2026-10-10 12:00:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e412c4ff-c5c8-3fc1-b082-0bb25844709b | -4.10192 | -54.01418 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 47cc58d1-0b4f-381c-b051-0b7a6cfc59b9 | -2.99329 | -54.17296 | 2026-10-10 12:00:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 99bea684-9887-3b88-9986-3a0ee9c0f337 | -8.45536 | -48.69381 | 2026-10-10 12:00:00 | TERRA_M-T | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6981af03-eaf0-30b2-ad4e-0e64482160b2 | -11.01828 | -45.40823 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 35cbd16d-b8ed-3080-92fd-902626e21d37 | -11.25861 | -46.24009 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 127b5c9f-43c6-3db0-958a-5c2b83749fa0 | -2.83851 | -49.87827 | 2026-10-10 12:00:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 60de668e-5701-34ee-b7ee-8a8d1f8d86bd | -8.52568 | -50.23275 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b8945b07-3aab-3495-9bb7-996d37b647e4 | -3.53793 | -54.73439 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 26e80778-b102-35d8-af1e-f44faa5ccb8a | -5.75323 | -51.44356 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5a1310c1-583a-378e-9bf2-a057210fef9e | -5.86965 | -53.51077 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| cfb4884a-0ae9-3850-9854-e0b087190bf1 | -9.11428 | -45.82145 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| ad4eefcf-4f6b-3990-8da0-a727cc0d81ef | -5.04439 | -49.35503 | 2026-10-10 12:00:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 60bc998f-00f5-3a62-8bdf-15c2fb02ecef | -12.06197 | -47.36545 | 2026-10-10 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| b2b6fc2b-947f-3a97-b87b-0dae74268b32 | -3.50497 | -49.93756 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e19421dd-9133-3336-b700-85dbe6512a71 | -3.47471 | -50.08803 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5216c418-0aac-3a63-bf09-d079de76faf9 | -7.1298 | -44.8871 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 39afa391-9ad9-3410-b466-4c0d2535fe94 | -11.00477 | -45.40734 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 230c6305-fdf4-3368-b20e-1f16870912d5 | -3.20234 | -53.85868 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| b2e370ff-55b5-3d9d-9ce8-a1b628f3c1e0 | -11.18302 | -45.32493 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 2e886066-ee1e-3196-bd7c-040cedb497d5 | -4.41267 | -49.77641 | 2026-10-10 12:00:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fe2b16e5-0214-35d3-b90c-3982c0126996 | -2.28741 | -48.7542 | 2026-10-10 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0eca6106-59ea-3661-bed6-feab1663eba7 | -11.7884 | -45.52616 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 924873ca-11c0-39f3-9f79-cefd766715ec | -3.80049 | -49.93285 | 2026-10-10 12:00:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 3d932302-bbd3-313c-a4f2-b117349be7b7 | -8.96201 | -45.89264 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 693ddbbc-2c3a-3379-ac54-11724f90f8ad | -10.92702 | -45.52285 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 347.6 |
| 16dc471f-4942-3eab-a7e8-b8a59fbff2ba | -11.38363 | -47.57468 | 2026-10-10 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 95564bca-7719-33a0-b77f-2df743aaf9c7 | -4.64363 | -50.95573 | 2026-10-10 12:00:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6fb06823-8769-3bae-a614-f26a0d3fb182 | -6.37312 | -55.15604 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 617728ba-09dc-33b0-bd42-16cf9a20fae5 | -9.93878 | -44.8726 | 2026-10-10 12:00:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3332063b-8391-3ef3-9e6c-812c063f4562 | -3.10002 | -50.31782 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c153d74-23eb-3d01-8f06-a3beccb35705 | -9.13987 | -50.05701 | 2026-10-10 12:00:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9e004bdb-8b45-3b56-9bd1-f299bb1b21d3 | -3.75187 | -42.50748 | 2026-10-10 12:00:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 15e60216-7788-322f-9a28-ef32d842d8cc | -10.93185 | -45.3687 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 6e34d718-4b69-30f3-a365-9ecb2c4c9d12 | -3.34503 | -50.41527 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f25f46c1-e145-36e8-90f3-c7e1dd1912d0 | -7.52207 | -45.30096 | 2026-10-10 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 74bfedc2-6658-31c1-a04f-0fa656d5d239 | -11.78322 | -45.45563 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 452a7450-b171-3780-9cae-7bbd79ef9090 | -3.53612 | -54.74704 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 77de2010-47a6-363c-9b36-f87bd78ab78c | -3.79363 | -50.75808 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 04d6b5e2-ec90-350b-af27-ea3deb14c4fe | -11.02921 | -45.43068 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 547.8 |
| 24f5621b-a39e-3e86-a233-d47ffd75ae1a | -2.519 | -48.34645 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 34e1531b-b33c-3a06-aacc-b375e2a5255b | -3.2386 | -50.18173 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a4b2f0d7-f7c7-3d07-b0d8-27f074821de3 | -11.78873 | -45.48599 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 0eb27404-c122-3f26-b805-aaf61703f9e4 | -12.21337 | -49.39447 | 2026-10-10 12:00:00 | TERRA_M-T | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b7428f11-f7c4-3903-8f62-87bb3b56d9e3 | -3.49015 | -50.48598 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6ba6809-a6b4-3e6b-bba6-61973ef7ab4e | -5.04576 | -49.34539 | 2026-10-10 12:00:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 14c358d3-5a7c-366e-b997-4bb89c1d900b | -3.23986 | -50.17288 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| da9c2555-5a52-39bb-821e-eacc12671cb7 | -1.91529 | -49.9422 | 2026-10-10 12:00:00 | TERRA_M-T | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cca0c132-778a-3e53-adc0-c41a66a3f801 | -3.57321 | -54.48777 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0ea7aec-244e-34cc-bca8-857399b873cf | -2.61554 | -51.7032 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f624ce4b-6398-3c78-944f-c2444fc01300 | -12.16857 | -44.78554 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 237.2 |
| f8e1bdd7-519d-3a45-9240-02e0c8330e63 | -3.35508 | -50.4077 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4c30a2bf-673a-3fba-be76-769bbb29de20 | -3.35383 | -50.41648 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3a17883d-f9b9-3e92-99e3-663582f0cbbf | -11.04265 | -45.43192 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 414.5 |
| bcca1c0f-4a42-3f75-8490-0c637a97c84d | -10.25023 | -53.92233 | 2026-10-10 12:00:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 61e2cd93-47e1-31ba-97ce-24be8d2cd077 | -3.3627 | -50.48032 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 5bad8904-4cb3-36a5-a3c4-9379d809c87a | -12.37764 | -46.58098 | 2026-10-10 12:00:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e4bdf988-1e78-3602-aa17-cf6ef8664288 | -4.41137 | -49.78555 | 2026-10-10 12:00:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b9a91020-abf1-3445-9797-cc9dc3888062 | -9.08814 | -44.25959 | 2026-10-10 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 207.0 |
| c887cdf3-9889-387e-a956-d3b4865fdaed | -9.27571 | -47.39222 | 2026-10-10 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f2bf8d01-3c9e-3ed1-ae15-cdaa86bf6f41 | -1.64109 | -54.39872 | 2026-10-10 12:00:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 62a249b1-b004-3d8c-b670-0043da0153e1 | -2.50335 | -48.34821 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 42a8b3b9-b0a8-326f-9cd6-aad6ee654c0e | -7.53242 | -45.32233 | 2026-10-10 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| cd1c1622-9745-38d6-b2bb-f2ad3373d479 | -4.12088 | -54.03507 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 81e99649-53d1-3b1d-bc31-b9818e5b949a | -11.3266 | -51.10794 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5a632c2b-e183-3cdb-a90e-15bfd7d68545 | -12.27638 | -50.97006 | 2026-10-10 12:00:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d962f4a-3779-3a51-863a-1d6d71f597a6 | -11.77529 | -45.48374 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 216.7 |
| b7831cbe-27e5-3f25-97d2-9f4d0f0a3b7f | -11.77769 | -45.50169 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 0eb6e453-3da6-3362-be3e-5300707af530 | -7.12965 | -44.90388 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| ba5cad28-e3b9-3e26-a7a8-8fb3f88b5e13 | -11.51641 | -47.61235 | 2026-10-10 12:00:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d421983c-4e43-3459-bc7b-079fd2b3eefc | -2.5176 | -48.35654 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |


[Clique aqui para ver as próximas entradas](README153.md)
