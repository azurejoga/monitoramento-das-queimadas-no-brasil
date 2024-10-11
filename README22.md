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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 713e2074-30eb-3aac-86a1-de8e99824538 | -2.9857 | -52.9164 | 2024-10-11 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 7df7be2c-96e3-3aaf-8a28-f20cc1e5af7a | -2.9857 | -52.8961 | 2024-10-11 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 168.4 |
| f124b312-527f-3890-8bc2-2503b2069b81 | -3.0343 | -61.6918 | 2024-10-11 01:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 350cb5a6-8056-3e0c-a56f-dccfdd151b0f | -3.0343 | -61.673 | 2024-10-11 01:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| cc445b59-a7f6-3ebd-9e11-653145a8fdca | -3.0525 | -61.6916 | 2024-10-11 01:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 9930bc89-b366-36c0-b21a-a22001d11ecd | -3.0525 | -61.6727 | 2024-10-11 01:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 2e75c305-113a-3a5b-9ea6-3c1b3fcdf149 | -3.1422 | -50.4562 | 2024-10-11 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1d4c2a46-6c9f-320f-abc0-8d0a331d4a9c | -3.1423 | -50.4352 | 2024-10-11 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| cd7a501a-085e-3627-a973-5c41a9a99f7a | -3.1607 | -50.4556 | 2024-10-11 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4f24d27a-3b04-3dcf-a6ae-a6c0fd9fa350 | -3.1608 | -50.4347 | 2024-10-11 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| d43b0773-2987-3c87-a2a9-a5c517790c41 | -3.2912 | -46.0731 | 2024-10-11 01:35:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| af8aa472-a5e5-3d88-90c2-2458b555dc20 | -3.3098 | -46.0724 | 2024-10-11 01:35:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6e5c870c-f432-379f-8213-1e038803aea5 | -3.614 | -44.7783 | 2024-10-11 01:35:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6e6e5a8c-7e7c-3b52-b4e8-3c754ebb556b | -4.0962 | -48.2523 | 2024-10-11 01:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 93c1b67f-e5c0-3461-9efc-485f66af7ca4 | -4.1146 | -48.2731 | 2024-10-11 01:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3f715493-f240-3a17-ad4b-f072fd7a8744 | -4.1148 | -48.2515 | 2024-10-11 01:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 258.3 |
| abb91e1b-e1d8-335c-bb09-8d5398143993 | -4.1149 | -48.2299 | 2024-10-11 01:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2acbd7a9-18dd-3fb8-ba85-a12be579c19c | -6.5404 | -60.0259 | 2024-10-11 01:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f19a1fa9-4c0c-3b66-9790-73591aa58430 | -6.5589 | -60.0252 | 2024-10-11 01:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 04baa701-a6e3-37f6-b9f8-40531afd042d | -6.8006 | -59.6319 | 2024-10-11 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 9cc5d632-3498-341e-a779-3e4d3d26ddb8 | -8.4231 | -55.4704 | 2024-10-11 01:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 62e90132-666f-378a-9fe2-5380472c8df3 | -8.4417 | -55.4692 | 2024-10-11 01:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ac29a82b-7d1b-3ba1-91a1-202eae52207b | -8.6119 | -46.4796 | 2024-10-11 01:35:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6287c898-3426-3f1d-88d2-9ffb61caa325 | -9.6575 | -64.9658 | 2024-10-11 01:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 294b90aa-df06-38dc-826b-2d21b1de73fa | -9.9481 | -58.1092 | 2024-10-11 01:36:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 0951a8d6-3148-3bb8-912e-12ae9b5731de | -10.3632 | -55.8554 | 2024-10-11 01:36:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 36a8183c-49c1-3f25-9715-8121272204db | -10.4713 | -49.9838 | 2024-10-11 01:36:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7391962b-d0bf-37a4-ba50-d406fcd960d2 | -10.5755 | -64.0438 | 2024-10-11 01:36:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ab067939-c8c4-30a2-aca3-f7bd21000111 | -10.5757 | -64.0248 | 2024-10-11 01:36:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a58517cb-5795-381c-abce-1402ddeff8fa | -10.6962 | -53.0354 | 2024-10-11 01:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 3bb0a826-2495-361b-8df3-8ff3203e7ba0 | -10.6965 | -53.0147 | 2024-10-11 01:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| ae7af2f5-a610-37d7-9cf5-f199d8c19288 | -10.7059 | -64.1138 | 2024-10-11 01:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 89bf95ee-3c25-3e4c-9652-70ded2e5b48e | -10.8935 | -52.3517 | 2024-10-11 01:36:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d99af256-7d3b-379e-91b1-33fac04487ba | -10.8938 | -52.3308 | 2024-10-11 01:36:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6691180d-797d-33e2-9d66-c47e06808c80 | -10.9124 | -52.3498 | 2024-10-11 01:36:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 29c022d3-f604-355b-b9e8-00f7ce96fe10 | -10.9127 | -52.3289 | 2024-10-11 01:36:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 502e0340-fa6d-3136-9954-bd0d487d5c6a | -11.2407 | -53.2738 | 2024-10-11 01:36:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6984f12a-a654-3a51-ac26-fd58b8861bff | -11.2597 | -53.272 | 2024-10-11 01:36:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 054a11f8-b7d9-3ab6-a5c0-802c498e3ef3 | -12.3463 | -43.7638 | 2024-10-11 01:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4fa9f9d4-b802-32f4-9602-1ec6e9d47b9d | -12.7871 | -44.8639 | 2024-10-11 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| fef2ed28-11ae-3fca-991b-90b9a4fad3d8 | -12.7673 | -44.8904 | 2024-10-11 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| c743393b-d2ce-3d28-9b21-2c42e70aeb94 | -12.7678 | -44.8671 | 2024-10-11 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 41c4c98e-8ec4-395a-a171-6a25fc6cf6fa | -12.7866 | -44.8873 | 2024-10-11 01:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.0 |
| d7b0c96f-cbf1-3b6e-b787-a03c2f8c7c65 | -13.7346 | -60.6079 | 2024-10-11 01:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 80413768-b0ec-3d10-a030-4d191db1d825 | -15.6719 | -59.3204 | 2024-10-11 01:38:19 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41918f5b-68e4-30ae-8c24-b5092b9bd17a | -15.6735 | -59.327499 | 2024-10-11 01:38:19 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97acae76-e290-3cc8-af09-949e94bd4726 | -15.4348 | -60.010502 | 2024-10-11 01:38:26 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8106083-5608-35fa-b753-7434e33e895f | -12.8902 | -53.459499 | 2024-10-11 01:38:41 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd9197ca-8222-3235-843f-44614e06c155 | -12.8936 | -53.472801 | 2024-10-11 01:38:41 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7247b386-6d41-334d-b2f6-fc086025e78c | -12.897 | -53.486 | 2024-10-11 01:38:41 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c5e8b44-1100-393f-bd4e-e239d6d87e4e | -12.8805 | -53.462002 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 318f50d1-f085-3382-aa79-3ec2427b6464 | -12.8839 | -53.4753 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7693f9b9-ef69-3625-946b-6073920e3e69 | -12.8873 | -53.488499 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cf7629a-a8e8-3691-848d-3c2f502690ed | -12.8906 | -53.501801 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5ae4c13-4e6a-3979-b22b-49b55bf9940e | -12.8708 | -53.4646 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b86c638-43d7-3495-9d9e-b3544bdd91e6 | -12.8742 | -53.477901 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a67e1ad8-244e-336f-9693-74c9c1d3252a | -12.8776 | -53.4911 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6724a427-6842-3937-af23-11c48ff82cfe | -12.8577 | -53.4538 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb02e798-ef06-3c02-a5f1-f11a9bea00d5 | -12.8611 | -53.467098 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48269c01-5d9b-36ea-ae62-b8aef105f546 | -12.8645 | -53.4804 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 424f650c-9876-3149-8059-bf149751da7d | -12.8678 | -53.493599 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 331517fa-9de5-3fb6-9ff7-2ce1e80dba2e | -12.848 | -53.456402 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99b0a046-6a19-3621-bd4e-cac949eb2955 | -12.8514 | -53.4697 | 2024-10-11 01:38:42 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d498142e-d296-380d-a37e-74437ce13f9a | -12.4678 | -53.1007 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 732cb4c8-46fc-3125-aa43-2af117778729 | -12.4581 | -53.103298 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7f81132-3301-363e-abff-f951b95c23ff | -12.4617 | -53.1175 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 350fddee-2cc6-31cc-831f-1430ce2f611d | -12.4654 | -53.131699 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 686cb0d8-4c0d-35fd-a345-259e9c443112 | -12.469 | -53.145901 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b1b2694-875c-30e5-9af9-0c7007d180a2 | -12.452 | -53.119999 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f71958b-c50c-3d8c-aa8f-4cb87d2d8f2f | -12.4557 | -53.134201 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4915d7c-5da3-362b-9314-3974b50ad58b | -12.4593 | -53.148399 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3adc5fc-f846-34c4-ab0a-6ece6291173f | -12.4423 | -53.122601 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf6f28a-3123-3874-a35c-e431b891fba8 | -12.446 | -53.136799 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9827c0d3-5b81-3a1b-97a6-fb00cab71505 | -12.4496 | -53.151001 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3bcbe76-a9ca-319a-9806-5f9b31e45e94 | -12.4327 | -53.125099 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd52b65f-fd12-39f2-bf49-3ded5b7f8513 | -12.4363 | -53.139301 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c720a575-f986-3811-b956-9469e7318058 | -12.44 | -53.1535 | 2024-10-11 01:38:47 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 691fb4dc-c322-35a2-8d45-cec45fa62634 | -13.7429 | -60.595299 | 2024-10-11 01:38:55 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef896f5-b6f4-37f2-8a60-614db6a1cd9a | -13.7445 | -60.602402 | 2024-10-11 01:38:55 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf9715c4-e971-36a4-b3ba-152a4e0dd77b | -13.7363 | -60.611698 | 2024-10-11 01:38:55 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59f7d7f9-8192-342f-a97e-3d2697d492c2 | -11.2547 | -53.248901 | 2024-10-11 01:39:07 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5e6e68a-a12a-35f9-9084-78b4a626296b | -11.2584 | -53.2635 | 2024-10-11 01:39:07 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2a218a-ca51-3918-a529-4d51207c686e | -11.262 | -53.278 | 2024-10-11 01:39:07 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b057f7d-f7dd-3fb6-80b5-e0316f529ccc | -11.2487 | -53.265999 | 2024-10-11 01:39:07 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33ff622b-33cd-3140-9553-252393bcbb4c | -11.239 | -53.268501 | 2024-10-11 01:39:07 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e08636c4-4a3b-331a-9190-97494d6a7209 | -10.8974 | -52.336498 | 2024-10-11 01:39:09 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f5b41b2-a13a-3d6b-970a-3e4fe4a827b7 | -12.9796 | -62.5023 | 2024-10-11 01:39:14 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 214ec40c-a879-3a62-9ed2-7b9629d03933 | -10.6981 | -53.009899 | 2024-10-11 01:39:15 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a68cc3a6-c8d3-3a46-ab99-808b5517e236 | -10.702 | -53.025299 | 2024-10-11 01:39:15 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8fb4c4-ef4f-3991-b604-b7b8593b3fc0 | -10.7059 | -53.040699 | 2024-10-11 01:39:15 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58051fe2-1fc4-3fd7-9854-8ae0f83ac840 | -10.6884 | -53.012501 | 2024-10-11 01:39:15 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25bde984-8251-35fc-b3ce-0e7c977282f1 | -10.6923 | -53.027901 | 2024-10-11 01:39:15 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c468d3a-eeac-3d0b-82cd-d396985e6ae7 | -10.6362 | -55.873001 | 2024-10-11 01:39:27 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 392981cc-68ce-3f6a-9260-9f265f58e81f | -10.6289 | -55.9282 | 2024-10-11 01:39:28 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7a58a16-73da-38fc-b8f6-6dc8403272ae | -11.542 | -60.290298 | 2024-10-11 01:39:30 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0e6373af-d3d5-3e9c-8c10-4b4ec6f06c48 | -11.5436 | -60.297298 | 2024-10-11 01:39:30 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 14799c29-8475-3875-81a9-98cfd4691b1e | -10.3726 | -55.8517 | 2024-10-11 01:39:32 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9e91355-bd45-37d9-a67d-070b542b9169 | -10.3751 | -55.8619 | 2024-10-11 01:39:32 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2df62c06-23d2-3620-9aa0-2e110170cee5 | -10.3629 | -55.854099 | 2024-10-11 01:39:32 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7ddfa00-1652-34bb-b77f-77d9446211ce | -10.3654 | -55.8643 | 2024-10-11 01:39:32 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
