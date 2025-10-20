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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6a3604b-3275-3c45-8c82-d523dd94d402 | -3.1514 | -49.51451 | 2025-10-20 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 16cd053a-d3e2-369e-9d1b-dc52066b20ec | -5.09174 | -42.75239 | 2025-10-20 00:35:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ce4c16b3-2498-3a6b-a4cd-5b5f59c6f228 | -8.3457 | -46.22877 | 2025-10-20 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8a19cef4-952f-35ad-86a4-cf7334554ab3 | -6.1732 | -47.86102 | 2025-10-20 00:35:00 | TERRA_M-M | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e67a3bb0-7041-34e5-aea7-ec7751dcb050 | -3.04184 | -48.73152 | 2025-10-20 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b2682620-1f50-3487-afce-af385d0faa49 | -4.40037 | -43.31779 | 2025-10-20 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.9 |
| a5ac3279-2832-3df6-8d77-0182e1bf4301 | -7.85356 | -49.65607 | 2025-10-20 00:35:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 60eb9611-f956-3469-8c96-caf451c10aec | -2.91814 | -52.70939 | 2025-10-20 00:35:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| b55319cd-0381-3652-8e7e-7a9e39f3df42 | -5.08793 | -42.77067 | 2025-10-20 00:35:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 840ee5dc-7399-30ca-80c2-cb81ff64e676 | -7.13053 | -44.2407 | 2025-10-20 00:35:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d2ee848f-c40f-3b40-9c7f-8fddd071b921 | 1.16997 | -51.26367 | 2025-10-20 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7caf1d1e-fe7f-34db-86f1-e72cf1b6a8fc | 1.11732 | -51.10722 | 2025-10-20 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96b20123-e724-317c-a011-71f721fa97ce | 1.08066 | -51.30735 | 2025-10-20 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.6 |
| fbeb9965-be48-3ca0-9375-70e346ba3d84 | 1.08187 | -51.2986 | 2025-10-20 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 24c0f6a1-99a8-3c46-a2f7-928505246524 | 1.72312 | -55.95283 | 2025-10-20 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 7a253bd2-20aa-32a7-9bcb-6e9140f9ae1e | 2.03774 | -55.76309 | 2025-10-20 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ef6ce39f-c25e-37b3-a793-8b3d232086e9 | 1.72108 | -55.96689 | 2025-10-20 00:37:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 35e7bef7-4991-343e-8219-d8578a31bde3 | 0.98127 | -51.14734 | 2025-10-20 00:37:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e9c39f31-05f4-3aa2-9789-f0cf54c30047 | 0.65642 | -51.43194 | 2025-10-20 00:37:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a7eebd65-c437-3893-9357-81f15c1a4bef | 1.51263 | -50.78332 | 2025-10-20 00:37:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ca128b7b-a1d8-39ea-be37-7279e511f46c | 1.7121 | -55.77558 | 2025-10-20 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 96de5136-4abc-33cd-a09e-0f19fb07044a | 2.1486 | -55.78453 | 2025-10-20 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| e6e2c1cc-be57-3fa8-aea3-67e164fa2e8a | 1.78051 | -55.70778 | 2025-10-20 00:37:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b7facf9b-afe3-3a07-a254-28d8a2175539 | -2.2527 | -51.9108 | 2025-10-20 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 3b636ac0-5faa-369c-967b-19c1ad3f0d05 | 1.0763 | -51.3099 | 2025-10-20 00:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 71f4a01e-62b0-3140-8cca-dbd0b3614ea3 | -16.1581 | -49.9802 | 2025-10-20 00:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| f4506c59-0d76-3eb7-9863-34089195fa68 | -2.2527 | -51.9313 | 2025-10-20 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 3a03a2fe-889b-3f51-90ed-740837a24dc6 | -8.0676 | -48.0112 | 2025-10-20 00:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| a7d87723-7287-3d55-9f4c-65ab099bc7c6 | -10.0201 | -47.0637 | 2025-10-20 00:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d103ffa9-3db6-3218-b940-c82bdf45fe0e | -7.075 | -46.197 | 2025-10-20 00:40:00 | GOES-19 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| d0b72ef6-1108-3a8a-9dd2-a413d9b4c036 | -3.3279 | -50.2195 | 2025-10-20 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 0a2fdc60-5073-39d9-9ca6-b8a4be93e217 | -2.2343 | -51.9111 | 2025-10-20 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8f033438-2647-3280-9976-866a9b16d69b | -2.9128 | -52.7146 | 2025-10-20 00:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 0e26b681-3730-3974-82be-3239314f54e3 | -10.0204 | -47.0414 | 2025-10-20 00:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8b87a31a-a9ac-31c0-a661-7d022304ff5e | -9.6401 | -64.7411 | 2025-10-20 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| eca434f3-5f9c-3d10-af69-4b4d59025a6e | -10.0014 | -47.0435 | 2025-10-20 00:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f2f25f3f-e37c-34eb-b632-a9cb1e7d775c | -4.4066 | -43.3118 | 2025-10-20 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3607768e-16c1-317c-9271-da2c0c1ccfd5 | -10.0011 | -47.0658 | 2025-10-20 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 054aec3d-b92b-34ca-b933-09c12717662b | -9.5534 | -40.3254 | 2025-10-20 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 03881ef5-a3ba-38a7-b311-46da001e43f2 | -3.3278 | -50.2405 | 2025-10-20 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 5ccd1b4a-f71a-3040-a65e-d53fde70c858 | -10.0204 | -47.0414 | 2025-10-20 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 0db7f56b-6fc0-3976-a250-bbc2669282e4 | -10.0014 | -47.0435 | 2025-10-20 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| a46240d0-1e50-382b-91bf-911cc5aa89f2 | -10.0201 | -47.0637 | 2025-10-20 00:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 78a7293f-bb8f-3b8e-a871-4148be66a5ac | -2.2527 | -51.9313 | 2025-10-20 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 2bb84f3e-5696-3afa-ae1e-f374c8ae695b | -3.3279 | -50.2195 | 2025-10-20 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| f551faaf-45f8-3051-96d2-db0b0c8fb4ed | -2.2527 | -51.9108 | 2025-10-20 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 3a147177-d35c-3777-9843-65238c1c5538 | -9.6401 | -64.7411 | 2025-10-20 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5ef46d30-f531-3eed-b150-e3da24c3bd1b | -8.0676 | -48.0112 | 2025-10-20 00:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b8eda9bf-ad4c-3261-b0cc-1c65073579fe | -9.5725 | -40.3227 | 2025-10-20 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 3492ff05-63f4-3b35-9b0d-80afe84bc96f | -2.9128 | -52.7146 | 2025-10-20 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 6054c439-8ac6-3333-badf-d2cc68282f2a | -2.2343 | -51.9111 | 2025-10-20 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 803d2fae-ca7c-3a83-a2b7-cb0804ab0363 | -4.4066 | -43.3118 | 2025-10-20 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8908b371-50e6-3cdb-81c0-26a64cd6a00b | -2.2527 | -51.9108 | 2025-10-20 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| fccd6d5b-a97e-369a-b09d-987fde48cf4a | -9.553 | -40.3503 | 2025-10-20 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 168.3 |
| 2422055c-3043-37b0-80af-843dbb76860d | -9.5538 | -40.3005 | 2025-10-20 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.0 |
| e77d7400-6d6b-3514-a635-dae72c2cecd3 | -9.5534 | -40.3254 | 2025-10-20 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 351.5 |
| 658278b5-ab23-3d39-9be9-a7ff4aa5a4fe | -9.5721 | -40.3475 | 2025-10-20 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 173.4 |
| ed6024c6-0a9b-3305-84b1-bc505934e68d | -2.9128 | -52.7146 | 2025-10-20 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| fcf98d1f-57e0-30e4-a5d9-184a51d05209 | -3.3279 | -50.2195 | 2025-10-20 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f7a6b4fa-7b9e-3e0b-832d-a86655e46b93 | -9.5725 | -40.3227 | 2025-10-20 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 487.2 |
| e85dffb7-5134-385d-b492-f75b15713d9a | -10.0204 | -47.0414 | 2025-10-20 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 9c8e0cca-6448-346e-999b-929e7b4174d3 | -4.4066 | -43.3118 | 2025-10-20 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f0ddecf3-d2e0-3fd3-be0f-13162507c704 | -10.0011 | -47.0658 | 2025-10-20 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 3bb911d6-9523-3336-8328-4835aa16b512 | -9.5729 | -40.2978 | 2025-10-20 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.6 |
| c6139e72-73d2-3e58-a906-27ee067c6728 | -10.0014 | -47.0435 | 2025-10-20 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 60ffeaa4-9af1-39cc-a1b5-295cf77f5f06 | -2.2343 | -51.9111 | 2025-10-20 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 14f173ee-998b-3cba-aadf-f82ebaef8921 | -9.6401 | -64.7411 | 2025-10-20 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c928fac2-8c38-33fc-868d-13d1ec568412 | -3.3463 | -50.2189 | 2025-10-20 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8184ad55-16a2-34d2-8dd4-2daf4e323673 | -2.2527 | -51.9313 | 2025-10-20 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 4174b5bf-2ffa-3781-9650-96792550e6e9 | -8.0676 | -48.0112 | 2025-10-20 01:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a9b38400-3935-3a76-91f3-32671051fb9a | -6.5631 | -51.1126 | 2025-10-20 01:00:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e5b9d331-ce33-3b0b-86ae-cbd9c5271747 | -10.0204 | -47.0414 | 2025-10-20 01:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 857f140d-518c-3385-9312-1af76b94b0c6 | -2.2527 | -51.9108 | 2025-10-20 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 33d4c6ed-723f-31a6-8e5e-0b5b9feb13bb | -2.2343 | -51.9111 | 2025-10-20 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b2fa7137-6879-3b1c-ae75-75a6f49c1e0c | -10.0014 | -47.0435 | 2025-10-20 01:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| be005274-1d98-377b-8463-b5b6e9adafd3 | -2.2527 | -51.9313 | 2025-10-20 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e0181154-bdca-30ee-8f55-fd88603ac6fa | -9.5721 | -40.3475 | 2025-10-20 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 4ed6079a-ba35-3313-b68b-35435a90cbab | -3.3279 | -50.2195 | 2025-10-20 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 48546656-cd39-36b2-910b-521c4b1e1b43 | -8.0676 | -48.0112 | 2025-10-20 01:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5f3623d9-1483-3b04-b340-ac3bf672c6ab | -6.5631 | -51.1126 | 2025-10-20 01:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2b5ea691-4b3e-3b00-9435-d2de8ce5deb7 | -9.6401 | -64.7411 | 2025-10-20 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| dedc541a-accb-3828-9003-7cd2e2353861 | -4.4066 | -43.3118 | 2025-10-20 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e86ed5c6-a0bb-3ce7-ae35-d574a40eccad | -9.5534 | -40.3254 | 2025-10-20 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 218.4 |
| 51bc688f-32e6-32f9-8282-3c669040a210 | -3.3278 | -50.2405 | 2025-10-20 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 89ca9fed-f668-39ce-acab-2450d09bf4c1 | -9.553 | -40.3503 | 2025-10-20 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 150.5 |
| 3bfe86b1-8f19-3e1b-8bff-25bd94baa79d | -9.5725 | -40.3227 | 2025-10-20 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 270.3 |
| 7b9c5756-a692-3750-b98b-11bb3e321c0a | -9.6401 | -64.7411 | 2025-10-20 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 939199b4-1791-32cf-a9ab-10e7f57e375c | -2.2527 | -51.9313 | 2025-10-20 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 552ef1da-b51f-3af2-b976-092cbc3a2d1d | -2.2527 | -51.9108 | 2025-10-20 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 0a32d884-096f-3dd3-b3cd-d2daf575c050 | -9.5725 | -40.3227 | 2025-10-20 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 438.5 |
| 353dfaab-6305-36f0-8e1c-c614338aa921 | -9.553 | -40.3503 | 2025-10-20 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 202.8 |
| ef9507d3-f0fc-37bd-bf2a-d40c22cbdeb6 | -3.6178 | -51.4613 | 2025-10-20 01:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f37b9709-1efe-396d-a0b7-7a72b7cce432 | -9.5721 | -40.3475 | 2025-10-20 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 256.9 |
| a47c2906-ae31-31a8-9687-f75ead9a6018 | -3.3279 | -50.2195 | 2025-10-20 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 1e7ee25d-0f84-37ca-b558-2795de7ada36 | -10.0301 | -36.1073 | 2025-10-20 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| b4f6d975-a1ac-3192-ae6b-5748f0fe5c3d | -10.0494 | -36.1038 | 2025-10-20 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 129.2 |
| c914696c-8a8d-34ea-aa2f-38df262bb29d | -10.0204 | -47.0414 | 2025-10-20 01:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 0a74ef9c-32ef-300a-9f40-d3d5e8a8c7a7 | -2.2343 | -51.9111 | 2025-10-20 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f3d9d708-f0e5-370a-a32d-ccaa135636db | -10.0489 | -36.131 | 2025-10-20 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 4402cbb3-d9f4-300a-9453-237b01b7c036 | -9.5534 | -40.3254 | 2025-10-20 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 288.1 |


[Clique aqui para ver as próximas entradas](README4.md)
