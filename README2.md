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
| 4bd2cd2b-e835-34e0-9397-e581619a47d4 | -2.6533 | -53.3506 | 2024-10-11 00:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| f9293b05-6b16-388d-bfe7-a066bbfeaf18 | -2.6533 | -53.3303 | 2024-10-11 00:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| fffa4811-55d7-3d40-81d7-2677e8b87892 | -2.6716 | -53.3502 | 2024-10-11 00:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 2be54cf2-ec8d-300b-9393-b3b8f75cd132 | -2.7663 | -52.4937 | 2024-10-11 00:15:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| c6e7008d-d552-3eba-8ea7-894b31a9fa37 | -2.7664 | -52.4733 | 2024-10-11 00:15:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d8064dfc-1800-3337-871a-4d9155297a9c | -2.7847 | -52.4933 | 2024-10-11 00:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 390.1 |
| 08d749e7-5312-35c9-8e10-47aa64db72b6 | -2.7848 | -52.4728 | 2024-10-11 00:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 335.2 |
| 3dc4678e-c57d-3c54-b0c6-9dc612b7f071 | -2.9674 | -47.9931 | 2024-10-11 00:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6a02e379-6938-31de-8391-2a0ad2efbeb6 | -2.9673 | -52.9169 | 2024-10-11 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 94254f1d-13f4-35fd-a067-426f386527e9 | -2.9673 | -52.8966 | 2024-10-11 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 06802b64-4ae8-3d9a-87d6-12c0fca9adae | -2.9728 | -51.3568 | 2024-10-11 00:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0ef8579d-7449-3dce-aebc-1c3f2018bf6f | -2.9857 | -52.9164 | 2024-10-11 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 186.5 |
| 45171e9b-0ef0-3556-840e-dedb63b0923b | -2.9857 | -52.8961 | 2024-10-11 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 69d709f9-74a3-3127-92f4-50b65a877fe6 | -3.0343 | -61.6918 | 2024-10-11 00:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 54861650-b283-336b-b82c-cb7261884079 | -3.0343 | -61.673 | 2024-10-11 00:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 5de366b5-4a8d-303f-88d5-31658faec8f2 | -3.0525 | -61.6916 | 2024-10-11 00:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7ce6c77c-8528-3998-bc62-26f01476df31 | -3.0525 | -61.6727 | 2024-10-11 00:15:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 66f14208-0ad7-3036-bfd1-378b64d202a4 | -3.1422 | -50.4562 | 2024-10-11 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6ab2bdd9-1d6a-3b4a-9149-893b99a3afbb | -3.1423 | -50.4352 | 2024-10-11 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 7f8c4fcc-ef2b-33d2-8e14-94409d1105c0 | -3.1607 | -50.4556 | 2024-10-11 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 701ef757-bb62-3299-bbdd-2635aa1dd2be | -3.1608 | -50.4347 | 2024-10-11 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 175.4 |
| 41443e92-6f86-3362-a5d8-020e8e2ef7fe | -3.3098 | -46.0724 | 2024-10-11 00:15:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6f72f910-28f5-3efa-889b-daec83dbaa4a | -3.3096 | -50.1781 | 2024-10-11 00:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| eb8145cc-085c-3708-bbd6-e12f7ea6f391 | -3.614 | -44.7783 | 2024-10-11 00:15:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 982e9873-2554-3229-96b7-d22ae0ca7b29 | -4.0962 | -48.2523 | 2024-10-11 00:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 6912c06d-11c3-3e07-8b7a-8f58135134fd | -4.1148 | -48.2515 | 2024-10-11 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| d1754a9a-9cea-3ed4-8832-1687cabf6fa7 | -4.1149 | -48.2299 | 2024-10-11 00:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7885adf0-06da-3122-82e7-94fdf919842f | -5.3264 | -60.143 | 2024-10-11 00:15:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 41c07c41-8e25-3146-8f40-92cecb775cdb | -5.3265 | -60.1239 | 2024-10-11 00:15:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| de947da3-5301-338d-a689-a81aa774699d | -6.5404 | -60.0259 | 2024-10-11 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f27541ce-7293-39a4-9838-6009c9cd27fc | -6.5589 | -60.0252 | 2024-10-11 00:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 83a9be6e-3761-3514-a779-f5f62de456b2 | -6.747 | -59.3259 | 2024-10-11 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2b2ca704-f7aa-3f16-8427-3f93f3c0e474 | -6.7654 | -59.3252 | 2024-10-11 00:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d84b3bbf-95c0-3594-80ef-65dfff825b6c | -7.0786 | -59.4087 | 2024-10-11 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 47a6d4ae-9945-3756-a8ff-c07423cd9ffb | -8.4417 | -55.4692 | 2024-10-11 00:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| ab1cb237-7575-3669-8ae4-1dbf134765e1 | -8.4419 | -55.4491 | 2024-10-11 00:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c053d1b3-7ccc-3a00-a2cb-7ddfb86efeb0 | -9.7374 | -46.9844 | 2024-10-11 00:16:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ee6461c5-06e1-34ac-b4f2-1ac2c3e8d25d | -9.7377 | -46.9621 | 2024-10-11 00:16:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 360e60dd-5dfe-31f1-bfdd-a1b077b3dc40 | -10.46 | -46.7885 | 2024-10-11 00:16:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 9346461b-ae2b-3d24-a113-ec976427c42c | -10.363 | -55.8755 | 2024-10-11 00:16:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| be94d0b0-0e02-3821-8a44-4e4c73f3852a | -10.3632 | -55.8554 | 2024-10-11 00:16:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 80.2 |
| f8c42609-b2ed-370a-9603-8ae9ad3b76c0 | -10.4791 | -46.7862 | 2024-10-11 00:16:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9c813997-6974-38a9-8872-858cffd80c29 | -10.382 | -55.854 | 2024-10-11 00:16:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d5858448-8fb4-35aa-8833-7b547060b112 | -10.6171 | -47.704 | 2024-10-11 00:16:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 8c2c4c10-1a9e-3d6b-a8ed-1034eae41d44 | -10.6773 | -53.0372 | 2024-10-11 00:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 29bd63fa-ddec-3865-9bf5-cb7898000869 | -10.6962 | -53.0354 | 2024-10-11 00:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 3f891dc5-8d64-3412-b618-fd2857427444 | -10.6965 | -53.0147 | 2024-10-11 00:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| fe3ed473-7eb5-32d7-a212-61023cd8105e | -10.7151 | -53.0337 | 2024-10-11 00:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 39f0cf50-be1b-379a-989d-d3fc1fe36fff | -10.7059 | -64.1138 | 2024-10-11 00:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4cdcfe6e-7233-3ff2-959f-5475765ce3d7 | -11.2407 | -53.2738 | 2024-10-11 00:16:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 06ca3528-2b8d-3f80-a013-9ebf5620ac21 | -11.241 | -53.2531 | 2024-10-11 00:16:10 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1e6a3508-8337-3f42-a572-d5da13f50298 | -11.2597 | -53.272 | 2024-10-11 00:16:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8186a3c3-9243-39fd-9b8f-55096cd89c80 | -11.2599 | -53.2513 | 2024-10-11 00:16:10 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 98f1128f-2274-3680-bf34-c5816e0090de | -11.2763 | -60.4844 | 2024-10-11 00:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 8b88090a-98f8-3e86-b1b2-8fae06085c81 | -12.3171 | -45.3083 | 2024-10-11 00:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| aef35578-0760-3e6e-b084-156f6e08c9af | -12.3463 | -43.7638 | 2024-10-11 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| db1a4068-14a0-3795-8cc5-bc9c11634b9a | -12.3467 | -43.7401 | 2024-10-11 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| dba6c993-0bb8-3988-bea3-8ecdefa3eff8 | -12.3656 | -43.7606 | 2024-10-11 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 914b4e29-02d4-39d4-b921-874d4174345e | -12.366 | -43.7369 | 2024-10-11 00:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ef20bc20-150e-3488-b6ee-e6086bc20030 | -12.4566 | -53.1294 | 2024-10-11 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| d02e54cf-8ac3-3c40-bbed-66444fe34e4d | -12.4569 | -53.1086 | 2024-10-11 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4329bc62-5de8-3bc0-b715-03ed4710cdd5 | -12.4757 | -53.1274 | 2024-10-11 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 186e0d51-8225-3b86-84a3-f0123f7e3a85 | -12.7673 | -44.8904 | 2024-10-11 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 2eec2a83-3553-3b76-8fe5-9a7392d97a4c | -12.7678 | -44.8671 | 2024-10-11 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.4 |
| a2631249-3079-365a-9a0f-ef6d475abeca | -12.7866 | -44.8873 | 2024-10-11 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 476caf7f-aaab-3d3b-a092-e2878bf5f62d | -12.7871 | -44.8639 | 2024-10-11 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 254.0 |
| 1f95b8ef-629b-3974-ba88-c8b35d2bb637 | -12.8064 | -44.8608 | 2024-10-11 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 91187f74-dc37-3344-ad10-8171b3926142 | -12.9852 | -53.4881 | 2024-10-11 00:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b4f3e7a7-8c99-3c22-8814-59a6d6b1cf96 | -12.9855 | -53.4673 | 2024-10-11 00:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 2f39bb13-b17d-326f-892b-5ec518006b27 | -12.9858 | -53.4465 | 2024-10-11 00:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 953595d9-fd6e-3ff0-92f9-9f57f2d18e1e | -13.5078 | -42.7246 | 2024-10-11 00:16:22 | GOES-16 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 75.5 |
| e24b4414-f564-3b73-92ca-a6b050bdd9b3 | -13.5084 | -42.7003 | 2024-10-11 00:16:22 | GOES-16 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 7c33a69f-1e9c-3eb0-827a-810bb9f1425d | -13.7346 | -60.6079 | 2024-10-11 00:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a6803991-f2e9-3d9d-996d-8b17b17e3e0f | -2.5444 | -47.2231 | 2024-10-11 00:25:21 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 12be1933-d1da-34d4-b787-336adebc69c0 | -2.6533 | -53.3506 | 2024-10-11 00:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 00b0debc-2b48-3181-9d96-a35247d65f56 | -2.6716 | -53.3502 | 2024-10-11 00:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 1677c391-3930-3ea5-a92d-ff1f08eb6519 | -2.6717 | -53.3299 | 2024-10-11 00:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a9c98dbc-7475-36f2-878f-3fb53c26efbd | -2.7663 | -52.4937 | 2024-10-11 00:25:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 822dadc1-0fbf-3b8d-94b6-1eff9790bd46 | -2.7664 | -52.4733 | 2024-10-11 00:25:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ae9c0d03-a361-3458-90a4-907fdb234938 | -2.7847 | -52.4933 | 2024-10-11 00:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 252.9 |
| 0f8c2b75-6b11-33cc-8520-b312a0e3740f | -2.7848 | -52.4728 | 2024-10-11 00:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 241.3 |
| a0815d21-e955-31e6-905f-3fd08a982cc4 | -2.8031 | -52.4928 | 2024-10-11 00:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d5795969-9ba9-3c51-a2af-cf64f5453b87 | -2.8032 | -52.4724 | 2024-10-11 00:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 60c140dd-c157-37b5-be86-a2c397257fad | -2.9673 | -48.0147 | 2024-10-11 00:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 25d9b100-786f-37db-b5e8-10f18a58cb4a | -2.9674 | -47.9931 | 2024-10-11 00:25:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 57770f0a-0021-3e85-8616-bc19a7b959f3 | -2.9673 | -52.9169 | 2024-10-11 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 2a1c1feb-9581-3199-b404-ef1f2543234f | -2.9673 | -52.8966 | 2024-10-11 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 865eeef2-9eb4-3627-8863-6836d171d2b7 | -2.9728 | -51.3568 | 2024-10-11 00:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 4fb7a721-bedb-379d-bba4-ead3b42f241c | -2.9857 | -52.9164 | 2024-10-11 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 3139a288-0f54-3396-8083-dc649a3e0519 | -2.9857 | -52.8961 | 2024-10-11 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.1 |
| f8cdb3dd-038f-39cd-ad43-fc36a7f4d8fa | -3.0343 | -61.6918 | 2024-10-11 00:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4fc3fc80-176e-3bd8-a5f8-3693db090217 | -3.0343 | -61.673 | 2024-10-11 00:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b80606b0-df87-3722-952d-bc7736387e66 | -3.0525 | -61.6916 | 2024-10-11 00:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f5c0cf96-ad44-3c29-ba2c-dde882ad7529 | -3.0525 | -61.6727 | 2024-10-11 00:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| e1127199-1054-3e92-a24f-076400653818 | -3.1422 | -50.4562 | 2024-10-11 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| ec3ecfa2-0753-3ef4-922c-723e85ce20e6 | -3.1423 | -50.4352 | 2024-10-11 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2c9d3b0f-e015-31d3-b72d-c3581b2c5d7e | -3.1607 | -50.4556 | 2024-10-11 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| c1dca44f-aa1b-3073-8a1c-4338744a2974 | -3.1608 | -50.4347 | 2024-10-11 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 7682f076-5640-3cdf-be66-8f27310b6a41 | -3.2912 | -46.0731 | 2024-10-11 00:25:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a65ff237-971a-399b-ae46-f5408ee95983 | -3.3098 | -46.0724 | 2024-10-11 00:25:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |


[Clique aqui para ver as próximas entradas](README3.md)
