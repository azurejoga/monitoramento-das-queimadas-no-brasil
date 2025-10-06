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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7dd0f1b-88f7-3d60-982e-324ccaf5117b | 0.57008 | -50.84498 | 2025-10-06 04:23:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e13243cd-6bf7-3a6d-9554-31e9ee658427 | 0.56575 | -50.84564 | 2025-10-06 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 464acf17-f0fb-34db-8f8e-5add14bbc14f | 0.56208 | -50.85042 | 2025-10-06 04:23:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b906500-a545-376d-bf29-90f00ec81c25 | 0.56784 | -50.84637 | 2025-10-06 04:23:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79d0e40e-b5fd-3473-87e2-dc956cfe75f8 | -6.54752 | -47.8536 | 2025-10-06 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e29afa21-7c71-31eb-8694-8ea5c2538feb | -7.47411 | -42.61998 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 881d07cd-ef04-33de-bcf9-04d8051d0e99 | -8.62964 | -46.32811 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 560ed3e5-a660-3ce0-a9ba-cedbfb13f267 | -5.6447 | -45.96619 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2ce6fe0f-e2d8-320b-a73f-0e0ea94fa67e | -8.88307 | -47.62148 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c965f13-79d1-3328-9f04-dd5e3fd56a28 | -7.71625 | -42.38979 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9232370f-d0b3-30b7-8c6e-7d305e05f644 | -7.47344 | -42.62459 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 35fbcf6a-f6b1-375c-bf51-28b412705345 | -6.55425 | -47.85465 | 2025-10-06 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 1e123292-b7cc-3e8b-8a92-4704adaf202a | -5.79969 | -45.47044 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73ce72d0-d565-309e-8ef5-ae14a2b266fa | -7.72316 | -46.25213 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b3249cd-c5de-3108-ad2e-55d2134665cc | -7.78612 | -42.60083 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d20bf07e-f1f3-3b6f-8e91-704a09caf6af | -7.61637 | -45.46936 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b74dc81-9047-3dfa-a120-adbeba4a531e | -6.49408 | -43.95243 | 2025-10-06 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d72b98a0-b5b4-34e0-8eaf-3d681047abd0 | -5.62695 | -51.08673 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72c9b381-2284-3c84-9d01-d2ba918350ce | -7.72449 | -46.33029 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36844615-4e99-32d4-8a88-b2e0562ba901 | -3.74526 | -52.3765 | 2025-10-06 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a65d78f8-fa75-3eee-bd5b-652294744111 | -4.36332 | -50.86257 | 2025-10-06 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6394264c-9b82-3f74-b0f6-0bc37de2fa24 | -4.8218 | -42.87187 | 2025-10-06 04:25:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4344c19c-377a-3bf5-8538-e6a5a1ff2bfd | -7.71108 | -42.3987 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5c5f8b8f-e4a2-3cf7-b35c-5b6169e69bdc | -8.86252 | -46.79876 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2084d80f-6a7d-356c-9c6f-f7eeb01a89e5 | -6.62016 | -41.97404 | 2025-10-06 04:25:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 625597fe-c719-329c-b3f6-7b268030bf4a | -8.88638 | -47.62201 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| add756a6-4951-321e-8631-cc972cacd7b4 | -8.6136 | -46.30067 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4ced242-1cbf-3f11-8c85-2e70407f1b26 | -4.65173 | -43.18614 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e446406-4618-3b2b-a355-2f55d5d6bc40 | -5.99565 | -44.24922 | 2025-10-06 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3874d1bd-6f9e-3434-bc3c-c038f70c03f3 | -3.15374 | -50.45772 | 2025-10-06 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05644ade-0fd4-3b5c-b0fe-be1fe7be5d1d | -4.90069 | -45.73573 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dc9a839-983f-3c48-aecc-fe65b527784b | -5.98635 | -45.4743 | 2025-10-06 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f41d5bb0-3660-3184-9fe4-2bc111fea5dd | -5.23302 | -42.4486 | 2025-10-06 04:25:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5e291632-f26d-37d1-a27b-42ff89a8d465 | -6.69392 | -41.38465 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ce933522-86ca-3cf3-aea5-460bdd6ddc46 | -7.25805 | -44.13416 | 2025-10-06 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 43a76b0b-f79c-34e2-a179-1518deebd419 | -7.56738 | -47.6731 | 2025-10-06 04:25:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 311dce85-283b-31ec-a1dd-08b724b13f4c | -3.75342 | -51.3761 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f61fa0c-7159-398a-bcae-d75d93e42993 | -6.25282 | -43.25733 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15521506-8dd4-3c1f-a511-ab0b2db16204 | -7.91404 | -49.27216 | 2025-10-06 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9942541a-5bf3-333e-99d0-2bf7c4934fb5 | -2.29402 | -47.99168 | 2025-10-06 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f592b963-c922-3732-8b9a-850e4a6dc07e | -8.55488 | -47.67279 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 788b195a-3523-305c-84b5-b60c09e293e0 | -3.81118 | -51.07156 | 2025-10-06 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05f5369d-0f7c-3999-b2cc-3acfaff6cde9 | -4.76741 | -44.45169 | 2025-10-06 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8f31c86-bf1d-3301-9ecf-63de67062456 | -7.21785 | -45.9131 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d237855-a648-382e-9045-951bffd91305 | -6.5944 | -43.72742 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 518a4bc2-1b7a-394c-bdf7-8e204a39b212 | -5.25623 | -46.48961 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 24ed3c85-9497-3b17-9b99-558bf9e686fb | -8.5496 | -46.25498 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 836938b0-11b1-398d-b3e1-6356b54eb6a8 | -6.5938 | -43.73138 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abaa9e45-220b-35ba-ab8e-556c6e8673e5 | -9.30318 | -45.66455 | 2025-10-06 04:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ce422de-d257-3d63-8d7c-88208f214073 | -7.77989 | -42.62106 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f34c1b94-f780-3ea1-82b6-bc5600878166 | -6.18884 | -42.71494 | 2025-10-06 04:25:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d966fe7-9044-3fed-a4f0-bd7a60b94cae | -7.40365 | -47.26923 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c49293c4-5fb7-3d17-8a41-e01711f4b58d | -7.03516 | -42.75985 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| af0a88ba-9ebf-3be9-9a8b-d4c1aee74f81 | -5.27724 | -42.92748 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b0ae853-eea9-366d-b3da-2e60eaaba7db | -5.79827 | -45.81021 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45590016-2534-3148-9ce3-fd325e84ee84 | -8.61192 | -46.28971 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cd8e9030-d0e7-345f-81e8-e884ac539e4d | -8.53707 | -46.29222 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5f19db1-0214-353a-9781-d331ff5494da | -7.207 | -46.85305 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbbe475e-0faa-31e9-ba6e-67a2a2b09782 | -6.67153 | -42.38724 | 2025-10-06 04:25:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fbd5fa7d-7e21-3603-ab48-85bb31bfdd43 | -5.81462 | -45.48344 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67f8012b-6fad-39f3-a6fb-1b426115e322 | -8.90324 | -47.81564 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f12dc5f-9b1b-3f63-9bb7-29a066ed0831 | -7.48242 | -43.02628 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 888dcbb6-b399-38a1-8062-68d954bf0e88 | -5.66457 | -48.92718 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5949104-6754-3c17-8604-24299f5e5bd9 | -6.68085 | -41.39006 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85f6bd1b-af5b-34f4-b75b-e436b05d1768 | -5.29874 | -49.49654 | 2025-10-06 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa53ce86-3d39-3fc4-9bdf-5f4bead4c499 | -5.63095 | -51.08738 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a0a4813-5f0a-3b98-825c-2a7b55ae4c1a | -6.94883 | -43.11846 | 2025-10-06 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e5d60ac-2799-3c1b-b25b-1be9c3b0999b | -6.3655 | -44.65086 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41c83936-ca8b-3511-a41d-e9e2547a071e | -6.5979 | -43.72798 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba4aa346-cb20-38f2-ac69-7beb7c07c29c | -5.64578 | -45.95932 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c1aff7c3-e360-3f59-b179-7e47ea3506df | -8.16744 | -50.16104 | 2025-10-06 04:25:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20f47ff8-abba-3ae2-9a2b-7fd833d2423c | -5.70663 | -46.33159 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 126152c2-8d83-34a9-92c7-2d2f9d8a409d | -8.18244 | -44.24149 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d27bc51f-27d2-3468-bb1f-0a3b127fa5a1 | -8.96398 | -44.61113 | 2025-10-06 04:25:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 584715a2-3508-35e2-8d6e-fa1fe0448831 | -6.85546 | -51.06375 | 2025-10-06 04:25:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77437839-e4b0-3324-8156-eae73263226e | -5.47165 | -43.1519 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66d5dd5c-9294-3c2c-ab89-0c52931ab025 | -5.69763 | -44.83586 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1697f86b-df21-38c1-9891-db8eae70c82e | -7.71983 | -42.55305 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7d553eba-0b37-339b-91b4-6c728a82f3d6 | -5.76976 | -45.74934 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69a4c294-bfa3-3947-b9a6-674f99119c04 | -7.39979 | -47.27218 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daf055c7-9d29-3211-8c35-00d161b031cd | -3.50832 | -50.47401 | 2025-10-06 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 693cfd78-b2ba-3d5f-a20e-4ed34267b0cb | -7.7072 | -46.24605 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0786726c-5f49-32f6-a079-3f1f2ceca6b0 | -7.80939 | -42.55013 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57f5dc54-85e2-3781-b947-aa7d9d1c596d | -6.50919 | -44.49252 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9075004f-7045-3b44-b09a-a60e8811bfe8 | -7.73535 | -42.3926 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1b477182-3c52-3a37-87e1-78cd0540ee31 | -5.7703 | -45.74588 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6de31f85-0093-3f86-8ad8-7cabae496b3a | -8.63018 | -46.32463 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ae124faf-bd0f-34c9-b4cf-49d0c5e350b3 | -7.68491 | -42.58094 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ab853ca7-0bb7-3e66-9c96-b6b212a93e0e | -7.21447 | -45.89122 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6464a06a-db70-3d99-af55-819207926ce3 | -7.80146 | -44.13338 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f0b84c3-9449-386d-b710-2f59a565b19a | -5.24238 | -45.37962 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb4ed267-9487-38e2-a936-45ab4b9f5ffc | -8.61391 | -49.13959 | 2025-10-06 04:25:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0b94a3f-4433-3960-86e2-789e74426ecd | -8.54492 | -47.67123 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e169bf7-cace-3baf-94c4-49294492ec2b | -8.45353 | -46.87186 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e988892-5969-3850-9640-b0de5ec58539 | -3.74337 | -52.37439 | 2025-10-06 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64627fe8-7249-3087-8c07-97ced8b89a41 | -5.29469 | -43.10204 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 522d5271-cad4-36af-a191-144f47ef1f72 | -5.30238 | -49.49715 | 2025-10-06 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c98fb127-f693-3b90-8879-fb46a4c578a3 | -7.29426 | -48.62559 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4734ff7e-782b-3fc2-a160-4855d3d40304 | -7.01888 | -42.79345 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 27b38573-6264-34e4-a4d0-5d8b71390e6f | -8.52562 | -46.3225 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README23.md)
