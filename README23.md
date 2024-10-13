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
| 39e60d68-2f8a-3da9-9cd5-313d0ddafeb0 | -16.892099 | -57.800301 | 2024-10-13 01:41:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ef0f46c-b4ec-39c3-99f9-b9a86e7d9ad8 | -15.9449 | -59.082802 | 2024-10-13 01:42:10 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4397c4b-e939-3b3e-8f51-a2357c856ad4 | -15.9474 | -59.092899 | 2024-10-13 01:42:10 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a98e2a7f-ff73-3dfd-8cab-a823ccab119b | -15.9499 | -59.103001 | 2024-10-13 01:42:10 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2bd4f53-9b2d-3b9a-86d6-100217efdded | -15.9523 | -59.113098 | 2024-10-13 01:42:10 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b506a492-072c-3a19-8049-eed5486fa6e3 | -15.9351 | -59.0853 | 2024-10-13 01:42:11 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad5ae7c2-6cc1-3b6a-86c1-0791ff675990 | -15.6845 | -59.331299 | 2024-10-13 01:42:16 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b7a0812-de73-3dc2-bb92-28267882879c | -15.6869 | -59.341099 | 2024-10-13 01:42:16 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 046ab176-6b09-345b-a271-bf494246ef6a | -15.6748 | -59.333801 | 2024-10-13 01:42:16 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5141c46-2d54-3fe9-b3de-fa2b2307cfc9 | -15.6455 | -59.341301 | 2024-10-13 01:42:16 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee527a18-3089-324f-b372-f0ee48199f88 | -15.6479 | -59.3512 | 2024-10-13 01:42:16 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebc364d4-4589-3787-bf33-8ed0d1bab6ea | -15.6211 | -59.368599 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1f9667-3c82-3f04-83c3-ee5fe88fdb04 | -15.6235 | -59.378399 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 510f04dc-b201-3b79-b458-497ea7815793 | -15.6259 | -59.388302 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3b0f0b-da6e-3410-81f4-859d989a9d64 | -15.6162 | -59.3908 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bd7a892-d965-3bd5-924e-61dd7063d1de | -15.6185 | -59.4006 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78a1e87f-f889-389a-a2de-696691715f93 | -15.604 | -59.383499 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb187e79-47b4-3337-93aa-b2548b8c312e | -15.6064 | -59.393299 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9fb9a3f-fff9-3d3a-a137-f70aa44fff04 | -15.6088 | -59.403099 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e46ae97f-c881-3d1d-8dbb-b71caf4be890 | -15.6111 | -59.412899 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11bc8d9f-3efb-3cc4-8370-6acbe4936206 | -15.6135 | -59.422699 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cefbb904-b450-304b-aaf5-3f58917cfdb3 | -15.6159 | -59.432499 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d95ff0e6-56ec-3d7f-a741-2b0f90f99d27 | -15.6182 | -59.442299 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfdb8176-38ab-3c6c-b909-39214022f8bb | -15.5943 | -59.386002 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa160267-227c-36a1-a5f1-608912f3a018 | -15.5967 | -59.395802 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71d7239b-4dc5-3ecd-87ec-a46de7826c5c | -15.6014 | -59.415401 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab8454b-274f-3b6b-8b46-61fb313541eb | -15.6038 | -59.425201 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeb9e864-421b-3c93-a31a-8382fdfb0c41 | -15.6062 | -59.435001 | 2024-10-13 01:42:17 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8201a59e-97df-38fa-b8a2-6a62c971acbf | -15.6498 | -59.917198 | 2024-10-13 01:42:18 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb573ee-db13-3980-9043-1cc0e54c5d34 | -15.6543 | -59.935501 | 2024-10-13 01:42:18 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afdd4696-8c2d-370d-af7a-d47faffb353d | -15.6565 | -59.944698 | 2024-10-13 01:42:18 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f03c94a0-b662-3470-9962-cbaa165a77ff | -15.6294 | -59.961399 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d41b0c6-de10-3a62-b4d0-30ecbd740fd0 | -15.6316 | -59.970501 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 464190b6-4101-3884-b038-5df0c16c8058 | -15.6338 | -59.979698 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d625c478-32e8-33ef-a4f6-3e6b4c8b9fc1 | -15.6218 | -59.9729 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3afd62a-53f2-3b7d-b456-405be1b929d6 | -15.624 | -59.982101 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5986ff9b-a251-309b-94b1-5443dcaa34f5 | -15.6401 | -59.919701 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| de86bb8c-6e4c-3f36-86ac-d5302d56e870 | -15.6467 | -59.947201 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d20e8f3-00d2-3c89-8610-4e706672ff7f | -15.6511 | -59.9655 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75feb6e0-0244-385e-be2a-84fccf813e55 | -15.6303 | -59.922199 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8d2addc-c026-3a59-a607-15a3fcf54bb4 | -15.6369 | -59.949699 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36a4ca50-1d18-3b93-b017-cac4e4748222 | -15.6391 | -59.9589 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9d75874-3964-367a-9213-95ea7f1623f9 | -15.6413 | -59.967999 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30bd1091-588a-303b-90a5-ca36f1b27785 | -15.6435 | -59.9772 | 2024-10-13 01:42:19 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55fdff8b-9c62-39b6-9aae-88689123e038 | -15.1661 | -59.712299 | 2024-10-13 01:42:25 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba8b254-14a1-3be1-8238-77965e2646d8 | -15.1684 | -59.721901 | 2024-10-13 01:42:25 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6dba9a13-add6-3396-af54-12a08e363bc9 | -13.775 | -60.5532 | 2024-10-13 01:42:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dfd37c26-2938-3090-b9fc-d3aa4a5811df | -13.7632 | -60.5467 | 2024-10-13 01:42:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e58d0a1-55cf-37e7-8d3c-5c9eb053209b | -13.7653 | -60.555698 | 2024-10-13 01:42:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90a1c3f2-cb6d-39cc-8aea-53b5fb5f5e71 | -13.7674 | -60.564602 | 2024-10-13 01:42:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e96845f5-9f9d-3ed3-b23d-b9e8a8e7ce25 | -13.7534 | -60.549099 | 2024-10-13 01:42:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c134c45b-e9bc-3d72-ba2a-e74fa7350ab0 | -13.7555 | -60.558102 | 2024-10-13 01:42:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 423577db-3f16-32a8-b2b2-454e77a72c54 | -13.7577 | -60.567001 | 2024-10-13 01:42:51 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b73f690f-f8b6-3489-b85b-d78261aa1dba | -13.7458 | -60.560501 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18e02993-1e49-3d03-a95e-2e9373b29441 | -13.7479 | -60.5695 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3ef778-a824-30d4-bddd-90e86fa5260a | -13.7382 | -60.571899 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6ff6db8-1d82-3b3d-b087-3b3c48764fda | -13.7403 | -60.580799 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a44a494c-165c-3e00-9bcb-34ecd947d3c2 | -13.7284 | -60.574299 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4247b1ba-e3b0-3ced-8fcd-7eacb78fc84e | -13.7305 | -60.583199 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05388030-f6d6-3fd8-947b-d5e4ef2cacc8 | -13.7326 | -60.592098 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f5e5ea2-2c66-3f28-a6bc-c409e53f226b | -13.7229 | -60.594601 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 746729ff-d590-3919-89f9-22dea661eefc | -13.725 | -60.6035 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97b2003e-57a4-3007-9cbd-4474009aaffc | -13.7152 | -60.6059 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eda9bcd0-212b-39b4-938c-1020a0a63dfd | -13.7173 | -60.614799 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc908aa-3694-36da-a22c-a1bf54bd57fa | -13.7195 | -60.623699 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc8e4d3-99d8-30a7-ae20-b7840774cb1d | -13.7216 | -60.632599 | 2024-10-13 01:42:52 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fae8562d-319f-3600-b8f9-79bcbb1f2280 | -13.2913 | -60.6922 | 2024-10-13 01:42:59 | METOP-B | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 09d8dbc1-b28a-3af9-b6d7-bd5cef8cb88a | -13.5129 | -61.721901 | 2024-10-13 01:43:00 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea5eaba5-accf-32c8-98d3-3888eb8f6d41 | -13.3612 | -61.3382 | 2024-10-13 01:43:01 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99211d46-a005-389f-ab22-ad34280b358e | -13.3773 | -61.938099 | 2024-10-13 01:43:03 | METOP-B | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 467f144f-97a3-34ff-b2f9-01fbeb229fe8 | -13.1404 | -62.297001 | 2024-10-13 01:43:08 | METOP-B | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 89e38ad5-9e43-3cdf-8908-b3c6dc795ceb | -13.0136 | -62.463501 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3240949-843c-34d1-a221-2e7eb8751e0b | -13.0038 | -62.465801 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99a6c687-157b-3dae-9ae8-98c574d08ef9 | -12.994 | -62.468201 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 198c58fc-14e3-398e-baf6-884d681b2b22 | -12.9957 | -62.4757 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| def835d3-5355-31bb-a8b1-adb62c3256de | -12.9975 | -62.483299 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0accdcfa-9490-3f60-84dc-78d33f6c2d69 | -12.986 | -62.478001 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ba5c5f5d-0fd7-3510-b7a4-e5bd94132549 | -12.9877 | -62.4856 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6adb33a2-e299-3dd9-9fb6-6032a99fbbcf | -12.9895 | -62.493099 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a7d26f68-47a3-3a20-bb28-8d12f4f50eb0 | -12.9912 | -62.500702 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 832dc220-0b26-3608-b1ef-ae6a4e7a4340 | -13.0107 | -62.630402 | 2024-10-13 01:43:11 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 958f6d78-1199-3d6e-b4c8-1906fcc1e462 | -13.0018 | -62.726601 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5302a436-893b-35fb-9050-16b97d7b6e93 | -12.944 | -62.519798 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2d033905-4463-38fb-b74b-49c9b67c7895 | -12.9903 | -62.7215 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6926c5ac-9827-324c-85f7-d159eeaa5bd1 | -12.992 | -62.728901 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2a548f41-e927-3402-a2fd-794b93b2fcfc | -12.9937 | -62.736401 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c9a3aab2-1405-3452-b63b-b62ef50a22d6 | -12.9325 | -62.514702 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| edd79533-81d7-37c6-b7fb-16b208dd3283 | -12.9342 | -62.522202 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 16886711-5a78-30bc-85b6-1d235dbe8cbb | -12.936 | -62.529701 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 044f6908-45a7-363c-8c85-617b88cc73f8 | -12.967 | -62.664501 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d49014f-f4bf-343c-80df-b1c13bf83b88 | -12.9687 | -62.671902 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa0b6ca0-b60e-34a3-b8f4-06d4f6f51655 | -12.9704 | -62.679298 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 58eb69c7-5c27-3e2f-9576-93fbccb5c1e9 | -12.9772 | -62.709099 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5a5275-e82f-3a5d-9d47-bdba6ecc64c0 | -12.9789 | -62.716499 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3a8d854-3158-34f1-92a8-825f4a4742d9 | -12.9806 | -62.7239 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b175b43-878b-37a1-af9d-7f4ce33572b3 | -12.9823 | -62.7313 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f03cf11-e2a3-3ee3-a42a-267ab8f86a62 | -12.984 | -62.738701 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de623d09-72f2-3ab9-933b-68d437054326 | -12.9857 | -62.746101 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cddb2226-bda2-329c-9fac-2f4cdaf8af35 | -12.9874 | -62.753502 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80556491-bb28-35a0-a700-60423b66ada1 | -12.9175 | -62.4944 | 2024-10-13 01:43:12 | METOP-B | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
