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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d5292c5-8543-38f7-83cc-5313c853fd5a | -30.62741 | -52.66168 | 2025-10-25 04:25:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 1c2b1242-117d-35ab-8b62-91a122481b44 | -28.73933 | -49.11926 | 2025-10-25 04:25:00 | NOAA-20 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6d1deb16-c427-3c61-8eb5-415616445c2f | -29.10332 | -50.31908 | 2025-10-25 04:25:00 | NOAA-20 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e7d08189-c293-3f50-9ef9-a2895b173af9 | -29.84676 | -51.71547 | 2025-10-25 04:25:00 | NOAA-20 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 6f8e3c33-e505-34f8-89ba-607b2e700952 | -2.7964 | -49.136 | 2025-10-25 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| fa8967cb-045e-3021-9b36-b8939748b5c2 | -18.5634 | -50.2666 | 2025-10-25 04:30:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 54.6 |
| f5adc4b3-b8a5-3bed-9a1f-8374c4ea69e4 | -2.8149 | -49.1354 | 2025-10-25 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a434cc28-b548-3011-8118-9701b681e0b3 | -18.1714 | -51.7466 | 2025-10-25 04:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 6df85af3-07bd-3e88-b460-cea700abd6d3 | -14.8706 | -48.0822 | 2025-10-25 04:30:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 805eddf1-9d7b-33bd-8340-9d26f9b05838 | -14.8706 | -48.0822 | 2025-10-25 04:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f2bfd81d-d9b2-3381-b324-cb9cd5541d8c | -2.8149 | -49.1354 | 2025-10-25 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d68f7f92-7dd9-36a7-895b-482f7a9e7935 | -2.7964 | -49.136 | 2025-10-25 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e9efc85d-f4ca-3d05-9eac-03b0f83605ed | -18.1714 | -51.7466 | 2025-10-25 04:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 19f1b7f0-e5eb-3a47-aeb6-ecc872886e2b | -12.8524 | -48.6309 | 2025-10-25 04:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 21530f51-4092-3250-8846-d3811ef3bf7e | -14.8706 | -48.0822 | 2025-10-25 04:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0353a112-4b49-3b62-9515-a6362b95c933 | -2.8149 | -49.1354 | 2025-10-25 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3e9768dc-cbee-3374-bb73-ee450db87278 | -18.1714 | -51.7466 | 2025-10-25 04:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9800a5af-c580-3c0f-8e59-763081bbfd33 | -2.7964 | -49.136 | 2025-10-25 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 418b02cc-f4e0-3c72-b9c8-12bdb763cb4d | -2.8149 | -49.1354 | 2025-10-25 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f4e815ba-bf24-30ea-af5b-ec176668913e | -2.7964 | -49.136 | 2025-10-25 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b0b1cda0-2959-3dba-b6e0-74a23e9cb9f9 | -2.80327 | -49.13887 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 7f6018c6-5a2b-3a1b-ab74-d4463cba8f5e | -2.72567 | -49.1613 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2785573-64b2-3b09-bec1-4afbe1b8bbc3 | -2.26394 | -47.85764 | 2025-10-25 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b537c06-fd8f-3de5-bf40-335601621100 | 2.0782 | -55.72017 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd4f5213-884c-3156-8dee-55546af7f129 | -3.12199 | -49.1095 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3bd106b3-f92e-32d7-887f-ad9e5eb6ffe6 | -3.10189 | -50.19978 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a37cbcf4-bedc-30ce-8d9b-1ce094b9ab3e | 3.88622 | -60.1268 | 2025-10-25 05:08:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f313280-2d07-39d7-9670-2647192aa878 | -1.81589 | -57.10773 | 2025-10-25 05:08:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb6b7cc9-f329-31ae-b7a9-a6973cc2155c | -1.3021 | -49.33585 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc646826-3047-3866-a718-b0120cd79ae3 | 0.37048 | -50.85659 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d38577a6-935a-3f3c-8dab-7882a4437651 | -2.73036 | -49.16205 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 71f47c70-a91f-34b6-aad2-f184e6ea3acd | 1.63339 | -55.74827 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e33be01d-70d9-3d25-803c-752a9a0e870b | -3.13701 | -48.62325 | 2025-10-25 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce23c637-9e9a-3a87-a8bb-2a3739946f7d | 1.63285 | -55.74485 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f2623a47-0921-3022-94c0-8bf5cb030255 | 1.68345 | -55.67333 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 465c892e-d233-37a3-8313-7c40095ecc10 | -2.80798 | -49.13958 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| c66ae419-3389-3805-af32-5869b35c84a8 | 1.55595 | -55.99216 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 772a9bac-b080-3cb0-846a-e51097b24cb7 | -3.12078 | -51.21354 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c7e69c1-5709-3df2-97b6-d7fc6d67083d | -2.85864 | -50.74149 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 916b5c92-4344-350f-a10d-ad44bc2b2fa0 | -3.58418 | -44.87492 | 2025-10-25 05:08:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78851332-d7d6-3022-96f4-5d0a30f5ee93 | -2.8127 | -49.14028 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b838bf6f-cc91-3221-a982-36466300056b | 1.64886 | -55.71785 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46fe421c-f9d0-3afa-972f-dd973e5396e0 | -2.26536 | -47.84842 | 2025-10-25 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3bf8dbd-5c62-3e21-8e8e-6f69655d93df | -1.78577 | -54.00118 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11b69e3b-715e-3564-b8d5-8d9e16708a3e | -1.3038 | -49.33398 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4592fe2-1d09-3ec2-9a49-5ffe33e435e8 | 1.55649 | -55.99559 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8f608d6-84ce-30b2-882c-32c898710f08 | -2.26695 | -47.85813 | 2025-10-25 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cd12432-7328-3fd9-99ff-400b660076ea | -1.30065 | -49.34502 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c76b72eb-8184-35bb-9412-ee23a0b42c7a | -3.58083 | -44.87445 | 2025-10-25 05:08:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2e26f04-5a89-3299-b1f8-47bba99f4fb2 | 0.37367 | -51.00384 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c862e3b2-095a-3275-918b-ceffab619129 | -2.603 | -54.23122 | 2025-10-25 05:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9e2b623-7fa0-3b25-8772-e8b28bb73210 | -2.77265 | -48.0179 | 2025-10-25 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 682d1ef6-2584-33a8-8dfe-c666924a9abd | 1.68621 | -55.6694 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7faa9d24-eb71-34d0-839f-2bb9b21b7c1e | -2.80723 | -49.14452 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2f65ba1f-1ebd-346f-8a55-fa2d2afa7a99 | -1.59468 | -54.30496 | 2025-10-25 05:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae0b72f9-c22a-3407-840e-16c9658081c3 | -2.73886 | -48.68798 | 2025-10-25 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e290270-4584-3672-a670-484dfc7507a1 | -2.94848 | -51.52777 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43d3a576-5ef6-3c69-a831-262b7da7d84e | 0.17768 | -51.39535 | 2025-10-25 05:08:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e9fecef-bac5-305e-beeb-2a9d4924b866 | -3.13429 | -48.6245 | 2025-10-25 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b85e709-0ac1-38ef-84f3-0fa5d8219ceb | 1.63507 | -55.7375 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2bb1be04-c943-3503-94e3-57ad8fa112b9 | 1.6461 | -55.72178 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 805d2a89-b836-35a1-8d83-9df04fa58a39 | -0.70381 | -50.35632 | 2025-10-25 05:08:00 | NOAA-21 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02fe2096-3623-3238-8b8f-31a9d9312759 | 0.36972 | -51.00446 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6108ce1-37a3-35e6-85cd-0861e6cbf68a | -3.15274 | -50.45912 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64ccfb6d-60a7-3857-b8da-c6a13133a551 | 1.55925 | -55.99165 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa9536fd-f741-3afc-9c60-00784fbdc54b | -3.14568 | -50.62032 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06dddcf0-cbb7-34ca-bb2b-3457a12e35c5 | 0.4741 | -51.00231 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7803b65f-8dd1-3977-ac2b-30e94e5f39ea | 3.13794 | -61.00784 | 2025-10-25 05:08:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 980e6a35-e562-3595-bf61-c7f79dbb66c5 | 1.63783 | -55.73357 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2570e290-a04d-3449-9d69-9f0f9fda99df | 1.62282 | -55.78848 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ca0e460-e411-3e60-a7db-d29f5008a397 | 3.42023 | -51.51546 | 2025-10-25 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abc2f890-c2c3-3369-8f96-668630e32755 | -2.87004 | -50.72319 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d49f7048-a39f-3973-a762-48b4af3817bc | -3.26256 | -50.1503 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e93bdeed-26d5-3770-a530-887364793707 | -2.86945 | -50.7271 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3db5672-ae63-3e0e-96b9-911d4c2fd355 | -3.11724 | -51.2092 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d32f32ed-417b-3eaa-b718-9536d1d40de7 | -2.86581 | -50.72255 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a70ba0c6-267c-308a-95b9-1df9c210ed67 | -1.51513 | -55.85732 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd2e16a9-fccf-398e-b7ce-052750fefee5 | -3.15225 | -50.16564 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f0e9251-8936-3fea-94cd-3f8f61d7295c | -2.79062 | -49.59723 | 2025-10-25 05:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38dc5be0-db14-3d6d-bc86-b822728f6d60 | -2.26583 | -47.84535 | 2025-10-25 05:08:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0dd3dd5-9bf2-3547-8b68-944abc04fdab | -1.92586 | -52.14023 | 2025-10-25 05:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2621d888-3472-36a4-9eb0-ef7d8ce66cf6 | -1.30311 | -49.33857 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0d13f53-d33b-3edf-9a20-bbd34abefdf8 | -3.11799 | -49.10378 | 2025-10-25 05:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b068a7c-72b3-3d50-9841-3aa5262bd01a | -1.41568 | -49.40032 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bafc77dd-c2e1-3850-9998-1cb08eb3daae | -1.30173 | -49.34777 | 2025-10-25 05:08:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8831fdd5-8867-34f1-a293-ba13548583e8 | -2.12682 | -56.84143 | 2025-10-25 05:08:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0f4218d-72d1-3eb8-81e0-7b855df13e66 | 0.37069 | -51.00598 | 2025-10-25 05:08:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1aa4ceb5-afa4-3be4-870e-1da1389ebf42 | 1.63232 | -55.74143 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1421302f-4a93-3ad2-b60b-96ccbddfad15 | -2.86345 | -50.73823 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6acff44b-df86-3d73-942c-cb2d4d1e76f7 | -3.10125 | -50.204 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f3ead09-b8b2-3eb7-adaa-61a3dd6e9b6b | 1.63063 | -55.7522 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3b6fe5d-6307-36e3-b8c0-bc55c2c760df | -1.60719 | -53.86308 | 2025-10-25 05:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33180bf3-6363-30c2-aef0-275772a487c6 | -1.67342 | -55.17016 | 2025-10-25 05:08:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db825904-04ea-320a-b37e-8d67ae391bc7 | 1.63837 | -55.73699 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6ff9c969-fd43-30d7-98dc-e5c1a8c4ef31 | 1.54767 | -56.00399 | 2025-10-25 05:08:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f70db71a-23be-3f21-9a7a-8837d770a958 | -2.8944 | -48.06272 | 2025-10-25 05:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f48a920f-f9d4-3329-989e-ab3ae52f9945 | -2.95197 | -51.53187 | 2025-10-25 05:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ac65aab-1760-3819-b88e-9d9100f31196 | 2.07551 | -55.70302 | 2025-10-25 05:08:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a333350-b0c9-3ad6-b33b-904c4c4822f5 | -2.26899 | -51.92739 | 2025-10-25 05:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d2fa2f4-65c8-327a-8a7e-13bd5b47cc37 | -2.73641 | -48.67112 | 2025-10-25 05:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README50.md)
