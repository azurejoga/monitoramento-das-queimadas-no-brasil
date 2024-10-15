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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f61b67bf-ee7f-352c-bb57-cdfccbe18e6c | -12.41332 | -53.11501 | 2024-10-15 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 975fc87e-1e72-3df0-9f0d-24e340bf9c52 | -12.40635 | -53.11412 | 2024-10-15 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d19d3502-6248-3d9b-9fdb-1d9da4928c15 | -12.39939 | -53.11322 | 2024-10-15 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e22ef4aa-14e3-3a40-bacb-a4cc60e3975a | -12.38532 | -53.11792 | 2024-10-15 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09803119-e68d-314c-9a77-07f7b507adb6 | -12.38477 | -53.11811 | 2024-10-15 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 899949dc-c1f7-30f0-82de-daf9b568b402 | -12.37837 | -53.11706 | 2024-10-15 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d48946e8-6bda-35a7-9fa1-f5e9dcac72bb | -12.37781 | -53.11722 | 2024-10-15 05:44:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 696ab612-eb1f-3574-a999-5af474ad89cd | -9.00858 | -54.50544 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24052692-2223-3086-b10d-d600a429da1e | -9.00244 | -54.50448 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a06987da-30c8-31c3-a96d-2bf2e7d65976 | -8.98535 | -54.59001 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ee10459-7150-3af6-878d-17b8ecbd0661 | -8.97926 | -54.589 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 77148c0c-c058-37c9-b300-cbf1340dab65 | -8.53694 | -54.77089 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bafad30-5999-36d1-9b5c-321fbd9d0943 | -8.53637 | -54.7753 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d09c4d8-bf8b-30e8-be49-d4d201c873a1 | -10.81224 | -53.89625 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0772763-f04a-32e3-bcf5-01611049c403 | -10.81219 | -53.89472 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65f43c1f-e36d-3461-904c-9eb53ca59f2f | -10.8057 | -53.8955 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2726213a-0630-3139-bf2c-ff82157ddb35 | -10.80565 | -53.89394 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d393bd05-d53e-370c-bfe4-ec6a415d08bb | -10.80502 | -53.89948 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e0f3d83-08f7-3beb-8219-18009480ba6c | -10.03935 | -54.33876 | 2024-10-15 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6592dc3f-56bd-3d7a-a861-6df32c177536 | -10.03872 | -54.34409 | 2024-10-15 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3bb2be5a-f5bf-3609-884c-1e8a6c9e642a | -10.03592 | -54.33792 | 2024-10-15 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 7bbcfcec-9fbd-34c6-8598-b389d494a3c3 | -10.03525 | -54.34327 | 2024-10-15 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0ded88cd-0bb3-3994-a949-38894165c8a1 | -10.03304 | -54.33803 | 2024-10-15 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f5dc5f9b-5706-3918-a796-322c09ee8d2e | -10.03241 | -54.34335 | 2024-10-15 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1add63ce-0116-332f-ad43-78d2f745c38a | -10.02894 | -54.34254 | 2024-10-15 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| db0eebc5-e6f8-3c20-9899-fb37eea1d7bb | -10.947 | -54.09802 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d8efe10-0c31-34a9-b62d-c3572dc84d57 | -10.94054 | -54.09718 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 55fcb50a-0a58-3b75-b748-8203c769b6ac | -10.93992 | -54.10246 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| df24d48f-7481-3701-a1a4-35947d7cfe4d | -10.9393 | -54.10778 | 2024-10-15 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d97db1e3-c322-36e8-bb29-9d3144b42fdd | -7.87472 | -54.7183 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56f1b8ae-8166-3d63-83da-3be78ce148ba | -7.87051 | -54.70369 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0306d19f-3dd1-3b93-b9b1-8f7c32450f6c | -7.86931 | -54.71304 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cc75a17-8fe0-3e89-bb0e-7aee39683cb0 | -7.86876 | -54.71733 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68c46371-567e-3639-95aa-beefc51b62d6 | -7.86388 | -54.70795 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3cf5dfe9-9311-362c-99b8-f23da07acf26 | -7.85973 | -54.69277 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b850e56c-c88d-3b3b-acf7-56c40d040dcc | -7.85912 | -54.69747 | 2024-10-15 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 727a3756-13be-3c9c-b203-d27390cd7303 | -13.00191 | -60.26606 | 2024-10-15 05:44:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e99c48c5-71f4-323b-9cbc-bad4f0755eda | -9.28348 | -60.25822 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8df8416c-5401-38b9-91cf-89bce98a4838 | -9.27928 | -60.2576 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52f3f5e2-9525-3c50-9def-82791a9fb6bc | -9.15184 | -60.39732 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f02ddc8-8591-3d85-9a8a-3829e1ff25e6 | -9.1228 | -60.39296 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 288405e3-376b-32a7-9749-6f0cd23262ae | -9.12175 | -60.40058 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 112b46df-a7ee-3e64-92a8-02ca4cf64fc0 | -9.02407 | -60.41744 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8c55437c-db87-3a73-b486-987cc077c7cf | -9.01993 | -60.41685 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ab72934-ae30-311c-8301-0472a9f73f58 | -9.01941 | -60.42064 | 2024-10-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6da9cb4-f0ae-3bd1-a670-504c84ca9fa7 | -10.62892 | -61.42693 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25f64592-e187-3cb0-b241-757258423d12 | -10.62821 | -61.432 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca4dacfb-6f9d-3de4-987a-03c2585e2949 | -10.44749 | -61.26554 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a6f483b-1822-3676-b364-9c3ea703a71e | -10.4288 | -61.01473 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7919c38-2ce6-32f5-b4fd-a1f7d8033923 | -10.42829 | -61.01845 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0b2e271-5cd9-3f71-9a8b-cbdaab86637e | -10.42693 | -61.02537 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a733f355-02ff-334d-a44b-818e17edecb3 | -10.42341 | -61.02108 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec9dab9f-627e-378b-99e0-3b622b865f4b | -10.4229 | -61.02462 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11170537-ee3f-3edc-aa3f-fe23dcc72fcb | -10.38794 | -61.26799 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21103c6f-2ffe-3123-bd38-c4fadb3407c6 | -10.38399 | -61.26715 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b17b2ccd-7b70-35e5-8573-b7e5ee09da09 | -10.38005 | -61.26622 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf59a17d-e28d-32a2-9285-8eab9e8ca21d | -10.37771 | -61.19692 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f4503a0-f3d2-380f-b1b2-61fc5a223711 | -10.37472 | -61.18921 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 990d8733-abda-3224-91ca-ef371aced96b | -10.3737 | -61.19635 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1c84ba76-ba06-3d34-8f3b-046f0becd569 | -10.3702 | -61.1922 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ce4bc442-beae-34d2-bc7a-f0e2e48519e4 | -10.36619 | -61.19161 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ee3a3cb7-f961-3cbc-985f-6456e38fe739 | -10.36169 | -61.19455 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5078f841-b6d8-31f4-bc8a-ea6b7672c08d | -9.73691 | -60.75984 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f67ca95b-04e1-35d5-90a2-9c5379ea5a54 | -9.7364 | -60.76349 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55f3d3a0-6026-3782-bc87-6f7b010a75bf | -10.62497 | -61.42621 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b5f696f-bf57-37c1-abbc-b4874dabf7fe | -10.62426 | -61.43133 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e98c4722-a4a5-362e-8037-e2cdf5950f1f | -10.45098 | -61.26973 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22c46bbf-e849-3522-8f88-01707efbfdc4 | -10.45048 | -61.27324 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 220cbc88-043a-3d3a-a5d8-957f2d98bd35 | -10.44801 | -61.26188 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30a4d7d4-10a3-3e78-914a-8c71dc3589a2 | -10.44698 | -61.26919 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7a94291-9ccb-3db0-9395-0a9d61b52e4d | -10.44648 | -61.27273 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6631f42-0bfc-332d-a329-1b605c112feb | -10.446 | -61.27618 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e843b9b-96b1-3b17-ada9-15d086ce2222 | -10.44352 | -61.26483 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b428ec4-654f-3f9b-9900-ce60281d99cb | -10.443 | -61.26849 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cac065c8-0a64-3837-84a0-bb79d3e6bfad | -10.42849 | -61.01451 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| deb75eb9-7a64-3721-a15f-0c3f279e0ed1 | -10.42796 | -61.0182 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ee53f74-86c2-310f-8380-c26560e91368 | -10.4278 | -61.02207 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ec03292-c820-3ad5-8942-6a22a4ead739 | -10.42744 | -61.02183 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac8e8c90-3561-31ae-a31b-9c1bad73814c | -10.42731 | -61.02563 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a97da22a-e9ee-324d-aed5-0a3f8b67aaf5 | -10.40703 | -61.26353 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 862ac0c5-187b-3cf5-afcd-0878667ecc7e | -10.37822 | -61.19335 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 407675f6-a03f-3e2c-8728-1a2932b19a01 | -10.37522 | -61.18565 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f7372506-2697-3bd2-b5e4-635bbe42e81d | -10.37421 | -61.19278 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 97c89255-371f-37a6-82d2-ff2ca67df0e6 | -10.37121 | -61.18507 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 082ea501-2512-3b26-9b9e-c8af9e30b31a | -10.37071 | -61.18864 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0ce6c1ef-a38c-3339-9d16-6293602c83ab | -10.3697 | -61.19577 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5cc6a147-ba4b-3750-9757-6f9293b241f7 | -10.36821 | -61.17737 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74fa6150-aa6f-342d-aa35-04d6feb5a5ee | -10.36771 | -61.18092 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3699440-de34-3ee4-9594-c739b677c3e2 | -10.3672 | -61.18449 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20127188-2836-3c41-a447-827844831921 | -10.3667 | -61.18805 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4b472f7-3c13-32b0-96d3-86ddd4240066 | -10.36569 | -61.19516 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c9fa4f8a-5dcd-340b-ad8e-0f68423aa304 | -10.36269 | -61.18747 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cb45bef-95ea-33a3-bd0d-e38b692d757c | -10.36219 | -61.19102 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 826c0dce-4dcd-3ebc-8f7a-b50ca21b629a | -10.94356 | -61.1358 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37572e7f-43b6-3d6c-ae97-a74c45c6c8db | -10.97956 | -61.08828 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d208f144-a93f-37be-905d-6aeddb584171 | -10.94457 | -61.12874 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f6a7a45-6fa8-3c40-9dc7-01a2d515cba7 | -10.94056 | -61.09854 | 2024-10-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ccbb19c-ee47-33c0-9ca5-05433fdd19f0 | -13.51655 | -61.76217 | 2024-10-15 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d347005-f056-3733-b326-1e3168b35bba | -13.36093 | -61.34718 | 2024-10-15 05:44:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| deca4f26-c6a3-3e19-9a64-55bd6e685ea1 | -12.97467 | -61.50116 | 2024-10-15 05:44:00 | NOAA-21 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README74.md)
