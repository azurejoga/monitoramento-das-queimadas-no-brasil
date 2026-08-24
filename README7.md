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
| 9207d744-b238-3758-bd35-3fb62fc1d08a | -6.8491 | -52.505 | 2026-08-24 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ea51fd3c-5b9c-3048-8bed-1a3c25146019 | -7.36 | -45.8361 | 2026-08-24 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 37b26b30-252f-396b-aef2-dc8ad73a1b53 | -9.4578 | -40.3392 | 2026-08-24 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.1 |
| a368ce14-1563-37a1-b1ff-becdecba392c | -12.0938 | -50.6166 | 2026-08-24 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| c9b1ab72-9c9c-385b-a2aa-344beb26d41d | -7.3603 | -45.8136 | 2026-08-24 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| e60646b1-3d32-3756-b834-ef77f501572a | -17.444 | -48.8199 | 2026-08-24 01:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 286.3 |
| a0d8e1f7-dbf2-3286-a944-ff6f39d620e7 | -7.3788 | -45.8344 | 2026-08-24 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 72671e28-70c9-3d09-8aac-b3e2455399e8 | -9.00256 | -65.39085 | 2026-08-24 01:47:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 146.6 |
| b412fc3f-30a4-33ff-937d-1fb28189386f | -8.99881 | -65.42072 | 2026-08-24 01:47:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| b227a025-2548-34f5-817f-d7373c2fa14b | -8.98622 | -65.39371 | 2026-08-24 01:47:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a8e97f37-aed9-3fc0-9e67-5e20f6360d7c | -8.99269 | -65.38547 | 2026-08-24 01:47:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 2426679a-67dc-3f4b-b7c7-e44e67a5cd84 | -9.6774 | -55.1022 | 2026-08-24 01:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 12b8291c-f65f-37ac-aecd-92f8ce56c13d | -6.8491 | -52.505 | 2026-08-24 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 257ccb30-760c-3978-8a17-2365dd476c63 | -9.006 | -65.4 | 2026-08-24 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 8061c463-bcd7-3477-b26a-f45392117805 | -7.3605 | -45.791 | 2026-08-24 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f46f3f26-0848-3e49-b95c-8f5ea031519c | -9.0061 | -65.3813 | 2026-08-24 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 54da6aaf-2c16-3098-b2dc-3444d69f5248 | -7.3791 | -45.8119 | 2026-08-24 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 5b547ad9-5ad7-3f30-a3f5-c9a8b1c9c3aa | -6.8008 | -59.5934 | 2026-08-24 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| da06e328-084d-33c6-89e3-8cecf9a52376 | -17.4241 | -48.8236 | 2026-08-24 01:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 347.3 |
| 98f285b3-3b27-3f4e-a628-075a53620605 | -22.9932 | -49.3831 | 2026-08-24 01:50:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.0 |
| 66cd9a05-bc6e-380e-9318-3cd5039fcc39 | -5.78 | -57.5605 | 2026-08-24 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 520c338b-4f9c-3567-a74b-ebfe01832793 | -7.3788 | -45.8344 | 2026-08-24 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 0be761d0-39cb-35ef-9e62-1bf71e0e7838 | -6.6233 | -58.383 | 2026-08-24 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 27913a86-e3d3-3f60-9acd-be5f586ebdfa | -17.4236 | -48.8462 | 2026-08-24 01:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 304.0 |
| 0a51bc18-1226-3fb6-97d5-b8fdad0c795f | -14.9392 | -52.664 | 2026-08-24 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 05158d41-d892-3289-a110-cd452a8a7fa0 | -7.7891 | -61.1054 | 2026-08-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b637ba34-3589-3bf7-a0d7-2afc40ce6ec4 | -7.2443 | -49.8654 | 2026-08-24 01:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 95ec6d13-e8d0-39f8-8791-c2ddd03b5575 | -7.36 | -45.8361 | 2026-08-24 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c5d5a7e2-40c1-326a-844d-cd9177d2dd5f | -7.3603 | -45.8136 | 2026-08-24 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.5 |
| f51725aa-7858-3f00-a00f-1741702162e2 | -17.4042 | -48.8274 | 2026-08-24 01:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| b5ee6f98-2d8a-34e7-8f03-9d59ef2fc06e | -17.444 | -48.8199 | 2026-08-24 01:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 325.7 |
| e2930190-b85e-3a82-bd34-009b56769646 | -6.6048 | -58.3838 | 2026-08-24 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 197d2ce6-9548-38de-a978-1db37e0f19f4 | -23.0142 | -49.3779 | 2026-08-24 01:50:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 12e29d52-a92e-384d-b17c-81cbe8ba7766 | -7.7706 | -61.1061 | 2026-08-24 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| cf4c69e9-d2ce-33b3-990c-bea430cd6b8c | -17.4435 | -48.8425 | 2026-08-24 01:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 353.8 |
| 6a79f706-b844-3d78-b392-ba76cd3a11bc | -6.6048 | -58.3838 | 2026-08-24 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 116c1077-3f62-3615-befb-b50145c47742 | -7.36 | -45.8361 | 2026-08-24 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| abcbf85d-c03f-3647-a75e-a660c614feb7 | -17.444 | -48.8199 | 2026-08-24 02:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 255.6 |
| 6f5b81f4-b14c-3b34-b7f7-7fe3d5a1a2e7 | -8.9876 | -65.3819 | 2026-08-24 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 830b2fe1-e9bc-3b62-8d09-59434a3d8e67 | -7.7891 | -61.1054 | 2026-08-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| aafa39dc-d1c5-3a42-a819-f107f986a405 | -12.0938 | -50.6166 | 2026-08-24 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| c132b6fa-4f38-3af9-9f36-f462330ca74e | -7.3603 | -45.8136 | 2026-08-24 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 7ff3fe07-ac31-32e7-a138-be83c25e4773 | -22.9932 | -49.3831 | 2026-08-24 02:00:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.8 |
| 98fadd91-8205-365c-adab-21860b7476fb | -7.263 | -49.864 | 2026-08-24 02:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d6e5fe2c-cd9d-3176-87c8-792113f702c2 | -7.7892 | -61.0863 | 2026-08-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4178d829-276e-3861-8157-6d40c268fa3a | -13.9153 | -54.007 | 2026-08-24 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 0868d349-cb7e-367b-b8d1-5d685d2c5d4b | -7.3791 | -45.8119 | 2026-08-24 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1f48139e-37d5-3cb8-a683-36489a464468 | -17.4241 | -48.8236 | 2026-08-24 02:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 500.9 |
| 5ec591d9-96f3-3a44-a5a7-4cc029a76c32 | -9.0061 | -65.3813 | 2026-08-24 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 7e183cad-0639-34f1-8250-8a8745423d5a | -17.4236 | -48.8462 | 2026-08-24 02:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 347.2 |
| 6a785ac5-78bd-3a44-9607-c02aaccc5c48 | -12.0941 | -50.5951 | 2026-08-24 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 35d9873a-06b5-3c84-a02a-1960349c2e03 | -7.2443 | -49.8654 | 2026-08-24 02:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 25dd79a9-1e08-3855-a2c4-5ae61aa249c1 | -14.9392 | -52.664 | 2026-08-24 02:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ef0eb39b-aa01-3167-9e0c-adb4a56b0f84 | -7.7706 | -61.1061 | 2026-08-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| d0f75c24-e15c-3e24-9e2e-d4a6636f651a | -7.7707 | -61.087 | 2026-08-24 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 424d105a-fc2b-336e-88c1-182a1e4157e0 | -17.4435 | -48.8425 | 2026-08-24 02:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 235.5 |
| c7d629ed-bb31-358b-a0b6-8d2ec8d5dac7 | -12.0941 | -50.5951 | 2026-08-24 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 66186e39-6e27-3088-a3c0-0066334763e5 | -7.36 | -45.8361 | 2026-08-24 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ee6d2021-e97d-3dde-a639-d8d516a1bf55 | -7.7707 | -61.087 | 2026-08-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 8adf402b-b389-35df-87dd-4e46b5e03a68 | -9.0061 | -65.3813 | 2026-08-24 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 10e63584-6e05-3a07-89da-6e1eadea4f68 | -6.6233 | -58.383 | 2026-08-24 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b06c0bd5-c3fd-337b-947e-6a8cbd741112 | -7.7891 | -61.1054 | 2026-08-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d28c5dc4-3689-3fd5-8f9f-11aacc9720ee | -14.9392 | -52.664 | 2026-08-24 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3c528a67-335c-3470-ba16-aa8ec17e99a8 | -14.9396 | -52.6428 | 2026-08-24 02:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2eb55cf1-442d-3b3f-afbc-10ae3719310a | -7.3791 | -45.8119 | 2026-08-24 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 763cdb72-c1e0-3fa5-b4ba-2ab57af30f8f | -6.8491 | -52.505 | 2026-08-24 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 27fce59b-14fc-31f7-9cf1-8d15f5bf9d34 | -9.006 | -65.4 | 2026-08-24 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d0070603-9687-398d-8b0b-714d0f817018 | -6.6048 | -58.3838 | 2026-08-24 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 28cd2b6d-7f61-3f7a-8dc1-76bcbc50643a | -7.7706 | -61.1061 | 2026-08-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| a0ea1d05-aa28-3722-84b3-eb311de62155 | -7.3603 | -45.8136 | 2026-08-24 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 58e7ddb4-0f2e-3bef-977c-d8a2ff5ec5c3 | -7.3605 | -45.791 | 2026-08-24 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 19fdba1e-7c23-3beb-b61c-4ded4c7e3aab | -12.0938 | -50.6166 | 2026-08-24 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 671be1d6-9164-3179-b33e-f9df0ce383a5 | -7.7892 | -61.0863 | 2026-08-24 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 03a748d8-f617-3e61-84a5-d12196917f28 | -9.0494 | -50.7589 | 2026-08-24 02:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 721bfda2-cd27-39d5-a52b-d69d6c15231f | -17.41 | -48.85 | 2026-08-24 02:15:00 | MSG-03 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2802f13a-0d96-366c-92ce-f090a8185720 | -17.44 | -48.86 | 2026-08-24 02:15:00 | MSG-03 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8520b690-4043-36a2-b48d-4f8d3ab06158 | -7.7706 | -61.1061 | 2026-08-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 7c025542-223f-3d76-9b32-788c3f11c6a7 | -17.4241 | -48.8236 | 2026-08-24 02:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 426.0 |
| f6243cd2-38b7-3a3c-a945-7d670421e7f0 | -14.9396 | -52.6428 | 2026-08-24 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 00a82fe5-538e-3b6c-baaa-3f89bd3bb7ab | -17.4247 | -48.801 | 2026-08-24 02:20:00 | GOES-19 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 69a608fd-cee1-3dfa-a4a5-392c6130346d | -7.7891 | -61.1054 | 2026-08-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| af52efbb-4902-3eea-81dd-2b74589954a8 | -6.6048 | -58.3838 | 2026-08-24 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 59391e9d-7ca6-338e-974c-76c0ddf0f8fa | -7.7707 | -61.087 | 2026-08-24 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 3307fd25-9aa1-3bd2-a000-51803b77efef | -9.0494 | -50.7589 | 2026-08-24 02:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ec7de8b1-59b7-3ad0-8946-bf983896809e | -12.1132 | -50.5929 | 2026-08-24 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 86574fa6-e0d5-3023-8b35-a745fa0e020e | -14.9392 | -52.664 | 2026-08-24 02:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a17d0eb4-7f76-3815-be37-f4973f3386eb | -12.0938 | -50.6166 | 2026-08-24 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 9792057e-e635-3eee-99a7-08b69e19f64a | -12.1128 | -50.6143 | 2026-08-24 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a2cab3d4-58e7-3030-bb50-e587c35a84ac | -17.4236 | -48.8462 | 2026-08-24 02:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 330.4 |
| 418ef7fa-d18b-350d-96a2-2109e46a49cd | -12.0941 | -50.5951 | 2026-08-24 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| f470ecb5-9790-3075-9387-460ccf085528 | -7.3603 | -45.8136 | 2026-08-24 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d2018bd5-1622-3150-a9c4-a5dee7a1df2e | -7.36 | -45.8361 | 2026-08-24 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9dd55a6b-5aed-30fd-98af-f3fbc700b93c | -17.444 | -48.8199 | 2026-08-24 02:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 206.2 |
| e8ddabab-3ca9-32e8-ae85-1d8c97dfb05e | -7.3605 | -45.791 | 2026-08-24 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5ce0427b-2b91-3118-a5fe-782022af598a | -17.4435 | -48.8425 | 2026-08-24 02:20:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 1da6eff2-137c-37c1-88db-504fcad31026 | -8.9876 | -65.3819 | 2026-08-24 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 749a9920-c4e4-3da8-a404-4fc7e568ca84 | -7.3791 | -45.8119 | 2026-08-24 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 88f20a0f-35b2-33b4-ae8b-c072320dff29 | -9.0492 | -50.7801 | 2026-08-24 02:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d2d95ebf-55fb-3ee4-aa2f-896504b92a07 | -9.0061 | -65.3813 | 2026-08-24 02:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 46e97ba8-7453-3e21-a23e-9f11a367000b | -17.4241 | -48.8236 | 2026-08-24 02:30:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 305.2 |


[Clique aqui para ver as próximas entradas](README8.md)
