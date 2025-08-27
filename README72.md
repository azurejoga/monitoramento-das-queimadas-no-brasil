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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dae71fa-bf64-3017-9a1c-a63b3455827e | -9.18401 | -59.49594 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 209e7dac-8307-3438-af65-bcac02373f23 | -6.77237 | -59.66304 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36e1dc3d-1568-30ef-8e0b-597cb567ddc4 | -8.13143 | -55.37186 | 2025-08-27 05:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a23144fd-4c7c-3cac-b49b-5275f56b824b | -6.68988 | -58.54136 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65e7554-0b52-36f1-81e4-00efdf09ae4d | -6.25844 | -60.01646 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f14c5a6-12b1-32a6-b716-01e2a3cb3fe9 | -7.47797 | -61.35107 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da746fc4-6e20-308b-9b8d-69353c49180f | -8.95498 | -63.36759 | 2025-08-27 05:44:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45a99c7e-ca0c-3e7c-b8d5-f9932b8a5151 | -6.94208 | -59.55952 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cd58cb2-7202-36f7-aa1b-dfda4bedf6f7 | -6.23751 | -60.01704 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6350303d-2a6c-3803-85d3-3fe89e8c297b | -5.61022 | -60.23003 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e61b354-052d-3939-858a-a770a318a701 | -5.23001 | -59.99899 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 205c7b71-db30-39b6-a49e-445ea052e44f | -9.39842 | -60.52673 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69caf0e2-0e72-3160-a7a2-4ba4f3837343 | -8.6505 | -67.27185 | 2025-08-27 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d094b976-eb8f-3ec7-89af-a78422807a8b | -5.76055 | -53.76223 | 2025-08-27 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee6a4203-d57e-373e-8206-af8b0a4646db | -9.41045 | -60.50188 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2798ba56-81fd-328b-be5d-2d9e2317ba51 | -7.62199 | -61.03199 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e3e9168b-1603-3331-9372-0b155f4b6805 | -9.41818 | -60.50683 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 957b6524-3b9a-3be6-8490-9bf40310e2b4 | -9.64849 | -59.6261 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33851818-01a8-362b-ac9c-7378c9b12bc5 | -4.70377 | -56.06754 | 2025-08-27 05:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f19f17ce-9c29-34c6-ae48-7b5856de74b8 | -8.90052 | -60.76646 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 832f9919-5bb6-3a0b-8100-24222415f67d | -8.21648 | -61.39223 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d69172c2-3516-3465-8763-1b13f19f49f9 | -9.41994 | -60.51012 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a4e8a0b-1bb6-3c52-95ae-15f08af8c7bd | -5.4252 | -60.16242 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f268f169-0b75-3e0e-ba3e-4a75070b36fe | -3.38265 | -59.68703 | 2025-08-27 05:44:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39fbcde3-2aa5-3f2e-a860-d74c2eaa03e3 | -7.4264 | -60.01248 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbffb7be-014a-3e57-b747-b33f4a7e449d | -4.96808 | -55.82548 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aeefa8d-8426-3d52-90e3-b0c817f06691 | -8.89209 | -62.47424 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 629381ad-b888-3c62-b3b5-0cadc4e3d196 | -9.41026 | -60.53222 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 380a2c4a-4040-33ce-ab86-b5c748a72968 | -9.23 | -60.91962 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62845737-308e-3ada-a966-60f87927dd36 | -8.89194 | -60.76879 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77497121-ebee-3a04-8936-e89b2da9625e | -8.57422 | -63.92466 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c15da3df-16b6-3635-aba5-3abfd94df2b9 | -7.05479 | -59.81736 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd370b0a-2401-3c87-92eb-bf9d14a33c06 | -7.47867 | -61.34642 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d88bc05c-2020-3885-b840-42be4b5c1f6f | -6.82694 | -58.9698 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 423ac4d7-90ee-37d6-a574-017d7cc3487b | -9.23538 | -60.82595 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f7059f3-b0fc-329f-81ba-da307f85c4dd | -9.34341 | -59.63364 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe4f06e1-4dd9-35da-9cc7-e300acec7c2b | -8.34733 | -62.93351 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76aa267a-446d-3ffb-8dbc-ef8cf1c96ad4 | -9.40524 | -60.50871 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 47c3b6f2-4709-3ffb-b1b7-499cebabac92 | -9.18682 | -59.4434 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e6e23b4-3beb-320a-a6d4-c7c1e5227cf1 | -9.27345 | -56.91313 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a046492-9bc9-3baf-bbf0-86f5ca973e96 | -9.18159 | -59.51328 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15a1762b-e24a-3c95-9896-9da6c3b40f66 | -9.58944 | -55.38505 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4932f9b6-fca8-39a1-8fd9-96f41a2ea9af | -9.15772 | -59.58807 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64e14e4c-f1a1-3730-929d-69093a7523b4 | -8.88433 | -62.45127 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| faa3562a-9ba3-3532-83f7-3129f4efc01f | -7.42765 | -60.61983 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94f85315-c908-3362-8e5e-8bce844c83da | -6.76704 | -59.67025 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3695a5a6-927a-37ed-ad44-eae2a05ad2b0 | -7.54175 | -63.85543 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88670bb0-b96c-3998-a06a-364884fcb60e | -7.16843 | -59.7466 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 342a0ee9-5d5e-3870-ba91-272695a8f6fc | -7.43665 | -60.02913 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaa0fdf3-07be-341e-84a0-bc488d7cefdc | -8.52928 | -64.01222 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c73446fa-7dd0-3058-bbe4-e83099c9e32e | -9.17055 | -59.46313 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f34716b4-c69c-3785-8f5d-e1d25203e37a | -8.11143 | -61.48091 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb024d4e-7b6a-33ad-9f3d-5cf06bd324cd | -9.41685 | -60.53244 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b8df536-e1db-3f7c-b436-89011a571120 | -9.40775 | -60.5205 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 889d1d84-8d2a-37b3-bcbe-760f9ba75976 | -8.95013 | -64.13241 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 689d8d2c-ddd8-3333-ad38-be75dca30815 | -9.18943 | -59.45708 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 02b1044a-c4aa-3bfc-80d8-11ac4e55a4e8 | -6.69767 | -58.5519 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 713d22b0-febd-3133-8d7f-44aeba78ec8b | -6.81432 | -58.96357 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42450b15-2ddc-35fc-abd2-fcd5614dcff8 | -6.84081 | -58.96752 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 642d7646-1833-33e6-82c5-436dd23fdc38 | -9.165 | -60.76776 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 199fd44a-c8b2-3526-9ad9-0579194edeae | -7.48296 | -61.3586 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a7a610e-82ed-3451-b4ee-6a8c2ec70f98 | -7.40906 | -64.35192 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 418d2168-635b-3e84-b3de-ad5715aafd2f | -7.35569 | -57.62329 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae3e78d5-1dbb-334d-99bc-3591044f32cf | -7.09928 | -62.97195 | 2025-08-27 05:44:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09f4dde6-db2f-3307-8299-21c9845d1070 | -7.34813 | -57.62733 | 2025-08-27 05:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ffcaaf5-22a4-3fdb-8e66-ff1e53643e5d | -7.38054 | -64.35839 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 129973b0-940d-364a-aad2-f25c47b9b502 | -6.56253 | -60.0608 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f37c28c-734c-32f3-a26e-94039e0aeee2 | -7.54739 | -63.84132 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52b87a5e-0018-3425-a4a6-a9e618e6e0fd | -7.62125 | -61.0369 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5a47f65f-94d3-3b96-8dde-fc092d148078 | -9.19293 | -60.80547 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b86a260a-83c4-344c-92ae-b62e265afecb | -7.36403 | -70.14822 | 2025-08-27 05:44:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a18acdf2-4ce3-3a5a-abcc-d0ab8dc34ffb | -8.34258 | -62.94096 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba7d58aa-2f2c-394b-a552-e2840dd97d89 | -9.17635 | -60.86441 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8941b097-7330-3a3a-b0d8-e63ecc057b52 | -8.90765 | -60.71687 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fc5346a-ebe4-3a1d-83d5-5d327acc34ca | -9.4108 | -60.52851 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 548f4860-ea6a-385d-b47c-33a1c95f0490 | -9.40722 | -62.48754 | 2025-08-27 05:44:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98e2ffe9-e731-3496-beeb-aaacaa48fd62 | -4.55932 | -55.96232 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5df68dd8-dad6-3548-a7e0-fcf110718a8c | -4.95958 | -55.82169 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f980ab7f-8aeb-3f27-8c8c-4c3d4c57cb2e | -9.41459 | -60.50248 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5953f2f-0cc8-3788-9cb7-037477adc454 | -6.70467 | -58.56008 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f72276a-5257-35da-a2da-4cc770dc1834 | -8.61052 | -62.64148 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 633db450-96c8-34b6-aab9-3c8de86ec677 | -6.83261 | -58.96191 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2394280-098f-3559-b334-d3ad72e03322 | -8.25739 | -61.46151 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27afe76e-0cf2-33e1-989d-2b6cb5b10372 | -8.55729 | -62.6224 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f9ea12e-f864-3f45-874f-03043d9fc6ca | -9.23802 | -60.92081 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c073d074-a195-33b9-997e-613904f0938e | -7.17379 | -59.73948 | 2025-08-27 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab1ad8c6-64df-388a-84da-35b630583cbf | -9.42045 | -60.53679 | 2025-08-27 05:44:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d4d0812-74fc-3dc8-8f9f-1fc858ea1172 | -9.1796 | -59.49529 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c98e294-2b39-3ee0-9e99-b067a20de84d | -5.45148 | -60.15056 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c08f4ff7-dd40-3d9e-a55c-0cb0cb916607 | -4.95925 | -55.81097 | 2025-08-27 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59c8269e-d4a4-377a-a003-5b89ed9fc6f3 | -8.11942 | -62.86792 | 2025-08-27 05:44:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56519cb4-dd81-33f7-abdc-3c2c339a27da | -7.54119 | -63.85909 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0c69243-be0d-370f-a28b-af89130ef2e0 | -8.57023 | -63.92783 | 2025-08-27 05:44:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e6f5c4-5df4-3aa6-a846-216381a6a3c8 | -6.24159 | -60.0176 | 2025-08-27 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7d227ed-0d37-3f90-8e27-ca70e5f19586 | -9.59191 | -55.37965 | 2025-08-27 05:44:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fbdb872-7ec2-320b-bd5c-0f44f9ecef67 | -9.18561 | -59.45209 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b9b6829-70c1-325d-ae48-b652e7ef0108 | -9.15982 | -59.54065 | 2025-08-27 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb938ac6-c826-3232-8145-8a0079386146 | -8.07324 | -61.53911 | 2025-08-27 05:44:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 557ae7e8-e259-3929-a5d0-b1e6d276ec06 | -9.26382 | -56.90493 | 2025-08-27 05:44:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dee05bec-694d-3ef0-99ab-cc5bc370553c | -6.79836 | -58.62876 | 2025-08-27 05:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README73.md)
