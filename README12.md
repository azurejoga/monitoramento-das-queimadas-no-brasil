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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0215f73-ed00-345b-88fe-e24733f5222c | -17.5434 | -39.9022 | 2025-05-26 14:00:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| e3c3799d-0aa0-35c0-8afd-d0b8c5362144 | -12.0703 | -47.3408 | 2025-05-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 44407922-a881-3d11-8909-845cfac4226b | -12.089 | -47.3606 | 2025-05-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| bd132a72-4a7b-385c-8aa2-c9b1887a0330 | -12.4086 | -49.9978 | 2025-05-26 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 80eabd6a-3489-326e-8880-be696e745582 | -11.5579 | -44.8905 | 2025-05-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7dd8b014-018c-3cc9-9043-2aa7fd21fee8 | -6.1606 | -48.0507 | 2025-05-26 14:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 334.5 |
| 20e659d5-4d48-3c88-bfd0-b3f328e3c7cb | -14.0328 | -55.13 | 2025-05-26 14:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 7df68d72-3de1-3622-8721-12face14e240 | -12.3529 | -49.8967 | 2025-05-26 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a1db8f0f-c4ed-3ce9-b5ca-1515069ac9f1 | -12.3898 | -49.9786 | 2025-05-26 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 9611a318-fe6d-3754-9c20-7033f559e204 | -12.4089 | -49.9762 | 2025-05-26 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 201.3 |
| e00aed06-4513-3a1e-abd4-0c38200dea21 | -14.0325 | -55.1506 | 2025-05-26 14:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 69cdec81-6204-34b1-a715-d0701df7765e | -8.0312 | -43.1964 | 2025-05-26 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 872.3 |
| aff68663-6330-34e5-aaeb-fd66cf9549fe | -12.0699 | -47.3632 | 2025-05-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| f2fe2ba0-1f9d-3770-a7ea-9ce5febe26d7 | -8.0123 | -43.1984 | 2025-05-26 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 283.5 |
| 54185f71-febe-3b96-8c5a-56572427f1f7 | -11.5583 | -44.8673 | 2025-05-26 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0e5c9f6c-10cc-3612-862a-bf42b3c302aa | -12.0894 | -47.3382 | 2025-05-26 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 3174cd1c-c3b3-3bc7-b857-63c126a6f060 | -12.3717 | -49.916 | 2025-05-26 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 029b697a-1ed0-3ed7-b80f-6d1850cc7eca | -8.0126 | -43.1749 | 2025-05-26 14:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 2ce6da5c-ca0e-33f1-a82e-3bf45f48dac7 | -7.595 | -43.3828 | 2025-05-26 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 84ac29b6-54a4-36eb-87fd-b7c111ab67bc | -12.3522 | -49.94 | 2025-05-26 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 4c92267a-d4b4-3bea-9db2-d9233cd9f738 | -12.3898 | -49.9786 | 2025-05-26 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 0a311e1d-209a-391f-b5b7-d9c559d34fba | -7.595 | -43.3828 | 2025-05-26 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a3073cb1-f02a-3318-812d-4bf8be6dacc9 | -10.5164 | -46.8264 | 2025-05-26 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| eaa1046d-ee27-3c53-8ff9-80b872f914cd | -11.5579 | -44.8905 | 2025-05-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| b923a591-6deb-3e0e-8081-1d4895aad16e | -12.0703 | -47.3408 | 2025-05-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 186.8 |
| ac3f13dc-05dd-3021-b1ee-7aa56f87c36d | -8.0123 | -43.1984 | 2025-05-26 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 235.6 |
| a8651aae-b16f-3bfa-a62e-ec002cb3520c | -14.0328 | -55.13 | 2025-05-26 14:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| a8ef4c47-1e76-3187-836b-39bd81b0a14a | -11.5771 | -44.8877 | 2025-05-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a37aeabd-1d38-3863-8500-ffcbcbf255ab | -12.4086 | -49.9978 | 2025-05-26 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 6fa43967-e73d-3fa8-8829-61f0dd8fea42 | -12.4089 | -49.9762 | 2025-05-26 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 32b7c730-7ed4-3444-b0eb-082cfa9e8eaf | -12.089 | -47.3606 | 2025-05-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4ce9d263-4447-3384-95b9-e2b253ac6234 | -12.3526 | -49.9184 | 2025-05-26 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 474.5 |
| f70e945a-b902-3760-a1d2-bba755947f96 | -8.0315 | -43.1728 | 2025-05-26 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 167.9 |
| 2fe0f5d6-2079-3981-a266-e5c816234291 | -6.1606 | -48.0507 | 2025-05-26 14:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 399.5 |
| 511359ba-064f-3814-b2a0-6fda106d3821 | -12.3717 | -49.916 | 2025-05-26 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 7c423f5f-a074-3291-81d5-2b3d1e6c8c59 | -12.3522 | -49.94 | 2025-05-26 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 7ac6c45b-6f58-3369-9894-dcfb2d14bdd2 | -8.0126 | -43.1749 | 2025-05-26 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 8f32c0d6-48a5-39da-99e8-3dc97d6816d0 | -11.5583 | -44.8673 | 2025-05-26 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 2fbd8198-373b-383b-82b4-e82ba6e4faa7 | -7.5764 | -43.3613 | 2025-05-26 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7585d982-1ade-3a2e-90cd-3d22cc1a3ce3 | -19.8052 | -53.8338 | 2025-05-26 14:10:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 6c87a5c1-be04-3465-9207-bad05d056bbd | -8.0312 | -43.1964 | 2025-05-26 14:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 444.4 |
| d479ec16-ae23-3007-bcf1-54cfb726eb7f | -12.0894 | -47.3382 | 2025-05-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| fa1a078c-84d0-3278-9834-4524c09d8285 | -12.0699 | -47.3632 | 2025-05-26 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 174.0 |
| bda4e213-f033-3d8c-8d75-b510d7a2ce96 | -12.3529 | -49.8967 | 2025-05-26 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4de3059c-9f77-3b61-9777-54c31fb23482 | -12.4086 | -49.9978 | 2025-05-26 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 3be2ddf5-37b5-3e4f-aacf-5841fc28c088 | -13.6871 | -45.2487 | 2025-05-26 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 4eb19340-86fc-36ef-9b5a-056b75ada6d4 | -8.0315 | -43.1728 | 2025-05-26 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 186.3 |
| 40d7b286-0726-3e19-8ad9-3e3627019503 | -7.5198 | -43.367 | 2025-05-26 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d3ae7961-db96-32a5-a75f-15981e6d56a1 | -12.0699 | -47.3632 | 2025-05-26 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 44238adf-2557-3893-88ef-590136cc4b7a | -7.5764 | -43.3613 | 2025-05-26 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a62f2237-da87-330b-85ac-2674ca149c2c | -8.0123 | -43.1984 | 2025-05-26 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 298.3 |
| c267ff98-8138-31cb-8792-419e02457a57 | -11.5583 | -44.8673 | 2025-05-26 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| c9d278db-86ef-3cff-be91-bbbcdda8ee8b | -12.0703 | -47.3408 | 2025-05-26 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 199.7 |
| cd145768-df33-367b-b8dc-7307e0b9d762 | -8.0312 | -43.1964 | 2025-05-26 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 555.3 |
| 1a9db694-c1e8-354b-9649-20d679e33a14 | -12.3526 | -49.9184 | 2025-05-26 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 392.6 |
| cb49dfe9-19b8-3289-9a90-9e6f5166d68e | -12.3717 | -49.916 | 2025-05-26 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 376c4c5c-8e28-39b8-a768-cb015a25c272 | -11.5771 | -44.8877 | 2025-05-26 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| fb8ea690-b4a5-3fd9-b231-3640523fa093 | -7.5762 | -43.3847 | 2025-05-26 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3f133d86-d33a-30e8-83ae-495af7e5d1ae | -6.1606 | -48.0507 | 2025-05-26 14:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 448.0 |
| bb78c12f-4bab-3a4a-9262-a8f50e81393b | -12.3529 | -49.8967 | 2025-05-26 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3c81f9b7-5654-3ca8-858f-75370a648383 | -11.5579 | -44.8905 | 2025-05-26 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0f82faa4-5fe6-375c-8908-a2e2c7f01d02 | -19.8052 | -53.8338 | 2025-05-26 14:20:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b66db6a0-58b0-3849-8d02-056aece69bf9 | -7.595 | -43.3828 | 2025-05-26 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e3078948-585c-3791-b382-75e63d2fbac7 | -12.3898 | -49.9786 | 2025-05-26 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a0636dde-34e6-3a21-987b-e57af8fa7cc9 | -12.3522 | -49.94 | 2025-05-26 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| e22831f2-4a49-3312-b6e9-e8ded67d15e1 | -12.0894 | -47.3382 | 2025-05-26 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 8ba369ee-162f-3654-af23-4c6a7c294ca0 | -8.0126 | -43.1749 | 2025-05-26 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| a1e7631d-f5ae-3032-a89c-b618ba066e5c | -8.0696 | -43.1452 | 2025-05-26 14:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 4420340f-4053-3869-bade-e559f0af90a3 | -12.4089 | -49.9762 | 2025-05-26 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 625cb8c0-4bc9-3ff0-875f-07eed14e5c2c | -12.089 | -47.3606 | 2025-05-26 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 76dc961d-a268-3ec5-b55d-89e9bf51f88c | -10.5164 | -46.8264 | 2025-05-26 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4816db5f-2558-3165-83d3-c78a37cc2116 | -7.5764 | -43.3613 | 2025-05-26 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| dabc1a17-ff83-34a8-9bd4-0a67b01f719f | -11.5583 | -44.8673 | 2025-05-26 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d1e68ac8-a476-3128-bf72-43aa6e4ebe29 | -8.0507 | -43.1472 | 2025-05-26 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 9f3b1a44-2251-3b8b-a9e1-aed02175a640 | -12.0703 | -47.3408 | 2025-05-26 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| aadc8aae-3b71-3287-84cf-0a7a60eb6445 | -12.3898 | -49.9786 | 2025-05-26 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 53dea450-b93f-32dc-a9aa-42de2c0567e0 | -6.1606 | -48.0507 | 2025-05-26 14:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 398.8 |
| 862a16bc-4469-3f51-a8ee-d648f9812d0c | -19.8052 | -53.8338 | 2025-05-26 14:30:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 687e3643-dbd1-3d17-8ecf-197a155195ee | -8.0315 | -43.1728 | 2025-05-26 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 181.4 |
| 64a386a3-db51-3268-8831-8b2558da7b7e | -7.5762 | -43.3847 | 2025-05-26 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1dd1cc67-b3ea-309d-a08e-bd57b73a61bb | -8.0312 | -43.1964 | 2025-05-26 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 413.1 |
| 10c222a2-1f8b-3cde-93a0-4261066d9f6c | -11.5771 | -44.8877 | 2025-05-26 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c7f90743-cf23-3d5d-900f-f913836ef6b8 | -12.3526 | -49.9184 | 2025-05-26 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 430.8 |
| 3c6a90c4-61e0-3fca-983a-7db94e82ae02 | -11.5579 | -44.8905 | 2025-05-26 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 76850c21-a0d2-3dc8-9e3a-cbf932976f14 | -12.0699 | -47.3632 | 2025-05-26 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 1743f97c-65ce-3c88-99a7-b4234043cefb | -8.0126 | -43.1749 | 2025-05-26 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 462758f3-869d-3c5a-b66a-cd8727bf19db | -12.3529 | -49.8967 | 2025-05-26 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e9e5b1f7-c2a5-3e0e-b179-ecccf02554d4 | -7.595 | -43.3828 | 2025-05-26 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 113.2 |
| e12eeb19-50c2-3de1-a8a7-8f3597dd54bb | -12.0894 | -47.3382 | 2025-05-26 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 81f3d01c-42e4-3724-99b9-205a71186240 | -12.089 | -47.3606 | 2025-05-26 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 3f03bf6c-24c9-3cb8-98a7-770b0e177800 | -12.3522 | -49.94 | 2025-05-26 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 59c6fad5-701e-3a61-9472-c06c350c8ee7 | -8.0123 | -43.1984 | 2025-05-26 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 264.0 |
| fa7d44f7-ca35-3318-b644-09ab2cd88b50 | -12.4089 | -49.9762 | 2025-05-26 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| ae08a235-ddd0-3022-8d52-36b5537adb7d | -12.3717 | -49.916 | 2025-05-26 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 6f4b7b02-7a4b-38e0-93fd-56e2841b94f8 | -8.0504 | -43.1708 | 2025-05-26 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 53e7377f-4487-3071-8f9c-3dc2b28452fb | -11.5771 | -44.8877 | 2025-05-26 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| d8e9d9a3-c31a-3e22-b040-6e6389fea71a | -12.3713 | -49.9377 | 2025-05-26 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0e6b54eb-5bff-361c-874a-f0079aacc506 | -11.5583 | -44.8673 | 2025-05-26 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| fe89f80f-246b-3805-bb59-dccc275c4e5d | -12.3522 | -49.94 | 2025-05-26 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 881e0f4b-87f5-3b20-8f57-f828b563c036 | -12.0703 | -47.3408 | 2025-05-26 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |


[Clique aqui para ver as próximas entradas](README13.md)
