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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceb9c589-1dd7-3881-bcd4-fa0b8b93caa4 | -4.9643 | -43.7182 | 2025-07-27 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 42d017da-aef4-3c5b-a76c-eb8ed7e1a0bd | -12.0011 | -45.8143 | 2025-07-27 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dd30d2fd-df43-3123-893c-011866af743b | -6.4304 | -45.1011 | 2025-07-27 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8826e115-600e-3bc9-9564-63f8d79e8492 | -7.0886 | -44.909 | 2025-07-27 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 21ba668a-1c14-360d-9a15-195352e8b902 | -3.4 | -43.0148 | 2025-07-27 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 81a3acf8-ae69-382c-af20-c7455c1ce12a | -4.9454 | -43.7425 | 2025-07-27 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| efbb5882-620c-38e1-9728-70fa8d511699 | -2.9558 | -42.282 | 2025-07-27 14:40:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 0befbb61-0bae-31f1-bb3f-5da6ad12c9ec | -4.9643 | -43.7182 | 2025-07-27 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 82edf6f4-3048-325b-ba7c-4159d446c00b | -7.0041 | -42.3567 | 2025-07-27 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 199.0 |
| c702bf5b-e4ad-3b38-8137-6228c5ec9a5c | -18.0027 | -53.1584 | 2025-07-27 14:40:00 | GOES-19 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 04eda96d-866b-3260-a622-1dd82cd1014d | -5.9627 | -45.069 | 2025-07-27 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| d8578e7d-5dab-3491-96aa-88a59d2af510 | -12.67 | -47.0092 | 2025-07-27 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |


