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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f230f8-8f10-3136-828a-81f94301444d | -9.482 | -63.1253 | 2024-10-10 01:26:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ca4df9f8-fd5f-3ef7-ae00-c0e45497e999 | -9.5005 | -63.1435 | 2024-10-10 01:26:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 353562b2-4a52-3b7a-b04d-59c74cf09185 | -10.363 | -55.8755 | 2024-10-10 01:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 792fb68a-dcca-3cd6-867f-28be441a6d00 | -10.3632 | -55.8554 | 2024-10-10 01:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| d09e8915-bf74-3df8-a6a1-7c99d20b5bc0 | -10.3707 | -61.2513 | 2024-10-10 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6a0c8f05-e544-384c-886e-17aee4849393 | -10.4287 | -60.9979 | 2024-10-10 01:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f160ff95-c959-3c2b-b60c-427432d9a906 | -10.5746 | -48.0178 | 2024-10-10 01:26:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a655e7a7-e607-370e-b9f8-ec3df5325fcb | -10.6258 | -55.8953 | 2024-10-10 01:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 6b09ede6-c648-3a4d-81b0-008fa48e344c | -11.0252 | -57.2436 | 2024-10-10 01:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 05d1006e-9761-37d7-9d76-3bacad59c4fe | -11.0254 | -57.2237 | 2024-10-10 01:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 2f71463f-6273-3eec-be3c-da77e753ba7c | -11.0256 | -57.2038 | 2024-10-10 01:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 165.7 |
| 2c7d8617-5c93-3783-a2c2-025aaff9927b | -11.0443 | -57.2222 | 2024-10-10 01:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 192.0 |
| a136b878-3ed1-3ab3-b545-23eaca0918f8 | -11.0445 | -57.2023 | 2024-10-10 01:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 50b52ffa-cd2f-3a63-b0d6-c9740f9f2f98 | -12.3256 | -59.1627 | 2024-10-10 01:26:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| aa2f5bd3-5ecd-32bf-b0af-d5fb211ddf8f | -12.3987 | -54.5816 | 2024-10-10 01:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 9db7b8ac-2417-30f8-bdd0-8bc9645254c1 | -12.4177 | -54.5797 | 2024-10-10 01:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 3b2ba080-6bdf-3220-8c31-1b50eac81947 | -12.418 | -54.5592 | 2024-10-10 01:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 8b9c187b-49b7-3089-9dec-8d7914fe8d03 | -12.9255 | -51.1361 | 2024-10-10 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 3c52b13f-33d0-3692-b2b0-8518f6f7436a | -12.9447 | -51.1337 | 2024-10-10 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| fbcbcf57-8d3b-33e9-9125-29514f1e8ec4 | -13.1845 | -51.7004 | 2024-10-10 01:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b08034db-9585-3ef7-b08c-53cadede5941 | -13.8374 | -44.5455 | 2024-10-10 01:26:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ae450ed1-187e-3d2d-ade9-88e46edd4b01 | -13.8569 | -44.5421 | 2024-10-10 01:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 5fa8d11d-36dc-3e62-92b4-ca579c86205f | -17.0549 | -45.2808 | 2024-10-10 01:26:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 73ab95dc-1f42-3731-8c49-66565591aacb | -2.6533 | -53.3506 | 2024-10-10 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 4714ca1e-9b09-3034-83b8-4c92e1fb6ec7 | -2.6716 | -53.3704 | 2024-10-10 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 166622a6-b25c-3917-b196-df307d8cade0 | -2.6716 | -53.3502 | 2024-10-10 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 401.2 |
| 4b2a2e7b-ba96-363b-b173-fe6d8b0f5336 | -2.6717 | -53.3299 | 2024-10-10 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| d13426f7-530f-3169-827e-ac38ebbfa415 | -2.69 | -53.3497 | 2024-10-10 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| e1548d37-baef-3591-aafc-dc84aa5ab93d | -2.6901 | -53.3295 | 2024-10-10 01:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 0a5eb815-ef86-38c5-89f6-7d3d17b0ffc0 | -3.8147 | -45.4918 | 2024-10-10 01:35:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 6ccf900c-e596-30e8-9859-36497f13135a | -4.0961 | -48.2739 | 2024-10-10 01:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| b254423d-708e-36e2-8f2e-fac60e9ed9a9 | -4.0962 | -48.2523 | 2024-10-10 01:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| bbe8c3a1-896a-3160-94fe-48645fbb4f1c | -4.1146 | -48.2731 | 2024-10-10 01:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 171.4 |
| da2d70e0-52c7-35c1-aa05-3bf12d151ce2 | -4.1148 | -48.2515 | 2024-10-10 01:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| b5a1e1d9-b667-3a71-8006-95ec2b41ac1e | -4.4776 | -46.5956 | 2024-10-10 01:35:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 44fde2a5-e7e7-3190-a93a-34fa849f3e9a | -5.9036 | -45.4127 | 2024-10-10 01:35:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a6bf1a8e-56fd-36b2-9336-c85f43c4e49d | -5.9223 | -45.4114 | 2024-10-10 01:35:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 38ad3da1-9b15-3c13-84fc-9c18c471a414 | -6.5218 | -60.0649 | 2024-10-10 01:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 5638df21-377e-3141-8107-41c521118eb3 | -6.5219 | -60.0457 | 2024-10-10 01:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 52ed8c62-662e-3db7-8cdf-6cea4793148a | -6.747 | -59.3259 | 2024-10-10 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 79cec152-aaf1-3925-8704-233e30266a3b | -6.7654 | -59.3252 | 2024-10-10 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 4dc8c8af-3fc5-3f42-b332-f0547c2fa1d6 | -6.7655 | -59.3059 | 2024-10-10 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| bf1ff6ac-66f3-3780-9712-428098edad8d | -6.7839 | -59.3245 | 2024-10-10 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b0672d67-cac8-327f-962a-11c6ec62c6eb | -6.784 | -59.3052 | 2024-10-10 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9758c3af-53e5-30dd-9a4c-cc0465f9117f | -7.1346 | -59.3099 | 2024-10-10 01:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 1cf6bc10-067e-3c94-8f49-d0c4fc1b4a22 | -7.694 | -42.997 | 2024-10-10 01:35:49 | GOES-16 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 8ef37195-3a42-3048-82e5-c46560346d12 | -8.1475 | -42.9717 | 2024-10-10 01:35:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| e64f63af-95b5-349d-a665-92a0c129380d | -8.2325 | -61.1823 | 2024-10-10 01:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ffc87e0f-0888-354f-84a6-f3104b6e096d | -8.6844 | -63.082 | 2024-10-10 01:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 269b3d69-e1d8-30e7-a403-5a8afa4efa2f | -8.7029 | -63.0813 | 2024-10-10 01:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| dd428d24-9dcc-3464-a0d0-26cfb9010c97 | -9.0084 | -61.6253 | 2024-10-10 01:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e0ef5275-138f-30f3-bd4b-61e13cce6afa | -9.0085 | -61.6062 | 2024-10-10 01:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3262bd42-863a-33aa-b3fb-433a79da4ff6 | -9.027 | -61.6244 | 2024-10-10 01:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| dd6591cc-1a03-351c-8859-0527e9c37e0f | -9.0271 | -61.6053 | 2024-10-10 01:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9e6e047d-87a5-3106-8e75-e8d081cb7f63 | -9.0656 | -61.3934 | 2024-10-10 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 326fad76-4938-3046-998b-987ae3ca8870 | -9.0841 | -61.4117 | 2024-10-10 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2d4ac787-d54c-32ad-aa68-338cd7dcfb4f | -9.0842 | -61.3925 | 2024-10-10 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| be4e9105-846b-307c-b395-295498313de1 | -9.1035 | -61.2769 | 2024-10-10 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 99efb002-345a-3eb1-933f-5efc22eacf9c | -9.122 | -61.2951 | 2024-10-10 01:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0442c9a5-8f1b-3dd8-ae59-e9f92a281a01 | -9.1221 | -61.276 | 2024-10-10 01:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 170.0 |
| dea55ac3-b8ce-31fa-8500-4f77d95e294a | -9.4633 | -63.1451 | 2024-10-10 01:36:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 08032203-4a13-37bc-a7a7-799424ebd76b | -9.4818 | -63.1632 | 2024-10-10 01:36:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 477ce5b0-9262-3795-91ef-a5cb8434aa76 | -9.4819 | -63.1443 | 2024-10-10 01:36:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 20c21d6b-0927-35a9-a1a0-07299c408d2a | -9.482 | -63.1253 | 2024-10-10 01:36:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 97c8fcdd-3bf3-37bf-8d41-35f478ce3781 | -9.5005 | -63.1435 | 2024-10-10 01:36:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 48ad4711-aca9-37a7-a2c4-d0b118eb741b | -10.352 | -61.2523 | 2024-10-10 01:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 136c0186-1e21-3ccc-aaf0-dac3f384b9aa | -10.3707 | -61.2513 | 2024-10-10 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| ed5b35d3-228b-3168-8062-0987ec802338 | -10.3708 | -61.232 | 2024-10-10 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a9d511b5-473f-3c04-8449-9809d64a1a44 | -10.4287 | -60.9979 | 2024-10-10 01:36:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 74dae5a1-eccc-30b5-83ce-f5ec5d8ada0c | -10.6258 | -55.8953 | 2024-10-10 01:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| ef0a6daf-6146-3c5c-95fb-ba14f83a0fc6 | -10.6832 | -51.0907 | 2024-10-10 01:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 865e6af1-97b2-3b50-8437-9d083cc7c21e | -11.0252 | -57.2436 | 2024-10-10 01:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 6c835bd6-01b9-3a65-9420-87de68de52b3 | -11.0254 | -57.2237 | 2024-10-10 01:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 44f9abf8-b304-36cc-ba76-584c77f5f6d4 | -11.0256 | -57.2038 | 2024-10-10 01:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 4809a76b-64d4-38ea-ac59-30980d4b3083 | -11.0441 | -57.2421 | 2024-10-10 01:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| f1a433c5-dc10-3712-91c5-8a048ecf3c41 | -11.0443 | -57.2222 | 2024-10-10 01:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 175.5 |
| 965cf292-0bde-3329-abe2-b18e8173934d | -11.0445 | -57.2023 | 2024-10-10 01:36:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 684c5674-9ef2-3143-912c-f31b3e9316f7 | -12.2888 | -43.7495 | 2024-10-10 01:36:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| e13b3143-c3d2-3fb1-8188-2e2a4ce97025 | -12.2893 | -43.7258 | 2024-10-10 01:36:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 952cca8d-6e96-3837-943d-9531a6096209 | -12.3256 | -59.1627 | 2024-10-10 01:36:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 304cb98e-4492-3043-9879-f2859be0c28d | -12.3987 | -54.5816 | 2024-10-10 01:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5f441915-91c1-3f4a-a8e5-65ca0d27596a | -12.3989 | -54.5611 | 2024-10-10 01:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c16e0c15-0447-33ed-abb8-cbd265d57527 | -12.4177 | -54.5797 | 2024-10-10 01:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 0264cf6a-1ee7-358b-a0c4-1646ba436ed4 | -12.418 | -54.5592 | 2024-10-10 01:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 8fc8690d-0f74-3ee2-adf8-08cfe07e9fc9 | -12.9447 | -51.1337 | 2024-10-10 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7a183c78-c8f2-32bf-ac19-eb8a7b7501af | -13.1845 | -51.7004 | 2024-10-10 01:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ac1a888f-132d-3bf8-9e8b-d9fe0c89f8b8 | -17.0549 | -45.2808 | 2024-10-10 01:36:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 564d298d-435e-3a5e-a5dc-3bda0532b496 | -3.8146 | -45.5143 | 2024-10-10 01:45:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 10a7ad0a-f7e8-30a7-9d59-342ddedda800 | -3.8147 | -45.4918 | 2024-10-10 01:45:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 18287578-b9da-3585-a299-42837e69054a | -4.0961 | -48.2739 | 2024-10-10 01:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 158.9 |
| f65994c4-adec-3dd2-9ce6-460a13c55ed2 | -4.0962 | -48.2523 | 2024-10-10 01:45:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 1feb1de0-d84d-3f7d-9bed-59885d254188 | -4.1146 | -48.2731 | 2024-10-10 01:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 179.7 |
| aed3d3d1-507c-38d4-9d8a-08d60b9c0ee1 | -4.1148 | -48.2515 | 2024-10-10 01:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 38698f80-cfdc-3757-8f0a-f7e1ed164a8f | -4.4776 | -46.5956 | 2024-10-10 01:45:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0db95c9a-da56-3dd8-9b69-00f2ca7a52dd | -5.9036 | -45.4127 | 2024-10-10 01:45:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 435cede9-a581-3940-8f78-739b39fb4b11 | -6.5218 | -60.0649 | 2024-10-10 01:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| b6606e1d-9c8c-386a-be76-9e6b23019ee2 | -6.747 | -59.3259 | 2024-10-10 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9db78eb4-34ed-3d1f-b494-db08bacf335a | -6.7654 | -59.3252 | 2024-10-10 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 95e8059d-a91c-3c98-8021-f94feab5f971 | -6.7655 | -59.3059 | 2024-10-10 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| f2ec11ec-98f2-3ab7-887c-d3eefbdddab4 | -6.7839 | -59.3245 | 2024-10-10 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |


[Clique aqui para ver as próximas entradas](README30.md)
