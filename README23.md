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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 177663f2-cbc0-3906-96ec-d1d5ca01cacf | -4.5429 | -48.0151 | 2025-06-17 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d0655dd9-14f9-371d-a5f0-077b6f4de0cf | -10.8694 | -54.3151 | 2025-06-17 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5e718c05-a974-30da-884f-d1e6baedaca8 | -10.9355 | -56.8322 | 2025-06-17 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 219.3 |
| 4afab216-de63-3354-985f-c31b95f33845 | -7.2605 | -44.6421 | 2025-06-17 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c19af708-7c65-3702-bced-02e9b529cb83 | -10.9167 | -56.8336 | 2025-06-17 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| d95ad068-3898-3f85-92e0-d4f1f807c1f2 | -10.9353 | -56.8522 | 2025-06-17 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 227.8 |
| a498fd8d-a7b9-34f3-bb0c-0cf6a0bb9a6e | -10.8694 | -54.3151 | 2025-06-17 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0a7617f5-c6fa-36c5-8116-94a033b04ba5 | -10.9167 | -56.8336 | 2025-06-17 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 6c00c126-13ec-3132-903b-223b74a97330 | -10.9355 | -56.8322 | 2025-06-17 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 294.7 |
| cae5e45e-8cbe-308c-a355-a76b63380c94 | -10.9164 | -56.8536 | 2025-06-17 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 154.2 |
| f8237ce5-ee15-38d2-9525-ad2d1ecff13d | -10.9355 | -56.8322 | 2025-06-17 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 353.1 |
| 96777440-1460-38c4-a135-eb2dc888bbab | -10.9167 | -56.8336 | 2025-06-17 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 151.4 |
| ac57a456-6f5a-3518-a3a2-da9f1b76f382 | -13.5854 | -54.2721 | 2025-06-17 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 8e4e45d9-2231-36d8-a440-46e523d4483b | -10.9164 | -56.8536 | 2025-06-17 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 7b796483-74d2-31ce-81e6-0009d4c34797 | -10.9353 | -56.8522 | 2025-06-17 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 269.0 |
| 02337aa4-b398-37a6-b7db-923d43ff3d1a | -10.9167 | -56.8336 | 2025-06-17 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 190.9 |
| e65edc36-16b4-3c57-b02f-64ec6940532b | -10.9164 | -56.8536 | 2025-06-17 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 192.8 |
| 9adcbe87-4fcf-3d31-8134-36e1af5ded31 | -13.7454 | -45.2388 | 2025-06-17 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 351d9ff6-0db4-35b2-bdd1-d7a43473f966 | -10.9353 | -56.8522 | 2025-06-17 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 302.4 |
| 7ea7627e-3769-3849-8065-9b6c212ab6f6 | -10.9355 | -56.8322 | 2025-06-17 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 306.9 |
| f4c62b92-b3ca-3314-94e8-590497cb8eed | -10.8694 | -54.3151 | 2025-06-17 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 4091aaeb-9e58-3aaf-88e4-f4a0bbc7776d | -10.9167 | -56.8336 | 2025-06-17 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 60ee2aa3-f535-3bb4-84f7-3d5afe17f08e | -10.9164 | -56.8536 | 2025-06-17 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 85c8e518-3919-3893-8551-897cdbb507d8 | -13.7454 | -45.2388 | 2025-06-17 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 20cab0a2-8e66-339f-9c7d-8d750ea49894 | -10.9355 | -56.8322 | 2025-06-17 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 340.6 |
| 2526150c-a6d8-3841-8be1-a2d5b1bde65d | -10.9353 | -56.8522 | 2025-06-17 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 247.8 |


