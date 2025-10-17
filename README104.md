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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3646eb8-fb5c-3d38-8951-e6915eee3038 | -2.87643 | -50.73009 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ea12384-97f9-3a50-92b8-abbc8683f309 | 1.78695 | -55.9211 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d3b9906-384d-34f8-845e-5bfb32858396 | -3.84198 | -49.93297 | 2025-10-17 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5409f6b-e13d-34ad-b5e7-f9813e5d11b1 | -2.748 | -49.38878 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37c46a20-85b4-3680-a185-9d468f1f3435 | 1.78965 | -55.72303 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64d9dcdc-b290-3511-b084-c09b2bc1da72 | 1.7935 | -55.72595 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d060bd43-7494-3f7e-9227-90e0a89acba6 | -5.25147 | -44.209 | 2025-10-17 05:08:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ba0d05-9d90-3ee3-8830-3c9f19d28bc0 | -2.56375 | -58.02063 | 2025-10-17 05:08:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6257b48e-26dc-3520-b61c-d45a1527a835 | -5.74002 | -44.98966 | 2025-10-17 05:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af2f614e-e7c9-36a9-a77c-0af13498b0e2 | -4.81454 | -43.20576 | 2025-10-17 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dce2330b-bfd1-35a8-a681-fdf6a40206e9 | -3.78247 | -49.42885 | 2025-10-17 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0cdf7fa2-8f9f-3970-83ac-23b48c9e755b | -5.89162 | -43.90526 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20021a38-6cc2-3559-b2a0-0874932fa98d | -3.93102 | -49.42946 | 2025-10-17 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 760bde68-6227-3818-accc-cbeb9c18526e | -3.87199 | -51.95017 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d66e013-5530-3dcf-ac9d-d894c9f2579d | -4.39616 | -43.41839 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56492272-0d86-385f-9feb-a9dcd8f573ba | -3.28754 | -52.54539 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db60cabf-0e3e-3aad-a8e2-64c099cd3d27 | -6.32095 | -43.62788 | 2025-10-17 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 84142652-d693-367d-a3ce-243f575cdeaa | -5.9049 | -44.75419 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67673ac8-942d-3b40-97ca-4759f0f2dec1 | 1.78424 | -55.90383 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33ed5ac9-7cb1-3ec7-8a91-b362fa12cb55 | -3.5089 | -52.48998 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 84f855ea-e81f-3032-b94e-8c66711f18e3 | -6.17613 | -44.33411 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40b55d5e-3693-3cc8-9aca-ae18c9d56385 | 1.74548 | -55.76514 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 32be6aa3-0f51-393d-8120-4cc487eb4c3d | -5.14815 | -46.05945 | 2025-10-17 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e29da9b-a989-3aaa-b913-38f4487eb5f0 | 1.04243 | -51.20895 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0425dedc-7688-3cc9-b6bb-0ead7d45eb16 | -6.42598 | -44.71939 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2de12583-fe5f-3c4b-9196-e4de70cc8c0d | -5.45636 | -44.64507 | 2025-10-17 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 554fd958-bab7-387a-8bfb-b90fb378946f | -4.25224 | -48.55119 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cf2d10d-502b-300d-bd1b-b09180aca408 | 1.82797 | -55.70644 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c2769f6-a896-3572-89f2-9e5a66f631b3 | 1.74657 | -55.77203 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e5dcf3f-13d6-30e0-91bc-494a4122ebe5 | -3.68068 | -47.63477 | 2025-10-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7994125b-d5ae-358c-8020-5d1972aec598 | -5.29177 | -43.55398 | 2025-10-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b78c4fb5-f69d-3b7b-b41c-1c17b1099c37 | -4.95542 | -49.57409 | 2025-10-17 05:08:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67edfcdb-187f-32a0-af2a-e5416275af0f | -2.86803 | -50.72882 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 618e93ff-763e-3b66-8300-ed625e11982c | -3.53079 | -54.17535 | 2025-10-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a38460e-c880-3b9c-825f-223c67ff35dc | -7.08847 | -44.26999 | 2025-10-17 05:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcebc5ef-cdf5-3da9-8144-0c425a93b7b3 | 1.79145 | -55.88501 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64b99901-50cd-3927-b276-ab776686aef1 | -4.60699 | -50.91683 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bfb49d0-0c4f-335a-b498-54f8e40328e3 | -2.73954 | -49.38268 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 337bb6da-311e-3f49-ba81-2aee695c2bd0 | -5.33374 | -44.47567 | 2025-10-17 05:08:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca109f1b-b4f6-3896-b794-d3868da031bb | 1.74879 | -55.76463 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c4a9e47d-0a58-3fd1-88b8-97d9695f9426 | -5.28383 | -47.92529 | 2025-10-17 05:08:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d96b999-f565-3599-bd3c-01cbf1c81253 | -4.30143 | -50.39932 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fc3f997-7986-3674-94df-9b5415c71454 | 1.88756 | -55.6549 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4951a3f7-0b5c-3856-b66b-d476a9a68671 | 1.86168 | -55.66246 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e8c844f-6457-36f9-bb71-884348496592 | -1.48574 | -55.68177 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99b779be-cc13-320e-85f3-977ee9ce8eb8 | -4.81413 | -45.73114 | 2025-10-17 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a69a210-0d8c-35b3-b362-87c3b3c96e62 | -6.39979 | -46.882 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a398429a-d7ac-3769-940a-7d4726b7c2d3 | -5.89761 | -44.75859 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 410736cc-cd80-3f3d-bab7-e807c264e01a | 1.83404 | -55.70198 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8127fe10-4969-3b3f-bd66-e0d601352bd4 | 1.83957 | -55.69408 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f090ef00-09fa-3039-ac19-d804b8dec65e | -3.23889 | -45.98021 | 2025-10-17 05:08:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25e5bcff-6c8c-3c4d-8ebf-08eb0190ef77 | -4.24952 | -48.56937 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b12388f-b0bd-342f-9aed-16f03b8290da | -5.74621 | -43.37887 | 2025-10-17 05:08:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 221375b1-5843-3c2e-9f67-06e7017cd168 | -5.87307 | -44.83803 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4981bcf8-db5f-3ce7-b23c-23e86f21a86e | 1.7405 | -55.7765 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c640d86-a95b-3a38-acd3-e26412a119d8 | 1.79195 | -55.90971 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4597f7ec-297a-3459-8707-9d80c0f7a98f | -2.8789 | -50.74234 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6181fa0d-299a-3e4c-a868-b07989445715 | -4.36759 | -48.71095 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f51ee7e9-5df4-3a12-82d1-7c9ef0bc0b58 | 1.85615 | -55.67037 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa7805fc-0fc0-375f-b45a-a88c75f1a148 | -6.20669 | -44.43092 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1ebc1f0-78c4-372b-80a4-a3fc569b523b | 1.7786 | -55.73885 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05e31a96-6f2e-3442-9122-812d2a514434 | 1.87381 | -55.65353 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77f2f6b5-cbec-37fb-9461-77cc4351800b | -2.70542 | -49.8586 | 2025-10-17 05:08:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c043d810-7447-38da-aa35-d9cdd86cf7a5 | -3.13258 | -50.2158 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15593b2b-bca2-3cf5-9964-cf6c89dea903 | 1.10089 | -51.14377 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b1065d2-50be-3595-950d-092747451829 | 1.01475 | -51.15942 | 2025-10-17 05:08:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a33dd644-4c59-303f-a4f1-c9047cd2152f | 1.74825 | -55.76118 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6d4f8a8-5407-3867-893c-a91ef7f2b806 | -4.40682 | -43.39293 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 802a5321-4ec5-3ccf-8a44-7dd4ceba7ceb | -3.81818 | -52.34575 | 2025-10-17 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5268be48-8b99-3dbe-97f1-2079238ad3a5 | -5.49983 | -51.15718 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d39bc64-8b93-3326-bd2c-3d3e8774adb9 | -2.69721 | -59.43049 | 2025-10-17 05:08:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a97782f-3571-34f6-b3f7-9d78889591b5 | -5.46168 | -44.64671 | 2025-10-17 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17a73448-1f2f-34f6-9402-2135ba7a95a7 | -3.51268 | -52.49056 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec4c510e-a907-372f-b3a1-0bfa2142217f | -5.88469 | -43.90459 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37cfc3b5-c5ba-3567-a509-2cc3c064c642 | -6.32305 | -43.62634 | 2025-10-17 05:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a6df6a8c-745c-3035-8dd1-4c2be3511ac6 | -5.59531 | -50.05862 | 2025-10-17 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b11bc79-dba8-3976-82df-38157cd92a0b | -5.23562 | -49.22737 | 2025-10-17 05:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cdf6d4a7-836b-359c-96b8-a264fe9a9899 | -4.56143 | -46.62603 | 2025-10-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 701bc770-c877-3332-9fa7-90b80d281593 | -6.29156 | -45.52605 | 2025-10-17 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cca0ff49-ab81-3d1b-a173-485a9ca357a0 | -2.70688 | -49.41152 | 2025-10-17 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a77bd11f-8705-3efa-ba3e-95eef2e8b55e | -2.50479 | -56.20085 | 2025-10-17 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc0a2db9-3d4d-3b65-ba78-b756e1f362cd | -3.47069 | -51.66613 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08cccc83-4015-309f-a1af-a2b00065fee1 | -4.381 | -43.38266 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14622488-34f4-319d-bea6-dfc7477b8e2b | -2.95447 | -54.63169 | 2025-10-17 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb11fd2e-6856-3c5a-a8f0-13f3cbc41103 | -6.58624 | -47.07516 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7b1feb8b-9504-3298-99c1-65ba2dd50b0c | -1.88804 | -56.9441 | 2025-10-17 05:08:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f054ef8-68a0-36df-8cb4-219e4ef2f994 | 2.05439 | -55.74183 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1e0c2ad-63a9-328b-b52a-bea7e19b6585 | -2.87107 | -50.73722 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86b42f7d-a7cf-379d-895a-6af62555bac9 | 1.82743 | -55.703 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b5564a7-0f32-3374-9f49-869d2c68fa62 | -4.04333 | -47.50107 | 2025-10-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64d35127-6f6c-3e1d-b00a-720cb9810c76 | 1.78364 | -55.92162 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb41e2d7-89b3-3f58-95e3-70782240c415 | -3.47654 | -50.0249 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 250d55b0-d1d7-3524-aad1-14ae5fe8897f | 1.78087 | -55.92559 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 333e59f6-8916-3cbf-bb5e-3796f808de3a | -3.53695 | -49.01201 | 2025-10-17 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0f7532f-9973-33d7-bf13-3badab813698 | 0.33001 | -51.35632 | 2025-10-17 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 516ed8f9-fbf3-36e2-b27f-1ebf11ad116f | -2.7983 | -48.94105 | 2025-10-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb95fae0-4786-30cf-82e9-be87329644c5 | 1.88328 | -55.60629 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a0e2423-7d37-3253-a109-1ddaa7ef0052 | -2.7092 | -49.86366 | 2025-10-17 05:08:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c37706d4-1300-3f9b-a75d-6034d724d449 | -2.94619 | -47.31447 | 2025-10-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 857cee8f-47e0-3abe-9fc2-80b70f6aa041 | -3.50512 | -52.48937 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |


[Clique aqui para ver as próximas entradas](README105.md)
