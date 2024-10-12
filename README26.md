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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99cea881-6c53-32f2-9fc4-21eeef77e2f0 | -4.73251 | -60.78085 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| cdd406e9-882e-333f-90c8-dd9a37df4b26 | -4.72456 | -60.7919 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 7efddf7c-f5ba-3b2b-bc20-eb4e0f966d0a | -4.72325 | -60.78214 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| fc92f2f3-c5a3-3956-b7f7-893322ce3acf | -4.72193 | -60.77239 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| daa78950-7bd6-3800-a6ff-683121e7bfd7 | -4.71842 | -60.79916 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 1a5ac396-8209-3b6a-9acc-ed5b03e3b01c | -4.71706 | -60.78941 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d8b65f3d-5089-3fa4-b240-7bbeb018719a | -4.71571 | -60.77966 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7a4691e2-8169-3163-b202-98af908d6bc4 | -4.71321 | -60.82975 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2d3c1602-70fb-3729-8ceb-b02dd36fd884 | -4.71186 | -60.81998 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7e4799f9-2874-36fd-a9ee-5ef2844ab969 | -4.70123 | -60.81149 | 2024-10-12 01:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 2dd7e7fb-78fd-3ac9-b96f-595dca84726c | -4.472 | -61.08279 | 2024-10-12 01:37:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9145feb7-d99a-36df-967d-4b72a9e2ea07 | -4.00575 | -60.37911 | 2024-10-12 01:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d52a2ad7-ce5a-3e98-900d-7755c4155fdb | -3.99799 | -60.38964 | 2024-10-12 01:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 38c9d58b-ddd8-345b-a01b-c14d088944c5 | -3.9967 | -60.38037 | 2024-10-12 01:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 67ce71a5-e7ca-3b5a-8588-a2dfd8445857 | -7.97825 | -61.22114 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e58d636a-9a9f-3c6c-b286-c971093334b4 | -7.90551 | -61.51749 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e29927bd-18bd-3ec4-8668-bc755fa89276 | -7.81998 | -61.64296 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7c53b13d-9359-3aef-ae55-90a5ccbc3daf | -7.81842 | -61.63108 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 051b7457-48f8-37b8-bc0f-f4c4aa2762c5 | -7.80984 | -61.64433 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1921a8bf-4c12-36cb-95e7-d2ee4f0b30c2 | -7.65006 | -61.20482 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b6b6ca5d-bc6f-3a12-883c-00308bd00f3d | -7.64861 | -61.19372 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ecbab1d7-87a2-36f1-aabb-eb23d75830db | -7.59151 | -61.22985 | 2024-10-12 01:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| aecaa44e-f952-3ab3-973d-9821a4e3b6f8 | -9.09443 | -61.16542 | 2024-10-12 01:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f88c9b26-e6c8-3415-8819-f6f3d1839a89 | -8.97155 | -62.36987 | 2024-10-12 01:37:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 15112f67-5b09-3d1d-863b-486b8256c1f1 | -8.96982 | -62.35603 | 2024-10-12 01:37:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ebd1f4fd-a972-3251-9f16-48c70f1069ec | -8.96753 | -62.36261 | 2024-10-12 01:37:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 34.7 |
| ec264d9b-ace0-3e7b-815f-299ae4007a55 | -8.96571 | -62.34882 | 2024-10-12 01:37:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 580d5c00-25cb-3d8c-a286-50f544bd142b | -8.90217 | -62.37133 | 2024-10-12 01:37:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e1b7a871-3f50-3eae-a87f-7f0bc51ba3ba | -8.90042 | -62.35747 | 2024-10-12 01:37:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 37ab9b88-44a6-3ac1-8903-eabd9e2dd0da | -8.23141 | -61.20329 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aa1f2b8c-e95e-30b8-8452-d040e958532e | -8.22991 | -61.192 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 764c2344-3a5f-3bcd-a3a4-2caf328faf11 | -8.22841 | -61.18071 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| abe7063f-ba9c-316c-9110-c9918344178f | -8.22002 | -61.19335 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 80e40025-f490-3ad3-a623-e72638157a20 | -8.21853 | -61.18208 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2bd25e5e-4c92-3440-91ee-2119b4bddd40 | -8.06536 | -61.26113 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a4572431-23f2-319a-aa8b-7d304bead85b | -8.06148 | -61.30798 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 99ce7ce2-fd9c-3e96-8921-5ab5f59f6df8 | -8.05996 | -61.29652 | 2024-10-12 01:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 897d4415-4e93-3627-b122-9bbd83382f6a | -9.02792 | -63.61922 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5fc8667a-82ba-370f-82f9-61c50744e29c | -8.91557 | -63.55263 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 28.9 |
| d9ecb913-756e-3f4d-9727-31f52c18a804 | -8.91337 | -63.53547 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 24.4 |
| f61629c4-2a20-358c-a732-936642aa9235 | -8.77014 | -63.2243 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e46becf9-1386-3443-833a-1289bd7af297 | -8.68559 | -63.09703 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0612c1b-c949-3b89-96d8-9b10de5b7217 | -8.65956 | -63.26133 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 314fd7a8-43b5-3b29-a060-8955ee4ee0e8 | -8.60511 | -63.10754 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 375ec34f-fe77-3532-bfc7-aa64a976c2ee | -8.57477 | -63.41 | 2024-10-12 01:37:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c72d55e5-3e83-3b99-9b7a-b190769defb5 | -10.57038 | -64.04306 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e9d05b6a-a83f-3ccd-9836-7a3f85297d5d | -10.56989 | -64.0374 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0d0a2577-a205-307b-8827-06dbf7c6e10f | -9.58736 | -64.10827 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 6e463c64-7c10-3c60-a835-d124f57b9952 | -9.58499 | -64.08879 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 3565d0be-7066-366d-99f5-263cc157d790 | -9.56092 | -64.211 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9ab577dd-6481-3342-a7f7-ffefdddfb601 | -9.55878 | -64.19764 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 1d76baae-1e97-330f-8feb-5604bd470029 | -9.55859 | -64.19128 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4e068178-e08f-3d5b-8a90-2bbab0508348 | -9.49089 | -63.13201 | 2024-10-12 01:37:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f3e4c349-9cf5-3270-b99f-0d39e9b4f60d | -10.50278 | -62.98301 | 2024-10-12 01:37:00 | TERRA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a4d3785e-6170-3d79-afc7-dae4da2ea21e | -11.74498 | -63.8344 | 2024-10-12 01:37:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f7157c71-f9ec-3b82-8e4b-86d86927c20e | -10.96194 | -63.60072 | 2024-10-12 01:37:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 03d06cff-8cdf-3a73-b89f-b6c02c2dc741 | -10.85347 | -63.90173 | 2024-10-12 01:37:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 57a7e9e2-4c74-3e52-8770-e71b074b206a | -10.82674 | -64.21941 | 2024-10-12 01:37:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| db952db9-88aa-34bb-9637-05fb54998377 | -9.31645 | -64.44925 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ca9a3dd0-6f52-36d5-9d2f-01032031b55c | -9.89643 | -64.81773 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1a897c85-070c-3f0c-8b91-79a38c5ad0aa | -9.89371 | -64.79554 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 19f064ca-6498-386c-9bf0-fb7380a34dd4 | -9.88295 | -64.81953 | 2024-10-12 01:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 2b278f0b-1fda-328d-858a-64347c9598eb | -1.60353 | -53.34927 | 2024-10-12 01:39:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 4495fdea-a54f-3afb-8423-d79a6ba8e745 | -1.59096 | -53.35118 | 2024-10-12 01:39:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b6c44806-7e33-3031-93ea-25d34124ee6f | -1.26736 | -54.69073 | 2024-10-12 01:39:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2dad9d78-e411-3d0a-a7c0-c5bda739d136 | -1.26529 | -54.67596 | 2024-10-12 01:39:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 896db1a2-a743-3dbb-9163-eb88fe1a4135 | -3.09408 | -59.38577 | 2024-10-12 01:39:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a445602b-8ae6-3c02-b52c-a4a2ec778f4f | -2.6075 | -59.73338 | 2024-10-12 01:39:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 85fd5a7f-ab63-350c-9ea3-37fb62036ff0 | -2.60873 | -59.74221 | 2024-10-12 01:39:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 24325876-0bd7-3a32-87fe-fd3ec7907668 | 2.57902 | -60.69237 | 2024-10-12 01:39:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c0fc16c1-6b57-396a-a63d-eb4e39aa140d | 1.96573 | -60.91424 | 2024-10-12 01:39:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f4fbda1-0e8f-3ba3-9005-d01e0deeee75 | 0.83245 | -60.57533 | 2024-10-12 01:39:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 10d973db-371c-33d2-9006-3cbd6f7bd676 | -1.49415 | -61.59709 | 2024-10-12 01:39:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f65943c4-009f-31b5-b256-16288df98e27 | -3.05341 | -61.68778 | 2024-10-12 01:39:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66224f92-7b9e-376b-8045-d224f757913a | -3.05199 | -61.67745 | 2024-10-12 01:39:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 16d39e1c-aea8-38db-9c32-97dd2654f560 | -3.04245 | -61.67878 | 2024-10-12 01:39:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 9da46652-8d59-3f6a-a422-f0a6c942f6e3 | -1.6061 | -53.3492 | 2024-10-12 01:45:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2a523cb6-5a25-31fe-921b-f520dd86c075 | -1.8793 | -54.4312 | 2024-10-12 01:45:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 609496ef-4e23-3a2e-b812-9db9945cf6f6 | -1.8977 | -54.4309 | 2024-10-12 01:45:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 248c05b6-ca88-3094-8b0a-a9a879d9c277 | -2.77 | -51.3829 | 2024-10-12 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b1323c76-2e2a-3051-bf9b-7c25ccc82a10 | -2.7701 | -51.3622 | 2024-10-12 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| a836e466-29d6-3a4a-b00c-74ed0831fa15 | -2.7884 | -51.3825 | 2024-10-12 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 31fb7676-cefd-3885-bdf9-128c9e0544d5 | -2.7885 | -51.3618 | 2024-10-12 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.9 |
| dc167a13-3537-334b-a619-553ff85dcc3d | -2.8319 | -49.5385 | 2024-10-12 01:45:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 19d68681-46e4-3fec-9151-0b93243a3210 | -3.0311 | -50.5642 | 2024-10-12 01:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8cbf9950-aa50-327c-87aa-c0df4d44921c | -3.1426 | -50.3724 | 2024-10-12 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 67612e46-6857-3b46-b21b-b031cf978b60 | -3.1427 | -50.3514 | 2024-10-12 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 7de59dcc-cd91-3378-a211-e32e5e2fae03 | -3.161 | -50.3718 | 2024-10-12 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 69909b40-4899-3c30-b88d-1746294ecdcc | -3.1611 | -50.3508 | 2024-10-12 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6dd2273c-998b-30b2-9227-2f814d24bdbb | -3.2136 | -46.7843 | 2024-10-12 01:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2db996f9-046d-3d7f-b191-736e4a0c0cf9 | -3.2321 | -46.7836 | 2024-10-12 01:45:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 32f90f58-3b20-355b-b107-026ad819803a | -3.483 | -52.8211 | 2024-10-12 01:45:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 16bd35dc-e248-36f7-851b-cc60ec278968 | -3.69 | -47.9451 | 2024-10-12 01:45:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 3fcc3721-8922-33b2-b21a-65ac338402e0 | -3.6901 | -47.9234 | 2024-10-12 01:45:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 210.9 |
| 8b328e88-e580-3c39-8b01-a316904d936f | -3.6903 | -47.9018 | 2024-10-12 01:45:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 1d19c9d6-d3c1-345d-8161-d9d52cac17b4 | -3.7086 | -47.9444 | 2024-10-12 01:45:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 4b114e10-ac38-3483-87bc-8535bb4eca82 | -3.7087 | -47.9227 | 2024-10-12 01:45:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 419.3 |
| 3b9a2445-0d64-343d-9547-a259f7168eb7 | -3.7088 | -47.901 | 2024-10-12 01:45:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9da75aa6-a5da-33bc-8660-f8d95cee5030 | -4.1148 | -48.2515 | 2024-10-12 01:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8c5a5d90-5dd1-3ae9-801e-03b4f8aa20c5 | -4.2665 | -50.9594 | 2024-10-12 01:45:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |


[Clique aqui para ver as próximas entradas](README27.md)
