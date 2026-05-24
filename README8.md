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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8dde7f-11ff-3883-a63a-9a8a74a847fe | -8.87 | -46.9215 | 2026-05-24 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 19d0698f-29de-3d00-921b-b9e503cfdc74 | -12.5372 | -57.1614 | 2026-05-24 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 180.7 |
| 7079770d-e225-3af1-a186-d84129586719 | -11.5559 | -56.9432 | 2026-05-24 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| a6a59829-127e-30f5-a5fd-e460f26f5444 | -12.5367 | -57.2014 | 2026-05-24 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 44cc4c17-ef73-323d-bfb9-8e441847993b | -11.5557 | -56.9632 | 2026-05-24 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 1df22b8a-0ead-30fe-aef5-570848537eb5 | -8.87 | -46.9215 | 2026-05-24 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7e28ea69-9f4d-35ca-bdaa-6a92f281c1e5 | -12.5372 | -57.1614 | 2026-05-24 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 152.1 |
| d28c50cd-f031-3827-930b-242fa92aeaad | -8.8697 | -46.9437 | 2026-05-24 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d93f6aee-2e1f-3ab3-95ca-5dba8662150a | -12.556 | -57.1798 | 2026-05-24 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 324861df-e565-3d9c-b75d-046d9c495ad4 | -12.537 | -57.1814 | 2026-05-24 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 6251783c-965e-3e55-a1a3-197ff86cd775 | -12.5562 | -57.1597 | 2026-05-24 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 4b7b31dd-05d5-3d45-b5f8-c7556c5ab5d5 | -12.5367 | -57.2014 | 2026-05-24 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ad86f3e2-3dc3-35a3-8249-4a89073edcdc | -8.87 | -46.9215 | 2026-05-24 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ccd4bda4-1813-33fc-9383-e952fb3b9cc4 | -12.5372 | -57.1614 | 2026-05-24 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 199.8 |
| c7befed9-a250-3be5-83fd-2f907c37f67d | -12.5562 | -57.1597 | 2026-05-24 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 90e22f93-85fe-320b-bc49-6641e9bcbb48 | -11.5559 | -56.9432 | 2026-05-24 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| ba462e71-f33d-313a-9b6d-23c367c5e098 | -11.5557 | -56.9632 | 2026-05-24 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| a05a9919-b3a1-3118-9cda-4893b4008c57 | -11.9138 | -57.0339 | 2026-05-24 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d9fbb253-6c43-3ef7-ae11-069b3fb696e5 | -10.5121 | -49.7648 | 2026-05-24 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 42a3c75e-7402-3a2f-97ba-74b1d7b20856 | -11.5557 | -56.9632 | 2026-05-24 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 15920aa2-7bc4-33b7-9367-9dcac11ca13f | -8.8697 | -46.9437 | 2026-05-24 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 6cb89277-5445-3220-abdf-c6a9931e7960 | -12.5372 | -57.1614 | 2026-05-24 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 215.9 |
| 11559053-487e-318c-97dc-ede21227e6ba | -11.0673 | -46.8471 | 2026-05-24 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| fa550a61-c63f-3e8d-a18a-214a7a970a2e | -12.5562 | -57.1597 | 2026-05-24 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f02e1dec-276b-36d4-bac3-46813a9bf86c | -11.5559 | -56.9432 | 2026-05-24 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 96e5c7fd-ac62-3b5d-8994-f046052a2416 | -12.5367 | -57.2014 | 2026-05-24 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 41acafb9-758e-3aff-9777-7ce78261d538 | -12.5372 | -57.1614 | 2026-05-24 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 220.5 |
| 72c290e5-6e32-3825-a18b-5e6770c6a5f6 | -12.5367 | -57.2014 | 2026-05-24 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 6b0737a3-f6f3-3e96-87cc-4f33a7817b78 | -11.5559 | -56.9432 | 2026-05-24 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| dcba652d-8bbd-3d02-accf-26a6b4e41495 | -11.9138 | -57.0339 | 2026-05-24 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2a7860a7-310d-36b4-9988-9b87bf96649a | -11.5557 | -56.9632 | 2026-05-24 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 83497686-f854-38c7-b558-4fc8225e9197 | -12.5562 | -57.1597 | 2026-05-24 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 5044af47-2bc7-3c75-9c4e-707d253213be | -11.5559 | -56.9432 | 2026-05-24 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 8e776b9c-43a7-3adb-abc2-c886a3813dd4 | -11.9138 | -57.0339 | 2026-05-24 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 89155eea-f77d-359b-a6b2-d2a1b4ea3935 | -11.5557 | -56.9632 | 2026-05-24 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| f354e360-742c-34b5-8d9f-149f97efc081 | -12.5562 | -57.1597 | 2026-05-24 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |


