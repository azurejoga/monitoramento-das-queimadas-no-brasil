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
| 3aff7d71-fed7-3f79-8eec-b6fda8c37228 | -3.9723 | -42.49664 | 2026-01-10 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6dcb258e-4ef3-3e4d-b7aa-b2b07070230b | -5.47772 | -39.65747 | 2026-01-10 04:25:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d2aadb20-9bf0-39ec-94e0-23957a2237fc | -6.66456 | -39.65477 | 2026-01-10 04:25:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fda58e62-8044-38fd-9d14-62c024ee4cac | -2.87008 | -45.23238 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 623b1239-b60a-3b22-a842-c6c62325b61e | -2.43504 | -46.89625 | 2026-01-10 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfca8273-912a-3b71-b6fe-5e6cb6c50e4c | -2.06524 | -45.59111 | 2026-01-10 04:25:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e2c068d-0605-3fc0-a748-4c3134e46ebb | -2.8783 | -45.22308 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c4435ae-8e56-3431-83ce-8a41576fe5a9 | -2.87169 | -45.22206 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3155ebc8-3206-34cb-969f-f11b2bd34923 | -1.70339 | -45.8156 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d23bd712-e515-356c-915e-f4ac6490cde1 | -0.09054 | -51.27822 | 2026-01-10 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e8b71afe-dee7-3293-ab65-bb8c63e33a0e | -5.885 | -39.07478 | 2026-01-10 04:25:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 306eb59b-0081-345f-a1d2-c9cf24a53825 | -5.49415 | -42.17152 | 2026-01-10 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2fcac459-e192-39f8-b9ef-92e920f4fe0a | -2.92012 | -45.21545 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6190cb1e-418f-3901-8bd6-5047dae57511 | -0.11687 | -51.45252 | 2026-01-10 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b50cd03-dc7b-33fb-a3d6-af5a04f06ab3 | -4.45148 | -44.1309 | 2026-01-10 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66680d19-39a2-3d74-ab52-cc9ad9dc3220 | -1.1391 | -47.1229 | 2026-01-10 04:25:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee9bc7ab-81b5-394f-8921-ff0c098c92cb | -2.869 | -45.23926 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4362530c-d792-39bd-bec0-e328b5a2e8fa | -4.24582 | -43.78069 | 2026-01-10 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df014aaa-a3d1-3c7e-acd9-417622a314b8 | -5.67384 | -45.20374 | 2026-01-10 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3538cd8a-8d2e-319e-ab89-ed8a83b5dd7b | -2.88822 | -45.22462 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86d69131-2355-32a0-8c6c-b8ddcb448293 | -2.79078 | -43.3448 | 2026-01-10 04:25:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c663a7ae-2602-3250-8b99-d0664cc20c9b | -4.17753 | -43.83551 | 2026-01-10 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34f3db48-b6cf-3c2b-83ac-957974dfbd84 | -2.4356 | -46.89272 | 2026-01-10 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a735ed2-3314-3004-92d8-fc674784f8b6 | -5.4822 | -39.658 | 2026-01-10 04:25:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52c20ff9-b9e7-3bc0-add6-7de95d820e95 | -1.70724 | -45.81267 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e99be0c7-ce43-38da-9207-2500765dbffc | -1.10432 | -46.6133 | 2026-01-10 04:25:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6e7182c-2ffc-363d-a6f2-d3b677db830e | -1.93008 | -45.1937 | 2026-01-10 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d70c91-9da5-3069-8dba-0d674d33e0b5 | -3.87541 | -40.34796 | 2026-01-10 04:25:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7b370c42-ddfd-379d-8984-085249a30408 | -1.93062 | -45.19027 | 2026-01-10 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee03f1ac-2c0c-320e-8083-e7bdf3304ba6 | -2.87 | -45.21122 | 2026-01-10 04:25:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0812f91-6e62-3e90-984b-9a826f359031 | -4.00469 | -41.79725 | 2026-01-10 04:25:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e586c40-8a6b-39bf-8c8d-ca36cfdc5f31 | -1.70447 | -45.80872 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 42a71a2b-e364-38d8-a4c1-f6953524a5e5 | -2.86892 | -45.21811 | 2026-01-10 04:25:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e793aabe-d4bb-3198-a57f-c43516334f74 | -2.66237 | -45.60019 | 2026-01-10 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b977e334-23d3-3939-8a21-9a5b85715a32 | -4.34013 | -44.12547 | 2026-01-10 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9837b60f-cace-3ca8-a2a7-3ef63213b1a5 | -2.14597 | -54.39027 | 2026-01-10 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29058321-446b-3705-aa06-ed31eece3b1d | -2.93935 | -40.39426 | 2026-01-10 04:25:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3b686463-c80f-3af4-8a41-803b124f0e5a | -4.99294 | -42.6796 | 2026-01-10 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dcf427df-5503-3afb-9098-4609e0572f12 | -1.70778 | -45.80923 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfb64b02-2b1c-3db6-bc06-5102e039c5fc | -2.79019 | -43.34859 | 2026-01-10 04:25:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f92ee7f-a447-3985-9a08-721146e8b436 | -5.49433 | -42.16891 | 2026-01-10 04:25:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1ed43531-0d7e-3d27-bd9b-d44d61406f8d | -2.78673 | -43.34805 | 2026-01-10 04:25:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bebac9a4-2a1d-38ac-a2c2-9ca33e80b59e | -2.0316 | -46.38897 | 2026-01-10 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9943369-b1d4-3bf0-832c-dbf1bb96c4c3 | -3.25529 | -41.83604 | 2026-01-10 04:25:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e61795bd-ca7b-3aea-a0ff-7dc0e9512d92 | -4.2464 | -43.77695 | 2026-01-10 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 026d944d-bdaa-3f5b-a41a-051d896b40e3 | -5.70302 | -39.87186 | 2026-01-10 04:25:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f63b0d6-47ef-3df3-8e07-017fc35848c3 | -5.04328 | -43.26237 | 2026-01-10 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a1dc9f6-0bfc-35c1-a02f-8533ee98803a | -3.64814 | -42.02316 | 2026-01-10 04:25:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90be1715-1fee-32ce-a3a1-4d90a4400fc9 | -2.91958 | -45.21889 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f5491d1-4699-3fe2-a3a3-3836e6152950 | -3.97595 | -42.4972 | 2026-01-10 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e3ac74b-f304-36d1-a3ff-52099546a285 | -2.89152 | -45.22513 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9d730ad-6f82-362a-91ce-f35415139873 | -2.93943 | -40.39524 | 2026-01-10 04:25:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| aa8f3fa8-600e-35eb-b899-1a7b4a6d694f | -5.40465 | -41.91841 | 2026-01-10 04:25:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c0ac971-1889-314d-9bfd-5f631957bccd | -3.44818 | -42.24915 | 2026-01-10 04:25:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b1655ade-2b16-3dae-8362-195c4f6b2e82 | -2.87884 | -45.21964 | 2026-01-10 04:25:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cda36e87-8a29-3d60-88de-62cf8137992e | -1.71109 | -45.80974 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71f382f0-20d3-3c19-b690-870acb29f0da | -5.1755 | -37.76196 | 2026-01-10 04:25:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1e261e61-f201-306d-93f9-f005d54d50ae | -2.87062 | -45.22894 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ece6ebe1-ef0e-39ac-878f-5694e5e4d69f | -1.10769 | -46.61382 | 2026-01-10 04:25:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be18ce7b-a57c-3617-add5-22657db4b23e | -4.45488 | -44.13144 | 2026-01-10 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bad73a9-6891-38b8-8b01-bd90707cec1c | -4.31744 | -39.14642 | 2026-01-10 04:25:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a35d6dea-92bd-3e94-86ec-08aafe22d568 | -1.6612 | -45.91144 | 2026-01-10 04:25:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a29b565-2822-3aad-b936-bda094833af5 | -5.91423 | -42.65047 | 2026-01-10 04:25:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c214994-d910-3411-8e01-caa12328ea53 | -2.19493 | -46.38931 | 2026-01-10 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 134dbe22-98f9-3d36-bc53-0dd11360ae86 | -4.32992 | -44.12389 | 2026-01-10 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b119e9-44f5-3606-98a3-41820e5120ac | -5.48286 | -39.65349 | 2026-01-10 04:25:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d80fe360-7ef1-3376-abc4-33df5f099e96 | -2.3619 | -45.58867 | 2026-01-10 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e4f6b9b-6cde-3822-8772-9bbc7aaebd55 | -2.89206 | -45.22168 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63a2b3d2-ef67-33b1-972e-0d6e5f0cc9fd | -3.75802 | -43.48799 | 2026-01-10 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86a31ceb-eaa8-3d8b-aa0d-78df73168840 | -1.10712 | -46.61739 | 2026-01-10 04:25:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 749ed27e-bfc6-3e2f-b8c7-da75df97ff13 | -2.86785 | -45.22499 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0fb0bb9-5134-3ce2-872b-126d670cd5c2 | -4.24238 | -43.78016 | 2026-01-10 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d3bd9dd-d09d-3a6c-99e7-127d0d209ba9 | -1.08605 | -46.7719 | 2026-01-10 04:25:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e8e869b-ba8c-3edc-be78-d0ebacf79fb6 | -2.88107 | -45.22703 | 2026-01-10 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab74578d-28a5-3743-ac57-3d0de7a5e28c | -5.35511 | -40.89171 | 2026-01-10 04:25:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68cc17f0-94d9-3b99-938f-5ad86e0cdce8 | -5.72252 | -41.27702 | 2026-01-10 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c6d7627-cd99-3084-b9ad-6ead66615d53 | -1.71163 | -45.8063 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06558728-8114-32e6-abdb-e2c07ccdb013 | 2.11206 | -55.7642 | 2026-01-10 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 773735c4-efa9-332c-844c-ad2b61e7dd28 | -2.36243 | -45.58524 | 2026-01-10 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db15c92f-2fd2-3f62-b100-3fb816ab767b | -2.58068 | -54.73071 | 2026-01-10 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c790d97-bb15-3411-b47b-ade01367fb60 | -2.06876 | -45.65489 | 2026-01-10 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8dadd2e1-fcde-3aad-ba4e-d68f2d655c9e | -5.88431 | -39.07962 | 2026-01-10 04:25:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 006e8df8-4ab5-32b6-870a-7e442dfcacda | -9.04199 | -46.98678 | 2026-01-10 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 210ce795-699f-3409-8acd-9c659006b77a | -7.70231 | -46.85066 | 2026-01-10 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b0e863b-5887-3812-afe0-8bd058e75252 | -7.49864 | -45.55912 | 2026-01-10 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6dc5fa7-8a61-3f44-a8f7-96a79853869c | -6.36144 | -46.15987 | 2026-01-10 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 047cf2dd-c064-3be2-b080-221ae6c91cb7 | -11.83842 | -48.64447 | 2026-01-10 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c780ea16-46ce-3aab-8bbc-e0d322b9036c | -7.49476 | -45.56214 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1168ecb-5cd7-3548-a902-268c7809bfb8 | -6.08622 | -44.3345 | 2026-01-10 04:27:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a3ebb5c-7545-3b33-8702-1770d48f980f | -11.83784 | -48.64804 | 2026-01-10 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81d2ff6f-e892-3148-a976-a7ef7c84f0b2 | -13.78913 | -43.24201 | 2026-01-10 04:27:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a90b8157-05ef-3850-ba21-850679dd4b6f | -10.8093 | -47.68986 | 2026-01-10 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46b7d62e-06b8-391f-aed8-c4f6a9d8eb97 | -7.3619 | -47.0275 | 2026-01-10 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d684a0c-d25f-36bc-a650-63a89f509dce | -11.13548 | -46.57763 | 2026-01-10 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82766058-4b42-3654-8163-d559626fc939 | -7.72513 | -45.63445 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ec48b94-1e3f-3d94-87bf-c261c56a9044 | -9.98738 | -44.75675 | 2026-01-10 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c72806b6-a3a9-3526-850a-8dc4f69f7b4b | -7.57054 | -45.62468 | 2026-01-10 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e992626-6713-3bd2-823f-748f5038ff04 | -11.83016 | -46.61401 | 2026-01-10 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fab4952-c6ec-3402-88ca-6e96bf534f12 | -10.95955 | -45.0649 | 2026-01-10 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92cd9892-ac07-3dad-a3d4-4b5c292bb6bc | -6.15706 | -46.96286 | 2026-01-10 04:27:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README7.md)
