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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af85caa3-b2a1-3ef5-b7fb-9904921e7eda | -11.41896 | -47.4923 | 2026-07-25 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48a0d94c-f7cd-36b5-bcb7-4fdc75b23b50 | -9.17543 | -58.31873 | 2026-07-25 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f398bb43-8711-3d57-b1ea-e009d2d969be | -13.30061 | -54.33351 | 2026-07-25 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3427d19d-976d-3ed5-a589-a0e316c24fce | -12.34449 | -48.21976 | 2026-07-25 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2196e8a-2153-34fb-b141-128a779b189f | -12.01734 | -50.48874 | 2026-07-25 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d6c21df-9f3a-3b2a-8851-f5aba79deefd | -12.02655 | -50.49019 | 2026-07-25 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb0128bb-432e-3610-b1f4-b5c5d2ab9b87 | -11.41102 | -57.80913 | 2026-07-25 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11924794-c6a2-3504-bb0a-84a670b8eb03 | -12.338 | -48.2188 | 2026-07-25 05:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a864c14-0693-3356-a4c4-ded428776120 | -12.02296 | -50.48948 | 2026-07-25 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b6381e09-e12f-3c36-a0c6-f495fabda92c | -12.05935 | -58.04492 | 2026-07-25 05:29:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbf84346-7d3f-3be5-9166-529ca73efa12 | -10.02175 | -65.05447 | 2026-07-25 05:29:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cae544c7-64d6-3b7a-ad64-9a866e57fee4 | -11.74589 | -57.80925 | 2026-07-25 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa3549f5-8065-36b0-b039-f5afa3fa0f37 | -13.78248 | -47.13147 | 2026-07-25 05:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08f76d29-33d6-3990-bfbd-68907bc9d08e | -11.41453 | -57.80968 | 2026-07-25 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 052056bf-d0f6-31ff-918a-52f04b26d26d | -13.30502 | -54.33413 | 2026-07-25 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2600518-8807-3870-8d79-b5419147a4e8 | -13.30883 | -54.33924 | 2026-07-25 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcef0502-5ddd-31f6-8fe9-ebddb8233773 | -13.78875 | -47.13947 | 2026-07-25 05:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c830128-dc07-369d-8b7c-76eff5b16123 | -10.01773 | -65.05372 | 2026-07-25 05:29:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 181339b8-d476-375c-a458-f12e56463059 | -12.00671 | -49.26799 | 2026-07-25 05:29:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d28e87b3-d030-3aef-bfa7-aefcf387ebe5 | -9.9619 | -64.96753 | 2026-07-25 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c788b67c-fe4c-3a3a-9adf-bdded141e472 | -13.39961 | -48.16801 | 2026-07-25 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6468be98-c5aa-3186-ad5f-55e89b058ba2 | -12.43982 | -50.40922 | 2026-07-25 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5379c70-597a-3eab-93a0-3c728c6fd5fa | -13.31002 | -54.33035 | 2026-07-25 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f5e9270-8472-3060-a090-643064531e31 | -9.67391 | -65.63223 | 2026-07-25 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4574ee12-1a75-3c1b-9fab-466d5a2ecac0 | -13.40622 | -48.16887 | 2026-07-25 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b776ecb0-91bd-37d3-b2ce-9adfe220f577 | -11.35767 | -55.43452 | 2026-07-25 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 442f7cc3-7275-3db0-a4fa-4408ab6bbdb7 | -13.30443 | -54.33859 | 2026-07-25 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58656df4-8143-376c-b9dd-6db729541d7f | -12.43414 | -50.40849 | 2026-07-25 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67c3e1d9-37dc-3e34-9034-a362983ec8a2 | -10.02237 | -65.05093 | 2026-07-25 05:29:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d3d0c6f-4b58-3a6e-8bb7-72c0f81d2c96 | -14.1731 | -51.89875 | 2026-07-25 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83c7f25e-d250-326d-8ebb-55ff152738be | -14.17876 | -51.89619 | 2026-07-25 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6668a595-d78e-36d4-a6ca-9ef60e95d594 | -14.17797 | -51.90269 | 2026-07-25 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 699812d1-0a18-3a64-afb0-6382bad6d036 | -14.17837 | -51.89944 | 2026-07-25 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2563aec0-b011-3315-aac9-5a4d61d6d8df | -18.81087 | -53.14611 | 2026-07-25 05:31:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59e72b1a-82e2-3e9a-bd2e-000937548f71 | -18.80572 | -53.14545 | 2026-07-25 05:31:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49cdd5f9-92d0-3560-a155-e67f723b7a34 | 2.9487 | -60.18247 | 2026-07-25 05:44:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0fefe02-b6d3-3fd2-98e7-118f3ee1c2d1 | 1.65792 | -60.71553 | 2026-07-25 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96ae5c8e-8f85-331e-8874-2194fdac784f | -3.79987 | -51.18322 | 2026-07-25 05:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82a3afd0-3ba8-3d3f-8bec-e0bf089139f0 | -2.7158 | -59.76842 | 2026-07-25 05:46:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 230d4034-f490-3f46-9ec7-023ac497302d | -2.39281 | -59.99309 | 2026-07-25 05:46:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 417705a9-8c74-33b3-bc01-2a93a3487232 | -3.79895 | -51.18954 | 2026-07-25 05:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f941088-108e-383f-aca5-1412c2a72bbe | -1.78373 | -55.52794 | 2026-07-25 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d5b8403-3bd9-3034-9671-7c92531f038a | -7.16472 | -59.32124 | 2026-07-25 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e412591-2537-397b-a151-1310df0541eb | -9.16046 | -58.3237 | 2026-07-25 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7f86193-a5c2-3130-92b4-b77e105bdc35 | -9.16138 | -58.32772 | 2026-07-25 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89e89661-3541-377b-acf2-b2955ae95fb3 | -8.89494 | -60.6012 | 2026-07-25 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3568fae7-9dad-3422-bf80-0fc217b050e0 | -8.89439 | -60.60497 | 2026-07-25 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3f1999c-e82e-3aef-ab1e-0e362cc4c27c | -9.16696 | -58.32317 | 2026-07-25 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fc27673-fa1c-3519-b3ea-3a3bbbf2184c | -9.18979 | -58.06506 | 2026-07-25 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dee8599c-d6e1-3144-8de5-a5677df201d1 | -9.1653 | -58.32444 | 2026-07-25 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f6a5f7f-d042-3a37-9df3-fece309fe585 | -9.16213 | -58.32243 | 2026-07-25 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ceec6f4-22cc-3cf1-8ecd-9cc4faa12967 | -9.1757 | -58.32055 | 2026-07-25 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1d0a5a5-b6af-3300-b24c-8188c2833390 | -9.08581 | -59.48294 | 2026-07-25 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ce585ca-92df-3118-a954-64f3a26a1b29 | -7.16535 | -59.31696 | 2026-07-25 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed51f192-3dc3-3784-b9f5-20c79a32a172 | -9.00993 | -64.13286 | 2026-07-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 02321df5-f1ab-339c-ba0c-f0423f6a3651 | -9.9612 | -64.96407 | 2026-07-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce11b3f7-2f0f-3270-9984-eb81c56323f7 | -10.01887 | -65.05002 | 2026-07-25 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f203b506-f6f9-3652-a11d-cc4f5faa6cd1 | -9.67106 | -65.63073 | 2026-07-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2db05f8-c81b-3675-be97-fa9c9c2aa658 | -10.05759 | -60.49703 | 2026-07-25 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d9ef1a-6646-3b1f-bcd8-8214a9dfc559 | -9.96456 | -64.96459 | 2026-07-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40cbd53b-20fa-333a-8933-6f9f1ca8ce2e | -8.66686 | -66.56647 | 2026-07-25 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b1594f8-2dea-315e-8c62-d2c4961dcdb1 | -10.54652 | -68.56836 | 2026-07-25 05:48:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a61225dc-62a2-3c19-9205-5fd392cd5cb7 | -11.3582 | -55.43415 | 2026-07-25 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa42e7cf-f2de-31bd-9cef-8d7dc32b7eee | -9.00937 | -64.13657 | 2026-07-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ea6fa805-a063-302d-8778-d7528ce3ab39 | -9.96065 | -64.96767 | 2026-07-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9a0fa33-38de-32c2-a87b-08a1ae02cd68 | -11.40907 | -57.81108 | 2026-07-25 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c485e77-7e86-3832-b191-647839b56696 | -11.41424 | -57.81182 | 2026-07-25 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c55a166-c8bb-3dc4-b9c9-2313a320819f | -8.86648 | -63.67277 | 2026-07-25 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c7cf9fc-1025-3de0-bdca-2c5984a8980b | -11.35764 | -55.43861 | 2026-07-25 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad5bbd00-a680-3b13-b2df-1515fd7587c0 | -10.02223 | -65.05054 | 2026-07-25 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6548f945-6430-3b55-ad81-be65321b8067 | -10.01832 | -65.05362 | 2026-07-25 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26593c65-bb19-38a0-b81e-ce95848bad98 | -9.67438 | -65.63126 | 2026-07-25 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9f2b243-2fa8-3a14-90f3-e9f22babe603 | -21.27962 | -56.03289 | 2026-07-25 05:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7706908a-01e7-30ca-bcae-bafca7188fb2 | -21.27917 | -56.03865 | 2026-07-25 05:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed78261e-50fd-35cd-b032-d156b2c035ec | -4.26 | -38.03026 | 2026-07-25 06:16:00 | AQUA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 32.1 |
| d12b8e06-5bc2-3a5e-9771-3321496ba976 | -4.37013 | -47.76625 | 2026-07-25 06:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4dbd3d48-d976-316c-9e24-93a2abd27756 | -4.36549 | -47.76003 | 2026-07-25 06:18:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 9fb715fc-df6d-3080-8910-2a8fa4fb0579 | -11.80492 | -47.09119 | 2026-07-25 06:20:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| cd98571e-d7ef-3b31-b428-6e3c49bfd638 | -11.79482 | -47.08945 | 2026-07-25 06:20:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| c6d1e508-46eb-360b-9dae-667a5797f04c | -11.42257 | -47.4909 | 2026-07-25 06:20:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dd9f9a7a-462b-340a-87fa-31353d27af33 | -15.58262 | -46.81696 | 2026-07-25 06:22:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 379a7b8b-cf26-3842-be43-98f834bd314d | -8.85754 | -44.15927 | 2026-07-25 11:02:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| f22d164e-b79e-3f08-af85-9e5776621355 | -11.807 | -47.0858 | 2026-07-25 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 4885c64e-4c74-32cb-ba09-a16ae9076b6b | -11.807 | -47.0858 | 2026-07-25 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 925e605f-7b55-3b0e-81e6-9e28bcf06026 | -11.807 | -47.0858 | 2026-07-25 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 43870846-fffe-304f-8ec7-945c07fdd8bd | -11.807 | -47.0858 | 2026-07-25 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 0d521e1c-fd92-3205-a62b-db3682aa4696 | -11.7879 | -47.0884 | 2026-07-25 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 4ab86249-b11f-343b-927a-91b2a062e7fd | -10.6755 | -46.3574 | 2026-07-25 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2db0ce62-9384-3b3c-b9e3-061d18c7bf32 | -11.807 | -47.0858 | 2026-07-25 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| dde44542-1958-3d8c-b571-31baa2c892c5 | -8.7296 | -54.5442 | 2026-07-25 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 7192cfdc-0c63-3cae-b723-9ecd12dab5a1 | -11.807 | -47.0858 | 2026-07-25 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b0d08b42-4590-3cfd-8555-637291fccab5 | -9.5274 | -47.141 | 2026-07-25 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ea640825-833a-31ba-a6b2-8ebd0d020301 | -9.5277 | -47.1187 | 2026-07-25 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0aa03258-088a-3701-b830-4edab361cea8 | -9.5274 | -47.141 | 2026-07-25 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 67c5d3a3-25f6-3c23-b198-fc66c106eed7 | -7.62791 | -49.79258 | 2026-07-25 12:40:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| f337cf8c-4f33-362a-a528-cbe524c58756 | -6.92929 | -51.91853 | 2026-07-25 12:40:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 25710a77-52f0-3aa9-b8a6-29ea2c424922 | -7.63269 | -49.7527 | 2026-07-25 12:40:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| fe7f2c2b-2f57-3b2e-abdd-bb4cb062d8e1 | -6.94137 | -51.91346 | 2026-07-25 12:40:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 8d6a1c23-5e18-3b3a-9914-cfc8536b14da | -7.63528 | -49.75798 | 2026-07-25 12:40:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 362ba244-3d6d-34c7-9f89-8c9c793154fd | -7.71092 | -55.38699 | 2026-07-25 12:40:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README9.md)
