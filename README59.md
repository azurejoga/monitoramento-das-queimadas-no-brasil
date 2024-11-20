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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2565df1-a83b-3a57-a5d0-ba2908346c39 | -3.36488 | -54.10434 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3702be02-410d-3df1-b62b-d1a9c0068783 | -3.98013 | -49.91946 | 2024-11-20 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 864bb0a4-f2ef-3f76-a6da-869686f02e3d | -2.20751 | -53.70664 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bb5ba69-ca5e-375b-be19-f36940aa200c | -2.54535 | -49.40663 | 2024-11-20 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c13b3a-625b-3f07-a0de-fe119f38cbfc | -1.72978 | -52.79715 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6185fb8e-d5b0-3537-bb67-9c854abb2a46 | -2.08837 | -46.39861 | 2024-11-20 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cea96b6-bf52-3049-bbc1-5fd2a60a5e8f | -2.0023 | -46.60487 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7ca51e7-4a32-30d3-b691-48c56dbf6909 | -1.55536 | -52.28083 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84ba3ad8-b97d-3c5b-9a29-bdf1504c129e | -2.71093 | -47.72625 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb93941f-b756-392c-af43-19190db6b319 | -2.95317 | -48.3245 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4585ca5-54cf-3750-8d44-2a89c9584d29 | -4.38979 | -47.76182 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9836ee1-3050-3282-83ff-73596d692d52 | -6.82691 | -43.28405 | 2024-11-20 04:50:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b1655b5d-7692-3ddb-a955-dfbac4c9ddb5 | -3.0272 | -51.52905 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04fe7af3-71f4-3341-ad77-4c99422df4e0 | -2.6227 | -51.801 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b017459f-97d3-3aa7-b258-3f937512d8de | -1.22319 | -51.74792 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8cf78ce-a61f-3666-a027-c27dcfbcdfb0 | -1.19546 | -53.67786 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ebec5a62-54cb-30c0-bdac-f207007fbcbe | -1.54107 | -52.04626 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c322bda-d7fc-3e5e-b976-a1b2ad947d18 | -1.11848 | -52.39292 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c06c6ad8-5fe7-3c68-9d15-c2d285494ebb | -1.8682 | -46.80114 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4cdceff-ca91-3bb8-b1a8-3de7e88a6109 | -5.69265 | -45.85025 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f8f0d2f-6984-3c5e-801b-7984b10eaebe | -2.90712 | -53.05691 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b94e6945-a707-3b57-b8fd-f65e46f34575 | -2.82281 | -54.01828 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c8c184d-2595-31eb-b684-030b1df07908 | -1.499 | -52.18246 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6f2b830-11e7-3097-8e64-7291a75f274b | -3.51519 | -53.80159 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b672bdd-c1b3-3581-b4df-19ef6f5208b0 | -2.91217 | -53.06866 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 563a72da-c219-31cc-9e44-efc31c3a1653 | -1.65341 | -52.53012 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9556a283-0241-3bae-9539-26e1a1227b60 | -5.69841 | -45.84219 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f27ff72e-12ad-31c7-af09-33380802de1a | -2.61174 | -48.21622 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 794de6ef-535f-39f6-a4ca-d26110821549 | -3.7665 | -53.84863 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e58659c9-c844-3951-9246-fff86a43613e | -1.24322 | -51.74751 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb9fa0bc-de6a-3979-aa73-20e8dd54aea7 | -3.29615 | -53.86053 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0486c6d0-5d36-3154-a548-52682c28f63a | -2.25903 | -48.81317 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6366c172-3c2a-3b84-8f8d-ee7b83383a80 | -2.18472 | -53.42651 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c34b72e6-8e93-3bbe-abfb-1172c1bf5b20 | -2.20308 | -53.66709 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ce891fd-9a1b-347e-baac-8c62a5004d17 | -0.81029 | -51.48889 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1affbe8-2420-34ab-91f4-3887c956b097 | -2.86753 | -51.78958 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48c6336f-3393-324e-8428-98e666edfe28 | -1.85521 | -47.82856 | 2024-11-20 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c64bc3e1-1744-31df-b6cb-d028937937f6 | -3.29167 | -53.8444 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01e9adc0-cdcf-3ee1-80f2-ee477cbc47a9 | -2.25965 | -48.80919 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 302349ad-6e9e-3248-ad99-5aa054cef75e | -3.06391 | -53.2802 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da074b1e-a034-307f-809f-30e05ea79399 | -2.92456 | -51.44884 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5acac17-3836-3603-97ac-a9db3dddc987 | -1.05718 | -53.09544 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea20e8f8-685d-3d0a-906d-bd906295c981 | -3.50583 | -54.03592 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f2edf0c-582e-35ae-813a-e51ecf7599a2 | -4.09479 | -44.85725 | 2024-11-20 04:50:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34fee0b7-c128-3f08-a54a-13a5665e1acd | -1.46327 | -52.69025 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef601c80-142e-3d65-90e7-6de2f63b685c | -2.02016 | -51.17687 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea386ec3-6a8e-3b66-9d0c-87d5e5a9acd7 | -3.0037 | -45.43756 | 2024-11-20 04:50:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb9085f6-9347-39da-bbac-f23ad275de7d | -5.70032 | -45.84447 | 2024-11-20 04:50:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2de58995-14c3-3236-9b09-48619337f1b1 | -4.11412 | -51.05095 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 275e28cb-ba4c-37f9-9e9e-bf3a92b17991 | -1.50232 | -52.03983 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c9a2bbb-2007-30a5-ad62-3cb881a86f1b | -2.81345 | -54.02545 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 875c59ba-257c-3bf0-9908-7dd5327e1313 | -2.91387 | -53.05799 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bafe28e3-b8a9-3b7a-bc77-20ebc800d74e | -2.24998 | -53.67443 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03cdca56-6270-3e07-9f64-87c0262bf03b | -2.18392 | -48.40193 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31c78207-4bd3-3a97-83b6-3aa4ce3a392c | -3.36898 | -54.10109 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c696b2fe-c1fd-3252-84ac-e60dc3014278 | -1.51035 | -51.92373 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afa417c6-c104-3344-8d42-74b1a7916b61 | -2.76294 | -52.60175 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f0678b8-bf53-36e6-a81b-50223d4e90a9 | -2.55109 | -47.29112 | 2024-11-20 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f0549a6-0a31-365f-9a3e-6aee57fa067e | -1.47886 | -51.97212 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a01ca21-2844-30a1-b7f8-da6c361c888e | -1.9943 | -46.60361 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0631c40d-ab48-3b22-906c-7ef114920dea | -2.72246 | -49.33886 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d547eb90-d9d3-3292-b557-3ae54457c2cf | -1.8633 | -47.82535 | 2024-11-20 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4f17d91-888e-30dc-b43d-af1b638c7439 | -1.55567 | -51.8461 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48269fdb-00ab-3ae6-b1a3-690d47ccdb44 | -3.22561 | -53.62428 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8ed0dd9-5aef-3d0f-a088-d4c600460fca | -0.96592 | -51.72517 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 963fd377-b937-30d4-8d85-d50fbb2a1e18 | -2.25224 | -53.68253 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2839049-9349-332d-9bb4-83d3c35e788c | -2.81406 | -54.0216 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65dc76f7-904d-3fa0-b425-0224b6fa11c1 | -1.25506 | -53.36857 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57da3b8e-06b9-376f-b973-ff5fe9a8fdda | -3.58504 | -43.62254 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d471d86-676a-3655-9eb7-17e5dcf52f53 | -2.61443 | -48.2472 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e673e065-9717-366c-8a5a-ff9b485d8b9a | -4.14365 | -47.98773 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46320acd-29d8-367e-833a-b58d8e3eaa6f | -1.30735 | -52.26337 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79822be8-5fba-3bd5-bdec-d12d013ae7ca | -2.90923 | -48.31773 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fba4429-5c85-39b5-af57-8ba0320e99d4 | -1.26582 | -53.41257 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18e8fc20-c38a-386d-bacb-95e05c6c45a1 | -1.3933 | -52.08699 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed9ea303-124e-3210-89e5-57cbb7738808 | -2.92455 | -53.07801 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34216f1d-a342-355b-a7dd-714a590e49d6 | -3.06383 | -54.40738 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d958abaa-9344-3ce5-b14b-5eee67ec89cd | -2.74005 | -51.72026 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16253adf-f0cf-367e-8e25-26e5e19e3816 | -2.91274 | -53.0651 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f018a70b-469d-3db1-b764-19aa20e6079d | -4.52417 | -50.68179 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd054aee-8879-3f0b-8a22-3cb61f1fa89e | -2.13007 | -50.13675 | 2024-11-20 04:50:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbcba62-f196-34eb-b243-c31fdb20d1bc | -1.54816 | -51.23014 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43d1d348-2948-3023-bfb9-00e428047a11 | -3.00694 | -51.44399 | 2024-11-20 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e999ac9f-238c-3156-9f67-1080c32c7c4f | -1.33574 | -52.23548 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2acb0516-94f7-341d-8a0c-27bfabb19a0e | -0.96537 | -51.72863 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a3bc9bf-bbdd-346e-bf4d-8787e2e0b0a4 | -2.7935 | -51.78868 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c20cfe34-debb-3fbc-b316-aee3f02dedcc | -3.88036 | -52.23532 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f79eca51-3cec-3591-8924-8513dd28538a | -2.3839 | -53.66762 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3a930d9-70b0-3d90-9476-6ded52161b53 | -2.79781 | -54.01114 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b03b88a1-70e8-3093-8557-3b1ca2c43a58 | -5.41913 | -47.39544 | 2024-11-20 04:50:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eca951f0-7438-324f-bf67-523cb4576fe6 | -2.95492 | -48.33148 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 67290228-0b16-3e9f-8c4a-4537e5ea0172 | -1.32369 | -52.39924 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5fc54e24-a6c1-3668-9132-dc202a24c3cb | -1.98639 | -53.13707 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e1f0312-2774-39c4-8bb4-d4b83b2a9694 | -1.6976 | -52.36017 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0e798f7-546d-3d78-92c3-1874e6eca688 | -2.8821 | -53.96077 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45d55eb6-dcb5-364c-ba5b-72d1048aea71 | -3.21557 | -53.84088 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f042682-1d0e-3366-ab60-85ceefe51e38 | -1.81815 | -52.69754 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a98c23aa-8e69-31b8-81ea-bbd0acd77f97 | -5.8281 | -46.54671 | 2024-11-20 04:50:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 115b61ff-41b4-3a5e-964b-e5de82bc6699 | -3.84893 | -49.44097 | 2024-11-20 04:50:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7628354e-b514-3f17-b6a2-42b6bf3f158c | -3.37869 | -44.42843 | 2024-11-20 04:50:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README60.md)
