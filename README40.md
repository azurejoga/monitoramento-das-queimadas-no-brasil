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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69f838b9-472e-3d82-9b3d-e1cf8bba9839 | -3.37651 | -50.84757 | 2025-09-07 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7d7dfe2-ae60-3c05-894b-adbb73cf6f7b | -5.55751 | -43.77503 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1e1ccf7-7494-3ceb-b188-9d66dc40e1d2 | -5.64584 | -43.11895 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7ad16a3-7f2b-307d-aabc-dd8a9f4a91bf | -3.24359 | -50.79863 | 2025-09-07 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f99e073b-5aff-3814-ab06-6399f06a3a47 | -2.84789 | -49.51009 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78698faa-fc0a-3da9-b1e8-300d7a2c20a9 | -4.2573 | -48.5471 | 2025-09-07 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a8e0553a-b817-31fa-a387-31163d903883 | -5.0361 | -45.31567 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a44c5168-9500-3b5c-8504-6f4222da8fbc | -5.32689 | -42.68805 | 2025-09-07 04:17:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4d278fef-0cd8-3138-bd42-2ad5779ca6af | -5.37625 | -45.9781 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d795e2e2-f500-3e9c-a0c5-ab9b5d012a8b | -1.62688 | -47.05242 | 2025-09-07 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58a01f7a-0352-30db-86dc-6aa17cd98222 | -3.58951 | -47.51683 | 2025-09-07 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f09f2c0-e3c3-31e9-865b-11e96b7bb086 | -4.1721 | -42.02385 | 2025-09-07 04:17:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9704b17c-133a-316c-9c51-f3b8701357cb | -5.21975 | -43.69746 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7863b760-12fc-3884-ad03-1cd61fc155ae | -5.45469 | -42.81546 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b41c0804-1c96-3e2a-8a98-6c188ff483dc | -4.17094 | -42.03138 | 2025-09-07 04:17:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 12b6ec8b-552e-35dc-8ebc-f986befb266c | -3.24661 | -50.80871 | 2025-09-07 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b750ef69-591a-37a1-9869-730baca2dc83 | -5.36186 | -42.64403 | 2025-09-07 04:17:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f2153aa6-f57f-3912-84e1-8a96dba4c8a5 | -5.63158 | -43.65047 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07ecc33c-bd8a-39cf-9167-a4b2081185ce | -3.32592 | -54.90922 | 2025-09-07 04:17:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2359a0d-8965-379a-991f-725c4bdf5a1d | -5.7597 | -43.12894 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5f174645-9f7d-3c4f-96f4-bbc8459f0626 | -3.78786 | -48.91515 | 2025-09-07 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d85ee019-a66b-359f-b388-be9eaed95505 | -5.0304 | -42.45428 | 2025-09-07 04:17:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 443e9311-74f1-3f84-b7e2-35a949a26681 | -5.53464 | -43.09062 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70a93789-78ab-3297-a15b-fc2643e07adb | -2.82073 | -49.19793 | 2025-09-07 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 329f5cfb-274d-307b-b9cb-2d5950ce486b | -4.88931 | -41.75507 | 2025-09-07 04:17:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92f1c6d9-a89f-3e3b-9b65-0ecbb49f4b6c | -5.03554 | -45.31919 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 617af11e-6fc0-3261-937a-b08858bd53a2 | -5.2131 | -43.69643 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96b158d2-06db-355a-a9c5-eb14084a57a0 | -2.84852 | -49.50627 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9dc79f7-7ba0-3c09-b0f3-1b073ba57489 | -3.82072 | -54.12218 | 2025-09-07 04:17:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97857e36-8fc5-3f34-86f3-1cfc3ab1d7e2 | -1.28778 | -48.43643 | 2025-09-07 04:17:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f24fabe2-ad07-3eec-90ee-356725f842ae | -2.31762 | -49.1682 | 2025-09-07 04:17:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fed52cda-983b-326d-ad22-0113948f6659 | -5.44055 | -42.81701 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 300c24d3-44b5-370d-8838-0d8a907e2b23 | -3.78294 | -44.51904 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ed250fc-8d8c-3919-b728-f8564f3fe19a | -5.1771 | -43.10591 | 2025-09-07 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 679df5b2-e722-3dd8-88ee-1a7eb0007cc6 | -5.86482 | -43.24097 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02b31cf1-7d9f-3303-be0a-a6a65786e164 | -2.55076 | -48.39093 | 2025-09-07 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba490e0c-30b5-3b0d-b756-b75eae177765 | -5.73109 | -43.90238 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2252b5e6-f48a-3f35-8910-ae5971c90527 | -5.21588 | -43.70042 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 536f5bd6-c654-3bf8-9cd1-0564fa9c5a56 | -2.85271 | -49.50693 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4730f4a-2125-36f8-831e-3d6389f2515c | -3.3252 | -54.91349 | 2025-09-07 04:17:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f87805c5-1de5-3dee-9c2f-06a7a6d47b32 | -4.32863 | -48.39143 | 2025-09-07 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c06d5110-7ceb-3174-967a-7a89da8c6de2 | -5.04425 | -45.45362 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a0ae841-b34f-38d2-a900-248bba446acd | -4.27003 | -48.18341 | 2025-09-07 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4b16891-61f3-3db0-9aa0-c7e8711bd0d0 | -5.53182 | -43.08648 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb0f8a1a-8032-3466-bd82-749d089a6221 | -2.85175 | -49.50708 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b693ed0a-d38a-3135-b714-c4f59f4a5751 | -4.677 | -41.01576 | 2025-09-07 04:17:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 08a4af15-72bc-35ad-b1e2-967fc86ddd16 | -2.78564 | -49.62341 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0755059-c9e5-3ba3-bf10-1268404e4b61 | -5.03277 | -45.31513 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2301b882-4523-3728-aaf6-30993c9ac81b | -5.55595 | -43.06443 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6492922e-cbfe-30dc-aefd-dc704990ab6b | -5.53151 | -43.78888 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a720a6e-6db7-388b-b5a2-24bb6800296c | -5.35075 | -44.87331 | 2025-09-07 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47243cf2-0a7c-3c57-b3ca-61cd6f8187d6 | -2.90867 | -40.40416 | 2025-09-07 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c87e72dc-4d7f-3628-91a8-0d2fbe83a1db | -5.86458 | -42.42487 | 2025-09-07 04:17:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3970a428-bd2d-31ad-84f1-eb49522bf2ad | -5.54977 | -43.05976 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae8f3e60-7cd6-3fcd-8bf5-55f36193e32a | -5.31604 | -42.80236 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 36e17d3d-5409-3a11-8cf0-949b166c68d7 | -5.35366 | -42.65071 | 2025-09-07 04:17:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| eb139d91-88a1-3cca-9717-e4f6db8f47bc | -5.2015 | -43.70533 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2b0c6f2-35d6-331b-8a16-ca6307dca20c | -5.4379 | -42.80596 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e8061652-ef05-33e1-aa96-4dac4accdd2a | -5.74716 | -43.71178 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 472fcf59-cb4a-3de6-b730-2126f25955b4 | -2.87708 | -40.29868 | 2025-09-07 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ca39e580-01b8-3c8f-8ae2-11a90a08a254 | -5.63213 | -43.64697 | 2025-09-07 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3e0969d-9bfa-3ffd-a144-2dd9adf4be84 | -5.37459 | -45.96672 | 2025-09-07 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6666b6fe-02e5-3402-9d23-ee6fa306a649 | -2.87639 | -40.30306 | 2025-09-07 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb92b024-ba5d-3a31-bc9b-416fc369434a | -2.42949 | -49.30473 | 2025-09-07 04:17:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c5e0f32-16b4-36bb-bf4d-3f4b479002ce | -5.45242 | -42.80763 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c3b09b4b-3c10-3ce0-84cf-e2ebd2111932 | -5.59336 | -45.12169 | 2025-09-07 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed4573b6-b566-3ef5-a402-678d6c92bcea | -5.44386 | -42.58857 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e59b6eff-1ab3-3ba1-bfe7-166b0214ff76 | -2.42888 | -49.30852 | 2025-09-07 04:17:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3f05e4a-18fa-3267-99ad-3ee33d525cad | -2.81602 | -49.20094 | 2025-09-07 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb6a7442-72ff-395a-8f52-d74ae1c7b984 | -3.41962 | -46.96635 | 2025-09-07 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d42b02fe-4352-35cd-8de5-94062ffc58ba | -5.51303 | -42.66291 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a3bfc00b-62ad-33f5-9faa-2a37395759d8 | -5.20035 | -43.69085 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7000e222-79d3-38eb-b43c-dfe2d2321561 | -5.72777 | -43.90186 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb901ea3-80e9-3283-850f-4f230cce0533 | -5.40084 | -42.32607 | 2025-09-07 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fb8a5269-4ebc-34db-876c-5a6f789799a8 | -2.88078 | -40.29925 | 2025-09-07 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1928f3f-2f67-369c-a512-d693c92e27cc | -2.42828 | -49.3123 | 2025-09-07 04:17:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 040c6f22-ccae-3859-834a-ac88a9f9e13c | -5.5895 | -45.12463 | 2025-09-07 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2a8026f-426a-3011-9778-3218b2508b52 | -2.91863 | -48.67414 | 2025-09-07 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7fbf4c8-13dd-321e-8cef-55e5ca174ca8 | -4.3293 | -48.3936 | 2025-09-07 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ac19721-d1d2-3639-b9d9-70f3cc4f012c | -5.83668 | -37.99685 | 2025-09-07 04:17:00 | NOAA-20 | ITAÚ | RIO GRANDE DO NORTE | Brasil | 2404903 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e33045f1-d2d6-337b-8c0f-b8806b567dce | -5.72445 | -43.90134 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633c9e61-f250-3927-b018-083225debfed | -2.42533 | -49.30405 | 2025-09-07 04:17:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6429ed53-beed-3aee-b0f0-8146f4dfabf5 | -1.79076 | -48.07402 | 2025-09-07 04:17:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa0a42eb-f850-3435-aefa-6d3800edbe02 | -4.29188 | -43.35609 | 2025-09-07 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ff52b8-b6d5-392e-92fe-e1aa9ee063a0 | -5.44902 | -42.80709 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5c2020aa-1b95-3d63-ace4-f71023eb0e35 | -5.81128 | -42.47921 | 2025-09-07 04:17:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6cdef939-4af1-39d9-89f6-8a0cff46ddde | -3.24737 | -50.80407 | 2025-09-07 04:17:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 866c5f0f-0994-30ea-bc43-4a19596ca880 | -2.78627 | -49.6195 | 2025-09-07 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fd799f8-b795-382b-b228-e4ac4d997850 | -5.20204 | -43.70184 | 2025-09-07 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5043a7cc-b7ff-3cf6-9371-5f523c6afb68 | -3.78349 | -44.51559 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0144d0e7-4985-38bf-a80a-6aa6255b49e4 | -1.94213 | -56.59586 | 2025-09-07 04:17:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58f1c033-4eef-35a6-bed3-dae97d7b05c8 | -3.20896 | -54.96729 | 2025-09-07 04:17:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 85cb0cd1-9d22-3b37-9590-9483c6bac17d | -5.55651 | -43.06081 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89759560-9085-35cf-9a1a-354c0ba14eba | -5.73278 | -43.91334 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3766ddf7-4dde-35cf-bc9c-1ff813ce297e | -5.44129 | -42.80648 | 2025-09-07 04:17:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 56e4c9f1-eefc-3302-9a2c-c29a7a39cc24 | -5.24578 | -42.71679 | 2025-09-07 04:17:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 28b4d764-cfdd-3f38-8ffb-dc6f60a28791 | -5.75492 | -43.70579 | 2025-09-07 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbd68960-57cd-3fc5-81de-6a238d0dd501 | -5.03221 | -45.31865 | 2025-09-07 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 649bc70f-70bd-372d-98bd-9aaa53c96181 | -3.62568 | -49.19777 | 2025-09-07 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ce17e66-55d4-3922-ad91-92fe9e092187 | -3.78625 | -44.51956 | 2025-09-07 04:17:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
