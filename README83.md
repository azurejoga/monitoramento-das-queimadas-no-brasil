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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3e81d92-6125-3ab7-8649-1d4f07dda5a2 | -10.47717 | -57.95052 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a21702b0-4bf2-30cb-b00d-578ac6345834 | -11.22839 | -55.05044 | 2025-08-28 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9fc214ba-c51c-3924-bf2a-dd8e9236fc27 | -8.0999 | -71.24841 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70479966-477c-3115-a68b-62bb3d5b1c83 | -8.87576 | -60.77142 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a1ddb92-0634-36d9-9c55-4557983cb9b0 | -9.8041 | -64.27714 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 106a4797-06d8-3303-9c21-0a8462c24c1c | -8.93342 | -65.9342 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93690cc5-e2d2-334f-a049-5f007fee7475 | -8.34816 | -70.84016 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e5b424f-895e-356f-9443-74b93d31cef0 | -8.99387 | -65.41783 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c516ae-bc69-39a7-813a-22c1b6660014 | -8.5786 | -70.11696 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3828bcff-4f83-3a52-99a9-fb04e3d20dc8 | -8.9406 | -64.15707 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9213a4ea-b654-3607-bd85-cccf194506ca | -8.95605 | -65.96761 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 732e568f-c1f9-397e-b1fe-cf530908e653 | -9.79396 | -64.24462 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30556abc-aaea-367b-80ee-54acac76c946 | -10.46455 | -57.96051 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b42ad339-e491-315c-8224-ec1d9d9867d5 | -8.95434 | -65.95614 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d377bb47-768f-3761-89d3-cb76b73154ca | -7.62621 | -60.85108 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7282d8aa-a458-3e36-892b-2225632d689e | -8.91759 | -65.92425 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 447a92dc-0de6-3a9b-bdaf-6210e49cf55e | -5.91779 | -61.30395 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb5e0167-d93e-3828-90cb-a87bd2bf5190 | -8.69916 | -69.669 | 2025-08-28 05:48:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6ba2e94-ce43-3a3c-b81f-532478109bba | -8.99594 | -65.7063 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 923aadcf-549e-33fd-bc52-8ed2695a4991 | -7.53964 | -63.85861 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0c32de3-681d-3d26-941a-3870adde86d3 | -8.35182 | -70.84077 | 2025-08-28 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e3ef0e2-04ed-37bd-ba2e-fd41d6ac81a9 | -10.48148 | -57.96161 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 459b8e05-dafd-3e57-8ee3-4453d25b2f48 | -9.08214 | -65.71564 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e4bdd82-bbfb-30df-ac77-f4bdd26b830b | -9.48263 | -62.39447 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91b4971e-83bf-3ee2-b260-1da90430d242 | -9.11981 | -67.70799 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97f0e651-ed36-3a77-8c1b-d52decc9c1a1 | -9.4025 | -60.51144 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9efc5bf-cb62-3dc1-a553-549ca0d52c73 | -10.46623 | -57.96141 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8dc58147-b113-3b37-a978-db0bd62eaaf1 | -9.12313 | -65.79025 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 8d95ccea-c6b5-3d38-bb5d-e9da7f4903d0 | -10.03494 | -59.36321 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2382e619-93da-3f9e-a54e-fe3c2024b01a | -9.085 | -65.71986 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ecbb86d-43a4-3aa9-9e19-5637c5542c17 | -8.68672 | -62.87102 | 2025-08-28 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ed36a30-dc94-3fb9-9cad-70f5f56befd0 | -9.54089 | -62.3955 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6099daf4-86b1-3283-b73b-defac93e1287 | -8.90436 | -67.45928 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1cde9a6-ad70-383c-8603-70abf23498f3 | -7.74557 | -61.08351 | 2025-08-28 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59dfc77a-938e-3e10-af80-fd8fdc76a667 | -9.10598 | -61.42999 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d388e170-71f6-3d66-8a7a-41e08a7c9669 | -8.9031 | -62.47334 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ae9894-ab92-3364-a04b-f8d12fff10e2 | -8.65288 | -67.26628 | 2025-08-28 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5a63b21-31c9-3570-b86f-633b240be815 | -7.40041 | -62.28361 | 2025-08-28 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 75e48fa5-01ee-3737-82e8-a147b8deeb71 | -9.41378 | -60.53274 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edc860b6-3296-373b-93d1-09228462efce | -9.16542 | -59.56672 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf804216-18a9-36f9-bbeb-820e47b83054 | -10.47064 | -57.95724 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 70334e8b-f91c-3eb7-b5ca-1c40d0765b8b | -9.41708 | -60.54312 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 681bc719-c4c4-3513-97b9-1021cbefc8e6 | -9.06789 | -66.05956 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b83de657-a04f-3280-b0c8-4e80c1f84a65 | -10.08005 | -62.89142 | 2025-08-28 05:48:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f14567f-29e4-3902-a652-c7e265ccad12 | -9.14188 | -65.78175 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c210e9e8-7cd3-397e-b0f6-5fbb09d75c92 | -8.94928 | -65.96655 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c2869f3-eea2-3617-97fe-34f43eb7bad5 | -8.88285 | -60.75383 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7b03661-6e2c-3ed3-9e1b-6655c2632dad | -8.94191 | -65.94673 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cd78cca-626a-3efc-98b7-1db4cb235e12 | -10.46576 | -57.96501 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8b5ca4c-a764-3f0c-a43f-cbbc948b6765 | -9.01186 | -65.69357 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbac37ed-7c76-367c-b73d-51913a97a8f9 | -8.69278 | -63.83429 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0a06402b-15ed-310d-9bc1-8c82166aee7a | -7.9346 | -61.57011 | 2025-08-28 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbf5e295-1555-3360-a9a1-25c488d3b803 | -8.96348 | -62.16344 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acc9e840-ae67-35dd-827b-1ca038f57731 | -8.96282 | -65.96866 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d7abce0-6154-38f9-b6ab-9aff929d1a2f | -7.5452 | -63.84636 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50452857-3535-333f-b2f5-58bdc44b2f7d | -8.84908 | -69.11125 | 2025-08-28 05:48:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5367a39b-55b0-3c71-9d7c-10fd4e0c8be8 | -9.00392 | -65.72274 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 353a847d-0624-3d1e-b9f1-fa80cdbee802 | -8.93286 | -65.93784 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2178b40a-9b1c-3cc2-b19b-b7d4a6e798c9 | -8.9453 | -65.94726 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3571ce6-272b-37ec-a225-552f79001c0a | -9.79029 | -64.24408 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19419d8d-d7f8-3a51-8d53-dccdfbe980ad | -9.14018 | -65.77013 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a7ec6c2-3bf7-3653-a950-b2ffa75b6857 | -10.32195 | -62.62126 | 2025-08-28 05:48:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8b8a844-cb8d-3b60-9a9e-1e7d2a764edc | -7.41227 | -60.6249 | 2025-08-28 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34069079-5b88-3c24-ac9b-a6c025681afd | -9.13336 | -65.76907 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b1af5db-6291-30ae-b1a9-6078f8cc0f8d | -9.11859 | -65.77437 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b40e9c16-a5a6-397c-af86-7b78a7416945 | -9.39127 | -60.52465 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b82aeee-0d0b-32e0-a32d-4bd4a625cfb0 | -9.19006 | -60.79952 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49915a5b-a598-35a4-86e1-9012ef4d9d01 | -9.41641 | -60.51344 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 759d1ca3-e68a-3d47-a7af-2d9afe46f62b | -9.15617 | -62.35615 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b85668ff-20e2-3346-a830-8cbdc1171c08 | -8.94757 | -65.95509 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46eecb80-70c9-3864-8506-e3db6d8c06a9 | -9.06395 | -66.06266 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a1d17f2-962f-3b09-9fc0-b701304f0d3d | -9.16463 | -59.57247 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f75eee83-ca83-3f8d-9223-c7153f28155f | -9.12597 | -65.79447 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7c192ba-fd75-3153-9d3e-2a670a81806c | -9.40452 | -60.53142 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f78a2f6a-f305-3fb0-902b-690bd8bba4bd | -9.25366 | -65.90069 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 955e7802-e8ee-3bac-a103-d0ae6feaccb5 | -10.45942 | -57.95599 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5103c108-15c0-34e8-8259-3375f3da3a4b | -9.47602 | -62.38224 | 2025-08-28 05:48:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94916ea0-0d07-352a-a93b-749d0bb9cd0c | -8.91135 | -60.71574 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ebd2fc0-49cc-3f76-9194-f584c40698af | -9.80108 | -64.27226 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e16cb64-5259-3352-b369-e8a04bed321f | -9.18814 | -60.81329 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1df30b7-4833-3ae7-bacd-4ee2719ffd58 | -8.73831 | -70.99906 | 2025-08-28 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 556d8794-bf25-3fe6-85f3-80eb8a09d758 | -9.1345 | -65.78439 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc8f3f93-ec74-3966-88e7-ff92804d6602 | -8.95267 | -65.96708 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3e846265-30a4-308c-a916-697e68da00c5 | -9.41706 | -60.5086 | 2025-08-28 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40a5ba41-f397-3b19-8140-1ecca1d76c8e | -9.14802 | -62.35492 | 2025-08-28 05:48:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 451da8aa-aff1-3b67-be36-4a05bf8a03d1 | -8.99879 | -65.71053 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f162428e-51e0-3394-8dce-c0521df704c7 | -9.1362 | -65.77331 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12c48650-ad42-36e9-85f3-b4660c934011 | -8.69378 | -63.83674 | 2025-08-28 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b11b11c3-7597-3d63-9a1e-350dcd97a78d | -8.9408 | -65.95403 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24cd7821-4de9-3c84-99d5-8d64267b8885 | -7.41934 | -67.72088 | 2025-08-28 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c53cd33-df6f-3a8a-8e62-8f279f9bdc08 | -9.24235 | -59.78561 | 2025-08-28 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33f4a34b-fac8-3dfc-90c6-126dadd01cae | -10.46824 | -57.94599 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b14f7fb-c0b5-35b5-b4bc-fb6229d363b4 | -9.04826 | -65.72958 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afe2fcc7-29df-35a1-a6cc-daef8523ceea | -9.01698 | -65.70579 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b8a0a23-cbbf-3115-b18e-fc56716e563c | -7.27764 | -60.29847 | 2025-08-28 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9cab91c-b736-3522-9010-63759a7f6d64 | -10.45893 | -57.95993 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb52fc19-3e89-37f8-ad97-e5e20964ec8d | -7.37669 | -64.36829 | 2025-08-28 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d28bfd60-af8b-3236-baf7-f2081237c79e | -9.11007 | -65.78445 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2175051-4f84-3414-927d-623e708266d9 | -8.95549 | -65.97126 | 2025-08-28 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b99249de-7758-3bfe-8bea-e0d10ecc1b56 | -10.46774 | -57.94987 | 2025-08-28 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README84.md)
