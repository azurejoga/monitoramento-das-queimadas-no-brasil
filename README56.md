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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d486239c-9676-3687-8aa1-aa5e33431ed2 | -9.40456 | -60.50194 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bc24c39-5636-3e8b-818d-f2b9d029107c | -8.34437 | -62.93363 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83463401-e03f-32fa-844a-05f508b79a75 | -9.25542 | -65.90405 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0f962c41-5d62-3a08-a4b1-d9c9db7ad2d2 | -8.24856 | -61.46832 | 2025-08-28 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1349c3d2-6e36-3837-b049-af5acbcf141a | -9.78969 | -64.24493 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fee8d7eb-b20e-3e4d-9c79-316e55f36b10 | -11.34278 | -43.53117 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e6539e86-488e-35cc-ab3d-c612e161f52e | -14.26461 | -53.06335 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b498bb03-700d-32ae-9ebf-f9df0b3fc98f | -14.30992 | -60.38564 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba7ff61f-d4c9-37ed-9aeb-21780a009fd1 | -13.17527 | -45.27939 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74f9f8e9-fdb9-3462-a94c-bf1229bc0672 | -10.88761 | -55.77754 | 2025-08-28 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2663f3d-b382-314a-b51d-a85501bbf23c | -8.87755 | -60.75299 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c4a4fb9-da7a-3dc4-97a6-a54f1f16373f | -8.94029 | -64.15636 | 2025-08-28 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 716c596e-d221-32b1-a48e-fd81e33325cd | -13.01331 | -56.89771 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fe384c6-6dd4-3fa8-980a-ee6503e6543f | -14.29486 | -53.04461 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| dd62188d-5ef8-3dc8-a268-53d2929d212a | -12.67453 | -48.18388 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f24e955f-f2dc-39d8-b8ba-74a249eb6c61 | -9.60716 | -55.37695 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3aaba6a-be84-3b54-bbb3-102baa24784c | -8.88668 | -60.75045 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fca00259-1102-37b1-abc6-d1f639ebdd68 | -10.46906 | -57.9465 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1db0acd-b6ad-31cd-bda9-15e0a13340ff | -13.51636 | -46.87561 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba46b5ba-0be8-39b6-add3-6acd3cee8b7a | -13.52128 | -46.87921 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 053679c9-577b-31ae-a37a-281070d2211d | -11.64802 | -46.38749 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4988d903-30ac-3c62-8d6c-9eb72948137e | -9.24338 | -59.78431 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49e873bf-cd93-3784-b8a4-3daf7dffec8e | -13.49242 | -46.85144 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4bc9827-91d0-3e08-9a74-dfbf5d79249d | -11.2219 | -55.05334 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0ee945d-e1d3-3fa6-9de9-1f22e02b751e | -9.40933 | -60.49891 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5d9c55b-8ea1-385d-8ae0-d58f86e7c97f | -13.55494 | -46.91067 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58b2165f-7189-3265-a922-b4d7129217f2 | -9.40277 | -60.53641 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1dbcc4c-c881-33a4-a109-657e8ab7a1d0 | -10.5312 | -46.68358 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eddb53e-a750-3bf8-b951-c8f3a1d66e86 | -15.63325 | -52.75847 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfdde88c-6d38-37b8-aab8-2cac93a1f221 | -13.51708 | -46.86949 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79c48cfa-cbf5-36da-a715-385bacc0b57b | -14.3451 | -53.35349 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6da387ea-3596-3ff8-943d-b6c6bba05a60 | -11.57897 | -44.65393 | 2025-08-28 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d9c1f24-28c3-3516-9f3c-4450ec9e4424 | -14.36137 | -53.21244 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4488f5d8-575a-3a15-be19-f02364ea9c79 | -9.41274 | -60.57691 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bd1b3d5-c036-3ce7-8fa6-8e23dbcdbb68 | -10.27997 | -64.49301 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a742d38-f978-31df-9c65-e0ccc2d01a45 | -10.54459 | -46.70124 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 89e4674a-fb73-3fd1-9407-4c1c91b23fcb | -14.3675 | -53.3488 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5806c491-76eb-362e-ba39-1fd54e32afdd | -8.95832 | -65.96095 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb378735-4206-3b8e-b7cd-f1994c002b18 | -8.26199 | -61.45926 | 2025-08-28 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7f4f731-2a04-3c0c-b300-f07b3ce262fa | -15.62954 | -52.75793 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 634ab364-3a05-38b3-bea7-422f994a32d3 | -10.32329 | -62.61922 | 2025-08-28 04:59:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9b308a3f-0097-3a57-acb2-3c0e47edb5af | -13.01159 | -56.90847 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7e282da-e051-34fd-b379-92a75a2be46b | -9.25699 | -65.89563 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cc4bc16d-58d9-3cf2-b791-9718420261b6 | -10.49761 | -51.58752 | 2025-08-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1e8481b-cf07-394c-81b0-823cf139a9dd | -12.89538 | -48.09983 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6d30b1b-27ad-3dab-9452-e7b20cb824f2 | -9.8114 | -63.0792 | 2025-08-28 04:59:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cce8bea6-6b91-30d2-87a0-6e4bb0ead2e8 | -10.32496 | -46.78383 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0130b09b-f1ce-328e-ae23-d12495581f23 | -12.79427 | -48.16571 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e71c6a0-813d-3759-a0d9-8818514065f6 | -9.2202 | -60.80717 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc6a78be-6696-3d6b-be38-433c2aa0902a | -13.36452 | -51.78684 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 705f4a7b-a7e7-3727-90cf-be2559706d9c | -9.4086 | -60.5762 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56557254-d49f-3f6a-bb98-fca6b3809878 | -8.95914 | -65.95646 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c7e1e5b-3aa5-3582-ae02-0b888187d1a0 | -12.77913 | -48.16877 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35e7b89f-d4ce-3654-aa2e-f12fd58247db | -9.19497 | -60.80254 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 044c81d7-0f5c-3979-b5e3-c0352cf2df4f | -13.98877 | -46.33846 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8dbcde75-5b58-3e19-a75c-8557088f4efd | -9.16601 | -60.76939 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f70761b-7e8a-3f1d-b09c-a90ba3fd7b72 | -14.12062 | -53.972 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4f652c7-2a78-3a5f-828e-fa40b84fe24b | -8.8959 | -60.59525 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62bec639-7fc8-3513-a4a9-db025ae468ef | -12.99548 | -56.90215 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 093d66a4-6947-3011-bc3a-dd91a2620fa9 | -13.48205 | -46.85162 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4fe7587-944c-3e92-bc61-0cd0b111a50f | -13.52036 | -46.93176 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11b0cdb0-2f59-3f40-b7cb-0c12e32a993e | -13.67044 | -46.88249 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb541249-bfbc-3572-8979-66285f2af2d4 | -12.6803 | -48.18171 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5fd80fb-1009-3b33-a6f4-3434ad9c278c | -8.95321 | -65.95527 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1202448-339a-370f-ba91-d4ff8d495849 | -10.24699 | -59.66593 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10459e8b-5a55-3d88-8537-acb8e21c65eb | -9.48504 | -62.38329 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58569018-2a60-378e-bd58-2e0bee91a428 | -10.15221 | -64.2475 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22512dbe-8f97-391d-bf4b-b1f2b4508e02 | -9.18939 | -60.80972 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2326494a-a2b1-37b1-9b00-068e14ee4188 | -13.36072 | -51.78626 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 841173c7-c8b6-380b-9919-4eda7b6eecf2 | -9.25621 | -65.89983 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a9cc6c0-19e2-3d0e-baec-6e417de593dc | -14.27117 | -53.06873 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 4a2c5104-0535-3db4-981c-240f7c5e3f4d | -9.26885 | -59.77758 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0563db8d-9a8b-3b1c-805e-cd2138a5d95c | -15.30393 | -52.82181 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f13e6f65-acd7-3155-9374-8c5f9b58e7a5 | -8.88464 | -60.7624 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd2f20c6-c7bd-30a3-9070-56c4b32f1bc0 | -12.89268 | -48.12054 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e1374715-0181-3ffc-8ea3-904b51638a5c | -12.68132 | -48.16913 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f39d08ac-b87a-3f6b-95b5-2bb8d5aa36f3 | -13.43646 | -46.96201 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63e751f9-f44a-30a7-baf2-e02726e930eb | -15.6388 | -52.74554 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ded0985f-a6ca-3b5a-867d-d39adb525dba | -10.53907 | -46.70367 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a05a6b7-d0e9-3d09-a8b8-52fe36caa5fe | -10.81731 | -46.36502 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb15422f-6c1c-3afd-b5b3-3c5451d57f66 | -13.4709 | -46.8522 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e595f72-fbdb-3f4f-b6dd-70dc82f08a04 | -10.48034 | -57.94748 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89cb2101-dd89-34e1-acca-3bdf1d001545 | -13.62667 | -48.21555 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c5652bb0-6280-31ee-80b0-2879a920f641 | -11.33458 | -43.52252 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75adc36b-22d6-34a6-b920-8a4331f8cb72 | -9.16421 | -59.56192 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 11c67f33-6362-3742-9d89-5b0c1da71e74 | -13.43451 | -46.97793 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21c44611-00ff-31a4-ade2-2bbd07632f01 | -13.00825 | -56.90793 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e809cec-a45b-3766-8eee-764c63d87232 | -9.13527 | -65.77503 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6a2abb8-ea61-3f67-bbfd-a54c6105d27f | -10.8101 | -60.77472 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 227f32c0-a258-3053-a934-bbdf8fe07c0e | -9.08903 | -65.7314 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0b3b28bd-01aa-370c-a06a-e99507a6def2 | -9.66471 | -64.98591 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df09c3b0-219f-340e-b6bb-e3836126deed | -8.96389 | -62.16328 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16f62c70-6bbb-3f58-a7bc-a1e25883c26d | -14.36268 | -53.20932 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81ad510f-c4c5-36f2-88c7-4c97ace305db | -15.66598 | -52.74047 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e90af810-1b10-37a2-907b-13970601eb7a | -14.51992 | -53.08908 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c2f5406-1e1c-3134-9d8d-da8d9295a131 | -11.55069 | -46.35348 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 098a9d77-7cb8-341e-b9a7-8990525fdf41 | -12.92618 | -46.31515 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a777123b-4c1b-36bc-80cb-a3a3e199b8e1 | -14.33154 | -51.91031 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14e506dc-2b2e-3a55-ac50-b08eac3202cd | -15.21706 | -53.79772 | 2025-08-28 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f426f58-f2d7-3122-a13b-ebbb0abc6be5 | -14.34864 | -53.35406 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README57.md)
