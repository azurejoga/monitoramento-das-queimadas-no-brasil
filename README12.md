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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad514d09-910e-3d22-a40d-1aaac1c6c2b1 | -4.4805 | -43.4237 | 2025-10-27 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| be8a1095-0058-30bc-88ad-321b34e602db | -7.822 | -46.4887 | 2025-10-27 03:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d0397fa9-fa84-38d4-9762-2c9c1c12de83 | -4.4807 | -43.4005 | 2025-10-27 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 975cf586-1f44-301f-9fb2-352c03ef05be | -6.16752 | -41.57684 | 2025-10-27 03:19:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| b01c4b68-e8ce-3e63-9656-4d4758207c37 | -4.25429 | -40.69151 | 2025-10-27 03:19:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e0e230d-2e7d-3138-985e-9fc2efc87991 | -6.44358 | -42.35356 | 2025-10-27 03:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fc57f0b2-5f02-3287-b900-d7f7319fc288 | -7.43195 | -41.88186 | 2025-10-27 03:19:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c3d9ee5a-e733-3e0e-b50f-ea206efc5dc0 | -7.33894 | -42.44939 | 2025-10-27 03:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2de5301f-d330-30cb-9aad-5ce482461d14 | -6.4478 | -42.35268 | 2025-10-27 03:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 75108b6b-c1e0-33be-9239-043b5834c67c | -5.12748 | -41.1933 | 2025-10-27 03:19:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74aefb19-663a-35f5-b773-1a6e5dba78cc | -6.6131 | -38.63521 | 2025-10-27 03:19:00 | NPP-375D | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6856390d-e318-3459-9da8-f33a46ba4ad6 | -5.12076 | -41.1925 | 2025-10-27 03:19:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 65bf88bf-6e42-3ff6-ab23-b43ba1d38546 | -7.33076 | -42.45476 | 2025-10-27 03:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8ff2bd5a-1032-3cb5-b3ce-3801c3ca37e6 | -6.61244 | -38.63888 | 2025-10-27 03:19:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae8fa56c-c162-3ae1-855e-484dcd922089 | -4.25873 | -40.70426 | 2025-10-27 03:19:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1467fe30-3155-3d95-b545-57e0da4b58f6 | -6.17052 | -41.57358 | 2025-10-27 03:19:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a6f0243a-5805-3197-9509-b5b9c9ede757 | -5.43379 | -40.87748 | 2025-10-27 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9cc3a88a-d09a-3a55-8c1f-89053512bf60 | -5.42697 | -40.87556 | 2025-10-27 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08c31171-ed90-3892-9cee-fe6a0e3bc75c | -5.59196 | -41.32176 | 2025-10-27 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10af24ab-622b-37d5-ace3-279e5e874210 | -4.2594 | -40.70051 | 2025-10-27 03:19:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e68978e5-fd96-370b-99c0-6624a4a6995d | -5.42713 | -40.87729 | 2025-10-27 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 26a580c9-9225-3fe1-b4f8-c10dd4370730 | -4.81231 | -38.64446 | 2025-10-27 03:19:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| a582d141-0084-375f-928b-d751c8584c4c | -6.16865 | -41.57056 | 2025-10-27 03:19:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 71562ea7-e702-3106-929b-1df99e5ccc21 | -5.81544 | -40.82711 | 2025-10-27 03:19:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5fa49862-9e1f-3100-8bf3-5606fe0d05c5 | -7.43433 | -41.86922 | 2025-10-27 03:19:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3f613a99-80ae-3e54-99df-54f57b74f860 | -6.08352 | -42.15473 | 2025-10-27 03:19:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bbf93a31-582c-3d0b-8a1c-b7b06e8f9990 | -7.43979 | -41.87693 | 2025-10-27 03:19:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| ca83f818-b960-3d1f-b62b-d347bb2a1bc3 | -8.72312 | -35.38654 | 2025-10-27 03:19:00 | NPP-375D | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c706fa6-c228-3f53-97f2-df7ff03fb859 | -6.08467 | -42.14859 | 2025-10-27 03:19:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 15f267ac-0188-364d-b5a3-8da7f6a24d50 | -4.81164 | -38.64834 | 2025-10-27 03:19:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b2c65d59-6f30-33cf-b108-42a75963bc49 | -5.59298 | -41.31617 | 2025-10-27 03:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21cc2de1-01fe-31a2-a67b-3362901e1ec9 | -7.44092 | -41.87091 | 2025-10-27 03:19:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| facbe1e2-e267-391b-8b6d-d6bff3ff68c3 | -5.65824 | -41.10703 | 2025-10-27 03:19:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5d6724c-97bb-383b-86c1-786423bfb536 | -5.82098 | -40.83329 | 2025-10-27 03:19:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0df706bb-983e-3e67-9a13-a126ff3a40c9 | -4.735 | -41.55322 | 2025-10-27 03:19:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 426f9fd9-db1f-3cbf-b863-9bac5ac65197 | -5.4741 | -37.8534 | 2025-10-27 03:19:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c4cb553-1c34-3ef2-a7d1-e3d4d983105d | -6.16936 | -41.57983 | 2025-10-27 03:19:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 09cc68c3-f76f-34d5-bb0e-7c3eee7ebc66 | -8.72381 | -35.38255 | 2025-10-27 03:19:00 | NPP-375D | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4181873a-a738-3f55-8dcd-69578570e45c | -6.44469 | -42.34748 | 2025-10-27 03:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cae1977e-cee6-3430-aa74-f9c50b0f4052 | -6.23421 | -42.55757 | 2025-10-27 03:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7d7d3dbd-b1e1-36eb-925f-a9f39020de06 | -5.65172 | -41.10564 | 2025-10-27 03:19:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c8f7a93-ef38-3b5c-8629-d4a81a894f1a | -5.43304 | -40.8817 | 2025-10-27 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| de509eac-d071-36b1-8829-7a9b360abaf4 | -5.43362 | -40.87586 | 2025-10-27 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ec7b903a-0c32-3b92-bde5-8dea51ed5484 | -4.26173 | -40.68767 | 2025-10-27 03:19:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e5e851c4-f847-3505-ab68-6b75650c35b1 | -5.43286 | -40.88002 | 2025-10-27 03:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a591063a-098c-3b4f-85f9-bac4f69f3d11 | -7.3388 | -42.44658 | 2025-10-27 03:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 09193f06-81a6-3bce-80f2-f24a37020c4c | -6.164 | -41.57146 | 2025-10-27 03:19:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91da43d0-35d3-3a4f-a5cb-25694cadd65d | -4.72825 | -41.55154 | 2025-10-27 03:19:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 942d84fc-6a7e-3d72-af2d-8222c0bcd171 | -7.3375 | -42.45323 | 2025-10-27 03:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0bcfb09c-6fa6-3fa4-8c3d-acc1db43781a | -4.81096 | -38.65225 | 2025-10-27 03:19:00 | NPP-375D | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2b697d94-801f-36ba-b9df-7eedaef930a7 | -6.44071 | -42.35206 | 2025-10-27 03:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 67ff6337-5be3-34de-88bf-8769e7ca04c9 | -7.43315 | -41.87548 | 2025-10-27 03:19:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 5cbc6c64-e38d-3dc2-9dd9-d225971012cb | -10.8401 | -56.959 | 2025-10-27 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| b27dcb68-fecc-368d-bf5b-2911c33df1e5 | -4.4618 | -43.4248 | 2025-10-27 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 36c592dc-7d39-3721-9d4d-e9a6c079eb3f | -7.822 | -46.4887 | 2025-10-27 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| eccac58d-cc2c-3708-9664-18721dcddf0c | -4.4805 | -43.4237 | 2025-10-27 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 153.3 |
| c7d2d7ad-b128-3d1e-a2e5-7364096fb829 | -4.4431 | -43.4259 | 2025-10-27 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| c671fd36-b601-3f88-9398-2e844c5e6c50 | -4.4807 | -43.4005 | 2025-10-27 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 54a4c37b-e5b1-36c3-bc28-4cf20eb79a5a | -7.8223 | -46.4664 | 2025-10-27 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| b292d5c3-d343-35ee-bc6d-bddf74ae3eb4 | -7.8411 | -46.4646 | 2025-10-27 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| f58d7c6d-3031-388f-bd4f-cb066a455ca2 | -14.314 | -54.3138 | 2025-10-27 03:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d73e5ed3-518b-3897-9f69-55190f1dc1e2 | -7.8406 | -46.5093 | 2025-10-27 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| c5e59bf6-9378-355c-8117-14db594ead0d | -7.8408 | -46.487 | 2025-10-27 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 1c0ccd61-d76d-3bd5-81eb-0e979d38d36b | -4.4804 | -43.447 | 2025-10-27 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f1215572-b66d-36f1-86d3-f6c488ee8725 | -11.66881 | -41.32402 | 2025-10-27 03:21:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6ccd7d53-af2c-34bd-a7dc-48bc71c2fccd | -15.12346 | -43.25657 | 2025-10-27 03:21:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6613c4f4-bec7-325d-8a2c-41828bfabba8 | -12.50691 | -44.33604 | 2025-10-27 03:21:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee9b79d6-13af-32bc-a9bf-39958b5c6ee4 | -10.76075 | -44.20144 | 2025-10-27 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 06b12651-5165-34bc-8ca5-e48be38bb0dd | -9.52442 | -40.30268 | 2025-10-27 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 45.2 |
| ca881e79-d575-38fc-9144-9e0850b07476 | -11.91407 | -43.83329 | 2025-10-27 03:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eca3c8fe-56aa-3321-a540-461e26e71db0 | -12.2856 | -43.76447 | 2025-10-27 03:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 885f0db5-fd2e-3916-bebf-a324ec9deb01 | -15.3002 | -42.38408 | 2025-10-27 03:21:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ca5c6018-9a84-3811-947a-d53897fa88db | -10.75214 | -44.20681 | 2025-10-27 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 6bfae60e-754b-38f7-8403-14f53aab3690 | -12.27887 | -43.76242 | 2025-10-27 03:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b897641a-408e-3298-9e3a-8ad668189370 | -15.12093 | -43.2602 | 2025-10-27 03:21:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d942860-488a-3362-83ca-b09ade480c19 | -13.08426 | -44.54753 | 2025-10-27 03:21:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 80f0f8a9-e4a1-315c-a514-ac2c87ec29ba | -13.07992 | -44.55049 | 2025-10-27 03:21:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da494d39-e08e-3dd4-8380-2839c1c73e08 | -10.75344 | -44.2047 | 2025-10-27 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 08d728c5-d537-37b9-bbab-64068a55f22b | -10.76059 | -44.20646 | 2025-10-27 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f07b4e1b-8078-3e1a-ac22-a14c39cc3f74 | -11.90856 | -43.82516 | 2025-10-27 03:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d9b1cf31-4c50-3b0e-b8fe-c5970798e344 | -10.76206 | -44.19948 | 2025-10-27 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06cf9903-02a8-32bc-9921-aab5268eb022 | -11.70749 | -44.44481 | 2025-10-27 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2179a727-fe8a-3384-a100-67d327b4bd49 | -12.50841 | -44.32899 | 2025-10-27 03:21:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a78c118-4853-3521-8862-542fb328c9a8 | -11.71465 | -44.44642 | 2025-10-27 03:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69fc5548-bc05-37c6-a5d0-052b40f0ec7c | -10.75487 | -44.19794 | 2025-10-27 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 1d5ace55-35a3-3196-aa3e-ff11bd8ba446 | -10.75357 | -44.19983 | 2025-10-27 03:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 73d801df-43bb-3729-9e40-5b0e11039e6f | -12.50543 | -44.34302 | 2025-10-27 03:21:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d140d076-3731-31ce-8761-0b6e5209ade3 | -12.28688 | -43.75838 | 2025-10-27 03:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e0415ef5-f6b5-34f7-af09-54191da3bc59 | -15.29829 | -42.38629 | 2025-10-27 03:21:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecf70b57-6a42-3808-ad5b-ccf61b987dac | -15.29731 | -42.39098 | 2025-10-27 03:21:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92788657-b070-3fd7-8c80-5d6bcad7002f | -12.05833 | -43.98903 | 2025-10-27 03:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| af1b14d0-6e28-31a5-a06d-35497918d7ac | -9.52362 | -40.30688 | 2025-10-27 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| 1c0ae37b-cd74-3a38-aff7-bba47f749e82 | -11.91548 | -43.82666 | 2025-10-27 03:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8c200f36-31a2-336d-acbf-f5e113523d80 | -11.91026 | -43.82674 | 2025-10-27 03:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c84dbd93-9014-359c-a7af-43092cc959cf | -11.90889 | -43.83339 | 2025-10-27 03:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d591a0d5-f0d9-3635-a153-7d83476e1c11 | -8.4832 | -41.23009 | 2025-10-27 03:21:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ac5801d-0a3b-3b84-927d-de5bcc0c1fb5 | -15.11348 | -43.264 | 2025-10-27 03:21:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31b26b9f-3838-3654-ad0a-a07f3418454c | -9.52281 | -40.31108 | 2025-10-27 03:21:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| d2dd651e-0644-3bca-9a10-4d48fb7f6b71 | -13.08148 | -44.54326 | 2025-10-27 03:21:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71897a19-46ac-3015-9157-99f15e0a0ed9 | -11.90715 | -43.83181 | 2025-10-27 03:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README13.md)
