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
| 55503593-ffa1-3983-b33b-df4e5d9ea043 | -21.70761 | -48.4342 | 2026-04-16 05:25:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3d50ae0-6d12-3df9-8ebe-2194822ce40e | -22.9617 | -52.7003 | 2026-04-16 05:25:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 610983b1-2113-3045-8590-0d86416a0f1e | -22.96154 | -52.70305 | 2026-04-16 05:25:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| be6ed5af-6367-3422-959c-9fed03b58506 | -21.70687 | -48.4281 | 2026-04-16 05:25:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 898a4551-9cad-3ded-8101-5d73dbe13ad7 | 1.80631 | -60.93853 | 2026-04-16 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43c863d9-ff38-3d79-b0b2-0407e9f9f8c8 | 2.02578 | -60.59421 | 2026-04-16 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53cfcaf8-9dce-3f90-a526-4f8b9dc3f8b8 | 2.5196 | -60.65021 | 2026-04-16 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be2ca57e-f6da-35d1-9cb2-da7edc33e9df | 1.81149 | -60.93768 | 2026-04-16 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d55a8b7c-6464-3d0f-855e-b66a851fd0dc | 3.30363 | -60.76295 | 2026-04-16 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aa1dd79-b2e3-3389-ade6-9e71a1c98aaa | 2.02506 | -60.59385 | 2026-04-16 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c394376-7e7c-3f78-bdc6-568183aa5a27 | 2.0256 | -60.59713 | 2026-04-16 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cba56c5c-a5be-3c27-8d76-c25303cd152d | 2.03196 | -60.60275 | 2026-04-16 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 505c5235-26a4-3c14-8d73-0a6b2cf2cf1e | 2.0263 | -60.59749 | 2026-04-16 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 517b338f-a64e-356b-b220-5c0363d02a1a | 3.30313 | -60.7599 | 2026-04-16 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34398011-525d-39db-8f1f-75eceb275b3e | 3.29851 | -60.76379 | 2026-04-16 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c37b4425-bfa6-309a-b0b7-2d33607cac36 | 1.80682 | -60.94167 | 2026-04-16 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dd7df2a-7fc6-3225-b72d-0ab4b11468eb | 1.81098 | -60.93452 | 2026-04-16 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d78761dc-8407-3b4a-bb4d-6800b4f88166 | 2.01135 | -61.08412 | 2026-04-16 06:05:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6ce041-752c-341a-8d54-51fefe1b5e47 | 2.51439 | -60.65113 | 2026-04-16 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 552cacdd-e326-3921-a264-389324e10b32 | -6.5631 | -51.1126 | 2026-04-16 06:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| aa063010-e8c0-370f-b217-d521d9ac9d94 | -8.85576 | -36.89723 | 2026-04-16 11:23:00 | TERRA_M-M | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5d470e59-cdc4-365c-a61d-17cb4693707a | -20.18549 | -46.58158 | 2026-04-16 11:28:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 41deebc2-7130-3dc6-9b68-aa51f0c26528 | -19.59446 | -40.07653 | 2026-04-16 11:28:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c2e02172-0c33-38e3-a6fc-22a2b1b1cb07 | -20.19228 | -46.58886 | 2026-04-16 11:28:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |


