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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0347679d-48d5-3014-8855-7e8ad6e9278e | -7.60612 | -45.84037 | 2026-08-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3abf398f-489f-36b2-89c7-d4a6b72f2235 | -6.12369 | -53.55591 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61aef0a2-4f42-3505-ba6f-18597db0a4f9 | -6.34874 | -44.09994 | 2026-08-30 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3d4ec4f-7a29-3293-8ec3-0cbce3cf4178 | -7.61658 | -44.84841 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e1360f9-77d5-3227-83a5-79a9be4ab5b8 | -6.06437 | -44.8797 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aab788d7-4c35-3730-a6b4-14df7a315758 | -6.8185 | -51.15474 | 2026-08-30 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14b31ac4-d42f-3944-867d-dc5c812c50bc | -5.60675 | -44.12336 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3367d3e-56e2-3a01-a810-7bc609267c80 | -3.4926 | -54.65309 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6275003-a1dd-3c33-b3ea-b26b9720b69a | -5.28633 | -50.93962 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6efec352-5122-3282-92ed-67e222c58e78 | -6.92833 | -55.70242 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1c6b112-be15-3325-ab9c-2a0b594b4ad1 | -6.60325 | -56.38064 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 397d96e0-7316-303c-83ff-7f09ec393fe6 | -3.49327 | -54.65032 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ced4e4c-d278-395a-aea1-0618c7c9ed5a | -4.09627 | -50.42889 | 2026-08-30 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8055988c-67f0-3db3-9dc6-7f2101b35b8b | -8.15307 | -45.50626 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e05b8c2-0034-3a28-ae53-96c42b995504 | -2.89638 | -48.27359 | 2026-08-30 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95373814-7eef-38a1-9c9d-e94aef4f593d | -6.94298 | -55.71222 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff0ef550-97f6-386e-b61b-49df17b90ab2 | -5.88162 | -57.76479 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 110ab965-07ec-32f0-a65e-fc0c5d74a9b0 | -6.34585 | -44.09562 | 2026-08-30 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a682bf24-6d70-3a3a-a11e-140486c3b6cd | -5.97026 | -57.69415 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16c625eb-3f86-3d17-a655-bf441bcc0ff1 | -6.42518 | -55.52754 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03d85aa7-1960-3380-8219-8120672c5176 | -7.37788 | -45.10244 | 2026-08-30 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0541887-eeb0-3a46-a772-c1bdc097c8cb | -6.86843 | -56.57426 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d8c48df-9d0e-3f2b-acb5-ba2b3f3353c2 | -3.48532 | -54.66464 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 117d4943-51ab-354b-a537-5cc6e806fa62 | -6.90518 | -41.62873 | 2026-08-30 04:32:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b06ef59f-d3cb-3ef0-be04-17f6602d06c1 | -8.14286 | -45.47167 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a78e9d03-8034-32c2-b6a5-073684ec1ce8 | -3.48645 | -54.6587 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3b48b8b-b93d-3882-8221-649f96706727 | -6.90423 | -45.68452 | 2026-08-30 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df1b8356-584a-38c0-9e08-4cd5b5a7b1db | -6.07825 | -57.89796 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5cc3b316-b68a-3413-87b8-00a798ace031 | -8.25233 | -46.5055 | 2026-08-30 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8049c099-892d-36b4-a9cd-89f3569da2ce | -6.06347 | -44.87637 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f47e44a-e6b0-3bf0-b6a6-43e393af7f66 | -7.0908 | -42.83448 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b6c10a33-c863-3177-911d-ae46d20f5571 | -8.01582 | -48.01213 | 2026-08-30 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 608e0f78-be3c-3a4a-8317-fe964176e591 | -3.43387 | -43.20535 | 2026-08-30 04:32:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bebd0b62-3ebf-32c9-88b0-9ec3ae9e1f6c | -8.16178 | -46.17254 | 2026-08-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9d38d89-3e7e-3b56-a9ad-a9e5fbc70124 | -6.93302 | -55.70676 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b456da40-0c75-308d-8301-c1115a15c559 | -6.1543 | -57.79123 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f75bd88-fe6e-3748-8420-24c226231dcd | -9.46647 | -46.18612 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d3f0ed5-a72c-3ed5-ae8d-0d500ad690fa | -6.54113 | -55.10769 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93da12dd-a038-3aaf-af9a-eef9f463963e | -6.11822 | -53.55999 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1c0e5ba-afcb-3f4d-a3ab-087d35371133 | -6.16929 | -45.93029 | 2026-08-30 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5b808a2-67b3-3848-8132-7b82f953c85f | -5.87822 | -57.78347 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 639d5c55-3c36-35d9-b11e-f911d2cd89a8 | -4.0958 | -50.42714 | 2026-08-30 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99774be-fa35-3be3-8365-6d59de5931d7 | -5.48652 | -57.15141 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fe1e6acd-bbd8-33ac-8945-aa810e21c69a | -5.8724 | -57.78437 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4bcc9b4a-3971-3132-a82a-be1a1e846a8a | -6.8297 | -42.87743 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 65957c92-d06d-3c32-bfdb-8ff556a7dbfc | -8.14916 | -45.50927 | 2026-08-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7df47ba1-fdd2-3be5-ac01-5b000ea980f0 | -2.9521 | -43.25073 | 2026-08-30 04:32:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71caa04d-8891-3a2a-aadc-c067bc985b51 | -5.99995 | -45.0835 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e71096c1-fd5d-37b5-a089-0881bd82148d | -3.78747 | -51.41217 | 2026-08-30 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f3346d5-c53b-3049-8f87-e309bda454f8 | -6.7637 | -55.6527 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5e10ccb-a0ba-3b92-b700-833399922a73 | -7.52037 | -55.32021 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7f97a8f-eafe-37da-9b42-58684e14e8c2 | -9.31557 | -40.21576 | 2026-08-30 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 14731fbe-60f5-3fc5-944e-2f8a1b761257 | -7.61544 | -44.85587 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 584ec4c6-7fc9-3074-a96f-24af55c2c9a1 | -7.20879 | -42.74361 | 2026-08-30 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c8f7ae1a-ff3c-3f88-8ce2-c8a1e9ab68a7 | -2.57793 | -48.25017 | 2026-08-30 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01c40593-7364-325c-919e-67fde240b9da | -9.21352 | -46.07007 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a90cca1-3770-332d-bd8e-28bf27a6fa85 | -6.86547 | -41.66529 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1931bb41-74c6-369e-9238-cb2ef1c1c32e | -6.7709 | -55.6504 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f79d7334-5389-320d-9980-b0d2515f9246 | -6.76503 | -55.65275 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f2c0088-566e-396c-8d78-882080277158 | -5.87323 | -57.77962 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bad8a807-94f6-3020-940d-d1fab6014a4b | -2.91334 | -54.11658 | 2026-08-30 04:32:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c87a372e-89c3-38ff-a7c0-728ba089789b | -5.99323 | -45.08244 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c910904e-109e-325d-a69f-8fb50953eb62 | -2.00253 | -44.8038 | 2026-08-30 04:32:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6d31d5b-6f19-332b-8605-c71339d62a06 | -2.93123 | -51.48397 | 2026-08-30 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ee7a208-ea4c-3ed2-a1f6-9ef0f297fe33 | -7.0142 | -59.65657 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 667b35c9-d52c-38ec-99f0-befd31396d5b | -3.37201 | -49.53201 | 2026-08-30 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cc0ed89-034c-34d7-80a2-c9925e0da9c8 | -7.11089 | -42.18913 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e33c6ae-c956-30f0-806c-be11cf6d6e27 | -9.21296 | -46.07362 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 263c6eb1-b2c2-3761-95fc-37d0a1e90c0e | -7.1072 | -42.21358 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2f46fded-8bb3-3086-91cd-93091955d00f | -9.21408 | -46.06649 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c45596e-25f5-361f-8549-85ef38601cee | -5.88875 | -57.76048 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2344adc8-91c3-3406-8d3f-0759dddcce7c | -8.22326 | -40.77244 | 2026-08-30 04:32:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2ff46eab-ee5a-3e02-9b21-0816b35b8016 | -6.90556 | -43.65448 | 2026-08-30 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b91fee3-bcdf-3b6a-bcc3-d98180eb5965 | -9.21631 | -46.07415 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1dfa34da-d5fd-3371-8907-7f47e9bdfa69 | -5.31741 | -45.25694 | 2026-08-30 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c41039e6-b199-3890-9526-474a5ac34fd4 | -1.20284 | -54.21334 | 2026-08-30 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b372d6-872e-369e-9204-0d5fcf817237 | -5.04244 | -44.68991 | 2026-08-30 04:32:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64d13c9b-8f76-3229-b1ea-9a6a79cc5d26 | -7.11647 | -48.06563 | 2026-08-30 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a62c69a3-0776-3355-91f7-0e02132aa6bb | -5.48959 | -45.63068 | 2026-08-30 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae1b1153-e9e9-3252-a740-7fa6f447d1bc | -2.0476 | -45.97883 | 2026-08-30 04:32:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe129b49-632c-3e7f-ab9d-54b9a9b27944 | -4.958 | -55.84415 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 546175bb-efb1-3527-910f-ebc69dd5224b | -2.11046 | -49.00242 | 2026-08-30 04:32:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2b7e6892-92cf-3d9e-b962-baeb7c61fcdf | -3.65133 | -40.91924 | 2026-08-30 04:32:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 34b4ce8f-3bf7-3f32-8820-3b6c8916d078 | -4.08482 | -45.94414 | 2026-08-30 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e0e73bf9-4c15-3f0c-b223-a4a833b45b9c | -6.94183 | -55.71869 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d89b234a-99fb-3f9f-aa66-0e86b660d4e1 | -6.7643 | -55.64942 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3797a61a-a7f1-31bf-ab45-8242b7f49772 | -4.95928 | -55.83678 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4954a0b1-8732-37f5-a76e-07723643c182 | -2.93566 | -51.47953 | 2026-08-30 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7a193130-8e3c-3683-b158-1d46574b65ba | -8.01639 | -48.00858 | 2026-08-30 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4105785-f8b4-35bc-b1e1-f55e5890cd98 | -7.12268 | -56.55095 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f43edad5-a9e2-3857-a382-727860f060c0 | -6.86792 | -41.67615 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9ba2552c-c549-30ab-a006-df13477e6d03 | -4.08206 | -45.94018 | 2026-08-30 04:32:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 669dc817-437f-3ec5-8b70-200817e8d82c | -6.86753 | -42.87857 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 11eeb513-b902-334c-8d0a-227a37b50909 | -7.61316 | -44.8479 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afcd36a4-f77b-396a-a803-6066671199eb | -6.6439 | -53.18094 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7b3e364-9e41-3294-8a26-c80c60c8b5d9 | -7.07861 | -42.21917 | 2026-08-30 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48b79c37-f3d4-32b4-9fa9-1e20884adf88 | -5.50782 | -44.62445 | 2026-08-30 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50fe60e0-1749-393a-8465-bb8b1f2692ce | -4.66867 | -43.22182 | 2026-08-30 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c59f9b81-adf8-3937-80a6-85a059a8afdf | -6.48484 | -49.90405 | 2026-08-30 04:32:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24886ae3-809d-3ea5-bae2-a2fbdfde9541 | -4.92523 | -55.77207 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
