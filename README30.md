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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcc69f39-597a-3a6c-895b-af51431bdaf3 | -10.5776 | -49.1316 | 2025-07-10 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b439626f-b63d-3303-b12c-2f8cc1bbf10e | -5.7887 | -43.6134 | 2025-07-10 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 023d7fec-d6b3-374e-90b0-79b12027dad8 | -6.1425 | -45.8676 | 2025-07-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| dc1de6d7-3f58-3a67-bd80-0121d5079048 | -10.5773 | -49.1533 | 2025-07-10 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1654da43-7f68-38b7-96b6-81e2ca86b956 | -19.3778 | -51.4008 | 2025-07-10 14:30:00 | GOES-19 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 145.5 |
| be0849d8-f315-30fe-8194-0f06e6ce9f4f | -6.8485 | -42.7979 | 2025-07-10 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 4e809bea-a509-3ebf-9853-d89c75759292 | -11.4397 | -45.0923 | 2025-07-10 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1c72800a-c7b0-3037-a0fd-054a1186054f | -13.8686 | -45.8421 | 2025-07-10 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 326eafd2-39fa-3f6b-9b20-f0f724e88865 | -7.0099 | -43.5098 | 2025-07-10 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 4b720e2d-97fa-3698-9388-21b9b1c01bb8 | -7.0102 | -43.4865 | 2025-07-10 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 91d10cb1-4ea4-39e0-87b1-d742a10c8b67 | -11.4397 | -45.0923 | 2025-07-10 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c306bcd4-5579-30b6-bb81-2c68e3e87289 | -5.7887 | -43.6134 | 2025-07-10 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4148d94e-afc6-3561-9bc7-76e6c3530315 | -6.8485 | -42.7979 | 2025-07-10 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| fcc7524e-06be-3da7-a9e3-c574e8b9ac33 | -6.1425 | -45.8676 | 2025-07-10 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 5558330a-315b-3f93-bd45-4b0d4193685b | -13.8686 | -45.8421 | 2025-07-10 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3ee89cac-d577-305c-b640-20c4a85649aa | -7.0102 | -43.4865 | 2025-07-10 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 161.5 |
| 094f63f2-1b9b-31be-a53a-1d47b7cee976 | -10.5773 | -49.1533 | 2025-07-10 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32603715-c33a-3aed-a99f-159f45ac7622 | -7.029 | -43.4847 | 2025-07-10 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 12680646-51c6-3a44-a00c-783e76a42d04 | -10.5776 | -49.1316 | 2025-07-10 14:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |


