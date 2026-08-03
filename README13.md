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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cb022e7-efa1-3731-83a6-3fe26fe0c3ea | -10.5741 | -46.7745 | 2026-08-03 16:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 650050f9-624b-348f-9a0a-90dec64638d3 | -6.57 | -55.136 | 2026-08-03 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d02bacee-a8f9-3a9d-9882-31f250bcd8f9 | -5.4762 | -45.1262 | 2026-08-03 16:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 140.1 |
| af4f2ca1-ed20-32af-8e8c-e68a24d891fb | -2.9581 | -50.3359 | 2026-08-03 16:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ff9582f1-7057-30ed-9978-692cc7bf4d81 | -6.9579 | -52.827 | 2026-08-03 16:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 654a5a0c-35a8-3d37-bf80-df4489e29ed4 | -6.5699 | -55.156 | 2026-08-03 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 380.1 |
| 56b8d7c3-049d-37a7-8d3f-1a12c518281d | -6.5514 | -55.1569 | 2026-08-03 16:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 602.7 |
| ad5cfe96-5177-317f-bf9c-84964356e056 | -11.1159 | -49.9138 | 2026-08-03 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 280672c8-d96b-398b-a498-1b39eeffd95b | -9.9565 | -46.22 | 2026-08-03 16:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 9efb44cc-12e4-32e6-89ce-d642032b2dd0 | -10.6312 | -46.7675 | 2026-08-03 16:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 907aaf1f-3815-3a6e-a094-229700fd3495 | -6.9579 | -52.827 | 2026-08-03 16:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 6f61d3a1-74a0-34b2-8995-6185779074d5 | -11.5856 | -50.2472 | 2026-08-03 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| acfdffd1-daa9-33da-8dc0-b2ed8a2e3a1d | -10.2053 | -50.097 | 2026-08-03 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| e8c190d5-eb22-348f-bb3f-3c0efc8deb02 | -8.9302 | -45.2041 | 2026-08-03 16:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 79636ff2-778d-3def-8b13-a38595b3fecd | -6.9581 | -52.8065 | 2026-08-03 16:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| d6036cec-b030-3b51-bfca-80911645512f | -6.5957 | -45.4275 | 2026-08-03 16:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 506f2aa7-4bde-39d6-969e-c2e7347b2d6b | -11.5853 | -50.2687 | 2026-08-03 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| ebbbd9a9-c906-3836-89be-14a4221bed38 | -6.1485 | -45.2137 | 2026-08-03 16:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| e5cb6417-599d-3d41-b3b1-e884245c8009 | -9.9565 | -46.22 | 2026-08-03 16:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 940cbc08-5497-3780-a971-d9709be4517e | -2.9581 | -50.3359 | 2026-08-03 16:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 38bbecf0-73a1-3dbc-b649-a492ef517126 | -9.9375 | -46.2222 | 2026-08-03 16:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| f3da8063-0b04-3197-a33f-e12a7f6e903b | -6.5699 | -55.156 | 2026-08-03 16:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 388.8 |


