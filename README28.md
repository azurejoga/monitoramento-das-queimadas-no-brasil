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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccf83f41-a304-3a26-8603-4e60e2a37484 | -8.93577 | -60.74642 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a5f8dd0-f669-3d38-b81d-6407cbfe43e8 | -9.71385 | -61.29404 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e9148cd-d92a-3fda-b4e6-0153fbab6a60 | -8.92609 | -60.73378 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 120ac265-67a3-3dbc-aea4-7c4becf67f35 | -9.7134 | -61.29755 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d84af9c3-fc35-3188-a5e6-7a15d42820a1 | -9.37719 | -61.53464 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c7330496-6791-37ff-8759-4396dd408e19 | -9.37064 | -61.5299 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 97aa79ad-c52f-3979-8d57-958ed010766a | -8.95105 | -64.34371 | 2025-08-10 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2980b88b-2886-3a54-8f2c-c39174af64af | -10.91761 | -68.43465 | 2025-08-10 06:03:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2485acc-72ff-33a6-9063-e355adcb226a | -8.93286 | -60.75199 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ec39a00-2a67-352d-b95b-9c4c14c23b0c | -9.55515 | -62.72264 | 2025-08-10 06:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acd00c09-1e88-3454-8a6b-e25c86919d3f | -8.93986 | -60.74163 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0672cc1-9cd3-3462-8277-55b3b1844d1d | -8.9256 | -60.73747 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 399f6801-3245-31fd-bf9c-b3be61165363 | -9.70663 | -61.30738 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e2fdce8-295a-3483-9a6a-86d431c2d320 | -9.36699 | -61.52982 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57b38a6c-5873-3e6b-b58e-c2c82be10488 | -8.93218 | -60.73084 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f208b830-387b-3c67-bcfd-4e68f228a65d | -9.37554 | -61.53399 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2d88152b-c934-3638-9e3e-84b8cac72199 | -9.3781 | -61.52798 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 24870721-2076-3cd5-b483-9fec7c85134a | -10.87729 | -69.21317 | 2025-08-10 06:03:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6ef49cc5-0970-3ed5-b4ff-760f84996b06 | -9.36978 | -61.53659 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 06832825-618c-3a72-83f7-58155200fecc | -10.04449 | -64.90054 | 2025-08-10 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 974cd4f5-483f-30f4-bf91-b0cd6267b8f3 | -9.71252 | -61.30455 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81ddf7bf-02f2-3920-99bb-52af5b9e555a | -9.37231 | -61.53056 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f16ef1d1-8de3-322c-a4c7-f73e69a4e648 | -9.37186 | -61.5339 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6aa852a9-38c6-3391-adbf-a67871c2029e | -9.71192 | -61.30352 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3d7cd71-f47b-3be9-9a3d-d3346ba7e173 | -8.9287 | -60.75667 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9c9bae3-4f2e-3034-bb63-82906873bf36 | -8.93332 | -60.7483 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c577396-f05f-3e02-82d7-284e1bf54cb7 | -9.70601 | -61.30636 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38e5da3a-951a-34fd-b288-ac1d959f8b66 | -9.37597 | -61.53066 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e372d7ba-a81d-3545-97a6-1e8dae295204 | -9.36653 | -61.53316 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d73a1af-649f-31df-afb1-c1ecb2a965e9 | -8.93118 | -60.73825 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb22e85-1750-3bda-8f68-b2f7f39c474d | -9.55589 | -62.71712 | 2025-08-10 06:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e688c649-ec6c-3e31-925d-37bdd3a313b9 | -8.93677 | -60.73898 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c90382ba-f5b1-306d-8c63-6c7c3a96f70a | -9.56082 | -62.71777 | 2025-08-10 06:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b57a6843-8058-3511-b298-02d8f2857ab6 | -9.37511 | -61.53733 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1770d7dc-5f4a-3a74-a833-9851e75c0135 | -8.93168 | -60.73455 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7421d899-d0f6-37ce-b201-57035bcd5ec5 | -9.36789 | -61.52316 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4206adf3-6044-3377-b40b-5791c11edbbe | -9.3715 | -61.52326 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 779da8e5-b364-3012-ab5f-e71f4e47bed4 | -8.92962 | -60.73274 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d60eb85-e1f8-33ac-9c8f-1c08deeb41db | -9.56009 | -62.72329 | 2025-08-10 06:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9840400d-1575-324c-bdac-aeb1c044320d | -9.82238 | -63.01274 | 2025-08-10 06:03:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38fa3747-25f4-32da-92e3-7f7052106f1c | -8.93009 | -60.72903 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abb88469-350b-3f61-a41f-1b21bb30a963 | -8.93239 | -60.75566 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| deb42189-d51e-3a77-9945-b1faddbfdeed | -9.70751 | -61.30037 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05ffc870-e61e-3cde-b039-27c2ffc645fb | -8.93527 | -60.75009 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d32c2edb-1e56-3ab1-968f-98fa4439fed3 | -10.08861 | -68.96593 | 2025-08-10 06:03:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cee7e0a3-5c6d-316e-8d8e-5f405e707ecb | -9.37107 | -61.52658 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2043ef04-33c1-3785-b47a-6be695097ec3 | -9.3714 | -61.53725 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 7b6e580e-01bc-3f24-b019-e2c7fa0e9671 | -9.3764 | -61.52733 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 908b3d7a-1cff-334e-bfa7-fd2e0c926d40 | -8.93891 | -60.74907 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afa03089-5a55-3759-9609-a26be0107090 | -9.70788 | -61.29232 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e454b19d-6721-394a-b44f-fa0f0741a249 | -9.37855 | -61.52465 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ea5e9a5d-860d-353e-bed3-b455f3b904cb | -9.70707 | -61.30388 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9887213-c90a-384a-9f36-8f9115854af3 | -9.37322 | -61.52392 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 172d9daa-5cf5-3709-8e05-f7bca5dddc39 | -9.71333 | -61.29303 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ff88af6-26e0-37f3-9b14-9e124346d88d | -8.92915 | -60.73645 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8294248b-8790-302f-aa52-51655938fbf8 | -9.67536 | -62.88583 | 2025-08-10 06:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06dd2ac3-8610-3697-88cb-a1e434008d82 | -9.37021 | -61.53324 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4b213f82-9e9f-3c49-8a89-7e9d09144906 | -8.93474 | -60.73719 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 881202ef-5edf-3fc9-a892-3c1be85eb4ab | -9.82325 | -63.01733 | 2025-08-10 06:03:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6793b4fe-b766-30a2-9a3f-bd0e2b21434f | -8.92659 | -60.73009 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 807b466f-ec26-3bf0-ba76-368bd36424c5 | -8.93427 | -60.7409 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b98bce44-a764-303d-a2d4-22d2c19fae2c | -8.9338 | -60.7446 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da492a14-5aff-3072-9e58-2f815128be81 | -9.67463 | -62.89119 | 2025-08-10 06:03:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8295610-d257-3dd5-92a5-8e458f682756 | -9.37277 | -61.52724 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0b494d69-cc30-3b69-8795-52768c447146 | -9.82398 | -63.01207 | 2025-08-10 06:03:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82ea3a9f-ce0d-30a5-9ccd-13328e3e9b9b | -8.93938 | -60.74536 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c04ba32d-94eb-3103-aeea-5bedb6414bd9 | -3.42429 | -49.04398 | 2025-08-10 06:05:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 9677dc75-935a-372d-9ed0-593fc357da1c | -6.18997 | -45.43673 | 2025-08-10 06:05:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d9b6d1bd-1d3c-3c7b-9cc3-118ca443da34 | -4.29725 | -48.07724 | 2025-08-10 06:05:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 68ca9318-d262-3ae3-8924-2ab7db635956 | -6.52847 | -42.76285 | 2025-08-10 06:05:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 26d21d7f-f420-3c5d-8ea8-0cfa29739295 | -4.29862 | -48.06782 | 2025-08-10 06:05:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 800016b5-8369-303f-909e-62e46626b44b | -7.1557 | -44.05428 | 2025-08-10 06:05:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e8c460b9-4125-309c-a7f0-0eae836bed3c | -3.4256 | -49.03519 | 2025-08-10 06:05:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b7b86bee-147d-3188-aaee-32285288bb49 | -6.9437 | -44.55249 | 2025-08-10 06:05:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 13e2725b-932c-3738-9d54-8f8988365464 | -2.5843 | -51.91459 | 2025-08-10 06:05:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4c98b04-c2c3-3738-a869-8840770f51e0 | -6.53731 | -42.75688 | 2025-08-10 06:05:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 44ca44d2-8b9a-36f3-ba81-3409dafd275a | -8.92541 | -60.72161 | 2025-08-10 06:08:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 29b7abdb-a050-3c40-a55d-4472458f08ea | -8.9332 | -60.75504 | 2025-08-10 06:08:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b04d0a3a-726d-396a-b0d3-be14bb3bca59 | -8.9398 | -60.71681 | 2025-08-10 06:08:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1d07a5fa-9542-3b84-8ffe-4cd8f36cfeaf | -9.06037 | -49.53106 | 2025-08-10 06:08:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f18939cb-df7b-3f6c-80c8-b46dcce4d84c | -8.9185 | -60.75982 | 2025-08-10 06:08:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 3766473b-2fed-3cd7-b79e-9d4d1ad718d5 | -9.48621 | -46.27694 | 2025-08-10 06:08:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9b2080d5-763a-3589-9338-b35036807ccd | -11.09484 | -50.4536 | 2025-08-10 06:08:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cb23c3f0-a013-3a82-ba1a-ab37565fbd34 | -9.49717 | -46.27836 | 2025-08-10 06:08:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a730d259-4371-300f-9dff-d66f92ffb7d9 | -7.63156 | -46.23382 | 2025-08-10 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c689d80a-b4a6-3c9b-aef8-93317ee2f433 | -7.87407 | -45.55317 | 2025-08-10 06:08:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2cc031ff-14a8-35e6-a96e-6abd376eb5b0 | -9.362 | -61.5324 | 2025-08-10 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| bb02d5c2-5ccf-3e9c-9cff-092ff8a37800 | -9.3808 | -61.5124 | 2025-08-10 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| f9d5d87d-d625-39ca-a51d-f1eeee444ee9 | -8.9399 | -60.7481 | 2025-08-10 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 40be2b15-a4c6-32a4-bda4-43fc45004214 | -9.3806 | -61.5315 | 2025-08-10 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 0e45019e-5085-3224-b46b-77c77274009f | -14.29474 | -51.97061 | 2025-08-10 06:10:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 19a37166-ed0e-36fe-bb8a-4b7826004c44 | -14.29338 | -51.97963 | 2025-08-10 06:10:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a39b11ea-2033-3615-a2d9-517ed423886b | -16.303 | -52.92502 | 2025-08-10 06:10:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92d9a07b-ba40-392d-a62e-f7d0ceaa73a6 | -18.16794 | -46.99076 | 2025-08-10 06:10:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 6f675994-09b4-3782-8761-2bd708c09d70 | -16.29417 | -52.92359 | 2025-08-10 06:10:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73fd792d-1443-38d4-91d2-2fec703c3b0e | -14.28731 | -51.96023 | 2025-08-10 06:10:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 17618b37-5e7f-37b3-b9cf-28c0feeba440 | -9.3806 | -61.5315 | 2025-08-10 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 9691d2e0-7695-3195-b34a-55a7632eb0a2 | -8.9213 | -60.7489 | 2025-08-10 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| c17644f8-8557-3378-947c-613c1849a902 | -9.362 | -61.5324 | 2025-08-10 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 5e74f019-6586-35f2-9c96-800547e36297 | -8.9399 | -60.7481 | 2025-08-10 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |


[Clique aqui para ver as próximas entradas](README29.md)
