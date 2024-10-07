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
| b5283097-9039-3d74-aea4-d40b5304da4e | -6.64962 | -42.12333 | 2024-10-07 03:34:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b2fe4414-9734-3561-a4b1-fe307dd351f2 | -6.6491 | -42.12623 | 2024-10-07 03:34:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ec0e851e-d801-3c1b-868b-dfe8807a9516 | -6.64231 | -42.13447 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c2a4f297-860c-33ce-bcf3-c3f7a9959d48 | -6.64063 | -42.13502 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edd5bdcd-d820-3208-a66e-c3faa40086a9 | -6.63495 | -42.13719 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5cbdbeb8-701c-3cc7-90df-e2852d78b9b7 | -6.62926 | -42.13939 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 576356b0-169f-3921-ba47-2f314b563d7e | -6.62413 | -42.13833 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e1dc0883-67f0-3558-976e-1750195977c0 | -6.62265 | -42.11628 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc29d055-c0b8-3281-9e06-edf9357ef605 | -6.62213 | -42.11927 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b0b5ff86-18c0-3156-8e6b-01b38aaf43c3 | -6.61641 | -42.1217 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66b9cc8f-b4b9-318a-aec2-e0aa104c2773 | -6.6159 | -42.1246 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e06898e-202c-3487-b782-bd53e068bcea | -6.6154 | -42.12752 | 2024-10-07 03:34:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3035cdd9-364f-3727-9e33-281276f9b90e | -4.28805 | -43.74292 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 906ca6ad-dbbb-3618-9094-f39768880608 | -4.28358 | -43.73329 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecf9b855-a5f5-399b-8de3-33626116c8b1 | -4.28286 | -43.73749 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b1ebe58-14d7-3a8f-a054-24fa51782481 | -4.2821 | -43.74187 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4a7570a-b7cb-30d2-a941-e20e2e1f1265 | -4.28135 | -43.74625 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 052e3c7f-c94c-3d16-8f81-2a401e17b1fb | -4.27689 | -43.7366 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| be9fe4cd-5c8a-358d-82f6-99d997532fcf | -4.27615 | -43.74089 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 24d14a5b-e9da-38ca-a4af-5bb05e913653 | -4.2754 | -43.74523 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 4ac459f8-7ec2-3a64-9716-6e1488d33f33 | -4.27463 | -43.74969 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 102a9972-e491-3173-a03a-e8cc1e8e5897 | -4.27385 | -43.75417 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4a4729cc-1a73-30fa-bd60-c10179699dd0 | -4.27091 | -43.73574 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0d6a3bd8-6c49-3a0f-9e36-e071df73bcb9 | -4.27018 | -43.73997 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| de77a43b-edd0-345b-b808-b7e8908d8d83 | -4.26943 | -43.74429 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| dd84ac27-a7b0-3f08-ba3c-e64496616e13 | -4.26867 | -43.74866 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 411faad2-81c3-3d4d-8879-2c236300871e | -4.26492 | -43.73498 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4ce22c42-81c4-3148-a629-65cc946ba640 | -4.26419 | -43.7392 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fb35e52-5833-3fd4-9a17-79d9077118e1 | -4.26346 | -43.74342 | 2024-10-07 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b00ddce-798c-3fbd-89a8-621fe87a138a | -4.04676 | -43.24417 | 2024-10-07 03:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e3ab39f-1b32-3014-af43-1963f6c8ae85 | -4.04099 | -43.24311 | 2024-10-07 03:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf33b4a4-ce52-33ec-8f2a-b79e0e974b99 | -4.04031 | -43.24711 | 2024-10-07 03:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80f21fca-ea46-39a6-90a1-2d761f2763c9 | -4.03962 | -43.25113 | 2024-10-07 03:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 472cc9c8-25e1-31f2-97f9-2344569271ce | -4.01787 | -43.23906 | 2024-10-07 03:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa5b5279-9011-3ae1-b340-87848ef142af | -4.01719 | -43.24305 | 2024-10-07 03:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa88d277-627b-3631-b829-c30831d9f347 | -3.95162 | -46.45427 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9cbb7a9-3119-3d5c-944a-b539eb781415 | -3.94897 | -46.45414 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d4d1ac3-546a-3abd-881b-eae7512fdeb9 | -3.94334 | -46.44514 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c0a7fde-6506-3f73-bf6d-335b6cddddb1 | -3.93899 | -46.44352 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1d872c8-7b6b-3750-9926-3aeb42a041e4 | -3.93781 | -46.45026 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ab89ecc6-1711-32d5-b418-6e4e519a9c74 | -3.93631 | -46.44388 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c06bed81-d37b-32ab-b4db-e42ed6654ce0 | -3.9351 | -46.45057 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a06ce46c-411f-360c-8bd9-9394f38f3798 | -3.93195 | -46.44229 | 2024-10-07 03:34:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b7e85d7e-fd34-3169-ae21-051e0c587a69 | -2.857 | -52.8993 | 2024-10-07 03:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 5d1878f7-4750-390d-8f2d-0157dc1416c1 | -2.8569 | -52.9197 | 2024-10-07 03:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7c442cee-0954-3f5e-ab20-34d065fdac35 | -2.8753 | -52.9192 | 2024-10-07 03:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| bfcb8288-1e0a-3021-b6af-0f99a78a03f1 | -2.8754 | -52.8989 | 2024-10-07 03:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1ae1c5df-301d-32c3-a78f-391f7de47abf | -4.2728 | -43.7601 | 2024-10-07 03:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b28f1e9c-fdb8-3b3b-9de2-f614d35e79e2 | -4.2729 | -43.737 | 2024-10-07 03:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 524d9112-44b6-30cc-81a2-c8790d2e528e | -12.71838 | -40.21407 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b478a1f1-fabf-304c-aa36-20b5fb55c682 | -8.93364 | -40.86861 | 2024-10-07 03:36:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ad42ebf-ae00-30d4-a4c0-d0a890105f4f | -8.85465 | -38.88063 | 2024-10-07 03:36:00 | NPP-375D | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e356eb24-5987-364e-be9d-d197ae62d6ad | -8.84976 | -38.88515 | 2024-10-07 03:36:00 | NPP-375D | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 71e33739-a01d-33e8-b134-b61179dd437d | -8.84487 | -38.88967 | 2024-10-07 03:36:00 | NPP-375D | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71960b43-4894-3e4e-a3c4-4b93dd09661f | -10.3096 | -38.93385 | 2024-10-07 03:36:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef02faf4-53c3-3bf0-b8ec-a46259a77d94 | -12.71772 | -40.21774 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f2af5b24-73f0-3e0d-b8e8-57edfbd73c6a | -12.71705 | -40.22142 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c0bfe6ca-0dc6-3df6-b0f9-184a5258ab2d | -12.71639 | -40.22508 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| fd9f9056-c5ba-3b0a-adf2-fcf973fb9cc0 | -12.71517 | -40.21706 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 06cb4697-5e52-3b23-b52b-ca18f9b3fd90 | -12.71453 | -40.22075 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ff7dccff-fe9f-3091-9902-742cb671cf3f | -12.71389 | -40.22442 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c0c901f9-f3a8-397d-9554-12d2f213a875 | -12.71363 | -40.21701 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4adc780-00e9-3d62-86d0-827424bd6f4e | -10.06956 | -36.55981 | 2024-10-07 03:36:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6bd4745b-7dac-3686-b7fa-35635dc424c1 | -12.7218 | -40.21848 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6ecff099-4b16-382a-8371-757e07b88af3 | -12.72114 | -40.22215 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 14215b4f-f7a0-3f44-bbc7-7c8893b7dd2a | -12.71296 | -40.22069 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a8acf71b-9536-31e1-a02f-c69d594e6313 | -12.7123 | -40.22436 | 2024-10-07 03:36:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fa22d111-7766-31db-abae-8100610a1f8d | -8.644 | -40.54722 | 2024-10-07 03:36:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 839ee5cb-502e-35e7-a87a-09a669cec2f1 | -8.6432 | -40.55169 | 2024-10-07 03:36:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fd9bafa5-24f1-3919-b2b4-d1c594454918 | -8.64149 | -40.54876 | 2024-10-07 03:36:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c4420c62-6f8f-3291-a9d3-8fb3e9a50474 | -9.62799 | -40.6129 | 2024-10-07 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 46f78b1f-60f7-30bd-9678-023201fd1acb | -9.57742 | -40.34213 | 2024-10-07 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e54a93d0-4fa5-37cc-bede-def5f9006357 | -9.57308 | -40.34135 | 2024-10-07 03:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d12773dd-cdd3-3525-a57a-29c4183fa8fe | -7.84133 | -42.22805 | 2024-10-07 03:36:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9a0586d-c0a9-36da-9dc0-08e3e2d27ed7 | -7.84079 | -42.23108 | 2024-10-07 03:36:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6d171c14-7e30-3889-b234-a7127aa85b99 | -7.83733 | -42.22117 | 2024-10-07 03:36:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1712ea96-3d75-3b91-a0b9-251edcf0e56a | -7.83679 | -42.22417 | 2024-10-07 03:36:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f880164-ac26-36f9-9b1e-7966f820e107 | -7.83625 | -42.22717 | 2024-10-07 03:36:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 07521c1e-e3a1-317c-b069-7714a5351932 | -13.41002 | -42.23431 | 2024-10-07 03:36:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be688cc3-bd2b-3b3f-80d5-0477d62c8879 | -7.7808 | -43.08382 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 898d3c86-59c3-3ae2-acd8-b80e18347abe | -7.77914 | -43.1051 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b990376-6c3e-30bc-8dc6-f1210d10fd95 | -7.77848 | -43.10872 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 228997f6-e88c-3021-bdca-c403a3757ea7 | -7.77824 | -43.0797 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f677c0f2-77ed-3066-afd2-2e0fa2e7cb43 | -7.77781 | -43.11235 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e8f11325-6c69-3798-a72f-789721e158d7 | -7.7776 | -43.08319 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 51ae7d86-4319-35a6-8db2-a94191a1b544 | -7.77711 | -43.10483 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 026d2428-332c-30e9-9f79-1a5d4a402c42 | -7.77695 | -43.08669 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dbb8cc84-c263-3e72-b9c6-3b87614f7a42 | -7.77476 | -43.08659 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 37893318-9144-3b85-99bc-30d2f9f021ec | -7.73421 | -43.06479 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 514d7b14-ae01-3cba-8b5c-75087551e77a | -7.73353 | -43.06856 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b6e29ea9-fb44-32e8-96df-692e6edb6441 | -7.73012 | -43.05665 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5418fe16-ea88-3467-b61b-e21f81dda857 | -7.72947 | -43.06026 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7fbf1479-5d56-3172-95be-b82d29d6ee78 | -7.72881 | -43.06394 | 2024-10-07 03:36:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f60645c8-3abe-3280-be95-0a8677dbe49f | -7.64699 | -42.49714 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bc98d1e8-a0e5-39a7-81e9-75aed90581c2 | -7.64644 | -42.50031 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9bf6fbc8-3e8f-3308-9bdb-1a54e2e4b30e | -7.64588 | -42.50347 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bd928279-6b50-304d-8c35-1206b98cbac7 | -7.64533 | -42.50665 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0343344e-6492-344d-a736-5d95207823a1 | -7.63958 | -42.50887 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d5aad69d-b325-30d0-8f4c-4b90dfcd473c | -7.63902 | -42.51205 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 95fd8864-9f7e-39c6-81f6-6ece8378b5c0 | -7.63384 | -42.51109 | 2024-10-07 03:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README43.md)
