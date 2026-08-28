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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c10111c-77cf-3754-ab45-12ce2c3ebb03 | -8.60852 | -70.91547 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 706a2def-9acf-3ff9-84f6-a73476ebac50 | -8.14441 | -70.39544 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd2b96b4-dd5c-3620-aca3-fb18af725f53 | -8.01025 | -72.05382 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 3d624f2c-5921-3cc9-99f2-9b88837ea7ca | -8.49526 | -70.31274 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 75c8cf15-fbd5-35d7-9814-31f9b71a4a9e | -8.37564 | -70.14166 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 21.2 |
| f8a7a2dd-c114-3c85-8e61-a488a0533bf7 | -8.33799 | -70.28666 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 103ae0fa-dd1e-39bd-9b94-6914d5ac6637 | -8.45351 | -70.60009 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 850044ed-2be1-35cb-9f76-8a8b212f330d | -8.40347 | -70.83549 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd5bc66d-fb47-32dc-93eb-7b59d070842f | -8.92193 | -71.24468 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2e822f30-6e9b-3202-b144-a1a74ebb9dbc | -8.96801 | -70.62218 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a688372-1cb4-382d-aeb5-b5fe86a99303 | -8.63804 | -70.50797 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 68899382-3378-34f2-9e41-b32d4feff5d8 | -9.04121 | -70.57591 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0d661661-b118-31f7-b917-951772e8f1f1 | -9.27982 | -70.33912 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 89fa200a-e261-3136-93fe-4e7ec255ba1d | -8.52646 | -70.94914 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4220176a-9795-3136-bb04-f55fabf1029e | -8.45763 | -70.41917 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af27878b-d6d9-36d8-b74c-ab4fe9cc18c3 | -9.42619 | -70.5772 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 13.4 |
| e49ee282-aea1-3be3-9e97-4338e9cab76d | -10.53908 | -69.84739 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a4c14863-ffb3-3d34-8d23-03c5726dd9c3 | -9.13385 | -69.82092 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 283139fb-4c07-3347-a2f4-b56fec9e0b2a | -7.92395 | -70.66516 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 57df8b2e-9826-3542-8378-33f7d73077ca | -8.22161 | -70.50683 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ec6c667-d74a-30a5-af13-8eefd130879d | -8.61433 | -70.94591 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 09d18243-23b6-36bf-82db-d420aada636c | -8.90953 | -71.24262 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6bf605e-20f5-3904-9226-b632f3d465bd | -9.07694 | -72.25701 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b1fff53e-ae22-3eb1-b899-96cc46b6f30c | -9.0776 | -72.26054 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 17.1 |
| a1e33ee5-6177-33eb-873e-dca8d4f1f54e | -7.93123 | -72.45653 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e8e4af7f-51c4-3ce0-9537-7c0288c8b311 | -10.52972 | -69.62225 | 2026-08-28 19:08:00 | NPP-375 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 54b09ae5-31f7-3f86-be98-36a2fa1881a6 | -9.04208 | -70.58054 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| eec24e3c-93b9-3e20-99c3-491d6ed1c578 | -9.13161 | -69.82245 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 8c0c4acc-5033-3af2-bed2-9f7c3fc789b9 | -8.86411 | -70.90522 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2ff098ea-1b95-3316-9d44-c64ea7591c3d | -10.55098 | -69.87498 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9c8103b6-7890-3d40-be9a-fcab69ffb140 | -10.07329 | -69.12581 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b043d32-38c9-3f1e-a0cc-865b13797f2c | -9.05431 | -72.25972 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9085800b-0154-3cc0-87b5-7ad083dad6bc | -8.64427 | -70.50797 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0641b554-fb98-33bd-a2a3-d284eabb395a | -10.32024 | -68.45753 | 2026-08-28 19:08:00 | NPP-375 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bc2f561f-6050-33cc-9c91-be799710a80d | -8.53543 | -71.47414 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5bf8f247-0246-30ac-856d-20fd15affa94 | -8.90293 | -71.39668 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e8439cb8-314e-3384-a430-429b46c47973 | -9.37843 | -72.71861 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9507dd3a-6d76-32df-bf26-175eff697941 | -7.87441 | -71.76624 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c2bea9-8781-33e3-b7fa-f17d26169d1c | -8.5507 | -70.47532 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 18.9 |
| a6d403c9-0e14-32be-99ec-1cb442b1abc7 | -8.87006 | -70.90418 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53923aab-3636-3dfa-a6cb-71304c4cfd93 | -8.529 | -70.94541 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c3c6ded-0b9a-3e96-b2f0-8120cb040d58 | -9.02509 | -70.91357 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 91103135-b7c9-3d58-994a-28f6f1dc22e1 | -8.37917 | -70.84537 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8da3437d-921f-3793-809f-5c4f049525d3 | -8.38034 | -70.84466 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 111132ec-09ea-339a-b28c-3f624a9c3de2 | -10.20594 | -69.35853 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6ff010a2-6e1b-3408-8362-5317ca4a231a | -8.91266 | -70.86897 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebea8f1e-a96a-3e33-8e58-a40f2aa36b52 | -9.03172 | -69.57719 | 2026-08-28 19:08:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 10ec3cd8-35d8-3a65-8b32-b02902587eb4 | -7.92453 | -70.66291 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a142d86a-6c55-3be7-b958-800739b768d1 | -8.89641 | -71.39355 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5b29586c-cb29-3202-884a-591e3308b8b1 | -8.01958 | -71.20412 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 25.6 |
| b555adaf-47aa-31c6-9eea-458458af5445 | -10.53276 | -69.62186 | 2026-08-28 19:08:00 | NPP-375 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5611f962-9bba-3cf4-93bf-3246a4332866 | -8.57325 | -72.41089 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a1f97047-42ee-38d5-93ac-5fa0b38c5fc8 | -8.60888 | -70.21188 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f01b6eee-311b-30e8-a3aa-cc8ed0dfc501 | -8.5673 | -72.41679 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 65d7b9f8-8c89-3857-a025-42c16f4c7bf6 | -8.37899 | -70.14065 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f663626e-7542-3a3a-b5bb-1209985d33b8 | -8.24872 | -70.1021 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 20.4 |
| c12316c0-a4d3-3f65-9e92-f5c4f3d5f69c | -8.84793 | -71.29277 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee52201f-59af-302f-8573-20f4d0e308f9 | -8.82581 | -70.63634 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 77a0acee-8346-347e-a256-4c9430c44dee | -9.07666 | -72.2593 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 0da3b202-ae01-320c-a448-efde973b116f | -8.59647 | -70.2144 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d3641bfc-28d6-3628-8365-d394c6238778 | -10.04567 | -68.99084 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 48b9c01e-7134-339c-87d4-b095efb18cda | -8.20376 | -73.03391 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 30.5 |
| a265b5ee-5f3d-34d0-b8e9-1480e3a3b3a3 | -9.69848 | -67.34366 | 2026-08-28 19:08:00 | NPP-375 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 422c29fd-7832-3ee6-b552-e96628d637fe | -8.03106 | -72.82081 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d58d02e2-877b-31c8-8e35-fe8ef131dc6b | -8.52694 | -70.8535 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 818fa4ed-0ce5-3772-adcb-3f88ba4032f6 | -8.65199 | -70.75188 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 08d9f00b-4f82-3fd2-8d34-2a53c937b1ef | -10.29007 | -69.10802 | 2026-08-28 19:08:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7141af71-2250-31c8-bee9-669bf58d041b | -9.43208 | -70.44505 | 2026-08-28 19:08:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 16ca274e-1818-3a96-8734-299c67c245ff | -7.54382 | -70.0007 | 2026-08-28 19:08:00 | NPP-375 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| be1920d9-e745-3bbe-ab95-44e6e16baa87 | -8.30225 | -72.07738 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4351429f-47ec-3af0-b5d7-c82b2e695bfe | -7.82257 | -69.994 | 2026-08-28 19:08:00 | NPP-375 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b586257c-c574-3ae1-a240-e030cdd42fd9 | -8.02765 | -71.24694 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8afc1318-5f99-3c30-bb3e-274d8c8698ee | -8.35851 | -70.29313 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0eaf1a0f-9120-3647-a0a4-4fcc855789db | -8.79807 | -70.82677 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1ba8e99-36b7-3a27-97b3-3cb325be8455 | -8.21362 | -70.49831 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bbd30894-4249-3c87-83d9-5f924d30c163 | -8.5721 | -72.41238 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 6b7a7bb8-97b6-3087-a530-86476d058f75 | -8.91593 | -70.87089 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c808d00f-47c6-3f4a-b1b9-b5782a1876aa | -7.99482 | -72.33925 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b98bdd33-8849-316a-ac68-11eb49c37c1c | -10.20695 | -69.36372 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 78751180-3165-32c1-9e8e-8e8af4b893b1 | -8.93469 | -72.52992 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23746135-2e9b-3ada-93fd-a649b4f05bb1 | -8.44765 | -70.6003 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1dc42a16-1538-35fe-98a7-4c42feba27ca | -8.7874 | -71.16251 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 06f6c0a8-e6d0-3f2c-8501-7b492f20cabb | -8.26629 | -70.78065 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9085d608-cf14-3b47-9e81-efba289a0ec4 | -8.3819 | -70.14046 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 62a82c81-a568-3cb1-a2b1-89aca2132370 | -8.63815 | -70.50903 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 89214c49-70a9-3521-87cf-3eaf3611a09e | -8.6066 | -70.9164 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9b44925a-46e8-3e4d-93e6-65df3708f272 | -9.03276 | -69.58253 | 2026-08-28 19:08:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7d06a05f-219b-3fb9-87f5-36cab9eb7a4e | -8.2511 | -70.10213 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cfa6fce3-9d3a-36fc-91da-227dd92bafb5 | -8.60925 | -70.95155 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d141c471-ba2b-3f8a-8235-cf07f9522972 | -8.61303 | -70.95143 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 5fcdd4d1-d5ff-3a20-9e8d-e1c73c2f235c | -10.5408 | -69.84726 | 2026-08-28 19:08:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3df38be4-b373-3998-8b65-076344ed1bc1 | -8.30388 | -72.07794 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ad786895-e764-380c-a728-d8edb03ecb3e | -8.27166 | -71.14487 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bcb8e227-6d9f-3cf0-9520-78b69d7abed1 | -9.07123 | -72.2603 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7891ec37-0677-347a-949c-dc01f99e9722 | -9.07152 | -72.258 | 2026-08-28 19:08:00 | NPP-375 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b598ecde-9ea9-3928-b1d0-f2240ed3a39c | -8.01652 | -71.20342 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 24.4 |
| eec6521d-6ca5-3bdd-a079-a633baaee0de | -7.88841 | -71.48671 | 2026-08-28 19:08:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6df75dfc-543c-3bbf-a1da-aa1333c27a59 | -8.03502 | -72.40746 | 2026-08-28 19:08:00 | NPP-375 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9bed7857-a465-3e41-8096-e7b663f0d87e | -8.89717 | -71.39769 | 2026-08-28 19:08:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 26574850-c8da-320e-a101-3899853055ec | -8.56847 | -72.41531 | 2026-08-28 19:08:00 | NPP-375 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 53.9 |


[Clique aqui para ver as próximas entradas](README170.md)
