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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfe50740-c1e6-37d6-a09e-f01cc626c25e | -10.7965 | -44.7437 | 2024-10-05 14:46:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 249.3 |
| da6d5f7f-c7bb-3c4c-b8ab-38f4f42b11ea | -10.7546 | -46.1667 | 2024-10-05 14:46:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| acf8d630-5e0a-39d6-8db4-a1b36a3cfaae | -10.6505 | -53.6994 | 2024-10-05 14:46:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 3fb64533-d933-3e4d-a440-d1f71bc559cb | -11.0966 | -54.2336 | 2024-10-05 14:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 280.9 |
| ab337bfb-f52d-3828-9026-6ec579e79e13 | -11.1155 | -54.2319 | 2024-10-05 14:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 199.1 |
| b2ea0008-2b39-3772-aafa-9513d5a3f31c | -11.2114 | -51.2052 | 2024-10-05 14:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 532f224e-12c5-3770-bb6d-25793d2db790 | -12.3292 | -54.0954 | 2024-10-05 14:46:16 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 29e12140-f62f-3e66-9d61-ddd71cb9d867 | -12.4948 | -53.1253 | 2024-10-05 14:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1098ba30-16e2-34b1-8b14-51c18924606a | -12.4945 | -53.1462 | 2024-10-05 14:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5f18e22b-a058-3210-b6cb-2ca0c0e0c8ca | -12.6723 | -54.0395 | 2024-10-05 14:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| ce6b84bb-583c-3800-99a1-eb084305bc25 | -12.6532 | -54.0415 | 2024-10-05 14:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 583db303-a1a8-3a3b-9063-7c0a08d6a8c0 | -12.9776 | -51.4706 | 2024-10-05 14:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| e2f04ee2-ad41-386f-92e1-32514f6cf0d4 | -13.1533 | -51.2573 | 2024-10-05 14:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3811fad2-3f5d-366d-9625-f3c32c048a4f | -13.2486 | -51.288 | 2024-10-05 14:46:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| f4a4af9f-299a-3be1-8e14-cde00cea4230 | -13.2019 | -50.6298 | 2024-10-05 14:46:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 4d41d198-77ff-3fa1-a76b-3e9bacefd4e8 | -13.538 | -51.1871 | 2024-10-05 14:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| fb28c967-9352-3586-9c61-f07c0f7a9e46 | -14.0202 | -45.0747 | 2024-10-05 14:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 54c43fb6-d32e-3d7a-bcf9-9930299d98c7 | -14.7744 | -48.0307 | 2024-10-05 14:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 217.1 |
| a0444310-e831-3e7c-9b07-e0e04d4d1185 | -14.7545 | -48.0564 | 2024-10-05 14:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| a22a827c-90a9-326c-a756-7cc788d9fef0 | -15.1826 | -48.0528 | 2024-10-05 14:46:31 | GOES-16 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| f11602ff-51c7-3961-9721-435c6118170f | -15.6697 | -47.1992 | 2024-10-05 14:46:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 8c4e955d-18cf-35eb-8230-e94f09f50285 | -15.6505 | -47.1799 | 2024-10-05 14:46:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| c506a499-a090-3c0f-bae1-9f2ed36c786a | -15.6702 | -47.1763 | 2024-10-05 14:46:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 340.1 |
| 692801ff-5c06-3929-ad11-07dabcd76897 | -16.95 | -47.1185 | 2024-10-05 14:46:41 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 112.7 |


