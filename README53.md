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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 250f14cd-4f1f-3a86-99a8-2753808892af | -8.45491 | -54.71691 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c4b9e062-214d-3861-87b8-159652d49c75 | -7.66651 | -45.87318 | 2026-09-02 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa586afa-c837-3736-b795-09a28601fde9 | -8.45428 | -54.72114 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5ebb2953-26d4-38ee-9c77-760b4024ef0e | -3.76082 | -59.33508 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edea18a5-829c-31c0-8c46-dd7273d1f91a | -5.97171 | -57.68288 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c99b6bb-2873-3db7-9d50-9fee8bc368fc | -5.95186 | -57.67974 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e0ddab3-703d-381c-bbf9-20d5867990bc | -6.05471 | -53.83831 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11364d75-c4f4-3769-9998-6d237e299fec | -3.36158 | -59.40516 | 2026-09-02 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ca22dda-4aa3-3188-b3e6-b512c8e37b60 | -5.9072 | -53.56631 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e123453e-5dcd-37e7-834f-b72a200e5184 | -3.61717 | -60.55611 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d685a91-c5c0-36a6-a468-0b342730598f | -2.83908 | -49.51152 | 2026-09-02 05:16:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0515eb1-6c0b-3fd5-b9da-5a6c476fc785 | -6.92326 | -59.64285 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cb0434b-04f7-37f6-af02-78c2f90aebc4 | -6.80718 | -46.20053 | 2026-09-02 05:16:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 847e63e3-c8bc-33b0-8eb5-ebc91457a3c5 | -8.44825 | -54.71154 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc528838-5f69-36b2-9079-cd9b4a64546d | -6.18154 | -57.73072 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a951c939-8470-351d-a7ff-66a2271a0c04 | -3.97091 | -60.03138 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d12e366-446e-3532-8c54-6076983ddbdb | -7.36214 | -60.60834 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06251c56-40fb-3f56-b85b-6a7d27e38999 | -6.76089 | -56.33696 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0fdf700-d612-37d3-89f5-246506e36961 | -8.46947 | -54.7191 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8df4668b-f6c1-36d9-9347-ec717bfd3bbd | -7.2927 | -49.81938 | 2026-09-02 05:16:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a46b4f1-aaa4-3c6e-8b64-74c3430bd411 | -6.10925 | -57.86421 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff4db1de-1e6c-37f0-9a56-7810670e6710 | -7.44255 | -61.41616 | 2026-09-02 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02c0414d-89ea-35f7-9a30-7ffebaf13674 | -7.20309 | -60.67029 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77402fc0-3084-373c-b135-a383aa77ceb2 | -3.61967 | -60.5546 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1327d251-b2ae-3ddb-8a39-eead492777b9 | -5.8718 | -57.77652 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bc77670-df92-3289-a2e0-784de62b7c3f | -6.75618 | -59.44122 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6d1c080-114d-339f-bcf6-e8a5dedf089e | -6.05557 | -57.64663 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0418589-f1e6-36a1-a98b-3ebfee772905 | -6.43656 | -53.56738 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d70a65c2-cbae-3fd4-b1b2-21330124d883 | -3.65284 | -58.91608 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee40386a-ad1f-3ede-b026-2dd0bc3c4d41 | -6.32263 | -54.75362 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5deb6d69-affc-3b7c-9c89-e1a9cc666bcd | -7.25366 | -61.10864 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b79db151-c4af-3f90-a983-38033fbca966 | -6.07307 | -53.66779 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f866d0f-637f-3ffc-8a91-fb4dbceadcb4 | -6.11731 | -57.64223 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29e245e4-34d0-39fe-afbe-68756ba728fa | -5.50669 | -60.14451 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0e4f640-9656-3340-8710-5990b1d4cf61 | -7.18547 | -60.68813 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e37c467-0fca-33cd-b88f-7b04e1b67aa2 | -4.96749 | -55.84185 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82f69eab-9983-3b95-98af-83b51bb5ba08 | -4.34555 | -55.45089 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0e50d8d-df95-3eb4-a7f5-0512d3039443 | -3.60179 | -54.55253 | 2026-09-02 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 084e2c69-72e9-349c-b1ca-9a855c4ebf1f | -7.35548 | -60.58232 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2ea8740-6af8-322b-9da1-9988fa7a8cdc | -8.47122 | -54.73246 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e3fb008-d1ad-3af8-bd00-3b923c1826e6 | -8.44575 | -54.72855 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39fc7b4f-641c-3d7b-aefa-ea1335d12366 | -6.73622 | -56.34057 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a3ecbc88-666f-310e-b4b8-031da5e4969d | -6.1331 | -55.64559 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5cec97e-d71a-38c0-8615-a4a61589f860 | -6.19826 | -55.4264 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7a8fa10-a4ac-36cb-a4f7-107bb09fb316 | -7.26868 | -60.62714 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e92f3291-5b91-3631-9831-fcd932f893b5 | -8.70532 | -52.36702 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59e9e494-54cb-3917-b09f-23235be0e8f5 | -7.34552 | -60.57656 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b985cd-927a-3474-8dd3-ba28ccc682ba | -3.18712 | -60.15356 | 2026-09-02 05:16:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 196a96b1-c591-3781-95de-03b950a6c1c7 | -8.44833 | -54.70953 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f07ce421-d661-3479-8446-04cf365c9645 | -3.61648 | -60.56049 | 2026-09-02 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 889b64c7-cd0f-3182-8c20-062084dc12cc | -8.42949 | -54.71099 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d5e19fc3-c8b3-3ab6-8f41-63fd515187cf | -8.47185 | -54.72818 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 051c474b-5055-36fa-8b04-e3b8880b6210 | -6.81871 | -58.8721 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c53d1929-f3e9-334b-96d0-788be3b729aa | -6.88776 | -59.45074 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52f7eee-648b-3db1-ba53-837e0509a007 | -9.42151 | -45.62794 | 2026-09-02 05:16:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a3557a3-4815-3c9e-a6ff-a63a733595e2 | -6.14622 | -55.67408 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37ce6f1d-c5df-3cff-855f-f6530868d97c | -6.14337 | -55.66988 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19296c6a-f14f-3771-a1a8-6edd7bcb6a24 | -4.11567 | -51.03038 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 238c9531-4772-33d7-b3cb-2fa4b1edfd49 | -5.56755 | -60.21547 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8aeae3d-d81f-3ca9-bac5-2b79e9a78267 | -6.87975 | -56.50525 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cded22e8-9f5e-36e6-8334-4e5626fc33e5 | -5.33514 | -60.15117 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1057dc08-4bef-3047-b50c-7caaaf3caf93 | -8.28639 | -54.9144 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77f8d086-770a-379d-9a29-4fd7042c4308 | -5.98093 | -53.58733 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 273c7a61-b741-3503-92b9-e69feae3916f | -5.25545 | -55.9075 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80ae9442-80dc-3ea4-a2f2-e0763187c168 | -8.46157 | -54.72222 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c1f496bf-aaff-3280-8c42-5ae115fd050f | -4.96974 | -55.84953 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bb5300e-e4b4-3d04-8259-b14782794a3f | -3.83151 | -59.39298 | 2026-09-02 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47f2ee0b-418f-3fd6-9dd4-f4758f53ad34 | -8.47626 | -54.69844 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bd9d9bb8-172d-3cee-abc2-890ab5b2faa2 | -1.50566 | -54.9646 | 2026-09-02 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 374b03b4-75ac-3028-bd7f-929be0cf50ab | -5.8707 | -57.78343 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe1c0f85-133c-3ed1-8bc9-7f14aa0ee02e | -6.76641 | -59.44283 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22d8086d-af2e-32e9-ae5d-9f3fc64f863d | -3.09626 | -61.18914 | 2026-09-02 05:16:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00a160c0-9e16-34c2-9677-3d3a73f66a3e | -8.71798 | -52.36883 | 2026-09-02 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8339c304-abfe-33a4-8b2a-fe1dcbbfc7a4 | -6.43415 | -53.55781 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a6c37f9-92e1-3f7f-aa70-7daf283d8a0e | -6.15249 | -55.67872 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59fd0703-95bf-30d7-87ca-85f74eb618ae | -6.94618 | -56.45354 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc86b7d8-de61-31f4-8be0-59a38c8805b2 | -3.65626 | -58.91663 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5650e478-e8d2-38fe-a8f8-7e326202ca76 | -8.46708 | -54.71012 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 64a91a92-a5bc-3171-bded-ee452b068a65 | -7.19596 | -60.66916 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1162654e-e464-3b87-aa8c-cef8d0aaf39b | -3.66287 | -58.9172 | 2026-09-02 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ad3d58d-2e9e-3efb-8da0-a517d64f2369 | -5.25489 | -55.91109 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 552a382a-fa94-3505-8244-cd8327b67a1d | -5.94745 | -57.68613 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b19f6212-4b03-3fc1-abb1-3f521d3bc7ab | -4.12495 | -51.02739 | 2026-09-02 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8864ff13-ecce-3720-b0e4-ea7335a341df | -7.34198 | -60.57595 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adb9aaa3-8960-3303-9ce3-3c466e4f1bca | -4.96862 | -55.85671 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b974615-dcf1-3938-80e2-7b15a05c14f5 | -4.36674 | -47.77697 | 2026-09-02 05:16:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| b088f3b0-16fe-3893-a781-756c31188e7c | -4.96805 | -55.83826 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd3fb792-2705-39f6-ba2a-56b675777ad2 | -6.2492 | -55.48435 | 2026-09-02 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ea32c9d-3654-36ce-b02b-8de87380d237 | -3.37452 | -52.79293 | 2026-09-02 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13a0768c-703f-39b3-9538-ef43716c8a23 | -4.35158 | -55.02876 | 2026-09-02 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49761bdb-a35b-31c2-bc8d-47778fad6168 | -8.4495 | -54.70301 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef361802-e405-3d25-ae47-effbd6487af6 | -6.91519 | -59.6492 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b898adf-da24-34a9-93b5-374e50371781 | -6.68312 | -59.09291 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ee5bee9-f8ca-3ac6-8f2b-21f6de235515 | -6.8751 | -59.39974 | 2026-09-02 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d1cd344-9495-33fd-a7a3-87b22205bca5 | -2.84097 | -49.51314 | 2026-09-02 05:16:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aad11f5-3a26-3adb-b77e-d5a3662cd3bd | -4.5878 | -55.94339 | 2026-09-02 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3273433c-1ebf-3040-bb99-a83abc550ad2 | -8.4573 | -54.72595 | 2026-09-02 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02a82297-619e-3705-9323-6114872a50c9 | -5.57792 | -60.19655 | 2026-09-02 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a287778a-b61d-361b-b73e-dbaa7d5c2706 | -6.13308 | -57.84352 | 2026-09-02 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 311e8ace-b18f-3bdd-a7ad-d3bc1bbbb876 | -3.54529 | -54.71983 | 2026-09-02 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README54.md)
