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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92fc928d-3160-3c95-b051-c147f6d87df3 | -10.09199 | -45.51624 | 2024-09-29 04:49:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8efb78c1-8900-3d97-9d5d-591f58456f98 | -10.09128 | -45.52166 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bee8754b-4ceb-3fa0-acf6-3b8c755c8dbd | -11.88133 | -45.56029 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19bab4ea-33e8-367d-89de-616006b8af7f | -11.88038 | -45.55972 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fd00d45-0582-35eb-a06b-9b927526b6d1 | -11.87707 | -45.55393 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2ffcdcf-9de0-3992-aad8-86a1fd57e211 | -11.87615 | -45.55347 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 265e9f1c-c098-3046-81ee-b5e57f7844e4 | -11.77961 | -45.47663 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6fbb5dc2-6a0a-3f09-ba66-eaf9b1897208 | -11.77948 | -45.47561 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e820737b-b342-353e-978c-3e88c72250a7 | -11.7787 | -45.4815 | 2024-09-29 04:49:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4e7bdc6-6838-3d77-a31b-0b7b34f9893f | -11.76108 | -45.50352 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e49d9bcf-5319-3ea1-baa1-b726315e93fe | -11.76073 | -45.50251 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d91f9e9-2bff-3ecf-b7f1-e945184321ca | -11.76036 | -45.50942 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ba7df37-2bb1-32ea-9d5a-db57de91f3a3 | -11.75996 | -45.50842 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85191560-3e0b-3ad7-b4e0-6850cc556a58 | -11.26087 | -45.39117 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b156d56-2bb3-3f71-947f-0efcc657fdd5 | -11.2604 | -45.38919 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0392b9f-9893-3819-8dba-bcedc095fbd5 | -11.11657 | -45.62641 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 59661ea0-2697-3505-b9c5-650eb5ba444e | -11.11582 | -45.632 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 6a9efba5-a638-382e-9cce-07132b79881d | -11.11389 | -45.62746 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 16af9c41-0fd0-3ca7-a2dd-ef5099015260 | -11.11318 | -45.63305 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| bd895701-9875-3a2e-9b90-4506a0c62c81 | -11.11092 | -45.63141 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 84eb8b78-5c75-321a-b1bb-ec1e45869c53 | -11.11018 | -45.63696 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d0fac38e-5ba6-3167-ba64-9054dcc64040 | -11.10898 | -45.62686 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97af9c1b-dc1e-3ae6-b236-4d0ba72a1aaa | -11.10828 | -45.63243 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50f21a51-0fb4-351c-9c5c-5324c4fc3050 | -11.10602 | -45.63082 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 616836ae-089d-3cbf-bd09-8c2ea0f08809 | -11.10339 | -45.63182 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 89f81380-5f33-326f-8597-359998b875d4 | -11.10269 | -45.63732 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| df4885ae-bc36-36bd-b0af-fe61a21dcb36 | -11.10114 | -45.55496 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b47c197a-0fff-396f-8973-b6088c6c331b | -11.10113 | -45.63017 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c50db07-9199-3414-bdc6-c603972f52bf | -11.1004 | -45.63567 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 833c0ca2-be54-31e7-92da-2f2927a92af9 | -11.09967 | -45.64113 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 33871877-4aca-3128-80d6-ce1b61b6354d | -11.09617 | -45.55477 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 746b61a3-f2cf-3908-96bd-649f1b3099ca | -11.09552 | -45.63497 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 20fb60b7-1bde-3657-bf19-2b79b05bf68d | -11.0948 | -45.64039 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9b0cd7eb-58d4-31a1-a008-0f9726ba772b | -11.09064 | -45.63419 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25dab09f-ce57-3972-b578-2b7999ab5687 | -11.09042 | -45.56041 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ca6921d-3603-3d56-a469-9a3dc236479c | -11.09008 | -45.52492 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c93b61e3-902f-3b0c-8119-5a5b95c23c5e | -11.08921 | -45.64499 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e22b5a-b649-35cf-a811-985df411821c | -11.08664 | -45.5129 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a41adf5-42ba-3afc-a3db-d524c44a45c1 | -11.08515 | -45.52433 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e6fa8e28-15bf-349b-969e-f8ac6a37a44d | -11.08366 | -45.64938 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dff9668f-413b-3f52-a352-64332efe9e95 | -11.08096 | -45.51799 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 31bcd346-3c23-3142-b769-4b5ed66315ec | -11.08022 | -45.52368 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72d1608e-47ea-3b22-8af6-0bac9fb58ad8 | -11.07884 | -45.64825 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fddba365-9477-3a3a-9067-8aaaa8716412 | -11.07686 | -45.62556 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dd5d9f3c-c3e7-3eb1-a0aa-19a847f4ec0b | -11.07402 | -45.64715 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6fc4da1e-9c18-35f9-80b1-44c235293906 | -11.07329 | -45.65265 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 74744e61-20c0-3e0d-8e87-6b54719084bb | -11.057 | -45.70119 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56c206ff-4b43-3724-bf72-c3ce4633b344 | -11.05628 | -45.70662 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| afbc58e9-a165-3ac4-ba7b-5d0d1c5c7e9e | -11.0556 | -45.71185 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 80de166f-16f7-38c5-8a55-a832dd699420 | -11.05486 | -45.7175 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 34cf2eae-b0f4-3124-9d87-20f413daefd5 | -11.05454 | -45.7948 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 865dd3d6-6b08-306a-91db-fe4562644ca6 | -11.05384 | -45.80009 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e4c65ed-c911-3f9b-abd7-232fe14bf998 | -11.05069 | -45.71157 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edb72061-3931-3761-aa87-6aefff82b9a1 | -11.04968 | -45.79433 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40c5e564-b7a3-3098-959a-7b1ec88a5806 | -11.04413 | -45.79918 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d39dc5bb-34ed-351e-ada5-64b158c8c5a5 | -10.89886 | -45.50232 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed337823-bcc0-3f15-bf95-1d7bc88e5530 | -10.89389 | -45.50201 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8006fbc-45d6-3f10-b296-f8a15929d352 | -10.87121 | -45.52225 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af1e6365-cc1d-3998-851e-a2504f2282e7 | -11.30394 | -46.15829 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b638a90f-787b-39f8-91b4-0a2980869859 | -11.29456 | -46.15641 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 65f96f60-7b1d-31ce-aa33-39b69e8f2429 | -11.28985 | -46.15556 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3a72e6ac-c7f2-35af-8e4d-fb5eadc034a1 | -10.86098 | -46.00702 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9c85a67-41a8-3b5f-903e-8e7314eff374 | -10.86033 | -46.01205 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f833fb78-cbf5-3adf-9d08-ac768b026bc5 | -10.85978 | -46.01022 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6011d76-d919-3b40-8a52-eeec33daae44 | -10.85968 | -46.01707 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f626b5c-a2ee-348d-8b5a-d18e657990ef | -10.8591 | -46.01523 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16f83bbf-68cc-38ac-af7f-d3ea0031afe9 | -10.85904 | -46.02206 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6403e60-b538-344f-a618-f80f7f4970d4 | -10.85841 | -46.02023 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7456ca8-9ab8-32cb-8e2a-bd79314aad94 | -10.85495 | -46.01629 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f38f66b-bc50-3e0a-9734-f7576cb20557 | -10.85437 | -46.01447 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 010e3d3c-2360-34eb-962c-eaf2cd0fbfde | -10.8543 | -46.02131 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 59d248c0-5823-3897-9a5b-60e35ab684ad | -10.85368 | -46.01947 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1caa9de8-6892-3573-9341-7f75fffc0210 | -4.92426 | -45.13317 | 2024-09-29 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 822af9ee-4e71-3941-bcda-5d693fb5b8e4 | -4.91966 | -45.13237 | 2024-09-29 04:49:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3c331eb-f1bc-3fda-9fd8-7b215155c93e | -5.72969 | -46.48307 | 2024-09-29 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb82cef5-741f-3013-b547-93f1f514ee4a | -5.24336 | -46.16972 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fc312c4-ec0e-3088-8da0-3ddc244f1762 | -5.24135 | -46.17078 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51387f42-d01a-3b88-9a1d-4206ce65d2ee | -5.23904 | -46.16909 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fecd0dd6-61a8-3411-8810-84c6883df429 | -5.23098 | -46.16378 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69186c5a-5bad-35fe-99ef-b16392f2528f | -5.22899 | -46.16485 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8ad300d-e9e7-32d6-81b5-4e22123270e4 | -5.11887 | -46.14897 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79082c50-b352-3d3c-8c0a-66fcb574a154 | -5.11457 | -46.14825 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ba33f25-a4b8-3656-ba92-068854723f0e | -5.08379 | -46.17726 | 2024-09-29 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f015c14e-2b74-377d-9c28-8270ced7694a | -5.90117 | -45.59457 | 2024-09-29 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d441041c-72a4-3bd1-a801-76b2047d2a4e | -5.32795 | -44.9912 | 2024-09-29 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b38b43e-11c8-3d43-a84b-c1623600ad82 | -5.32397 | -44.98552 | 2024-09-29 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61d35d69-6b1b-3fdf-8981-5042b09a0931 | -5.32325 | -44.99052 | 2024-09-29 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f26ef14-526e-3390-9bd8-f991323a86c9 | -5.2221 | -45.14304 | 2024-09-29 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d42313a3-4a01-37e6-90b6-ceaad83fd78a | -6.39666 | -45.95619 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03b0af62-4699-3efc-8d7c-deeeb136e7fe | -6.39221 | -45.95547 | 2024-09-29 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c98f331-ff24-3701-874f-e34d8884c21c | -7.72868 | -46.561 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94e4a8f3-0c71-3079-9af1-86641f93ade9 | -7.72491 | -46.5562 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa5db678-cca9-3fd4-a8b1-c278b855ccc6 | -7.72431 | -46.5604 | 2024-09-29 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4708f3f-2eb1-3fa0-9473-f3bc0de59890 | -7.49014 | -46.12861 | 2024-09-29 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca127ab9-8641-30d8-bfd7-6d2f68c20ec1 | -7.83622 | -45.53469 | 2024-09-29 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e74de2e8-6e87-3830-87a9-0af191ffcc12 | -7.83551 | -45.53984 | 2024-09-29 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed1a26f2-0171-38fc-a3e1-dc875bf018dc | -7.82125 | -45.57395 | 2024-09-29 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9349a92b-6554-3d40-a71b-c6ea4e55c324 | -7.14589 | -45.59608 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cf0a6c59-2e39-3bb2-a9d7-27cb772707ba | -7.14533 | -45.59385 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f45fc725-815e-3d00-9eb3-90ea1effc456 | -7.14466 | -45.59872 | 2024-09-29 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README43.md)
