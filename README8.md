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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96cd704b-42f8-3881-ae2b-5434de17aadc | -3.5429 | -47.351799 | 2024-11-08 00:56:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e587b01-6b02-3a23-aeb5-537fc599422a | -2.4536 | -53.681099 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 982289b1-0931-3a62-b53e-e1477e0c0585 | -2.7977 | -52.935902 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0467a1c1-80a7-3191-a465-2f06fb0558f2 | -2.1498 | -54.516602 | 2024-11-08 00:56:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb6e3bb8-b3e5-3546-8690-8b29f7056370 | -3.4776 | -52.624802 | 2024-11-08 00:56:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae3c3ee-3375-3d15-9c2a-444cfce7bdba | 1.6698 | -50.988098 | 2024-11-08 00:56:00 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cfdb1532-a6db-3956-987c-f857a0212a90 | -2.6417 | -54.7766 | 2024-11-08 00:56:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e98ec749-b81e-3da7-b4d3-7d58aa037634 | -2.7481 | -53.213402 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0789d2b3-b4e5-34d6-b6e5-4d50ff4643f5 | -4.658 | -46.4245 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad5c900-dded-3937-bc77-b4b7f24bff56 | -1.1488 | -53.6479 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3078f4ed-4da1-3d84-91a5-ebba9ea2de16 | -3.4912 | -54.569901 | 2024-11-08 00:56:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c072f9b2-21ca-3a4d-ad3b-aa851fd4d7ce | -2.8054 | -52.9245 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 276bfaad-df73-3e0d-b3f8-77ef8c35c6fe | -2.2848 | -53.798901 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2201a4ea-9752-3309-abc5-5fc62ab8d6f7 | -2.7579 | -53.211201 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f027b7c9-4a63-3735-bd96-a88cf280efaf | -4.6018 | -46.487701 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a43c7c3-028a-3372-99dd-2d32a5cf5b86 | -3.116 | -53.111301 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7cb51e2-c9f6-3328-a537-aac9233776fe | -1.2504 | -53.371399 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5169a144-d179-36d5-a006-4c30cdd8e982 | -1.1468 | -53.639099 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a01910-19d1-38f2-9a32-2a257592919f | 0.3063 | -51.132401 | 2024-11-08 00:56:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a0f1257e-f7f3-3e3a-b98d-bf6240e3e7ee | -1.5517 | -52.258701 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65a9d33b-8ca8-3920-97d5-02682736a6ea | -3.1474 | -54.4632 | 2024-11-08 00:56:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2afd2a9-219f-36ee-a13f-3306419b019b | -1.7331 | -52.466999 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f36b7f85-c2c9-3e22-a924-01dd6caedd7f | -2.9407 | -52.707401 | 2024-11-08 00:56:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4471344d-6b6f-36a8-aa30-901379738009 | -1.4571 | -53.419899 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e381dea5-9398-324d-b1b4-4ee8b6ccb35b | -2.2577 | -53.7253 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 617c7b75-a7f8-3932-9dcf-89438aafb148 | -3.0388 | -53.2682 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 059c8cc8-0005-3169-ac91-5a9f56439123 | -3.0277 | -51.525002 | 2024-11-08 00:56:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccc217e1-92ca-344d-8db0-3f9376238ee0 | -1.721 | -52.459099 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09ba6429-e516-3088-8f7e-ae98290fafe7 | -3.4838 | -52.617 | 2024-11-08 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 7debb007-9952-311c-96ab-c408cf8173b4 | -3.5446 | -47.3855 | 2024-11-08 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 812fafab-a71f-3383-a335-ef9d75ed4215 | -3.5632 | -47.3629 | 2024-11-08 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0be0f5ae-8cd5-3aaa-9553-4b30a2c9ad60 | -1.3961 | -47.5103 | 2024-11-08 01:00:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ca6ff965-5771-39d1-84cc-139050b2ed8a | -3.9854 | -48.1708 | 2024-11-08 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8c7fa72e-026c-3a01-9e51-7fdea12d7b21 | -4.6834 | -46.4296 | 2024-11-08 01:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 236.3 |
| e3b3e6e4-e9d4-3f0b-9be1-8078863c9a29 | -3.0396 | -53.2805 | 2024-11-08 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 128b3b01-4107-3457-a404-22c3f19e8fc5 | -3.9669 | -48.1716 | 2024-11-08 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| d9be7b92-bcfa-3bbf-adcd-b096829590b2 | -3.1642 | -54.4654 | 2024-11-08 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5af7b31f-8965-3154-ae63-18f86f111f21 | -3.7255 | -41.6748 | 2024-11-08 01:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| cb063bed-0e3c-3d36-9b0e-c97b93c2c3d2 | -2.6764 | -51.8189 | 2024-11-08 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3d3e0365-0988-3573-8bf6-ea33e78dada6 | -2.82 | -52.9613 | 2024-11-08 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 41496f55-6a25-3585-9cba-9947ad3a2081 | -6.264 | -39.3797 | 2024-11-08 01:00:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 52.7 |
| 242b67e9-ca2f-3922-a445-b07d98bf23fd | -2.6228 | -51.3038 | 2024-11-08 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 01763088-5ba4-3117-b583-06c26c6d669c | -3.0698 | -45.747 | 2024-11-08 01:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 0be2738c-7425-32b7-a1cc-b28605de5b7e | -4.7018 | -46.4508 | 2024-11-08 01:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 8d8a62cf-977d-33c3-b905-ac74097e487c | -2.6214 | -51.7585 | 2024-11-08 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 6e7f7f2e-424c-3d04-9278-1de71259b7c0 | -3.9485 | -48.1508 | 2024-11-08 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 0b41c6b8-55ba-3b63-af64-c3bdde752a82 | -3.5447 | -47.3636 | 2024-11-08 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3485d5ab-95c9-32a6-8c30-f577e6543c27 | -2.8016 | -52.9414 | 2024-11-08 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 270.8 |
| 9bf272db-eabe-3cba-a135-eb89c0d7b4d4 | -3.9483 | -48.1724 | 2024-11-08 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3de45581-c62e-374a-b827-72e60435a1fc | -3.0947 | -53.3196 | 2024-11-08 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 5d709480-4676-37c7-baed-a293747ae2bf | -2.82 | -52.9409 | 2024-11-08 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| a290925e-b548-3518-b636-a6cb30220d2b | -3.5631 | -47.3847 | 2024-11-08 01:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 3d491e0f-0a21-39ab-8e9f-2fac41ff832b | -3.1641 | -54.4854 | 2024-11-08 01:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7e513869-8d00-37a9-91e0-8203544f1a47 | -2.7832 | -52.9418 | 2024-11-08 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| d98535f5-363f-3810-90c2-f074177dcd7f | -4.6832 | -46.4518 | 2024-11-08 01:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 390.4 |
| 37b4516e-a475-3b48-b796-e0029ddc3ab3 | -2.6214 | -51.7378 | 2024-11-08 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b4c98748-c642-36f2-a98e-7b4b18f70d3a | -3.967 | -48.15 | 2024-11-08 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 8050cb20-eee8-3312-9cbe-13a9ee8d49c2 | -2.8016 | -52.9617 | 2024-11-08 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| a343f3ca-983b-39da-9312-67059299f9dc | -3.7254 | -41.6987 | 2024-11-08 01:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 4e868673-4db6-3750-94e8-0fea28f761d7 | -4.6269 | -46.5213 | 2024-11-08 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 0be2f5ad-bbb7-3cb1-8d97-e2390e492c44 | -1.3776 | -47.5106 | 2024-11-08 01:00:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5ca80b33-b4f8-366f-9515-de17eefcf104 | -3.7066 | -41.6997 | 2024-11-08 01:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| c002b5c5-deae-35eb-b08d-fbd453b42c23 | -4.6646 | -46.4528 | 2024-11-08 01:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 004b4e78-9036-3fd4-a718-631f942e923d | -4.68 | -46.43 | 2024-11-08 01:00:00 | MSG-03 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1be755d4-9e5a-3aad-9d5d-2bf3278ddd98 | -4.52 | -45.65 | 2024-11-08 01:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 832de8a6-d4dd-3d28-9faa-686d52c0612d | -4.52 | -45.7 | 2024-11-08 01:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32e921bf-d902-3978-b1f6-88a2a0767d61 | -2.78 | -52.94 | 2024-11-08 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cafb6b99-879b-38f6-ac8b-b7d299300f2e | -4.49 | -45.7 | 2024-11-08 01:00:00 | MSG-03 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4d9db4-6697-369e-b9ae-970ef3ebd291 | -3.7255 | -41.6748 | 2024-11-08 01:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 2270f639-2006-3401-9d1c-f8c2307ddd2a | -3.7066 | -41.6997 | 2024-11-08 01:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 6e87fc72-3de7-3fe3-816b-1d2c98620af1 | -3.5631 | -47.3847 | 2024-11-08 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0c223666-9b3a-35b9-b18e-693e94222942 | -1.1489 | -52.0099 | 2024-11-08 01:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 0570c119-11ae-3543-9026-df09d016d7ac | -6.2832 | -39.3528 | 2024-11-08 01:10:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 6ddbeca5-961e-3b5a-8e06-8d2975bea340 | -3.9669 | -48.1716 | 2024-11-08 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 445b53de-1275-33de-8afa-796f796df378 | -4.6646 | -46.4528 | 2024-11-08 01:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 70225bf0-12ed-313e-8821-9fb13eb647d7 | -2.82 | -52.9613 | 2024-11-08 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 8858e382-c66e-30b5-9669-799649426071 | -3.5446 | -47.3855 | 2024-11-08 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| e0a8d56b-b592-3c30-9c01-54081ffeea1e | -4.521 | -45.658 | 2024-11-08 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 2d5c6a6a-ee39-3af0-a367-9de9a8fcc4f9 | -6.2642 | -39.3546 | 2024-11-08 01:10:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 80.3 |
| a5a84812-91c1-3839-8dd1-165c9140fa9b | -2.7798 | -54.0334 | 2024-11-08 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ea961267-3266-3e73-a045-ba0fad552ad7 | -3.5632 | -47.3629 | 2024-11-08 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6288f248-1c33-3e15-840b-0aedb56a258f | -1.3961 | -47.5103 | 2024-11-08 01:10:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 93add711-237e-3361-b7b8-419736e5d570 | -4.5395 | -45.6794 | 2024-11-08 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 01835b3f-dd77-302d-8426-04757c645c39 | -3.9854 | -48.1708 | 2024-11-08 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 42687818-982e-329e-9ec8-75deba720a11 | -3.5447 | -47.3636 | 2024-11-08 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a7171471-5383-39cc-b87a-233f6b3f2221 | -1.1489 | -51.9894 | 2024-11-08 01:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 50c74cb4-0510-3a0c-a4c8-5144f8126f19 | -3.967 | -48.15 | 2024-11-08 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5029a773-4c42-3ded-9f4c-3bd550d1dbf3 | -3.9483 | -48.1724 | 2024-11-08 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0602e494-8006-32bd-9d47-92818d67577a | -4.5022 | -45.6815 | 2024-11-08 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 146.0 |
| ad6a5419-abec-3664-959f-0b606c6eb173 | -6.2829 | -39.3779 | 2024-11-08 01:10:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 66.9 |
| a3c84113-4cbe-3429-9cdc-cc5a68908143 | -4.5207 | -45.7029 | 2024-11-08 01:10:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 223.3 |
| 38427a4b-c433-3a13-95dc-bb4d52d74e4d | -2.8016 | -52.9414 | 2024-11-08 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 241.9 |
| 5913e2dd-5a48-3df1-bb31-bf5de285027a | -3.1642 | -54.4654 | 2024-11-08 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 9b82f67c-e8ea-353b-92c1-7addb0fd1b62 | -3.1458 | -54.4659 | 2024-11-08 01:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3d033cb6-ec15-3d4f-85bb-93161a854484 | -4.6834 | -46.4296 | 2024-11-08 01:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 28b1d43a-77a9-39fc-98d2-d8722d41c83b | -4.6269 | -46.5213 | 2024-11-08 01:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f29ac971-6a67-37b9-a017-e213878b1723 | -3.0698 | -45.747 | 2024-11-08 01:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 62c35767-da5b-337b-8852-a20019e1a630 | -2.8016 | -52.9617 | 2024-11-08 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |
| c939ce70-b1bb-3015-b33c-3217841dc97d | -6.264 | -39.3797 | 2024-11-08 01:10:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 41d137de-8198-304c-ad5f-789d333d4d75 | -3.7254 | -41.6987 | 2024-11-08 01:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |


[Clique aqui para ver as próximas entradas](README9.md)
