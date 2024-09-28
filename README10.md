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
| 4ac7adb5-1641-34ed-a000-3fd01fffb6b1 | -3.5753 | -50.530499 | 2024-09-28 00:15:42 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25cdbbf6-2277-34b2-90da-25d6a74b110c | -2.5944 | -45.971699 | 2024-09-28 00:15:42 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 866b88fe-9ffe-341f-a389-1d88df7bc3ca | -2.5961 | -45.979 | 2024-09-28 00:15:42 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9aa5d068-f8f3-3b08-997c-14a9b4687a5d | -2.5977 | -45.986301 | 2024-09-28 00:15:42 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b75af2fe-263a-3ead-80cd-05404a5c4f75 | -2.5846 | -45.973801 | 2024-09-28 00:15:42 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19ad3617-f19c-335c-a898-93875047ddf7 | -2.5863 | -45.981098 | 2024-09-28 00:15:42 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aaf5691a-6a02-359d-907d-042e0d1de363 | -2.5879 | -45.988499 | 2024-09-28 00:15:42 | METOP-B | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 26758b18-2b91-31b4-8922-823979dd76e9 | -3.5568 | -50.353401 | 2024-09-28 00:15:42 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87e4a9f1-b482-3e80-a3d3-5d545a14b606 | -2.7192 | -46.7127 | 2024-09-28 00:15:42 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9fc795f-0d4d-361b-a39c-8ec89491ad41 | -2.7209 | -46.720501 | 2024-09-28 00:15:42 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7eee1bb-e695-3194-987e-dc8201ced7ee | -3.5655 | -50.5326 | 2024-09-28 00:15:42 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4558dd6-f31a-30bd-ab70-d8c4a4c1aafb | -3.5685 | -50.546101 | 2024-09-28 00:15:42 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a384304-f751-3f47-a1b7-3fa2f3266fe4 | -2.7094 | -46.714802 | 2024-09-28 00:15:42 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0faed4b3-eab8-326d-8e6f-7a0a02db1249 | -2.7111 | -46.722599 | 2024-09-28 00:15:42 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9411d90b-8bf9-39e7-8edc-6928bf434c46 | -3.5587 | -50.548199 | 2024-09-28 00:15:42 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe49cb7-0e5c-3e6f-b241-0be0e2ea37f2 | -3.5617 | -50.561699 | 2024-09-28 00:15:42 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e55175ae-d2f2-3565-8c46-62e19aba0644 | -3.3164 | -50.2827 | 2024-09-28 00:15:45 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebe7cb5e-6441-312d-afb1-f7d3c7bcb900 | -3.3193 | -50.295601 | 2024-09-28 00:15:45 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be2a88d-ff3c-3a4e-8b60-56ecdd92e7b6 | -2.5614 | -47.295502 | 2024-09-28 00:15:47 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae0360f5-e683-384f-862c-cf9167919bb9 | -2.3778 | -46.520401 | 2024-09-28 00:15:47 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 369e141d-bf77-3557-ae82-f9bafeacdf47 | -2.3795 | -46.528 | 2024-09-28 00:15:47 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c56c41e-dec0-345d-adb6-a147fce5c426 | -2.5332 | -47.215199 | 2024-09-28 00:15:47 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5444fc10-3389-3178-8bf2-6eb1c8aa9b8b | -2.5351 | -47.2234 | 2024-09-28 00:15:47 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bafb2053-0704-3e90-9ed9-10f0e2f75b6a | -3.1899 | -50.4049 | 2024-09-28 00:15:48 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eafc5bc-9c61-35cf-9eb7-12b6120102e6 | -3.1928 | -50.417999 | 2024-09-28 00:15:48 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce95abe-6dff-3d12-8e08-842007fef33d | -3.1957 | -50.431099 | 2024-09-28 00:15:48 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8179ae60-2bcc-3590-badb-6097ac18f6a8 | -3.1831 | -50.420101 | 2024-09-28 00:15:48 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf4fdab-7cac-34d0-b3fd-83dc766d216e | -3.186 | -50.433201 | 2024-09-28 00:15:48 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9068a554-be99-397d-b949-21823363a123 | -3.1363 | -50.254601 | 2024-09-28 00:15:48 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebe65c6-ef9d-3756-9596-3cd4fd864e68 | -2.6356 | -48.0424 | 2024-09-28 00:15:48 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a877ae36-332e-3770-b6b1-f3b680304ccc | -2.6258 | -48.044498 | 2024-09-28 00:15:49 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a371920b-3661-387a-86a2-01fb08b51d09 | -3.0883 | -50.4543 | 2024-09-28 00:15:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 596d4187-ac61-3640-bf90-38411e427d7a | -3.0757 | -50.443298 | 2024-09-28 00:15:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65ac95fd-6085-3f3c-8509-924c452c364c | -3.0786 | -50.456402 | 2024-09-28 00:15:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cea33a96-c658-3fda-bb87-ee20fdd50a75 | -3.0815 | -50.469501 | 2024-09-28 00:15:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e171f37-0a34-3862-953b-db9bf8106c54 | -3.0659 | -50.4454 | 2024-09-28 00:15:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c01e7585-6c4d-3f4f-85cc-7ebb5c92e31b | -3.0688 | -50.4585 | 2024-09-28 00:15:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69db0520-1b04-3509-a9b1-3b3bc720a5d3 | -3.0717 | -50.4716 | 2024-09-28 00:15:50 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db5d2e6b-38dc-33d1-a762-8e73850a5a10 | -2.4806 | -48.0382 | 2024-09-28 00:15:51 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6745680-5e4e-34e0-b71b-5c3d096478ab | -2.4826 | -48.047298 | 2024-09-28 00:15:51 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abd4eeac-b77f-3482-925a-9eaedec35392 | -2.4708 | -48.040401 | 2024-09-28 00:15:51 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf7b88b7-1eb7-3ca4-b11b-5f23aed992fb | -2.4728 | -48.0494 | 2024-09-28 00:15:51 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b378e68-eaad-3092-a64a-30c3e766323c | -2.8913 | -50.4422 | 2024-09-28 00:15:53 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56aa34c-2b73-3c4c-8168-fb3589a51d62 | -2.8942 | -50.4552 | 2024-09-28 00:15:53 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be92b195-3227-3b23-aa01-91d4f50bb727 | -3.0108 | -51.030102 | 2024-09-28 00:15:53 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 677a985a-6c3a-3000-b19b-bbf3496e32b6 | -2.1056 | -47.096298 | 2024-09-28 00:15:54 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee9ce8e2-fb07-3b27-b2f3-5b1874160d5c | -2.1073 | -47.104401 | 2024-09-28 00:15:54 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc18fb6-6ad1-3716-acce-7ccee08314e6 | -2.1091 | -47.1124 | 2024-09-28 00:15:54 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91bdd2fd-8e38-36b4-a9b8-fcb213897ca5 | -2.1109 | -47.120399 | 2024-09-28 00:15:54 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 246fadaf-a459-3b85-b385-481d4e9f9b7f | -2.0975 | -47.106602 | 2024-09-28 00:15:54 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ded4c22-a88a-3030-988a-c367e0e1c2e2 | -2.0993 | -47.114601 | 2024-09-28 00:15:54 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcffb887-e9db-3979-92fa-e3aca13db3bd | -2.1011 | -47.122601 | 2024-09-28 00:15:54 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b3b0903-20f4-3cdc-912a-689476a6a072 | -2.8773 | -51.3503 | 2024-09-28 00:15:56 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3034f3bf-d56d-3f3d-b9ed-da18d6e5695d | -2.8675 | -51.352402 | 2024-09-28 00:15:57 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a30e5469-e191-30a7-ac72-ebe9504717cc | -2.87 | -51.640999 | 2024-09-28 00:15:58 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d9f67f-85c4-38ff-84a9-cc169d01d63c | -2.8734 | -51.6567 | 2024-09-28 00:15:58 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64fe33c3-886b-3e05-8983-183a29960b44 | -2.8602 | -51.643101 | 2024-09-28 00:15:58 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c659cc3-7a7c-36c0-b61d-c2a71e7e22dc | -2.8636 | -51.658798 | 2024-09-28 00:15:58 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddd3ba14-1999-3cef-be67-3cbcb897e90d | -3.2038 | -53.346298 | 2024-09-28 00:15:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1926d16a-96ab-3015-bf10-3821bf0c4871 | -3.2084 | -53.367298 | 2024-09-28 00:15:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f817a84-04a1-3f42-b49a-512ce34f8a2c | -3.1941 | -53.348301 | 2024-09-28 00:15:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3142558f-6e57-3a50-83a7-929786beb7be | -3.1987 | -53.369301 | 2024-09-28 00:15:58 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0815d704-ff6f-3da8-8c91-d0d25eff1904 | -3.1339 | -53.629601 | 2024-09-28 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4516599-783c-390e-a273-33ebae2b994d | -3.1387 | -53.651501 | 2024-09-28 00:16:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adaf65b2-ff85-3d47-a180-683cc2da1c08 | -3.1242 | -53.631699 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e293714d-a701-3e90-b9df-379055e6218f | -3.129 | -53.653599 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6729cce3-274d-38e0-ae75-190c76e3fdb8 | -3.1338 | -53.675598 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0795d9-26a0-39ac-b2c2-f337dfc5999e | -3.1145 | -53.633701 | 2024-09-28 00:16:01 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72c2065-7ad0-3648-8232-bd1efbf6a9f8 | -3.1193 | -53.655602 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94b1a784-ba60-3916-b9a7-872817825262 | -3.1192 | -53.701698 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fae51d1-0ace-367c-8847-ff7bdcc86a95 | -3.1241 | -53.723801 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb34b12-f04f-32b2-87ad-86b2696f509c | -3.1095 | -53.7038 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d72e8b39-8015-3d0a-a95a-8b4890cb6c47 | -3.1144 | -53.725899 | 2024-09-28 00:16:01 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78da8d50-c117-342e-bced-7e40c1eaaff5 | -1.1724 | -46.698101 | 2024-09-28 00:16:07 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49a1138c-50c4-309d-88a2-745d77c8e557 | -1.1741 | -46.7057 | 2024-09-28 00:16:07 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f45e5939-45ce-303d-9ce9-067a37c6f00d | -1.1758 | -46.713299 | 2024-09-28 00:16:07 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 325cf535-4e47-3b2c-86f6-2b97d4b9ae40 | -2.2091 | -53.626099 | 2024-09-28 00:16:16 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc89f605-4246-3885-b5e0-c325bd6b31e6 | -2.2138 | -53.647202 | 2024-09-28 00:16:16 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fbd32cc-1e78-339f-af95-b95cfb90aeab | -1.5696 | -54.719299 | 2024-09-28 00:16:30 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06fa84c2-e4da-3f6d-a85f-021d8a34b2eb | -1.5751 | -54.7439 | 2024-09-28 00:16:30 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af01bd2f-d1db-318a-bca1-bfd89a23c69c | -1.5599 | -54.721401 | 2024-09-28 00:16:30 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a5de27-b64c-395c-a5d6-97560f64f5fd | -1.5654 | -54.745998 | 2024-09-28 00:16:30 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 830504ea-7001-3228-ac1c-0849564f154d | 1.3707 | -50.722 | 2024-09-28 00:17:03 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8e5ee7ac-4b9a-3f42-8b5f-e781c08ec0f5 | -22.11054 | -44.72862 | 2024-09-28 00:22:00 | TERRA_M-M | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 0f9815b0-128e-3245-bb83-4dfbfa26a822 | -21.70602 | -41.82191 | 2024-09-28 00:22:00 | TERRA_M-M | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3fcd80bf-a3ba-37d2-b3b5-77d57a07c99d | -21.63293 | -47.775 | 2024-09-28 00:22:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e0b38df8-3239-3933-a677-095f8b99b887 | -21.62017 | -47.77118 | 2024-09-28 00:22:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 195f4de1-de3b-3897-8cf9-22463ebf5cc6 | -21.51587 | -42.05285 | 2024-09-28 00:22:00 | TERRA_M-M | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| 0ee91f66-ea62-3d17-b23b-47c9e82d7312 | -21.51446 | -42.06076 | 2024-09-28 00:22:00 | TERRA_M-M | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| f1980baf-713d-3e1a-bf9c-d5f150e497b7 | -21.51259 | -42.04464 | 2024-09-28 00:22:00 | TERRA_M-M | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| dc3a2a3e-0f51-3056-8b5b-9f58e9698e7a | -21.29555 | -41.93796 | 2024-09-28 00:22:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 0ff16e0e-c2dd-3413-a693-d7f2220eb6cd | -21.29378 | -41.92265 | 2024-09-28 00:22:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| c386ffcb-2941-3537-9999-f9bc1dcdb15e | -21.27654 | -45.80356 | 2024-09-28 00:22:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.8 |
| 167e9383-ac9d-342d-b1e1-ed21be37382b | -21.27504 | -45.8088 | 2024-09-28 00:22:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.5 |
| 78dcfacb-d74a-3792-b0ba-3c5282cded12 | -21.13795 | -42.25575 | 2024-09-28 00:22:00 | TERRA_M-M | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| c84c37ce-c082-33ec-8266-7708f17088a7 | -21.12687 | -42.25719 | 2024-09-28 00:22:00 | TERRA_M-M | EUGENÓPOLIS | MINAS GERAIS | Brasil | 3124906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 75672e2c-415f-3d95-a18a-43efd50bb6db | -21.03709 | -42.67551 | 2024-09-28 00:22:00 | TERRA_M-M | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.3 |
| 17480bfd-45d6-3717-a9ee-11549b0786b6 | -21.0351 | -42.65809 | 2024-09-28 00:22:00 | TERRA_M-M | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 52203c1a-e8c5-351d-be79-bd0ff0896dd6 | -21.03508 | -42.66903 | 2024-09-28 00:22:00 | TERRA_M-M | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.7 |
| 08adf292-a0f2-356b-97a9-833a21979693 | -20.83428 | -41.62512 | 2024-09-28 00:22:00 | TERRA_M-M | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |


[Clique aqui para ver as próximas entradas](README11.md)
