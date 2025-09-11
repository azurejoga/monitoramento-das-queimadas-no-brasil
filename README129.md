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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cd6f201-fbe3-30eb-b6b7-4bb946e9bdd6 | -17.37737 | -52.93456 | 2025-09-11 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e1815fc1-88d7-309a-9898-57bf98dc69fe | -20.48979 | -54.91538 | 2025-09-11 05:40:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5087d08e-d8da-3cbb-b765-639e697d59ab | -11.7129 | -50.6394 | 2025-09-11 05:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6c705a58-a667-37b2-bf8b-6cf476e72119 | -19.9994 | -47.6271 | 2025-09-11 05:50:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8c36baf2-d3e9-3b94-8386-96f353c18c46 | -11.7132 | -50.618 | 2025-09-11 05:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 28b797ad-dc2b-36aa-8a3a-88b79bebea1d | -11.7322 | -50.6158 | 2025-09-11 05:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e9f74845-830b-3a49-944a-aad3ce955a49 | 4.12648 | -59.97509 | 2025-09-11 05:59:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d01eda05-7fe4-35ac-a403-064738a5f3a7 | -11.7322 | -50.6158 | 2025-09-11 06:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| f1684e89-53bf-372c-9731-ac46b6d8aee5 | -19.2212 | -48.0077 | 2025-09-11 06:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 6984dbeb-9102-34f7-9277-68bb867ae96c | -11.7129 | -50.6394 | 2025-09-11 06:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ab5dd707-ae12-371b-a87c-d42fc849c121 | -15.1016 | -50.1468 | 2025-09-11 06:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 19066bf6-9f60-39c2-96ce-9aea4c13c030 | -19.9994 | -47.6271 | 2025-09-11 06:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 036c3519-ddd4-3038-b3e6-c274a181bdb9 | -11.7132 | -50.618 | 2025-09-11 06:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 3ad48fdb-01a5-3f74-9de3-8bcb7af6bc77 | -19.2415 | -48.0033 | 2025-09-11 06:00:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| e6e77b24-7654-3c2c-9d99-0921a40b7aac | -4.93546 | -55.78415 | 2025-09-11 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 272406ba-b81a-323f-a9aa-c846727f3d2f | -4.93351 | -55.78426 | 2025-09-11 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 914c6055-93ce-35fc-8825-416a6e38e14c | -4.92629 | -55.7832 | 2025-09-11 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ab22694-555a-3002-a0da-f0f91e8b487d | -4.92824 | -55.78308 | 2025-09-11 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 73143377-845b-3b01-9dac-e5164ad83370 | -11.77656 | -64.9379 | 2025-09-11 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fbc176e-41f7-3695-ba6f-421a92318bf6 | -10.0024 | -67.59713 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a17e9ef-3776-30fd-bc7c-21727293d7ad | -10.16933 | -68.15343 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 550590fa-c401-3af1-bc76-d4fed4560625 | -11.77599 | -64.94217 | 2025-09-11 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdb304b2-d96f-379a-9598-03035ab4d442 | -10.16513 | -68.18166 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31c60164-d6ca-3745-b694-b26dc46aaddb | -8.71512 | -70.54112 | 2025-09-11 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41e18114-918f-376f-9736-b49d306086d6 | -9.99875 | -67.59657 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83e7f58b-d159-394a-828f-a2621f17fa57 | -8.98513 | -65.45046 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c391b2b-2144-36c7-ad8d-53fff58af58a | -9.14435 | -70.84554 | 2025-09-11 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 18d304f4-c05f-3ba0-abe8-00c31b7b9617 | -9.0768 | -65.47169 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75df61e4-87c5-3426-9c8a-74187fccde34 | -9.80203 | -61.52428 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7feef41-53b8-39d3-b2e9-e1dfc9b48ca3 | -9.80247 | -61.52085 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f15d619e-4678-3fc3-b3f6-dbb0a75703cd | -9.78291 | -64.88492 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 677f0820-8d50-32ff-b10d-b84f543aa25e | -11.77592 | -64.94397 | 2025-09-11 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49a6cfe5-06c4-3cfd-9295-521ac25e275a | -9.99893 | -67.59843 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27ddef6b-4a68-3178-881e-dbade0269144 | -9.80743 | -61.52502 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbd8ccba-5c6b-311c-afbd-beb825e44b1c | -10.15121 | -64.24819 | 2025-09-11 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a137b17f-790c-3dba-86a8-ea2fb4e6587b | -10.37771 | -67.82626 | 2025-09-11 06:03:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9508ee59-e17a-335b-be90-8eb992c715b9 | -9.80787 | -61.52155 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f1201b8-61a3-31e4-b815-25ef5e43c298 | -10.72912 | -69.34291 | 2025-09-11 06:03:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbaa0ad7-f3cf-3e7f-bc38-b9ae4a4eb650 | -9.79663 | -61.52356 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d36061d5-cc21-36fc-9f55-cc3777b96249 | -9.0396 | -65.41045 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e6f3e83-bda9-3596-bb49-d171083dd8af | -8.70677 | -64.21117 | 2025-09-11 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a85352a7-4f99-38a8-a772-181b647a22ab | -11.77651 | -64.93972 | 2025-09-11 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72e5ca92-549f-3789-8441-d3e25370f83a | -11.79482 | -62.73791 | 2025-09-11 06:03:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e4bfce7-fd43-3535-8dad-566c48a6ef78 | -10.92994 | -69.30482 | 2025-09-11 06:03:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13771133-f672-3809-bf68-21cbe7cf7d0e | -6.62542 | -62.84633 | 2025-09-11 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e8364c1-6126-3fbe-a009-5d5fe2ff60dc | -11.88078 | -58.80812 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4188a30b-92a7-3ed7-8344-6695075ad5c0 | -10.46512 | -67.83794 | 2025-09-11 06:03:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 238dbba3-15a2-330f-9b81-f0e98d3946bf | -11.88616 | -58.81998 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c362131-a523-36fd-bad5-824db21afc9d | -9.79212 | -61.51591 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30a06742-cb7f-3231-a108-0c1b4fe9b5e1 | -8.88703 | -70.60765 | 2025-09-11 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 63c3f349-c89c-3f4a-8a6c-c6dd8166569c | -11.87347 | -58.81391 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9ae1366-5bc7-3144-9fd5-0e04ffc9fd1f | -10.46873 | -67.8385 | 2025-09-11 06:03:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00086631-41b8-3b6b-a80e-56aba57e8875 | -9.79707 | -61.52009 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2e36ef7-c107-3a84-96ff-32f313a40df4 | -11.87948 | -58.82002 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0dd4450d-d1c3-3cbf-806d-241aba8f204a | -9.03601 | -65.4062 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 196e9f96-61c6-3234-a8b7-9e58d2424bfa | -11.88159 | -58.814 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf65c0ae-c131-34cc-a2a8-c386e2af1d53 | -9.08665 | -70.75747 | 2025-09-11 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa75c3c8-6c25-3c1a-9596-ec0ff5cd0af9 | -9.15167 | -60.2584 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c21296e-bbe5-3628-a68b-25c6497200bc | -9.98301 | -64.98874 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee883f51-2d40-3dda-9a9b-e05c27cec2b5 | -9.44794 | -68.57427 | 2025-09-11 06:03:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d911fffe-c116-3956-ab43-7c26d3cd45b0 | -10.16517 | -68.15694 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbbee963-a292-3f36-a111-21f53220e207 | -11.97139 | -63.17961 | 2025-09-11 06:03:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0b1f333-9714-3bcc-82d7-6b5d7536fa2c | -8.88758 | -70.60415 | 2025-09-11 06:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b42815d-dffa-31dc-9f6d-3ccb426d00c6 | -11.7865 | -64.93053 | 2025-09-11 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 216cc6b5-6e90-3cfe-b8f1-5935cb52326c | -10.05199 | -68.45779 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1c4cd3e7-a1fd-38b8-96af-051cb710d6b5 | -10.16578 | -68.15289 | 2025-09-11 06:03:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5da1708f-06be-336f-baae-8b31b805fba4 | -9.79168 | -61.51935 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1771fdd-573c-3275-a164-c5d412112fc3 | -8.98566 | -65.44686 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72f91a78-58a7-3db3-9a39-b3e629ccf341 | -11.87428 | -58.81936 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2010aff-b895-3c42-b32a-f0fafa8cf096 | -9.84472 | -64.99498 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 223e1270-41f2-30db-bbf7-99c117ebbba7 | -9.98413 | -64.98072 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97896930-f3d1-3baa-92f9-05c3d4fe0dff | -9.84899 | -64.99558 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 583c9b38-095b-3c9c-88aa-413b64561aa4 | -9.93054 | -65.00324 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11c17b8b-c178-3256-a8f9-a4b79fb880d3 | -11.87495 | -58.81363 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4343728c-c7a4-33dd-84e0-815d72b3cecc | -9.98357 | -64.98473 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85b110c4-dfff-3a37-ab9c-f8b3618436b9 | -11.88011 | -58.81429 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 013cc003-6337-3878-adc6-583dd488b98d | -11.88092 | -58.81966 | 2025-09-11 06:03:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 100e8c1d-f10e-3260-b7d9-e7fc96dea937 | -9.07272 | -65.47108 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6021ad5-cc26-3003-9b2c-e907f1ebe4ef | -9.04011 | -65.40679 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7bcf04d-2921-34a0-8987-bf8f9823f7e1 | -9.15748 | -60.25922 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b51c05e-6e1e-37fa-8da7-39c12134098c | -9.04063 | -65.40312 | 2025-09-11 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dee11580-7ded-36e0-98fd-77e6bcd02d15 | -9.79752 | -61.51665 | 2025-09-11 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db9862cc-6a75-3a87-bd7a-29a2bdfd666c | -9.7872 | -64.88551 | 2025-09-11 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8b2adba-6d22-31a3-a5b9-6472fb6f538c | -11.78707 | -64.92625 | 2025-09-11 06:03:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d04d0376-3f52-3f80-9356-9238b6705dba | -10.15378 | -64.24983 | 2025-09-11 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22c26b25-f6fd-3c42-9409-32904bb3590c | -10.15571 | -64.24884 | 2025-09-11 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a474d2d-3d88-3267-ae8e-d85844fa357f | -12.35254 | -63.6409 | 2025-09-11 06:05:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b10296f-3fb6-33db-af75-7f89f41cfa79 | -12.07196 | -64.17873 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef11e5a5-f020-3efb-8b09-65109b8f9b06 | -12.06731 | -64.17811 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 159de398-8fcb-32aa-99d1-35be9c35f489 | -12.40226 | -63.81609 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95f7ee01-d4e7-334b-bd01-009879b25eb3 | -12.39745 | -63.81554 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 950d77db-5c61-3a2c-8143-ace3e68df91b | -12.40158 | -63.82128 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e3ab952-5a4f-30f2-afe1-a9f587f1d003 | -12.42212 | -63.88742 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c42264eb-3d9c-3fed-8352-5ed1c4abc390 | -12.40774 | -63.81143 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26328728-1c6f-38a9-97ab-82d9ef675ca8 | -12.41666 | -63.89194 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35235c6c-03ba-3f01-b2b8-9dc7f5c221e7 | -12.41119 | -63.82243 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17180d91-6470-39b9-ab32-34ee78decd5f | -12.06331 | -64.1726 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3dd77f08-fef5-3df7-972d-8a6442956160 | -12.39265 | -63.81494 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1632650-63b0-3b4a-87e1-e99ac2f8cc87 | -12.8669 | -62.12463 | 2025-09-11 06:05:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1ef0d454-5ab9-3024-a468-75bf8a676f0e | -12.41255 | -63.812 | 2025-09-11 06:05:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README130.md)
