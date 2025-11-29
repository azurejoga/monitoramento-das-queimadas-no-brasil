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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cee9d9a0-507c-3038-9aac-2717968973b7 | -20.1813 | -52.3754 | 2025-11-29 02:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 1e2f8231-75f8-3926-b877-a09695e7a9d6 | -20.2016 | -52.3717 | 2025-11-29 02:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 120.1 |
| f7b613df-873a-3659-8470-e2c315232a34 | -3.2134 | -46.8283 | 2025-11-29 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2fa9f34b-14e9-3606-83fb-8fcca0eda8f0 | -2.7845 | -47.4343 | 2025-11-29 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ab0dcaca-4179-35a8-90c0-2b8f70fb4e04 | -8.0321 | -43.1257 | 2025-11-29 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| fafeb1e8-60c3-3622-a103-485e4c81f3f3 | -20.1813 | -52.3754 | 2025-11-29 02:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 3591c2bb-c959-3dc6-bf8e-c81a7711f24e | -1.4737 | -45.7907 | 2025-11-29 02:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 62c727d6-2add-3ddf-babc-39de829ab766 | -20.2016 | -52.3717 | 2025-11-29 02:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 140.3 |
| f589dc72-63f3-3317-903c-e457c8578dc4 | -20.1807 | -52.3975 | 2025-11-29 02:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 685acc73-80a9-350d-934f-524471a5c9db | -2.7845 | -47.4125 | 2025-11-29 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 84456c48-68bc-3fb6-b520-e278a8076baa | -20.1609 | -52.3791 | 2025-11-29 02:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 06b15ee0-90c9-32ee-ad53-d6af192df3d8 | -3.2134 | -46.8283 | 2025-11-29 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 84c1014c-e9be-39c4-beb1-5e4bd85b3156 | -2.5327 | -45.3843 | 2025-11-29 02:50:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 07c00b35-d545-3410-b494-f20b9e6b6af0 | -2.7845 | -47.4343 | 2025-11-29 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1496bf26-8fdc-3bea-a476-bed865280107 | -8.1633 | -43.2055 | 2025-11-29 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 2af9e7c7-f444-3a0f-b438-627fa39ba840 | -1.4923 | -45.7903 | 2025-11-29 02:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4a476c70-42f0-3813-9cfa-92b6bd4da09b | -8.051 | -43.1237 | 2025-11-29 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 5c706827-91c2-3842-b4a7-38b0b1fcbb15 | -20.201 | -52.3937 | 2025-11-29 02:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 78.4 |
| da506ca4-1d66-3d82-b07a-01630e6c3201 | -20.1813 | -52.3754 | 2025-11-29 03:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 7465a221-abd7-383a-b9e9-808ec9efae68 | -20.2016 | -52.3717 | 2025-11-29 03:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 57795bfb-6bdf-3ddd-9f7c-f2877cce5ce0 | -20.1807 | -52.3975 | 2025-11-29 03:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 0dad117c-b4c9-3cf0-8e44-2b504c60fa0b | -2.7845 | -47.4343 | 2025-11-29 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 72ec150f-f07a-3206-811f-1b75b23aae9e | -8.1633 | -43.2055 | 2025-11-29 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 62341f8b-a5eb-3b4b-b400-20dfd6744b4a | -8.0321 | -43.1257 | 2025-11-29 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| d2f4aab5-1d77-39fc-905d-650da64587a9 | -20.201 | -52.3937 | 2025-11-29 03:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 76.0 |
| bb319c8d-e041-328c-9250-06aae8fca067 | -3.2134 | -46.8283 | 2025-11-29 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ad7508dc-2eee-370e-84cd-e607d106b8a7 | -8.051 | -43.1237 | 2025-11-29 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 43ad40ab-75a5-3b46-b004-088a33e240b9 | -20.1609 | -52.3791 | 2025-11-29 03:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ef1ff3e6-7348-37e9-8484-36af5d298585 | -1.4923 | -45.7903 | 2025-11-29 03:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 00f5c0ed-d4f2-31f2-878f-b6bb02d472bf | -8.0318 | -43.1493 | 2025-11-29 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| df4e41ac-9136-38d3-a1fc-520333709112 | -2.7845 | -47.4125 | 2025-11-29 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b73fa4c3-139c-366d-aa0e-e7fc30c37d96 | -7.23281 | -35.10502 | 2025-11-29 03:02:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| dc15c76b-d60e-3ce1-ba90-23ff33050e3d | -7.2336 | -35.10075 | 2025-11-29 03:02:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| a07609d2-1229-31ff-9691-8500c6c20dcf | -7.23957 | -35.10157 | 2025-11-29 03:02:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c81f93f3-d872-37cf-b19c-4b4442384fda | -10.13934 | -36.33957 | 2025-11-29 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c35e539e-4700-3212-b564-985783e6bcdd | -10.13982 | -36.33732 | 2025-11-29 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 89ea00c2-5c0d-3825-bd56-3c6e24ac7b78 | -10.14026 | -36.3348 | 2025-11-29 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 1d844db4-a678-3771-9c17-9d2e4017c314 | -10.14073 | -36.33274 | 2025-11-29 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 542baf9b-227e-3656-b35c-d2469d8b7358 | -10.13884 | -36.34221 | 2025-11-29 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4dfab158-294a-31a0-926a-55ce3808dc57 | -20.1807 | -52.3975 | 2025-11-29 03:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 5a82f14d-db52-32e4-a388-53b52a03db71 | -20.1813 | -52.3754 | 2025-11-29 03:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 65d1f9db-8d5f-34f0-aad1-1e7565fd1dd8 | -8.051 | -43.1237 | 2025-11-29 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 0f18819d-401f-3be4-bb28-ccd9433f45f2 | -8.0321 | -43.1257 | 2025-11-29 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| c06e3d4d-6c09-356c-bc44-982d424c684e | -1.4923 | -45.7903 | 2025-11-29 03:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ffa57f1c-ccb0-36f7-a113-5c346d140c09 | -20.2016 | -52.3717 | 2025-11-29 03:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 87.9 |
| cf5f9dbf-ece9-31ce-b8d8-7c9cbde19a0d | -2.7845 | -47.4343 | 2025-11-29 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 29312552-c55d-39c0-8e3c-f52584cc7ca0 | -8.1633 | -43.2055 | 2025-11-29 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| c2a61a08-9281-3be5-ae5a-11772600ddb1 | -2.6322 | -48.542 | 2025-11-29 03:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 32f2c82d-ce89-31c9-acc7-4c89acfe7262 | -2.7845 | -47.4125 | 2025-11-29 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9f1c18e1-ae89-3100-9a8c-f035db84ff20 | -8.1822 | -43.2034 | 2025-11-29 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.1 |
| 025dbfd9-5d3b-310d-91e5-8ee373f2c32f | -2.7845 | -47.4343 | 2025-11-29 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| cf7e0980-df92-3d0d-b427-e86e0fa48346 | -8.1633 | -43.2055 | 2025-11-29 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| e0884d19-7e49-3546-9aa8-dffe36edd7c7 | -8.0321 | -43.1257 | 2025-11-29 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 91095a57-87b6-3443-bca3-106d04740bab | -20.1813 | -52.3754 | 2025-11-29 03:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 8d04b347-6228-3d28-9eab-01a9bd00d739 | -2.7845 | -47.4125 | 2025-11-29 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 68f2012e-b38f-332f-9ac5-35e845f476ff | -2.6322 | -48.542 | 2025-11-29 03:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fc7f5758-105b-3bec-8edd-1a4fc77f1a96 | -20.201 | -52.3937 | 2025-11-29 03:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 56.3 |
| fe0cea8d-6ceb-3c7c-ab87-f3beaf8895e3 | -20.1807 | -52.3975 | 2025-11-29 03:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 63aef496-ef66-394e-a0db-db84a3e5e01b | -8.051 | -43.1237 | 2025-11-29 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| ec61176d-8065-3b9a-9ae3-e9f898152c95 | -20.2016 | -52.3717 | 2025-11-29 03:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 9c712202-327d-318f-8055-cb4776d84460 | -3.68638 | -38.74078 | 2025-11-29 03:21:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a67e010e-4861-30f7-8bdf-041e8f1ddb66 | -5.54744 | -37.50568 | 2025-11-29 03:21:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aad0a2aa-2f93-3636-81b9-dfc1097d4b5f | -3.89308 | -40.77046 | 2025-11-29 03:21:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 13e296e3-12ca-3b19-926f-8db5aa8c7921 | -3.6869 | -38.73762 | 2025-11-29 03:21:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d92f16b-83ad-3685-9ece-6d2aa8e94f53 | -5.54196 | -37.50979 | 2025-11-29 03:21:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9cfff797-3da0-381a-b3ec-11001098148c | -4.16626 | -43.76355 | 2025-11-29 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3aad905-2b2e-32d2-a507-0814aa235ed0 | -3.13985 | -40.18583 | 2025-11-29 03:21:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ee9dbe97-0440-39c0-8842-da781146cd31 | -5.00309 | -38.54396 | 2025-11-29 03:21:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 36778f5f-d47c-3b1f-a8c2-10be06857b93 | -5.54519 | -37.50603 | 2025-11-29 03:21:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eefa73d0-12ae-336a-baf3-c749e21e67fb | -4.1675 | -43.75639 | 2025-11-29 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b6ed6aa-89a7-3e20-bb11-2a710780156b | -4.85058 | -38.74378 | 2025-11-29 03:21:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 75e363ba-2441-35ef-9c1e-34f2d2a17ec4 | -4.99855 | -38.54008 | 2025-11-29 03:21:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 128f91f8-95b5-39d2-b94d-66e3e994d0ba | -3.88712 | -40.76945 | 2025-11-29 03:21:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d3cceb5-1477-35a5-b857-e51695189ad2 | -3.88787 | -40.76505 | 2025-11-29 03:21:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c44e80d3-37e6-3a99-9564-cc0690dc1542 | -3.14056 | -40.18159 | 2025-11-29 03:21:00 | NOAA-20 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f37f0c1-3dbb-33a2-9917-b4904915d5c0 | -4.85104 | -38.74109 | 2025-11-29 03:21:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 966d0e2b-123f-3ef7-babc-cd6fe2adde95 | -4.846 | -38.7397 | 2025-11-29 03:21:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3ad08ca0-3f4c-3e31-b240-2475b9129a4c | -3.55542 | -39.11188 | 2025-11-29 03:21:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e291afcf-d724-333d-9176-4dbe0b070972 | -4.16402 | -43.75738 | 2025-11-29 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7a8f1b69-41f5-3142-b9ff-798bdf7268ae | -5.00359 | -38.541 | 2025-11-29 03:21:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d610297d-e2fd-399e-96cb-dc06c4e302dc | -6.69638 | -41.46421 | 2025-11-29 03:23:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 9ad55f5e-d690-3e9c-b012-c9c85808f446 | -8.79336 | -40.43458 | 2025-11-29 03:23:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 088e52c7-c683-3105-b072-c54df2fbe0a3 | -9.42447 | -40.34825 | 2025-11-29 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c2ec70b4-1dc8-30e5-9270-5a839d4a8b5a | -8.16494 | -43.20853 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 199e7e12-9eff-3818-95f3-b9b226be8046 | -6.5972 | -43.69704 | 2025-11-29 03:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8ce0cbd-75b9-3577-a1b7-dd8e8f525021 | -8.16596 | -43.20312 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 39c12be1-15a9-3957-80be-89bd2b15a1c6 | -6.7141 | -40.81536 | 2025-11-29 03:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5da6a94b-d70a-3a7e-ad03-785c43a2dd96 | -8.15849 | -43.20725 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 3a699a57-605e-3593-ac1c-2804b4ad95bc | -6.69318 | -41.46449 | 2025-11-29 03:23:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a7ed84af-65d0-3c83-932d-b11e44789b81 | -6.46482 | -38.86475 | 2025-11-29 03:23:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 079ab221-0a42-39a4-bc9c-5925bdff7b34 | -9.28284 | -43.15708 | 2025-11-29 03:23:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a13acf7b-bf5f-32dc-acf0-70df8527331c | -5.33273 | -40.88611 | 2025-11-29 03:23:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0ece05a2-0338-381e-8bd6-97359c83aa7e | -9.37642 | -35.95968 | 2025-11-29 03:23:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8123de56-8866-33c9-85ba-0f143ea38b0d | -6.71239 | -40.81657 | 2025-11-29 03:23:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a5048b89-a702-3c03-9725-a5f2a10ae4c6 | -8.03809 | -43.13533 | 2025-11-29 03:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 664893af-bcf6-335f-a7a7-e7b40faf5182 | -6.69556 | -41.46861 | 2025-11-29 03:23:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 95cc77b1-78ff-3f7e-8f9c-ad07003a930b | -9.42386 | -40.35156 | 2025-11-29 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 645f3283-f0fc-3025-bb91-6784f6cce069 | -6.24143 | -40.30126 | 2025-11-29 03:23:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4051fa49-b79c-3635-81e3-92216e6db203 | -7.23087 | -35.10426 | 2025-11-29 03:23:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e9e6ee15-bc06-398f-8cf0-560067b231a9 | -5.06963 | -40.8243 | 2025-11-29 03:23:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |


[Clique aqui para ver as próximas entradas](README11.md)
