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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7157d03a-4dfe-34b6-bb18-5f6efd6ecd09 | -9.03459 | -65.40503 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e80bad4-fa63-3af5-8929-4084f25114e7 | -9.0157 | -65.45341 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b71fd91-1b8c-3aac-bf9c-90db03085128 | -9.00811 | -65.41171 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecc7d24a-c78c-3a94-a15c-a794d93b9a8d | -7.68459 | -67.12546 | 2026-09-02 06:37:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9adb2f5b-47ba-34fb-a989-cf6f5bd71f89 | -8.45707 | -72.53318 | 2026-09-02 06:37:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5fc52ba-c763-3cc3-ace6-21220c26f549 | -9.00526 | -65.41508 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a87da60d-509b-374d-8d14-88c82fb18f6f | -9.02261 | -65.4493 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4e8c3e7-c372-38a6-a87e-9fef24881103 | -9.02136 | -65.45924 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdaa9b77-b8d3-3ab9-87b4-391a392f5dca | -8.0027 | -70.62074 | 2026-09-02 06:37:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dbec3da-c314-3b30-9dea-91374053efbc | -9.0289 | -65.45014 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 666e8f6c-f52c-3bb0-9fe8-690aca56d8a0 | -9.09213 | -65.38007 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79822631-f9aa-39b0-ba18-04801d4e47d3 | -8.77433 | -69.33936 | 2026-09-02 06:37:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a460d945-06c0-34bb-aa8e-40ca5a85a918 | -8.56532 | -63.18628 | 2026-09-02 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b30a055-ca16-32e6-a87c-52b2da78424c | -7.69568 | -67.12703 | 2026-09-02 06:37:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dbae837-4c48-3b52-a156-513f15d07526 | -8.00708 | -70.62141 | 2026-09-02 06:37:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b413c089-dc58-3882-9980-8486c83f4d3f | -8.65034 | -70.68632 | 2026-09-02 06:37:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a65ccb7-6011-34ac-bdcf-576ecb5afa7b | -8.55726 | -63.19239 | 2026-09-02 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d1c5d86-93e6-3b14-9414-0d267081a247 | -8.56868 | -63.18576 | 2026-09-02 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19883742-d558-3eb0-a26b-6667e7849cdd | -9.0144 | -65.41261 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bed49b8b-f9cd-3a71-969c-a84a85eca3b8 | -7.69065 | -67.12254 | 2026-09-02 06:37:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52592611-11df-3b81-bc75-27bf3fcbb1c5 | -7.59165 | -72.74877 | 2026-09-02 06:37:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b751ebb6-51db-3660-9145-7a3eba690c04 | -8.65975 | -70.6834 | 2026-09-02 06:37:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3ec6572-84b7-3080-a048-981e29450f37 | -9.00262 | -65.43513 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a74d870-5586-3292-857e-ea913c01666e | -9.08966 | -65.37624 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9d89b0b-1400-3138-9ee0-873e54b95e1f | -8.56067 | -63.19184 | 2026-09-02 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0a35fb98-9b20-37c3-acdb-8ad0241d2d9e | -10.9755 | -50.465 | 2026-09-02 06:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ae120de5-a526-3a67-91b6-ae652a411a06 | -10.9752 | -50.4864 | 2026-09-02 06:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ee97ac49-2b88-33c9-8704-adaff100d9ed | -10.9204 | -45.3253 | 2026-09-02 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5accbb36-c66a-324b-b026-bf13f6144459 | -8.4671 | -54.7035 | 2026-09-02 06:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8c3dbe20-1c59-384b-b791-3e438ff111cc | -9.87684 | -64.98864 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4909b9d-bbf9-3338-ab05-b93484953818 | -9.87822 | -64.97762 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a012ebb5-b5ef-3a04-83b5-d7ce7c697369 | -10.4828 | -64.32806 | 2026-09-02 06:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47ecd9cd-84a2-3e7f-8d93-b1a154c32c34 | -9.88323 | -64.97755 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9bb0065-88a4-3822-aac4-6aea596e3283 | -9.44157 | -67.45239 | 2026-09-02 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e318bdca-f56a-3d9c-bfe2-8ebb996087ca | -9.44495 | -67.42676 | 2026-09-02 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43c7f1ec-117a-3d42-bbf0-8a84f6a84a1d | -9.87538 | -64.98775 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aea1c027-5ad6-3dff-8adf-49496ea4ad93 | -9.43986 | -67.42236 | 2026-09-02 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f949084-762a-3946-b7b4-8e541eb22294 | -8.861 | -71.34946 | 2026-09-02 06:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44df1fab-ab8d-31f0-ba4e-0f2c1fbf20ed | -10.48382 | -64.32755 | 2026-09-02 06:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0eed51c-2792-336b-8784-72ff8d3827c4 | -10.8977 | -68.55627 | 2026-09-02 06:40:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c7123b1-8eed-36f7-8944-f8d9606d16c9 | -10.16714 | -69.31603 | 2026-09-02 06:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9555c444-f861-308f-816c-027eb026b7e3 | -9.87099 | -64.98228 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdbae53b-c9ac-34b9-9489-78118af7ccae | -9.44205 | -67.44875 | 2026-09-02 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c389c573-09e7-356f-90a8-beaba82356e4 | -8.8123 | -71.24316 | 2026-09-02 06:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a64c7a71-2aaa-3cbb-8be4-8e84ba7852d3 | -10.49073 | -64.32787 | 2026-09-02 06:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c7ee34b-1d5b-39a8-bdae-2d4692f837fa | -9.44544 | -67.42311 | 2026-09-02 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc08d0b3-08de-304e-a2c0-7f14888870a0 | -9.6185 | -68.60234 | 2026-09-02 06:40:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cbac291-ad51-3326-8f7a-ec5cf767d17d | -9.62365 | -68.60313 | 2026-09-02 06:40:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e33115f-08b9-339c-81d6-3b5cfe90e99d | -9.87237 | -64.97117 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 275749bb-ed90-38d8-b8e1-e6bcd41109a7 | -8.89344 | -71.39411 | 2026-09-02 06:40:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a15dbe7-a7c8-3037-b190-cd4229fd6bc3 | -9.87603 | -64.98223 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef967e42-a8d1-38f8-ade5-4274a337d0e4 | -9.87168 | -64.97675 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e5a41f3c-aa1c-3702-864d-b22e57e04268 | -8.86045 | -71.35339 | 2026-09-02 06:40:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f96e371-a64f-39c9-bbba-5027ddcc786c | -9.86514 | -64.97585 | 2026-09-02 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8e681db-eb80-3a93-bd76-dc0611b6bb36 | -9.042 | -71.94237 | 2026-09-02 06:40:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da5613c4-8f17-31ed-8acb-71a82a0ce0d0 | -10.48972 | -64.32832 | 2026-09-02 06:40:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 137620be-746c-3671-a454-72ada44deea8 | -10.89727 | -68.55953 | 2026-09-02 06:40:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc249485-4e47-3a10-9ff6-c0f3023be6be | -10.3953 | -50.0132 | 2026-09-02 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f0ea97e4-feaa-3937-8659-1be8a48f47c9 | -10.9009 | -45.3509 | 2026-09-02 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d1501c65-e3ef-3179-892b-2689b2d1e34b | -10.9755 | -50.465 | 2026-09-02 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| d04ed982-b759-3c0a-87ed-c60eec5738aa | -10.9013 | -45.3279 | 2026-09-02 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| b4ce77ab-c75b-38a5-9b2e-e48e066670b4 | -10.9395 | -45.3227 | 2026-09-02 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| fafeaef2-ecdb-31a4-afb5-0bf7a78e2624 | -10.3956 | -49.9918 | 2026-09-02 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 71a28445-ec77-3475-87fe-59a709c612ef | -11.3048 | -45.1575 | 2026-09-02 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| efd11497-e1ae-326c-98e0-06e1609d32a6 | -11.334 | -50.5752 | 2026-09-02 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6cacbc45-67bd-3ef4-808d-19f9ef66d92f | -10.4142 | -50.0112 | 2026-09-02 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| b5e346f1-6f62-3f8f-b113-544d89b71ad0 | -10.9208 | -45.3024 | 2026-09-02 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| de23ee19-8dbd-36fd-ad1f-8e1908076a34 | -10.9204 | -45.3253 | 2026-09-02 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.9 |
| d6474f93-99d9-315e-8770-0961bde10856 | -10.92 | -45.3483 | 2026-09-02 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c24323ae-aeff-32bc-8046-a75bba42c54d | -10.4145 | -49.9898 | 2026-09-02 06:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 72d4d301-cda6-323c-83de-d5e0c596db45 | -8.4858 | -54.7023 | 2026-09-02 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| de3ecfbe-22aa-3e3d-b239-d9d266fa4c6a | -11.334 | -50.5752 | 2026-09-02 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 6039af94-1491-3dc6-a6ca-324a2460ec63 | -8.4858 | -54.7023 | 2026-09-02 07:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| eb61ec94-b41e-31ec-9814-efe1b3a35ce3 | -10.92 | -45.3483 | 2026-09-02 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 838cb649-c947-31ea-8a11-a9192338f39f | -10.9208 | -45.3024 | 2026-09-02 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 4f7409b6-0bcd-3d55-8ac8-c9ce8cc9ed25 | -10.9755 | -50.465 | 2026-09-02 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 37c6e51f-f83c-34d9-b635-fbddb4678d52 | -10.9013 | -45.3279 | 2026-09-02 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 7b4fe8c6-ad47-3f29-b70b-ee0b9bb6910f | -10.9204 | -45.3253 | 2026-09-02 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 339.7 |
| 567eb3f6-2052-346e-8971-d4a29d017e46 | -10.9395 | -45.3227 | 2026-09-02 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 888a2d05-e6fd-306e-923b-b39097b17cb8 | -10.9009 | -45.3509 | 2026-09-02 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| ba9b924b-413f-3ab2-9a61-f80e42a647b5 | -10.9013 | -45.3279 | 2026-09-02 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d6ee6eca-5240-3ca9-8ba8-f7a223c44bde | -10.9009 | -45.3509 | 2026-09-02 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 6094f977-3648-3733-9e09-c86a1cdac8e4 | -11.334 | -50.5752 | 2026-09-02 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 67aa3e9e-57db-3e46-80ca-cd32f57e92d7 | -8.4671 | -54.7035 | 2026-09-02 07:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 8ba0f1e1-6c71-3ec8-8d15-f86beb2ff323 | -10.9204 | -45.3253 | 2026-09-02 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 391.7 |
| e4d91e29-3a38-3a84-b303-4ce72a2a144d | -10.9208 | -45.3024 | 2026-09-02 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9e8c9b5c-ad91-31e7-b05c-409313602ad7 | -10.92 | -45.3483 | 2026-09-02 07:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 17f06744-2753-3af8-a2bd-60858e5f2a34 | -8.4485 | -54.7048 | 2026-09-02 07:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7f7a09d1-959f-347a-8a1a-8ecc239dcd8b | -10.4 | -49.97 | 2026-09-02 07:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4651a268-a530-30cf-8cfe-df027933c0bb | -8.4485 | -54.7048 | 2026-09-02 07:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 852a5a19-3314-3404-829a-a2b6ae725fd1 | -8.4671 | -54.7035 | 2026-09-02 07:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 4d3efe3d-8b61-3b3f-b09d-4a278a100a5e | -15.3659 | -47.6838 | 2026-09-02 07:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 136.7 |
| f72956fa-3335-37f8-a1d2-84063d1113ab | -10.92 | -45.3483 | 2026-09-02 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| bb5e4fd6-93c0-32ae-b33b-d5681b40e53b | -10.9204 | -45.3253 | 2026-09-02 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 3999e480-2b0d-317b-a4a1-5e60e7615b86 | -10.9013 | -45.3279 | 2026-09-02 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7ac972c3-a379-3bf0-a2af-4d55bd70a0fb | -8.4671 | -54.7035 | 2026-09-02 07:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 50b2a531-0b5b-3df4-af51-1a564c127a5a | -10.92 | -45.3483 | 2026-09-02 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 342a0170-1cdb-31be-9a95-7c4110697d43 | -10.9204 | -45.3253 | 2026-09-02 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| a9455d55-6151-333f-827f-e2c8101723d9 | -10.9013 | -45.3279 | 2026-09-02 07:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| f204181e-4579-3941-a7eb-94b878eddf63 | -10.9013 | -45.3279 | 2026-09-02 07:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |


[Clique aqui para ver as próximas entradas](README67.md)
