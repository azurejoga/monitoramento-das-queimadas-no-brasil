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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ec249b7-e453-3ecd-8022-3773c8f0b91a | -11.9329 | -58.7588 | 2025-06-19 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e317ef05-41e8-37cf-952a-9d2d093227c5 | -11.9707 | -58.756 | 2025-06-19 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 218.3 |
| b5a60a91-5f1d-3edc-9a76-3804257c2e49 | -11.952 | -58.7376 | 2025-06-19 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 266.9 |
| 825b9b49-ced5-388b-b0d4-16b4fcdc0f91 | -7.2405 | -43.0899 | 2025-06-19 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 200.5 |
| 78f9b27f-49cc-3305-94a3-cbd0dd8d5094 | -8.1264 | -43.139 | 2025-06-19 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 3938aac5-3e45-3850-8707-071f97d9836f | -11.9709 | -58.7362 | 2025-06-19 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 39887bf1-c182-3fa8-bb02-04219db46468 | -10.0972 | -52.7376 | 2025-06-19 00:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 1213d821-f1eb-3473-a2d9-3b05f017ddd9 | -7.2408 | -43.0664 | 2025-06-19 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 435d0241-41df-397a-84c9-7c43414f195c | -8.1267 | -43.1154 | 2025-06-19 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 474f38fe-4edc-319c-9722-2a9c6aff44bb | -14.4467 | -48.9063 | 2025-06-19 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 121.3 |
| dc882d9c-ddf6-3243-97a1-b73857e8adfa | -6.2473 | -44.6601 | 2025-06-19 00:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 79786cd9-2543-3b39-ab79-b647ae9efce4 | -16.3047 | -58.2676 | 2025-06-19 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.2 |
| 4092e629-5e72-350c-963e-4f0223658e94 | -11.9518 | -58.7574 | 2025-06-19 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 321.1 |
| 4df6aa85-6db9-3614-9c7a-1b8bd4021b3b | -14.4471 | -48.8841 | 2025-06-19 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| ec1d359e-01ce-3d2c-bbed-b2a91944a4c8 | -9.4994 | -56.0788 | 2025-06-19 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 36811cd5-b183-349c-b155-c8d83589beec | -11.5366 | -56.9847 | 2025-06-19 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| eeeffbca-baf8-3879-8fef-d79d1faadd70 | -4.7686 | -47.5686 | 2025-06-19 00:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0bd24c1e-b276-30cb-aaac-47bef4ac4bd7 | -16.305 | -58.2474 | 2025-06-19 00:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.8 |
| 29a07b0e-34c9-34b0-8615-5e1f738c55e2 | -13.9924 | -58.1127 | 2025-06-19 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 983cec1f-b3b5-3a26-adc7-c197c350394b | -13.973 | -58.1344 | 2025-06-19 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 25169868-b879-3340-bf86-da4d65733c32 | -10.6486 | -49.47 | 2025-06-19 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ddea2e33-751a-3689-ab42-3d672a54c790 | -11.1379 | -53.9429 | 2025-06-19 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d2453835-ce88-3a24-a94e-b24592fb8358 | -10.6489 | -49.4483 | 2025-06-19 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 9264da72-a83e-3c8f-abd7-b52b199c37c1 | -13.9733 | -58.1144 | 2025-06-19 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 60f885e2-9aa1-3320-a465-2a455a456e52 | -21.3387 | -48.618 | 2025-06-19 00:00:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.7 |
| 8086c80b-0a85-32d6-b1fc-a0123a81f164 | -8.13075 | -43.12996 | 2025-06-19 00:01:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 162.3 |
| 77966b43-9693-3194-8ee2-4d8bb7d0ff71 | -7.24726 | -43.10249 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| dbcac304-b53f-36dd-b0ac-462e446cb1f3 | -8.0738 | -43.11016 | 2025-06-19 00:01:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 83a3525d-62c8-3fd3-82c6-0f2405b6d5e7 | -11.91135 | -44.17149 | 2025-06-19 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| c4528e4c-72b1-3a1a-b464-99d7a9e95c09 | -7.24397 | -43.07664 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| bfd3d599-f901-32fd-9a27-b05430b8fae6 | -7.1524 | -44.07161 | 2025-06-19 00:01:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 4dbdf84a-acf1-3853-82df-1ee633fc3114 | -7.36343 | -47.0486 | 2025-06-19 00:01:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| edb15a09-dfd4-3ed6-8b7f-b2aa7b5536ec | -6.68266 | -43.20718 | 2025-06-19 00:01:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2b0d7451-b54c-35bd-92e7-49b2a672bb4e | -6.29111 | -44.23957 | 2025-06-19 00:01:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 6b3c4225-a12f-31b7-90e6-ee0a66d49c07 | -8.72053 | -47.99886 | 2025-06-19 00:01:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 08dd278f-9120-39f0-97fb-21e57cfbae36 | -9.54659 | -40.3429 | 2025-06-19 00:01:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 44.0 |
| de3066d0-bd32-312c-b1e7-e1366dfc9a6d | -7.24924 | -43.08175 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ccd56ae5-e484-3aec-8dbb-47c7bd6a9d18 | -6.71068 | -43.25591 | 2025-06-19 00:01:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7776c90e-ba33-31f8-a750-460bf92716e9 | -6.29063 | -44.22961 | 2025-06-19 00:01:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 597621fc-887f-3225-9941-86948e11a3ee | -5.12473 | -45.01953 | 2025-06-19 00:01:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9b6b4b24-f939-32ce-bdbb-52e42b305dca | -9.8939 | -48.02967 | 2025-06-19 00:01:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 88eb91e4-5693-320c-9690-4a823e5f4c04 | -7.36522 | -47.04319 | 2025-06-19 00:01:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| b231f575-91c6-3407-9170-fa0e99847860 | -8.96598 | -47.99156 | 2025-06-19 00:01:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| ca5531ea-955e-375b-805c-c67ec4d49f8f | -7.22819 | -43.08463 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| de503de9-45e9-31cb-8e27-a2cff6ce786b | -8.06807 | -43.10363 | 2025-06-19 00:01:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 58cfa1b9-557d-3d11-b93a-c87f7e492a6b | -6.29274 | -44.24526 | 2025-06-19 00:01:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| cdafe023-6438-396c-81ae-db6616d827f9 | -8.12001 | -43.13118 | 2025-06-19 00:01:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| a061b881-2209-309d-b000-16dc083e4c0d | -7.24045 | -43.09612 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 900bf1a1-a4ad-373a-80d9-680ca1b95735 | -5.12131 | -45.0312 | 2025-06-19 00:01:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 4d57cc4e-2c22-3813-92bf-f174da895d9d | -9.5479 | -40.35253 | 2025-06-19 00:01:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d3a04f6e-f06b-3df2-bc6e-4c2071cc61f4 | -8.06984 | -43.11693 | 2025-06-19 00:01:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 9162c91d-7de5-3cac-ba19-6cfa5bd02532 | -7.23699 | -43.07032 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 060cb741-8c77-322b-88c0-0505ed65a67f | -7.23872 | -43.08322 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 260.6 |
| a729e360-4530-3f67-ab89-39d3bde2b2e6 | -6.86037 | -45.55808 | 2025-06-19 00:01:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e8d40d39-aa97-392b-8f33-93a628c38f3b | -9.37836 | -47.65005 | 2025-06-19 00:01:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| eea4e46a-5e1d-384a-84d2-5b8409a273fb | -9.37304 | -47.64399 | 2025-06-19 00:01:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 06d1cdb9-b4ff-3080-82f5-583b00b8a8a5 | -11.91356 | -44.19013 | 2025-06-19 00:01:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| fb959d36-e0bc-3c30-9e4d-27991e542722 | -8.13247 | -43.14321 | 2025-06-19 00:01:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| c1196ef3-c8cf-3a64-8505-5f8b76a30833 | -5.127 | -45.03614 | 2025-06-19 00:01:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 9c6abf1c-e6d7-380a-b9f6-3b3977de954f | -5.91083 | -43.45749 | 2025-06-19 00:01:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 47725097-e09e-314a-8459-684cdce17833 | -7.24561 | -43.08958 | 2025-06-19 00:01:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 6f0b6206-89c2-3b03-9bf1-c67030257fbd | -8.96194 | -47.95839 | 2025-06-19 00:01:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 71118d0a-6b6d-3fb8-a151-1e20ba743b8a | -6.28915 | -44.22407 | 2025-06-19 00:01:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e8384b40-4a76-3c01-bb5f-7504845dc11b | -6.6844 | -43.22022 | 2025-06-19 00:01:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 04eb3cfe-03fc-36ed-9f26-45254bb310e6 | -6.24438 | -44.65823 | 2025-06-19 00:01:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 9279a14d-be47-32e7-bd2c-6f1e5ab43ac6 | -8.95875 | -47.98728 | 2025-06-19 00:01:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 9b25d980-f11f-31eb-aca7-a2c61963b344 | -6.24215 | -44.64154 | 2025-06-19 00:01:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2300282e-ae7c-39d9-b2f0-3c807526451f | -9.90132 | -48.02354 | 2025-06-19 00:01:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 393f2337-24a6-3813-8791-84bfed4a0c14 | -6.30253 | -44.23862 | 2025-06-19 00:01:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 988c105f-2c01-395a-9cc0-06afca6c1409 | -7.15037 | -44.05603 | 2025-06-19 00:01:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| fea74262-650b-3aa5-a3f8-cd27b20bc859 | -9.8843 | -48.000702 | 2025-06-19 00:02:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35975155-ab8b-3755-ac76-212eec9e5919 | -8.9535 | -47.971901 | 2025-06-19 00:02:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2447dd3-47c4-3cf3-ac7c-d77bed0a3be2 | -10.645 | -49.440701 | 2025-06-19 00:02:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5782d4d4-925b-3e63-80ea-383c8f59b267 | -7.244 | -43.071999 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0315a08-62b1-3d54-bc85-791d7e18f6c8 | -11.9055 | -44.1623 | 2025-06-19 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd07893-c765-3e7c-89bd-43384c3d1e4f | -7.2366 | -43.0849 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb165cac-1fdf-3dbd-8cf6-66c9c8261f5f | -5.1236 | -45.0187 | 2025-06-19 00:02:00 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20cbea98-ab30-380d-81e4-aaf56e9b26a0 | -9.5499 | -40.344601 | 2025-06-19 00:02:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 416672a2-f475-3dc2-8397-49403bc032f3 | -8.0716 | -43.115398 | 2025-06-19 00:02:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 59552587-ad3d-3b96-a5d1-126720f7f0d1 | -7.2487 | -43.0937 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 76f6668c-2da2-3ae1-a8f3-777ae157b1b2 | -7.2318 | -43.063202 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 00657f8e-b31b-3568-877e-dc9ae9d5bf3d | -5.1266 | -45.032299 | 2025-06-19 00:02:00 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a549bd9-4221-3524-b6c9-70064acbd115 | -4.7648 | -47.568802 | 2025-06-19 00:02:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1419f2b8-33be-3998-9a53-f214fdeb5a55 | -8.9485 | -47.946999 | 2025-06-19 00:02:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1db2fb68-869e-3a63-ae12-78ca94213fb7 | -10.629 | -49.4091 | 2025-06-19 00:02:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce76051-499d-3d14-917a-d07318405374 | -4.7745 | -47.5667 | 2025-06-19 00:02:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce7001e-aedb-3a5a-8173-4027dc07a324 | -3.0295 | -49.403999 | 2025-06-19 00:02:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd24afab-b3f8-3217-8cb3-3548b8166c4e | -7.1532 | -44.0681 | 2025-06-19 00:02:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f7596d6-46fb-317e-9c96-ef04d690ce23 | -4.7701 | -47.546501 | 2025-06-19 00:02:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebe36b9-fd3b-387b-90d3-0c53beec17a2 | -6.2911 | -44.237801 | 2025-06-19 00:02:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65066af9-dde8-3097-a9b4-f1a195d24e82 | -3.0198 | -49.406101 | 2025-06-19 00:02:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac645ed1-1544-36f1-bda7-c80ea1816edc | -6.2485 | -44.6525 | 2025-06-19 00:02:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c77e39ef-3035-3096-8dfc-4f2bad86421c | -14.4262 | -48.8587 | 2025-06-19 00:02:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6c9689e8-9b4c-338e-bbb4-7ea12624bdd6 | -11.9085 | -44.177399 | 2025-06-19 00:02:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da773bef-9414-3833-b2c0-7c4f8a345490 | -6.2387 | -44.654598 | 2025-06-19 00:02:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5af9ba-f3e7-32c6-9861-e561e4ea7021 | -7.2342 | -43.0741 | 2025-06-19 00:02:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49f1db97-01b0-3fc5-ab95-b833eff4ec46 | -6.2456 | -44.639099 | 2025-06-19 00:02:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8bc670bc-2023-37fd-b274-3e805d378308 | -10.6386 | -49.407299 | 2025-06-19 00:02:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3931dd2-dd7b-3922-b34f-6cec36c79efb | -9.5481 | -40.336399 | 2025-06-19 00:02:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 02ea917c-cb3f-3f88-830c-3b3d8ef3c564 | -8.1278 | -43.139 | 2025-06-19 00:02:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
