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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9b6c9ec-c1e6-3919-a740-65202b918630 | -10.65683 | -49.36582 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 04c1e5ef-95da-35f4-b1af-375c8ed116f0 | -6.16213 | -44.4171 | 2025-06-18 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8488aedf-0bbc-371a-84f4-4062d0935977 | -12.23511 | -44.20201 | 2025-06-18 04:38:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bdbb1b5-7931-3239-9be2-3612b09c0973 | -10.62462 | -54.91515 | 2025-06-18 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6c94b21-a7f3-3dd0-8f24-f7086cf5a4cc | -8.72711 | -49.02497 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1f7ecab-2b0c-3c07-b07f-9d4eb042a254 | -10.35544 | -57.24951 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f1b5116-aa9c-3ae7-b195-b8493f6a0752 | -11.91136 | -44.17854 | 2025-06-18 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 376efa34-ec93-36e6-9385-79de630368f6 | -6.69596 | -47.38921 | 2025-06-18 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 793b000a-12eb-3eec-9707-4ee7939acc20 | -9.85785 | -47.88465 | 2025-06-18 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8cfc8f8-1d45-3385-b5c9-7b95cacb32fe | -11.79445 | -43.79253 | 2025-06-18 04:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a138394c-dd1a-3a76-b695-7340e8778d9d | -6.12883 | -42.53535 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9413498b-1f3d-3451-8e3a-bee4c0a936f0 | -8.96285 | -47.97168 | 2025-06-18 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30d464a6-d3dc-34dc-b4d2-687e900671c4 | -6.41828 | -44.79628 | 2025-06-18 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89d6d221-3065-3fb6-b4be-b5541690ec9f | -8.72323 | -49.02798 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd6d5dbc-93b4-3532-b778-ad7823fb0ca4 | -6.67627 | -43.18346 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb6b529a-0261-3cf8-bd26-756df65eabf9 | -6.1204 | -42.52936 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 34449094-02ee-384f-a0a1-52dccc978ec8 | -8.79551 | -47.52426 | 2025-06-18 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97fdd603-115a-38b0-9162-5d3db41dd95a | -10.73143 | -49.56355 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f227304-3fd7-3373-a74b-cf466e7272f7 | -10.616 | -54.91883 | 2025-06-18 04:38:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14bbc74c-3486-31ce-84e3-53d2cbbd7bdb | -10.65404 | -49.36172 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7f6aaa7-a834-3e3a-871c-c5c86f687d6f | -9.84348 | -44.7012 | 2025-06-18 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b2eb424-3afa-30af-8328-cce4389f8d9c | -10.66072 | -49.36278 | 2025-06-18 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ca8e9ee7-da46-3ccd-b39d-d47eb5862baf | -7.99155 | -49.66735 | 2025-06-18 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98b45082-215b-3e57-b872-f8b79de84774 | -10.7281 | -49.56303 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92696b79-a2be-398f-ae1e-0a9c36698707 | -8.72504 | -47.99348 | 2025-06-18 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e627c634-7b66-3acd-b623-74012dd6ed45 | -7.54548 | -45.63924 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f267c960-951d-30ea-9562-df4f2c5472c5 | -7.54414 | -45.64843 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8845067f-7a1f-34d1-a2ed-480609082b8a | -11.90693 | -44.1779 | 2025-06-18 04:38:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb5689bd-53e6-32c6-9b79-c78c58b0f716 | -9.15772 | -49.63909 | 2025-06-18 04:38:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 26cf18d5-2524-31d4-a778-c955e3299260 | -9.96496 | -47.93998 | 2025-06-18 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3cf9dd7-34fa-3eb3-be9b-dec29189b89d | -8.2271 | -46.09626 | 2025-06-18 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72a07653-9221-31e3-8c3d-b1036eeb3f7a | -10.29486 | -57.13941 | 2025-06-18 04:38:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecbf1600-a66d-3be7-be8d-b932ae91d2e3 | -6.37249 | -43.7542 | 2025-06-18 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ee5f0540-4948-329e-9447-2822baf5ea38 | -7.2831 | -50.00196 | 2025-06-18 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56d17bc9-f388-33d1-8f8e-9ee40088bdd4 | -7.25558 | -44.63812 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ff353eb-1b22-359b-9a7f-18abb39c739f | -8.06892 | -43.11011 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ad62df5e-3bb9-31a0-a256-819e0bdef38b | -9.88313 | -44.79547 | 2025-06-18 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7a1f680-9725-3e43-8710-d2370eb0b8ff | -4.81516 | -46.82215 | 2025-06-18 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 180868a9-c4ac-36d8-8455-0ed0d54ac525 | -6.8694 | -44.83435 | 2025-06-18 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e616af54-cb23-3283-af00-4fa9b83ee747 | -7.27924 | -50.0049 | 2025-06-18 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d6f7546-dd17-3634-9073-4b2fda585a61 | -8.43905 | -46.9073 | 2025-06-18 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df15ab79-030d-3a6f-9010-bb675267fefa | -9.85726 | -47.8885 | 2025-06-18 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cbe3a36-12c2-3750-bf16-a1ef200282fd | -7.54456 | -45.64576 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 490d76ff-4b27-3d0d-922c-8982b8da485e | -9.26452 | -50.04119 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00c07792-8af7-3a5f-ad3c-94fcdf033124 | -10.91821 | -56.84033 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c68412c-fba0-3d32-b329-bdf9911ebda4 | -8.32648 | -46.23 | 2025-06-18 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c8c7fec-6910-35af-bbfc-aecc684aa011 | -7.80713 | -46.57501 | 2025-06-18 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f43ba82-4338-362c-92ae-fc7391e4aaac | -8.06314 | -43.11856 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 68218060-b059-33c2-93cb-b49028578cf2 | -8.07794 | -43.11135 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a3b405bb-c8fd-352f-8b5d-6ad0ff818b61 | -11.12562 | -53.93942 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0517282c-16c5-3a96-9c6c-74f7ec629cfb | -11.12915 | -53.94189 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c13e59a8-f7e2-3cb7-9faf-c8537cbaaddd | -9.10639 | -46.48109 | 2025-06-18 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4033f334-3d64-3fd4-a1f9-2ecac8d69a6b | -7.5428 | -45.65766 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2da76145-e12c-36dc-b812-e51bead6c6ab | -6.12496 | -42.53003 | 2025-06-18 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| de68c231-4316-341a-9c33-7c462ca0226c | -7.60779 | -45.55818 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2a72c35-e658-37de-a883-2a2f7d9b854a | -11.13217 | -53.94502 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8d56aedf-6014-318e-ad53-ea5d789a5f33 | -10.91306 | -56.84388 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53ae730e-3f65-39ac-879c-cc6228235828 | -10.98472 | -45.09993 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 450d29b5-e5c4-37b2-a153-6f8be5d30f9e | -9.41363 | -48.41566 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aed45684-9840-32ae-80a7-9736aa69e93d | -9.25757 | -50.04037 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9272388-0009-37dd-8ba6-57b0ae4189a7 | -7.23621 | -43.10036 | 2025-06-18 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bb7c458c-9c0c-3850-8575-53e9ad2b012f | -10.24163 | -52.22705 | 2025-06-18 04:38:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99e38079-82ca-3894-a840-e717d1eed492 | -9.40405 | -48.43304 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4893abb-1098-3b04-9002-8b86955200a7 | -8.06764 | -43.1192 | 2025-06-18 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dad82213-0028-3cd1-a325-fe271727f749 | -11.58017 | -44.8403 | 2025-06-18 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a29d5fb-4be5-360e-acb6-0bffe70b6da8 | -5.84938 | -43.63961 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22ac2a23-2acf-30e8-b74a-5e30f6dac3f0 | -8.8797 | -48.51807 | 2025-06-18 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85098088-5580-3931-a8de-1ec12f4ea08b | -8.23832 | -46.39133 | 2025-06-18 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21521621-44f8-3a5a-a04a-bd26b2cedaa8 | -11.12927 | -53.94006 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 92284d8a-2407-335c-b9e5-1a9caefec43c | -8.72448 | -47.99721 | 2025-06-18 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc9b72fc-b790-3119-975b-069db995caf0 | -9.25867 | -50.03341 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcc54f04-f40a-3c70-a3df-ea0fad3bab86 | -8.81402 | -48.48558 | 2025-06-18 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3915905-cd75-3983-a399-336dfd26bcf2 | -5.91614 | -43.4476 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe340846-2979-3d6c-8be0-3b3c285c550f | -8.72099 | -49.02039 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 47ee9722-442c-38ff-9886-c414340c40f6 | -7.48578 | -49.5801 | 2025-06-18 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af8e3527-abdd-3ea3-bb2c-c0e37dd30597 | -9.41419 | -48.41197 | 2025-06-18 04:38:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d4d0711-eb89-3cf7-9e53-8ee0edb26abb | -9.86074 | -47.88904 | 2025-06-18 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4157c25f-575c-3b75-9e50-84199ed97966 | -10.54415 | -48.64334 | 2025-06-18 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f505cc17-da8b-34c9-8d16-92c02fbf338f | -10.98422 | -45.1036 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f288cff-4677-3329-8290-c2e7eb5d8017 | -7.42016 | -47.66609 | 2025-06-18 04:38:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e563e179-2b2d-3ae0-9bfe-65a57e1288c6 | -4.81817 | -47.3245 | 2025-06-18 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f4f4ce-a7c2-3699-9c2b-71480670da67 | -9.25481 | -50.03637 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a741b52-355a-30e3-9966-1c0de3c15b62 | -6.01801 | -46.69162 | 2025-06-18 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0095a167-eba3-3376-b35b-ef6224229dff | -9.84508 | -44.7051 | 2025-06-18 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5b166eb-a8e3-34b8-b253-68726461a066 | -9.14557 | -48.97396 | 2025-06-18 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7a8a056-b4ff-3deb-b4e5-3cf6fb2e55c0 | -6.04252 | -44.04847 | 2025-06-18 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56fd8e3c-0433-3c25-bc9a-19781502aa6a | -11.13731 | -53.93695 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d62e877b-a310-3195-af73-574444a43bb7 | -4.69708 | -48.58389 | 2025-06-18 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0335c59-d3a7-393e-a190-b796572a7a3a | -10.86256 | -53.76548 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a370eb02-6b0e-35a6-aa99-2d68a75831ec | -6.67064 | -43.1914 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8cc63f2c-0fd9-320a-9494-f215cac2cbbd | -9.45802 | -57.84799 | 2025-06-18 04:38:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5bc67e2-3b68-3c49-bbde-e0264669d028 | -4.71441 | -48.4306 | 2025-06-18 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f9bfc84-4bed-3bd8-a9de-56f781a686d5 | -11.13806 | -53.93259 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7883fc42-476b-35d1-8737-ad4fde642f77 | -6.68874 | -43.68697 | 2025-06-18 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b42e987e-a1e0-383a-af45-51318d7a594b | -9.14612 | -48.97041 | 2025-06-18 04:38:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1a8e0e6-221d-3f42-979b-cbb451c650a2 | -11.0806 | -55.05337 | 2025-06-18 04:38:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5553d20-d924-3d77-981e-a47f9699ee5d | -10.85966 | -53.76054 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0512b4a-dcb5-3b64-8909-b673e61920ea | -11.88251 | -47.45739 | 2025-06-18 04:38:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31b6932d-d070-38ca-bbd8-1d503c984f7b | -10.72755 | -49.56657 | 2025-06-18 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0eb45b81-8f48-375a-b947-561556f8a148 | -8.72154 | -49.01686 | 2025-06-18 04:38:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README19.md)
