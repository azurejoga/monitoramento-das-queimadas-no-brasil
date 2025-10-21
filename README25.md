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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e63f9f4a-a4bf-3eec-b777-1375bf7d64c5 | -18.19047 | -52.98093 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9e35566-0fd1-3894-94d5-ec23cc285832 | -17.40568 | -55.05527 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 539b6ae5-71d6-3ab9-800c-10b84998fed3 | -17.68206 | -52.26178 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e675761f-da1f-35b9-8bc2-d7d5c519d43d | -17.40649 | -55.06559 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cdb525c4-d11e-306e-a0f6-7a5a4a4cc2df | -17.68233 | -52.27386 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4f85e422-b71f-3088-8f68-6d8870a6022f | -17.41752 | -55.05664 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49d142a9-15cb-3526-961f-a7cecbaaae66 | -17.68293 | -52.26732 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f9e77ca2-47b5-3362-a24c-279f3cad8ebb | -17.68094 | -52.27487 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9207826f-7d5e-35f0-82c3-a5bcbe3289a3 | 1.712 | -55.6854 | 2025-10-21 05:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3d4570db-fc3a-37fe-ad29-ce746c084554 | 1.712 | -55.6854 | 2025-10-21 05:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 08663be8-be4d-382d-97e3-c0cf5861179c | 1.712 | -55.6854 | 2025-10-21 06:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| be560263-e5ae-3cd5-9527-d23580a2bf08 | 1.712 | -55.6854 | 2025-10-21 06:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 312ed372-b115-3367-836d-b905893b480a | -9.4792 | -67.06664 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e27ddeb0-a678-3b82-aab0-60eca73545ab | -9.60041 | -67.17464 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46e497bf-e405-374c-bbd5-dbdd31c831f2 | -9.00182 | -65.93549 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af44c4b3-8fc5-3e97-ac0f-29afbabd919f | -9.00954 | -65.92286 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f7a7f404-42eb-3e43-9259-e966cc19f228 | -8.99154 | -65.92026 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2616ea26-4cae-3124-b1ad-ba1c9139182b | -8.99211 | -65.91574 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e354db8-e47c-38fe-aa20-23b6c29c53f7 | -9.00839 | -65.93185 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fedb6bd1-95a6-3770-a2d6-25b8b236b31d | -9.00411 | -65.9175 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dd1bcc7d-e539-3445-8495-0276c16eb656 | -9.11019 | -65.36612 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f45525c-9c08-322c-828b-bb38d76968fe | -9.59532 | -67.17004 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c438e775-00fc-3b91-8ca7-ebd4c1125ef5 | -8.64259 | -66.51426 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a0a154a-cfd1-3fcb-9ef2-63504a7c26d0 | -9.79825 | -67.02809 | 2025-10-21 06:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ebd36b2-305a-3c40-9402-4bad9f7b23d6 | -9.05036 | -65.7001 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e36729-9946-3ceb-9cf2-a0a59f77b038 | -9.11763 | -65.35701 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d551a8b9-53d1-3765-864a-1abee148ceb9 | -8.99811 | -65.91662 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1dfc3865-e863-399d-b238-1d0da151b298 | -10.07837 | -65.16824 | 2025-10-21 06:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8305f055-231b-3282-b73f-a0b379524c70 | -9.72407 | -67.48223 | 2025-10-21 06:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6eb62880-ead1-33c0-9f3c-a374eae61277 | -9.01554 | -65.92374 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08972772-6f80-344f-b405-c7a17cb86927 | -8.94182 | -65.92702 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 52523583-4fcd-3a8b-b27f-022c42cebc34 | -9.71859 | -67.48153 | 2025-10-21 06:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1baccda-fd04-339b-835f-f037e8dd0a3a | -9.11885 | -65.36177 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff1c29ce-e865-355e-9921-0ab1f1cb1ff7 | -8.9226 | -66.88713 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4df9ebd-fe36-35db-9475-57281c771a5c | -9.11198 | -65.36593 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac6122a8-2b4b-3ba6-8090-253c55c49353 | -9.04367 | -65.70387 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe66098a-9783-340c-9a5a-a0718493fa83 | -9.11702 | -65.362 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 75832814-7965-32bb-a3f5-a756c341465c | -9.00782 | -65.93635 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25b94dec-3b9f-3a24-953f-aa32a8c913d0 | -9.0024 | -65.93097 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0bfa6d1-840f-312f-a825-ac51cb4565ab | -9.00897 | -65.92735 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bff6d8d3-a4aa-31cc-bcf3-0f343bb9dfda | -9.10575 | -65.36504 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 611abe72-1c59-3028-b3a2-a473be0d644b | -9.71265 | -67.48438 | 2025-10-21 06:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1bed52-51a0-3651-9b76-35fd030f87de | -9.04426 | -65.69929 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dca3ef9d-aecc-39f5-8392-efae8c86e1e6 | -8.99582 | -65.93465 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db3f3cff-bf15-38e5-8dd8-b85ce069e098 | -8.99754 | -65.92113 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c076597a-ea41-309e-8e63-d8165bd6833f | -9.72318 | -67.48934 | 2025-10-21 06:25:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e056ec22-bbdc-3740-8bd3-999c8e35d7fe | -9.01382 | -65.93719 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e54be0a-968a-38c1-99d9-22eedefc3a95 | -9.01012 | -65.91836 | 2025-10-21 06:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d62f8fa0-58bc-36e8-864d-82a53a2cfc70 | -10.30796 | -68.86185 | 2025-10-21 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2caf4f55-6bf7-3e7a-a849-e4be7782be08 | -10.30757 | -68.86481 | 2025-10-21 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07194e05-874b-3814-ac17-77fbfab453d4 | -9.98252 | -68.85091 | 2025-10-21 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90a5305b-804c-3565-896c-f7bd8c5f913a | -10.30291 | -68.86124 | 2025-10-21 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 573d1ad8-ca99-31ae-a40e-3c46e14fef51 | -10.30253 | -68.86422 | 2025-10-21 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a60f29c1-0477-303f-a3ae-ddb11e611b8d | -9.97751 | -68.85016 | 2025-10-21 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73dcd548-98b7-3a9f-80c4-97064a38e448 | -10.30835 | -68.85882 | 2025-10-21 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98facec9-5843-3bc0-aa34-a5aff486cbed | 1.76301 | -55.67242 | 2025-10-21 06:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| fcc9116a-b101-3c39-a477-bd3fea333462 | 1.75284 | -55.66486 | 2025-10-21 06:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 373124e5-51cf-39b3-98e4-20905d8775eb | 1.69715 | -55.72498 | 2025-10-21 06:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 347ed979-0873-3dca-bb77-31811febf75f | 1.70948 | -55.68696 | 2025-10-21 06:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fc93a042-9e07-3d97-8049-08c9ef98c6fd | 1.69582 | -55.7161 | 2025-10-21 06:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46cd5492-7884-3668-98f0-9733f57ecc5d | 1.75417 | -55.67369 | 2025-10-21 06:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e196f915-c658-39d3-8486-f18553845d24 | 1.76168 | -55.66357 | 2025-10-21 06:37:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fff1cc5a-2443-3621-9d16-494fd9146911 | -3.31607 | -53.35 | 2025-10-21 06:40:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 58b5d0d2-b8fb-3ff8-bdc0-7bcf4612982b | -2.16859 | -53.48764 | 2025-10-21 06:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9fb0d5f6-b568-355a-acc7-d290335ee0f9 | -2.86127 | -50.7326 | 2025-10-21 06:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 372aaad6-cfe5-348e-95c0-39f9ee6b6240 | -2.92167 | -48.30732 | 2025-10-21 06:40:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 518cb566-6674-33f9-aa63-b364b926eb6f | -9.00282 | -65.91759 | 2025-10-21 06:42:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| a72c954c-a138-3d47-9e0c-9770aa275273 | -8.9985 | -65.92454 | 2025-10-21 06:42:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a42458ba-ac63-3cbf-b504-c3bce5a31c2e | -9.18392 | -61.38372 | 2025-10-21 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b1e5cd08-8f1c-38c8-86a6-0ea09e74cdc2 | -9.67713 | -63.17236 | 2025-10-21 06:42:00 | AQUA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 301d10bf-6469-3346-9fae-624850ed6cf0 | -17.40554 | -55.05649 | 2025-10-21 06:44:00 | AQUA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 0a87bcbc-f378-3dd3-be49-d5d521777a8f | -17.67807 | -52.25716 | 2025-10-21 06:44:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 6701e46f-fb27-3a92-a2e7-646a1630588c | -9.0036 | -65.9226 | 2025-10-21 07:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| d0e37d17-53ea-31ec-be6a-5540ffa3249e | -9.0036 | -65.9226 | 2025-10-21 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 0edfb82c-8716-39c4-901d-1c05e20e7cda | -9.0036 | -65.9226 | 2025-10-21 07:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| b55aeda0-4854-3beb-b0d1-1e2ef9503dfc | -9.0036 | -65.9226 | 2025-10-21 07:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 01d4749e-b7a7-3d64-a2a1-592e08c2a991 | -23.7369 | -51.8964 | 2025-10-21 07:50:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| bd27ecee-eba7-3769-a350-404b9af938ff | -23.7362 | -51.9193 | 2025-10-21 07:50:00 | GOES-19 | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.0 |
| 3f0b8126-243c-3fb1-8433-617e5988cc81 | -9.0036 | -65.9226 | 2025-10-21 07:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 296a64cf-1da4-3ad1-bd61-7461a3b26178 | -9.0036 | -65.9226 | 2025-10-21 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 165e5066-e983-34a6-86ab-8af9f94c7df2 | -9.0036 | -65.9226 | 2025-10-21 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 1b507c69-ff9a-3a72-aef4-c71a2493a953 | 1.4269 | -50.7449 | 2025-10-21 11:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 7eab4967-7205-315c-9002-db4f56fc089f | -3.03655 | -41.62831 | 2025-10-21 11:57:00 | TERRA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0b5ffae8-8f63-3821-a340-5d31170b4255 | -4.68145 | -41.02673 | 2025-10-21 11:57:00 | TERRA_M-M | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 26674e0e-4dee-31c1-8139-fa3e5f70cf1c | -3.49102 | -42.19357 | 2025-10-21 11:57:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 30521237-900a-343b-ad23-5af4192c99fd | -3.19303 | -42.40217 | 2025-10-21 11:57:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d45b14f1-bbab-3199-8d79-0f9042c27f27 | -12.62618 | -43.65562 | 2025-10-21 12:00:00 | TERRA_M-T | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b57b169b-80da-35cd-a5f1-82b80e67eebb | -22.03772 | -45.27055 | 2025-10-21 12:02:00 | TERRA_M-T | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 94d11bc8-8525-3835-aafe-f679eedb2f8e | -22.02884 | -45.26914 | 2025-10-21 12:02:00 | TERRA_M-T | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| f4c42727-5053-30e2-add3-8a258abc6eb9 | -18.17757 | -44.54608 | 2025-10-21 12:02:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 78ac41c7-1324-346c-a43e-5bb9c47ae090 | -18.17888 | -44.53678 | 2025-10-21 12:02:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2605bcb0-8f43-3e99-95ef-8c90023e1890 | -22.61945 | -46.99284 | 2025-10-21 12:02:00 | TERRA_M-T | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5cec804b-7ebc-35c2-8359-832f1e0b40fe | -21.22614 | -45.41417 | 2025-10-21 12:02:00 | TERRA_M-T | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 2a527ee4-db4f-38ba-b2df-574e638a0a51 | -21.22747 | -45.40474 | 2025-10-21 12:02:00 | TERRA_M-T | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| fd833c47-6d46-32eb-9ee3-e1b41525db5d | -21.16807 | -43.02192 | 2025-10-21 12:02:00 | TERRA_M-T | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| acb839f1-6796-3de5-98d4-3890e82c15f5 | -21.41703 | -45.49548 | 2025-10-21 12:02:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3e68d569-a4fd-3c7b-8be1-cbfa9456fca3 | -19.7826 | -47.37627 | 2025-10-21 12:02:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d98f8919-c03f-3d67-b05a-2f884b537021 | -22.36126 | -45.59071 | 2025-10-21 12:02:00 | TERRA_M-T | PIRANGUINHO | MINAS GERAIS | Brasil | 3151008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1d34ae83-c75a-3c3d-aed8-37608479bdb0 | -21.63613 | -48.98624 | 2025-10-21 12:02:00 | TERRA_M-T | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1aa7fdfd-d2c5-3b7b-9633-6105e5917cdf | -22.17843 | -45.84716 | 2025-10-21 12:02:00 | TERRA_M-T | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |


[Clique aqui para ver as próximas entradas](README26.md)
