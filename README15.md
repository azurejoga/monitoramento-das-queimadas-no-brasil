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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd946ac-136a-3671-b3cc-3de4e7df6c00 | -10.07337 | -52.74266 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22a06feb-d6ca-3c48-abcb-3c9fe1b3e283 | -10.24229 | -52.23396 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccc10d19-7f39-3634-a1ee-74babc726248 | -10.07966 | -52.74355 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 705c9e93-bc20-3a22-8e89-b35ed6f1580a | -10.07639 | -52.74585 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2a3df78-fdb0-34c3-8824-7d2cd562a011 | -10.24232 | -52.23854 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ce8b2cb-4486-3f28-91cb-8531e7dca993 | -10.08269 | -52.74673 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d6253386-981b-3823-8196-7d56a206e1e5 | -10.09594 | -52.74316 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a816de8c-f4e9-308d-ba80-470e8fc8889f | -10.08535 | -52.74932 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72b806a8-bf44-3670-81af-4b5c059884e9 | -10.24302 | -52.23296 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 487a9c63-02c1-3200-9891-cc6cb28acd1c | -10.2358 | -52.23777 | 2025-06-15 05:33:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27ff550b-193e-3a6e-bd96-280656b48ba3 | -11.00678 | -55.07502 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08ef69ca-641f-3796-9fd5-de2d8dd8c20c | -10.93177 | -56.83674 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5613150-e9b6-3c47-96ee-f7696d3e3b9d | -13.91537 | -54.64921 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e599506-a7e0-3b3f-bdfb-5c39bd671ffb | -11.01183 | -55.07933 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7885cb7f-2726-3c48-8940-94088b185f92 | -10.91168 | -54.75786 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71d38c4d-f6de-37fa-94a2-d56a79e792d6 | -13.91783 | -54.62744 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2515cf35-1f51-3227-a036-47f80f9f3a41 | -12.6933 | -52.40125 | 2025-06-15 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6bb914cf-2fec-3458-8927-307b26d6d50b | -13.91926 | -54.61474 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d743aba8-c5ac-3be4-8962-c286e1c57b6e | -10.50381 | -53.58119 | 2025-06-15 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 04e70350-cdcc-38b1-b085-8f7cf3791b80 | -13.9134 | -54.61374 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dea6b6ec-2d66-3e5c-8c50-fab87ef20b9d | -14.67355 | -53.13102 | 2025-06-15 05:36:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 492e70fc-cb6d-3873-ac41-aa6376124d0c | -13.90755 | -54.61272 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1cae3736-42d1-3bee-8cea-d31eeef0d928 | -10.92689 | -56.83611 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8008df32-aad8-3d66-98f9-e037a72f343a | -10.92939 | -56.83777 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f010cdf2-be0f-3acb-bd92-38ab4380571d | -13.91293 | -54.61794 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2b31bd57-ba50-3ae7-b130-c047fdbd675d | -10.91776 | -54.75479 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6d80e653-2faf-3756-9e4f-f21e40510bbd | -9.65481 | -66.56637 | 2025-06-15 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f807cfcc-0632-3651-a0a2-e749bfb2f834 | -13.91542 | -54.59575 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50e9cc7b-294c-3848-8a45-6ef02303480c | -10.93252 | -56.83123 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e05230d6-7958-3658-bbdd-aba3dc22cbed | -13.91489 | -54.65353 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27149744-9fca-3298-8a37-a1b262187674 | -10.85362 | -53.78895 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe5a3c88-8b29-3ddf-a839-45342d0f3b44 | -11.01275 | -55.07203 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2dd6385-f86a-3b5f-93c7-50cf68c33ebd | -10.93008 | -56.8323 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8428395d-96d7-3040-9727-7a26a462f79a | -10.50596 | -53.57913 | 2025-06-15 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 246649b6-76eb-3075-9254-4c67f85a5943 | -15.61635 | -56.11767 | 2025-06-15 05:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 035e79b7-505b-37a1-a8d0-485fc25623aa | -13.92565 | -54.61096 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3a95e50-a9e1-3041-904e-be49b4d6b530 | -10.04565 | -64.98886 | 2025-06-15 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90e5a16a-66be-366c-a98b-be9a12587426 | -10.91728 | -54.75864 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7659e01-273d-301d-b0b1-7c45000737ce | -13.9183 | -54.6232 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3dc2cf67-275c-362d-a49b-f836b32eed0a | -13.92467 | -54.61967 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6388fecf-432d-30b7-89e4-be05d8df74da | -14.673 | -53.13608 | 2025-06-15 05:36:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62240d04-32c4-3c83-927b-6b330c009e7b | -13.91735 | -54.63171 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 592e8c4b-ebe1-36ae-ab0b-30744562f5d6 | -13.91439 | -54.60491 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d3002d9e-e683-3b99-8d6b-819dc81ce042 | -12.69397 | -52.39517 | 2025-06-15 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4e40926c-4848-3223-96a5-c48bf58fa238 | -13.91246 | -54.62214 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f341e04-4138-3273-a7aa-f1c3565d74f9 | -10.04234 | -64.98833 | 2025-06-15 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 301971cc-9bf0-3928-93bc-104a84a30b76 | -14.67334 | -53.13317 | 2025-06-15 05:36:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9a8f5bf-242a-31f9-ae90-65a77142b0d8 | -10.50982 | -53.582 | 2025-06-15 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8037a5b7-8e26-3aa4-aa2c-56711bae0e9d | -10.62283 | -54.91833 | 2025-06-15 05:36:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdc51bb5-85b3-3ebd-b275-a8ab955d7d68 | -10.84326 | -53.7745 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c1a14e4-f0d2-3887-8f03-4be0ff14d95a | -10.51145 | -53.58433 | 2025-06-15 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0597b60e-df24-33fc-a79d-174e4e0e02fe | -11.01092 | -55.08652 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a585748d-14c3-36eb-96c6-a7a4ba6cdc26 | -10.92195 | -54.76699 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d9d185a-78b4-3b2e-a547-8260926eb709 | -10.91681 | -54.76244 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5f93100b-af6a-373a-9da5-0877e05a8542 | -10.91214 | -54.75409 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e582c15b-7fd5-3f46-910b-fd978f4e5c70 | -10.85468 | -53.78028 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 622c4a93-353e-3003-b741-9731fa1e77d7 | -10.51197 | -53.57996 | 2025-06-15 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3da32868-195f-3858-bad2-859f792a848c | -13.92079 | -54.60109 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3304b471-36fe-370e-bba2-790cfb3bd39f | -11.01229 | -55.07568 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a66f95b0-01f9-31d2-a2d0-5542ce1d01d3 | -13.91441 | -54.65773 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6d38057-747b-37b6-aeaf-6361cd47ebb5 | -13.91878 | -54.61898 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fe45d4d3-b346-3b9f-9129-77ea3c32be16 | -10.9159 | -54.76987 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77fb35bf-8af8-3f8d-b424-821e1593c166 | -10.91122 | -54.7616 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d2549542-9648-3c91-9b63-07c3a673859e | -10.92616 | -56.84152 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f91e34da-29a2-334f-8392-364e58585546 | -12.16321 | -56.54118 | 2025-06-15 05:36:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5fb9ab9-335e-339e-b9de-afe1555cf4f5 | -13.90804 | -54.60833 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cb60c2ff-ec3c-3d2f-bc76-980fc5f859bc | -12.16827 | -56.54194 | 2025-06-15 05:36:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbf981ea-f1fc-3a1d-bb58-bf1886e403f2 | -10.50543 | -53.58352 | 2025-06-15 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b2dd17c-a82e-3dd7-a342-384df0ca8537 | -13.91389 | -54.60938 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9e631d57-1fa7-3859-a083-cd15bb565907 | -13.92418 | -54.62397 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd59658c-be08-3534-afa1-b1213838f4ca | -13.90903 | -54.59947 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 600021a8-d204-331d-aca9-ced1a1e6d960 | -10.84818 | -53.78386 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8102b622-1253-32ef-b67a-5e9365dbc829 | -10.8487 | -53.77958 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f348d87c-de6d-3b99-890b-df4321847fb7 | -13.90853 | -54.60391 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6ebffa60-df57-38b7-a4f5-62956a383074 | -10.85415 | -53.78461 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8df9f51-8297-3203-94a9-c1f2a5840d0a | -11.00724 | -55.07135 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d4a76c9-92ad-33aa-814b-d3b44dbd85d5 | -10.9213 | -56.84081 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a367b057-17d0-3fa0-a755-367b40a83293 | -11.01137 | -55.08293 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c7c06b4-266c-3945-8de8-6c436ef48774 | -11.04896 | -62.58495 | 2025-06-15 05:36:00 | NOAA-20 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2162b1-bbe6-3ae4-9313-9e4846791ee9 | -13.91491 | -54.6003 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04119945-a86f-354b-98d7-8c6c461eb56f | -13.92027 | -54.60578 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2de9f9c6-0a46-37a2-98de-3fccc6c004f3 | -13.91587 | -54.64484 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67ec9137-9b29-349e-9c36-fd44135ae0ca | -10.93358 | -56.84384 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0782eba3-06ac-36c3-9696-36c6e803fb1f | -10.91636 | -54.76616 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d366bb76-40f8-3289-891a-0d62926ffe5b | -13.91975 | -54.61035 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 76924797-7e28-3687-b166-9b19d96c300b | -12.68731 | -52.39444 | 2025-06-15 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5975764-e1a9-39af-a091-c5e0dac9d838 | -13.90706 | -54.61709 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1a0c3d2b-acf8-304c-8228-f0b213a5307a | -12.68665 | -52.40051 | 2025-06-15 05:36:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faa42067-c568-32e0-bc6d-39495c8493ef | -13.92515 | -54.61539 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37c3f9ad-2fa8-3461-93f8-cd49157609d8 | -11.00632 | -55.07869 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc4f115a-4e6d-3469-a472-ec032bf53b18 | -10.93078 | -56.82676 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d93b834-da2e-3e76-82bf-b0a72a49f4fb | -10.92149 | -54.77074 | 2025-06-15 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8950d8eb-1fd7-3b27-b8da-aca4abc84cf1 | -10.92763 | -56.83065 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 32baddf9-2d0c-368d-88b7-956a381af8ac | -10.52268 | -68.04632 | 2025-06-15 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d933bd35-66a0-3d3f-85f0-0da6a1df2f95 | -13.91197 | -54.62646 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3b096993-7edb-3293-951a-320f7bda7ffe | -13.90217 | -54.6074 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 47aede42-1241-347f-8fdc-cbf82ff2f9ef | -13.9237 | -54.62827 | 2025-06-15 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16250e22-904e-357a-9ef1-c10105d5b910 | -10.93592 | -56.84282 | 2025-06-15 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4974f03a-39ab-3784-9315-2ee43c63dd81 | -11.00586 | -55.08229 | 2025-06-15 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b21d454f-4ae3-3b92-8574-414ef7b746da | -13.9251 | -54.627 | 2025-06-15 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.1 |


[Clique aqui para ver as próximas entradas](README16.md)
