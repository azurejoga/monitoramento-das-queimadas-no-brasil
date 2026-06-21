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
| 17305409-d980-328c-b414-77c0183143e7 | -9.1818 | -58.05812 | 2026-06-21 06:05:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0abbbd40-b4ff-31b5-96be-9e89d19b7383 | -10.68386 | -60.7507 | 2026-06-21 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 08180bb2-956d-32d7-b1bf-0efc69a806e0 | -9.18801 | -58.05572 | 2026-06-21 06:05:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3baf3f22-6cb4-34be-be39-9a5104e356ff | -9.77869 | -66.62973 | 2026-06-21 06:05:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c818984-dddd-3908-9b63-533edb479fc8 | -10.68912 | -60.75146 | 2026-06-21 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d76246f1-860b-3b5a-b597-8724147549cb | -10.68954 | -60.74818 | 2026-06-21 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0027af0-dbd3-3b44-a527-6ea24bf1e824 | -10.27431 | -60.54938 | 2026-06-21 06:05:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cdbc85c-b0a6-36bb-90c1-b4f26c5363c0 | -10.68302 | -60.75722 | 2026-06-21 06:05:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| aa3b4eaf-f34b-3523-a061-d0c34eda3774 | -11.1165 | -54.1499 | 2026-06-21 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ed5b4992-4d22-3ec8-8e55-b8e55e3a53b3 | -11.0976 | -54.1516 | 2026-06-21 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 9ada882e-e93a-3eeb-9df3-312e206250c1 | -11.1168 | -54.1294 | 2026-06-21 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| b56dc745-e73e-37fe-962d-8382127246ce | -11.0979 | -54.1311 | 2026-06-21 06:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| f22dad82-a275-375c-a3e5-5f3b5184c555 | -11.0979 | -54.1311 | 2026-06-21 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 251a9b64-e7ea-394f-ad07-b907677ecfad | -11.0976 | -54.1516 | 2026-06-21 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| b335f5fd-eb01-3e1b-9344-25230f2ea71f | -11.1165 | -54.1499 | 2026-06-21 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 04b24d88-1183-3c00-b19b-c38a9db93c34 | -11.1168 | -54.1294 | 2026-06-21 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ca59a676-d006-387b-ac91-ed9bdb8dad8a | -11.0976 | -54.1516 | 2026-06-21 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 67b7963d-0711-3e87-a430-4f001cf07e08 | -11.1168 | -54.1294 | 2026-06-21 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| dabd0650-36f0-3e86-ab33-736fb551a9a6 | -11.1165 | -54.1499 | 2026-06-21 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 211998d6-5455-3976-8c7a-76dca19b96eb | -11.0979 | -54.1311 | 2026-06-21 06:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| d3bbf13b-3700-3705-8972-b80da8d005f6 | -11.0979 | -54.1311 | 2026-06-21 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 179b5fb7-ada8-3487-b6f6-eb24bfcaa17a | -11.1168 | -54.1294 | 2026-06-21 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| c44cc81d-dbe3-3881-9091-2297fb95150b | -11.1165 | -54.1499 | 2026-06-21 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 162e860f-629b-3944-b3dd-60608b1d1b33 | -11.0976 | -54.1516 | 2026-06-21 06:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| e1d14131-52bc-35ca-a196-7c71588222b8 | -11.1168 | -54.1294 | 2026-06-21 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 68b2e8eb-965a-3f8b-87aa-d7e0464c2cd4 | -11.0976 | -54.1516 | 2026-06-21 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 1e03e7ac-232c-30e6-9f90-ed439bec404c | -11.0979 | -54.1311 | 2026-06-21 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 0b158aae-c60a-3ed3-a1f6-095f3d0dc394 | -11.1165 | -54.1499 | 2026-06-21 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 922698cf-3e61-33a9-832f-d61099860ee3 | -11.0979 | -54.1311 | 2026-06-21 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 1489965e-a3e6-38be-a977-44c3f1cc8a36 | -11.1165 | -54.1499 | 2026-06-21 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 8e991e5c-168f-39bc-8c25-d7c06c68881d | -11.1168 | -54.1294 | 2026-06-21 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 3087b742-9762-396a-a0b7-2cecb0fbc7a6 | -11.0976 | -54.1516 | 2026-06-21 07:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 159.2 |
| 9c3be4b6-b1b6-3223-96a2-739867d92bb6 | -11.1168 | -54.1294 | 2026-06-21 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| e14505d7-0cd7-3361-ac80-a306c7c9b345 | -11.0979 | -54.1311 | 2026-06-21 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| a6da54af-53bd-33ad-a6c4-51c87d458f64 | -11.1165 | -54.1499 | 2026-06-21 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 19f8b5cb-9436-36df-81bc-0bd7f17062d0 | -11.0976 | -54.1516 | 2026-06-21 07:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 166.8 |
| e0f3c8df-3a13-37a3-ac2f-26941c3ec1c6 | -11.1165 | -54.1499 | 2026-06-21 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2c04b272-5d40-322f-8804-bb0acd90a8d7 | -11.0976 | -54.1516 | 2026-06-21 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| e29be7e7-8ae8-380e-8194-2e2bf16bbfde | -11.1168 | -54.1294 | 2026-06-21 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a0ab677d-2cd1-3825-9725-d8771a29691d | -11.0979 | -54.1311 | 2026-06-21 07:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 630e7dcc-d7c3-3997-a1b6-4f1e619161d3 | -11.0979 | -54.1311 | 2026-06-21 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| cab3eef3-99ab-3606-b748-b342a7b97947 | -11.1165 | -54.1499 | 2026-06-21 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 9ae50890-71c1-3170-8cc3-2f545ee698c2 | -11.0976 | -54.1516 | 2026-06-21 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 43cfff92-f7c3-3e64-9b99-8a722ecf1982 | -11.1168 | -54.1294 | 2026-06-21 07:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 96d90d33-333a-34d4-85dd-4dc430084955 | -11.1165 | -54.1499 | 2026-06-21 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 45f88642-d744-3952-96d4-4adf650fe2aa | -11.0976 | -54.1516 | 2026-06-21 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| ee5a5d16-1531-344c-836b-38f153a113cf | -11.0979 | -54.1311 | 2026-06-21 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3b271327-8b34-3cda-b4c7-8cecec443172 | -11.1168 | -54.1294 | 2026-06-21 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7eb55f91-1279-31ab-92a0-0382379c3a34 | -10.68447 | -60.74909 | 2026-06-21 07:41:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ccfb5f93-ab10-3aeb-94e8-1df4b8216656 | -11.0976 | -54.1516 | 2026-06-21 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 8007c27b-fab8-36f9-880d-d239ae9a7a4f | -11.1168 | -54.1294 | 2026-06-21 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9e7a0a3f-d38c-3e0f-97d2-c41dc6029193 | -11.0979 | -54.1311 | 2026-06-21 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 109b9400-df2b-32b1-882c-0b8ef328a84a | -11.1165 | -54.1499 | 2026-06-21 07:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| af58f9ee-b06f-38ba-8d78-f2c28955a183 | -11.1165 | -54.1499 | 2026-06-21 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 3a0c37d7-67ba-3532-9efd-64589b9f6b74 | -11.1168 | -54.1294 | 2026-06-21 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 0c5376fc-3ef6-3190-b07b-4b6220ef2d0e | -11.0976 | -54.1516 | 2026-06-21 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 14f31715-9ffe-376f-b822-aa774517f1d8 | -11.0979 | -54.1311 | 2026-06-21 08:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 12348401-5500-303c-b1c6-575a3cb2b1ce | -11.1165 | -54.1499 | 2026-06-21 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| ca3b3ee1-069c-36a2-b82a-36b27e820c62 | -11.1168 | -54.1294 | 2026-06-21 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 13f49277-aa61-3f91-8954-19d58404b358 | -11.0976 | -54.1516 | 2026-06-21 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.6 |
| f2726f77-acc2-3ca2-a0fd-2864f555c9bf | -11.0979 | -54.1311 | 2026-06-21 08:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 7d9a4137-b641-31f4-b9a0-ac3a75346bc7 | -11.0979 | -54.1311 | 2026-06-21 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 341fb0d0-7859-3845-bc0a-7fea99792309 | -11.1165 | -54.1499 | 2026-06-21 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| dd30ec4f-80f7-30b7-9b17-56832eed99a5 | -11.1168 | -54.1294 | 2026-06-21 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| b4dffde9-347f-3850-94c9-c7e83e163814 | -11.0976 | -54.1516 | 2026-06-21 08:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 5b4b36f7-9f73-3660-a717-2a3335f9803a | -11.0979 | -54.1311 | 2026-06-21 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e85cbe77-f14b-37ed-85ca-2762784d1b90 | -11.0976 | -54.1516 | 2026-06-21 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.6 |
| e5b71b28-b51f-30d8-b657-75a3ae46d1ea | -11.1165 | -54.1499 | 2026-06-21 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| fc979ebd-a20a-3ffc-9206-029acb195c2f | -11.1168 | -54.1294 | 2026-06-21 08:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 64844943-c40a-3c23-838c-09456977282a | -11.1168 | -54.1294 | 2026-06-21 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| deccbddc-ac1f-3c18-82fe-a4b9911ca2f7 | -11.0976 | -54.1516 | 2026-06-21 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 50c1b134-4f53-3a81-805f-e68a97f3f61e | -11.0979 | -54.1311 | 2026-06-21 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 0d12fd02-0b4f-3cae-8fa3-9cae1c3f5b22 | -11.1165 | -54.1499 | 2026-06-21 08:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ae382756-17cb-3d54-8d74-ad0fab3b32ab | -11.1165 | -54.1499 | 2026-06-21 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 613f79f6-66f2-30d0-9d05-9f450cadbbe6 | -11.0979 | -54.1311 | 2026-06-21 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| f08593f4-b083-32e7-acac-c9a3a81dce7f | -11.0976 | -54.1516 | 2026-06-21 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| ec2e0e18-f600-3d17-b72c-7899b1dfb505 | -11.1168 | -54.1294 | 2026-06-21 08:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| f9f5b1aa-d92a-368d-950c-6260ef268080 | -11.0976 | -54.1516 | 2026-06-21 09:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 412621a2-ccae-3ea6-8bf1-fc9a3f603cbb | -11.1168 | -54.1294 | 2026-06-21 09:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| aa1e1046-925d-38ed-acd0-9025712f5243 | -11.0979 | -54.1311 | 2026-06-21 09:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| fe160e02-25b3-33ff-a3cd-970b77ed1f84 | -11.1165 | -54.1499 | 2026-06-21 09:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| b17b6b12-de51-3dfc-b2e0-662da7343d5e | -11.1168 | -54.1294 | 2026-06-21 09:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c8a23976-8739-395a-8d9f-0c5a9c69280d | -11.1165 | -54.1499 | 2026-06-21 09:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| c943bdd3-7723-3714-b639-07badc0fd8b2 | -11.0979 | -54.1311 | 2026-06-21 09:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 6bbefaeb-9868-3b62-8a28-86b6ab333168 | -11.0976 | -54.1516 | 2026-06-21 09:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| d7532a3a-8c9b-3c7c-adfc-ef8a17c766ac | -11.0976 | -54.1516 | 2026-06-21 10:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| a3857b99-aeb5-3cd5-9fc8-c7bee0a17a0e | -11.0979 | -54.1311 | 2026-06-21 10:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 80aa4841-0197-3bb8-87c9-55929393ba68 | -11.0979 | -54.1311 | 2026-06-21 10:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 431ad1dc-3508-302f-ae88-7b552b6f72f5 | -6.49852 | -42.22681 | 2026-06-21 11:49:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 15ec65cb-3a77-3cdb-b6dc-4f10efc3fc32 | -10.52062 | -46.39941 | 2026-06-21 11:49:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09766640-d07a-3dd9-bc37-8c52978734f3 | -12.62549 | -44.62387 | 2026-06-21 11:49:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 59250b12-6c74-3dd6-88e9-16803334507e | -2.56921 | -47.19881 | 2026-06-21 11:49:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ae31ec20-7c1e-3e3f-94e1-a09be8f84dc5 | -11.06512 | -52.4889 | 2026-06-21 11:49:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 13cad890-2317-3613-80e5-582f248891b6 | -11.05343 | -52.487 | 2026-06-21 11:49:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c13a7927-16be-37b4-a255-66fd343194e7 | -10.69489 | -47.69579 | 2026-06-21 11:49:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c4cb8e3b-0808-30e4-83f3-6c16bdeaa5d1 | -11.64308 | -48.53135 | 2026-06-21 11:49:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 21d971c2-ec23-3e8c-9f02-9a335bfdfecf | -11.11098 | -54.13335 | 2026-06-21 11:49:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 50187107-8522-3e8c-8cfa-cc273c5736ac | -10.90958 | -49.4877 | 2026-06-21 11:49:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 17de39dc-2d66-3048-afb2-3782ee40535f | -10.54082 | -47.73444 | 2026-06-21 11:49:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 51f22803-dbe8-3d18-9448-d6c4b7c8d9e8 | -12.61584 | -44.62255 | 2026-06-21 11:49:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README11.md)
