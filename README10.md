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
| 5cb926ae-71ff-3e1c-a51b-3410be24b21f | -3.21812 | -50.40049 | 2026-01-06 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37c0519e-5238-3075-8224-b56c58c32f44 | -4.09991 | -47.29559 | 2026-01-06 04:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 781bf5bf-f5c7-31ca-88d0-9044e53ed3fa | -2.52063 | -47.82487 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16f47e77-8168-310d-86a2-556d35ba0938 | -3.22642 | -50.93185 | 2026-01-06 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ff1de91-8806-3d2c-bbc9-7b5315aea444 | -2.0789 | -47.87888 | 2026-01-06 04:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a4e4758-6db3-312a-8395-bedc0ee8dbe5 | -2.24621 | -48.46626 | 2026-01-06 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a54898f7-312d-3d1a-a4b5-30df3b4093ca | -1.91898 | -53.47435 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f94b2da-89d5-3848-9011-8bec5141ec11 | -2.89077 | -50.23082 | 2026-01-06 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6f98455-fd2b-3a19-9b23-a39f446fb624 | -3.56486 | -47.17522 | 2026-01-06 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55ea6c47-57c8-329c-8fc1-0a6321332de9 | -2.44341 | -49.02921 | 2026-01-06 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e90e92d6-81cf-304a-a32e-a96035cce736 | -1.00681 | -53.1951 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc81ab70-9f62-379e-bff4-43d2c9e83be0 | -1.83799 | -53.80989 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c36e71e-ea3f-304b-a68b-028e621cda2d | -1.65711 | -52.0545 | 2026-01-06 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 57d3bdcd-759f-3467-8ca5-38f51d25fd95 | -2.81039 | -52.94394 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b155bf33-992c-3429-81bf-cf8ba64f376b | -2.53512 | -47.83176 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 948f01e1-da12-385f-b654-57a64df05193 | -2.09252 | -53.50875 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9a619a3-7cbb-385c-8d7f-281111246244 | -0.74196 | -50.29813 | 2026-01-06 04:53:00 | NOAA-20 | ANAJÁS | PARÁ | Brasil | 1500701 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a99f9a7f-319d-3511-b860-249411f6643a | -4.15226 | -43.65197 | 2026-01-06 04:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5de72325-f0f2-3840-ab65-37a246305791 | -1.25458 | -54.08656 | 2026-01-06 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30d1151f-6daf-3ee3-bf4a-fd3ab919881d | -3.70226 | -46.97881 | 2026-01-06 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e13b68d-c5d6-3126-9ea0-fde0a63b0bab | -4.07278 | -42.88859 | 2026-01-06 04:53:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 538b22e0-191f-3866-bded-bfbf8f7d0f15 | -2.91772 | -51.40625 | 2026-01-06 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c06673c2-6f1c-357b-ac8c-330fd40c2f7c | -3.25611 | -42.54509 | 2026-01-06 04:53:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e4228c1-8b6f-315d-a56c-e76774cef347 | -2.27649 | -53.78529 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e4818e48-68ab-3535-8976-acd310a0f683 | -3.70279 | -46.97521 | 2026-01-06 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aad731a5-3de3-385f-9859-37ebf27c7b69 | -3.70332 | -46.97162 | 2026-01-06 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff4a383d-f6b6-3080-a94d-71a5fde8cdbd | -3.17887 | -51.0829 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9ffa2ea-fc87-39c8-a6c2-1f775a772f56 | -3.4435 | -52.63668 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 909f22aa-d75b-3a7d-9a31-4fee1cab51ed | -2.9275 | -48.22225 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07020419-577b-37b7-a10b-a04345fd27b5 | -1.36146 | -49.41598 | 2026-01-06 04:53:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6a482f48-f2e5-3983-aa79-3e57624e4133 | -2.27306 | -53.78476 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a922c77a-ace4-31e2-b550-8cc40a57c949 | -2.89229 | -52.57837 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a46ce0a7-2885-35bd-8993-e42349b70963 | -4.06849 | -42.53612 | 2026-01-06 04:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bdd11dec-106b-37c6-b71f-b9fd549f658c | -1.3586 | -49.41166 | 2026-01-06 04:53:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe193cee-cd7b-3179-97a9-290df977ce1b | -3.70133 | -43.44012 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 674df7e4-9661-382a-9c60-624d4ea5bdb7 | -3.70295 | -46.97506 | 2026-01-06 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0790720c-b789-3988-81c4-c73b692d5f5f | -2.4491 | -47.7872 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cae32ed7-61a6-31df-9d97-da1b75c99431 | -2.88197 | -45.221 | 2026-01-06 04:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17efa8f8-ae0e-3a82-bb37-cddd7ede592f | -1.14337 | -48.10349 | 2026-01-06 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 420954a4-38c3-3d3b-b4e8-bf989a787e02 | -3.69613 | -43.43936 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c7114acc-b062-3051-891c-ed8bc85b8de9 | -1.81887 | -54.16426 | 2026-01-06 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac3ea0b1-f1ec-382f-bb14-678042ff5ff5 | -5.663 | -46.23262 | 2026-01-06 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 36b4f53f-66b9-33d8-9de3-e236fbc13d87 | -2.51992 | -47.82948 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2a5adbda-5187-32a3-a9e1-50e45898e3ae | -2.80034 | -53.00709 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91f6d029-4dfe-36f5-b133-9f9a005ee52b | -3.56084 | -47.17463 | 2026-01-06 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d775cf-51ae-348d-853a-1ba0ca4aa038 | -2.8576 | -52.79728 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc50531-7216-361b-b19f-3438deb7e140 | -2.93357 | -48.23231 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4be7b077-b347-3d02-92ed-ffad6719ee29 | -3.6958 | -43.43542 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 82103656-ce04-361d-8a4b-e4873a299e38 | -4.73224 | -45.5748 | 2026-01-06 04:53:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a702ee03-01b0-3a95-9e52-e5565c8ac85a | -3.55217 | -50.52518 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9029dd2e-b33a-3d1f-a030-3ed2c9fa6227 | -2.48399 | -46.30259 | 2026-01-06 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 475e8c5a-6ddd-3da3-9050-cc4494e8f58c | -3.36766 | -50.49319 | 2026-01-06 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93dfa627-b30b-3163-9d29-c5c2ec303f4a | -3.26104 | -42.54952 | 2026-01-06 04:53:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cd4bf4d-1ead-3444-8aec-1bc53909b87a | -2.73756 | -42.58939 | 2026-01-06 04:53:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc174b2-6339-342d-a4ff-33ba415672f7 | -2.08174 | -48.37042 | 2026-01-06 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a33e94-0a7a-3145-9da5-4eb45b9bf3f3 | -1.91841 | -53.478 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5ee2f07-fead-3163-934e-95ea4e31be1f | -2.88012 | -52.56932 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 625241f2-962a-3770-a73d-eb67a4796052 | -2.36129 | -47.68076 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40d1ba47-fa7e-32bf-84e0-c6033a138c15 | -2.36584 | -47.67668 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd726e9c-f294-3221-b11b-44b11fd5faa2 | -2.11073 | -53.48175 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd08e23-6c68-361c-94c2-132f4ba5aaa1 | -2.74349 | -42.58672 | 2026-01-06 04:53:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 811806bb-1858-35ba-b96e-ac4065d61300 | -2.85427 | -52.79676 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55ba50c7-a24f-3d40-b9bc-493669c2fb11 | -3.22098 | -51.33602 | 2026-01-06 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85dcab66-e50c-3e90-87d2-426c04a51818 | -2.80089 | -53.00359 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d091afb8-78f7-3eac-b061-6b33ed799bb5 | -2.09534 | -53.51295 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a830d3b-4f45-3d88-972e-fdacc0f290df | -2.63235 | -48.48421 | 2026-01-06 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a98b4ed3-3290-3f3a-8ed1-8a9687ff928a | -3.18056 | -51.09394 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33c860f6-f01e-30bc-9b7f-bc16bcb7270b | -3.1905 | -52.00346 | 2026-01-06 04:53:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bfacd27-59ef-3ebc-afbf-2e0ad36df54d | -3.19277 | -52.03199 | 2026-01-06 04:53:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41d29b1b-108e-3003-848a-206f4d5a4646 | -3.18111 | -51.09044 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f3a90b2-c3c0-3c8f-a1b6-8ec0cceba1bd | -4.40902 | -45.3226 | 2026-01-06 04:53:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f749622e-9f28-3018-9483-c347f5f10ad5 | -2.88737 | -50.2303 | 2026-01-06 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4177dea-d0f8-399b-9b40-f718e5ca827b | -3.21409 | -50.66903 | 2026-01-06 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1a21426-a413-3a7f-832a-9d73e9c6ca36 | -1.82968 | -53.86242 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6f4cf05-09d1-3d09-826a-17530db97842 | -3.70224 | -43.43383 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 19e01b7b-d051-317f-8e9b-8dc4fbf5b18b | -3.33209 | -52.6973 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 117ca959-b39b-3fef-ba5c-9ad88138f9ad | -3.70148 | -43.43307 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bd5e5bd7-0d52-3901-8730-82f90a620cb8 | -2.47483 | -47.97265 | 2026-01-06 04:53:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf63792b-eac9-334a-b8c9-02555b97b82c | -1.44308 | -53.40432 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3ff9185-8af6-34a7-8d30-2fd77e5f976d | -3.70239 | -46.97865 | 2026-01-06 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94266b4b-9ce0-3405-8c0f-68cf5802f495 | -2.00638 | -53.21363 | 2026-01-06 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5aa00122-ac2a-3440-8550-a270285b3389 | -2.19292 | -52.74636 | 2026-01-06 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7455028-af71-3b7e-a5c3-7917c53aaf77 | -2.80368 | -53.00762 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e442ce9b-e58d-3965-9925-8da076b0edfa | -2.35066 | -48.41956 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e938ca5b-5d00-3bf3-9255-805266cbc44f | -3.26157 | -42.546 | 2026-01-06 04:53:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff80c9ed-0252-3df3-a306-d61006eaca41 | -2.73598 | -42.58926 | 2026-01-06 04:53:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07883b1e-72a7-320a-b4f0-6c1e1a833452 | -2.00301 | -53.2131 | 2026-01-06 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3530073d-963e-3784-b175-631c6d455864 | -2.67283 | -49.85427 | 2026-01-06 04:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b44e026e-eec6-3805-ab9d-9ddb2748efc7 | -5.66361 | -46.2284 | 2026-01-06 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 353e0503-8a14-3a2f-8fc1-038b86d46417 | -2.87736 | -52.56534 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93147c75-c289-37c8-b631-e32890c356fc | -3.70178 | -43.437 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 673c3eeb-5df8-3ad4-96d1-963e1bd6a470 | -1.79535 | -52.74882 | 2026-01-06 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94d83297-c081-31f9-92de-60f96f6d6ac2 | -1.02317 | -53.5549 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f8d9de-98a4-39cb-a5cc-156c0baa50a8 | -1.00623 | -53.19873 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40fe6404-2086-375c-986d-201e081dec67 | -2.53132 | -47.8312 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 14dc04e2-625f-3531-a92a-58132136dba7 | -3.69532 | -43.4386 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 778d59bf-8d40-3aec-b870-fad3567911e3 | -2.90762 | -46.73425 | 2026-01-06 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b98b638a-a360-3d3c-bc1f-49cfc69f06ad | -2.80423 | -53.00412 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28eb3ff7-3ed0-3556-9947-b47caa4877f1 | -2.89284 | -52.57491 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bed611c1-c0d1-3265-9b79-65706f9db236 | -3.83778 | -50.0204 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
