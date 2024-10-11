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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5af30d18-17d0-37cd-934a-4e0479d01b78 | -4.1148 | -48.2515 | 2024-10-11 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3ec3fc41-9749-3141-a6f8-4ad4deb50e4c | -4.1149 | -48.2299 | 2024-10-11 01:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 7e11bed5-be1b-393a-9276-08ff282954c6 | -6.1299 | -47.2884 | 2024-10-11 01:15:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 1842faa5-614a-38cb-b1c6-2ff8d67f5757 | -6.1301 | -47.2664 | 2024-10-11 01:15:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 56386dd9-77f0-3370-9e57-3e9f6b4427b4 | -6.5404 | -60.0259 | 2024-10-11 01:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 14ea2396-e55b-3d71-85e1-c8433f011cc2 | -6.5589 | -60.0252 | 2024-10-11 01:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6f2fc245-cea5-304a-a00d-0e39b5413f44 | -6.747 | -59.3259 | 2024-10-11 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f8033c72-2f51-3804-8171-e486573d8c1c | -8.4231 | -55.4704 | 2024-10-11 01:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 231710ed-187e-31ad-b524-a8cd84d6aae7 | -8.4417 | -55.4692 | 2024-10-11 01:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 80c7db85-4910-3bd9-91a8-661cd27f4c6e | -8.6119 | -46.4796 | 2024-10-11 01:15:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 93f165f7-79af-3148-b7d7-4876f5933c69 | -10.4713 | -49.9838 | 2024-10-11 01:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7cf41d0a-5791-3198-b6fe-cdff5f655360 | -10.4716 | -49.9624 | 2024-10-11 01:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 32be4200-6078-396d-aed1-acf4de707e4d | -10.4902 | -49.9818 | 2024-10-11 01:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ef2853cc-4d81-3706-afda-731cc0c6ccbf | -10.5755 | -64.0438 | 2024-10-11 01:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 3234408b-acc5-3d06-bc34-195fa03d9912 | -10.5757 | -64.0248 | 2024-10-11 01:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b92cba29-40c5-3e1b-909a-4ce83a385323 | -10.6962 | -53.0354 | 2024-10-11 01:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 689a3fbd-da80-34e2-98ef-f0fe5294b8f3 | -10.6965 | -53.0147 | 2024-10-11 01:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 8a7ccb66-120d-3f63-8ea3-3d09b4cd8572 | -10.7059 | -64.1138 | 2024-10-11 01:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e71e36e6-9943-366c-8d69-118f15df7853 | -10.8935 | -52.3517 | 2024-10-11 01:16:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| aad99311-9e8e-3c4f-89d3-e5e9d212263e | -10.8938 | -52.3308 | 2024-10-11 01:16:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 06f9b4a0-93b8-35a8-8b0b-d3637c293ce0 | -11.2407 | -53.2738 | 2024-10-11 01:16:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b66d6be2-984f-3a8e-8e81-82a95c038c23 | -11.2597 | -53.272 | 2024-10-11 01:16:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| fc51d05b-a795-37d4-a1a2-3e200dc3c7df | -11.2909 | -50.9421 | 2024-10-11 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 415473e2-71bb-3c7c-b301-8237fd22122e | -11.2912 | -50.9208 | 2024-10-11 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| ba94a853-c294-33b6-a71e-c07ea238f213 | -11.2763 | -60.4844 | 2024-10-11 01:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c045d3f1-9f02-3301-9cbe-e48e48c9270f | -12.7673 | -44.8904 | 2024-10-11 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 1e4c1f17-b064-3c92-9aa2-dc54a4e2f173 | -12.7678 | -44.8671 | 2024-10-11 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 7376628c-bdbc-3b7f-9728-1b3a1b9e9b22 | -12.7866 | -44.8873 | 2024-10-11 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 12d98d91-68ef-30aa-8d94-b16f58ab920f | -12.7871 | -44.8639 | 2024-10-11 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| acb51c97-11e3-3768-9658-3f1d36796e81 | -12.8705 | -53.5007 | 2024-10-11 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ca694d9c-5537-3efa-ba02-21bb3928a4b7 | -12.8708 | -53.4799 | 2024-10-11 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| e731608d-bab6-3acf-8043-fc2fb229d8ee | -12.8896 | -53.4986 | 2024-10-11 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c8595f18-be96-31a7-bc02-ab1808643663 | -12.8899 | -53.4778 | 2024-10-11 01:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| cad66029-adce-3537-b276-32032982762c | -12.9855 | -53.4673 | 2024-10-11 01:16:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d1ceabf9-1e2d-3926-8849-a0a5ecde14f1 | -13.368 | -44.7676 | 2024-10-11 01:16:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 94925f33-adbd-3559-8a80-02bf50b4dfe7 | -2.6533 | -53.3506 | 2024-10-11 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| a5d3225e-52cd-3509-a9c4-c3289f2a53ed | -2.6533 | -53.3303 | 2024-10-11 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 348e28e9-47e1-397a-9d60-0c34a5d5cc6b | -2.6716 | -53.3502 | 2024-10-11 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 706505f3-e1bc-33c8-9143-61539e263410 | -2.7847 | -52.4933 | 2024-10-11 01:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 5d10c689-8305-3086-afc6-6eb28a7f88c3 | -2.7848 | -52.4728 | 2024-10-11 01:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 6318a40d-5098-3b38-b0a8-c2eae45f208e | -2.8081 | -51.0084 | 2024-10-11 01:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| aac8efbf-fb14-3be3-8a62-102c3882ca3e | -2.9673 | -52.9169 | 2024-10-11 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 228701fc-1798-34d9-a5d3-de9f8ba636f9 | -2.9673 | -52.8966 | 2024-10-11 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| dcfd0b37-8122-3308-99a2-a864644e8775 | -2.9857 | -52.9164 | 2024-10-11 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 6d48fce7-4175-37d0-8eda-8ed3a5a1826a | -2.9857 | -52.8961 | 2024-10-11 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| dd07eb8d-4966-3e59-a3d7-565b618e3c7c | -3.0343 | -61.6918 | 2024-10-11 01:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| e84b8fcb-eef2-3ddc-a325-40d6d5b9d636 | -3.0343 | -61.673 | 2024-10-11 01:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a61e408a-432a-3a5a-8ace-52ee200aaf23 | -3.0525 | -61.6916 | 2024-10-11 01:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2f20b5ce-c407-3c0f-a39b-3cd8092b18c4 | -3.0525 | -61.6727 | 2024-10-11 01:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| a99cfacb-462f-3a46-9c37-001b990e9d83 | -3.1422 | -50.4562 | 2024-10-11 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4907d302-d444-3f1e-b91b-9d80d38cdb25 | -3.1423 | -50.4352 | 2024-10-11 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 11280a22-449f-391e-b042-b90bffa87ad8 | -3.1607 | -50.4556 | 2024-10-11 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 6ce38f9b-b815-31bf-b9b5-131fc9307c1b | -3.1608 | -50.4347 | 2024-10-11 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 857f9cb0-c749-3fa9-a9ac-6ab69888e9db | -3.3096 | -50.1781 | 2024-10-11 01:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 322fe34c-89b3-383b-8f60-2e4b60521210 | -3.614 | -44.7783 | 2024-10-11 01:25:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b7d47169-8fcc-302f-82ff-788d37c69fcb | -3.9207 | -46.468 | 2024-10-11 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4dddbff1-a719-3ca4-a096-d038e79f49d8 | -4.0962 | -48.2523 | 2024-10-11 01:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 87551f09-3f96-322b-998e-7e07d7425130 | -4.0963 | -48.2307 | 2024-10-11 01:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 57aebb86-6c65-325e-8c80-7a768dbbc59d | -4.1146 | -48.2731 | 2024-10-11 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| ba571b20-9f65-3c66-93c9-0abbde97c314 | -4.1148 | -48.2515 | 2024-10-11 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 302.7 |
| 9e9d6ffd-93ec-3d92-bfa0-07a314ad1a85 | -4.1149 | -48.2299 | 2024-10-11 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 7dfef827-044a-3395-8d6b-a3f4a8ce691c | -4.1333 | -48.2507 | 2024-10-11 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2af76095-541e-37fc-9dad-3ae092f4f0f9 | -6.1301 | -47.2664 | 2024-10-11 01:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9aa5f0d8-17f9-327e-89c2-d0be64cca7a8 | -6.5404 | -60.0259 | 2024-10-11 01:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 44a3d42f-d6e0-3c93-a57d-dafd825cf5ab | -6.5589 | -60.0252 | 2024-10-11 01:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 230d7e39-d400-388e-861e-c4a4a4e9e5a8 | -8.4417 | -55.4692 | 2024-10-11 01:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 78453809-b017-38c0-8127-58166e29f69c | -10.3632 | -55.8554 | 2024-10-11 01:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 42da1067-75cd-3339-a419-642172815467 | -10.5755 | -64.0438 | 2024-10-11 01:26:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 1297edc8-2097-3b55-aaf1-ccbd1caa0258 | -10.5757 | -64.0248 | 2024-10-11 01:26:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5c185a28-ff67-396e-bcea-bfb8e1962eb8 | -10.6962 | -53.0354 | 2024-10-11 01:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| b0748ef1-fcff-384c-a916-0ee3051f708e | -10.6965 | -53.0147 | 2024-10-11 01:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 24de81e3-c796-35d4-b308-9855f49b4967 | -10.7059 | -64.1138 | 2024-10-11 01:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 1cf6c3a5-14dd-3e6e-a288-00b2589fdb2f | -10.8935 | -52.3517 | 2024-10-11 01:26:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| f1c29824-3cd5-33e9-b0bf-a2bf3c5b2af0 | -10.8938 | -52.3308 | 2024-10-11 01:26:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9603ca07-5c35-3e8b-9bb5-99affa0feaaf | -10.9124 | -52.3498 | 2024-10-11 01:26:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 1ddb5076-c474-3346-8ab1-e4423eab76f9 | -10.9127 | -52.3289 | 2024-10-11 01:26:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c7aa4ccc-c7ed-3d95-8bfe-1025e2a87ab3 | -11.2407 | -53.2738 | 2024-10-11 01:26:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| cd1074e7-eb8b-325f-91c4-ad28576fc1b8 | -11.2597 | -53.272 | 2024-10-11 01:26:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 990b34a4-b526-3026-b908-bea8fae1e5ef | -11.2912 | -50.9208 | 2024-10-11 01:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 85f377fc-afa9-3e33-a695-5ce791d0cbb1 | -11.2763 | -60.4844 | 2024-10-11 01:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 560477cb-b8da-32ff-a156-4fbc43380b2b | -12.3463 | -43.7638 | 2024-10-11 01:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 38314178-2e23-33cf-820b-da5902ee2697 | -12.3467 | -43.7401 | 2024-10-11 01:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 27cb727d-c2cc-3065-b53e-3e5d00bc3b5f | -12.7673 | -44.8904 | 2024-10-11 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| ec4d2032-a483-3b0a-ad06-b95652f9249e | -12.7678 | -44.8671 | 2024-10-11 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| d5711ceb-707b-3af8-b817-ade058810698 | -12.7866 | -44.8873 | 2024-10-11 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| d88b4f83-8d73-3d0f-ac03-ecdc15db4fdb | -12.7871 | -44.8639 | 2024-10-11 01:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| afb3e4b3-92f3-365c-b458-806a453ad2b1 | -12.8711 | -53.459 | 2024-10-11 01:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 42433539-64d3-3e2b-9cf7-c3a6edb97df9 | -12.8714 | -53.4382 | 2024-10-11 01:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 947aad2d-7170-3cc0-9eed-b07e6a81d6f2 | -12.9658 | -53.511 | 2024-10-11 01:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 739e5274-3a20-3b67-8a5f-a826f1230d32 | -13.7346 | -60.6079 | 2024-10-11 01:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 545a11be-5fed-3074-af11-d3d611550876 | -18.1582 | -56.4286 | 2024-10-11 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 9ce23f25-e1d6-30e6-aaa1-2f1ac10901a9 | -2.6533 | -53.3506 | 2024-10-11 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 82df7678-cfbd-3c07-917d-86bc1a5aece1 | -2.6716 | -53.3502 | 2024-10-11 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| aa8a73e6-39f4-3edf-aa42-e1ca08b6f12a | -2.7395 | -49.5412 | 2024-10-11 01:35:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f4b436df-3ab9-3fb6-875e-c615ec69feee | -2.7663 | -52.4937 | 2024-10-11 01:35:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9f8a83ac-4f15-32b2-a4f4-d2b25aa31b6f | -2.8081 | -51.0084 | 2024-10-11 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ab1f465f-0295-35a2-b0a2-7cc52459ae60 | -2.7847 | -52.4933 | 2024-10-11 01:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 0961e61b-1c06-3c8b-bb67-d1ec6d26a9a2 | -2.7848 | -52.4728 | 2024-10-11 01:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| fc104598-b8e0-3856-8bc8-51246772a244 | -2.9673 | -52.9169 | 2024-10-11 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 8a407d57-f53a-3ab9-a5c2-f671c743510a | -2.9673 | -52.8966 | 2024-10-11 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 132.9 |


[Clique aqui para ver as próximas entradas](README22.md)
