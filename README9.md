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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c5cd531-db61-339b-913c-63e023713d87 | -12.0502 | -45.2103 | 2026-04-23 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 279b272b-7f71-3dbd-9c85-ce8349e767ff | -11.7528 | -43.646 | 2026-04-23 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9a1f68c5-59de-3fd1-a0cb-7e64306a5c2e | -12.0502 | -45.2103 | 2026-04-23 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| afd72af2-75c5-3309-a559-5aa10ff74e5b | -11.7528 | -43.646 | 2026-04-23 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| daec995a-5cb5-3a31-ad31-bde6b2c4f8cb | -20.2068 | -46.759 | 2026-04-23 14:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 4bec4be4-44b0-322e-9b6b-5f2a16d1af38 | -11.772 | -43.643 | 2026-04-23 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| c7392e68-47a4-3fb2-8540-9b315eee7479 | -11.7528 | -43.646 | 2026-04-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 7050d8bb-8e71-36a8-a70d-e24ed90066e1 | -12.0502 | -45.2103 | 2026-04-23 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 731100f3-7f86-33f3-a396-20ce5af4f60a | -11.772 | -43.643 | 2026-04-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 359be290-a4c3-319f-8d99-ac414eb4c58f | -12.0502 | -45.2103 | 2026-04-23 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 54fe1484-ad84-3844-bb9c-9c5808e7afa1 | -11.7528 | -43.646 | 2026-04-23 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1c5d59d3-4d99-32d2-ad00-c6150cd5a634 | -11.772 | -43.643 | 2026-04-23 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| b2d9a01d-3f02-30eb-a96b-3d968c1a63f7 | -11.772 | -43.643 | 2026-04-23 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 151.9 |
| c2e5e880-dd77-31d9-b073-f571abc7f6a5 | -11.7725 | -43.6193 | 2026-04-23 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 14bd1468-c972-3b9d-99d6-1bd2c67897f8 | -12.0502 | -45.2103 | 2026-04-23 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0537a372-5668-39d0-98cc-c8d2cabf8bad | -11.7528 | -43.646 | 2026-04-23 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| dc5055b6-8985-3065-b05c-95a4da6ecd98 | -11.7725 | -43.6193 | 2026-04-23 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 1cbf5cb9-6da7-3a9e-9cbc-8c5c4f6d153b | -12.0502 | -45.2103 | 2026-04-23 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 41673c62-5b29-3402-921d-8b1fe4b37615 | -11.772 | -43.643 | 2026-04-23 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| b61928b5-2c53-3a2f-ac43-097b0fa99a5e | -11.7725 | -43.6193 | 2026-04-23 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| adf9a0b3-1c30-3a93-8a91-2fdf75e4d13e | -11.772 | -43.643 | 2026-04-23 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 8bd0b688-d7a0-38e2-8c88-4764a8be69e7 | -11.7528 | -43.646 | 2026-04-23 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 5229ce92-1079-363f-ac8f-030101bc5085 | -13.4463 | -43.789 | 2026-04-23 15:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| bc33cbe8-5221-3c42-8a91-68648687069a | -8.7841 | -44.8315 | 2026-04-23 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |


