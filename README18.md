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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51c3a9a6-4c95-3b6a-a42d-43206e430fad | -3.09944 | -49.25088 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a75fdce-e00a-3d0d-896d-d5f5999dea99 | -7.53517 | -47.38673 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5026cbc9-9ab0-33f7-9f88-e2d1b3dde0c3 | -4.28728 | -45.89165 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4995db0-c91d-3d2e-bfba-371999e26fa9 | -7.46583 | -46.6387 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca1d380b-ec72-398b-9b91-af8d153cbbe7 | -7.57021 | -45.86452 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c84fe03-a150-3fb7-93a4-72d6a12d5d4c | -6.22915 | -47.32912 | 2025-11-08 04:36:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77333555-7bbb-38ee-9838-8fe44a746b3d | -4.47639 | -45.33059 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7eefa1a9-6b2d-39aa-bfad-ff8bc1d0f334 | -7.04159 | -46.9845 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 699864e3-cce5-3d35-a6e2-ca3ee330b97b | -4.68239 | -46.40235 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91563bf8-9592-3137-b56c-baa524386848 | -2.70747 | -49.53973 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cecec4a-26f8-32b4-aa6b-5f941aa2160f | -6.16472 | -44.26595 | 2025-11-08 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fabf1a80-9d6f-303a-9cd8-ea454f03ef7b | -3.24658 | -48.7619 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2490254-bcfc-3270-a284-d8c8d536b509 | -2.61432 | -49.22252 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70ef4343-eff5-398c-ba25-16919d2b5114 | -3.43954 | -52.63785 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 413c8340-0aa6-3ed5-809c-9782f9afe098 | -3.45515 | -49.84885 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07516c42-9a6d-3f49-8f4d-28996aa55ba0 | -3.33547 | -52.56395 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7a3106e-1daf-3b6c-833d-9f0b3e04986c | -3.31744 | -50.12003 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b7ced53d-bf71-35f2-ac3a-ec8ad0f4e39b | -3.03994 | -50.30767 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ea13ed4-d881-3078-8588-313ae0109547 | -5.79272 | -43.73598 | 2025-11-08 04:36:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7fbb67e-d3f3-3550-b47c-5c9d2777e321 | -4.81351 | -45.58043 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4e120ee-508a-39d4-9a7a-c536ce11e300 | -4.59891 | -45.99476 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b86ff61-0b15-3199-b539-7ccf7b6fcb32 | -3.40475 | -45.44024 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7e336cb1-e291-3c89-878c-aeca4bf91754 | -3.93908 | -45.41451 | 2025-11-08 04:36:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 935b8895-361f-3784-b441-a4b6e41d65b5 | -3.45203 | -49.84966 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e240b340-e6ff-3d6c-aefb-b6a0789b2788 | -4.59156 | -45.99735 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d3dcce82-8d62-3d97-aed5-df711a086f61 | -3.36144 | -49.51217 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c215e0a8-7baa-3fe7-9575-7bfd2f6f3207 | -2.8977 | -53.13041 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1cd1dcd-8cbb-33e2-9b86-ce81c0bd4cb4 | -4.26472 | -48.55709 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00744469-abe1-35f7-b462-8458e5e89291 | -7.38317 | -46.92805 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4a4b52a-7d19-3bf5-9f8a-3eecd354ab00 | -4.60783 | -45.55772 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d411498e-1c37-3d8e-a558-d455a5b219cc | -3.31386 | -50.11946 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d9d2338-8c4b-3d24-b5aa-923765ffac29 | -8.22418 | -47.39359 | 2025-11-08 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4fdfb4a-4337-36d6-b32c-2bf8604e0561 | -3.33416 | -52.56045 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3699a1c3-33d8-3529-a5c5-01406d4e8224 | -5.41265 | -44.82652 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adad2fba-5df7-345f-af0d-7f51a060b2d6 | -3.43524 | -50.2421 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e2422b2-22f0-3355-aa5d-d658415fc012 | -5.18826 | -46.15506 | 2025-11-08 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c67d72a-ea58-3091-b71f-fc1a8034f8f7 | -5.73027 | -44.5096 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da655110-cce6-314d-b0c4-a916832ca9bf | -3.4361 | -51.5229 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2462e085-53c9-328a-a540-384a40fbda20 | -3.404 | -50.27514 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b7ae01b-2075-3b3c-b207-000eed6cf665 | -3.40874 | -45.4371 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 61a41ce4-927d-3e0c-9298-acd38b490161 | -2.99067 | -48.70292 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e655ae4-f8f4-31fa-8584-fae2a582379f | -3.1888 | -49.8014 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce16803d-4f28-34f7-af2f-bb4d280904ff | -3.58201 | -51.24474 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49b62b39-d448-397a-8c3b-8d9195a917f4 | -8.49152 | -44.7277 | 2025-11-08 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed29367c-a59d-399d-93da-47fa7b5dc784 | -3.1225 | -50.14542 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20882121-0528-3eb4-972b-e11e1460c525 | -4.77377 | -49.50157 | 2025-11-08 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94217818-95a1-304e-93b3-d791ca9f39b1 | -4.83009 | -45.60968 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2df4a42d-ca7d-30bc-ad07-c489f489a177 | -6.47042 | -43.2702 | 2025-11-08 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06619b5a-c9f2-3006-b4cb-203593794dec | -4.64991 | -46.87148 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7759f1fa-9129-3a0f-99b4-1e78043c7d8d | -3.61607 | -52.12095 | 2025-11-08 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26efe30d-0b2e-32e0-b41e-0175f40e1f53 | -3.35257 | -50.17597 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7c5c543-3175-3b5e-95de-88adc7cf047d | -6.41042 | -39.5933 | 2025-11-08 04:36:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c06d4a52-da85-39fd-b54a-e61a69f48c7d | -6.26631 | -43.68217 | 2025-11-08 04:36:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3cda407a-599d-35f6-b338-18500714d66c | -5.77641 | -40.79968 | 2025-11-08 04:36:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ce557cf-df65-31d9-ae1c-02e89963880a | -2.49467 | -48.15216 | 2025-11-08 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 324cce9b-b5f1-3eec-af07-866ccd6ac550 | -3.63037 | -43.65672 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4fc5498f-4fc9-3926-a4fd-34a66ebba9c9 | -2.46004 | -49.37446 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2b82288e-e645-3eeb-97e4-57155e97de32 | -3.75341 | -45.08869 | 2025-11-08 04:36:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 418e0a65-fda9-3078-8534-b62ae7cda21d | -4.64603 | -46.87444 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e95ef6d-2cdf-3792-a51a-f4d2a7c883b9 | -5.78122 | -46.56076 | 2025-11-08 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 087a5a82-b12d-3cb8-969e-6d848dc3beb7 | -3.10104 | -50.32458 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 553964de-a177-353c-a27b-340048adadf1 | -3.14989 | -50.29814 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05e70160-ce4b-3a05-8b65-9b29132eb37c | -4.11447 | -48.01084 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3904fa2d-2778-3971-ac0b-15973db100c7 | -4.33732 | -45.72738 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c65a5a7-f880-3436-abab-fcb3b20c4d91 | -5.67554 | -40.85424 | 2025-11-08 04:36:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c25334a9-9ca8-37fe-a96f-31aa392a07c1 | -3.43164 | -50.2415 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92e80707-4f90-3b8a-8997-df0517355a73 | -4.03106 | -49.2751 | 2025-11-08 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6895699b-b450-3e23-be1a-6b28103c09a6 | -4.89663 | -47.96426 | 2025-11-08 04:36:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 421de1eb-9443-3a9b-84c9-879912ad55ff | -4.64827 | -46.8819 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d181517a-a8df-3e04-a982-76aedc8b62d6 | -4.6852 | -46.40641 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ddc19886-f9b9-351b-be18-fd53cddcd161 | -8.49523 | -44.72829 | 2025-11-08 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0082a0c7-2d0d-3d30-b7ea-94863e0aeeda | -7.46639 | -46.63507 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48722e9c-48a2-389c-b194-460db31d41d5 | -6.01207 | -49.13775 | 2025-11-08 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65befe96-a0ea-3959-9963-0e03a3cfb883 | -6.09883 | -41.70965 | 2025-11-08 04:36:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7405552c-69f7-30f5-a1a2-2ed1f8544f12 | -4.5697 | -48.48571 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9818deec-9711-3386-aa7c-c12740eb14a3 | -2.43913 | -49.34461 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3fa395d-8ac0-3930-ac92-0dd1948df03c | -6.3676 | -41.7445 | 2025-11-08 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8ab06ddf-78ce-3771-a0a0-a61a2bc0b122 | -3.52569 | -51.56438 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f2e2215-05f2-3e22-ad26-c5c4de0f7826 | -5.23564 | -45.53267 | 2025-11-08 04:36:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa73d48f-4e25-3307-9fbf-e5fb52aa4d5d | -4.45055 | -46.43538 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f56779db-b29e-328c-9a0e-e713434bc25e | -4.38574 | -49.67375 | 2025-11-08 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e507c098-fc56-33dd-85f4-604bc2f6b58c | -8.07028 | -47.12553 | 2025-11-08 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cabd1bb-0c2b-3ff9-8eb2-0461244c7602 | -3.33424 | -50.19823 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51ce7139-ab1d-3064-87e1-87e7dbba8e13 | -2.98268 | -48.70951 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad83511c-a8af-35c4-85b0-c434a57a6f0d | -4.78266 | -48.50826 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66c5bef7-9235-3cc7-8d4a-29b9a5eb1f06 | -4.91237 | -45.10176 | 2025-11-08 04:36:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18aca491-b62e-3ebc-8338-6c35452e4a32 | -6.22359 | -47.01661 | 2025-11-08 04:36:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19816859-85a9-3254-b532-20992002b96c | -5.50028 | -40.77868 | 2025-11-08 04:36:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 3119b11b-13bb-371d-bd5d-5056bca31cc1 | -3.34439 | -50.20397 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 19fc63e8-1808-34e6-8c13-1170bf3937c2 | -6.41548 | -39.59408 | 2025-11-08 04:36:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc451049-74f6-37f5-87d6-8b5e439ba516 | -4.82971 | -47.79055 | 2025-11-08 04:36:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26cf9221-4345-3696-816d-7eac6acd8a61 | -7.08119 | -46.55411 | 2025-11-08 04:36:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 34a5c9d5-3915-3a8d-8c63-ca9d1dc0ee75 | -3.28404 | -49.77057 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d6ff8c6-799b-387f-8054-15fbfb6208e4 | -2.98326 | -48.70588 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2c08649-5dda-37d7-b772-5faf0b156542 | -3.56792 | -50.41489 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f23cc72-b40f-34f2-a8f4-173c52178ab3 | -4.67959 | -46.3983 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80509173-7053-3873-8fb4-83f4dcfd424b | -3.46586 | -53.28757 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8481f68e-f633-3792-b503-5fb389024f12 | -4.64548 | -46.87791 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d1ff6dc-7c96-37c0-b187-bedba5628600 | -8.93043 | -44.20114 | 2025-11-08 04:36:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbbf6b63-c9f3-3eaa-ad37-3513b45d8acc | -3.78186 | -45.84382 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README19.md)
