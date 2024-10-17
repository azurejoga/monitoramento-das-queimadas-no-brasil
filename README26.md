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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 282def36-abb0-3b7c-8e8f-26e7e8288184 | -3.90305 | -42.38836 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a919a2d1-ce09-3ba4-aed4-e519dd4d348b | -3.90251 | -42.39179 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ae1e2026-eede-3cf1-9c93-467938260803 | -3.90197 | -42.39523 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 74c8b016-d0a1-3f8d-b72c-1a6df1650fb4 | -3.90143 | -42.39867 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6565aefc-1514-3ba8-b336-ecbd2f79adea | -3.90089 | -42.4021 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 598f60e1-c729-3790-8ef0-741808516cf0 | -3.90035 | -42.40554 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 23c00109-3e01-3056-bf2d-aec822b912fc | -3.89981 | -42.40898 | 2024-10-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9ffe131-a920-3f1e-8032-e98837ba1700 | -3.89975 | -42.38784 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd56ef40-29ac-3671-ae0e-8bdbbaedfacd | -3.89921 | -42.39127 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| dde15c65-7ef6-3cff-b22d-b8c24f4ee8ce | -3.89867 | -42.39471 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 4190674d-1c86-3438-8fcf-3c693ea765f5 | -3.89813 | -42.39815 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 43f68f01-4e16-31c9-93c1-88a0889bcaca | -3.89759 | -42.40159 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5fe44f1d-c120-3693-89f2-ed3ffbe43331 | -3.8959 | -42.39076 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| b1352545-db65-37a1-be1e-4851b4229854 | -3.89536 | -42.3942 | 2024-10-17 04:12:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 76d430de-3348-333f-8e7d-774cabce63a0 | -3.89482 | -42.39764 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 88f53965-3c80-33ca-ad48-3d428f3f1dfe | -3.89428 | -42.40107 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f8d75f24-15cc-3263-9f2a-fc3a7b742849 | -3.89206 | -42.39369 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2d3e0920-fb55-3fea-a26a-315d8b1d52ac | -3.89152 | -42.39712 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| babcc52e-d09e-3f5b-8ac7-d3e2171856cd | -4.70494 | -42.66971 | 2024-10-17 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d203317c-a636-3644-8716-ba958d2adc0d | -4.70164 | -42.6692 | 2024-10-17 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d37d689a-da95-3b9c-8635-38c1f19b5751 | -4.48295 | -42.87077 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90290657-46b8-3b57-b6cb-909d21e972df | -4.48019 | -42.86682 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00e0e023-f52b-3789-97d1-f1390634c30b | -4.47689 | -42.8663 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94e7e20f-5f1b-3efe-88f7-b44138d764eb | -4.47635 | -42.86974 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6429cd28-a5a4-3607-9167-f4e6d252ce50 | -4.47581 | -42.87319 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4b0bd0b-8611-3ddd-831c-953512b61c4e | -4.47358 | -42.86579 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75474af9-730f-37d5-a958-982d7b3039fd | -4.47304 | -42.86923 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d6c8ea6-7c33-3a78-a447-e5fe5d2e7946 | -4.4725 | -42.87267 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5978ce11-0a5e-3b14-be99-c932e6345edf | -4.47196 | -42.87611 | 2024-10-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ba91e7a-6b26-35ee-96e3-cef2128072af | -4.49752 | -43.12381 | 2024-10-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91d0e3f0-59dd-30aa-9a71-16f02ca6bd9f | -5.96735 | -43.37009 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b9ed8c55-799a-338b-9e7a-f275c5f508cf | -5.96405 | -43.36958 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 536090ff-07f3-3958-9502-04df5958acf3 | -5.96074 | -43.36906 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 65d9fd7e-cd3d-3062-966f-a10be5c20274 | -5.96019 | -43.37251 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| ee0fb3b7-0d2d-339d-a177-cf8e4e12ff2e | -5.95965 | -43.37597 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| be01ea24-c27c-390c-8968-1ebe3789a283 | -5.94478 | -43.38426 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4b2e831-0a6e-38d5-9699-ff4f2ff11fb5 | -5.65417 | -43.00597 | 2024-10-17 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 580952bc-4d08-3275-b9c3-2301e0a62989 | -5.96681 | -43.37355 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29c38e87-3863-347c-b64a-aa47dbdfbf06 | -5.96459 | -43.36613 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2043cfd7-0f12-3c5b-b3b5-047aa53b126d | -5.89483 | -43.01216 | 2024-10-17 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a3ee18f-0e59-32d9-9dfb-faf30a2b2cd8 | -5.65639 | -43.01337 | 2024-10-17 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b4a340a1-3376-30dd-a3a0-79387de4b43a | -6.21231 | -43.28173 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03b3a799-c050-3ebd-96bd-780233c6539c | -5.07451 | -42.5651 | 2024-10-17 04:12:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5c84acda-6827-3977-aef0-6f368dfe8ce6 | -5.9679 | -43.36665 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 13af708c-93a4-3be2-9d38-0d51c4ab54d4 | -5.9635 | -43.37303 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb924f3a-4f07-3f17-a0ff-00750df74b0a | -5.96296 | -43.37648 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f23eaef-27da-3e9c-abf6-eeb9b668451e | -5.95689 | -43.37199 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 42e6c75e-86b5-314f-a471-57da5a75b2e6 | -5.95634 | -43.37544 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 0995ebb5-a563-3f27-966c-e91beb531ba4 | -5.94809 | -43.38477 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7ee96825-f8ca-38b7-bade-2be97c958047 | -5.65693 | -43.00993 | 2024-10-17 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b9feb457-5df0-3e5a-a46c-10ae08ede1c1 | -5.65363 | -43.00941 | 2024-10-17 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cfc5f3a9-df2a-3f53-9f72-df75bf0ec4cf | -5.65309 | -43.01286 | 2024-10-17 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e5c5b85-a29d-37a1-9cbd-22a091bbdcd3 | -5.96129 | -43.36561 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8846a05c-108a-3b76-bd54-e21b650dd727 | -5.95139 | -43.3853 | 2024-10-17 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 42751bf3-f635-323b-95c8-eb306dc0f589 | -5.32688 | -43.07834 | 2024-10-17 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14c36dd7-5e36-3172-a850-c6797e80dead | -5.22082 | -43.19242 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d01451ce-7b31-3abf-967e-c1df4784cedd | -5.21806 | -43.18845 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01a700dc-72d9-3dbb-94e7-18dba153871f | -5.21752 | -43.19191 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e38eb6d4-f1e1-3510-9e6d-8809c46f31f1 | -5.21476 | -43.18793 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbc321a2-a37e-3b82-b8ea-31e652a951aa | -5.21421 | -43.19139 | 2024-10-17 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f7cb046-d5c4-3db6-a6de-b5a7be340c4e | -7.73136 | -43.19271 | 2024-10-17 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 265c9ea1-e535-31d8-88d4-64d31e3c9786 | -7.18246 | -42.66166 | 2024-10-17 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aa944cd8-bd1e-39ef-898f-ce64fd083389 | -7.06483 | -42.63258 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be63bd62-0ebc-358b-ab64-affc40bcd5b9 | -7.74509 | -42.7785 | 2024-10-17 04:12:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a6f3ed4c-d542-3158-916e-3fd0f12b2217 | -7.18192 | -42.66514 | 2024-10-17 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| df7868af-9cb6-33e5-a2c5-26dc61614cd8 | -7.06815 | -42.6331 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2237fd3-b27a-36e3-84bf-bc781d96813f | -6.72208 | -43.56119 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 446cfe93-4d3a-3d38-94a9-6539d485147d | -6.69943 | -43.51146 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 074768a8-14f4-39bd-85c3-20801e1c7f0f | -6.68734 | -43.54502 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7db5a049-9ef7-3dfb-8452-9fdeb4bbd2d3 | -6.68294 | -43.55143 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7123b958-2b8c-3ee4-856a-65dfd7ff664f | -6.72539 | -43.56171 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e547b44b-78c3-31f7-8d91-7ead3d17b5aa | -7.19126 | -42.64878 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c8126e7-ac28-3e0b-8ef2-973be803103e | -7.19072 | -42.65226 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18babd88-cb92-3258-8441-57454096743a | -7.17915 | -42.66114 | 2024-10-17 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19395a7f-b768-3506-af14-69dfe2d23645 | -7.18794 | -42.64826 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d71716dd-a02f-38f8-872a-7d8cfd6bd61e | -7.1874 | -42.65174 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56831a31-9e83-3ada-b8fb-5529388ad554 | -7.14535 | -42.57371 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a61bf0cc-c336-31b2-bb11-0e61a91dc125 | -7.07254 | -42.62665 | 2024-10-17 04:12:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8142d6b6-1755-3726-a98c-debadda076cd | -6.88633 | -42.83965 | 2024-10-17 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0286e3e6-89f5-36ed-86c9-b1eab5cd8834 | -7.7358 | -43.2076 | 2024-10-17 04:12:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1461ea1-f321-31ff-ba1e-3e63d1dcd46b | -7.45455 | -43.18117 | 2024-10-17 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60730198-e29f-337f-a85f-5820b985bd9b | -7.19177 | -43.14653 | 2024-10-17 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f50aef9c-0ac4-3050-a225-85cb5d35c640 | -6.72869 | -43.56224 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23ae4b38-df8d-3796-bd6b-d1dc948d4b12 | -6.72593 | -43.55825 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e19fb8ac-07d7-3bda-b7b7-8cf6170036d6 | -6.68679 | -43.54849 | 2024-10-17 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96202567-f228-361a-87c4-9e0cf49801fe | -9.298 | -43.27288 | 2024-10-17 04:12:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a179853f-6bec-3ff8-a77c-06d9e12e7232 | -8.13755 | -42.89707 | 2024-10-17 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 21d43d8f-ab81-37ef-850a-b66b10ae00ab | -8.13424 | -42.89655 | 2024-10-17 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2dcba9e4-6cfb-3400-85fc-abeef8b45841 | -8.7157 | -44.01769 | 2024-10-17 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6fdc9745-b330-37c9-8fdb-416766276b54 | -8.71515 | -44.02118 | 2024-10-17 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20606ed4-8a0a-3102-9fc5-2aecd71e5a19 | -8.71349 | -44.01019 | 2024-10-17 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 40dd52ed-6b89-3acd-8401-292c97ea1902 | -8.71845 | -44.02171 | 2024-10-17 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98681cae-2e0b-32d0-8787-d93f9c82925f | -8.33766 | -42.78905 | 2024-10-17 04:12:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c724194c-b90c-35ae-8b87-7a8aeac64c7e | -9.29855 | -43.26939 | 2024-10-17 04:12:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2cc17d89-a9d4-3f59-97fa-c2544d0cdb65 | -9.28893 | -43.15684 | 2024-10-17 04:12:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1a2b594e-e7f6-379f-96e5-7d821d8aaac1 | -9.28839 | -43.16034 | 2024-10-17 04:12:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2774b1d4-a3a4-3048-b68e-17490aef1224 | -8.71901 | -44.01822 | 2024-10-17 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4691916e-1414-3644-9ce5-b118e766ccb9 | -8.71239 | -44.01716 | 2024-10-17 04:12:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da03df49-6bbe-3d41-8895-75ef04ce1f10 | -4.13327 | -43.08428 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a096914f-7336-30e8-8364-c740ee81be57 | -4.13273 | -43.08773 | 2024-10-17 04:12:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README27.md)
