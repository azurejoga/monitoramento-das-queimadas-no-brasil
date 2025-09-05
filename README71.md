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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c2b60ca-4728-392e-b7e0-4d3e95a729ed | -5.7923 | -45.3078 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 5e68cf3a-7f76-3408-885b-45a36531cf39 | -15.2159 | -52.3506 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 160.6 |
| e030a2bd-394f-3a6a-8b93-6aa8bf74b763 | -5.608 | -42.8798 | 2025-09-05 14:40:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| bb6addda-84a7-31f7-ac64-7ba34288ed44 | -12.2532 | -50.168 | 2025-09-05 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c3289de4-7dfe-3863-98b0-e11816f5db6a | -15.2156 | -52.372 | 2025-09-05 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 210.0 |
| c605d33a-f6fc-3a18-ba62-c751d7cda48e | -6.1491 | -43.1885 | 2025-09-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 72.0 |
| e43dd91e-388a-3dd9-8c42-7163a25ab657 | -8.6883 | -62.4002 | 2025-09-05 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 522cb215-8a96-3fe4-9f98-b5bb0c9389f5 | -7.6491 | -63.1197 | 2025-09-05 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 79382132-b9fb-3601-80e0-f33b8318426e | -6.2606 | -43.2961 | 2025-09-05 14:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 824e0505-5793-34ec-9607-234efe55e49e | -6.0045 | -46.6797 | 2025-09-05 14:40:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 950f09c4-fad3-3284-918d-7407324e7b4e | -12.7251 | -45.0828 | 2025-09-05 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 86b3efc6-7cac-3c5c-b4ba-5334ed887888 | -13.8845 | -47.9705 | 2025-09-05 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 39b7e405-493f-3ce2-a36e-e03074022de4 | -14.4427 | -53.4855 | 2025-09-05 14:40:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| b68dbc4f-c3cf-3a8e-ae22-b3889146ee88 | -11.5961 | -52.176 | 2025-09-05 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d8fefda0-317f-31dd-94e3-4014d3cb7f2b | -6.2857 | -53.4369 | 2025-09-05 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b35f64ba-3505-35dd-bd13-137d6317889f | -6.4645 | -43.5586 | 2025-09-05 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| bdae0e79-8e0c-32df-a9d3-d427bdd2de28 | -15.0639 | -50.087 | 2025-09-05 14:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| b4820743-5126-3210-a22b-26367bc65b19 | -8.2001 | -49.5988 | 2025-09-05 14:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 10c417c5-e1df-33f5-a01a-f9f62bff56b1 | -8.5374 | -51.3278 | 2025-09-05 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 286.7 |
| ca331aff-40b1-3fe4-978c-e6e5ca248e18 | -11.2007 | -54.9992 | 2025-09-05 14:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |


