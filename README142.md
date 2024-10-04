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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83d0f7c4-986b-3694-be86-d8ba18955f88 | -5.43514 | -48.89787 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9177fac-097c-35a0-a3b0-659d63b37c7a | -5.43462 | -48.90138 | 2024-10-04 04:55:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b7ee45e-6117-38a6-9a22-54815f747cf2 | -5.30153 | -48.11232 | 2024-10-04 04:55:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a104ca11-c58c-36f7-a1fc-dc2d9f433f27 | -7.37846 | -49.61969 | 2024-10-04 04:55:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1850d213-2e02-34e6-97c1-dc20cb746fc4 | -8.34106 | -49.51963 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2af9c11f-be12-3869-9bed-b317673455db | -8.3214 | -49.57105 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1efb4d75-a73e-3c8d-ab5e-3f47ba5f3c7a | -8.31738 | -49.5705 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7d2dabf8-aabb-3556-b929-a7b1cd4a7317 | -8.31688 | -49.57398 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49537a00-e695-3251-aca0-1a1935a349aa | -8.31336 | -49.56994 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04d2d319-5904-3624-92d2-84626b7dbee3 | -8.30935 | -49.56934 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f404b55c-1189-3988-a3b2-2d8c06f12d34 | -9.02156 | -49.81857 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d062a072-1037-314f-90d7-57341f928dd6 | -9.01805 | -49.81453 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ee43899-c917-3149-96bd-c4097cf17786 | -9.01756 | -49.81801 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2671eb80-c612-3c6b-8974-11c1165b5d85 | -9.01562 | -49.8177 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09cafeb1-7f43-316e-970d-ccf488d4109f | -9.01511 | -49.82117 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de363fa9-45af-3061-b775-76ceedaa1d07 | -9.01308 | -49.82093 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c22304f2-c5bc-35e1-894d-bb9cac28619a | -9.01265 | -49.81021 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 290a2fee-412e-3925-a0fc-d839e79f7de5 | -9.01163 | -49.81715 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00153943-b18e-36ca-bb0b-265fe270f7b0 | -9.01112 | -49.82061 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9484a774-8b74-3a15-944f-78b4446c9d4e | -9.00815 | -49.8131 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c282c86-df54-3de9-862f-efbe6c9be70b | -9.00314 | -49.81946 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe0140db-b4e0-32a0-83fa-cf3f59e21c57 | -8.91413 | -49.68842 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 07656440-d625-36eb-8062-2e2284caee77 | -8.89059 | -49.65259 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 630716aa-cfa8-3e5d-a141-849e5ad352d2 | -8.88348 | -49.7019 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c4d61923-7b15-3c77-8af8-30014970af52 | -8.8014 | -49.66505 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cdb8d09-202a-34b7-8357-ddee1d24efdc | -8.77979 | -49.94489 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d061c1d4-7023-35c1-a04a-e56431395737 | -8.76832 | -49.60971 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9bb3e57-2170-3025-ae4a-cd89fa49c7da | -8.76781 | -49.61325 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02b932a3-67a3-38fc-adb6-a587322111e8 | -8.76429 | -49.60912 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7d8f6ba-eddd-314b-9b7d-e1073d550b9d | -8.65882 | -50.03614 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12c4c2f5-da12-3100-831f-199b8a19f344 | -8.65871 | -50.03853 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bbd0ed45-e964-37ec-9f68-2874df204d34 | -8.65731 | -50.04846 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ea5a4bb-e441-342b-a8b8-2d49abbc1d0e | -8.65662 | -50.05102 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b077db8-b122-34a0-8bce-6e091d58d00b | -8.65417 | -50.04053 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7039fdde-ecb0-3cb0-86bd-4ead7122e608 | -8.65344 | -50.04549 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6a7c635-cef9-30ad-9dfe-862912e8c246 | -8.65339 | -50.04789 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7c70627-21df-3874-9bb0-b270cb7bf43d | -8.65269 | -50.05288 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2939f354-9866-3a64-b88f-51ec4253b80e | -8.65197 | -50.05544 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7c73b48-a42d-334a-9c92-a0bf48c93c49 | -8.65026 | -50.03996 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8577b1bd-02f5-3025-9b2c-0de990505b2f | -8.64948 | -50.04731 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a2f3d8-e3c7-380a-91bb-7f274a634a03 | -8.64878 | -50.05231 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeb7f354-024e-391b-92d1-bda4718ec30c | -8.64808 | -50.0573 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d92d343-5f64-3c0d-9a9a-4cae8063ec0d | -8.64732 | -50.05984 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a20fcc9-cc02-3367-bbea-7207be62ab0b | -8.64635 | -50.03939 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9eb28ac5-2dd9-334a-b186-34d5c596d552 | -8.64561 | -50.04435 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfb78892-359c-3f80-9021-2c027ffc8837 | -8.64414 | -50.05433 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 404b99fd-8ad5-3e33-8487-c5144c034051 | -8.64243 | -50.03881 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ec91418-e643-3b25-8025-8488429443f5 | -8.64147 | -49.936 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 829876a5-c309-3519-8df2-8f769913f60b | -8.54648 | -49.6505 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 718556e8-614c-3ec2-a843-8430ca83a298 | -8.54496 | -49.6611 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4934dcb-5fa2-3bc1-ac8b-eaee50d860a2 | -8.54095 | -49.66056 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc705f58-d73d-3437-8441-95264ddad7ab | -8.3209 | -49.57455 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9243a84f-ebe6-340c-a9ac-ecda515180fe | -8.31639 | -49.57746 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abf7aacb-3a96-3e17-b1e7-629e6939ad80 | -9.02204 | -49.8151 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 439f4ed7-1a8a-309f-9f8f-f931ab33ff31 | -9.01707 | -49.8215 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 148e9101-962b-3372-b19c-df9a64323881 | -9.01613 | -49.81423 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a8077e7-6338-38ef-b641-6702bafd3215 | -9.01357 | -49.81746 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4ea858c-883a-32e8-8e49-7d88b12bb98e | -9.01214 | -49.81367 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a41701d-4958-3fc2-a98c-51a0e5f26928 | -9.00865 | -49.80964 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5cde0e6-0a26-33cb-9dc8-5847bc267f16 | -8.96225 | -49.82062 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e1b421d-1011-3b2b-a670-74da1f4162c3 | -8.91269 | -49.67023 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ff49398-f1d6-364d-9fee-368646194f7f | -8.90464 | -49.66906 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a82f9816-2fe7-314e-8ce6-5a8cc28688f4 | -8.90413 | -49.67258 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fac2c20-8845-3e1b-b8d1-e0d8fe66fefd | -8.89162 | -49.6455 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc26f4f4-fb6c-3e71-a14d-5c1bea0266ca | -8.8911 | -49.64905 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbd9e4e0-b4ec-3b07-85ce-a04d3bd392f1 | -8.88297 | -49.7054 | 2024-10-04 04:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9159e208-376c-37b7-a896-b3fbc22056b9 | -8.78086 | -49.94316 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 45357015-e6e1-3f77-9aac-fddcb0afa470 | -8.78051 | -49.9398 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 916436e7-c958-30de-9e0e-026ab8a58493 | -8.65809 | -50.0411 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| baa83aec-33e8-30af-b54a-2ff50cf19157 | -8.6548 | -50.03796 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb5c6d16-48f8-3f65-b090-1680a76ec7f3 | -8.6541 | -50.04292 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4762ad97-db2c-3db9-9c5a-1a7b747c7fe8 | -8.6527 | -50.05046 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cec7761-2c54-3608-9281-0f0c8b8197a9 | -8.65018 | -50.04234 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9688f16-5b5e-3840-ad5a-01e890c55c0a | -8.64953 | -50.04491 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e9f5087-193a-3a77-aceb-20d1b7674cc5 | -8.64805 | -50.05488 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87597196-b8cf-3afc-8c92-60f5ae6ce35f | -8.64488 | -50.04933 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe1a885d-02b9-3c51-8558-3597c800b261 | -8.64096 | -50.04877 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63b02c92-3738-3294-84ca-77dd0d5d76e6 | -8.64023 | -50.05377 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f58f870d-26cd-3429-b4ad-70880d1f5af0 | -8.63852 | -50.03824 | 2024-10-04 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b04da6d3-40f1-3718-bf11-d09b969e73c9 | -8.54947 | -49.65813 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ffdc0e2-148b-3cf5-b6f1-e65f152f34a8 | -8.54896 | -49.66165 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13767dc8-1e8b-3847-a15d-d8a5c425a91f | -8.54196 | -49.65346 | 2024-10-04 04:55:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57ad8ea6-0015-39fd-a951-79b4ea857c46 | -9.62953 | -50.10831 | 2024-10-04 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1ef8f8d-8e56-3617-b132-8acfa86326b9 | -9.62842 | -50.1092 | 2024-10-04 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e88e3b7b-be5b-3004-8af5-2c50fbae5c80 | -9.60188 | -50.10429 | 2024-10-04 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f62b656b-53a6-33c1-87b9-5318c29d190d | -9.59867 | -50.18153 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6988eda3-329d-392a-8cce-f82378194383 | -9.59301 | -50.16524 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 727e9cfe-a6e3-3727-89ec-19fa880e40fb | -9.59081 | -50.1804 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73cae554-2d03-3d8f-8ca3-2124df3a04a2 | -9.58908 | -50.16467 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4092995e-5ce6-3cdc-b699-0f9011afc428 | -9.58834 | -50.16973 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 65229724-9228-390a-8528-b5a370ada158 | -9.58687 | -50.17984 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aa84f94-df3f-30ef-8ea6-447e63ba4c20 | -9.5864 | -50.21062 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1aeb27b1-5a5f-3900-b310-c9a36946e2fb | -9.5771 | -50.21952 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9fa76f00-e7bb-37de-9a21-05d4986853ff | -9.56781 | -50.22842 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f6516be8-13cb-3601-9c99-cf0d174db03d | -9.56607 | -50.21278 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25a349bf-efb4-3566-9696-fc9bfed57cb3 | -9.56215 | -50.2122 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3df2112e-d66c-3a6e-a504-e87268d88048 | -9.56142 | -50.21722 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecf01b88-5522-3ffd-bbc2-f5c40f2c3096 | -9.5607 | -50.22223 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb289330-56c0-3145-bd6f-01e072b0d81b | -9.55895 | -50.20661 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8dc68376-95f8-3c49-add8-ee25ac35d364 | -9.55822 | -50.21163 | 2024-10-04 04:55:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README143.md)
