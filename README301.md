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

## Dados Diários - Página 301

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 101027af-2afc-3f03-aeaf-db388b2aa396 | -6.14699 | -47.95381 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f2d8ae5-4809-337d-91e8-b4227668f066 | -5.74965 | -41.65467 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fcf73e57-20ef-35f5-9b0a-a6edebca162d | -5.72925 | -41.77884 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| a2ef6226-9f53-3dd6-93ae-b2cca4527f7b | -5.95944 | -43.90379 | 2026-10-08 16:20:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 908311bd-e9ea-3a12-9c56-67b60b7647ca | -5.73564 | -41.77395 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b428f496-f95d-321b-9303-15e9003c3d91 | -3.01489 | -54.04924 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| fee2eabe-9996-3f4b-b3e6-aa9549739eca | -5.97249 | -40.91182 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6fead48b-e9cc-3eba-9025-9866eb1996c2 | -5.74962 | -41.67794 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| e3b33e6a-8a02-3f5f-8f29-0683f3b5cc8d | -4.78174 | -43.33971 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| c8c61a25-5668-3d74-b840-a27c7ea2f299 | -2.83325 | -48.651 | 2026-10-08 16:20:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 04d5893f-0ccf-3f4c-95e5-a4c16ff6bccf | -3.08897 | -53.95084 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 6840d6fa-1427-321d-8949-1ed8f0972534 | -6.21666 | -45.18706 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c841faf6-6ae0-3714-8a0b-e4de9cfaff2f | -4.67549 | -40.23584 | 2026-10-08 16:20:00 | NPP-375 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| dc8e6265-70ee-3674-b73c-47a384a1a72c | -3.07552 | -53.95949 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8fcedf1e-5080-33e1-be6d-c920fa811585 | -7.96106 | -47.27268 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be0683a8-6118-3897-b291-38bccaeeeff7 | -7.853 | -45.15183 | 2026-10-08 16:20:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62c3d121-83b4-3f8e-ada2-cf6dc3c07b6e | -5.70105 | -53.49348 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 495e663c-7781-3cec-adb9-01f06e6cbc26 | -3.3476 | -42.4919 | 2026-10-08 16:20:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6819eec-3fbe-307d-b97b-3d405f073df5 | -3.39162 | -50.2185 | 2026-10-08 16:20:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d3bf2a09-e5a2-3965-9f4e-2e86b8cc83de | -1.19887 | -48.92522 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 739270fd-8216-3977-8640-ce2ea7fdcd12 | -6.7913 | -45.05569 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 0783147b-940a-3c76-b4b2-27e91a8be204 | -6.3175 | -44.04095 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1d34ff3-26d3-30ad-99d8-9ae569b61576 | -6.19915 | -52.87858 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 29a1d89b-aed1-30db-819f-eb32eda136ac | -6.41145 | -44.95642 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 5edf240c-1bb6-34c8-ac67-5bd8d2e6e755 | -3.08066 | -53.94461 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| bb9eb445-2190-31e0-a3e6-bee2ef3ec8df | -8.19337 | -46.36216 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 68482e07-6075-329a-b2b7-1f8e05d0f14c | -3.00869 | -54.05748 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| de00d833-3709-3905-b6c6-b0b0c4361281 | -3.91199 | -44.38884 | 2026-10-08 16:20:00 | NPP-375 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7d67de0b-0bb7-347c-836b-615fb07ced50 | -4.51902 | -44.01076 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| faa38fed-58f2-33f3-94b3-30260f1072b4 | -7.37646 | -46.23088 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9071b297-b9a0-3452-a187-1f43dcbf3eef | -6.17236 | -46.02012 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 78087fcc-5ef6-3405-917a-494ba15bc3cc | -6.83019 | -50.35203 | 2026-10-08 16:20:00 | NPP-375 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35cc7713-0ccb-30a9-9122-753a34fe4de2 | -6.67778 | -45.37745 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f36acbf2-dd82-3ef9-aac8-74a2f26dfef1 | -3.195 | -42.00997 | 2026-10-08 16:20:00 | NPP-375 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a774e738-a869-3d31-aff0-4dc7110b2c19 | -6.12313 | -44.1433 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73c9f922-6500-3181-bafe-f04687756981 | -3.36008 | -50.4851 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 462a6790-5458-35d3-b667-ca1e7103f782 | -6.36791 | -45.80122 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 9a86c20c-61a0-3c85-b91e-2e8ac1aa6e11 | -6.33544 | -44.8738 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea39231c-88d6-35be-997f-379ec26f45ce | -1.87948 | -46.70214 | 2026-10-08 16:20:00 | NPP-375 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ba133cb0-cf1b-3a8f-a143-8799a25abf01 | -5.54713 | -43.22724 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 2b964da3-5509-305d-a972-3b43558ba19c | -6.19733 | -40.80775 | 2026-10-08 16:20:00 | NPP-375 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd06a19d-9050-3e59-895a-1b8209489c12 | -2.05194 | -45.45966 | 2026-10-08 16:20:00 | NPP-375 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8bac90e-9380-3d14-aa0b-7e56ef1b0feb | -6.2064 | -52.8424 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 345c54e5-431b-328a-90a9-71421d1ce5ff | -5.29794 | -43.05539 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1a05cd4b-a515-38c8-8232-58fac266a3ad | -6.12709 | -44.14264 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bb504106-c39d-37e0-80c0-aea719b26b96 | -6.83645 | -39.55635 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 2b241ad1-4197-3da0-a882-03e5370ea270 | -4.84993 | -44.09232 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 64920f88-5863-3641-bec2-aee2811344a2 | -6.57885 | -41.61004 | 2026-10-08 16:20:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 475de9cc-12f0-3f0d-bc06-9ecedc157339 | -4.29537 | -48.60409 | 2026-10-08 16:20:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 644005c4-b30c-3e93-90db-f4940b9cd8d8 | -6.67949 | -45.57988 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| aaa1c244-599b-3018-a72a-5ebe3c4fe31f | -7.81884 | -44.57596 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2903a478-ad69-3442-ad00-7d2b116a1f80 | -5.09226 | -37.49939 | 2026-10-08 16:20:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| cf47be59-9753-3cc2-b055-e74b1fbab016 | -5.39427 | -42.95454 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 13.1 |
| e1955ef8-512f-3d0f-8aff-d9c9449dc690 | -3.55803 | -44.55762 | 2026-10-08 16:20:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 194a75d6-8303-3452-ad9c-1da7da669bdc | -3.50387 | -45.19792 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f74a6c5-ee9b-3675-90e1-9bcae3aecb0c | -4.93342 | -42.81092 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9b55e7a5-39bd-3490-b1aa-99d152dbbc39 | -7.46117 | -42.85807 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a0075ced-91e1-3ff8-94e5-187347d7b022 | -7.88165 | -44.96689 | 2026-10-08 16:20:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4548d0d4-8d4b-3006-b7bd-c4d191d8aff4 | -5.75191 | -41.74016 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 45b26ea3-6d6e-3e9a-bd85-9d4be63a3730 | -3.25382 | -54.04352 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5857edaf-73fd-3859-90ce-81749f7c6ae2 | -6.06849 | -37.03009 | 2026-10-08 16:20:00 | NPP-375 | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 7d489da9-8ba1-3be0-866d-2ea28f421547 | -6.33499 | -43.34822 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 57242521-3240-31f9-b8dc-63d6e6996ab4 | -5.50828 | -42.82232 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 0c797616-8e15-3502-9855-233d0513f076 | -3.79429 | -41.66193 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 9d57e1bb-3d92-3992-a75a-b25ee2b64197 | -5.08982 | -46.21684 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 39e07822-27e5-3b94-8bde-6a4c2da0862e | -4.36185 | -40.41995 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4ba1a291-22ae-3a6b-b3f8-6656c3bc583a | -7.2637 | -45.34628 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| b30b3db7-1c28-3b80-9863-6d239267119f | -7.59881 | -42.38766 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 38.3 |
| a80b53f3-8c88-3c92-9462-30c8cbe5fc0f | -5.53021 | -43.21606 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5a7d11fa-77b6-3ea4-8388-747a0a2da928 | -6.2943 | -43.87208 | 2026-10-08 16:20:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 63520be4-3d04-3b63-a7e1-d74ca5562352 | -7.20874 | -45.09047 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 065d02d6-3f45-3351-b039-bc10d9155da2 | -6.67719 | -45.37329 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| d627b70d-23e1-3266-80d2-c7f1ee875ddc | -1.70014 | -50.38016 | 2026-10-08 16:20:00 | NPP-375 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c673178a-d55d-3253-9c9e-cbbedb32e05b | -4.17947 | -43.0192 | 2026-10-08 16:20:00 | NPP-375 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94ff6be1-e4b3-32d8-ac8d-6a083f95e0a6 | -1.42984 | -51.5434 | 2026-10-08 16:20:00 | NPP-375 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| bad64b1d-99ba-3d74-a19b-324812b12ea7 | -6.53623 | -45.38858 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| e0c1a041-8c46-3e54-856c-34039e02dbd5 | -1.73969 | -50.14602 | 2026-10-08 16:20:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17d9cd91-0639-3163-9c42-0f9870e7763a | -4.36797 | -40.41546 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 3485e598-b4bb-3788-9c87-d72f9fcfa7e6 | -3.09112 | -53.96511 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 015292e3-9f9d-3331-9919-5d8679367804 | -5.70285 | -53.45246 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 91d372c2-b4f2-3f2e-bf83-3c873924ae29 | -6.94526 | -43.07135 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b5aa55c4-1fcd-3c22-81f8-21335f83992a | -5.50098 | -40.53563 | 2026-10-08 16:20:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |
| ccf6260f-c5f4-35a2-88d4-6e65edc7315a | -7.47421 | -42.84229 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 43724af3-350b-3c68-a197-e58f3cfb807b | -5.98873 | -40.92778 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| eea7a0cc-0e0a-398a-8e9e-63e2d2057475 | -5.27917 | -47.91615 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7c5ac3ea-9b18-3445-b3b4-e18b5f980f8f | -5.70382 | -53.45956 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| a931b2cc-5774-304c-9a38-0481824b1c41 | -5.74876 | -42.07868 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 0d14c6c9-0ec9-37b8-a5d8-d9fdd73d137f | -5.96825 | -40.91287 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| a701a324-7cd0-392f-ac4a-2764b55e24b5 | -5.38495 | -44.17817 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c9871ac3-0d18-3c7f-89ca-69f3294abb28 | -6.77192 | -44.12659 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8b81618f-7a35-32e5-b431-dccc02975361 | -7.08677 | -43.09148 | 2026-10-08 16:20:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7d47efe8-b033-36df-b1a1-74b42135f120 | -5.73215 | -41.77446 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 5a6be2ff-11b9-338f-b75c-136204b11532 | -6.15001 | -39.44511 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| f9a201fd-40e8-315b-8960-f64107a4994f | -6.23516 | -43.74103 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0268017-faa8-3518-a1cb-0c139c8cbf76 | -6.3248 | -37.7503 | 2026-10-08 16:20:00 | NPP-375 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c5e59bde-e653-3494-b02c-1472951447ee | -2.99399 | -43.28329 | 2026-10-08 16:20:00 | NPP-375 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5ddfcb8c-466c-3abc-bacc-bd8146a0727f | -7.22297 | -44.27668 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c53e886-bf16-3893-a780-923e563f5f4c | -3.4439 | -45.09583 | 2026-10-08 16:20:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c5192592-c810-3c3f-8eab-e0ddef998cee | -6.13417 | -47.93695 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 77a8ae19-64b5-3853-ac53-038a0a4d47e7 | -2.95492 | -43.51777 | 2026-10-08 16:20:00 | NPP-375 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README302.md)
