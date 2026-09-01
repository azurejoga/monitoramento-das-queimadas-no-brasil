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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42bd01ad-fcfb-33dc-a2c5-a4ddaa046619 | -4.95903 | -55.83924 | 2026-09-01 12:49:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 0316ab83-3d4c-39ae-a10a-1e765eed30a2 | -7.19046 | -60.67987 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 9786fee9-1df7-34ff-9c41-d7ef0f3e7c58 | -7.91788 | -61.34269 | 2026-09-01 12:49:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e8da710c-ed37-3339-b7b4-a770a7293169 | -5.491 | -57.14333 | 2026-09-01 12:49:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f95c1ac9-e9a8-3e60-b045-43573f5f502d | -7.86267 | -61.1452 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2085bbb9-a9a1-3a97-95b3-ab2a4848f64a | -7.04336 | -59.22062 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 06283595-9e04-3f53-81dd-41f3f9e1fdc2 | -9.48008 | -57.0202 | 2026-09-01 12:49:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| e56011b4-ddde-310d-bfa5-f3405737386c | -7.34984 | -60.57302 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 53dd09b3-404e-3ca9-abfb-ecbe20ad1778 | -5.82015 | -61.26181 | 2026-09-01 12:49:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b27132da-6581-3d1c-8785-5906ff119aa9 | -8.12108 | -54.95534 | 2026-09-01 12:49:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| ffc0a62e-7db8-3f3e-9af7-3832e21ed738 | -7.57558 | -60.48372 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 031b253d-4957-3f4c-a1a1-934a82fb7b42 | -9.14844 | -60.94829 | 2026-09-01 12:49:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 2b0ef581-1fa8-3d75-852a-ac001d837095 | -4.15881 | -60.69272 | 2026-09-01 12:49:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f821db86-7d44-3e9d-bcc5-16dca5f9c951 | -6.96365 | -55.63687 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| e7575459-2ad4-3771-8320-33fec87fe349 | -9.13625 | -56.62431 | 2026-09-01 12:49:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| b8b08322-a452-3d8c-ba6f-96b42cb21f4d | -7.91925 | -61.33275 | 2026-09-01 12:49:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 55d4b055-ab48-3e8d-af2b-e21dc05e058a | -6.86394 | -59.47413 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e220d095-be3e-3d44-8791-c2ad3b7e66e8 | -9.16424 | -60.29282 | 2026-09-01 12:49:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 195bb456-46f3-3c86-b4e3-75e1567e9018 | -7.58679 | -60.47435 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 60a5ede7-2544-3240-ac79-4f9c1fd8a29d | -7.03278 | -59.2193 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 158993b5-d013-3bf5-b4dd-1daff517f402 | -3.50913 | -59.05584 | 2026-09-01 12:49:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| bc10a70a-154a-3d30-a867-a66fe097d9a8 | -9.00315 | -65.43282 | 2026-09-01 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b66a5678-246a-3b1b-9095-64282c849c74 | -7.57706 | -60.47289 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8fb3d843-4594-3cda-9416-30d81fc676f7 | 0.14202 | -60.39878 | 2026-09-01 12:49:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f822e31-6988-3b29-a14d-e668581d516e | -5.25047 | -55.91589 | 2026-09-01 12:49:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 777ab7d9-ac7b-33a9-8552-e02537d1bf0f | -7.56879 | -60.46067 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 048c75e0-6635-3d68-a07f-e949f6338012 | -8.72247 | -67.10625 | 2026-09-01 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1e2717fb-cc5f-31e3-9146-815613a2aace | -3.34491 | -59.43548 | 2026-09-01 12:49:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7f4feaf2-f735-3565-9233-6965c08f957d | -6.18797 | -57.73533 | 2026-09-01 12:49:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| b5c96296-6c98-3fac-a857-dca06846e651 | -4.15469 | -60.72183 | 2026-09-01 12:49:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 37baf98c-a641-3b82-beac-28ed523de176 | -4.35156 | -59.54767 | 2026-09-01 12:49:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f033e672-8f70-3042-913f-9261d02c6e45 | -7.84385 | -61.14262 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 003a0f83-71dc-30b1-8759-8840a2bd188f | -6.61312 | -58.59683 | 2026-09-01 12:49:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9a2d94f7-bf9b-3cd2-b73a-1b3b52fa1f6a | -9.02933 | -65.44655 | 2026-09-01 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d0c790a4-2cc4-3394-bd3b-bff6f02f3809 | -5.95519 | -57.68626 | 2026-09-01 12:49:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| be210e2e-bf5d-32f3-abaf-dbad7e688cf2 | -6.94953 | -55.63527 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 76e1eb2a-9bfe-34b5-8b19-299920fe832e | -6.76259 | -58.66539 | 2026-09-01 12:49:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 94f1f890-a1f0-38fe-a28d-56d66de79ed5 | -6.16453 | -57.73227 | 2026-09-01 12:49:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5f4e5470-c8f1-3464-b364-9069330cc07b | -6.41555 | -55.5319 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| e27972b5-6932-38e1-8505-e7d5cfd265ac | -9.45941 | -67.45634 | 2026-09-01 12:49:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e22c5b80-65b9-3890-84ff-a573fae3600e | -5.57192 | -60.18912 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 709abab7-04a3-3ce6-9c02-6ebb3bf717ad | -3.61877 | -59.07704 | 2026-09-01 12:49:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3632fd75-f1e6-3f95-a265-d187d55df592 | -4.15743 | -60.70243 | 2026-09-01 12:49:00 | TERRA_M-T | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6d007a89-2f27-355f-a2c0-a99943d8b685 | -3.09676 | -61.16029 | 2026-09-01 12:49:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dfb2bd6a-daa6-31b8-94ac-cf730722a658 | -3.34415 | -59.42885 | 2026-09-01 12:49:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 70008161-7f39-3ba3-8e1f-8129f2c0f666 | -6.77497 | -55.64432 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 319e3df3-a34f-36e4-b6f5-0257e652f02a | -4.2252 | -59.8717 | 2026-09-01 12:49:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e8912066-8319-389e-8087-71e1d11c1ff4 | -7.4554 | -59.93849 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c9a40ab6-a16e-3c1a-8b68-608452036c4a | -3.12453 | -61.22641 | 2026-09-01 12:49:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9ac7f476-c261-3cef-b7d5-26a9e2db510d | -7.34839 | -60.58379 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 28b9c4cf-235a-328f-b488-6115ce1b8e77 | -6.41125 | -55.52439 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 8712ca67-f3e7-3d43-911e-3ce7296ec509 | -6.95934 | -55.62966 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 0184a2ca-c2da-3b5e-85ec-01d55df65379 | -7.53544 | -61.37657 | 2026-09-01 12:49:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4e83d2e7-3325-3934-a136-1f79466ae443 | -8.53278 | -55.31723 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| aef6ccda-c319-396d-b420-6987d82b2ef1 | -6.9376 | -62.88296 | 2026-09-01 12:49:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1d5cb822-a66f-31e1-8140-a7d0a5039d32 | -7.20006 | -60.68108 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 4c447f68-42d2-3740-93f0-e768a2032261 | -9.14138 | -56.61953 | 2026-09-01 12:49:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| ceb1ac08-b778-36f3-81bc-cb40a1ff7ef9 | -7.85326 | -61.1439 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 44657a0f-8c52-3b2b-add0-e2518c023f0a | -9.47754 | -57.04089 | 2026-09-01 12:49:00 | TERRA_M-T | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 7e7aae79-55fb-300d-98e7-9e857c61f1c2 | -7.58531 | -60.4851 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8e0e5dfb-a445-343c-954f-c80c342708ba | -3.62423 | -60.56292 | 2026-09-01 12:49:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 9676ae02-a7d1-3abc-8000-dc7780a57a50 | -6.95252 | -55.61048 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 1db8e6d6-1b77-37f5-85f2-a8c056c9c357 | -6.40807 | -55.54893 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a5cc6633-7704-3a40-bc95-c915f203f545 | -7.3595 | -60.57433 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| cdf4c1f9-d31b-3e67-9ea5-cbafccda7552 | -6.15322 | -57.90965 | 2026-09-01 12:49:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5242da0c-0de0-3456-9d65-05a4d505e6f2 | -3.76728 | -59.33382 | 2026-09-01 12:49:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8abfef9b-93b2-3591-b479-c1c284381cc8 | -3.64956 | -59.2998 | 2026-09-01 12:49:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a72729a6-f48f-334f-af5d-2dbc0e04b9c1 | -4.9725 | -55.84066 | 2026-09-01 12:49:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 9ce171cb-116f-3932-bcd4-11112fef053c | -5.25336 | -55.89393 | 2026-09-01 12:49:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| adace6b9-3db9-3e16-888b-345dab520072 | -9.02792 | -65.45627 | 2026-09-01 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 453496b8-abfd-31b9-b249-c7c698d0f95f | -5.81881 | -61.27133 | 2026-09-01 12:49:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 02b0955b-bd84-3678-abba-e0b8836e03e9 | -6.66441 | -59.4352 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 3345a0ef-c7d1-3da6-9356-5831cbafafe0 | -3.2065 | -61.16904 | 2026-09-01 12:49:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 93690b3b-0126-3fe9-add1-08d5b82fef9f | -8.7628 | -46.4642 | 2026-09-01 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7a087002-628d-3faf-8993-884600b2bf88 | -11.5479 | -45.4676 | 2026-09-01 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| a7c585e8-23ba-3207-b3cb-85d5121604ea | -9.4719 | -57.0354 | 2026-09-01 12:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 924e32c3-bb48-3b8c-880f-e087bdaf6db0 | -15.4235 | -52.6836 | 2026-09-01 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 8bc43021-f6ad-32d9-af2e-5874750cbb50 | -3.879 | -44.0576 | 2026-09-01 12:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 70ad0ea7-9180-341b-96bb-5508b625a099 | -12.9032 | -45.8382 | 2026-09-01 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 56180333-663f-3d29-8775-9818802f1416 | -10.8627 | -45.356 | 2026-09-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c2f10246-3ebe-3812-a65d-26d7d92179f0 | -6.9552 | -55.635 | 2026-09-01 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 8972b7ac-fb47-311c-9c8c-9ef11c0e9921 | -10.1321 | -45.8825 | 2026-09-01 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 7b20cc3b-69d9-34ac-bcdd-2045140bd198 | -7.3487 | -60.5883 | 2026-09-01 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 1c88b2b0-7e0f-3b6e-b658-06f627b9675a | -8.279 | -54.9174 | 2026-09-01 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d6273f10-0cb2-3aa2-8530-3e9d3517b8a2 | -3.8604 | -44.0585 | 2026-09-01 12:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c58b6aa2-f59c-34e7-829a-5210de071689 | -10.696 | -46.2646 | 2026-09-01 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| c10ff622-8c17-3ee3-8880-7ae57d84b0ee | -10.1324 | -45.8598 | 2026-09-01 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a95b0e66-f920-3175-8a9f-af9cff243707 | -10.036 | -44.7056 | 2026-09-01 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 74c10019-1b38-357f-b69e-7abc6288813e | -9.4349 | -45.625 | 2026-09-01 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 53f120aa-b492-35ad-922f-e19445828dd2 | -6.1659 | -57.7403 | 2026-09-01 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 1c558b3f-f937-3755-9cbb-895bf0ff96aa | -11.8056 | -46.0476 | 2026-09-01 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| aa6ed32e-7e25-3f4e-8f3d-2a23513b1cf4 | -6.9553 | -55.6151 | 2026-09-01 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a45445a8-b2c9-3d69-881b-317d39d31b1e | -12.8839 | -45.8412 | 2026-09-01 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 4f772cc1-fd0a-310b-8717-36eec89bad67 | -10.1538 | -45.6982 | 2026-09-01 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 316c9b1f-70f2-3643-861b-0943615284e1 | -11.2317 | -46.1041 | 2026-09-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 12e2db2a-de47-3e2f-ad49-50176360a4aa | -10.8818 | -45.3534 | 2026-09-01 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 149aea73-8c2d-3bd2-9d0e-21f8d4310135 | -17.1146 | -46.8556 | 2026-09-01 12:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| c3cb8bba-da46-343b-8445-a0faa3523fc4 | -14.6732 | -53.5408 | 2026-09-01 12:50:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a3d977ad-d2dd-3960-a0db-806a0ac81547 | -8.7817 | -46.4623 | 2026-09-01 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 19438eca-8a1a-32d5-b8f2-fb8cf9bfc33e | -15.4429 | -52.681 | 2026-09-01 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 185.6 |


[Clique aqui para ver as próximas entradas](README94.md)
