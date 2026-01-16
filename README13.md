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
| 3ff2e28e-3f2c-3a15-814c-f1f3c6ea1299 | -20.45 | -57.8476 | 2026-01-16 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| fdc26ec1-3224-31c4-b78b-c71d99c86f93 | -20.4496 | -57.8686 | 2026-01-16 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 126.4 |
| 11706e38-429c-3177-a608-a3b573ca5ff9 | -20.45 | -57.8476 | 2026-01-16 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.3 |
| e968decc-47e3-34f6-b589-59b62c63c0fd | -20.4496 | -57.8686 | 2026-01-16 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 17a723bf-341d-30cd-b29c-ac9fee1e2758 | -20.45 | -57.8476 | 2026-01-16 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.3 |
| d178ecb6-6627-3bf8-8e16-a183e99b04aa | -20.4504 | -57.8267 | 2026-01-16 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.3 |
| 8b0bc851-1277-3bbc-a497-c05f6af0d4e3 | -20.4496 | -57.8686 | 2026-01-16 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.2 |
| b0f48c3f-ac51-3b44-a4d2-6b1f27a04d5c | -20.45 | -57.8476 | 2026-01-16 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.4 |
| e4e0e2c4-1d0e-3a09-b3fc-8b7b70d5b532 | -20.4504 | -57.8267 | 2026-01-16 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| e8a6f274-f581-3404-ab65-bfd26c12ac1e | -6.9982 | -42.878 | 2026-01-16 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| be2fff93-2a94-30ea-afbd-1a3d9308b80e | -7.2599 | -43.041 | 2026-01-16 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 7803cb99-4ab1-3f8d-908d-5f1de97e2cdf | -6.9793 | -42.8798 | 2026-01-16 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 8b0d1325-7d20-3776-847a-9ca78de074cc | -20.4496 | -57.8686 | 2026-01-16 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.2 |
| d3fb11fe-5b34-324e-9d7a-70ff67028fa1 | -6.9982 | -42.878 | 2026-01-16 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| e208c21a-6f87-3b87-ae7d-5d16a2f9ec54 | -20.4504 | -57.8267 | 2026-01-16 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.5 |
| 689bf162-9c92-3e9d-a657-2a4c6d8b6177 | -20.4496 | -57.8686 | 2026-01-16 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.4 |
| a093fdef-c49d-39fa-8fed-fab2dbc29d06 | -20.45 | -57.8476 | 2026-01-16 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.9 |
| d39b93dc-6eb3-3109-b742-477cdd66c38c | -20.45 | -57.8476 | 2026-01-16 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.7 |
| 3e1b00de-0bc2-3d0f-a4da-c113f73f3dd7 | -20.4703 | -57.8449 | 2026-01-16 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 1805ca47-e22b-399f-8451-a37f89a77c29 | -20.4504 | -57.8267 | 2026-01-16 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.8 |
| 65ea35ab-8645-3e9b-afb5-500025ca03f2 | -20.4496 | -57.8686 | 2026-01-16 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.2 |
| 0ef5da2b-e5b9-3dd4-a646-498776eee4d6 | -20.4496 | -57.8686 | 2026-01-16 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 0e5b6191-4a3d-333a-b241-42917fb1ff78 | -20.45 | -57.8476 | 2026-01-16 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 90c687a2-08f7-351e-805f-2039b8419442 | -20.4504 | -57.8267 | 2026-01-16 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 6fe0d8e2-c9a8-3fa0-91e2-9c0ccbfe5978 | -20.4496 | -57.8686 | 2026-01-16 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.7 |
| d748cb53-b9d8-3e75-9215-495ab5231778 | -20.45 | -57.8476 | 2026-01-16 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.3 |
| d27a033a-b92e-3439-8913-1de418d5925d | -14.2121 | -57.4098 | 2026-01-16 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 85ba07b4-93af-3c04-98d0-abe7b0693868 | -14.1948 | -57.2704 | 2026-01-16 13:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| f3841674-33fd-34b0-9ce8-b2f1bb6461c0 | -14.1948 | -57.2704 | 2026-01-16 14:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 537248e4-9a7a-3716-a0fa-94b0439bc613 | -20.5279 | -58.0039 | 2026-01-16 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |


