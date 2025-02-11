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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c60a8c2-6460-3c44-a59c-9dc4cf0e2cea | -20.28701 | -54.99879 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1fcad90-78b5-3676-8cec-d41a34e78dfa | -20.29283 | -55.00448 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ac5b3ad-7c2c-3831-87c7-06a1a9d193c8 | -16.0842 | -60.06643 | 2025-02-11 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 343a7f2c-7c3b-3b2f-a06e-67a7f3378932 | -16.08473 | -60.06231 | 2025-02-11 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 602b2f0e-89fe-39e2-9273-ac398ad75703 | -20.28443 | -54.99928 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de5c2a90-bcdd-34bd-a345-38cc5f80ff6d | -16.08849 | -60.06701 | 2025-02-11 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2d895f1-07c3-30c3-bb98-55758e462032 | -20.28072 | -54.99831 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bb9dd40-7064-3c28-b206-fcacbecd45b7 | -20.2933 | -54.9993 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c79a019-5254-3365-92df-ce0b60689ece | -20.29028 | -55.00503 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3393679-3729-3a6e-8912-107819180249 | -20.28653 | -55.00405 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31bdd827-44f7-330e-a6e6-ca070b47923e | -20.29072 | -54.9998 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ce0a9dc-b763-3bdb-a6fb-2a1eb4eeca75 | -20.28488 | -54.994 | 2025-02-11 05:40:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff56ff4e-edfc-36af-987a-1b4528278489 | -30.1945 | -56.68859 | 2025-02-11 05:44:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.8 |
| d7c4f034-a482-3da8-9ef6-7647c8b3e7a9 | -30.18824 | -56.68822 | 2025-02-11 05:44:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 5522844e-37cf-36f8-aa49-a4009f6976ab | -30.19057 | -56.6883 | 2025-02-11 05:44:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| 1db92a0a-67f5-3eb9-bb1c-531d973c9652 | -30.19649 | -56.6942 | 2025-02-11 05:44:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 20727aa7-a696-328a-bd15-944d6f6c45a2 | -30.19683 | -56.68867 | 2025-02-11 05:44:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.7 |
| bc503c07-9b02-3dd0-b2e6-d5c61e5deea4 | -30.19023 | -56.69379 | 2025-02-11 05:44:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 5ee423fe-8258-38a5-b75b-c428903cc5b4 | -30.19419 | -56.69411 | 2025-02-11 05:44:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 3.8 |
| d6126ff5-eba2-3a4e-a0b4-0e1569a8e477 | -16.0843 | -60.06197 | 2025-02-11 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59cc5994-2b60-349c-a766-89a09754b7ff | -16.08377 | -60.06729 | 2025-02-11 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 808da61d-0e2d-3ed8-9303-57e9a86b1e95 | -16.0825 | -60.06599 | 2025-02-11 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b7cf9f9-26e6-33e2-9dbd-4e199638b6b9 | -16.08325 | -60.07254 | 2025-02-11 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


