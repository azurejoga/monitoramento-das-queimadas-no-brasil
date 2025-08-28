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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31c74614-3a8d-3fcb-b10d-ad8f50448b4e | -10.28058 | -64.48974 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e71184e5-36fd-3b7e-a902-fbc66b712701 | -9.41345 | -60.49961 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6640bfe2-b6b3-354a-b707-ff51d1fa68a3 | -9.17589 | -59.493 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8c4665b-1e98-3f1f-99b3-574271b1bf89 | -10.47163 | -57.93068 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35790c18-d8a1-377f-a6b3-eecc943f807e | -12.67685 | -48.17032 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40f459ed-ed41-34a0-b8f1-de7441df761b | -9.5688 | -55.38152 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3f46ee0-5bfd-32f9-99ac-9dccd5d14192 | -11.23791 | -55.05947 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 947f774f-0eb8-3136-976b-6769022d52cf | -9.4054 | -60.52139 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2b25667-927c-36c6-81ec-af1c91e0c5d2 | -8.96185 | -65.9752 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d81bc3b-c1a3-3d20-838b-933b054d8463 | -9.12938 | -65.77406 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b962bffa-f23b-3fcb-bafb-581e0ea769f7 | -13.00492 | -56.90738 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4db3e80d-57eb-34da-8fbf-7ffc7a439017 | -9.41711 | -60.52728 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e4e2ed5-6795-3e7b-9288-5f98516e9713 | -9.57872 | -55.3831 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97f3fb82-cfbd-35a8-8430-bbae869f3026 | -12.89011 | -48.10001 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2569efa-6ff8-35ff-afd4-1b8c2315286e | -11.22907 | -55.05087 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c6e19b00-4a5b-3b1e-a0ab-38128a0e76e7 | -12.79148 | -48.14879 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b990b07-33b2-32fa-80d2-288ec58566be | -15.08077 | -48.51083 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d9216f3-6278-3a3f-8ec7-559f5bbde944 | -11.65298 | -46.39102 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6e7cce4-940b-326a-bb0c-82b28d585236 | -13.18012 | -45.28858 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 18ad0b7d-94c7-32c9-9b4d-ec00d6c44cf1 | -8.87929 | -62.47879 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62edf631-1814-3282-9c79-0acc908b74ea | -9.13972 | -65.27254 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75d68957-b693-33aa-9336-121d0c46e38f | -11.65313 | -44.87211 | 2025-08-28 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f79cac3c-de20-3bff-86f0-c0c204a1891e | -10.59579 | -54.90312 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84206dd3-b785-3c89-a886-13f0bef67bbb | -8.96437 | -65.9463 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1c098c9-a510-312f-b94e-6b45b7778612 | -15.61723 | -52.72189 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e26cc953-c51c-33cb-90b3-d55c26b55fc8 | -9.41299 | -60.52657 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f386e627-971a-387c-b432-edf678a1f0be | -14.36574 | -52.08607 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 220961c1-29b3-3792-902c-3faacfc88f97 | -12.92928 | -46.3356 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f2b483e-376b-3630-a48b-4f98c7d64cf4 | -10.60653 | -55.40222 | 2025-08-28 04:59:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fc82508-ac04-3e9a-bd21-61a30ffa396e | -12.44084 | -48.71461 | 2025-08-28 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 941a02aa-5806-356e-9701-5e7d20d38588 | -13.63635 | -48.21657 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 653223b6-9cbb-3819-9e25-02c9f76b66b3 | -13.43953 | -46.84858 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6724cf18-8a41-3dfe-8854-596b8af4b675 | -13.9937 | -46.34416 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c983fbf-5e0a-3ce1-a074-36706cd9a60b | -9.16257 | -59.5716 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97134d61-3635-37c3-a751-0ab01d0d4aad | -10.52453 | -46.69505 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16130153-f2f6-32a9-a5bd-19354dc1f37a | -9.13754 | -65.28421 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2086a12c-fd42-3a9c-8f50-00113a8c6e6c | -10.5308 | -46.6867 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9daf5fc-155c-35e9-92af-f50e50ef92ae | -8.95501 | -65.96298 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 567b9af8-ba37-3165-8ba5-702137e513ba | -9.02391 | -65.69803 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ecd1508a-9060-377c-9785-364787c6a35c | -15.09749 | -48.53395 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a9ac1f62-908f-341b-9fce-2618f3d9250a | -10.06675 | -58.36484 | 2025-08-28 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e84a820-4e8f-38cf-bbeb-15407161dfee | -9.08078 | -65.71728 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 595fb1f6-3f40-3e52-8d3d-c8d44ff858db | -9.40343 | -60.53267 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d1ef34a-2f2d-34dd-9dfe-551f2f525d97 | -13.08471 | -46.34173 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 528fa993-6450-30a2-ba98-2f3cb28d3343 | -14.44108 | -53.19048 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d296f913-2b53-30ea-bd0c-1334aa78a43c | -11.6059 | -46.21536 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1ccee8a-c648-3eb0-b84b-d5805ab3924c | -12.95546 | -44.57483 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9dc13427-37a3-39ba-b43a-ab219649519d | -10.53711 | -46.6781 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 289d9ba6-a9aa-3bb7-a90f-2d7cc6a1f585 | -9.16339 | -59.56673 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e86c98d8-5dad-3e1e-a3ab-f4fb613ea60f | -10.30595 | -46.81123 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e084baf-d267-329a-976a-4016968ef94f | -9.11446 | -65.7887 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| cb7a406a-6f7e-3046-be45-be54f8df050f | -13.37863 | -51.76952 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 48f77396-f262-32cf-8f4c-5d06068296e4 | -9.64895 | -59.62348 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27011e37-b27f-355a-9ba5-b301c2fb5342 | -9.13444 | -65.7794 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09a5f58e-9e2f-3c10-8462-c0b42b40969b | -9.1195 | -65.7941 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 54605e5a-c2db-377a-b969-3e972831bd9b | -10.60626 | -54.90121 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ecb0de4-280d-36c1-8565-3fe9aa332db5 | -14.27635 | -53.07196 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| d66f09e4-62b0-3245-af63-5660e6e616f3 | -15.61596 | -52.73086 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| befd039d-17d9-344e-afb5-24872d821033 | -13.39547 | -46.85877 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08bb2341-6bee-3cb4-8c46-bf17a966612a | -13.37837 | -51.76635 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa738c53-7368-3d8a-93e9-7221c2d8ad2d | -14.31802 | -60.36016 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e876da3f-059b-3efa-bd88-324fe8e3edea | -14.29068 | -53.04824 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 4c1675a2-46b1-3cba-b2cd-c3d2a09aad18 | -14.26636 | -53.0766 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd7a00df-ad00-3308-9e25-73b6814bd1e7 | -9.10415 | -65.74735 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44cdfb30-35d5-360b-bf8a-1a121300b09b | -14.36196 | -52.0855 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e749e00-b443-34dd-a004-7d9dd7cef907 | -11.5693 | -46.42059 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac54f7d8-4df0-3eca-9204-ddfbf4985145 | -10.80665 | -60.77026 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9b567ee4-e0be-39cf-b5d5-0541833b853a | -9.15473 | -59.57055 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37d48ac9-d06d-37ea-807c-e5f14ade1c8a | -10.4649 | -57.94984 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8389f048-e462-3486-b090-97b28648e7ea | -10.46842 | -57.95045 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4243a06d-7e8b-3a03-b7d2-21023c3f3cdf | -11.56973 | -46.4171 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dc09bee7-8ae8-3d56-90a1-4fca375859da | -12.80159 | -48.14607 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1dea1807-62a8-302f-b91e-62a68cad6fc6 | -13.51747 | -46.86619 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a850121-63bb-3f7c-abb8-fdfdd03356e3 | -13.62807 | -48.24289 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bcd59869-5b87-3431-8ce1-0e2304855976 | -12.79014 | -48.15899 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d0747ceb-5000-3e47-b8ff-70978e91e93f | -10.4588 | -59.12567 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1894900-68f6-31ce-9af2-59959bbb2257 | -12.95493 | -44.57951 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1dcbe4a1-c635-33e2-b707-2646f4904777 | -9.52597 | -60.5274 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fb5b65b-f29e-3610-9a75-b5ef0ce5a45c | -9.18871 | -60.81367 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d29d0126-6242-374d-8cc5-1611917dd3b7 | -10.47737 | -57.93974 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| fc583be6-b3a3-30ed-b7e3-23ec6cfb179b | -9.55158 | -65.69869 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cdf25c2c-bac3-3f51-abab-80dc6ea737cf | -9.19459 | -59.64373 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e5cf350-b8ce-31e7-b40e-54e8adf54f01 | -13.47111 | -46.85336 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b9d3e36-3a7a-3792-8ef4-3ca3b9d9823f | -15.68203 | -52.76109 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6360acbf-5439-3584-8752-23cc571fdd5b | -9.5299 | -62.40134 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fecdb6e-8a6f-314a-a120-835c5ed97895 | -15.60856 | -52.72966 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9146610-9023-371f-b1a2-5be7ce3164a4 | -9.16114 | -59.55639 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3d57a31-47be-3027-b6b9-c0308b671a41 | -13.18061 | -45.28438 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4dd4832f-4264-3ad5-9530-49e60811f6e1 | -8.26281 | -61.45464 | 2025-08-28 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 06969d33-4ad6-339b-8858-7a8886246799 | -11.34219 | -43.53639 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e1f5ce5f-6478-3173-b913-9d3e10fd69c1 | -13.98206 | -46.34847 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f91073b-1108-3802-b292-cddd55aa8cf4 | -14.51213 | -53.09225 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af7e9951-a48d-3a13-9e7b-519073b3e955 | -12.93006 | -46.32895 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0df1f303-75e6-32e8-a0fe-4eac80ef0b43 | -12.69647 | -48.16882 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b1d5ca6-3a80-3a28-83c3-f89145773d42 | -10.59964 | -54.90015 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58073095-3343-38a1-8630-21d69424c921 | -9.23136 | -60.91861 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d033f943-c8b6-3db1-b420-e1cfcabc088d | -9.40212 | -60.54016 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78e64a72-4ffe-3330-a89d-d3a6c4661970 | -9.59614 | -55.38234 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee1c775e-8810-3522-b94f-a093bfad600c | -8.95843 | -65.94518 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82bf1c0f-9005-3e76-bd81-c319c931177d | -9.12113 | -65.78553 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |


[Clique aqui para ver as próximas entradas](README61.md)
