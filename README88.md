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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cbc5052-9d76-3a81-97a8-c90920c23436 | -9.10758 | -65.76546 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c6590c43-956c-3677-add0-138c0ce9fe96 | -9.77375 | -64.25037 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 049bf4be-fba0-3d20-84a0-2f1bf0c34c36 | -9.10918 | -65.79597 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cd42acc-257b-39fc-b0a1-76cadeaec222 | -9.12762 | -65.77792 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 840a2430-1439-35ae-b92c-905106ae22df | -8.96222 | -65.96897 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67d59e0f-c199-345b-9e2d-12c391f5a199 | -9.13635 | -65.79828 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 273040bc-12f2-371f-a7a5-c38a2c57b973 | -8.94537 | -67.71332 | 2025-08-29 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6196bace-8525-38cf-b7bd-0baf0ea86ca4 | -10.29336 | -64.49352 | 2025-08-29 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a985def-133a-37fe-8d4a-92fdddd9e5e4 | -8.85398 | -68.50575 | 2025-08-29 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35a7ebcd-04df-340a-b516-2b9816112936 | -8.70144 | -69.42064 | 2025-08-29 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c77a1a24-a5c2-30ac-831c-2e083fccb8d4 | -9.11065 | -65.78497 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 247453ed-9942-3470-9222-19de80907719 | -9.10707 | -65.76929 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c1fe9859-65b9-3ffd-95df-575d07f23e26 | -9.12395 | -65.76217 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de5e2385-7128-3b1d-9489-f590f6265c5c | -9.17623 | -65.79636 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15d004d5-fc0d-3f18-9f2e-03fb4beaa55b | -9.54987 | -65.69438 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9d5cecb-1260-3265-8770-fa1e5895a0f4 | -9.11185 | -65.76826 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6116121f-ca90-362d-9613-f62d4f4fb66e | -9.17212 | -65.78438 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a4e6e42-d8ed-3120-8c0d-d129225e98be | -7.99542 | -70.28484 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5f7d3eb-4afa-3b49-bcac-41f8568286e9 | -9.11114 | -65.78127 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a256339d-69de-3076-97ef-9d63bfbe2a8a | -9.78613 | -64.25207 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 968d1822-3f81-326e-8be5-381dbe49e963 | -8.58063 | -70.11739 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f7e3d46-3f60-3d53-a345-6315d88bdaa9 | -9.10967 | -65.7923 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fd6ccfe-0e66-3e6f-a35d-e2dc774c29dc | -9.54783 | -65.69212 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67189f70-cd64-3f6e-96a2-cc81bdcbc6c5 | -9.104 | -65.74044 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a9f8b0b-5d02-3edc-b23e-f745b681f7d5 | -9.12348 | -65.76591 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3e306338-21b6-3971-924f-26f0aaa334a7 | -9.78113 | -64.24152 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d10ac965-8575-3569-9594-e850f647e28a | -9.10657 | -65.77302 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ad1567d2-fb38-37da-b5cd-7e0e62b8f5ee | -8.95762 | -65.96814 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef3e1069-ee36-30d6-bcd3-4c9a23dbc9c7 | -9.88243 | -64.69489 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b68269e6-65b0-3766-8dfb-3595d463bc71 | -9.1294 | -65.29144 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ea11641-91a1-3c0d-996b-12a8b7d2af55 | -8.76984 | -70.57713 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fd0b10a-34e1-35f6-a02e-97c5f621b0f4 | -9.16099 | -65.78282 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 185da9d2-ed92-3432-943c-b596ea9d013d | -9.13618 | -65.28426 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69d39555-12c4-36e2-8b79-a70727fe5bf6 | -9.73272 | -64.90591 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 02da5ce7-53f6-31ae-bb73-da24b7d5928a | -8.95723 | -65.96453 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3b5927-0c38-3b1b-9547-6fb8424ae854 | -8.7765 | -71.30082 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30098d7e-a2c6-3a43-ab59-b792dd86d2b5 | -8.27874 | -70.07854 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59d939e9-d3e2-3498-b230-82d9395929a4 | -8.35531 | -71.19081 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c79d99dd-4efd-336f-b9d2-691a6c1a838a | -9.12109 | -65.78484 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c1b9646-44b6-3424-af7a-ed9b74c15228 | -9.12061 | -65.7886 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74eeb714-f3c5-3d81-a065-cf60989ba37f | -9.15591 | -65.7783 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26b6a64d-2036-3615-a33b-67bf49819e91 | -9.11164 | -65.77756 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8f43878c-0ece-3015-a00d-21bc1694dc81 | -8.03897 | -70.0966 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 724f8235-1875-39db-ba51-f0bb7c65fe01 | -9.11647 | -65.77653 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 99eb45f4-75d1-3ccd-82a3-5f66928c6028 | -9.77315 | -64.25523 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 60a4fe12-eef3-3840-9ead-2226a7f1e70c | -9.11505 | -65.7878 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd7a093d-af94-3403-88f1-131c7e6505be | -9.06771 | -66.06404 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc7a3f0f-4d83-3e2c-bc00-32392ce54c4a | -10.03578 | -67.83244 | 2025-08-29 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b60ac94a-6308-39c1-87ba-d0531351f9f3 | -9.11055 | -65.74317 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7e9fa77-26e8-3bd6-95b2-7616a8d9acdf | -9.12983 | -65.80505 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4fb66444-f583-3790-8be0-61d47162703f | -9.16607 | -65.78735 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 477c559e-5512-3abf-81d1-0817c4b5c6de | -8.95222 | -65.96019 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a1b80f-b0d8-38e6-8005-d4eeef36f604 | -8.93129 | -71.27681 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4a80dc0-5960-3e9b-9f92-83636a91b6ff | -8.534 | -70.74706 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8db8e3f5-69ae-31b5-b458-33aa44002687 | -9.72904 | -64.90486 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a3b57a63-a580-3dcc-85c0-ace49d4c5c06 | -9.11137 | -65.77206 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 73be6109-c574-3789-bee5-c8b26c719b79 | -8.58127 | -69.68771 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb4cceda-d9d2-3d08-9397-345e9ff70c52 | -12.42459 | -63.91462 | 2025-08-29 06:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2e1c51e-91e6-3e11-94d9-e187c0287136 | -9.53812 | -65.69665 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2323ac5a-2e98-378b-a7de-8a3f7ef11dde | -9.10956 | -65.74131 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1d97e3e-e591-3a91-a1a1-1b600737688d | -9.54173 | -65.69512 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f014920-cd3a-3234-90dd-0c4bc473b359 | -9.78054 | -64.24637 | 2025-08-29 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0bb1642a-eb6e-36b6-8b4d-2bafa28e21de | -9.80545 | -67.83925 | 2025-08-29 06:22:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c2150ccd-0894-320b-b86c-8ab87ddef7b1 | -9.11213 | -65.77383 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 22952fd0-37a9-3a28-ac43-902bb699b2cc | -8.04305 | -70.09721 | 2025-08-29 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 801dcc53-cb1c-3416-9f20-b13b77795e15 | -9.11743 | -65.76892 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1649f3d2-4efc-3537-a5e3-d20fa47909d8 | -8.77583 | -71.30556 | 2025-08-29 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e7d7ac-d19c-32df-bd4b-6c27786547a6 | -12.42398 | -63.92023 | 2025-08-29 06:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5616916b-ddd5-33c3-8957-6fe90a1e5f85 | -8.89723 | -69.43765 | 2025-08-29 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a23f73b-de5b-3050-ace0-5a3e7cfec70a | -8.95716 | -65.97178 | 2025-08-29 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dd72793-5ede-3cff-b1fa-fee88607fbbf | -9.773 | -64.2469 | 2025-08-29 06:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0095be1b-2dc2-3d41-a013-e12fb0be81fb | -10.3814 | -57.8048 | 2025-08-29 06:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4d7c0eb7-1641-3164-9e9f-c70ac11f90ad | -14.3149 | -51.8969 | 2025-08-29 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| e91f634d-9296-3a51-af85-3b7bee465286 | -10.3624 | -57.8258 | 2025-08-29 06:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 209.5 |
| ca59fa05-817f-3cab-a514-49a9c1d9b5d0 | -3.4254 | -49.0517 | 2025-08-29 06:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 02ccaf84-f665-351d-8907-d247f56c8076 | -9.1155 | -65.7699 | 2025-08-29 06:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 7c4d78e8-d586-3ceb-b406-e837cdf4e394 | -9.4433 | -60.5499 | 2025-08-29 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 328e1730-7c78-378b-9fef-0c2c60a11cad | -10.9709 | -46.9266 | 2025-08-29 06:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 3afb07df-f4d1-37e4-93d1-b2a72c1df250 | -9.462 | -60.549 | 2025-08-29 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| c2d7846b-2578-3dd7-b58e-32ce90a0cfe4 | -10.9705 | -46.949 | 2025-08-29 06:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| cbb68b38-1539-3c35-83f8-2f46f50c4df6 | -9.4618 | -60.5682 | 2025-08-29 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c48450e0-6142-3a60-9679-8272ab99f538 | -14.2949 | -51.9422 | 2025-08-29 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| abae5368-703e-3799-9f0a-72ea69ef965d | -10.3626 | -57.8061 | 2025-08-29 06:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 497e1067-452e-3358-b518-398d4c5cc1aa | -10.3812 | -57.8245 | 2025-08-29 06:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 29402581-f8ee-370d-9e93-c614adcca497 | -10.99 | -46.9242 | 2025-08-29 06:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| c207eda5-ad7a-3aef-8a85-a9724355db2f | -10.9896 | -46.9466 | 2025-08-29 06:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 0263ed71-adb6-3dbd-8174-484e5b01da50 | -9.7728 | -64.2657 | 2025-08-29 06:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b4084ab5-d517-3fcf-83fd-930158147125 | -10.381 | -57.8443 | 2025-08-29 06:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8f2b903e-1f65-3fcc-beeb-8fd16fd3d9c8 | -14.3149 | -51.8969 | 2025-08-29 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 70ad34f3-c0a9-3450-8722-5c0bdbccee6b | -10.9705 | -46.949 | 2025-08-29 06:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| e534c2ee-5dea-3433-a145-dea314fafe6b | -10.9709 | -46.9266 | 2025-08-29 06:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9e07320e-aba5-32c8-9558-0c0bac1a40e2 | -10.3812 | -57.8245 | 2025-08-29 06:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 62387033-c1e0-3899-9b05-73dd41a9f6d8 | -10.3622 | -57.8456 | 2025-08-29 06:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 18d415fc-d2f7-323b-8e26-f84fbf8c72e7 | -9.1155 | -65.7699 | 2025-08-29 06:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9a468149-8dce-3ce1-960a-bdb314b5ee8f | -9.462 | -60.549 | 2025-08-29 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3922eb47-d48b-3963-b198-59072318ab19 | -10.3626 | -57.8061 | 2025-08-29 06:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| dc09a6c4-5232-3b45-9d97-e9f1b6659042 | -8.1758 | -61.3755 | 2025-08-29 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 80c35a91-b43a-3b01-a6d7-e5240a068e89 | -3.4254 | -49.0517 | 2025-08-29 06:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a28e3d8b-46db-3d9a-ac04-e59b34dc7430 | -10.3814 | -57.8048 | 2025-08-29 06:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 33b9c30a-0290-3d39-a403-fb4ab8463dc5 | -9.4432 | -60.5692 | 2025-08-29 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |


[Clique aqui para ver as próximas entradas](README89.md)
