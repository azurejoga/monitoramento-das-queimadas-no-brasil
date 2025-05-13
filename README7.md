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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3253e1c-f283-3305-b4b0-fc16168e02df | -14.63663 | -45.09728 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6a183a5-af6d-3d1d-99d3-b60bec29a095 | -12.19223 | -46.71684 | 2025-05-13 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7979a99b-39ed-3f54-8fb0-9dbc1b3c8d97 | -12.55855 | -49.66112 | 2025-05-13 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7721b1de-199c-3750-91f7-b6fc46d3979a | -12.29021 | -52.47015 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b045255-926f-307b-9cb3-d128cb4d8d48 | -14.18619 | -45.47123 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 824c7721-395f-3d90-9bd2-a3f393aa4621 | -12.1503 | -48.01189 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e1046800-154d-3717-8b7e-c0cb29588771 | -17.11274 | -49.13957 | 2025-05-13 04:14:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d7cd2f1f-ad56-3b17-9908-e13cb1dd8bd8 | -13.09214 | -52.29213 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 062bf1e5-b2c8-37cb-b098-729b89be914e | -13.97909 | -56.80094 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| cb5856ff-e098-367e-8bcb-a8333e4dff68 | -13.37527 | -47.60157 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ff0bbce-de09-3f1b-a8c6-1aa1969c7bdf | -13.57369 | -52.87267 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2792f08b-cfc2-38d1-8059-a74c8cc90ad9 | -12.29997 | -52.47203 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9ef2bfe-086b-3737-b410-320e6f83fdbf | -13.67065 | -53.93425 | 2025-05-13 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87a5acaf-b079-3cf4-b352-8fcb0014c569 | -15.82421 | -45.16632 | 2025-05-13 04:14:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7e79ce61-c1df-31f1-8409-578f466f8cb8 | -12.18247 | -46.71114 | 2025-05-13 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16e40dc8-5406-3e2f-8aa2-c7e326d906cb | -16.79706 | -49.0985 | 2025-05-13 04:14:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2641a74d-9b4c-3339-b909-bd9d926c91c1 | -13.56773 | -52.87721 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4d07287e-d3ee-3d49-a4b6-4319b16bef0d | -15.78191 | -43.34222 | 2025-05-13 04:14:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4141b67b-a38c-3459-91f9-51d6062b697f | -10.48683 | -46.18267 | 2025-05-13 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c48d5626-bd91-3888-beba-78c43b767d4d | -11.6222 | -48.11878 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec4ac7f4-c122-3cf5-82f4-39783ca99550 | -11.60738 | -48.00408 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6412369d-1ab9-3e44-99ed-f50691355e7d | -11.77531 | -48.70099 | 2025-05-13 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15a79a37-b724-36ed-96fc-6860f8defa4a | -15.84429 | -49.67448 | 2025-05-13 04:14:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bdf5231-ca13-35b8-bfeb-8dad4b3ed973 | -13.56665 | -52.88279 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8f80d4e6-710c-3611-97f1-9fdc34713a50 | -14.80361 | -46.75579 | 2025-05-13 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cea2c22-cd09-3e64-b8ad-4d588a0b135c | -11.79599 | -47.41017 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27f005dc-0408-325a-8716-0e0675642e7b | -12.14739 | -48.00676 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b50f56c0-d27c-3091-bc6c-478e3e05df43 | -14.80702 | -46.75633 | 2025-05-13 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e791ea40-7ca2-3ccf-a03b-68b2a37db878 | -11.61925 | -48.11355 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de8ae1f-9861-3a94-af4e-b64c15573a71 | -14.195 | -45.48005 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d9d82a3-1803-3ce5-bc9e-25280b8b3e52 | -12.14662 | -48.01122 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc4f5913-921b-3080-996c-514c9bcda5ad | -14.66249 | -45.12716 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54ec4d9a-b117-3602-9943-273c7ccfdb57 | -14.19168 | -45.47948 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 486b8b14-769b-3d3d-bb0f-8e2e6566ab96 | -11.00498 | -50.76441 | 2025-05-13 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7480745-918e-3fea-ae74-5b9907b2fd7b | -17.66441 | -46.68223 | 2025-05-13 04:14:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aab1ddd-4a50-3476-83c8-47b54b1080fb | -12.29099 | -52.49324 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7fa3b9fe-602a-3bc4-9ca7-bd1f2a7a8e54 | -14.65918 | -45.12661 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f731b20-036d-3b6f-b89d-6cd3935d9c61 | -11.12012 | -43.33821 | 2025-05-13 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6caabc5a-a421-3117-976c-198d5dd36d88 | -12.82935 | -47.39547 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 110e3cab-5919-38be-8a0c-cbef63f0dba5 | -11.62003 | -48.10898 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d9650ee-766a-3ccf-86d2-4bbfc6f179c5 | -14.18676 | -45.46766 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 334f160b-e243-330d-b7c2-64b25f5671d1 | -17.90287 | -44.40266 | 2025-05-13 04:14:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aef4046a-5b1a-3e7e-a271-e7b0ee2c3dfa | -14.18561 | -45.4748 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4620574a-217d-3d59-abd2-c16e89371c87 | -13.36166 | -47.59539 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0bbab97-1bbe-3f86-9652-969280d30674 | -14.18734 | -45.46409 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 746335ef-2ff1-3508-918e-c985e7e72c1d | -11.80155 | -44.27739 | 2025-05-13 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01136a73-bd1d-36c0-8907-6f630b1610fa | -14.89649 | -48.12579 | 2025-05-13 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cff00e5-6170-3761-a6fd-cfbae5efdd14 | -13.67003 | -53.93737 | 2025-05-13 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 397f1cbd-4ecf-3a12-b506-11a897fda4d9 | -13.09196 | -52.29446 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79a78d20-71fe-3a76-a31a-afcae48c494d | -11.77916 | -48.70168 | 2025-05-13 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d606b24a-d19a-3c80-8247-1c2cdec89504 | -11.7883 | -44.27523 | 2025-05-13 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21739078-cec0-3654-8e78-441e4f74a267 | -12.29695 | -52.47277 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac6ec7a0-2f21-366f-9d39-8ee9c25b9b4c | -13.5527 | -52.86727 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 37ed9c17-d5a9-3619-b7f3-1e559d38e50d | -13.06587 | -52.01523 | 2025-05-13 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8f786b7-af61-3afb-9ece-b15def319df0 | -10.65945 | -44.41214 | 2025-05-13 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 198d6243-0d15-307f-a4da-6567e2a7582c | -11.78843 | -47.40128 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62d6dc79-2558-3668-a903-de590c0bea24 | -12.15476 | -48.00809 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 34b1906d-849d-32c3-a7be-099a58d49077 | -14.65974 | -45.12305 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1709b338-03a6-38e4-97f4-79d66a4a1cd8 | -11.79957 | -47.4108 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6036056f-37f7-3510-ab12-f0895dc2bcb0 | -14.17717 | -45.46686 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0e9f1b5-de81-3e58-8c19-b3354f022b60 | -14.66305 | -45.1236 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28800c3f-eddd-3158-bdab-6196c8d6ced2 | -13.37231 | -47.61928 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aed7d828-0a91-3be3-b2ba-41ec3d42b3a5 | -13.55412 | -52.8687 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 13f0c4c7-86e1-328f-8cf1-2d8537042d88 | -10.66276 | -44.41269 | 2025-05-13 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48fe700e-9a68-3521-94e7-c6bc8c2b0e1a | -14.18446 | -45.48194 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b46e0ae-a830-3c72-84e3-7fc34f2f7b4b | -10.18111 | -48.028 | 2025-05-13 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51e8837b-5330-3659-86e0-c35f3b6e6018 | -13.36524 | -47.59585 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c03fa5d-f31f-3cc3-be9d-d95c7f565699 | -11.77614 | -48.69611 | 2025-05-13 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d59444c-3414-386f-86a3-6de7bea0a16f | -13.57474 | -52.86718 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ddc9b7dd-58b8-3396-ba8c-8513065d0b68 | -10.4194 | -44.89474 | 2025-05-13 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfe347c3-1b60-3fdc-abf8-77677e386434 | -12.15107 | -48.00743 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 44f18ae6-08d6-3619-90e2-3783868ac1ea | -11.79422 | -47.41094 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48b83c45-a658-356e-9047-2981436ddc1f | -10.00377 | -47.83973 | 2025-05-13 04:14:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e176d8ed-ed4d-3141-950a-67c36340e9de | -12.18182 | -46.71503 | 2025-05-13 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a26f5ae-0d69-366e-917f-254868ecfcf8 | -11.6111 | -48.00471 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a8b92a2-531c-365f-9068-e04036d135a4 | -10.04536 | -49.66612 | 2025-05-13 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d07116a-27be-31d4-86e2-5e16a8b3e6fb | -14.18106 | -45.46385 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 109faaa3-46ad-3c2a-a234-9ab8f404640b | -12.18941 | -46.71234 | 2025-05-13 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65fa447f-8f1d-3b3a-9463-e6e7f7f0ff51 | -16.67989 | -43.88324 | 2025-05-13 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536db9b4-7980-35ad-8f82-32ea44bf0f58 | -14.18779 | -45.48249 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 709fd21c-a3ec-3122-aed9-c2c4cdc29023 | -13.67583 | -53.93561 | 2025-05-13 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77521290-203b-39ee-aeed-721016aa8806 | -16.55272 | -46.85136 | 2025-05-13 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c721b081-421b-327c-855a-67909010f4dc | -14.18049 | -45.46742 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06bc6b34-d1d4-3bcd-bea4-8b331c1d4668 | -11.8021 | -44.27387 | 2025-05-13 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35df4a38-d94b-3144-8967-1b470032dcbd | -14.17992 | -45.47099 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56e3d698-25f2-39d4-900e-053b2d9cf253 | -13.97291 | -56.79948 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 05f6a2e0-944a-3eef-ac1b-db8a9cd6c7e7 | -15.84513 | -49.66971 | 2025-05-13 04:14:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 986f0539-7795-30c2-b389-c8d225ad1f69 | -12.83794 | -47.4096 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8c7c3f7-46bc-3211-885d-afd017c81515 | -16.29669 | -45.09769 | 2025-05-13 04:14:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48a12017-1a3c-3237-84f7-b842bc912a7d | -12.18594 | -46.71174 | 2025-05-13 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37c3f4c6-df60-332f-b47b-9edf150c1c05 | -11.78773 | -47.40546 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e87e0e1e-f778-3041-bd15-66ed797fbf57 | -14.641 | -45.11261 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15015b98-d009-3cc1-bcc7-a7e03d12dffc | -14.63938 | -45.10139 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7794438f-1065-3e4f-88cd-304ad4bd223a | -13.0612 | -52.01435 | 2025-05-13 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19490f05-024e-3d54-8b12-5d79fbf33790 | -13.56177 | -52.88172 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1edff943-709b-35c3-901f-e3fb75f1e32b | -10.49093 | -46.17938 | 2025-05-13 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebc29126-d467-3086-b10b-548c997989a6 | -12.35197 | -49.97218 | 2025-05-13 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c20ed2fe-6395-35dc-9a23-2131828cdee6 | -12.18529 | -46.71563 | 2025-05-13 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04cb9061-6e09-301b-b484-2b70608c824b | -11.25815 | -52.47175 | 2025-05-13 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9b45ee6-420c-3ba3-b293-1a7c251a50eb | -14.18894 | -45.47535 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README8.md)
