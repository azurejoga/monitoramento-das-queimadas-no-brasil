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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e81c85e-1dd3-3af3-94ce-d419f4536d00 | -16.85674 | -56.7134 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c8151d14-663f-3b08-a907-0a895057fe07 | -16.85636 | -56.71681 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bad14639-114d-36f0-96ba-709cc731ba87 | -16.85484 | -56.73044 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ebaf86ac-d7dc-35df-8e7d-423477ee2759 | -16.85446 | -56.73383 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 447aca17-a458-3eac-a286-385f32edfeac | -16.85408 | -56.73722 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2561e481-f779-3b9c-a1ca-0333e4577f3f | -17.01659 | -56.71834 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| f6a2a1bb-be73-3474-b8e6-29a511163232 | -17.0162 | -56.72177 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 203276e2-366a-3540-ae86-d292ea2d532f | -17.01596 | -56.69989 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4eecd1c3-b709-35c5-8477-49194795ee16 | -17.01581 | -56.7252 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8298d771-d4e8-3a70-80e4-3425a4c722fb | -17.0156 | -56.70333 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cf909bdd-da69-31d7-85b6-4070025f5357 | -17.01548 | -56.82151 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 37f98b5c-9bb9-3b5c-99c9-c433a97a8cda | -17.01541 | -56.72861 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 19696ef5-03a4-3cd6-8f86-b07e386c89d2 | -17.01523 | -56.70675 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 93b3327c-a318-3d79-ad3b-854d6e336659 | -17.01502 | -56.73203 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bbdc6a27-6398-384b-87ae-93e17c9160ba | -17.01486 | -56.71017 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0c07c0ce-51fe-357a-92ef-1c001f6e3e31 | -17.01449 | -56.7136 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f4ccaf45-481e-3cce-b141-e4665913c221 | -17.01413 | -56.71703 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5c47f0ea-ae64-3ae0-91a8-f1bc64aeb137 | -17.01376 | -56.82047 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 10732dd5-940a-3614-84c2-b4d973f7636a | -17.01376 | -56.72047 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6f543d2a-0621-37d6-b8fe-1cdbf14e6b92 | -17.01339 | -56.7239 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fac70bde-e291-3f27-922a-372000e25178 | -17.01321 | -56.70057 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e6dbeebd-246c-3019-b5d1-06e614707ead | -17.01303 | -56.72733 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e29a162d-ce4d-325a-a122-06006d7ba833 | -17.01282 | -56.70399 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 286cb0e0-b54a-3cd1-8de7-76b4e4f3dd1f | -17.01266 | -56.73075 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0a67ae16-b6a8-3737-8856-6e1a437880ea | -17.01243 | -56.70742 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| bf9c1b36-cb75-3df2-86bd-c3ed8e2248f8 | -17.01204 | -56.71083 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f6f2372a-e126-3523-b317-762714de03ab | -17.01165 | -56.71426 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ef416d31-ddb3-359d-a152-2048c25cecf2 | -17.01126 | -56.7177 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a1d4050a-f010-3591-b129-28269cbc012a | -17.01086 | -56.72113 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| acfd8eb6-f11e-391d-8a5a-caeb542578fe | -17.01062 | -56.69923 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fcdc9c1d-6d37-335d-b857-390b15d22ac9 | -17.01047 | -56.72455 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d09bee1b-32cb-392f-bd31-e06b736db2ec | -17.01025 | -56.70266 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4daf2133-e9d9-328d-a153-cd0e7e94cb93 | -17.01017 | -56.82086 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f2a6a216-cba6-326b-b293-8135d6ab5ef2 | -17.01008 | -56.72797 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 71b29384-9879-39aa-af57-a5e552aaf76f | -17.00989 | -56.70609 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5ea534eb-8b67-3492-b132-b269c95786ea | -17.00969 | -56.73138 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 924cad57-71c2-3aab-ad1c-65059261473f | -17.00952 | -56.70952 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0c533266-cc33-315e-8e03-35d155955f6d | -17.00916 | -56.71294 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 59a67c1c-26ea-38c9-b11b-7fe778a8ffdc | -17.00845 | -56.81981 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ec88d26d-1d7e-30bd-9f31-b2cf3ad6b744 | -17.00842 | -56.7198 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e7a2563f-a53f-313b-a93d-ef7650c3fe93 | -17.00826 | -56.69649 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e4f3cb4d-6402-3553-8803-602c8075d1f3 | -17.00805 | -56.72324 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c3bbaacf-de3a-3a8e-a295-8aa659edcca7 | -17.00787 | -56.69992 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 82876602-b938-38ef-bb82-eb3116a5ae2e | -17.00769 | -56.72667 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e6378646-c15f-3c64-88bb-5fecaaf5ba9f | -17.00748 | -56.70335 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 91d9556e-5469-3ffb-8fc1-a307cea663d3 | -17.00732 | -56.73009 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| df41fff8-e7ed-3adf-b37e-3b17c288c80a | -17.00709 | -56.70677 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3197fdf7-a7a9-34f3-87ac-4aca5bad5e93 | -17.00696 | -56.73351 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| cb1e9e63-9ae3-3969-a3ae-d03985c53c9e | -17.0067 | -56.7102 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a7a77236-4d6c-3616-a2ec-dd562da7a220 | -17.00631 | -56.71363 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f8a3542a-0dea-3a78-abfd-5a22c8a32d2b | -17.00553 | -56.72047 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ea56db9b-b376-3f77-8bd5-95e870c508de | -17.00526 | -56.81685 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| fcdf2453-2c6a-3118-b4a9-c611b13d0353 | -17.00514 | -56.7239 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 98e1641d-bb47-394f-9570-a001a51075e1 | -17.00488 | -56.82022 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b581b9f6-5e46-3dba-9b12-509616c20b69 | -17.00475 | -56.72732 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ffeaba3f-6df6-31ed-a98f-355a7a5cf196 | -17.00436 | -56.73074 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| e0f4303d-a286-3285-aca7-b23cb2615fa3 | -17.00397 | -56.73414 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 7292ef62-acd4-36c7-b2e4-b55e9d645661 | -17.00279 | -56.82252 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 481d8d10-a0f6-3038-8a88-2128c52f5913 | -16.99996 | -56.81622 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d86ed981-0d9c-3dd0-9cd4-cb434e60a258 | -16.99919 | -56.82295 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a6c36eca-dad5-3b18-8446-d7d719c93fbd | -16.99902 | -56.73008 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bd257e45-46f9-3a65-bcb1-cb1b75e90670 | -16.99864 | -56.73348 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 8ac28a91-2b1f-3bfb-8c27-35dce2f87357 | -16.99821 | -56.81513 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7b8647b4-f78d-3286-8f0e-030ade4688a4 | -16.99757 | -56.69519 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c6f46618-4a1d-3400-b25e-67eabbeaca66 | -16.99718 | -56.69861 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 496665a2-c8ed-3e0d-9b2f-5c1905302a01 | -16.99641 | -56.70546 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 713250ee-bfa5-30c2-b9de-3eda7dfd7536 | -16.99602 | -56.70889 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b4ba9f56-3f66-3a00-8845-19a2772a46d8 | -16.99504 | -56.81221 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 856af475-f3e7-3cb6-8f83-8f50bd97d6f3 | -16.99427 | -56.81893 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ce3bad73-0364-3456-bec0-82daed00af06 | -16.99331 | -56.73283 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0ca4b1a0-3524-3ad8-80d4-9e8067441e91 | -16.99223 | -56.6945 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4424a130-ea6b-330b-988c-c37b224cd121 | -16.99107 | -56.7048 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0bfb5230-1aba-3f67-b4fd-a31a609bba6a | -16.99068 | -56.70823 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3a927110-cf19-37da-a46c-ccc690f89ad8 | -16.99012 | -56.80819 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c23bbc53-02a6-3bc4-8c85-66d1c824533b | -16.98759 | -56.73558 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a1d77db7-e523-3e9f-9ed8-3869e5d84ff3 | -16.98721 | -56.73898 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 97fa134f-74d9-3239-a1d0-f3a91208dae6 | -16.98682 | -56.74238 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6f59d350-f137-3c8a-889f-fa04d81e323f | -16.98567 | -56.75261 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 80d946db-edaf-3a9f-912b-cbd0a69fe99c | -16.98558 | -56.8008 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 18ff752e-caf1-3644-b70a-05e5542a5fbb | -16.98528 | -56.75602 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0ed0c890-20d3-3dd7-a989-8f94d07f65a3 | -16.98489 | -56.75942 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 63b46585-abe5-3537-a838-473984e784a9 | -16.98451 | -56.76283 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3af26416-c585-38a4-a830-20085af96f03 | -16.98444 | -56.8109 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f8462fc5-a11d-3381-9ee3-e5ea373ae210 | -17.13186 | -57.42039 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cdca7b81-0752-3390-ae23-c1fa827b6b3a | -17.1315 | -57.42349 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e16589cc-f25e-377b-a69d-266077194086 | -17.12676 | -57.41975 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 324c20af-4039-317d-99b8-997ffefa94ec | -17.1264 | -57.42286 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3947468b-6bee-3622-ac3b-42926381b8ef | -17.12416 | -57.3975 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 58dfedba-e299-3210-8550-e7c0ed33561c | -17.12165 | -57.41911 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6f4c9767-77e5-3c83-8cc1-8b986bb5c532 | -17.12156 | -57.37512 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 4230b8a8-5d07-32b1-b250-f38ffeaef07f | -17.11941 | -57.39375 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 04796e4c-4393-36b4-a7b9-1e8b6fa26516 | -17.11905 | -57.39685 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b59628b1-aa11-3e6b-9d1c-4a053d51c415 | -17.11869 | -57.39995 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8a0b2491-679e-33c3-9654-79c45147293c | -17.11833 | -57.40305 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 3dcbf63e-200c-3f39-ba6c-ad24c1ca9efa | -17.11762 | -57.40921 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| cb2605ed-60d1-394a-a653-c4b7186ce9a3 | -17.11691 | -57.4154 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 359ed4f2-ff92-3c3a-a7f6-13a97cab6e6e | -17.11655 | -57.41848 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 99975006-6914-3c30-b5a2-3297c4275d34 | -17.11619 | -57.42158 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5e055ad9-a145-3d90-aaca-3c8df687473e | -17.11608 | -57.3776 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| fb219452-5578-31c3-acba-6d43ae48072d | -17.11572 | -57.38068 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |


[Clique aqui para ver as próximas entradas](README145.md)
