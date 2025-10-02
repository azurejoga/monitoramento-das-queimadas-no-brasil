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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00b21f41-252f-3285-b340-6458b600789e | -12.94213 | -46.43594 | 2025-10-02 04:51:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69bfd313-a2f7-370b-af2e-21e45c1b7964 | -13.7597 | -51.21298 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1f5edc1-d251-399a-965e-af191441bdc1 | -11.81009 | -45.00381 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfad2d16-8c8c-3b5b-9693-91bdef2c9a4d | -13.3204 | -47.21743 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c584d6f2-5dc5-3d00-9198-ce1d101e45a1 | -13.00867 | -45.23073 | 2025-10-02 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd43512e-8fb3-3473-a34b-ea15a9d760ac | -13.95517 | -48.10559 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15a6f0a0-d747-3985-8b01-e8b054001435 | -11.90699 | -47.88736 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1c7b941-1ae1-3f8e-ba29-4c9b0273a9c4 | -11.88012 | -51.22888 | 2025-10-02 04:51:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aae67677-bb7a-3671-8d7c-9a31fed9648c | -12.80208 | -46.86792 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bead0d5-fcb4-333f-9745-59100394259b | -13.75414 | -48.70791 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33e11ef5-2d85-3dc4-b9bc-2765174ef590 | -14.9072 | -48.32306 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b757ee86-3d55-3631-82f7-66602d17ddb0 | -14.33957 | -47.13027 | 2025-10-02 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2db25f9d-11c8-3ce6-b1d2-f04c9bae2f1c | -12.82378 | -47.06015 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c81bb81-1aea-3735-8568-f922050e231c | -12.49644 | -50.2394 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf509cf2-c9c8-391b-9d91-ddcaf036d603 | -13.61907 | -47.28928 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa269f46-113d-3938-8271-52b3c5bca5c8 | -11.81996 | -45.00874 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2722353-032b-3313-8d77-212927bcd184 | -15.69917 | -46.26159 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ccdf444-6b58-3de6-a35a-f7433220687b | -9.83332 | -48.26391 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ad8ca7d-bfd6-38f7-ae55-874d65a78d25 | -10.834 | -46.64342 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4949e85e-9b9e-3e0f-bd2e-85130954935b | -11.82593 | -45.00308 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f6344f3-cde3-3e44-8a06-5015db678fae | -15.25899 | -49.30925 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7005472f-7e72-337c-bd2e-f63cfd5e765f | -10.22491 | -50.28756 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8abe457-5268-3bc8-aab8-d647c866fef0 | -13.05483 | -47.00448 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bba9c7db-9963-3b57-bb5d-7252fb1a7da9 | -13.75247 | -48.01081 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 44b5dbc5-9e20-3b61-81bc-6d65430d93ab | -10.6679 | -48.5953 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b43d2f0a-baa6-3503-9bab-bc8272c20d82 | -11.43749 | -43.88923 | 2025-10-02 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d00d077-490e-3b9a-95f2-7063a0ea54f5 | -15.26355 | -49.30605 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 451abe3e-8e7b-33bc-a7e1-fa38478b6923 | -10.22117 | -50.33794 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb8e3832-350c-3249-b95e-88e481bab8ef | -11.1663 | -47.27496 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 26819f22-b85e-3aed-80a4-cd937e254023 | -13.24576 | -47.32977 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b952872f-81cb-36b9-ae92-f3e56417ec90 | -11.46479 | -45.01583 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f837ae2-a1bc-35a6-9a54-e3a591df6ea8 | -10.18982 | -52.56235 | 2025-10-02 04:51:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d89a0ddd-e599-39bf-9189-1004c73f415c | -13.68067 | -48.07306 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8995c919-e672-3b30-b2b4-8509a80253cd | -11.15454 | -47.19654 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f8638d5-fd2e-381e-a623-f9d77ac883cb | -11.78595 | -47.5667 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff027912-51b5-3dc1-a666-7baeb80bfc26 | -12.76593 | -48.25297 | 2025-10-02 04:51:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8faca7fe-4a0a-3f86-8eaa-8c80b2fe7c00 | -11.28571 | -47.83055 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7d71895-e5d8-3e29-b237-91b8f0ffd6b1 | -13.32401 | -47.23376 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fff3a84-2597-3f61-910d-c9b77752cfa7 | -11.43941 | -43.5005 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a456dbf-4ea7-3357-83e3-31d8317284a3 | -14.42644 | -46.10542 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dcca96f-a898-3650-a325-3e0fc5371227 | -11.01992 | -49.81973 | 2025-10-02 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d709f75-0945-373d-89b7-e3ee9a8e4408 | -12.41432 | -54.35484 | 2025-10-02 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a4b32a3d-744a-38a9-a2ff-20e6217c73fa | -11.43373 | -43.49975 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54187192-984d-32e4-b9ff-39808ad9d7c9 | -11.59421 | -47.65343 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 90a5311f-056b-3b1b-8047-11673fb9d958 | -10.68384 | -48.56853 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 530f6886-38b7-351a-91db-34de4909da93 | -13.69509 | -48.61448 | 2025-10-02 04:51:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0bf7ddd-b9f8-355e-92fd-3ae234c3e5e6 | -14.9053 | -47.22892 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbbd0582-51c1-3b88-9998-631652a18fa0 | -11.08913 | -47.81793 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f261c00-5e38-3a3c-b84b-3d15c4a85625 | -10.69876 | -48.57834 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 096638e6-4c7c-3c3d-95e4-48af4ed8e648 | -11.59493 | -45.05733 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 527cabb5-b182-3117-ac5d-1daafd065c1d | -11.11055 | -51.06147 | 2025-10-02 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f16b6f4a-8ff4-318a-9d00-1f32153dda12 | -12.81428 | -47.02575 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d22a2934-b02a-320e-ad14-ca45597b6b01 | -12.83034 | -43.80858 | 2025-10-02 04:51:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40488481-2460-3210-9c40-5f2f0a8d8de0 | -14.65347 | -48.26762 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f2b5342-182b-39ee-82e0-3aaf4171eec9 | -12.27679 | -45.37711 | 2025-10-02 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76e9ff41-dc89-353f-bee3-070bd636c4e7 | -12.70841 | -48.58889 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf60dbb9-24a6-3d6e-ac68-4df9915a06aa | -13.31979 | -47.22194 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f94a334f-dd12-307e-96cf-5192af57ce54 | -11.4733 | -45.00793 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56fa1f91-8882-3df2-a14f-2736e1ecd6a4 | -11.87199 | -48.01621 | 2025-10-02 04:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bc868e3-9cb8-34ee-a9f4-941392ca76f7 | -14.69749 | -49.62318 | 2025-10-02 04:51:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8355fe2f-206f-3152-a029-bc52c15f6190 | -14.21028 | -46.12666 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f67e16c1-56f7-398b-877c-b3607e416608 | -13.78198 | -48.0545 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c468c18-9d93-326f-a085-bf696d7d119c | -11.27729 | -47.82917 | 2025-10-02 04:51:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f50390c8-b047-3379-a5a5-24661bd8774e | -14.21749 | -46.09774 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b2af132-a9dd-324b-bb95-a199910972ce | -16.13697 | -46.67949 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2755caf1-dd57-3ca8-80d5-bf887ab69fe9 | -15.15911 | -52.79923 | 2025-10-02 04:51:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da8a6ba0-3df3-3bee-a317-7afe4dee89be | -15.5069 | -45.90068 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 210a51c8-2e24-3f41-80f9-96ddbcaded3a | -9.92966 | -43.75128 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 30.0 |
| 8893a970-3d25-3a14-8fb4-ccd06ff22999 | -13.78146 | -48.0584 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ed72a25-703b-3a77-9421-727a4b81d6c0 | -11.59021 | -45.05343 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab4556d-4a7f-36d6-b551-0c94c0779f8c | -16.04803 | -50.85554 | 2025-10-02 04:51:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3471a9ba-3f81-3f8e-b82c-e5ce0d8ae7c4 | -14.18972 | -46.13067 | 2025-10-02 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd15683a-0ba7-317d-93af-674a0ab9a98d | -14.42126 | -46.1382 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8984637-7d8b-317e-88a6-6b8f5ceae674 | -14.02221 | -47.99657 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab550049-2efd-3b47-8e11-4fe44b93d4e0 | -9.82928 | -48.26349 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0332959a-5695-3da1-a357-b344a319c7eb | -11.74849 | -46.82668 | 2025-10-02 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a92b251-00a6-35d5-abd3-24934b856b5e | -15.25407 | -56.77437 | 2025-10-02 04:51:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f59463d5-a4f2-36cf-9543-a42c874affb5 | -12.68617 | -48.57601 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d31e8bca-8472-38cd-9f9f-ee9cd4ebe139 | -14.30747 | -45.99286 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 703e8f43-66ec-3d17-846f-f8b6bb8b4c4f | -11.58728 | -47.64005 | 2025-10-02 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0f76d414-caff-31af-a683-a0f7839ad30b | -9.64331 | -62.84863 | 2025-10-02 04:51:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19bec5bd-8e9d-3273-b8bd-9ac51bf0e8a8 | -15.5088 | -45.90266 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e2240d3-bbc8-3abd-bb7c-b002dc01c00e | -10.19546 | -50.27559 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fbe6a09-a1f2-322c-b69a-71d57d12d83f | -15.25877 | -49.28012 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dac65c39-f7b0-363d-92c6-86e40ece9646 | -13.80065 | -47.53905 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a99d8800-11cc-3174-9246-efe5bdf16bbb | -16.14313 | -46.66975 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e67f3206-f975-3dcb-af0b-0e847747b38f | -12.40826 | -47.50103 | 2025-10-02 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71d0e105-4724-3020-990c-9812161f3fc1 | -11.49059 | -43.50655 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52866359-bdfd-3c6a-b3a3-a64a24a3dc7c | -11.79682 | -44.98388 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6206b788-2a1e-31d7-a9db-3ee7a02d8e4f | -12.70201 | -48.5824 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 98cd7096-6232-37a5-8396-83989f43f829 | -13.32306 | -47.20482 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22b20e15-1522-3559-8273-6946cb5d6b69 | -15.35066 | -46.28668 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7aa2432-549f-3589-84a5-f0b5ea16848f | -14.90285 | -48.32285 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bb5758f-eeea-3a90-8c52-1fff7141a776 | -10.69826 | -48.58183 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 62fc2a36-6cd1-3cdb-a0b7-7b8a0406fbce | -10.26013 | -50.32261 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3683e33c-9dac-3f49-934e-c6028cc1f66d | -13.15939 | -47.81727 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 585d67c7-eec4-3184-bdd9-660b8557dd9c | -12.43326 | -50.16422 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4d34514-aa5d-335e-8460-499f07d970ee | -10.25418 | -50.31322 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34160dd0-1273-33af-a7aa-32a3bdc42015 | -15.39737 | -47.04465 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6276fbb6-e111-3fdd-b745-0e56fcbb0c42 | -14.47185 | -48.39971 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README114.md)
