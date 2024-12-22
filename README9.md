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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e4a0663-bfff-3944-a18c-7f1b22205cd1 | -3.81179 | -46.70964 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29c76bea-33d7-3bc5-945e-649eed5df10b | -2.15502 | -46.45007 | 2024-12-22 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd09f2d8-9e41-3cc7-9b42-1aa07ebdb67f | -3.25798 | -48.88956 | 2024-12-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8b0baa4-e193-3d9f-8216-fd1010f76d8a | -2.88685 | -51.80071 | 2024-12-22 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d855b688-95b1-358c-aacb-e5b47274132c | -4.00668 | -46.91958 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 763b5b9b-8462-33d0-9357-f4a0ced47205 | -2.75629 | -45.56183 | 2024-12-22 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f5645178-b2ec-35b9-8179-1a538179316d | -4.10113 | -46.81608 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 916735ef-da8b-3115-bbd9-e098c81205cf | -1.93841 | -45.63773 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c4dcfa-d9f4-3497-9e2c-9edae22dfb40 | -2.63207 | -48.03799 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4efcb59b-dbb1-3164-9395-8d157d203112 | -3.8361 | -46.68488 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a8d61d-9e5b-3e4d-9ef2-6a7dd0c5be39 | -3.17438 | -45.97956 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aae0f166-95a7-3b38-a6b7-7598a63b3702 | -1.30784 | -53.4858 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2812a60-3316-3054-977f-2397a654510d | -4.09899 | -45.30612 | 2024-12-22 04:25:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb26308b-7a91-3ad9-85be-445394e72050 | -3.79974 | -46.85093 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2737e710-c7d2-3614-ae29-f099805581fc | -2.71441 | -46.15783 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19253710-27ec-30d7-b6f5-e313ba0b5666 | -0.7912 | -48.09848 | 2024-12-22 04:25:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b7ad06c-b91b-37fc-b659-2959d3169e3b | -3.98058 | -46.91192 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97bd1cf5-e8e9-3b43-bc1c-c1eec3744a55 | -4.9111 | -41.31313 | 2024-12-22 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5db7b363-c25e-3091-90cd-89ce52ebb3ef | -2.86651 | -45.24881 | 2024-12-22 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 236f77b3-cda4-364c-bfd6-84c17877a9f9 | -3.17768 | -45.98007 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcebba72-179b-3a99-9b1c-676b04b0b264 | -3.99108 | -46.73759 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3bacccc-74d6-37b2-9b7d-8bbdc90b2bc7 | -3.0142 | -46.99919 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24457925-656f-367a-b01f-e02b4db6a8d4 | -3.94996 | -46.4152 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| baf66bb9-5ef2-3c24-91b7-da21c4b42ffa | -4.32696 | -47.77925 | 2024-12-22 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eb476f8-656f-329d-8246-77f221aa1ee5 | -3.92266 | -46.91314 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15b2f6bd-221b-3dc7-9d1f-753f36f3dc93 | -4.0403 | -46.46875 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e31530a5-21db-369b-8546-0da5a0d8fdc2 | -2.50598 | -47.26233 | 2024-12-22 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95e097f1-8e6c-3e11-8a20-0da5965fd659 | -3.92464 | -46.35816 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1673d1d0-e558-3ae1-81a9-513050f04fdd | -3.76472 | -47.20356 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaaefbe4-444a-36f9-9a63-fc780eb336df | -4.08936 | -44.49091 | 2024-12-22 04:25:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e531338-ef36-3333-83dd-c064f70eefa7 | -3.92109 | -47.01019 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 868c4157-cafd-3b65-9423-db5db9cb591f | -1.81169 | -48.45494 | 2024-12-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6a1c29d-1515-3ac9-8b56-ac188819129f | -1.36833 | -53.68203 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b989a31b-aa7a-3363-bdd6-b1743eb7fa03 | -3.16938 | -45.96824 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e06e76c1-23aa-38a4-89ac-97c30ce233e2 | -0.96253 | -46.85006 | 2024-12-22 04:25:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 651b5e8e-ab71-353c-81d7-160f1c8c4ef9 | -2.49816 | -48.06129 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 821cee5a-8bff-3bde-a174-5fa5614aaf93 | -4.92557 | -43.95845 | 2024-12-22 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2123359a-e93f-3204-a7ff-238bff0c9bee | -3.92518 | -46.35471 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 425cf489-478b-3006-8533-cfafc52945b1 | -3.91293 | -46.67203 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c70ede5-7fed-30c5-a23b-7dadfe8ab347 | -4.02598 | -46.79713 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a7c0b83-a393-3f57-b1be-2e25cff5b7dc | -3.81069 | -46.7166 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d54e08c-295c-36de-8d40-bf2fa71eb545 | -3.90607 | -46.99694 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af264345-cd3c-3cf5-9c87-7d9624abe581 | -3.91998 | -47.01724 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a4a9e71-7a5b-3d8c-9b49-cc1be00ff4d6 | -2.57151 | -49.48566 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 206e93f3-1952-35b4-ba14-7ce5234377ce | -3.98721 | -46.74058 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ecc37dd-c552-3702-a26f-b6174e66cbce | -3.9505 | -46.41175 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| edafc023-26bd-384c-b9d1-a6fdee94782f | -4.00551 | -46.5584 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be2432ec-4821-353a-b87e-f7ff8ae46673 | -2.37061 | -48.52094 | 2024-12-22 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 807cc7df-1b75-35fd-bd6e-042196868f18 | -3.94973 | -40.58823 | 2024-12-22 04:25:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 469a01c3-c179-3127-8ecf-7b4c46687091 | -1.71238 | -52.59407 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ab1ecd13-082e-36e3-ac0a-19c003a337fd | -3.98999 | -46.74458 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3852cd31-ce2c-3945-a997-bf84bbb7277a | -2.22602 | -53.81296 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6858a50d-76b2-3356-a8db-149acd1c0c06 | -3.78651 | -47.10878 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df2e8706-32d4-3967-9990-752188d5d37f | -3.0685 | -47.767 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cf8e9a55-ac01-332c-b007-2ce9cd356bb7 | -4.07973 | -46.80185 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11d816f6-03a4-3d6d-b40b-6255954a538d | -4.03182 | -47.04226 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1641e0d-7a93-3501-995c-98942f3851ef | -2.6501 | -46.11185 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e378fc68-ebb2-3eb4-aa1c-3121488be0a0 | -1.94171 | -45.63823 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b601629-785c-33e7-adec-d5bbe9f58a18 | -1.43646 | -52.63588 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbe211f9-f42b-3553-bcf8-271b818d7b73 | -3.91933 | -46.91264 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d57069f4-233c-35c4-ade8-9971946eb3d2 | -2.87143 | -45.23899 | 2024-12-22 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bf14da6-ed8a-3b50-a6e1-93df93e60f90 | -1.71383 | -45.223 | 2024-12-22 04:25:00 | NOAA-21 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f457eab2-fef4-3c7e-ab6c-a1338fb4f4bd | -2.57221 | -49.48114 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba72f9ce-55f2-3ff0-b48d-9ef489e06f6e | -4.81721 | -44.41609 | 2024-12-22 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6df8366e-285e-3f6e-9571-d81692d47bef | -4.4512 | -44.76517 | 2024-12-22 04:25:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3795816-3024-3167-ad20-b415beed9d5e | -2.58417 | -49.4784 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27ca7834-1170-3334-a0fc-792109036381 | -3.7664 | -47.19291 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2600bf-e7ff-3655-ab62-19701fde9eb6 | -3.85855 | -46.58523 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8663232-36e1-371f-9146-bd9308a298a0 | -2.8023 | -46.74523 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04137a4e-2502-3a00-99db-642328578755 | -2.65341 | -46.11236 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acc51456-7a78-35e5-a025-cf951b5dc6c6 | -2.80453 | -46.75277 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c953611c-e5b3-3da3-bed1-44327df64eac | -0.86786 | -47.09263 | 2024-12-22 04:25:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8304f470-2204-3e4f-8e34-97c7c5acf006 | -3.2112 | -42.70428 | 2024-12-22 04:25:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0144d32-5ca6-3079-a60c-753cbd21142f | -3.17269 | -45.96874 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 531cc4b1-e90e-3c5a-b51a-cc07ec83a6e3 | -4.01685 | -46.61761 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b46f69d2-fd95-3bb9-9fed-094f8e576327 | -4.0396 | -47.03624 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db73b0a7-ee20-3733-91a8-5726c3cc569f | -11.54342 | -40.4155 | 2024-12-22 04:27:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa8d8aa7-2bce-3523-a051-98adcf916fb0 | -9.64431 | -44.70455 | 2024-12-22 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c185fab3-001d-3c2f-9514-08f886a56016 | -5.49598 | -46.77268 | 2024-12-22 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7db191a-e450-3435-a491-c6582ec5842a | -4.51671 | -48.0666 | 2024-12-22 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ff6f567-bd93-3bc0-98fd-527b921024e9 | -4.77475 | -46.38288 | 2024-12-22 04:27:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae3ed456-7f9e-365b-a5c1-0c5c70bef3f1 | -6.4519 | -46.2061 | 2024-12-22 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c482364-d6d6-3b00-9729-7079266b09ca | -7.06895 | -40.56071 | 2024-12-22 04:27:00 | NOAA-21 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 52e183c2-3f06-3542-8b69-3d448f3349c1 | -4.79704 | -46.15375 | 2024-12-22 04:27:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91254bd8-3769-3052-a8d7-93fd41d569d2 | -12.33997 | -43.67582 | 2024-12-22 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7c219b07-cf3e-351f-b186-45b8e310b889 | -5.21484 | -44.90759 | 2024-12-22 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f19a284-a3bb-3a2b-80de-df37ed651079 | -12.3393 | -43.68058 | 2024-12-22 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f2893ab9-356d-30a7-afa4-c503ff480eee | -10.49796 | -40.3013 | 2024-12-22 04:27:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 81ad0256-e5ee-30c3-a1b6-691194385b85 | -5.30314 | -46.46247 | 2024-12-22 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3c6f9cd-8343-3c66-ba5e-7fbae7747a77 | -5.03197 | -44.66006 | 2024-12-22 04:27:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cfa379a-dbb2-3b50-940b-bd1790355f17 | -12.72028 | -42.75879 | 2024-12-22 04:27:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8b6bdfe-283e-37a2-841b-2ca24b0360fd | -4.73282 | -46.54246 | 2024-12-22 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 270da5c7-6fcd-30b7-9a9d-c01f75ad323d | -4.40324 | -48.78288 | 2024-12-22 04:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a873d20b-9b37-3bec-a642-53a36d872cdd | -12.44638 | -41.44383 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ea6357be-fa4e-372d-9f51-2a45e839132a | -6.45244 | -46.20264 | 2024-12-22 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f13302fa-72a2-39d5-b635-03287abc27a4 | -12.43823 | -41.43785 | 2024-12-22 04:27:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ec03bdcd-a850-3e27-814e-3ee313229d55 | -5.31966 | -46.46505 | 2024-12-22 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b89cca0-097c-3dec-90e8-61eab8fe3abd | -12.46025 | -38.47966 | 2024-12-22 04:27:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4f5d3f24-0a97-35d0-b027-ea33cb5f5a0a | -5.31912 | -46.46849 | 2024-12-22 04:27:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25ac70a6-7d45-322f-8362-23c573a7a4fa | -5.23497 | -44.91067 | 2024-12-22 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
