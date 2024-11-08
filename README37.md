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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f74052e6-5d12-35ae-9377-4d0475416bc5 | -2.81341 | -52.96868 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c1dd7b8-baaa-3341-a2c2-4690c8f1730e | -2.79843 | -52.9539 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d95e9ab9-a107-3cc7-8111-7b6071d61d32 | -2.46013 | -57.91253 | 2024-11-08 05:40:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 416266af-6f98-3173-9c82-d0443a2fe72e | -3.09397 | -53.32234 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c596158-2105-37df-ab4b-85eda31c0be4 | -2.8202 | -52.93696 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c91cee1-f9ed-3cfa-9571-c79c21c077f2 | -2.94459 | -52.70644 | 2024-11-08 05:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a65ae55c-a988-31c7-bf77-968dab036ccf | -3.05826 | -57.1093 | 2024-11-08 05:40:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e391d69f-4699-3dcc-b4db-b1c5fedb1ab1 | -2.76321 | -53.2272 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2216010a-7cb6-3759-aa60-24b1ffeb4d9c | -3.01549 | -53.42849 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f73f7bc-0d91-38c5-83ca-fe3767dcfc5b | -7.92962 | -61.46791 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 836d3aab-62cb-3885-b306-bbccebd650d2 | -3.01415 | -53.43746 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91025c4c-a1e8-3c5d-b62f-283c21568323 | -2.81319 | -52.94094 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf055059-b7c1-3b95-b56d-62496421da58 | -2.80621 | -52.94476 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a5d0c208-abf2-3e51-896e-09f5676190aa | -2.83095 | -52.90856 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3540c27d-29cd-3b44-acc3-0accb87445f4 | -3.09516 | -51.11733 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b535efd-fd99-37f4-976d-ceb80db03c06 | -0.77926 | -62.90813 | 2024-11-08 05:40:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 236a1773-635e-38f9-a4ef-fadde1274a70 | -2.82678 | -52.92076 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 031c4056-4fed-3cb3-b28c-6dd41b1c289b | -2.82345 | -52.95755 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8ba6556-61ba-3cc0-867e-555d1bc63676 | -2.81408 | -52.96402 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 21441fea-dfdc-34b2-b67d-672ccfaa35f4 | -2.84151 | -52.90767 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9f9282a-e050-3d30-a5e0-880fef909f69 | -2.83723 | -52.90944 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b5f2df-ba6b-3b30-a26e-a83b11f154f0 | -4.16565 | -63.12953 | 2024-11-08 05:40:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7ba689b3-3d59-37c0-b645-5baa248f49b5 | -2.61764 | -51.29819 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e3161e1a-d815-3dd6-8342-f8dafd1a753d | -2.81089 | -52.95606 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a4ba3da-c284-37c4-9d36-de4019c251ee | -2.81164 | -52.95111 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49eb78f8-30b6-36e2-a0af-5954db30510a | -2.80919 | -52.95372 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 557e5924-8341-3d85-b0bd-768560a0c23f | -2.82242 | -52.95066 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29822520-3efe-3b25-a6b3-8cd3606ba6df | -2.80296 | -52.95258 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d4811560-66b9-3abd-9ce7-307d2c13377f | -7.8721 | -61.67847 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 191b0a3b-5a86-39fa-a6a9-d1575f3859ca | -3.02656 | -51.53476 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9565b785-f9e1-38c8-a128-798698005175 | -3.09412 | -53.31986 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f71fc69d-9f44-3833-b411-e72c358967f9 | -2.80446 | -52.94226 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fb629339-0b3a-34de-8f98-9474776d0004 | -2.82818 | -52.91116 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 781cc45d-8b6b-30f2-8d17-3ee128a60d23 | -6.47737 | -60.07071 | 2024-11-08 05:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c31ed85-37ac-31fc-a3ab-22118eb1f254 | -7.8722 | -61.67611 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56e44f44-0eb4-325e-83e6-aa5dc641b7d9 | -3.04377 | -53.28056 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2050a1f5-cf5d-3f7b-97c3-cba560cf34dc | -2.82198 | -52.90974 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81cf9e01-8d31-3349-b010-59b51566ae46 | -7.32235 | -64.62039 | 2024-11-08 05:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a3319b7-b265-3132-a968-0a2b93c132fe | -7.9258 | -61.46734 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02f1e11c-9ab9-3d26-b962-f37b866d005e | -2.6236 | -51.30541 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6331d36-087e-3ca5-8c79-a818b8fdfa86 | -3.15554 | -54.48264 | 2024-11-08 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd34a84e-c7ad-3388-a02f-c35529d5a588 | -3.27715 | -61.50747 | 2024-11-08 05:40:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7abc0c5d-a773-3865-a0ce-382c4b73427a | -2.82036 | -52.96481 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a6b3b17-a7d4-3ca2-bfc1-f35d7c06be4d | -2.62459 | -51.30099 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60a5bfa7-8e14-383a-8c1a-5572b6a9fcf0 | -2.79749 | -52.94621 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 073706bf-a2f4-39c8-a190-547e315ae378 | -3.02746 | -51.52881 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eebc8c2e-0a4f-3bac-bcd1-0f1bab85cac9 | -2.82312 | -52.94589 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 821c60cc-6701-3159-a83e-a76267a851e9 | -2.82099 | -52.93183 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c123be9-3fc6-3787-ac0c-6706f86395c7 | -2.79822 | -52.94114 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7e653af2-350f-3305-aea3-4d42c08b08b1 | -3.0135 | -53.44187 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5e46b99-d8f0-394e-8b42-5e27cc650406 | -2.81616 | -52.94972 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00aa30a5-136b-3b5e-9d07-b9572a3ae39b | -2.81764 | -52.93959 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68b8430c-0028-35b7-ab7d-606bf015d5a0 | -2.83521 | -52.90689 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce91276c-c84a-3553-9e01-87615366b8f7 | -2.82174 | -52.92687 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a38298a8-e3ab-3f2b-babc-5f749966f743 | -2.81215 | -52.93332 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 860f9a94-1848-3867-9f9d-61f7f3935650 | -2.82395 | -52.91239 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11d76e47-b0b5-30e7-b7ee-977848a13708 | -6.9144 | -59.06448 | 2024-11-08 05:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 735bffcb-9a35-3319-83fa-16a7729a85c6 | -3.04449 | -53.27575 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40b19e3b-e574-3a87-a480-2acdc64a873c | -2.61387 | -51.75248 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 16458c63-58d6-3395-9f20-e01fb080ca57 | -2.83806 | -52.90406 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea5701a-2ba8-3786-9262-7e581fe77599 | -7.87145 | -61.68303 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d6a4849-687c-396a-a8e5-5b3570045efd | -0.78205 | -62.91216 | 2024-11-08 05:40:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c83694f5-59d6-3962-8295-82e55e46c6c9 | -2.81476 | -52.95935 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab5bf2ac-c061-3f2a-8f27-03e229590bee | -2.6167 | -51.30439 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e8843af8-b28b-31dd-8476-32402958016f | -3.02843 | -51.53069 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b4ac2946-4a5b-3596-b706-212227973750 | -2.82893 | -52.90599 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbdb9141-b4b1-3b42-8f48-68e3242706fd | -2.81965 | -52.96961 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 609ba039-0bf6-3988-becb-9324f1e4c4cd | -3.09345 | -53.32447 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2c71035-5578-3148-991a-33fa1fcbdde5 | -2.81983 | -52.92452 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 034174e2-3b8b-35bc-89ff-66e58358507b | -2.81864 | -52.9472 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93514bd0-526a-3880-9d69-d27caf0096d1 | -2.80372 | -52.94733 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| badc8757-ea5e-3f83-ba09-092aaa7a44fd | -2.81839 | -52.93443 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dcf80bd-4952-3243-ba15-3d47907a898d | -7.89362 | -61.66287 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82939ad8-bd3f-32f6-b639-696a335027ff | -3.02757 | -51.53662 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ff406caf-8002-32aa-9275-e299756c925a | -7.92198 | -61.46676 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42f3895b-fe27-3c31-b43d-6f70f18f4ca1 | -3.03442 | -51.53756 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d6f848df-229f-3e01-ba2b-d3ba34b2bea9 | -2.79921 | -52.94877 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9039ad33-b15c-366a-ae59-1369f4814a20 | -3.01482 | -53.43297 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d5149f4-bc50-3b9e-9447-558b1e70612a | -7.92649 | -61.4626 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9b3beff-510c-3f66-b745-f3812ab86851 | -7.69208 | -61.06088 | 2024-11-08 05:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d56f79e4-07d7-3ac6-8803-d09b90927605 | -3.74916 | -52.09899 | 2024-11-08 05:40:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77121d0a-3e5f-32dd-813b-b8a06c1d2f00 | -3.0334 | -51.53571 | 2024-11-08 05:40:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 02976164-12c7-3973-a00f-d21f2daf928d | -3.04991 | -53.28151 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b1be188-9e02-39ab-8102-d51fb8649572 | -2.81913 | -52.92932 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8ee91b7-1986-34c4-b286-681c249c75e0 | -3.00804 | -53.43674 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca25e6a1-b42b-3302-a944-b0cc02d8eebd | -2.61678 | -51.30629 | 2024-11-08 05:40:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bfde69c-4c25-3f99-aa63-762f85c41b21 | -2.80948 | -52.96534 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01f248cd-8838-3c41-b556-bb78ec3abdeb | -2.79298 | -52.94765 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de348912-0819-3289-a69e-86e15973cba6 | -7.87152 | -61.68065 | 2024-11-08 05:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a294269a-7c2b-3b6f-8eee-8d87b3699e8b | -2.81141 | -52.93844 | 2024-11-08 05:40:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6af94d1d-4b38-3374-a2ce-f88392554c53 | -9.39259 | -63.26108 | 2024-11-08 05:42:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9efd1a2-0d50-3337-bf01-24c77de9ad6d | -8.39182 | -63.94058 | 2024-11-08 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afa4fb4e-b802-379d-82ca-4e7ccd603159 | -9.16437 | -61.53723 | 2024-11-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 036a6235-d6fb-3147-8ef6-24f3e7728eb8 | -9.03261 | -61.99005 | 2024-11-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c7b9e97-4872-3737-a143-9a0ea0bc7e30 | -9.392 | -63.26509 | 2024-11-08 05:42:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dce7c7ae-a1d8-3e48-adc8-0505f9ff58b4 | -9.80081 | -61.51201 | 2024-11-08 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93f21682-adff-3daa-b1ad-77e322db2d28 | -9.03195 | -61.99462 | 2024-11-08 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95a49e07-1187-326d-a97b-16a98651dee3 | -3.3833 | -50.2177 | 2024-11-08 05:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 57dc5586-b192-3663-94fe-1870e3ae873b | -2.8016 | -52.9617 | 2024-11-08 05:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c9540ac5-c45b-3232-a5c3-0468949936e3 | -4.5209 | -45.6804 | 2024-11-08 05:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |


[Clique aqui para ver as próximas entradas](README38.md)
