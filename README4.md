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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ec4f9c6-977b-3e29-a42d-3e35ad293d2b | -14.1487 | -45.4242 | 2026-05-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| f5791475-e0c6-34e9-b9c8-b5f17a0ceae6 | -9.6449 | -42.9559 | 2026-05-11 13:50:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 158.9 |
| 75094ab0-20f1-3c68-8b4e-0ad9d9d998f8 | -14.1682 | -45.4208 | 2026-05-11 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 8068192c-169e-3a15-85ad-4b18c0a2d863 | -14.1682 | -45.4208 | 2026-05-11 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d9104ec6-742b-3744-959b-92db84200780 | -9.6449 | -42.9559 | 2026-05-11 14:00:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 155.7 |
| 348319b8-f874-341e-b13f-c9d8f26c535e | -14.1492 | -45.4009 | 2026-05-11 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a6df371e-d028-39cf-957a-490dd66cfd43 | -14.1487 | -45.4242 | 2026-05-11 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a51e3a62-1995-380a-8291-b11a1c3cd532 | -14.1682 | -45.4208 | 2026-05-11 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d3bd9b02-93e0-35aa-9674-c738afe128c1 | -9.6449 | -42.9559 | 2026-05-11 14:10:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 155.4 |
| 1c206bbd-f7a8-3320-982d-3d656c4244d6 | -14.1487 | -45.4242 | 2026-05-11 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 90010aa0-8140-32b2-a922-7e4c11697474 | -14.1492 | -45.4009 | 2026-05-11 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| b7392aa8-1585-3cf3-8909-149ac34cbab0 | -14.1487 | -45.4242 | 2026-05-11 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 5511f245-e6ea-3d2d-a28b-8da5c175921f | -14.1682 | -45.4208 | 2026-05-11 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e0676b2a-d715-3223-beb8-385c0a3be010 | -11.8027 | -49.7263 | 2026-05-11 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7196dd5f-b659-3b17-a9dc-26539af5af5e | -14.1492 | -45.4009 | 2026-05-11 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 09b47292-55e6-32c5-85b7-856b8a188c99 | -9.6449 | -42.9559 | 2026-05-11 14:20:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 5f1ae310-5e3e-385c-a1bc-6361578baa4c | -14.1492 | -45.4009 | 2026-05-11 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 9146bf2f-7728-3d66-a634-59fd677d4cc0 | -14.1682 | -45.4208 | 2026-05-11 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f52a033c-82e5-3bdc-bd0f-03799e58bdfc | -14.1487 | -45.4242 | 2026-05-11 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 13140488-c94c-3eb4-acdf-edf0a761b918 | -9.6449 | -42.9559 | 2026-05-11 14:30:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 2ea7e456-63ca-3188-8e26-b563db8e4a2a | -14.1487 | -45.4242 | 2026-05-11 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7d08db0d-40dc-345b-8c5b-787ac8128e80 | -14.1492 | -45.4009 | 2026-05-11 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 7aa0e47c-46e0-3a0b-ada3-39518eb35160 | -9.6449 | -42.9559 | 2026-05-11 14:40:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 9f18df12-624b-35d4-a6d9-5dac87df60b9 | -14.1682 | -45.4208 | 2026-05-11 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 5fef225a-de84-34ae-968f-cd48f3c2f688 | -14.1492 | -45.4009 | 2026-05-11 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 521269eb-c901-35bd-8e5f-28c434edcc1f | -14.1487 | -45.4242 | 2026-05-11 14:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 8ff935d0-c836-3b49-92fa-ac9dc36c37fd | -14.1492 | -45.4009 | 2026-05-11 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a31e8ab8-5a2b-3805-b5db-b04d06e262a5 | -14.1492 | -45.4009 | 2026-05-11 15:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e27a85d3-a095-3d5f-91fe-ffcdf14ced00 | -14.1682 | -45.4208 | 2026-05-11 15:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |


