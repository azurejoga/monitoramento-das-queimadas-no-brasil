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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81b749e2-0bd2-3610-946a-9684e890e0a8 | -3.08861 | -46.56897 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dc0a727-1ab5-3cc7-837f-bcbdc859819a | -2.6314 | -48.0377 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c687bdc1-fd59-35f1-b7c1-6c6abdf17d9d | -2.77268 | -48.5718 | 2024-12-21 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4410648d-2dc3-3e55-b511-963b6291f367 | -2.05754 | -52.05614 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab6abb9e-faba-32d3-8330-39488d2fd028 | -3.79752 | -46.85087 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aedf1afd-f0ff-3dda-b322-66fd8c72a4eb | -2.67624 | -46.9315 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03a18ff7-892b-35c9-bf27-527188a12712 | -5.69188 | -46.52916 | 2024-12-21 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 998bbdf9-2d22-30e8-9631-6ce8c973a11d | -3.08556 | -46.56383 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6af82d6c-385d-392c-bf63-604a3da0a947 | -3.94211 | -46.59155 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5723c9b-411f-3308-b383-41156fd190b3 | -2.80406 | -46.7081 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2568a2ee-24f0-3411-8a1e-42a96eae1a65 | -3.09059 | -46.56195 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fee9e74f-2d61-3c32-8705-bfae48ff9bdd | -4.06744 | -46.4057 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 850179e5-2620-3632-a2ae-629555fae186 | -5.17513 | -37.58314 | 2024-12-21 04:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ffa3937a-55fc-3189-b288-a82a881667b4 | -3.69517 | -53.46326 | 2024-12-21 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e502877-062a-3224-8097-db85768ab762 | -1.74584 | -45.74763 | 2024-12-21 04:46:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfd0e165-646a-376c-a2ce-8543d94e5b13 | -2.67713 | -51.70906 | 2024-12-21 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d48d4e15-39fc-3c5a-89bb-75ca94d8f7c2 | -1.66234 | -50.69462 | 2024-12-21 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08a1ce1c-3cfc-322b-a579-71acd347bf69 | -2.6799 | -46.9321 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c674a00-2c15-32fb-b870-45d4c1071665 | -2.63199 | -48.03389 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c79c406f-3eb6-3567-bdab-d27d810a84de | -4.01022 | -46.9411 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 380bce76-1b68-3ad6-bfc3-3597038fc924 | -3.4628 | -52.9619 | 2024-12-21 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8dc3dfd-934a-385e-a343-a0cb93d08a21 | -2.58148 | -51.92157 | 2024-12-21 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 761b556f-d913-323b-afbb-34e88a41f8eb | -2.7908 | -52.94734 | 2024-12-21 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287b79a0-208b-302d-bc6d-82c8570f4791 | -2.65453 | -46.11306 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f8b03cb-7424-3f9d-accf-36246739ce44 | -1.15358 | -53.59851 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef970f8b-6b24-3426-9347-25770c0cff1d | -4.47383 | -44.09599 | 2024-12-21 04:46:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18c19050-eafa-35ee-a1e8-21519dbefb09 | -2.76692 | -47.39539 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e6044f4-1d98-30f7-8394-805aa732f378 | -4.55908 | -45.72428 | 2024-12-21 04:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a50026b2-deaa-32af-b4ba-e35e144118f8 | -3.88606 | -47.02939 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d762f73-89ff-3e5b-a638-e659aa496e38 | -3.91842 | -46.36129 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d6675f5-b260-3be8-bd0b-845ff23051e4 | -3.2855 | -46.13855 | 2024-12-21 04:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8ac086c-f8b0-35fa-aafa-3599600a5258 | -2.81801 | -52.97954 | 2024-12-21 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d087fd5a-d320-3a5e-aa88-fb4f7883baed | -5.60498 | -42.82481 | 2024-12-21 04:46:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2449fde6-7dfa-3334-b0ec-a2234f661b5b | -2.43996 | -51.78901 | 2024-12-21 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84913a2b-23ac-33c7-8505-2ef12ff1f1b3 | -2.70747 | -46.14313 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab0095bf-7a5e-3c11-b105-a4bed8765266 | -3.76771 | -47.18868 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63bff549-5926-3c48-ad7f-9f8e24c4cf98 | -2.07628 | -52.04778 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4967fd5d-e691-362b-9511-840c3b62b477 | -2.41962 | -47.81717 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db76bc41-207f-3e75-b9e3-07347276b61a | -1.21956 | -53.68401 | 2024-12-21 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f97f035-446a-38b5-acc1-b27b9bea07d3 | -3.79937 | -46.84894 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d99fb5b-120e-3c6d-858c-855246087b23 | -5.60457 | -42.82777 | 2024-12-21 04:46:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4335b816-ac61-30af-9641-395a088a4399 | -3.75608 | -47.19135 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01fef07f-2926-318e-a819-a471f181720b | -5.9191 | -43.48136 | 2024-12-21 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f48c2683-6573-31df-9a49-4f3320ab7a71 | -4.139 | -46.46716 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7f84f77-7683-3618-b0d4-3e87811ed2a8 | -5.61235 | -47.5405 | 2024-12-21 04:46:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a2c1021-a46d-3dc1-aa71-ef3ed838e30b | -2.77112 | -47.39186 | 2024-12-21 04:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e171b2c1-b1fd-387c-89e4-75db2adb614b | -1.8752 | -45.55836 | 2024-12-21 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdcd36a8-6138-38e6-9974-0ca7a7ad4483 | -1.21855 | -53.68298 | 2024-12-21 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 712260a5-d727-3015-bdf5-92717adf115f | -4.03525 | -46.79798 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daee9a90-3fd5-3e40-9063-124b1044b053 | -2.67559 | -46.93575 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef0d93ca-9cd4-307e-a882-dc28e5f65a31 | -2.55625 | -46.88321 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 098f3b2f-3d0b-3f88-a521-936ee03e81c4 | -5.17424 | -37.58971 | 2024-12-21 04:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 70f793e4-f8ca-3b6f-a663-5c8d85e5a834 | -2.87399 | -45.23897 | 2024-12-21 04:46:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29cde157-3213-3017-a9d1-b4d12aa51232 | -2.67259 | -46.9309 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c22a4ab-6445-3b97-b50e-6e354226a445 | -1.34616 | -53.85099 | 2024-12-21 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7710d46-d994-3cb6-bdc7-85250e894619 | -2.70534 | -46.14026 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b8a7bc7-5f54-300c-9cc5-0a4646582c2d | -4.00304 | -46.98946 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 804843b6-e141-39f8-bf0d-7c623c89e87f | -2.06094 | -52.05666 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34d79df3-331f-3289-a754-39061bfcec66 | -3.92108 | -46.8886 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56fa9f84-0acc-3890-92b6-548101b26b50 | -3.94959 | -46.41508 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9c1c6aa4-d74a-3da5-874b-1b279642a47c | -3.47343 | -51.4475 | 2024-12-21 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c65178e-1674-31a3-a1b1-cd8bc5eb0f18 | -4.00432 | -46.90366 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38adaa5b-c9a5-3aa1-aa11-ed2f29be31d6 | -4.04957 | -46.80492 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21eae981-d0cc-3c5e-b6f1-de560206192d | -2.55258 | -46.88263 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c26c5916-52da-3381-9c5b-df89ace00acf | -3.97297 | -46.92375 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6cadb5b-b4bf-3ddd-b9b4-0884ef9bce4b | -4.05949 | -47.09257 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15a980f3-7ab0-3dc5-8132-2478e4945dc1 | -2.21872 | -47.03153 | 2024-12-21 04:46:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d337e6e4-2ffd-30f6-aa4f-92cc0f073faa | -3.94225 | -46.58946 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 311db976-14fd-3726-a972-eaa3f8b7fae4 | -3.90759 | -47.00454 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce197692-4d10-3077-a701-d2752ba79908 | -5.99005 | -46.15897 | 2024-12-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4218c6c7-9c90-396c-881d-e90be0d2c610 | -3.80193 | -46.84702 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d3e44db-4c6b-31b9-b400-4e9dd9f1f8ea | -2.84767 | -49.50747 | 2024-12-21 04:46:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ee3137c-91db-37de-9bec-0d9e07be5f22 | -4.58533 | -38.60378 | 2024-12-21 04:46:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 11a996b3-41b3-3122-8cbc-7eab86b82e70 | -3.75974 | -47.19188 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71001370-dc69-31b5-a4aa-4e98acf41d64 | -3.99158 | -46.64874 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d404b57-2376-3f19-979e-ebd4e1a26c2a | -2.61842 | -47.46549 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57c8d58e-4913-3f46-b7ec-8a36cfa17b1e | -1.2582 | -53.48238 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 991ac83a-f842-30ba-a7cd-3802ec571ce8 | -1.70505 | -52.58227 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec031529-3b29-3b20-89b2-91863770afbb | -1.29467 | -53.12542 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cf3c3ed-cbbe-35f6-a791-bd6d0def56cc | -3.95342 | -46.41573 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| aad60e03-ca59-33e4-a925-51e4c85963a5 | -3.92347 | -46.89819 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a769c7e7-4a9c-3689-9245-1bf91b669608 | -5.60668 | -46.80233 | 2024-12-21 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f06c1ab-d18b-3503-b82d-940cbb8cb7eb | -1.29236 | -53.11664 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9d2c4cf-21b0-3e9a-8cdf-4cdca1914b52 | -2.5013 | -51.82823 | 2024-12-21 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a3f6a27-add2-39d7-95e8-7e7fa2fad07a | -2.73395 | -47.73074 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49acb26d-d102-3425-b10b-1b5eaa14a9bf | -2.65141 | -46.10766 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d6aae8-0e79-339c-86a8-ff74d3a89489 | -2.7873 | -52.9468 | 2024-12-21 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdbcee5-912e-3d43-a1da-6ecc37224b57 | -3.81078 | -46.71502 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 389d6f33-ccd3-3fbb-b8bb-ff5004d543db | -4.10778 | -46.72503 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37309717-5dac-38f6-bb21-eeac2fb4da4d | -3.97164 | -47.03189 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d58ad3a8-3b1b-3585-bca4-2ea5b288061f | -3.08931 | -46.56443 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba27ec0c-db66-32c6-95d2-2e160018f99b | -3.9089 | -46.99577 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8db4cf7f-61dc-3895-a168-a442fe7782c8 | -3.75353 | -47.18414 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ed95cdc-471e-31be-80fe-1bc000d96e4f | -1.48506 | -51.99131 | 2024-12-21 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 358efb9b-2164-36b3-bf47-040f51138f97 | -4.53938 | -44.05871 | 2024-12-21 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b1760175-dc52-38fa-9fd2-9bcaf8e9939a | -4.03899 | -46.79861 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71293a48-1ae7-3bc6-801d-3d47b9fef5df | -4.02413 | -47.05137 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6002b3ef-dd81-371a-8c52-30ba3f64880b | -4.10196 | -46.73796 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dac3d96b-2de0-3d23-a1a7-d0a64f778f93 | -3.83409 | -41.56702 | 2024-12-21 04:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 942954f3-a157-33bf-98b8-f6328a87dccb | -1.88382 | -45.55461 | 2024-12-21 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README7.md)
