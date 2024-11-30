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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 020bf12d-1334-3590-9c81-9e35c1a2f466 | -2.2746 | -46.43331 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc75247f-856d-3242-b07a-fb21cf62e3ed | -2.76186 | -54.08876 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 591028a1-93ca-3c4d-a441-815a184f4674 | -2.76606 | -55.32902 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0ad5c38-c7bb-3730-9324-79d5d1153f45 | -1.68188 | -45.78961 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e9bd45f0-876d-342b-9c23-edfcb15e0240 | -3.863 | -50.53888 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65f30e2d-cd53-3751-b8a2-597c1dc74104 | -1.26943 | -51.63217 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3f91d07f-59d3-3b20-80ba-d9de3e483596 | -2.86935 | -54.00489 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46e9fa72-1b62-3b72-8456-91836629947b | -3.52831 | -51.48098 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d3ae932-0fc7-347e-b1ce-1eddbe41f386 | -1.32028 | -51.67194 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1537bff-ca2d-3034-a842-28b38f8a6968 | -1.19099 | -51.76046 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7565fc8-613e-35a3-87ba-5f6f0ba0e1ab | -1.28086 | -52.69265 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f035a021-ca83-3786-bcbc-3069510dd28b | -3.03596 | -51.77993 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4f25221-eaef-33ea-bb6a-9e9c6f74cc32 | -3.54193 | -50.18063 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0b21633-db6f-3a5c-9cf7-8b59a37eb915 | -1.62869 | -53.86633 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41a357be-34fc-3bed-a464-3d1af7254d45 | -3.33473 | -54.14146 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e4c44e7-8847-3ad0-9235-3bcaeb8f17de | -2.59307 | -54.21189 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdd4fd88-1b46-3fa5-ab0f-f5edaa37fd8a | -4.86819 | -41.31535 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e2bdc471-e71a-38b9-b96d-1278c224d0d4 | -2.46419 | -46.56145 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66e4a026-1bec-3757-9fe3-0aa587c899df | -2.76086 | -49.22807 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 712465d9-4a81-351c-8345-3c7abf84a68e | -3.14651 | -53.82747 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17727453-97f6-38ad-a5e7-6cdad151c436 | -3.70173 | -45.68977 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f26ffafb-1063-34aa-b2c8-479715281899 | -1.59831 | -51.269 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b06ea6a4-7fb2-3136-b310-570ba8efaf54 | -2.23832 | -53.62543 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21f057fe-3086-3bdb-ad8b-96922f1ac318 | -3.08106 | -49.50103 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b51f8e7a-203a-3038-9dde-c15672d9fce9 | -2.78848 | -53.20941 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0607528f-275d-391e-a037-b2a60b00d444 | -0.91315 | -52.70119 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cdc2610-c849-377d-ada8-8d63a4f1135e | -3.14877 | -53.83504 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 296a599d-b51b-3344-9339-fcb2571e985b | -2.59577 | -53.9765 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e7ddba8-651e-368a-b633-2361ae29b12d | -3.46661 | -53.78888 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b691cc5d-81dc-3601-8653-fa9cf7329d61 | -1.53635 | -55.86827 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed5f9ad-016d-3b94-af5b-62291ed41d7e | -1.72539 | -52.47908 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f3f07b5-c919-3291-bced-a1076a24b810 | -1.65577 | -54.23649 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee21e7f7-3f3d-3846-9ad2-90ad3172533e | -3.3754 | -50.82023 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e70b9bb9-95af-3cda-859b-1c154ea27d21 | -1.60287 | -55.55702 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b6ff414e-f680-36fc-80bc-0e28f05bfcf8 | -3.40434 | -50.66474 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2248458-7b9d-36a2-adb6-22d1385adc87 | -2.60173 | -46.56802 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db0633ea-8b9b-35d6-8dc8-eb1c7a2b7408 | -2.21733 | -53.75955 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fba1b41-53a9-3bd8-b07b-abff081962a5 | -2.24057 | -53.63303 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f28dee-952d-3ea5-b98e-36bc9619e4c5 | -3.40308 | -53.02558 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e892e8e1-00e3-3785-8f09-f3676910983d | -4.1073 | -50.98361 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8304f6b8-4d7c-3a96-afa1-924a4eedf83d | -3.08352 | -53.28796 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b576f82-4211-3caf-a431-7511e2a3cf86 | -1.07768 | -53.63096 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 69048dcd-a1bc-344c-a48d-e9e7089dedf5 | -2.44516 | -53.97121 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38f2edef-be14-32c8-b0f0-b040ea7b0a16 | -1.36352 | -55.18737 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64009329-b055-37b9-9e9e-aea4bfeadeb5 | -2.88864 | -48.87316 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa819b77-37ba-31d1-8c22-08a33c48f6bf | -3.95934 | -50.18972 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73bc9bb0-2a48-3d16-a810-ed5008f3377b | -1.45482 | -51.49815 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa19beb1-2298-3f51-a74d-36381d250a55 | -2.85169 | -54.09539 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a27254f1-3a1c-3840-bc8b-c5af02f85d73 | -3.67487 | -50.17547 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 191f20d8-3c5b-35ff-b736-0412ba4cca0e | -3.75564 | -49.94457 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 810e4633-57b4-36ec-871d-2dabe79d3148 | -1.41527 | -52.03596 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbf23e46-d785-357c-ae15-f6581304b3bb | -2.82275 | -52.9693 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 251d065e-21de-3e3d-a5ee-a302de6e9381 | 1.38163 | -50.94564 | 2024-11-30 05:01:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bedbfafa-7371-30f7-b44b-68821b3d5b2f | -1.0033 | -51.71696 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca410d94-ab7f-331d-9a68-d2b6678ab6e2 | -3.63611 | -54.4421 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef69679e-f358-30be-bf4c-24c95885bb69 | -2.80705 | -53.04677 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5316ae74-1ecb-3a72-ae68-dad948b825d9 | -1.57712 | -52.27022 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd1f6be-25df-307e-92d1-658251540a2e | -3.25794 | -53.64426 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 762f6e94-510a-3154-a4f2-0ca28c6a5fca | -1.11602 | -53.7262 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 414f1d03-0726-371a-b08f-83c640e9974e | -2.87541 | -53.32375 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce0c134b-40e7-3c01-9994-4eca50f095e1 | -1.33125 | -51.42704 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe5491ff-5b97-3ac7-bb58-45f4a0c43a1a | -3.31468 | -53.75123 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5591ba8-8355-3587-9052-882286a90b6e | -1.96524 | -52.89412 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d530d0dc-24f9-3210-9cbb-5d16a0582e0a | -3.80433 | -46.53767 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2be73f7-935c-3aed-990c-cbf7bf229843 | -1.72394 | -52.47972 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35d025ff-a9bc-3322-8ff5-f6ddde4d04b2 | -3.65636 | -54.72244 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62fc5fd6-84e4-35de-b518-fa759b954d1f | -0.29886 | -51.79764 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f88fc633-ab56-3504-9712-e62b1d7c9e8d | -3.48034 | -51.26125 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9463a1bb-dcb5-3600-9176-449cc4ba8bf3 | -2.59911 | -53.97701 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0a1d34d-5fe4-3a36-b445-3257329ba19e | -4.5482 | -50.70665 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 740fd8e3-9751-30c3-9098-02d53683538c | -1.09635 | -53.3815 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2f58857-724a-36a8-8f05-4348e05e9f0d | -3.11788 | -50.29353 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6011f6ae-37c4-3092-9764-d2ad70550674 | -2.95795 | -50.57617 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 64dc9075-4b8a-3086-8ec0-7d0ba3eb3f9c | -1.06208 | -53.21663 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb70bc83-3e9e-3890-a142-9df93dd24bbc | -4.12732 | -54.28936 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b03cc1ff-774a-303d-a348-817c9412aa77 | -1.09356 | -53.39926 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6460d0c2-8650-3d4e-aedb-761791822268 | -2.65861 | -48.79522 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bee07e9-f846-3057-ac84-e78f36a18e27 | -3.76214 | -49.90092 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 961d048a-7013-3784-b30a-60fef51db112 | -3.88466 | -52.36047 | 2024-11-30 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f58e8f95-a066-3144-bbb2-69326d33e95b | -4.91113 | -49.89985 | 2024-11-30 05:01:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e1d5d56-da0b-3bb8-846a-f03cabe361df | -1.65552 | -52.73385 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d51e6acd-fd0b-3d1e-8aeb-f702acb36730 | -2.81928 | -54.0402 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13c01127-b568-35e0-8819-1baf24efe306 | -2.93092 | -54.32525 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7ad6a9f-d3c1-340d-93fe-c48239e5dcec | -2.60094 | -54.24869 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d98b5cb8-dbff-3714-bbf5-bb39c1c392f9 | -2.76219 | -55.33196 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd26770d-d6b5-3fc4-ad2d-31cc19388f23 | -3.48406 | -53.80983 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5341b499-2188-39c2-ac87-d3a9d0310f4e | -1.38282 | -53.64596 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e5732b4-1f7e-3563-a856-a04e04044be1 | -3.39293 | -50.31536 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 65ae3145-59a5-372f-82fb-c48c82596f4c | -2.88201 | -54.11432 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ece394d8-2068-381f-b152-5eb0b2131326 | -3.6524 | -50.21474 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab1f8f80-4aad-3374-8ad4-98581f375779 | -2.97468 | -53.29013 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5540bbd-56e9-37c6-a65f-d7c864acd748 | -3.34213 | -50.23793 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a59c9aa1-8a98-33c6-88da-6215fe29c28d | -1.52908 | -52.66918 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efa5d175-a0d4-3aa3-bc37-e954efc31874 | -0.97456 | -53.6833 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab093773-198a-35bb-82da-4149614ae2c1 | -1.72274 | -52.48729 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70a01f16-e791-33fd-bc55-0f9779a16022 | -1.36795 | -51.96833 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3900a153-cb61-3b34-9228-09e8398b3a4b | -1.61759 | -53.8718 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29aefece-951c-3e47-b34c-088a4e463553 | -1.70605 | -52.76373 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad77527d-0028-3280-bde5-971a35e1f37d | -3.96344 | -49.91092 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7f492c9-120d-3b79-89cb-0eecdd9beaab | -1.18364 | -53.92202 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README115.md)
