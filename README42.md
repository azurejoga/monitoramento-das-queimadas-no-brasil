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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d444dfa-7230-33e6-ab14-005388551287 | -3.3871 | -59.4075 | 2026-09-07 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| d57fcd25-b2d9-3df4-af5f-460f7ef4f437 | -3.387 | -59.4266 | 2026-09-07 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3a5f08b2-3fa0-3503-9eb6-58d4aed008ac | -3.0894 | -61.5214 | 2026-09-07 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| baf728ca-fdf5-39a1-b378-431f7289498e | -3.1174 | -57.6973 | 2026-09-07 16:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 51918079-d837-3ff4-b876-fb8bb42e5d4b | -9.74 | -43.47 | 2026-09-07 16:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 032e056c-6eeb-3b8e-a22e-155a259e431e | -9.77 | -43.48 | 2026-09-07 16:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47818840-5aa7-38f8-9c00-1fd8d8b9b390 | -9.74 | -43.38 | 2026-09-07 16:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0f6365d3-45e2-3eb2-a115-51177100d632 | -3.1174 | -57.6973 | 2026-09-07 16:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d6f11fb1-de08-3010-a1ba-cf916896d802 | -3.3871 | -59.4075 | 2026-09-07 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f1af4d1b-b2dd-3eed-8599-1367dd74247d | -3.0894 | -61.5214 | 2026-09-07 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 3b72825f-516f-3b0a-9d7f-c3068fa0abf0 | -5.65 | -45.55 | 2026-09-07 17:15:00 | MSG-03 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 896f87d6-1252-33a8-a234-1c6638eb3063 | -7.57 | -40.42 | 2026-09-07 17:15:00 | MSG-03 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 701d9c68-d491-300e-b14e-3891cf607b12 | -7.57 | -40.38 | 2026-09-07 17:15:00 | MSG-03 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 7e2eb85e-f197-3c7a-ad7e-a7fdf1b3555d | -9.74 | -43.43 | 2026-09-07 17:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0af1929d-0bf6-37d6-9542-16945f6bf944 | -5.62 | -45.5 | 2026-09-07 17:15:00 | MSG-03 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11411299-d65e-3cdc-b6a9-07dc68d715f7 | -9.71 | -43.42 | 2026-09-07 17:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0833a4fe-0696-3daf-afd5-dbb49e4f2a1a | -10.25 | -45.19 | 2026-09-07 17:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc23cae-b3b2-3124-8d3d-e9976dde1d54 | -5.65 | -45.5 | 2026-09-07 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb4acf1-fa67-39c0-b63d-ae56186de42b | -2.4653 | -54.9001 | 2026-09-07 17:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 227bf570-eead-3498-9f59-bb674627d189 | 1.9424 | -50.8824 | 2026-09-07 17:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 76.5 |
| e4c34438-c323-30fb-ae08-3593f30893e4 | -2.4653 | -54.9001 | 2026-09-07 17:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 33e67560-eaed-395c-bffa-1cb969e1560a | -3.3871 | -59.4075 | 2026-09-07 17:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 636039a8-9462-3cf5-888e-01f9172ef747 | -6.7648 | -59.4408 | 2026-09-07 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 310b8537-88bf-3632-8b05-1c96e5159e9e | -6.7832 | -59.4401 | 2026-09-07 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |


