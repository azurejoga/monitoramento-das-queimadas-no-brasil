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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa179ef7-6d53-3cdc-9795-a718dbac5331 | -2.56104 | -53.87476 | 2026-01-04 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79f6462e-2036-34e1-8098-65d7e8d356f1 | -2.11221 | -53.48207 | 2026-01-04 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5ccfd78-4990-3a00-adb1-605909c39570 | -3.06632 | -54.02795 | 2026-01-04 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af40853b-fd21-351c-84f6-7b32091ccb26 | -18.81576 | -51.61572 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3f34da2f-ef36-357b-8ea7-37c795afd25a | -18.81736 | -51.60588 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 936447c3-f91c-3890-a571-7abbcf51bb1b | -18.81633 | -51.60919 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b894a155-3ab6-35f5-a534-ca4aed45a2d4 | -18.82258 | -51.61667 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1cf092ea-86b8-3f46-ba28-bc3a4721d971 | -18.82317 | -51.60999 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 34267185-4dbe-378c-a077-b11eae9cb249 | -18.82367 | -51.61323 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e15e974b-6e37-3ee5-aa4f-b0b2258c8726 | -18.82311 | -51.61998 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1741ce98-9655-328d-b56b-3cf0ddd770ec | -18.81683 | -51.61238 | 2026-01-04 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 14d4e1f8-f0dc-3e24-8a9e-3b50898b401a | -13.80151 | -39.00079 | 2026-01-04 05:37:00 | AQUA_M-M | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| dc5fed55-95d5-3168-a031-da580a62084b | -13.80016 | -39.00996 | 2026-01-04 05:37:00 | AQUA_M-M | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 59ef879f-694b-3784-8a01-185e55d96020 | -18.81998 | -51.59954 | 2026-01-04 05:40:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 773a8d3a-8d69-3ad3-be98-ee765db0e71e | -18.81828 | -51.59123 | 2026-01-04 05:40:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 1fe8a2ac-9ded-3a0f-9151-faabec1bf3dc | 2.54618 | -60.35749 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ce509b5b-5f1b-3ebe-b0da-5b315e4b4312 | 2.55371 | -60.36189 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65690f63-0f8c-34d0-92b5-7f09269c6513 | 1.82965 | -60.8697 | 2026-01-04 06:18:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84a478e5-ca42-3d83-ac62-64eef7bc5009 | 2.54715 | -60.36337 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f3e5a2b9-5bdf-3f98-b877-393734b0bbc2 | 2.55275 | -60.35607 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| eb58e20d-29c7-35ac-b652-bf4666aab8d2 | 2.5506 | -60.35719 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ef48b0d5-d235-3cce-967a-cdf0b92727b4 | 2.55159 | -60.36301 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b39caa49-9832-3945-9145-e34474ee72b1 | 2.54502 | -60.36441 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 453e9fa4-d666-3014-bed8-b1419e7cb2e3 | 2.55356 | -60.56616 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bc83114-39d8-3213-9e2a-cb2e5a4f8398 | 2.55275 | -60.56656 | 2026-01-04 06:18:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12273c0b-bc41-31e4-a392-276bc26ef241 | 2.55096 | -60.35217 | 2026-01-04 07:11:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6a6c5c92-e5e9-324c-8777-04405c43b5af | 2.55229 | -60.36095 | 2026-01-04 07:11:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |


