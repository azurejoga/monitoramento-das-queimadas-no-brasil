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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd8feca2-951c-3770-a274-d060af6ec11a | -11.8653 | -57.3582 | 2026-01-13 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae74378-53e4-3136-bb5b-7ce3ee586020 | 3.7327 | -60.5541 | 2026-01-13 00:57:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1ac9e3-214b-301d-ab67-82b3611b8a44 | -11.8555 | -57.3605 | 2026-01-13 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03283603-8f3a-373f-955b-92002a8f4cc0 | -11.8636 | -57.3507 | 2026-01-13 00:57:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59035c09-d652-3b2c-b576-76487b267a0f | -5.099 | -43.2444 | 2026-01-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 4b2c744f-121b-3453-b980-7a0d43607b8e | -5.118 | -43.2198 | 2026-01-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 282d3ee4-af38-31f7-b1e3-6e0a925af5f0 | -5.0805 | -43.2224 | 2026-01-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1a71d90f-ae7d-3a2f-b390-81da06ad8947 | -5.0992 | -43.2211 | 2026-01-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 334.8 |
| 9bbb9d78-ecda-3096-a036-04d0597302ad | -5.1178 | -43.2431 | 2026-01-13 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 515de3b6-46dc-36fb-bc46-427c5a482d66 | -5.0803 | -43.2457 | 2026-01-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 47b20477-8343-3500-b711-ba05636f39a4 | -5.099 | -43.2444 | 2026-01-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 1f4bf61c-c7ca-3d26-abf9-9243456981cd | -5.118 | -43.2198 | 2026-01-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 5626df81-21e8-3281-8275-6e68bfd0444d | -5.0805 | -43.2224 | 2026-01-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| eba0a508-03c0-36cd-a393-c44e15f88378 | -5.0994 | -43.1977 | 2026-01-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3d5388d2-ef01-34ad-8873-f25576d5a108 | -5.1178 | -43.2431 | 2026-01-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 88f84780-8fbd-36d8-a3e0-e1a164504928 | -5.0992 | -43.2211 | 2026-01-13 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 461.3 |
| 00c206e2-9aab-336d-9e51-2b24a2233b7d | -5.0992 | -43.2211 | 2026-01-13 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9a2f6ece-d3aa-326a-8e1d-46b87e56b529 | -9.9691 | -36.2802 | 2026-01-13 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 0bff1f0d-8064-3ce5-b919-db14e570c242 | -5.0805 | -43.2224 | 2026-01-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8a85ebff-9a08-3130-b56c-9839f95f97fc | -5.099 | -43.2444 | 2026-01-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 3dfdb49a-0763-3323-bbbc-6fd24a144fdf | -5.1178 | -43.2431 | 2026-01-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c00f6d94-31a5-3f23-b588-b606ef5c5491 | -5.0992 | -43.2211 | 2026-01-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 307.6 |
| 804f4cdb-9526-3717-a3e4-1a35d76be590 | -5.118 | -43.2198 | 2026-01-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 45465f57-2beb-34c3-9770-4c0c0337c448 | -5.0994 | -43.1977 | 2026-01-13 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e5942a91-b8d8-3440-ad12-52a6c82adff5 | -5.1178 | -43.2431 | 2026-01-13 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 6bd14a5d-23ec-31aa-9845-3cbbc7147227 | -5.0992 | -43.2211 | 2026-01-13 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 328.8 |
| 182971ff-291e-3289-a406-f9ee20241c9a | -5.118 | -43.2198 | 2026-01-13 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 135174d2-aaa1-300a-a362-0faddd41aaec | -5.099 | -43.2444 | 2026-01-13 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 553439f2-4249-3b2d-8e40-637fa4d42a91 | -5.0992 | -43.2211 | 2026-01-13 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 360.3 |
| ec1c5fef-3034-3e0e-b2da-986cb8c4e633 | -5.099 | -43.2444 | 2026-01-13 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 266.2 |
| 2ff938e7-2232-3329-bc8c-3e8af33e77a3 | -5.118 | -43.2198 | 2026-01-13 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| bd59cf7f-d1e8-39ab-a6f1-9fcb800fa2c3 | -5.0805 | -43.2224 | 2026-01-13 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d6dbf536-3fa9-32e6-aea6-42031c322711 | -5.1178 | -43.2431 | 2026-01-13 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| a2bcb520-e18a-3726-b1e5-90513ec94620 | -5.0992 | -43.2211 | 2026-01-13 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 335.8 |
| efdd7158-e04c-347b-817f-65bff17a8513 | -5.0805 | -43.2224 | 2026-01-13 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| aa569a90-6821-3d5b-8a9f-cffe940d207d | -5.1178 | -43.2431 | 2026-01-13 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 0d083702-0032-347f-8587-7562947256b0 | -5.0994 | -43.1977 | 2026-01-13 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 06a6fb3c-47b8-348c-a61b-dda625be737a | -5.099 | -43.2444 | 2026-01-13 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 5eb7afc0-4509-38d0-b74c-041250bfdb48 | -5.118 | -43.2198 | 2026-01-13 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 74394714-779f-37e7-ba08-a45019081d9d | -5.118 | -43.2198 | 2026-01-13 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| e3f4cab1-252e-391d-bb55-f886fdedffc9 | -5.1178 | -43.2431 | 2026-01-13 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 8782cf2d-6560-306b-be90-78cdc3ac5d0a | -5.0992 | -43.2211 | 2026-01-13 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 307.5 |
| 50f60e47-ba71-3d12-999a-3b36f2be41fb | -5.099 | -43.2444 | 2026-01-13 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 231.8 |
| 187b4115-bd1e-38db-93e9-e8bf6aa97758 | -5.118 | -43.2198 | 2026-01-13 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 33045b49-aecd-34d5-a6f2-5d880f8ecb66 | -5.0803 | -43.2457 | 2026-01-13 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| c39cdb87-2c7e-344d-b7d3-2371075c0986 | -5.0992 | -43.2211 | 2026-01-13 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 273.0 |
| 5906db05-fa52-3b08-940f-90d92beb3d6d | -5.099 | -43.2444 | 2026-01-13 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 9a4fbd72-9a1d-3389-83b1-c7e0cc211497 | -5.1178 | -43.2431 | 2026-01-13 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 11aac94c-0422-3068-bfea-24d3d41e6b88 | -5.0805 | -43.2224 | 2026-01-13 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3b7e2117-9d5b-3647-ad53-a02799d07778 | -5.118 | -43.2198 | 2026-01-13 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 6f704fc4-4656-3f0f-ae95-c2f04152f9cf | -5.099 | -43.2444 | 2026-01-13 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 429f83f7-91cb-3da8-8468-e44d97bd5c34 | -5.0805 | -43.2224 | 2026-01-13 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fef7eb0d-da58-32b8-8900-3c49492c67fd | -5.0992 | -43.2211 | 2026-01-13 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 361.2 |
| d2066faf-bab8-3e87-8d36-3764b51d195f | -5.118 | -43.2198 | 2026-01-13 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c3ca7a96-fdbe-35ec-a644-f212d80fcba3 | -5.0805 | -43.2224 | 2026-01-13 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2ca259ad-7a92-3431-ac86-820489c1a5d7 | -5.0992 | -43.2211 | 2026-01-13 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 279.2 |
| f165709b-c19d-3662-b8bc-8322c44e50ba | -5.1178 | -43.2431 | 2026-01-13 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b2408ad4-0056-3e66-a324-b682d2e62a5c | -5.099 | -43.2444 | 2026-01-13 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 201.9 |
| c3d397e9-da53-3048-a0b2-cfd198a6846c | -5.118 | -43.2198 | 2026-01-13 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| bc481e4b-d2db-3e03-9bea-679453741b20 | -5.099 | -43.2444 | 2026-01-13 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 218.5 |
| 3873b254-28d8-3c69-abb4-9c118bd8f2ab | -5.0992 | -43.2211 | 2026-01-13 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 292.4 |
| af3edd0f-66a4-3c77-9289-8a8a3ffabd33 | -5.099 | -43.2444 | 2026-01-13 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 219.5 |
| abfb02f8-7b6a-3198-a322-4896fae925e7 | -5.0992 | -43.2211 | 2026-01-13 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 287.7 |
| cb04582f-0120-36a0-894e-f17eb1488108 | -5.118 | -43.2198 | 2026-01-13 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| db5bcd6c-4b1f-3520-9a2f-8094deb79196 | -5.118 | -43.2198 | 2026-01-13 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f26267f6-133d-3391-a062-23a57abc7374 | -5.0992 | -43.2211 | 2026-01-13 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 306.2 |
| da192ab4-3ebb-3006-8329-86cb0737b997 | -5.099 | -43.2444 | 2026-01-13 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 16f27074-cbd4-3f05-ac79-95fb6dc40d79 | -5.0992 | -43.2211 | 2026-01-13 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 260.1 |
| 3675faa2-aa38-3dff-9548-c7d666e07b60 | -5.118 | -43.2198 | 2026-01-13 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 1819af65-0d7b-33cd-9cab-e1102b384073 | -5.099 | -43.2444 | 2026-01-13 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 200.9 |
| baa77172-46ed-322d-9021-1e319a378d78 | -3.38803 | -42.11586 | 2026-01-13 03:29:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bb6c6c82-a823-34e2-8571-2c6da9a847cd | -5.4975 | -42.15531 | 2026-01-13 03:29:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 82ca726d-491a-367e-8066-958cfde43003 | -3.28985 | -42.54551 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5624957-2e87-33a2-91ca-0f334c0c6cd6 | -4.42394 | -43.10245 | 2026-01-13 03:29:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 34e9f841-1bc6-358f-9ade-9031028ae1b6 | -5.2479 | -37.50051 | 2026-01-13 03:29:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 14acea6e-91d2-3ce8-ad50-e8a0e951a8b5 | -5.09575 | -43.23094 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 4798e4bc-dd2d-37b3-be15-4a12fdcb02da | -4.42476 | -43.09771 | 2026-01-13 03:29:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b04d4991-0ecc-3aed-8db3-b45ed2d657e0 | -6.21913 | -38.31645 | 2026-01-13 03:29:00 | NOAA-21 | ÁGUA NOVA | RIO GRANDE DO NORTE | Brasil | 2400406 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 155f77a8-901b-3730-a8d2-1104f16f0ec2 | -4.91611 | -43.42738 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e04022c-483c-3a91-8794-749c8e7b070b | -3.30275 | -42.5429 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85d8c2a9-d7fe-3ace-97e1-0b02e662fd2f | -5.9249 | -43.3304 | 2026-01-13 03:29:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 473d747b-f225-3c88-85e9-4dede874ca88 | -5.09488 | -43.23595 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 82b5a4c4-3941-3793-ab00-a4b86f111cdc | -7.42366 | -35.24147 | 2026-01-13 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| ffa4876c-2b52-32bd-bb51-7b60e9d51cc3 | -3.55217 | -43.65601 | 2026-01-13 03:29:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86e368a6-6515-3502-9b7c-65057cff16ec | -6.10363 | -35.26308 | 2026-01-13 03:29:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ba4e007-5a15-3586-a6d4-aaadd693c93e | -5.10802 | -43.23154 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 668e4409-f906-31b2-afcb-122747de5ac7 | -5.10981 | -39.46412 | 2026-01-13 03:29:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 96a64b17-6f8b-3c81-bb6f-3edd053c3a60 | -5.41652 | -38.1657 | 2026-01-13 03:29:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c8249cad-f733-30a3-95ef-e7001cfa1660 | -6.08547 | -37.31506 | 2026-01-13 03:29:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 953bf2a3-66e2-37bd-aaa4-3bf96765f035 | -5.09585 | -43.22885 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| bbc91cd5-f78b-374a-8c9e-bc86ec3d5afa | -3.30353 | -42.53831 | 2026-01-13 03:29:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fb5e9aa-be71-31c4-9cfa-831ac9c99d19 | -6.33456 | -35.50854 | 2026-01-13 03:29:00 | NOAA-21 | SANTO ANTÔNIO | RIO GRANDE DO NORTE | Brasil | 2411502 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4a662a9-921d-330c-bb4c-d3715624983a | -4.20101 | -39.56654 | 2026-01-13 03:29:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e652384f-6cc3-3db1-bfd6-75d827964696 | -5.24507 | -37.36409 | 2026-01-13 03:29:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a5c7c7b-ec7a-3913-bf07-ec2bd8b17803 | -7.39583 | -35.21289 | 2026-01-13 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e18aefc8-0936-36dd-ac96-67510427a2af | -5.75612 | -39.80333 | 2026-01-13 03:29:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 449637ea-cc52-38ff-86c5-618658959295 | -5.10107 | -43.23502 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 9f5aade6-5321-3dda-88bb-56a632998311 | -6.10724 | -35.26363 | 2026-01-13 03:29:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6d101033-f5ca-3506-9e96-655d0437a3de | -5.10344 | -43.22297 | 2026-01-13 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 5ea50fa3-8504-3870-aafd-1d583b24e6f7 | -7.80936 | -36.44219 | 2026-01-13 03:29:00 | NOAA-21 | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
