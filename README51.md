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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3f66936-b574-33e0-846f-e4fb4bf665a0 | -4.04284 | -54.23528 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9da0599-00db-33c2-b15c-25cec8500011 | -6.40969 | -56.40673 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aab2115-fa94-3e2b-a67e-403bf7fb7073 | -2.96478 | -54.10055 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc2464f1-774c-343a-96ad-86b9c796dc93 | -7.2832 | -55.59299 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85243101-fc22-37b3-bc74-b72026a89bf5 | -8.18464 | -54.79182 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e06a1a-6b49-3ef1-a939-9fa419e1da7e | -5.30097 | -55.87342 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6ec4a52-6b68-32b9-9d49-ee146a0cdd93 | -8.26703 | -54.74518 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff622497-5570-3210-a21c-d7ca168ac869 | -2.89495 | -54.11081 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc3265ef-0a07-3ddb-9fe7-80498eb37948 | -6.2148 | -53.26096 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbf16a49-fe0d-3de1-91c2-42bc5f948433 | -8.04292 | -50.11686 | 2026-10-02 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38182729-1999-3f4c-ac3d-2b7c99fab7ac | -4.99296 | -56.15044 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f33f893d-ccbe-394b-b5b4-337b258b409c | -8.91496 | -49.25873 | 2026-10-02 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3165f3e4-20ca-39d6-a152-3ff791a059d9 | -6.26327 | -55.43408 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0f30f1-d069-3022-aca4-855a39737691 | -7.75212 | -49.20181 | 2026-10-02 04:57:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df221245-1fae-39ed-b5e3-813a71bb01d4 | -3.01574 | -53.88326 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68f9d1db-1c1b-3f20-9dbc-907bd10373fd | -4.28965 | -50.77951 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6c332d4-d5e2-3552-a1e3-e8738ea232b6 | -8.16598 | -54.80308 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 898b879a-279d-3097-94c6-83c1b7eaed6a | -7.87883 | -44.17759 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 64a4b5fd-b900-318b-82b1-6a1b11435d8e | -4.27902 | -50.75237 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e769056f-b093-33ee-8942-92b6f2695bd0 | -6.23727 | -53.13749 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbaafdf0-0b29-36ec-820c-80e0d5200ed4 | -2.89393 | -54.13889 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a7efc31-a49b-3f61-aaab-57f403525bcc | -7.65991 | -55.10225 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9209752-0103-337c-a290-cb1ea620f635 | -6.40127 | -55.20803 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9266e70e-671a-339d-b52e-f4cf8b17cb8b | -3.03438 | -53.87208 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65c02d6e-85c9-3077-8b70-4ace75cfe00b | -6.902 | -43.68205 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73643836-3659-3348-86fe-0e0465b03d02 | -7.88546 | -44.17788 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b27a90be-5d2c-3482-ab2c-6ec832d29637 | -3.44222 | -50.26741 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87e650e2-ca3b-3475-857e-c8477ba6a280 | -3.29059 | -53.84227 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 745ac01c-04ce-382b-b799-befad4caa494 | -1.8673 | -54.88741 | 2026-10-02 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6ca072b-e396-3d84-8322-b342ba6ba7aa | -7.72909 | -54.81178 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7990e119-734c-3415-8c10-879918485cbb | -2.39428 | -56.99133 | 2026-10-02 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14085cc7-5f01-3ef1-9c54-ba7a44e3eb71 | -6.90144 | -43.68636 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1394a4e7-539e-3893-a58b-819ccc4a825c | -3.13243 | -53.74741 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b36f5f1c-eec6-35fe-9936-eb68da42a3dc | -6.20041 | -52.80532 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d12f9a0b-9f71-34e2-89ba-6b6851262154 | -3.02489 | -53.97602 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8c3d8e-78e8-36de-84c0-07757d97c638 | -6.12578 | -53.19965 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 032afea4-8573-3437-aabe-151db85ff90a | -5.85042 | -53.48441 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a66dbaa8-cd4f-3121-8200-751556983ad4 | -2.96532 | -54.09711 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e08496c-130c-3559-9e99-9bd0a8cdf5d7 | -7.8393 | -55.13123 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7880f3de-23c4-3ca0-b569-b439c9cd3ef1 | -8.24129 | -54.78015 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13e404c8-23a3-31d6-bf80-82c7ef09dca5 | -1.64508 | -55.13477 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c78447d3-cc5c-344b-93c4-4346370da72c | -7.27765 | -55.58492 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04a9e686-9602-30eb-89f2-c33785de6a71 | -7.6847 | -55.11683 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 574286b8-7148-3b42-a398-6038c4524920 | -6.91451 | -43.67925 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c5cf48de-81eb-32a9-bbf6-bdd926e7d42e | -7.83764 | -55.1203 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33a26230-3310-3092-a965-d86e38331419 | -4.36243 | -47.77581 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4f8a2097-9fcc-390c-8e25-184f22e8d615 | -7.49686 | -54.99066 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 713d1808-8545-3c7a-92f0-d9b96ad187d6 | -6.40686 | -56.40246 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5e499cf-6f52-3c8e-8e72-9c8d431718e9 | -4.27007 | -50.73832 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e66b9af7-7081-35ee-8eb9-e597ca8defa8 | -7.83434 | -55.11978 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30a26845-6062-39d0-8ab0-32da0cce347f | -6.70112 | -56.14653 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19b30fe5-bcc1-33bc-ab65-d54a1cd58a65 | -2.86196 | -54.12691 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d9d862a-7c19-3538-bbef-7fc30d882e7b | -3.01298 | -53.87932 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b9970dd-9a94-3639-bda3-e56fd6493290 | -8.16057 | -54.83769 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0706984e-8b10-39a5-b7c7-e402b7a46473 | -4.39413 | -49.95881 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 722c9d17-d0d5-3077-995a-89f68d97ca2d | -4.26523 | -50.74599 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4f7d16cf-f662-3e17-a426-5ecef240c607 | -4.26806 | -50.7762 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72579c1a-ffb3-33a2-8758-d69b266a53b5 | -5.37609 | -56.05841 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a102273-f08f-303d-95c0-57081c8358ca | -3.58829 | -54.52792 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aac4e85-38d6-3236-8dee-aee22ffddeaa | -5.47898 | -45.86668 | 2026-10-02 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1388d40e-3262-37c1-9e2d-2efd78b3fd6c | -6.19028 | -52.80388 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72d8b360-b9fc-31a2-a8f7-1465a7572945 | -4.28308 | -50.7743 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d7dbe32-f337-3574-b3b0-a218a758749a | -7.69346 | -54.8451 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce4a1361-63c3-3f89-9bea-c3f1471e1a21 | -6.9033 | -52.50138 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed584c3d-f93e-385e-9946-7d82cff83cb3 | -3.00308 | -53.8778 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f594bf9-6a6b-3b8d-91d1-a03a249879a7 | -5.85705 | -53.48547 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bbc0343-0ab6-3714-996b-561fa958abc0 | -6.68403 | -55.33542 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ed70fe8-3634-374e-a5ab-99cdb83e2c15 | -6.67682 | -52.49139 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d6ca40f-2028-313c-a5eb-8d58cc1c0274 | -6.10739 | -55.6862 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e084948-aa3c-3c48-892d-709058646a75 | -4.0646 | -51.09257 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1848772-3064-3b49-9d9b-46ea51413e43 | -3.00536 | -54.23038 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ab6e4c6-bea2-3089-8d10-0f79d70d7982 | -1.63713 | -55.14103 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5020cca-f90c-3dfd-9ec3-e15b15a54b45 | -7.41966 | -55.58993 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3602790-2b85-3e24-b883-f36b4cf78384 | -3.97942 | -41.51676 | 2026-10-02 04:57:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0920e132-4cd0-39c3-8c01-0ecaa03cccab | -8.17312 | -54.80065 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23224b74-98f3-3d97-ba8e-9f8aa5988ba9 | -7.72573 | -54.79 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 237dde7e-4426-3e87-822b-0a47855132a1 | -7.41244 | -55.59242 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b620a259-1d1d-3e9d-bdd3-0a47edbe3928 | -3.0086 | -53.88568 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0431d35a-9c96-349c-bd31-327699e56504 | -7.33773 | -55.22499 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cf12582-161d-30ae-8285-4f05e052d4b4 | -2.89231 | -54.14923 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b815c008-bbde-3bf0-8f4c-7fb7f027912a | -8.19888 | -45.51916 | 2026-10-02 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32233e85-9fdc-36e8-9c5d-695a554dc89f | -8.01611 | -47.43146 | 2026-10-02 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2e8a2e84-fd4e-3c3f-9370-bc3cc1bbdd97 | -5.8964 | -53.49507 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| deeab3b4-cb90-3be3-bd81-fd21281e675e | -7.54977 | -55.02448 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b38014ed-8b30-37fc-9139-085c82ec9a27 | -6.11461 | -55.70564 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e81ddd85-20a2-32bd-ba6d-f66ccf0b36b8 | -8.16928 | -54.8036 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83170cf1-6a94-30bf-9b99-87fb9cf67f8f | -4.27885 | -50.7779 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ad39921-bdcc-35d3-9a3b-584bafa41c32 | -6.44554 | -51.70481 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dfdd0a4a-e45e-3fec-98f7-f15364145b38 | -7.51348 | -55.0401 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffb4cb71-ff12-3537-bae7-b7821ef413d9 | -2.84213 | -53.98986 | 2026-10-02 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69798f59-9f07-3216-88c1-f298b971c54a | -3.12128 | -50.26079 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cc9e884-709e-3e45-a490-4a5d711d7d7a | -2.89285 | -54.14579 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a3490f60-e7d8-3c27-b9df-ffd682018d06 | -5.73748 | -53.61967 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8d44c64-91f5-308e-b720-1fac14b5a772 | -7.63504 | -55.04508 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aec7303a-82df-3453-b2e6-4c9f9c32d8a9 | -2.46156 | -56.07645 | 2026-10-02 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1864cc0f-3db4-3aba-b3da-f94218a5aa5d | -3.58884 | -54.52446 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 625b404b-b0ac-3583-a8a7-6067b13d3076 | -8.25027 | -54.65748 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3c761a4-b8ac-3be8-a703-b6fe0c395967 | -3.02212 | -53.97207 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f4a71842-af4b-3648-994a-37056f943161 | -2.57759 | -49.99416 | 2026-10-02 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af7ee952-28d1-39d9-b887-2dff13b1d4b1 | -3.84919 | -55.96645 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README52.md)
