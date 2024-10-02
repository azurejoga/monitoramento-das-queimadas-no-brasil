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

## Dados Diários - Página 179

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 440ae4d7-f986-360a-82bd-864b3f484922 | -16.86353 | -55.85307 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 127f52cc-66b3-3e71-b0eb-4f730c08cf88 | -16.86323 | -55.83612 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 48c0f3c9-c63d-3435-94d0-7c521a252287 | -16.86283 | -55.84003 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a49d4206-7d8a-3419-9c50-7c46bf033b9c | -16.86242 | -55.84393 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9e86c626-46cb-38f2-91e8-d11f766c68b5 | -16.86201 | -55.84782 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4afb6d13-550b-37c7-af9c-408133293564 | -16.86161 | -55.85172 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 33cfe50a-5b49-3964-bec0-1897d0a614ad | -16.86008 | -55.83294 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 48cac843-46c5-3415-ab37-f5ee5d617136 | -16.85965 | -55.83685 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d8a7746e-0b61-3d22-9a4f-6b22a438dbdf | -16.85879 | -55.84464 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 94da667d-8a67-30d6-89a1-dd0e164f998d | -16.85835 | -55.84852 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 48de26aa-c6af-3951-b685-b69567651ea6 | -16.85802 | -55.83153 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2d15416a-271c-35c9-b6bc-5e026c0cf508 | -16.85792 | -55.85241 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 52d7a868-5811-3e77-a0d4-5db646d2d04e | -16.85761 | -55.83545 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0721a0a5-b9be-3784-a517-63332aaa7610 | -16.8564 | -55.84714 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b71f20af-a9ef-354d-9131-160ff644cf10 | -16.856 | -55.85103 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 688ae308-954e-3504-b87f-174b083cca4d | -16.8549 | -55.82839 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8acce93a-8adf-3e4d-b27a-41731734d517 | -16.85447 | -55.83229 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 42fc1e84-cd4c-35c8-b45c-11503c5d3011 | -16.85403 | -55.83619 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6aac503a-bcf1-36d7-99e8-ce857d0b29e9 | -16.85317 | -55.84397 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c26ed092-2f44-3800-ab5d-269e48acfa58 | -16.85274 | -55.84786 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 36f04320-6d02-3b5d-a0e0-72c474ba7de2 | -16.85231 | -55.85175 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 38fc10fe-10d6-3546-bd62-235803436886 | -16.85199 | -55.83478 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5d2bb106-aff3-3401-affd-6c1e016ef60a | -16.85038 | -55.85036 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a3fb0160-3c8e-3720-ada8-5321b73ac6c8 | -16.87274 | -55.90792 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2258138e-28e7-3f5e-8b2e-6f7fd93facec | -16.86836 | -55.89568 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 74420e3d-568c-334a-8222-7f85d0696ed5 | -16.86714 | -55.90727 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5c843a83-8f2e-307c-9d01-74cdb1b8cce1 | -16.86673 | -55.91114 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 19c5e872-ac69-3660-805e-d164fe205cec | -16.86438 | -55.89626 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 93a335ac-cd49-3de4-80e0-197a5c708a98 | -16.86308 | -55.90784 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e913d566-7998-3dde-ac45-310cf37f5c44 | -16.86276 | -55.895 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b6a4612e-219a-3d1e-9a12-bcdbc9d6a8fd | -16.86265 | -55.91172 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 565b4e5a-10d3-39eb-95c4-d0a27ae3cc84 | -16.86195 | -55.90274 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f5259f5c-5e0d-35c6-a881-71dbc0ee71a2 | -16.86155 | -55.90661 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5f86982a-421a-333c-addc-1eee0b76d4db | -16.86114 | -55.91049 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 62c7bfe2-48a0-3d15-8536-5b5dc8b7b6f5 | -16.85878 | -55.89563 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d784ea19-b1b1-38b8-98d0-8e6503ea7704 | -16.85835 | -55.89948 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 528de87b-141f-3f1a-aaf7-b3ebee5d9452 | -16.85792 | -55.90334 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 345c2f8d-65a3-31d1-9ddc-a484f0df278b | -16.85749 | -55.9072 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d9f795ee-eb3a-3030-9873-1a72517841f9 | -16.85716 | -55.89436 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 00fd56c4-a732-3da1-81ea-02a314d4a409 | -16.85706 | -55.91105 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 56eefd62-1095-3a14-957a-8eab7c080885 | -16.85676 | -55.89822 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9bb124fe-07a6-3e2a-86b4-bf8734288d70 | -16.85636 | -55.90209 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2913488e-737c-31a7-aae4-5257bc761c72 | -16.85595 | -55.90596 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| be90b959-c884-353c-9e33-615e937ec955 | -16.85555 | -55.9098 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f982796f-85a4-3081-ac0c-5d0d1e600039 | -16.85362 | -55.89112 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e5d63000-bcf5-3e4a-9d1a-8b74c6a6899b | -16.85319 | -55.89498 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 051d064c-f4df-3632-87e4-efbcb1014a6d | -16.85276 | -55.89885 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fcd52b6f-15ae-3156-b83b-1f01379ebcd5 | -16.85232 | -55.90272 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b840a52-24a0-399a-929f-eee264150878 | -16.85197 | -55.88983 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ac67eeda-a4b8-3fcd-8e19-6db64cbe1c2a | -16.8519 | -55.90656 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a1ba2c4b-a447-3ebc-a26f-7119b52cfce7 | -16.85157 | -55.89368 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6061c85b-def4-3c18-afe9-555234fec4b6 | -16.85147 | -55.91039 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f1070f83-a616-32b1-baf7-2252bc77378b | -16.85116 | -55.89756 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 09e14ff6-3e9b-31ea-9b43-b4211407bc6c | -16.85076 | -55.90144 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6d6296e8-31c6-38cd-9d7f-6bf685c25247 | -16.85036 | -55.90531 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fb96b72f-abe0-3e15-8d07-f047f0efa431 | -16.84996 | -55.90914 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5fc0cf0b-8c65-3c24-a428-bf40aac6f035 | -11.49086 | -56.79459 | 2024-10-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1093a940-174f-30bb-8387-8738193f9f87 | -11.48595 | -56.79393 | 2024-10-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a5b2df76-808d-3a5f-a220-e614647bcd7e | -11.48249 | -56.78216 | 2024-10-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a231a04a-e5ed-3401-8423-299f52efe664 | -11.48177 | -56.7877 | 2024-10-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dc61a988-5add-3622-9660-ec8c1788d29b | -11.32871 | -56.23791 | 2024-10-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2a0e75d-53d6-353d-9313-4267ea66eafd | -9.00028 | -71.57914 | 2024-10-02 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bf47583-981e-3a53-ad70-c0637fde2611 | -9.02079 | -71.58405 | 2024-10-02 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 834c1e25-c56b-33e6-a0b0-cb12d56bd2e1 | -10.93483 | -69.75508 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00d29ac6-40e7-3de3-957e-9536fb0d6e07 | -10.93544 | -69.7515 | 2024-10-02 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd9159c8-679a-39ed-ab8e-5fc211e77f1b | -10.07749 | -69.16709 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccda5ad7-8552-38cb-9e53-716b1a3cd9e5 | -10.11363 | -69.25996 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2e9db6f-499f-3444-9d6e-ef973b2c7067 | -10.30301 | -69.1897 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b00f0ff7-034e-35f9-b24b-992bac1e533d | -10.30324 | -69.18689 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddefde7f-8b9a-35e8-9970-0b2c3d21512c | -10.30716 | -69.18758 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e604c12f-d8e2-3cca-ba11-c8f9d401cb31 | -10.41147 | -69.16663 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da9d1ae0-364f-3e11-ad4b-6c7241fa492c | -10.41185 | -69.16478 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bc2545e-3045-3a06-8ffc-7f091fa6c332 | -10.42706 | -69.21604 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 091b97d5-8159-36b7-96d1-12d25a3aeb8c | -10.44969 | -69.51138 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a063eae3-6a00-3f6c-b609-5b0a88723e4d | -10.45029 | -69.50786 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83319b9e-bd8d-358e-8cb7-095a1a19deb9 | -10.45492 | -69.1949 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18eba6dd-0ed4-3da5-8054-edef133927fb | -10.48596 | -69.50278 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 095914a7-551c-3d6c-938c-da64d193f4cc | -10.48658 | -69.49925 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a503db0-cdb4-3589-b429-41fef52cd5fc | -10.53401 | -69.32035 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 853c0ab1-f5a0-3a3b-aaa8-c007a0e68018 | -10.53489 | -69.31527 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3685b82e-b16e-34dc-b9cb-c8d7eeeb756a | -10.53795 | -69.32104 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20309070-e38e-3af2-898e-e697e6cf895b | -10.53883 | -69.31596 | 2024-10-02 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b93ab8e-9179-34f4-9180-086b3d3c547e | -11.32833 | -56.24091 | 2024-10-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 49054e23-4945-3533-9352-36e69db2b764 | -11.32323 | -56.2403 | 2024-10-02 05:36:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 947e9f28-8843-3148-b9fc-892fa679e61c | -11.82581 | -56.84464 | 2024-10-02 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec953c30-c122-3269-9c7a-2763675dd7b2 | -11.82508 | -56.85019 | 2024-10-02 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec0b36aa-92b9-3f7d-ba5c-c4462f37b2ee | -11.82284 | -56.84417 | 2024-10-02 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3906a421-013a-3eca-bf75-05a4a50361b9 | -11.77247 | -56.31482 | 2024-10-02 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76b7959c-46a7-3687-bb66-c6542e14c8b3 | -15.79601 | -57.3519 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff69f1b3-7009-3226-8dd9-ec1fb4485048 | -15.79564 | -57.35493 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 120292c4-f717-3a49-85ef-e857d4f9172c | -15.79484 | -57.36171 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7467400e-fb60-3a91-b369-d18cdde1cbe1 | -16.50943 | -57.32999 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 81ebc126-f699-3865-ab3c-f182d90ec523 | -16.50401 | -57.33242 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1f51ff2e-e02b-3509-a7be-bf44c3febd00 | -16.49929 | -57.32872 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e8c9ae50-5700-348c-a8ae-3828acb370dd | -16.49388 | -57.33114 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 91719874-87c7-37fd-bbab-2c0138bda3cd | -16.49353 | -57.3342 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 465d451e-545a-3bdb-83ca-e16ef77d19a9 | -16.47186 | -57.35549 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4da262c2-c3a8-3dd8-b790-2b968852ddac | -16.47054 | -57.35602 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c9c0b741-d049-3bf6-89f6-fb9ee726be67 | -16.4668 | -57.35483 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 328bca06-fcc0-3c8f-b78a-a63ddad32047 | -16.46572 | -57.36395 | 2024-10-02 05:36:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README180.md)
