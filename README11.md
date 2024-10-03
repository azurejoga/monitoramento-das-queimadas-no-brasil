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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e60b214-6afd-3815-bb38-e8d173c45ae3 | -5.2253 | -43.8164 | 2024-10-03 00:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| bca468b0-1610-3a92-b91a-72f748d83203 | -5.2255 | -43.7932 | 2024-10-03 00:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 298ce4a9-861a-3805-80ab-08409dd51bac | -5.2441 | -43.8151 | 2024-10-03 00:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 8320dcae-5714-3c4f-aef6-2f66efeb2dc0 | -5.2443 | -43.792 | 2024-10-03 00:15:35 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 238.6 |
| ef2d68c8-1ed0-34e3-b1ca-5f5db27e5e9f | -5.2628 | -43.8138 | 2024-10-03 00:15:36 | GOES-16 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 85c1b1de-1536-3474-ba85-b73a8dd3616b | -5.263 | -43.7907 | 2024-10-03 00:15:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ede33590-7592-306c-9500-cc7fa9ef8433 | -5.3515 | -46.7226 | 2024-10-03 00:15:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d72458d6-281b-38f6-9a1b-4da5a7fc7cd7 | -5.8358 | -44.6231 | 2024-10-03 00:15:39 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b25a0e23-42bb-32b2-8ba8-3c12811aaf95 | -5.836 | -44.6002 | 2024-10-03 00:15:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| d6508635-495d-3d11-8be5-cec388e685ae | -5.8545 | -44.6217 | 2024-10-03 00:15:39 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 240.7 |
| f2847998-0f01-3171-8172-3fb32524970d | -5.8547 | -44.5988 | 2024-10-03 00:15:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 556.5 |
| 980fac67-a56c-305e-a01c-fa7ffd9fb533 | -5.8549 | -44.576 | 2024-10-03 00:15:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 8cb04db1-37d2-3374-a43a-baa4c53d94b4 | -6.1301 | -47.2664 | 2024-10-03 00:15:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 926a5fab-4835-356b-82a8-f29c5b2388ae | -6.7112 | -59.1345 | 2024-10-03 00:15:44 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b4bf7cc1-5761-3858-a438-6a10c103164c | -6.8777 | -59.0504 | 2024-10-03 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 3bbcd555-3119-3dda-8771-27b3d41d201e | -6.8778 | -59.031 | 2024-10-03 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| fa881191-1b93-3edf-ab8b-930a20309741 | -7.1871 | -59.7893 | 2024-10-03 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 2d4a4e71-f896-3b58-b402-5a055c153422 | -7.2056 | -59.7886 | 2024-10-03 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 69f45ebb-bdcb-32d6-bdd7-fb1785ea8a4d | -7.3726 | -68.0177 | 2024-10-03 00:15:48 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c178972d-c889-3f3b-8468-5b12ebb3ebdf | -7.8785 | -72.805 | 2024-10-03 00:15:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 98fd9127-a0e0-39d8-a8f1-8c4d381067ad | -8.5224 | -50.9721 | 2024-10-03 00:15:54 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4b6a602d-9149-388b-bf33-5b94a2af2ac2 | -8.8926 | -62.3348 | 2024-10-03 00:15:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 40f32f94-d404-36af-bcdf-6b099552b89e | -8.9594 | -63.6187 | 2024-10-03 00:15:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 57a704f7-1041-35e0-b87d-4010d9ffc0c9 | -8.9595 | -63.5999 | 2024-10-03 00:15:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 3cfa911f-a276-3614-995c-54500b8b3ea0 | -8.9791 | -67.4099 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a2712520-0ff9-3015-8be2-4da63b661642 | -8.9976 | -67.4094 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 871b1cf3-f198-39cd-a472-622aa67cc440 | -9.0149 | -67.7608 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 469c1d3a-8753-3a02-8bbb-bd38f34c1987 | -9.0149 | -67.7423 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 75f7fabb-dee7-3e3b-86b4-4254796fad40 | -9.015 | -67.7238 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ee06221c-6119-3172-aab7-f6f14a51babb | -9.0334 | -67.7419 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 80d38fd9-c082-3536-9b44-08ec4441a07b | -9.0515 | -67.871 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 0d6e059e-edfe-3430-969d-bc8ea4564ae5 | -9.0516 | -67.8525 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| bf7f7ae6-13fe-36a2-a25d-84ff54fcba7b | -9.0898 | -67.5183 | 2024-10-03 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| d3e7a9dd-ebe7-3586-9b3a-cc02552e8d15 | -9.1566 | -61.6758 | 2024-10-03 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 02bd91db-a710-3745-bdce-cb834f8e75a1 | -9.1568 | -61.6567 | 2024-10-03 00:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ffcb8adf-f92f-3bd3-9993-b75de8b1d182 | -9.1752 | -61.6749 | 2024-10-03 00:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 357bc8d7-5123-3cff-9f34-88e2423b1a41 | -9.2739 | -67.8286 | 2024-10-03 00:15:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| ff72d7c9-1870-3121-96bf-3e1d12e89885 | -9.2739 | -67.81 | 2024-10-03 00:15:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 599fa3cd-dc83-3ba8-a2af-2a54288675ea | -9.3496 | -67.4003 | 2024-10-03 00:16:00 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 452545d1-97dc-3602-aff3-8eefaa80cfdc | -9.3839 | -61.0526 | 2024-10-03 00:16:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 01bd4071-66e8-3488-811e-aeabf8cfeec7 | -9.4025 | -61.0517 | 2024-10-03 00:16:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| aa66f558-5d29-3016-aa71-d357910d40cc | -9.3832 | -68.3441 | 2024-10-03 00:16:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 33.9 |
| bfa16b69-78e2-372f-a2dc-9fc64cf55819 | -9.3833 | -68.3256 | 2024-10-03 00:16:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 73c7c630-3056-3c8b-a43e-6a192e5f4552 | -9.4244 | -67.2313 | 2024-10-03 00:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b6d8ec5b-2221-3483-b397-755ec9425f0d | -9.4368 | -64.5419 | 2024-10-03 00:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a71abb2e-ab76-3ffb-8673-72afc065b276 | -9.4554 | -64.5412 | 2024-10-03 00:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9bd91f49-64e7-3be5-9677-67ef7f83cc1f | -9.468 | -62.3857 | 2024-10-03 00:16:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| c33a15c5-e324-33ce-9104-8f6f3ff43d81 | -9.4865 | -62.4039 | 2024-10-03 00:16:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 61cb7b5b-69e4-31bc-90fd-eb18fd532da6 | -9.4866 | -62.3849 | 2024-10-03 00:16:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 121.1 |
| bbd57fba-4bdc-3984-aa27-20b4516eef97 | -9.4939 | -68.508 | 2024-10-03 00:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b88bf118-2a42-3875-b4c8-3301ed969e58 | -9.494 | -68.4895 | 2024-10-03 00:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 77651391-fdf2-39a8-9301-c1b7d1bf94cd | -9.5125 | -68.4891 | 2024-10-03 00:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 64df9938-6c84-384a-92e3-f25679bae1ba | -9.7173 | -64.2302 | 2024-10-03 00:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 3e1cb77e-49d8-37d4-89e3-2015661de617 | -9.9067 | -67.3294 | 2024-10-03 00:16:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b4dd9b2d-89b8-3803-81ad-7a47933d2e5c | -9.9665 | -63.0094 | 2024-10-03 00:16:03 | GOES-16 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f257395d-94f0-377f-bd48-b0270073b2a1 | -9.9667 | -62.9904 | 2024-10-03 00:16:03 | GOES-16 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e7438e2e-986a-356d-86aa-ec9b147f5f5a | -10.129 | -56.7722 | 2024-10-03 00:16:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bbdf4461-0ccb-3d8b-afa8-7f2e1f336bcb | -10.4475 | -56.789 | 2024-10-03 00:16:05 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8dfae56b-c580-3780-8fcc-db9ee829b10f | -10.7355 | -46.1692 | 2024-10-03 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 76cdcd7a-4eee-323a-b136-397f5dd88d3b | -10.5136 | -69.2435 | 2024-10-03 00:16:06 | GOES-16 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8e4c0c35-b5c2-3da8-a38f-6c1dc15ab379 | -10.6505 | -53.6994 | 2024-10-03 00:16:06 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 2e7aee20-a57c-3d9e-af60-352aace87e02 | -10.6128 | -64.0611 | 2024-10-03 00:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6eb0475f-d77f-376c-8a5b-5a3dd93d322e | -10.8942 | -63.8971 | 2024-10-03 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 7da3d28e-09c2-3db7-b58c-6b0a7e26425c | -11.2567 | -46.9123 | 2024-10-03 00:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 1c99a576-0c5f-36bb-81ea-4b28ab123910 | -11.2758 | -46.9098 | 2024-10-03 00:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 6881b2ba-33a7-3cc1-9e41-619cc5bb5ca7 | -11.6243 | -64.0339 | 2024-10-03 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 1a47a9b3-548e-308c-a27b-64d04f54f7ee | -11.6742 | -65.0172 | 2024-10-03 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| f6686867-5f86-31e8-8da2-acd471ae1951 | -11.693 | -65.0163 | 2024-10-03 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.3 |
| eddac536-de48-3cc4-b588-dface2ae8d46 | -11.9876 | -57.1877 | 2024-10-03 00:16:14 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 1ac10982-822b-3b73-be24-2b2d0c908787 | -12.2668 | -45.958 | 2024-10-03 00:16:15 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ff21fc12-e573-36d3-afe6-0475bab7b9eb | -12.3849 | -63.002 | 2024-10-03 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9e666513-c755-3adf-9900-b4459dceedb2 | -12.4038 | -63.0009 | 2024-10-03 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 0a4e164d-40d4-3c4a-a7e5-a6e3c975d635 | -12.404 | -62.9817 | 2024-10-03 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 37fd70b8-b86d-3506-a237-e02d7ea3c384 | -12.6295 | -63.1225 | 2024-10-03 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 8c81078b-25a2-314c-95a3-d32a88e96154 | -12.6484 | -63.1214 | 2024-10-03 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.0 |
| c7a42ce1-f46c-3959-b4fd-a06ca6119945 | -12.6486 | -63.1022 | 2024-10-03 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 44e1ac4d-f087-3599-b1b6-8d0942fe2b5a | -12.7858 | -62.5174 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| aaf9d40d-8f23-3bdd-be76-dcffdf66ed5d | -12.786 | -62.4982 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a9d91c6c-53fd-3288-b667-6a312b3066e6 | -12.8047 | -62.5163 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| bd505d01-f389-3105-baa0-6cac1e48de1e | -12.8049 | -62.497 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 7a3ae24b-779f-3dcf-bfb1-56dd8b8d3236 | -12.8238 | -62.4959 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9c60e706-8d41-3b3f-8ef9-9da1cd453a3a | -12.824 | -62.4766 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b466f7a4-4622-34f3-892c-110421dfdad6 | -12.8619 | -62.4743 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| fdac3761-5f98-36fc-86fd-c7d416266fe4 | -12.8808 | -62.4731 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 100.0 |
| e5772cac-6b7b-3c69-8233-4d4e663c40a9 | -12.881 | -62.4538 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 2d1eb675-ad25-3ccb-a926-83646fde074c | -12.8996 | -62.4913 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 1c11a4a0-057a-31fd-94ad-1eeff07a1f0f | -12.8998 | -62.472 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 8e61ba3d-f1e7-3a4e-91c1-52dc5841dcba | -12.8999 | -62.4527 | 2024-10-03 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 1a45af5a-1bd5-3888-be92-9d9fefc66535 | -12.9741 | -62.6409 | 2024-10-03 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 157.8 |
| fc7b0d02-031c-3e13-9c2e-13bc2c822497 | -14.7017 | -48.7559 | 2024-10-03 00:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 19d50cf9-a843-37bf-bbd4-e05d04aaced9 | -15.2332 | -47.5032 | 2024-10-03 00:16:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| bb00406f-785d-37ab-b0b8-ea6df0996dc2 | -15.2528 | -47.4999 | 2024-10-03 00:16:31 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| b221788f-36c8-3a94-980f-755ce3f56937 | -16.5582 | -58.2407 | 2024-10-03 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.1 |
| eecfccc2-23be-318b-bc0a-8dd14eda5322 | -16.5585 | -58.2204 | 2024-10-03 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.8 |
| 7b589e3e-29b9-354b-a925-c9584262a385 | -16.5778 | -58.2386 | 2024-10-03 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 3fca6482-c3a3-3a24-b612-313a48ffc1b0 | -16.578 | -58.2183 | 2024-10-03 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 8f7ba01b-b250-3bb4-9ce9-7d62399ae8d6 | -16.5973 | -58.2365 | 2024-10-03 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 8ab0860d-1dce-34ac-924e-6843b6e28a4f | -16.5976 | -58.2162 | 2024-10-03 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 38c233aa-3a62-3877-bf66-c097b7488a12 | -16.7594 | -57.8328 | 2024-10-03 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.5 |
| 0e54d073-206c-32d0-82fe-f0f96fc54ab8 | -16.7597 | -57.8124 | 2024-10-03 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.9 |


[Clique aqui para ver as próximas entradas](README12.md)
