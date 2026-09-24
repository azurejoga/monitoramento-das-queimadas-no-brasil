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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9c8e5de-168c-3fb3-b06b-fbae70ddefe9 | -11.2113 | -54.1208 | 2026-09-24 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1b77aa0a-7950-30e6-a185-3732a0a3e2d9 | -2.8608 | -57.7994 | 2026-09-24 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b8c61ffc-dfef-361b-9269-ca5bf2d48876 | -11.7357 | -54.5227 | 2026-09-24 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d1b063fc-011f-3bd3-8acd-d086a550911c | -1.8402 | -55.7034 | 2026-09-24 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 90d78f6c-73dc-3958-af51-e82a8e53ef72 | -12.8246 | -54.0442 | 2026-09-24 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| fc9d0577-c07a-31b3-bd23-92b8fd557d44 | -11.2113 | -54.1208 | 2026-09-24 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 215a6a3a-3abd-3f1d-bdff-e5d5b63fbf4a | -12.7865 | -54.0482 | 2026-09-24 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 720004f1-ce57-3e60-b722-e20ffb29ec30 | -3.4975 | -59.1752 | 2026-09-24 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 8bffc05f-c6c4-3ce2-9d10-835f91c12dbb | -7.952 | -72.9322 | 2026-09-24 15:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e53823c2-feaa-3481-ac80-9dd373007c26 | -12.8056 | -54.0462 | 2026-09-24 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 13a96021-91a6-35a3-a8ad-c216d9a6272e | -5.9818 | -57.7087 | 2026-09-24 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 9bcbc9e8-4505-3c35-8526-3f88076f5a5c | 2.145 | -50.8784 | 2026-09-24 15:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 14249504-b9a8-321a-9d0a-af98d036c4ed | -14.0425 | -52.06 | 2026-09-24 15:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 24e4c1d3-db72-335a-8e06-daa72309250f | -5.6567 | -60.2092 | 2026-09-24 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.9 |
| c3f33b5f-036b-3884-b2ee-1eb7191a8f57 | -8.7687 | -61.3879 | 2026-09-24 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| cdca475f-de7f-3e32-b2f1-1702e5a1b894 | -1.8218 | -55.7037 | 2026-09-24 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a3eca48d-c05e-353c-bf8c-d2b85ccaa683 | -9.0646 | -58.9443 | 2026-09-24 15:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f58e2cbc-7e46-381f-9909-b3928cd87946 | -9.1392 | -58.9207 | 2026-09-24 15:30:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 5acaddfc-7bff-3055-85e9-b75612fdd408 | -6.0368 | -57.765 | 2026-09-24 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 38ca768b-9fad-3824-a2ac-0642c72fe946 | -2.7713 | -57.0229 | 2026-09-24 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 43b492b0-b521-3542-b879-19ca76ccaff8 | -6.5444 | -44.9327 | 2026-09-24 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 3432a29b-e58e-3565-b357-73b161bc367e | -10.29 | -59.6515 | 2026-09-24 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2bd34365-face-3905-8266-0bd566903dd0 | -13.3943 | -57.0645 | 2026-09-24 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| f7315860-8905-3976-a1b4-758a150579db | -7.1392 | -42.0811 | 2026-09-24 15:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| f4567de4-4e3b-3767-8b4a-a401947b29b2 | -1.8402 | -55.7034 | 2026-09-24 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 7dcaa9f4-af04-31c7-8235-eb48b10b1661 | -5.9819 | -57.6892 | 2026-09-24 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f4f857e7-8516-3992-87e1-750abf4d9ad3 | -11.7351 | -54.5636 | 2026-09-24 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 8cae98c1-b079-35b6-9580-cc979a84d57c | -6.0994 | -59.8884 | 2026-09-24 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b24e9348-d665-3c5e-9606-ca09b02742f9 | 1.4452 | -50.8071 | 2026-09-24 15:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 65.7 |
| f0cb7876-eaa9-38c7-a98f-dd8a17b51d26 | -9.1163 | -59.4854 | 2026-09-24 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| bb5cea4f-e50f-306a-8646-766eacb86f37 | -14.08 | -52.1188 | 2026-09-24 15:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5b05dbd7-a9f5-359e-8035-8dc9c2d68396 | -13.2037 | -51.698 | 2026-09-24 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b67101e7-1e8b-3647-b362-4809a8274a32 | -13.3632 | -51.3163 | 2026-09-24 15:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e7ea9ded-9fa7-330b-9126-062553b9886c | -11.7159 | -54.5858 | 2026-09-24 15:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 57fa55b8-9a23-34fe-a5f0-730d3270c30e | -11.2113 | -54.1208 | 2026-09-24 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0db56a3e-4858-309b-b8e9-b353d3737513 | -1.3926 | -49.3152 | 2026-09-24 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7b28d015-a2fa-3380-8bf5-b18746926b4c | -12.8246 | -54.0442 | 2026-09-24 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7b7da816-dc01-3604-bb88-b472faa8b6e5 | -14.08 | -52.1188 | 2026-09-24 15:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 37ea6605-3743-3dbf-a306-7d9634a90df4 | -3.4974 | -59.1944 | 2026-09-24 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 3d4fd968-7f1e-3e9a-8e6c-0d3382311a1a | -2.7713 | -57.0229 | 2026-09-24 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| fda955f3-0194-3eec-a3cb-03135d873204 | -1.3742 | -49.3154 | 2026-09-24 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5e9556ce-d5a8-3ea4-894d-2a7c4056b490 | -8.6757 | -69.9611 | 2026-09-24 15:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 35a18c4a-0ce0-34e4-b8db-7a36331b3e34 | -13.3443 | -51.2973 | 2026-09-24 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c3dbaad7-334f-3dbc-a179-e0cd58550703 | -9.0646 | -58.9443 | 2026-09-24 15:40:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 57a080cf-4752-3780-ba4b-bff1695eb0f8 | -3.4278 | -58.0009 | 2026-09-24 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 46f6efd1-6134-3d19-bbe0-e44b1c6735b9 | -12.7865 | -54.0482 | 2026-09-24 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f3458739-ba6b-38d3-942c-96f2c43b7625 | -13.3251 | -51.2997 | 2026-09-24 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| d41eaed6-44fd-3508-8850-f0789ec0fdb9 | -13.4327 | -51.7547 | 2026-09-24 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| b043144d-83af-3112-92c3-fafc5b12b7cd | -6.2026 | -47.5026 | 2026-09-24 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 15034fd1-e0d2-32e2-9c0c-231c84b7177a | -9.1392 | -58.9207 | 2026-09-24 15:40:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b95129ea-a798-32e1-8ce6-d4b8ed40ce47 | -1.289 | -57.0436 | 2026-09-24 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 36104070-465f-36bc-b169-0f16b8dd8fb0 | -12.8056 | -54.0462 | 2026-09-24 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f72f383e-880e-3270-a985-c402c507cae9 | -12.8994 | -52.8301 | 2026-09-24 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b553cacc-e37d-3bdd-bdfc-5a8dfd8a1eae | -11.2118 | -54.0797 | 2026-09-24 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| eecd11ee-5336-372e-8bc0-1609aae08ad0 | -12.8246 | -54.0442 | 2026-09-24 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f30e3b65-53a9-3f2c-9e3d-01f96d252edc | -9.1392 | -58.9207 | 2026-09-24 15:50:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3cc23867-18cc-31cb-9fdd-c3db7d2ed74e | -14.4455 | -52.1563 | 2026-09-24 15:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a2647d6a-9ab7-390c-8da6-7f64405fe1c7 | -10.5906 | -57.4936 | 2026-09-24 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2ba0d05d-0adb-3a10-aa23-256f10278043 | -9.2086 | -59.5773 | 2026-09-24 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6acb34aa-7f56-3a7f-b91a-449f757d61a6 | -13.205 | -51.6129 | 2026-09-24 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 4ebab9aa-28ec-34fe-bafa-b6b3eac5ff1a | -11.2299 | -54.1396 | 2026-09-24 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 77eef06d-f649-3abe-b0cc-5bf6e8e0f9fc | 2.145 | -50.8784 | 2026-09-24 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.8 |
| f50426f0-debc-3d94-999c-e44dda8bb000 | -11.2113 | -54.1208 | 2026-09-24 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 15f6ef90-630b-3d8d-a339-7123f31efe51 | -14.08 | -52.1188 | 2026-09-24 15:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3bb9fb67-9884-3675-a95a-6a8779fadbf7 | -13.2979 | -51.7926 | 2026-09-24 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 1f137780-b177-3417-a766-6e45ba59902a | -12.8056 | -54.0462 | 2026-09-24 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a5adcb63-5ea9-3600-8ab1-990269c08c9e | -13.2249 | -51.5679 | 2026-09-24 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| de47ccdf-3a34-36b9-ac92-ec01d0a4f46a | -12.7865 | -54.0482 | 2026-09-24 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e424518d-4459-33a8-82fb-5e46b4969ceb | -13.2054 | -51.5916 | 2026-09-24 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| fa5febdd-76bb-374c-9269-d883e4201f1c | -8.8942 | -71.517 | 2026-09-24 15:50:00 | GOES-19 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 84e9527f-26ec-3e22-9c60-df23db8baaea | -13.2057 | -51.5703 | 2026-09-24 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 7f56ecac-3a60-37cc-b47b-585e3a3bf9b0 | 1.9976 | -50.8813 | 2026-09-24 16:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 450cd06e-da20-3856-afda-bcc3703f2b93 | -6.5444 | -44.9327 | 2026-09-24 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bcd39163-bea7-380d-952f-25694c9ada9a | -6.2024 | -47.5245 | 2026-09-24 16:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 12f1f11d-ceb7-32a3-8002-9fd0ca5458ac | -12.8056 | -54.0462 | 2026-09-24 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2c67c537-117c-34e2-a092-585a4f68b8c9 | -9.1813 | -60.7747 | 2026-09-24 16:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 03840bfb-0a74-3774-ad10-7c452f537494 | -1.2455 | -49.0407 | 2026-09-24 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a322aa12-7705-39b7-bbd3-0940f8292187 | -12.8246 | -54.0442 | 2026-09-24 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3bef8c6a-0525-3935-bd30-4efff901a75a | -11.7357 | -54.5227 | 2026-09-24 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1d0717b6-2eb9-3dcf-9489-cf0640e5bb6a | -14.08 | -52.1188 | 2026-09-24 16:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| dc765758-19a4-3ae1-84da-39abf6d986f2 | -13.2054 | -51.5916 | 2026-09-24 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 08521f60-9ec4-3992-b241-5b716e3e06b4 | -12.7865 | -54.0482 | 2026-09-24 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2e23521e-fad9-3c5a-866b-f7a72d6bae48 | -13.2057 | -51.5703 | 2026-09-24 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| c9ca9f78-c100-30f8-b4ae-57fa83b703ea | -11.7357 | -54.5227 | 2026-09-24 16:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 7bf94a0c-e482-33cb-8306-aae1c5c0b0f9 | -13.2054 | -51.5916 | 2026-09-24 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 44974328-46a1-3155-8b50-1c1e9e01e6e3 | -7.1392 | -42.0811 | 2026-09-24 16:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 7b21984b-146c-3b45-acca-69fe76792aa0 | -14.3882 | -52.1213 | 2026-09-24 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8ffb264c-1280-37ef-9d2f-e955ae48d251 | -11.2488 | -54.1378 | 2026-09-24 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 022905b3-e725-3e44-9c08-9718ad841a46 | -14.79 | -45.62 | 2026-09-24 16:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b8c3100-e381-3853-9d41-b8315b9a5ce5 | -14.75 | -45.61 | 2026-09-24 16:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be1a02ea-9785-3f47-b2b9-240ea62d4c21 | -4.37 | -55.55 | 2026-09-24 16:15:00 | MSG-03 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f0b142c-2aec-3eb7-9629-d9ae4990d954 | -7.89 | -54.79 | 2026-09-24 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bc0819c-a682-3eb6-b42e-1c88e2cc3453 | -7.89 | -54.73 | 2026-09-24 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db2290b0-40f3-369f-92de-ecfb70a34b08 | -9.64 | -43.9 | 2026-09-24 16:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 603ed12b-fa79-336c-bf67-faab6b772caf | -7.92 | -54.8 | 2026-09-24 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9dff67-96df-3c9a-b6e5-69def26a69cd | -9.64 | -43.95 | 2026-09-24 16:15:00 | MSG-03 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3f3b2aca-c06b-3db3-a0c0-f8c7b8da8c9f | -4.4 | -55.55 | 2026-09-24 16:15:00 | MSG-03 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72379c17-4bf6-3077-9f65-d8a211f1b059 | -14.76 | -45.66 | 2026-09-24 16:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1804e6c3-8c88-3c7a-b66e-9f7a387509ac | -7.92 | -54.74 | 2026-09-24 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1174e7b6-c651-34a1-ade2-607035fe9e64 | -4.4 | -55.49 | 2026-09-24 16:15:00 | MSG-03 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README99.md)
