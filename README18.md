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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 193ce7bf-fa52-3e44-9135-3e28dae751aa | -10.9882 | -47.0362 | 2026-06-05 15:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 94bca0ad-25e5-3592-a2b7-3aa433365e78 | -10.8573 | -53.7425 | 2026-06-05 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 7966542d-3fad-305f-a1a1-872b9c059e0c | -12.7272 | -54.1988 | 2026-06-05 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 988a413c-e2ba-3772-b0ef-a31af1543a5d | -10.8573 | -53.7425 | 2026-06-05 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 9fdb2a40-98cd-3192-989d-38a694752796 | -11.5274 | -56.1236 | 2026-06-05 16:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 640ff9e3-48c0-39d5-921e-a369278c2e71 | -12.0923 | -51.9966 | 2026-06-05 16:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 7d9f9b57-bdb9-31b6-be7e-9d6814e34eaa | -11.5085 | -56.1251 | 2026-06-05 16:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0f97aa28-b44c-3105-a2e1-217dd282888f | -16.5973 | -58.2365 | 2026-06-05 16:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 1559f24c-48b9-3dc7-a61d-70eab3a2846a | -11.5085 | -56.1251 | 2026-06-05 16:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a6b298ff-8d60-326e-bdc1-51c966599620 | -16.5973 | -58.2365 | 2026-06-05 16:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| dfcec5c2-029b-319c-9815-4543185f7cfc | -10.8573 | -53.7425 | 2026-06-05 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 469ce0cc-f3eb-34a9-98b2-4e8e1f4151e2 | -12.0923 | -51.9966 | 2026-06-05 16:10:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| c60f020d-3b69-38e9-bdb6-0c9486920814 | -11.5274 | -56.1236 | 2026-06-05 16:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| c46649c3-4ac1-36b2-a318-e88fb3e9c6ba | -12.7272 | -54.1988 | 2026-06-05 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 664713a5-19de-3b47-8d06-a47759e9bbdd | -11.5085 | -56.1251 | 2026-06-05 16:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d3d687c9-1349-329c-a828-8237e333f810 | -16.5973 | -58.2365 | 2026-06-05 16:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 665c35c4-744f-358c-8661-92902b725f00 | -12.0923 | -51.9966 | 2026-06-05 16:20:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| b5f57803-c2bc-3d34-b059-11314433b5a5 | -10.8573 | -53.7425 | 2026-06-05 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| df238a75-b187-358f-a91f-e2fab1de4024 | -11.5085 | -56.1251 | 2026-06-05 16:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3af55b9b-cd3f-38fb-947f-d855d4866116 | -12.0923 | -51.9966 | 2026-06-05 16:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 132.9 |
| 5f74a2eb-2544-3128-ae29-0ce1fb743ffc | -10.8573 | -53.7425 | 2026-06-05 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| f3302c93-23ee-3d04-b2d6-6c3622868607 | -16.5973 | -58.2365 | 2026-06-05 16:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 59317631-744c-353c-af0c-9dd0e766daef | -12.0923 | -51.9966 | 2026-06-05 16:40:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| ccb51a54-49d9-3a1b-a103-f7bfceedf005 | -10.8573 | -53.7425 | 2026-06-05 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8630dab8-8a79-3b3d-b9c8-27e006127ba0 | -11.5085 | -56.1251 | 2026-06-05 16:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 284e5501-dee7-3261-9a87-f2c1a0324e40 | -16.1461 | -58.4862 | 2026-06-05 16:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |


