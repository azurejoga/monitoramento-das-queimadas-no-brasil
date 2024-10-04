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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca578924-5f74-3f89-abca-e9aa4bb19833 | -16.92864 | -55.84354 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| fb4e1871-d7b6-304a-a088-22b8c8713263 | -16.92519 | -55.83017 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ce45d102-f779-3109-8515-ce01c01a3ff1 | -16.92468 | -55.83232 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 0072b209-65f2-3467-bd71-bb0ed9f9090c | -16.9241 | -55.83506 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b896a969-facb-3798-9717-3977a73d9a3f | -16.92362 | -55.83725 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 8842c1ce-30d2-3e5c-959b-50a25286bee3 | -16.923 | -55.83997 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 9776bdd2-ea23-3784-908b-4ca0e16fec00 | -16.92256 | -55.84215 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a8856b5b-c92c-3e1b-a866-2560ee0a0edb | -16.92191 | -55.84486 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bdc9eeb9-f669-34aa-aebc-71bc8640ec63 | -16.92021 | -55.82394 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f6f9ff24-5542-3f17-b541-463a5269f1c1 | -16.91967 | -55.82604 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 536d3b7a-1bcb-3915-bfb0-4ed56fb3e27a | -16.91912 | -55.82877 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d49bf14b-c934-3acc-9d53-e5e5c77c1dd4 | -16.91861 | -55.83092 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 64a7968d-9487-3996-82c8-697486d35f5a | -16.91802 | -55.83369 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 12ddb37c-f4bb-3c51-8a46-08261f37d4e1 | -16.91475 | -55.84825 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ba3094e0-5b4f-37e9-b799-4e74275cb80d | -16.91358 | -55.82471 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9b012127-0f2f-345a-8dfd-c553cf090f30 | -16.91252 | -55.82959 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 01fa2fde-68f1-3a33-91d6-e95292806901 | -16.91147 | -55.86292 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c0dd4b86-1c76-34a4-9fb5-9a5da0b8d07a | -16.91119 | -55.86512 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7397f7e3-28d0-3e35-a3f0-4b89b97fb949 | -16.91037 | -55.86781 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3e04b819-f68f-3833-bac5-759b101902cb | -16.90511 | -55.86368 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a006eb3c-101a-313e-a6a3-7d28828fde7c | -16.71251 | -55.46125 | 2024-10-04 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 65573648-ca51-3ede-a334-65c84db8dcdc | -16.69114 | -55.46296 | 2024-10-04 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1af629e1-e05b-3ab1-b60f-5208d9966a9c | -16.67038 | -55.91568 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5de217be-56c9-3df2-b570-993ffd98f978 | -16.66425 | -55.91426 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a15cec24-ef72-371b-b3e9-3a9d4fc97768 | -16.65813 | -55.9128 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f1a31af4-cb9b-3613-89f6-86afa060d983 | -16.65704 | -55.91778 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8792ced2-c606-3d03-9b1a-d3f4b937146e | -16.62638 | -55.91068 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9b2f8e5a-c4ec-3d63-8b0d-985184f53037 | -16.62528 | -55.91565 | 2024-10-04 04:12:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 922d50b8-b0a7-3741-bed8-4c8c65dc06a7 | -21.40581 | -57.22991 | 2024-10-04 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 588d8fee-e8c1-3125-b4c5-8c4d48cbc8ab | -21.40495 | -57.23179 | 2024-10-04 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eb6998a8-e0b2-3601-8f0d-a392916d5c97 | -21.40486 | -57.23388 | 2024-10-04 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ae9c099-99db-3b75-bd97-430989eeeca5 | -21.39986 | -57.22803 | 2024-10-04 04:12:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d32c607-4c61-3b1a-ba7e-f18b66739b11 | -16.61706 | -57.19775 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| ad90fc89-3dc4-3fd6-a688-1f3c46038dc2 | -16.61523 | -57.19266 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| a9b03a16-2029-313d-b032-e56f79fee181 | -16.61419 | -57.16714 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c6e77604-0a3c-3100-8ea4-80497de3d80b | -16.61384 | -57.19867 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| d96b2256-c1f8-3352-8a5b-2f07e98e6123 | -16.61317 | -57.18415 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| efb37e41-7e8f-3b1c-9190-1281cf175d6d | -16.6128 | -57.17312 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a9e206ae-8135-3829-ae0b-9b3c940b6c21 | -16.61182 | -57.19016 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 44a305e6-d244-35ea-bac5-fdc7734a449a | -16.61142 | -57.1791 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a952eb13-bf94-322a-a190-40bba6e14bee | -16.61047 | -57.19618 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 7ce45525-1822-3d4c-bd6c-5ee35599ab2e | -16.61003 | -57.1851 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c5e94fc9-7ee0-329e-b8ca-4c06b1c52ffd | -16.60928 | -57.17055 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bdde70ac-1f61-336d-bc88-71c4b5dfb82f | -16.60911 | -57.20221 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 9128cc51-e180-3ce9-8958-eebc68d7853e | -16.60864 | -57.19111 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| dd8d7bce-c011-3c64-816a-2b12ea1d11cf | -16.60793 | -57.17655 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4d5a4f96-d91e-3a85-b207-9c10178f18fb | -16.60775 | -57.20826 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 15300edc-6432-3183-be7d-29e4a61abb74 | -16.60725 | -57.19711 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| f3b218eb-82ff-3b01-b9ff-14aee6cf4b2d | -16.60658 | -57.18255 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 43bdbcf5-1fb4-3ebc-af1a-42de44100a53 | -16.60586 | -57.20311 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 4040dc92-a32a-3068-801b-ea5ceb2b82ee | -16.60523 | -57.18856 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 1b51ce7b-008c-303f-a612-682baf6db90e | -16.60446 | -57.20914 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 02585062-dc1b-3301-9441-8f9b573dd397 | -16.60387 | -57.1946 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| c75bb900-1aee-3ea4-8a5e-0eda86451b58 | -16.60252 | -57.20062 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 0ede01f5-1641-376b-abb3-7378cbadf416 | -16.60135 | -57.17497 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6c9033ee-7cc6-38e8-87ac-515878ff9d59 | -16.60116 | -57.20666 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8627e4fe-12f1-3bd3-9e44-00a15f82daaa | -16.6 | -57.18097 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| f8bfacee-45c0-39ad-92ef-c2cda65ed0be | -16.5998 | -57.21271 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a21afd54-9b1a-3186-b474-4f8d54f8d735 | -16.59864 | -57.187 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 524407cc-228c-323e-a1b4-144ca4f10339 | -16.59728 | -57.19301 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 7aef3b0e-13bd-333b-bd47-00669fe64da2 | -16.59612 | -57.1674 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 44817571-ceba-3292-be96-2f8234eddb03 | -16.59592 | -57.19904 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| a7de9b45-479c-3837-b96b-04f1a00331af | -16.59467 | -57.25136 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9b7127a9-4c50-327c-98f8-d5316dff6c7b | -16.59205 | -57.18541 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 445d021f-b2df-390a-84a7-e13031013eef | -16.59069 | -57.19144 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ce2e9c61-58c2-3b3f-a777-4c7956dfb691 | -16.59024 | -57.25515 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cfbfeebc-2c72-335f-b05b-c1ac1fcebdcb | -16.58362 | -57.25355 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 07a51954-3cc3-3e8d-8390-84b885c7f123 | -16.577 | -57.25197 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8c30fcf0-9422-33c0-97b5-ae4c305a7ca5 | -16.57562 | -57.25808 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 233bb107-4d78-3a33-ae10-e7eb43521a78 | -16.56734 | -57.29467 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c41ef144-57e3-35ec-8ba7-1e0472f1fb31 | -16.56515 | -57.24271 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ee3ebe6f-6e90-3219-b634-583869097cc8 | -16.56377 | -57.24879 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1030dfce-015d-3348-98b3-22409a98cb01 | -16.56209 | -57.28698 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 93958a6d-07ae-3321-a98e-5b620addca45 | -16.5607 | -57.29309 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| eb51439d-86d6-3d09-81f7-13bd0b73bc7c | -16.55546 | -57.28537 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0d864a08-95ef-3c58-a938-47731f79ad9e | -16.45568 | -57.30917 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 81fc5f8c-1271-37a4-8179-525dab003016 | -16.41598 | -57.39111 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| ef489394-f049-3e77-9469-33f6d2dd262b | -16.41455 | -57.39736 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 6470bcad-5b07-30df-b1f2-fe88090d5548 | -16.41072 | -57.38325 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 26f852eb-681b-3cf9-8c45-6c5d233f286f | -16.4093 | -57.38946 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 760d59cc-c433-3c4a-9283-e3431f79e2cb | -16.40788 | -57.39571 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| b60b4ea6-59f7-3fbf-93c6-5f3595295d08 | -16.40263 | -57.38779 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 98a4a139-f196-3ac7-8c51-0f1bb6199112 | -16.4012 | -57.39406 | 2024-10-04 04:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 56ed53bc-6515-32da-8001-a1355e675f07 | -17.1234 | -56.75093 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ae2c55fe-90a3-31d4-991a-0109fef5a762 | -17.11704 | -56.74937 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fcf26865-63e8-38cc-9f18-e7682c98ee30 | -17.11471 | -56.78965 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 9211124d-8892-3535-91f6-dfbb9459c163 | -17.11207 | -56.77148 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1f910bff-a474-3f27-8a8e-aeaa7fc35a54 | -17.11082 | -56.77702 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 5aa3502d-76ed-3326-8945-9f77f1491db0 | -17.10958 | -56.78256 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| f6f79cee-b320-3a0d-b6a1-ed23224e67cd | -17.10833 | -56.78811 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 92bcd975-d4da-3e6a-a840-e95b4d6fcccb | -17.10709 | -56.79362 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a7276186-472c-35b4-b176-23882fce88e2 | -17.1032 | -56.78101 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9413e483-51ed-3a94-855c-7ecd2b459c5e | -17.10194 | -56.78657 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 30a78049-d5dc-333f-a094-e0477cfff5fb | -17.1007 | -56.79209 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| af7ee042-47fd-3b2c-be9f-580a0648d256 | -17.09556 | -56.78502 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6417bdbf-c31b-3801-b770-cac860c0981d | -17.09431 | -56.79057 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 305bebd7-9527-3a96-bb43-eddf3d2d89c1 | -17.09042 | -56.77797 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 80e27270-aa86-3d98-880e-da79bd5ffbc0 | -17.08917 | -56.7835 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3e3179e9-5bf1-3c73-ac75-9c9cafdcd445 | -17.07639 | -56.78048 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b949f190-c4ef-38c2-a841-136e957658e1 | -17.07261 | -56.79715 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |


[Clique aqui para ver as próximas entradas](README91.md)
