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
| fcd60fda-b7a2-3a0d-a1f4-1308ec7adc3b | -14.4197 | -44.581 | 2026-02-18 12:20:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 1bcb6be0-f748-3efe-9fed-f0962f9ccbd1 | -14.4197 | -44.581 | 2026-02-18 12:50:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 0b84d689-9462-3f85-8a62-f9b1c417d8fb | -14.4001 | -44.5846 | 2026-02-18 12:50:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 98.8 |
| b89b4cfa-7ad0-3716-9bb6-f6e2cbd8dd13 | -14.4001 | -44.5846 | 2026-02-18 13:00:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 105.0 |
| b82ee43f-8a21-3a3d-9038-000516866959 | -14.4197 | -44.581 | 2026-02-18 13:10:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 09029629-031e-3e4e-aa51-23aa9466b6a7 | -14.4001 | -44.5846 | 2026-02-18 13:10:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 58d0eb6c-927a-33f5-91c0-63a3ba3072cf | -14.4001 | -44.5846 | 2026-02-18 13:20:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 386ae56f-ce19-3909-8248-9a7eae5322d0 | -14.4197 | -44.581 | 2026-02-18 13:20:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 4bb9a710-69a6-3c6d-b32b-2ba99a8ef19d | 2.6542 | -60.1455 | 2026-02-18 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 90.7 |
| eb68694d-8e1a-38df-af18-8351971b7bcc | 2.6724 | -60.1453 | 2026-02-18 13:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 65a61a3b-79cf-3d8b-8fa0-5137fed4f5c2 | -14.4001 | -44.5846 | 2026-02-18 13:30:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 94b63eb9-2bba-361f-9486-6f642f3ee735 | -14.4197 | -44.581 | 2026-02-18 13:30:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5e07dbf4-d980-3fe0-9ff4-acac7fa2a860 | -14.4001 | -44.5846 | 2026-02-18 13:40:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 2ad9cec9-195f-306d-b18b-8a8cb56e2e69 | 2.6724 | -60.1453 | 2026-02-18 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| bef4b888-5a53-34b8-8d0d-be583cc9cc11 | 2.6542 | -60.1455 | 2026-02-18 13:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 2a56eede-b89b-33b7-9208-9771ff4aa3fe | -14.4197 | -44.581 | 2026-02-18 13:40:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| fe9caaeb-009b-3a98-9779-ce0ef2cf6d3d | -14.4001 | -44.5846 | 2026-02-18 13:50:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 29f42fc7-c6e8-358b-b1e1-e8b7524c2399 | 2.6724 | -60.1453 | 2026-02-18 13:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f799af80-2337-313a-ba80-cc1aa287fe7c | 2.6724 | -60.1453 | 2026-02-18 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 6fce32de-a221-3621-9dbc-7bb9afb50c10 | -13.015 | -45.036 | 2026-02-18 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 56b6b7e7-0b7d-3ab3-8833-4f6e6ab3becf | -14.4001 | -44.5846 | 2026-02-18 14:00:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e01b7054-49c1-3f29-8ada-d95e03c34f12 | 2.6907 | -60.164 | 2026-02-18 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ec2adde1-854e-3430-a6c1-15a5aa9d0653 | 2.6542 | -60.1455 | 2026-02-18 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 120.5 |
| ead624fb-0ddd-37c3-b48c-b95498ed36b6 | -14.4001 | -44.5846 | 2026-02-18 14:10:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 124.5 |
| e2e913e4-a670-3f9b-b59e-18f5dd015ae3 | -13.015 | -45.036 | 2026-02-18 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 9153bb49-462c-3667-be99-c8236cd3bc4d | 2.6724 | -60.1453 | 2026-02-18 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 00ea6d2f-5c51-319b-92ee-ae8a53e181e1 | 2.6907 | -60.164 | 2026-02-18 14:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 7e0e0e6c-30f3-3717-b47e-f4af69000e5d | 2.6907 | -60.145 | 2026-02-18 14:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 90543491-1aa1-359b-b2be-d2b81613fd6d | 2.6724 | -60.1453 | 2026-02-18 14:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 7fa6ff73-b9bc-39b6-8541-a170f5c99013 | -14.4001 | -44.5846 | 2026-02-18 14:20:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 197f3be0-689f-3967-a26a-00c8c754a4b1 | -13.015 | -45.036 | 2026-02-18 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| fa69bade-7cd9-3bd5-bf31-51a46f3adfa3 | 2.6907 | -60.164 | 2026-02-18 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 38987bff-3454-30cd-92fc-3df00d64dcee | -14.4001 | -44.5846 | 2026-02-18 14:30:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c5e439da-4ccf-3574-a9f7-32c6b18dcaeb | 2.6724 | -60.1453 | 2026-02-18 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 525a35a1-ec4c-37e2-b2d5-c7e7f4fa8094 | 2.6724 | -60.1643 | 2026-02-18 14:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 6a7773bb-fe05-316e-b831-3dc45fdabd35 | -14.4001 | -44.5846 | 2026-02-18 14:40:00 | GOES-19 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 836dc142-a146-3e98-a007-c913b2f513eb | 2.6907 | -60.164 | 2026-02-18 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0857a3f6-12ff-3f75-b3d9-439091f2ddce | 2.6724 | -60.1453 | 2026-02-18 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 730e093d-5abb-35be-ae90-eb22d9fedd51 | -13.015 | -45.036 | 2026-02-18 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |


