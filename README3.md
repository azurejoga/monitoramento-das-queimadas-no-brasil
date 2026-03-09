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
| f4b7a5e2-f43e-355c-a902-eb751d7fd7de | 1.71282 | -60.29305 | 2026-03-09 05:29:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3bac70ad-0e67-3557-9a21-96834793879b | 2.32092 | -60.22511 | 2026-03-09 05:29:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97f91aaf-cc41-3fbc-b760-cd43a2bfea6b | 2.88546 | -61.08467 | 2026-03-09 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61017537-fb20-3ee9-ad83-171fa0c969a2 | 3.2522 | -60.81739 | 2026-03-09 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8aef36a3-b3d4-3894-8144-56347b8cf06f | 2.88231 | -61.08827 | 2026-03-09 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18be2e02-4653-3bac-b94d-836bf8a34122 | 2.70902 | -60.24987 | 2026-03-09 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c7282fd1-b6aa-3840-abb5-698c2a8599be | 2.88006 | -61.09078 | 2026-03-09 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 09133364-1828-33fc-9d81-7c2735e1e53b | 2.88775 | -61.08211 | 2026-03-09 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f4f68c1b-79af-348d-b2e3-3b80ae5519d9 | 2.93005 | -60.41294 | 2026-03-09 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a304d740-9463-37f5-b515-656be397d7d0 | 2.92911 | -60.40743 | 2026-03-09 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a06727cf-3efc-398a-94df-b3c576ba6ba6 | 2.69579 | -60.25212 | 2026-03-09 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e654371-b8fb-3048-a7c6-9f97433fa894 | 2.88459 | -61.07965 | 2026-03-09 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3e79e67-275e-3d3b-bd87-a67fec2e2a33 | 2.88315 | -61.0933 | 2026-03-09 06:18:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| acd17086-2874-39b7-bff5-4e2de9a383e7 | 2.70999 | -60.25559 | 2026-03-09 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f0d4667-64a0-35c1-a681-f20ebce5927d | 2.70241 | -60.251 | 2026-03-09 06:18:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c66333c2-7feb-35c0-9164-8b9df7dcbf94 | -9.37523 | -36.4573 | 2026-03-09 11:10:00 | TERRA_M-M | QUEBRANGULO | ALAGOAS | Brasil | 2707602 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |


