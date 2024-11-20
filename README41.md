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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ea20b26-63e3-336d-a7b9-0fe475b08703 | 1.53824 | -55.91966 | 2024-11-20 04:48:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6c9c610-65fb-30c9-b833-094204288529 | 0.04828 | -51.46068 | 2024-11-20 04:48:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9bf4535d-9f35-3f10-9c46-3d795a52fc54 | 0.14452 | -51.21269 | 2024-11-20 04:48:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 267d9555-18b7-3db0-b319-b56dd45c948b | -0.19229 | -51.62964 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c65d808-99b6-3d1a-a71f-dec3a669bf96 | 0.12292 | -51.05387 | 2024-11-20 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| add5a5ec-fe2a-3c6c-8035-b0629963444d | -0.08528 | -51.47437 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28b7d9b6-1f39-3a8f-ac02-64ccead4b2d7 | -0.89106 | -47.87253 | 2024-11-20 04:48:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c979944-0d48-3706-bc53-afd3442e4284 | -0.1143 | -51.43629 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 830025f0-aecb-3e0b-b728-f5a55b034c62 | -0.18564 | -51.6286 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a8424f2-36e3-32d9-9ef8-5bf3dc13a2d1 | -0.27982 | -51.44144 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a304649-66ca-331e-ba89-b309d08564a3 | 2.40454 | -51.63783 | 2024-11-20 04:48:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eb9b85d1-8090-35e7-b1e0-2ce4c5afb2b4 | -0.19562 | -51.63015 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60d066d8-e473-32ef-8732-ec702d5e3ba3 | -0.09819 | -51.40904 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fe1f30f-8df7-3f89-8307-bb8560a4824e | -0.39888 | -51.5447 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66973e10-b631-3744-83f4-ccafa314148a | -0.36143 | -51.60968 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bd9cd04-01e5-313e-8475-55f8694f80c0 | 0.37012 | -53.81375 | 2024-11-20 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abbdf6d7-43ef-3662-b970-fb8bf554c31e | -0.09558 | -51.40878 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61d0da35-9a65-3ea2-b833-7387edacae01 | -0.32747 | -51.76063 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62334599-896e-3e2e-a732-49e0b77d5766 | -0.03353 | -51.11333 | 2024-11-20 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 793624f7-5e05-3f8f-8389-47310e8c69d8 | 1.11932 | -52.59066 | 2024-11-20 04:48:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ede389c8-81c8-3b94-b4be-0ed846d75ec7 | 0.64519 | -50.73611 | 2024-11-20 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 304ce1fc-7b49-38c3-981c-61cf4c778112 | 0.69499 | -51.44145 | 2024-11-20 04:48:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21222432-874d-31b9-80e3-556404454858 | -0.19531 | -51.74022 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bba2d58-6a07-3510-b2a5-2749088f3808 | 0.61429 | -51.77115 | 2024-11-20 04:48:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e202c2d-ceaf-33ff-a06e-32ed12bdfcc4 | -0.11098 | -51.43577 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4dee48b-e2cc-3445-be31-f0b2aa9defed | 0.37077 | -53.81783 | 2024-11-20 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66e2309e-07a0-32ae-845d-25cceb92e15d | 1.5347 | -55.92391 | 2024-11-20 04:48:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6ed89b6-32d8-3f05-877e-fe8c0cd5ceed | -0.33686 | -51.7443 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b939fdf5-0598-3e5f-80af-182f9d4ae790 | -0.30868 | -51.55544 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6b3d923-beec-3131-a274-d1a210bca8eb | -0.29703 | -51.54301 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdb1d603-3149-3188-a379-fce13d69c780 | -0.29439 | -51.50026 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95aeb5f9-acec-3c78-8559-3834689ff4c6 | -0.03299 | -51.11678 | 2024-11-20 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58b92699-017a-35e8-95ee-31c29cff0050 | -0.13415 | -51.61288 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13bfa1f7-2830-3786-a6ca-8bb5a73c23da | -0.18842 | -51.63258 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 001b30a4-fcb4-3033-8825-757c8dbbbbad | -0.79906 | -47.79461 | 2024-11-20 04:48:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ba9a85a-29ea-3ea3-aff1-e03cf578c7f5 | -0.27746 | -51.39162 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b349741-e545-30e8-b9be-f3bfb66b143c | -0.27691 | -51.39506 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e42aaf5e-033c-367e-a3c6-6a6eebfa8048 | -0.19175 | -51.6331 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a167e16-7747-3d71-988b-3fe5e5043be4 | -0.03671 | -51.329 | 2024-11-20 04:48:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b9d6d6a-8e91-358f-bf51-2c405a397ce2 | -0.18286 | -51.62462 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3fd0532-f151-3849-8b25-ef6c940684f2 | 0.14784 | -51.21217 | 2024-11-20 04:48:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c35f068-afd1-325d-9007-cdda55842010 | -0.34923 | -51.4062 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1260097-cd8b-3613-a607-9f20f5e4e630 | 1.01775 | -52.27484 | 2024-11-20 04:48:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7531d75b-24a6-358f-9b28-12132004e4e8 | 1.79149 | -50.42954 | 2024-11-20 04:48:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5150893d-2114-3e01-a077-d4c436c48e06 | -0.27928 | -51.44489 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1b51845-f6f4-388a-b7ab-71d54416235e | 0.0439 | -49.50675 | 2024-11-20 04:48:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3821a7e-1fd7-361f-a9d8-35bfe1f5f40d | -0.18673 | -51.62167 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d177eac-4efb-3c79-bdd9-980db72f30ea | -0.0431 | -50.81522 | 2024-11-20 04:48:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4cb5af6-d596-339e-98b0-f2dbf0f8fc38 | 0.63944 | -50.57426 | 2024-11-20 04:48:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c90d1d23-3ad2-36eb-992a-110ece24c1c6 | 0.63686 | -50.57513 | 2024-11-20 04:48:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4849e737-fe5d-3334-9dc9-e43b17eec1cb | -0.19271 | -51.39194 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85b315da-eeef-3d78-a2c6-05112037657c | -0.27852 | -51.55797 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a888b1-36bd-3ca9-aa21-7dedcaf1a4a7 | -0.24679 | -48.58872 | 2024-11-20 04:48:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc391ad6-1987-3d3d-9c65-6b718a079ab3 | -0.33999 | -51.46482 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6955993d-8b80-3c9a-9abe-bd622d307332 | 0.61484 | -51.77464 | 2024-11-20 04:48:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| abcf2945-59e7-3ab8-8601-6a601e0fa3a7 | 0.03518 | -51.22604 | 2024-11-20 04:48:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 297161b1-c61f-3d36-9bf3-85ead3866fb0 | -0.08304 | -51.46694 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64799121-03ab-3368-a0b9-4bdf73b81c1c | -0.18619 | -51.62514 | 2024-11-20 04:48:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0080bec-b0b1-3a48-8589-7f48a4db494c | 0.1473 | -51.20873 | 2024-11-20 04:48:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 086fb78b-f592-39dc-bf28-28fe22ca3b30 | -0.79539 | -47.79403 | 2024-11-20 04:48:00 | NPP-375D | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 301ed76e-aa5c-3ea6-a0d3-67c274e9605e | -11.1109 | -54.6204 | 2024-11-20 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| edd4e000-c711-34a2-853e-909907de3718 | -2.9115 | -53.0809 | 2024-11-20 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| efe349d2-77bf-3903-b9d7-75cd183ea04f | -2.93 | -53.0601 | 2024-11-20 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| adebe42b-51ee-3c86-9ae2-d3dd8ef0940c | -2.9116 | -53.0606 | 2024-11-20 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 688a3303-81d9-3e62-aef5-de48606baafc | -1.2017 | -53.6769 | 2024-11-20 04:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 31758ad4-1c13-375e-b9bf-147d6a8c4051 | -2.9299 | -53.0805 | 2024-11-20 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f7986d1e-7e4f-31ad-bb8e-011510013fa0 | -2.75 | -51.8377 | 2024-11-20 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3d7a5d42-3035-3bbe-b118-f14c314da95d | -4.4592 | -46.5745 | 2024-11-20 04:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3b3da08c-c7fc-3b28-884f-3a0f69449596 | -11.092 | -54.6221 | 2024-11-20 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 7dd0e354-46b0-33df-93c8-ab43b1942bfa | -2.7501 | -51.8171 | 2024-11-20 04:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cd623ea8-8d05-31f7-8c8b-1be50fd9691b | -11.1106 | -54.6408 | 2024-11-20 04:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 929a9dc0-b63e-3e05-8fa4-beef307f3eea | -4.4405 | -46.5754 | 2024-11-20 04:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| bfd9b875-aa57-32eb-b21e-6dde95760dbf | -2.7217 | -49.3508 | 2024-11-20 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 4fad5761-92fe-3b3a-9f49-e0e6877a948e | -3.48502 | -54.69969 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8309cce9-7320-3564-8aed-47ec8a6b44c0 | -3.85843 | -54.08241 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5cbe95c8-bb59-3c37-97a3-81e12f7a6c27 | -3.91004 | -53.82452 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5587c694-cca7-361e-88e4-5a1d0cba4d12 | -3.81928 | -51.35475 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e54d67ea-4ff8-3586-b5dd-e36104a12d88 | -1.48291 | -51.1282 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17278173-31c7-350d-a3d3-ea5c4856e2fe | -1.62525 | -52.59137 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9816be5c-9126-3fe0-8c2c-29d9f63d0e54 | -3.31338 | -54.17651 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f647441b-6210-3e8d-b095-ceb10410870c | -1.13832 | -51.68163 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f5902fa9-ff89-3c6a-b931-f63c3712411e | -5.69524 | -45.84818 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a521a3b-a9f9-3d85-94c1-bfaefa62b4e8 | -1.20935 | -51.74931 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49fe3b08-7ac8-3a06-ac42-dc3ab97fbc21 | -1.47465 | -51.13751 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a1c7524-60b6-3b90-900c-dd03893d0697 | -3.51315 | -50.22572 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c15b586-e8f1-360b-a618-ca0a782ea862 | -5.96644 | -48.06084 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c218d547-dfea-3424-b1a8-98b6bf246c10 | -1.21376 | -51.74291 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b53f28e0-a32c-3637-8de6-415eb65daddf | -2.4652 | -48.94859 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6c0c909-1893-3baf-ba68-3bfec2ae3e9f | -2.26668 | -48.44704 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b586f1-3246-3c1a-a05f-0f1f1554a930 | -2.766 | -54.05354 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c06326a0-437f-3208-bea0-80c3076f7f9d | -3.11203 | -53.70163 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb5b0565-8418-363d-af18-68501c286b67 | -1.7101 | -48.02082 | 2024-11-20 04:50:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8d6f3a5d-99e1-33a8-a861-ed0dc4e7d704 | -5.38038 | -50.47347 | 2024-11-20 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80b5bc64-3405-353e-be9f-e454afd899ce | -2.75028 | -48.57352 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ccf282e-3965-3830-9a30-9878038ddaa0 | -1.20091 | -46.5364 | 2024-11-20 04:50:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6db8b909-9093-3bd4-939b-56db1202e037 | -2.28226 | -50.58814 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e7f2a3b-d90e-3f76-ac77-62a7d589d3e2 | -3.28767 | -53.83279 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65bbfa83-c18e-3183-9fc1-11927c6db09d | -3.30677 | -50.36411 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d36e454c-c77e-34c2-b6a2-bf69283837bd | -1.20439 | -51.75916 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88c3b3e2-e820-3e2e-bc6b-0a3c35e7b2ba | -3.54744 | -50.27504 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README42.md)
