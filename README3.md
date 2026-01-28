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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9203d7b-6d45-3667-a6cf-df743db81e2a | -27.65549 | -48.6999 | 2026-01-28 04:46:00 | NOAA-20 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cacec223-4e7f-39b1-9d96-76b0b523bb79 | -26.74917 | -51.63628 | 2026-01-28 04:46:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 91f28ddf-12d0-3840-99c5-e13a60f7cdd8 | -27.09684 | -50.52903 | 2026-01-28 04:46:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5d1f51b7-7793-347f-b530-3ff92b7949d2 | -27.03142 | -51.36382 | 2026-01-28 04:46:00 | NOAA-20 | TREZE TÍLIAS | SANTA CATARINA | Brasil | 4218509 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db00510e-e7ee-35f5-bc0a-22f2deb4d160 | -25.09832 | -52.91154 | 2026-01-28 04:46:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3c665f4-d4e8-3a7b-9dcb-ed0447392909 | 3.77458 | -60.70987 | 2026-01-28 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e0ca43f-0113-3c67-bb5d-1684db0d588d | 3.89419 | -59.62831 | 2026-01-28 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a696599e-eddb-3257-8241-73bf117296c7 | 3.77842 | -60.71282 | 2026-01-28 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bfc5afb-6f84-3d0c-97c2-0c52f5c48e69 | 4.23557 | -60.65508 | 2026-01-28 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfaa6cdc-8b7f-3ccf-bc34-5edcbea22695 | 3.89749 | -59.6278 | 2026-01-28 05:29:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24658099-60f9-3121-adff-ec40a6292839 | 3.96682 | -60.93982 | 2026-01-28 05:29:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d4e89aa-a82f-3720-b4d7-966edb6e837f | -1.31298 | -53.19622 | 2026-01-28 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b48fbcd6-94fd-30ff-86a5-dad22563d19a | -5.14933 | -60.37505 | 2026-01-28 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2cc4e43-0a2d-3c1c-bf98-1e9b217c1651 | 4.00444 | -60.63481 | 2026-01-28 05:29:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3abfe9a3-97b4-37cb-b57f-defd5629dc8f | -1.31217 | -53.20173 | 2026-01-28 05:29:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b788122b-e481-3aad-abcc-341a25151370 | -5.13697 | -60.38799 | 2026-01-28 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76b9d910-40a1-3e13-af1b-aa997fefa511 | 3.97789 | -60.94529 | 2026-01-28 05:29:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 632894f0-a4b6-3527-a11e-4db3220f0bc7 | 3.58545 | -60.46023 | 2026-01-28 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25feac2b-8e65-3745-bb8c-fbe7f21dd7c0 | 2.96363 | -60.85788 | 2026-01-28 05:29:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65e69419-348b-3c4d-add1-f98449b217ac | 3.77524 | -60.71181 | 2026-01-28 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25ccae7c-e16a-3a50-ad7d-3688515c379d | 3.97 | -60.94286 | 2026-01-28 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a449039-2b59-3c7c-985d-f2966f2e0639 | 3.96688 | -60.939 | 2026-01-28 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bafea70a-13e4-3991-80d9-4f2c1fce27b0 | 4.15111 | -60.6332 | 2026-01-28 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 574b2a3d-2070-3d12-b411-3428d8180b10 | 3.96748 | -60.9427 | 2026-01-28 05:59:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1551c90-ea21-3bf0-8902-ca93d4678220 | 4.0054 | -60.634 | 2026-01-28 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |


