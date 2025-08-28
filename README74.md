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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29783bd8-f0a1-31ab-af33-df902a5772b7 | -8.90167 | -60.59671 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d312f99a-7ecd-3445-a3f3-df624a7ad62b | -9.16043 | -59.56038 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dd515b6-eb70-333c-acf5-ed7ad76d6e2b | -8.89614 | -62.47509 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cf2073f-ae62-39e2-8b0b-0151f3d1b7b7 | -10.25816 | -64.49799 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d851f371-aa57-35c9-a914-7fe2cc9e79a1 | -8.94692 | -65.96039 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2f65957-7ce9-3d18-8770-5118be901dc4 | -9.5498 | -65.6992 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e11b3e8-94d7-3f33-9297-1b10ab4693f3 | -7.49904 | -60.30724 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f365948-7974-3ce8-a69b-f5c9d0bc4d44 | -6.91377 | -62.94118 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 21e00dbf-315f-373a-a22f-4b71ba9e6158 | -9.4092 | -60.5039 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e09f3631-c0d3-3d21-98eb-a7f7cabc80b2 | -8.90631 | -62.47675 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a1dc524-dd25-3c51-850e-44a387016839 | -9.18018 | -59.45458 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d56cef3f-8669-33c2-bacd-ec89c8cd26a1 | -9.2538 | -65.89931 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61e1743d-3fc3-31c0-bd86-5bf6b47f1cdb | -9.08726 | -65.72925 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59c9ae5d-5f69-3c51-a350-dedb2a58ece1 | -8.34831 | -62.92812 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ce511b2-bec8-3e4b-a28f-be8896755f9b | -10.59229 | -54.89054 | 2025-08-28 05:25:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6659ae2a-e270-39c9-8947-00631767d3ad | -6.92713 | -62.94735 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc7afa11-1675-30aa-8b46-0ab0a3b6e76e | -7.55579 | -63.83995 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b69a417f-e8ac-3a50-a387-1647d73e4054 | -9.2851 | -68.25909 | 2025-08-28 05:25:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a39bd6bd-f985-3332-a37b-70e84839a432 | -8.96236 | -65.96667 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbb8c5b2-25bb-34bb-b32b-cd30688fdb7a | -9.46916 | -62.389 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 827313d2-91e5-36f5-98c0-cd45ebf81cb0 | -9.73187 | -64.9015 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e329802c-262b-35af-8e1d-47c6810d918b | -9.17793 | -59.49184 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ce11941-1e59-3419-8e8e-eccb2c37c1ab | -8.88582 | -60.76267 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| def6a9c2-8398-3cb3-86d1-c7b29a80a0d5 | -9.40367 | -60.51746 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80f6b93c-00a4-3e77-b5da-5be991f3737a | -9.13963 | -65.28817 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c89aa17f-6882-36ef-b5dc-b490ed6fa89c | -6.24897 | -60.01814 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98c8de91-b0e7-3e02-8d94-4cabe9231a59 | -9.54479 | -62.39717 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 010cd290-3991-3686-8957-d122aebbad18 | -9.41536 | -60.53013 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12cede53-efd9-3c1b-9eaf-6b003bdd57a6 | -8.35275 | -70.83959 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b09e89c-03c6-3a00-a9ff-45eb225881be | -10.94266 | -63.63285 | 2025-08-28 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fa82faa-805e-3e3a-b443-0c1a32dd1404 | -10.94089 | -63.63263 | 2025-08-28 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e43a9ef-44bc-37f4-9b1e-131624686026 | -9.20402 | -59.43567 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7b8f7d7-3212-3185-9746-40a7916f83a7 | -8.34702 | -62.94659 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd470656-b121-31ef-b4c5-7852d7e9b0fd | -9.13953 | -65.78018 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cc62cbe-4e12-31af-9183-91af0b9a4e54 | -12.80982 | -48.1366 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67779c5a-82c0-3e50-afd2-0c41075f8ee4 | -8.87972 | -60.75812 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d524802-0c30-31da-9fb1-af3b1b9df6d5 | -9.48997 | -62.38872 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95ecbd67-0b23-3e3e-bc95-f01972ae8a9d | -10.47709 | -57.93898 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ca5d20fc-a812-3eee-8e72-73fdc86a7eb2 | -12.81037 | -48.15847 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f035f5f-8b67-3a0b-b5dd-127be316e5a3 | -9.0851 | -65.71828 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1acc7804-db62-3fcd-aab2-f297fd273af5 | -9.80255 | -64.27485 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45d1f611-8029-3e9c-bee5-d0f53de49341 | -9.52718 | -60.53032 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3427524-d7cc-38f1-afbd-999df7c93809 | -9.17393 | -59.44985 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30c3088d-05d0-3894-b397-fe1a2bf99059 | -12.85565 | -48.11033 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8fe15bb9-58a8-3ccb-90a9-b2de35405e72 | -9.46446 | -60.30265 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aecb8fb3-ea8f-3a7f-a37f-b1e92a66269d | -10.08232 | -62.89613 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a4a872c-0ed5-3c81-8949-3535fdae7087 | -9.01337 | -65.69332 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 532b5c96-605c-3af2-831f-e1157f54c79e | -7.54212 | -63.85488 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75d76197-4f51-30b9-b9c4-59b17639c3ac | -10.25784 | -64.50047 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77230727-d056-3d9e-be92-0eeea42153c2 | -9.66366 | -64.98713 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1755d097-1715-376b-8929-061625054130 | -9.40591 | -60.52503 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9efc4a36-5276-34e8-9a2e-8930e193bfcb | -9.40641 | -60.49984 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5c50a3f-758c-3a3d-aa69-389690a7cbbf | -6.95042 | -60.0782 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eb30994-4ba0-3a10-abf8-fe6a4d59a390 | -9.18418 | -60.86391 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d98c78c-96c8-3a7d-b0f9-fd1187e425f9 | -6.2451 | -60.0211 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 074356c0-787d-353e-8dc6-672e6f51caf9 | -8.89834 | -60.59619 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e6623f-ab57-3fb2-8320-e69b3e0f3d10 | -9.14349 | -65.78085 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c74b37e6-45fc-3ad2-8847-62406739e23c | -9.20117 | -59.54422 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa2a75e4-3ba2-39ec-b507-4cdbc236eb76 | -9.39257 | -60.52291 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1185c334-9659-3414-bb14-3a0268c08cd9 | -10.35536 | -64.47379 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6cf7f06-b840-3e66-a13d-12bc87729c04 | -10.81832 | -60.77337 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73a740ef-3491-3a3b-95f4-a1ab724b45aa | -8.93332 | -65.94361 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7b6aaff-ceeb-3afe-94b8-cf66b193b88b | -8.34587 | -62.94328 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21058e32-da54-3901-9ed2-017793e94875 | -8.88027 | -60.75462 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3149f141-efe7-30bb-8efc-812e6b33290b | -9.17687 | -59.61145 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0ca5194-6145-35c6-ac74-76ce1b57c490 | -5.29761 | -60.19843 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ceb224b7-6a42-30b6-80fd-590600d865dc | -6.24564 | -60.01762 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cbe45fc-c053-3c8d-b484-0d39a608504a | -8.65564 | -67.26624 | 2025-08-28 05:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0463b489-372d-3328-9b59-d059370b4078 | -8.09847 | -71.25329 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8757c700-7b03-3763-835d-a23acf5ecd7f | -8.34544 | -62.93465 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9c94a04-3cfa-3a28-a275-1f6501214dbc | -10.28101 | -64.4957 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a9ff67d6-c689-3962-813b-24abaf0f3ad2 | -8.09347 | -71.2481 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e1cf1f9-5c90-3660-ba61-7632583f2d31 | -7.5432 | -63.84743 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b878ebd-5417-35bf-96e2-811de4bf1bf4 | -10.93855 | -63.63613 | 2025-08-28 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c47b74dc-1e18-3980-b698-76f136862d96 | -9.21299 | -60.85416 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bd07bc6-5f79-3012-9892-901b986ea643 | -11.57283 | -47.61748 | 2025-08-28 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67854630-b99e-354e-8402-f47628b7a0fa | -12.80403 | -48.15073 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d54c4d0-f470-3c00-b13c-4540ee6f6d88 | -12.86452 | -48.1232 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f8436567-f323-32bc-aa0b-07a7de202927 | -10.79439 | -60.77319 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| cf0559bb-ffcd-351f-aef8-fd5feddfb577 | -10.80272 | -60.76362 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 01c78a4a-d70d-3543-af6e-278f0d451ce7 | -9.14046 | -65.28341 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5878bb8b-e7dd-3bb7-a6d8-6da06745e438 | -8.9069 | -62.4731 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20e2d6e2-b0f6-37b9-a95a-3fe932546623 | -9.49055 | -62.38511 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9196d585-ea5f-34ef-baeb-f5e3eeac2650 | -9.4032 | -60.56428 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09334936-dc3f-30ec-93b0-29edae607ad6 | -10.1579 | -64.24632 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6036525-3a41-3850-a0cb-0761a884e962 | -8.89889 | -60.59268 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b0bea6d-2531-35dc-bc52-83cbc9a740dd | -9.00421 | -65.72307 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b1357f6-8010-34e2-8096-42c6eaffd16b | -9.14885 | -62.35921 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76416984-f923-3aea-85bf-5bcf6bfeb83a | -10.46351 | -57.9548 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e77bda15-6773-3684-85d7-3876b3d58091 | -8.24225 | -61.45129 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37c9e07c-1f2a-3380-aac6-37c11c7084cd | -8.10001 | -71.24512 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5e7156b-8376-38f9-a552-74965ed6d990 | -8.89938 | -60.54607 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94b0e55a-b843-30b3-8e8b-524e7d3ca53e | -6.24008 | -60.00962 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 256c5220-be5b-36ed-8138-8fddcee64c6a | -13.72953 | -51.91665 | 2025-08-28 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a46df6b-3ae7-34e3-b137-f9f40b97e81e | -8.85375 | -62.41264 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32445b1a-901e-308d-9ab4-4355a774068a | -8.92692 | -65.9285 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52e42ee1-ac48-3002-9bec-51d52db8d126 | -13.10174 | -57.12604 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c367d244-3a57-3b58-9ad6-b1a74bcac77d | -7.4407 | -60.03329 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1249eaaf-f616-386d-814b-66019ab688be | -12.80779 | -48.15658 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e92ec9f-3dec-389e-81c8-831b59568dbd | -10.81553 | -60.76929 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README75.md)
