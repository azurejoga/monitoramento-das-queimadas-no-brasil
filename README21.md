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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59fb427a-10fe-31e7-a931-f3d33af4257d | -5.0418 | -41.11 | 2025-11-12 12:50:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 92.1 |
| 4ca520c7-6c89-3bea-a822-428d27a4f232 | -7.627 | -37.98 | 2025-11-12 12:50:00 | GOES-19 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 70e01052-7162-30b0-84f1-0fa6410a56bd | -5.0418 | -41.11 | 2025-11-12 13:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 112.6 |
| 2eb300a3-1960-3b47-9793-626270275be8 | -5.4922 | -39.1751 | 2025-11-12 13:00:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 102.0 |
| 467707dc-dcd4-39ca-8c37-ce12adea2a05 | -7.627 | -37.98 | 2025-11-12 13:00:00 | GOES-19 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 100.7 |
| b8a7532d-dc39-3388-b83e-91afaf1d4b70 | -8.2497 | -35.8316 | 2025-11-12 13:20:00 | GOES-19 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 130.2 |
| 0f856565-6e4e-37b6-b2a0-1c32fc8b7fdc | -4.8244 | -40.1491 | 2025-11-12 13:30:00 | GOES-19 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 74252447-dbcc-3ada-9e1b-f42bce29ad1c | -7.1229 | -41.8673 | 2025-11-12 13:30:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 6d91238f-001c-316f-81ab-e470b556bee3 | -8.2497 | -35.8316 | 2025-11-12 13:40:00 | GOES-19 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 137.8 |
| 6cb74f5b-a524-35bf-9ea2-742b349f17c6 | -8.2497 | -35.8316 | 2025-11-12 13:50:00 | GOES-19 | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Caatinga | 137.1 |
| e8323133-6575-3f04-b6ac-7ac0251dc1d9 | -9.8765 | -36.0806 | 2025-11-12 13:50:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 141.4 |
| 5e00aff0-6a21-3843-94c2-c63563005d84 | -9.3029 | -40.485 | 2025-11-12 14:00:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 8ade082f-27f0-3097-8606-8ffec1588b0c | -7.0271 | -38.8454 | 2025-11-12 14:00:00 | GOES-19 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 107.1 |


