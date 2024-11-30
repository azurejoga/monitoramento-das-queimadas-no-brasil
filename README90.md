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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b51bd6b0-125f-3578-a817-d8444998c484 | -1.64818 | -53.87286 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1f9a2389-340b-3401-b41b-b0d4453fa93f | -2.17371 | -53.65567 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a87c8886-8ee3-380e-8f44-b7669c6fea2f | -3.38392 | -53.50812 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2f4bcec-23be-3f9b-8af7-1c7fabe3b86e | -2.83225 | -54.11027 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 322edb7c-1323-377f-92d3-095a19c59ce5 | -2.58683 | -53.96794 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93aef978-c3aa-30f4-8130-9fc34adae602 | -3.27384 | -53.41011 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8087c798-dfb9-3a75-bd88-280e823e4a68 | -2.61471 | -54.20451 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6983f061-c158-37ba-8e61-40b66813f41f | -2.60197 | -54.2204 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b98cb8d8-8450-349e-8846-c7e7b4e554b0 | -2.02823 | -51.19346 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d7608ed-fe7b-3173-9d87-105b43cedb1d | -4.02018 | -46.99789 | 2024-11-30 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87c52a13-7f74-3221-aad6-b30b9afcfc07 | -1.25167 | -54.54436 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d11fbc2c-109b-37d8-9aac-9bd10a640596 | -4.23096 | -47.57463 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 53ceb8e6-dd22-3ef9-8f05-a43a221ce5ea | -3.07517 | -54.56817 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 394eb4ff-d83a-326e-a920-448ad067c732 | -3.97376 | -47.24276 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad2c8b72-b819-319d-922b-304db9327add | -4.0152 | -46.99676 | 2024-11-30 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d6d6d47-d3d7-3e03-9548-ac0c23f32db3 | -1.94848 | -53.33724 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c30de2e1-3ccd-3d47-bc7f-e8989d660e16 | -2.62551 | -54.07059 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad703361-3552-38b0-8db6-6bbcba1c6ce2 | -3.22222 | -50.4445 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88779d7c-3c7b-346a-a889-055d6fb76a3f | -1.70891 | -52.76796 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98c21c75-740f-3e7c-897c-fd43d50c87d5 | -1.76174 | -50.85456 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2044d042-93ec-36b5-a7bc-d62c46d0082b | -3.50487 | -53.83123 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 74eda5d4-ef22-37ff-9cd2-0c3918c10d7f | -3.03959 | -54.05967 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83f404f7-a4aa-3ee6-bd03-157747d5e23b | -3.28372 | -53.00803 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0a6ead6-6c71-304d-aca0-89dd27a57a35 | -1.18558 | -51.77193 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4aab837-9ec9-359e-8747-2b0b7fb30115 | -1.63209 | -52.14806 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e5ce12-a0da-3dec-adc1-df07498b57a7 | -1.34123 | -55.90713 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc54cc49-7099-3996-9360-9ab63471fe32 | -1.49809 | -54.95684 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6df22f1-833b-3330-9958-51a6a7c8890e | -1.76298 | -53.63243 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a45017c3-fb83-35bb-b128-4b9f4fc0ff3d | -3.26446 | -51.62717 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f9b8cb0-f3c9-393e-86d8-6eff2582cc75 | -2.53895 | -54.06443 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7764a23c-aebb-3d9c-ac6f-37d4626bf837 | -3.21746 | -49.83014 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39b0bf10-3d1f-3534-896b-ef399d1052d5 | -1.29768 | -51.73174 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ac797bb-df0a-3d93-88ca-686f346abf63 | -2.41382 | -53.66731 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01628eed-3612-3fe7-9dce-80d6d2b7a47a | -2.72403 | -52.9775 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3f1a9ef-2d8d-3cdc-84c5-2df06d0a2a8e | -2.84714 | -53.03415 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2679fa36-7424-3850-ab83-3bffabd71c06 | -1.1867 | -51.77345 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa9b3391-d841-358e-a8d2-9fd85d2e5ce5 | -2.59413 | -53.98701 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c831d6e2-2b15-34e8-bfdd-6bbddd3ad40f | -3.97054 | -41.51726 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2acaf20b-83d1-3b7d-b5a8-5321343e951a | -1.14423 | -51.67229 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9a13718-ca98-319b-bba5-ef826b89d1f1 | -3.06969 | -54.40763 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ff3e16d-dbe2-3225-b419-b0789c4409e4 | -3.71682 | -47.14943 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7da9d427-a700-31f2-8791-521ebf937757 | -1.4359 | -54.92232 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4919621-d8bf-380d-a54c-a978ac42d34e | -1.21669 | -51.7357 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a067c87-3d53-3a24-a76a-d98e310635fd | -3.38755 | -50.35091 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 742a8421-9e8d-3be4-ae61-d418ea572f43 | 1.19492 | -55.9537 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 260523bd-c93c-38d3-aef2-78c442aec189 | 1.85763 | -55.77471 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a181e84-ce68-3ce0-ba8d-c81bc84f8e6c | -3.07729 | -53.26078 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28ba7cd6-48e4-3ae0-8e91-76e14c9aa21f | -1.69739 | -52.21681 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e663dfff-3e84-3bd5-a4d2-98e5dcf41d8e | -1.61743 | -52.35494 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0b465de-a897-36a8-be81-b7167ae65d18 | -3.35709 | -49.0959 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb85fc9f-aad0-3c0f-9117-df49aa3df70b | -1.1459 | -53.66651 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8308ece0-1fa1-3f81-8fe0-37f32a73530f | -1.39796 | -52.56892 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bee8dc1f-1d7a-319e-83db-4dbff453b0d7 | -1.833 | -54.52947 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8f2ffde6-80d5-3cd9-94ac-a36c32b86de0 | -3.34827 | -46.30053 | 2024-11-30 05:01:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9944332f-f061-34c3-8a85-c65c3ebf77d0 | -1.18406 | -53.87578 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35765d86-f170-3ff3-8914-88f1425f2dfc | -1.15242 | -51.69007 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32f485f4-1c3c-31db-ab32-9f28c1a49c94 | -1.87659 | -53.59927 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f44397b7-f83b-3fdd-b5cc-3fe709e22cf0 | -2.18168 | -47.14244 | 2024-11-30 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 94245082-6ce6-3214-af7a-58dffdbf784b | -3.26305 | -53.27788 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 986ff31d-d0da-37df-b392-ac9e80e0d920 | -3.21291 | -53.6225 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d0e6e8-9ee6-306d-a996-d53c6115d386 | -1.56826 | -52.14216 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a77beddd-94df-3056-b965-3bc5cbf4cda2 | -3.12191 | -53.26337 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4906e681-0343-30bc-baf7-9ebc30253564 | -1.45482 | -55.14482 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6dcc5d0-36f5-3186-b352-70656d97ca02 | -2.9798 | -53.27969 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ca87561-34b0-3f5f-9e8e-d48a48f6d7d9 | -2.75256 | -51.65923 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de0086ba-afe2-3750-8705-72f54e420603 | -1.35964 | -55.19033 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9d951f0-5cdb-3380-91b5-942cafaa6321 | -1.71747 | -52.78066 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cc7bab1-026d-34d8-a95b-26e19df918ac | -2.58531 | -54.21782 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff74c934-1cc8-37e8-bab5-7dd7cc5c9937 | -1.68104 | -52.50408 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 216bf55a-cfce-3096-a42e-f4aad6f44505 | -2.35971 | -48.54777 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5b9724e-1d71-3b5d-9af8-cb358440adad | -2.87548 | -54.00945 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95111766-a72e-3e67-af0c-f7fb00261bfa | -1.21008 | -55.89772 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 518c528c-1d38-3518-93f0-e63a91b1059d | -1.249 | -51.78581 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e12e189-3832-3c36-893f-9e57279de590 | -1.32386 | -51.6725 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 15e80cb1-3361-34fb-8952-858918a89444 | -1.63674 | -54.35726 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d252103b-10ac-3fbb-b556-bf361596aded | -1.34946 | -51.38562 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 893f7897-2053-358f-b352-a1f3a5ccada8 | -2.03601 | -51.20613 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1d426b7-c5c8-3757-bb23-7a9aaa045026 | -1.63871 | -53.86785 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 090cd601-e2dd-3605-b48a-508c89ae3ba9 | -1.34532 | -54.97889 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 752533f1-f18c-32dd-8f7b-6578c952617d | -0.96289 | -51.65869 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8971f62-4015-392f-88cb-923687ed8ed6 | -3.32051 | -53.29046 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87ea3959-a23c-324a-8251-e34a9e27d0aa | -3.70751 | -47.15013 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0eab8e7-0f23-3d96-be26-a524be4a6d07 | -3.96381 | -48.09491 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b70a4d6b-b278-39f9-b840-7ddef300f9fd | -3.25318 | -53.85838 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d31a21f2-011c-36b5-ad11-abe5a7da38d2 | -3.30203 | -51.06684 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f9043de-0e5c-3887-a66c-03eb3468aab2 | -1.071 | -53.62991 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4ee15a85-8c90-3ca9-8def-b2c13c0b3358 | -1.69232 | -55.01233 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9cc63a5-ce9f-3288-b24e-181aa39ba5b6 | -2.00271 | -51.1628 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 268e82ab-85ca-3437-8ef0-8ed4b1d77187 | -1.09188 | -53.38808 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e54b7a-4035-3160-bedd-afb4467018b9 | -3.10619 | -50.36902 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7250c3e9-efdd-35e0-bf58-0ded84454c48 | -1.1846 | -53.87233 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19abd2dc-576f-3a71-8a1c-5c6e840f9603 | -1.09937 | -53.60202 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937d382c-4bd2-31df-bce3-a7e3d4b177bd | -3.7835 | -52.40747 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20fd9f4d-1500-312b-ae00-7a6a1d5383f9 | -3.0721 | -50.32782 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 633c6764-851e-3f7c-9ab3-49905fbc28be | -3.72967 | -54.23122 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfe484fd-889f-33bd-8c3f-7932aff5b1fe | -3.09499 | -53.81544 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ded92bc9-e8b5-3e90-afe9-bb19c514e98c | -1.08796 | -53.39112 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c88af68-9e91-39af-8c84-3d9ccd818785 | -1.72305 | -52.49424 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0eab7e1f-1569-3d3d-8d7a-d861d02c9e9d | -3.28655 | -50.62309 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ee5bc5f-22ae-3330-80e6-89cd357adfd6 | -1.65638 | -52.25007 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README91.md)
