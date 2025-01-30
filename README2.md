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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ce80094-b958-3d45-aecd-a810a4f5f30a | -6.935 | -43.4976 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52fadcc3-5e69-3d2f-8603-ec50fbddc532 | -6.94189 | -43.50605 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| d65dec7b-2247-30a1-9543-e08e7eae3dc1 | -6.94309 | -43.49893 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| b226d14a-c91f-3b4e-b4dd-0443f8acf536 | -5.1484 | -43.22669 | 2025-01-30 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5acb2583-7116-302e-aa47-8bd90a5bc358 | -5.73464 | -43.49658 | 2025-01-30 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7af240b6-0d1d-333b-9aae-b7842e2f2cfa | -7.17871 | -44.99466 | 2025-01-30 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eec27ce-eec3-3445-b74b-842bb9325403 | -6.93036 | -43.50047 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c78fc62e-60ca-3a04-96fc-90e5fd514518 | -6.94023 | -43.49119 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6615d61b-6921-3405-8fc0-2d9a591d1009 | -5.1478 | -43.23034 | 2025-01-30 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fa4c2ca7-6a89-340a-8c31-9944aa97f64c | -6.94893 | -43.48887 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00145a4b-2de8-390e-b42e-dfcf9459c9fa | -6.92916 | -43.50758 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8444cd99-8c2b-3d74-82f7-aea27ec9a0b0 | -6.46465 | -35.24252 | 2025-01-30 03:53:00 | NOAA-21 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4e1954de-6ef9-3b2a-8c3a-530e58ed30fc | -6.93784 | -43.50542 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 2d5ea3d6-80f4-362a-9a43-16453e671ea7 | -6.93964 | -43.49472 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 0d67a6b1-acf8-34d2-88b2-9cdf47b8443e | -5.51811 | -42.88843 | 2025-01-30 03:53:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c2535bb4-dc29-3382-bda8-c8a13cd64e48 | -4.91691 | -38.60215 | 2025-01-30 03:53:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ee11ffba-6ca5-3258-b57f-17a8a97b1edf | -5.46459 | -42.92538 | 2025-01-30 03:53:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c02fc904-6e7b-3cfc-8c05-935bf61b7fee | -6.94428 | -43.49181 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82cbd282-32a6-30cf-89ba-f8766ddb6595 | -6.94368 | -43.49538 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 645f2e2c-a7d5-35e4-b5b7-de587da8d947 | -7.79827 | -43.0845 | 2025-01-30 03:53:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c0fa432-4e07-39ed-b538-4a8f92d17f86 | -6.94083 | -43.48765 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2a936ee-2fa5-3ba9-b31f-56216f0769a8 | -6.94129 | -43.50964 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 32a94ca4-f368-350d-894f-94af98944998 | -6.93663 | -43.5126 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 113f6933-d5a2-388a-a9b4-9f94ce1bc5ae | -5.15187 | -43.23106 | 2025-01-30 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3bf3106b-85ea-3bdb-bfaf-d4b4bed9d043 | -6.93724 | -43.50901 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ba9c7d2c-b862-39eb-bc76-2c802904917f | -5.46403 | -42.92886 | 2025-01-30 03:53:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3172a647-9a8e-3b85-8625-5792f2d98b4c | -6.61962 | -39.17987 | 2025-01-30 03:53:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07ea96a2-832e-3641-a5ba-6cf0a44dea30 | -6.94713 | -43.49958 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b12447b4-ae54-3232-85b8-edb8e62cdaf3 | -6.94488 | -43.48824 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00ffdd1f-b1ce-346d-9b35-5bb342c7519e | -6.94833 | -43.49245 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b4ce2f7-4147-324e-8655-cc717bb3e9c5 | -6.93904 | -43.49828 | 2025-01-30 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e56f8f99-9f0e-39b9-84db-a5945e3771dd | -11.26798 | -44.49685 | 2025-01-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9a8b3bf-4a04-3f91-b6a9-cf97d9439245 | -15.51094 | -41.91103 | 2025-01-30 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60196576-daea-3d3b-9a1a-8f8d86f37001 | -4.58658 | -38.34448 | 2025-01-30 03:55:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6f07e7cd-c994-356c-b914-b0b8478a00c0 | -3.42473 | -39.02021 | 2025-01-30 03:55:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74cea213-c5a0-30cb-a93f-82ee455de4d5 | -11.59319 | -44.86551 | 2025-01-30 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 286e7dfa-e21c-3281-87fa-57c1716fdf2d | -11.25715 | -44.48753 | 2025-01-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4dd6999-a16b-3fa4-b32b-d825b42ef97c | -12.78096 | -38.49836 | 2025-01-30 03:55:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6c180a93-46c8-3252-ae34-ec31c8e58254 | -11.85366 | -44.62504 | 2025-01-30 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54fc2277-9a23-3bd9-bf26-c5152e0cd2ee | -10.69509 | -37.05036 | 2025-01-30 03:55:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73792c68-4dea-3e33-a9f9-087721bfed2f | -3.86812 | -40.45503 | 2025-01-30 03:55:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 14b907ab-e851-3e07-9466-cce2c56dbcfe | -7.89221 | -44.19016 | 2025-01-30 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93ccc6ed-25fb-3eca-8de0-6b924dca5265 | -8.39481 | -43.5681 | 2025-01-30 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa52b004-0e51-3f81-9e97-2c1fe03ac368 | -11.26396 | -44.49612 | 2025-01-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac8ac177-7efc-3c09-8362-68a7ef63fee1 | -11.26117 | -44.48824 | 2025-01-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 381bf848-2f97-3889-9e45-1811aa2e51de | -11.25653 | -44.4911 | 2025-01-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c84fbfe-a29a-3efa-a50c-86f41df4f7c9 | -12.08386 | -38.07505 | 2025-01-30 03:55:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aaccf286-8a24-3a85-a77a-d2e50f0171ab | -15.51431 | -41.91161 | 2025-01-30 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| deb422e2-837b-3947-b88f-c4fe0c166c07 | -11.59385 | -44.86179 | 2025-01-30 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ff939da-e23f-3d16-b3b7-f416562e9462 | -10.74786 | -37.05066 | 2025-01-30 03:55:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 3c36e3a4-e4a0-3ff6-b49a-d3c916afa9d9 | -13.47849 | -44.01937 | 2025-01-30 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b02d9c1-7d5c-3f03-b528-05c64974699f | -11.69578 | -37.94794 | 2025-01-30 03:55:00 | NOAA-21 | ACAJUTIBA | BAHIA | Brasil | 2900306 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 48d5356d-169c-3af8-8968-ff3d55da561d | -12.2838 | -40.23306 | 2025-01-30 03:55:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 745edca1-e7bb-3940-8ada-68e01d0e66eb | -11.59795 | -44.8625 | 2025-01-30 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 460c2994-2ba7-352c-b231-573e2afd3c30 | -3.12571 | -40.99386 | 2025-01-30 03:55:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b8d6c2b-282a-37db-b549-5fb6c2fe2d4d | -11.85302 | -44.62864 | 2025-01-30 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94b36f77-16f5-3440-9f30-915c2309e424 | -10.78424 | -45.20222 | 2025-01-30 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdf662eb-0f3a-379e-ad78-9ddf3ffa55a1 | -9.90741 | -38.10497 | 2025-01-30 03:55:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b88add14-7bef-387d-8aa6-95bff7f9c3a9 | -12.0805 | -38.07453 | 2025-01-30 03:55:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7b3b2010-9b45-35b6-ad8c-49db3f09866a | -3.86459 | -40.45448 | 2025-01-30 03:55:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e42b7ab-395b-36b1-8772-e1e6bc2e9eab | -17.07103 | -39.42358 | 2025-01-30 03:57:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0da351d5-218f-383d-80ba-5e7cd927ff8f | -6.9535 | -43.515 | 2025-01-30 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f06377ff-a332-3247-a19b-5a75c544b23f | -6.9346 | -43.5168 | 2025-01-30 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 69286f36-3fac-3b33-844b-ea86ce5e367f | -6.9537 | -43.4917 | 2025-01-30 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| cd15c9e6-0596-3e38-84c9-5e00f850e068 | -6.9349 | -43.4934 | 2025-01-30 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 250.5 |
| d921145a-473b-3490-8ab5-88c832d5dbfa | -6.9349 | -43.4934 | 2025-01-30 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 73464b64-4647-3e7b-8a1b-833d3cabed0e | -6.9537 | -43.4917 | 2025-01-30 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 235f7cc6-00a2-32da-b721-7b35b5289baf | -6.9346 | -43.5168 | 2025-01-30 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 75ea1750-a5bb-358d-84e2-4e0470dfafcc | -6.9535 | -43.515 | 2025-01-30 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fe154240-87cd-3857-89fb-bbb6a33d713a | -6.9537 | -43.4917 | 2025-01-30 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 51024e0c-646b-367e-8a4b-76da4608b342 | -6.9346 | -43.5168 | 2025-01-30 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| ef4bac7d-1f56-38e7-9dc3-f9d1317da906 | -6.9349 | -43.4934 | 2025-01-30 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 207.4 |
| 0dc6787d-dfb4-334a-898a-636226ae3039 | -6.14724 | -43.26229 | 2025-01-30 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c5e318b7-5210-3e2f-87f8-93ad949a05bc | -6.93696 | -43.50148 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 1f363170-a03e-37ae-a751-a4d86cc13efc | -6.93528 | -43.51237 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf57e080-ed78-3ce0-b395-e81f78c2df7d | -6.93867 | -43.51289 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edc6b269-4390-3e0b-bed2-8347294b44b7 | -7.17968 | -44.99477 | 2025-01-30 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fea41853-cd51-3188-9cfb-1e2c34a5bf5f | -6.93413 | -43.49733 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b4f5e04-659a-3d1e-b078-6c789a2129a9 | -6.92849 | -43.51134 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06e59a44-db6d-30eb-9e39-3ce2ce7fc183 | -3.86472 | -40.45534 | 2025-01-30 04:21:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ada44771-a4b9-31a2-aa06-96fd1a356233 | -6.93074 | -43.4968 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67923a59-8ba5-3c97-bd5c-5b418cdd853a | -6.93923 | -43.50927 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 03309cf4-b441-383a-a313-1fdcb08e2795 | -5.01652 | -41.86887 | 2025-01-30 04:21:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06d8a9e4-6724-3298-9f2b-4fd68648cb7e | -6.93244 | -43.50823 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fc564f34-f530-3e5a-b284-145454cc99ee | -6.9347 | -43.49369 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa31743c-cf42-39cb-84da-9ccd7e229974 | -6.94206 | -43.51343 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b7acd8b-084a-31ec-986d-b2d7f73c8a06 | -6.94375 | -43.50255 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 014483f6-5729-31a6-9610-e983e427c825 | -6.92961 | -43.50409 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33bfd49b-86bf-32e7-abda-1a584b6d58a1 | -6.94318 | -43.50618 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e07941ef-60be-3121-8164-4083fb76516f | -5.73361 | -43.49798 | 2025-01-30 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68afb604-8ef8-3e20-8375-837f0e3fd834 | -6.44469 | -40.00263 | 2025-01-30 04:21:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e34a102b-1bcb-35d3-bce3-3525c519f231 | -6.464 | -35.24147 | 2025-01-30 04:21:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c2263c8f-2387-3729-8c4a-d2b5393855e4 | -6.46228 | -35.2438 | 2025-01-30 04:21:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 407547d5-4c5c-3b6c-ac25-1424b36604bb | -6.92622 | -43.50356 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 958a4c18-034f-3038-ba02-1919afad476f | -3.86415 | -40.45671 | 2025-01-30 04:21:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f36cbf59-9a4d-3e04-b173-bb17407ed576 | -6.94488 | -43.51759 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95572aef-b16a-364a-b0e9-9fd423897af2 | -6.93753 | -43.49786 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 29ace86b-3afe-33f0-84e3-2d9170fa1251 | -6.94714 | -43.50307 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4424727-dc38-3d43-a9d4-a24dc87a7ffb | -6.44068 | -40.00209 | 2025-01-30 04:21:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6e6e78cb-7ea4-33cc-b829-be67ec443c63 | -6.93132 | -43.51548 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
