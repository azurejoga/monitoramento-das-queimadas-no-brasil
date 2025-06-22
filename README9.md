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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cde705d7-dc23-3100-b400-37f8cb542bc9 | -8.59765 | -51.58942 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 730a2ebe-3ce2-3bae-856c-0dbeeff5636a | -13.49595 | -53.49594 | 2025-06-22 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d66b8068-d0e3-3c1e-8c3c-810e2d1284e5 | -12.50741 | -58.35598 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ff8d1c7-e632-3463-94b0-3e9a7c722ebf | -8.59424 | -51.58889 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3b6f0055-ea5b-3481-b462-37771b03dde1 | -8.36295 | -55.09449 | 2025-06-22 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca188e64-95b8-37f6-a862-45c52be61d0c | -11.61599 | -58.28911 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 78b4791d-1c50-3d60-8200-d60eaead372d | -11.83582 | -57.76569 | 2025-06-22 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fca22c4a-ae9e-309e-9e1f-95f114f7f276 | -11.78914 | -57.23969 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f97a8a39-917d-3307-8f2d-db34e57d7bb7 | -12.0254 | -57.10133 | 2025-06-22 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 257120a7-34d1-3c8b-819e-7107ddcc081b | -13.65261 | -53.94247 | 2025-06-22 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0670a04d-e638-3ea9-a859-96b9f50dd2e1 | -9.09748 | -50.02892 | 2025-06-22 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56a8ae2a-cd8d-3119-930e-446344b3ba52 | -11.14313 | -53.93737 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d8aaee7-0c17-32b6-995c-ee6cdc050e60 | -10.88892 | -56.47363 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 58d3e1d6-e2a3-3177-bf16-a0edadafac20 | -10.12638 | -51.66379 | 2025-06-22 04:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4032ef55-3470-329b-9958-a6aa16a119bd | -9.24983 | -57.53109 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2243d386-a128-3b3e-8d53-c18c7a9bafdb | -9.52877 | -46.29634 | 2025-06-22 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0755e91-f6bf-3d74-86ef-90eeb0d03a7f | -10.60407 | -52.83997 | 2025-06-22 04:42:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a101593a-ce0d-3fc6-afa7-faee1377d5a2 | -12.50933 | -58.34568 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6655481d-a40a-35b8-b2e7-3e42631c89b3 | -9.46016 | -56.06331 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ead2805d-3541-3371-a703-e1585c90c85e | -10.08695 | -48.31352 | 2025-06-22 04:42:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43286bef-5a95-3251-81ec-fce7d13b39fa | -11.62076 | -58.28997 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ce3141d7-e14d-3f0a-896c-61ca9d226ac7 | -9.25455 | -57.53193 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 004194a3-4ecf-3946-8669-79b9dbb86144 | -11.7871 | -57.24309 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 246fa6dd-408d-3fcb-88ef-e6e53a7f6e38 | -11.78471 | -57.23886 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c14b88d2-e1e3-34b1-b4d8-21ee476ba1ee | -12.51902 | -57.23971 | 2025-06-22 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7674a4d7-7aab-3570-b72e-255cdd578d48 | -10.57674 | -46.924 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24b8b8fc-0ea5-3801-b25d-904228c21bf8 | -10.99003 | -45.08891 | 2025-06-22 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eddf46df-d84e-3729-92d2-189742d6610f | -11.78835 | -57.24415 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11e4a80e-0b85-3cc0-9eb6-7e3b27588cb4 | -12.02617 | -57.09699 | 2025-06-22 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ce3c883-e80f-3a31-9a47-c3577dbf2d8b | -10.8622 | -53.76458 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1daf8d9f-0800-3514-bb8c-1662567cd106 | -10.44697 | -47.02582 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a9f63b19-7308-3068-8293-7c3f70dcedfa | -11.93742 | -51.74839 | 2025-06-22 04:42:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0690fb6-0384-388a-bc4e-a599fe84df67 | -11.78956 | -54.77945 | 2025-06-22 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 398fd5dc-fe31-3574-982b-0b9f51b1a998 | -10.02888 | -54.32695 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6180c8b0-ccae-3fe7-af01-baa8dff49c67 | -11.95757 | -58.76327 | 2025-06-22 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 144c2be7-7343-3f7e-bb9f-55a11b7e5855 | -10.23254 | -54.29368 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ca7e653-2e80-3237-af53-eaa048b15a0a | -9.48092 | -57.33326 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0c476f8-de0b-35d1-b15b-c8dbb416f7ec | -9.92151 | -59.91578 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0298bcaa-b84e-3c08-8023-77ae0f984f0d | -11.13801 | -53.92311 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92b7ff2a-3b4e-3d40-b0a0-8bf4af41473a | -10.44331 | -47.02525 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4ef43fa-982f-38ae-9f70-d4016fa66d7e | -10.28985 | -60.55044 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0720f8ae-bbab-3070-ba87-0555c02e86f9 | -10.49909 | -47.79904 | 2025-06-22 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94679b2e-3173-3654-8a58-2d6c260a5aa8 | -13.23902 | -48.41452 | 2025-06-22 04:42:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87bb94c0-b971-322c-9602-68802a1fb719 | -9.33082 | -57.84464 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 105133d7-0451-3352-87a9-4c5de7104337 | -10.22801 | -54.29759 | 2025-06-22 04:42:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78d2da25-7b85-32c9-acdf-c0ea637698ac | -12.30481 | -50.08721 | 2025-06-22 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2761b80e-ee30-3d23-a269-78b45494696a | -11.79152 | -57.24395 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 023d91c2-903d-31e4-a4ce-825c225ee9c2 | -10.57242 | -46.9278 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 377a9eab-2d96-37a5-8b09-c8f5255e2e38 | -14.25099 | -45.5014 | 2025-06-22 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 985f0e90-c50a-300b-9ea8-37f82f4c1aa4 | -12.58017 | -56.97313 | 2025-06-22 04:42:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0718874b-c045-3fe1-99de-3150d64d663e | -9.46086 | -56.05928 | 2025-06-22 04:42:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 47ab09cf-21fd-3225-9278-846c190ca2c0 | -9.25071 | -57.5288 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a7739e2-4816-3202-8c27-d7f7e7d6a0ce | -11.61122 | -58.28825 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a448599e-24ea-3e00-a520-83316fe74ff4 | -9.46931 | -57.8392 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7aae5562-0274-3940-a804-ad316f6a52e3 | -11.95474 | -58.76007 | 2025-06-22 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16125a5f-1edd-30ce-987f-2284582bad9d | -11.62552 | -58.29086 | 2025-06-22 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 84a525b8-6c50-31c8-b651-50388aaf764b | -13.23939 | -49.83629 | 2025-06-22 04:42:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa86f4f2-f20f-3720-b610-f6fd6d2993f4 | -11.938 | -51.7448 | 2025-06-22 04:42:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4a4bf57-2a7e-3b60-ac9f-d14623a50a16 | -13.04134 | -53.71181 | 2025-06-22 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce5c9508-f419-3766-85a9-43240776c781 | -8.12329 | -61.41555 | 2025-06-22 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f671d00c-5c82-3749-9592-0a9be3173728 | -11.10047 | -46.67892 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65d14e9f-3d9f-3c03-8540-14f9a9ccc869 | -12.29481 | -50.10754 | 2025-06-22 04:42:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97989780-d3fa-3071-9d13-ac58b595eeb1 | -12.19474 | -49.62142 | 2025-06-22 04:42:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 985b4c55-c6c4-3fdb-8d92-7473c881cbf4 | -8.12126 | -61.41362 | 2025-06-22 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f140369d-6c7d-30b5-88b8-c54d9346b0d6 | -9.47408 | -57.84021 | 2025-06-22 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0f79ce6-9114-35b6-9373-ec992c5f4194 | -13.04243 | -48.84079 | 2025-06-22 04:42:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4decfa3e-ae91-3eaa-8263-6fb5b4e0fc41 | -13.2693 | -46.83476 | 2025-06-22 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3879319-38a5-3bdb-a4db-6bc977a00721 | -13.6533 | -53.93835 | 2025-06-22 04:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e7c72527-39c9-3bec-bc61-c5236b039a84 | -13.79171 | -54.29481 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba0e0405-cc4b-3a35-b953-afa839ab9f25 | -10.4586 | -47.02313 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0347aa55-0ce8-3d40-83a3-25c3959e86ee | -10.89463 | -56.46631 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f261507d-0f0b-3332-a015-28e7cbf85ad3 | -10.88537 | -56.46878 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 75baf078-9fbc-39bc-8cda-37a41d1457a5 | -10.9895 | -45.09268 | 2025-06-22 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a7be8f1b-83a0-335f-a134-ed065591fdce | -13.14174 | -56.80692 | 2025-06-22 04:42:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7c08c12-7abf-3ac7-93f4-6b8718a8994c | -13.79891 | -54.29611 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 318bdb1d-6417-3ee2-bc70-3105b8dc73f8 | -10.062 | -49.6568 | 2025-06-22 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5010a1a7-6f6e-3d7d-a332-dd468a6f5f27 | -10.86148 | -53.76887 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6cd8147-a92e-3567-9059-7002dd5d038b | -14.25522 | -45.50198 | 2025-06-22 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a1e9536-44ed-3bbf-ae0f-926c36fc3771 | -11.95274 | -58.76201 | 2025-06-22 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d9e509b-def4-367d-a070-c123fc836a86 | -10.43903 | -47.02895 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5e17a2f-5fec-3bc0-8bea-fa2498c1968b | -13.8018 | -54.30095 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53568b0d-9be5-3955-aadb-3b387d535f28 | -8.59543 | -51.58157 | 2025-06-22 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4d4f13af-d15b-3a91-8ba0-44827bb3695c | -10.88681 | -56.46071 | 2025-06-22 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 289fc839-c86a-3605-a2d2-39f2072cb101 | -10.95813 | -49.56842 | 2025-06-22 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 250f5aa8-7147-3874-8dbe-f27e594e5fe0 | -9.86134 | -60.29328 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc0d5ecd-4bd7-3782-bb5f-f094a76a24f6 | -12.60496 | -48.3753 | 2025-06-22 04:42:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a25c27dc-6cd3-326c-a83b-162fea7ea799 | -12.02333 | -57.08755 | 2025-06-22 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32026ec5-e406-38fc-9baa-0735f7b9a193 | -10.28231 | -47.61179 | 2025-06-22 04:42:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ba9208-fa4b-32b9-8de5-8eca2091c0db | -13.80251 | -54.29675 | 2025-06-22 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a785473e-5859-3e33-9d7b-2634679043a1 | -10.57179 | -46.93216 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f62c16e-f0c5-3e57-9498-f4b478306162 | -9.86207 | -60.28942 | 2025-06-22 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa5e0529-7455-36c6-b005-c015fca0256d | -11.94986 | -58.75907 | 2025-06-22 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ef7b7db-1545-3e81-b8a4-88940524935d | -12.0277 | -57.08833 | 2025-06-22 04:42:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02faf7b8-6775-39c4-921f-ffa19aae8917 | -9.99956 | -48.05881 | 2025-06-22 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eff7e3a2-5e95-3ebd-95b4-e000217a99a2 | -12.4767 | -54.427 | 2025-06-22 04:42:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7cbf1ff7-3fc1-303f-a67d-bc2c4f1dc79f | -9.32886 | -47.82307 | 2025-06-22 04:42:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb41dd5b-693c-3974-a110-1808f3d84df6 | -11.13508 | -53.9182 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 786d8e68-1d4d-3975-93e3-f32d05e7c269 | -11.11373 | -46.66714 | 2025-06-22 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77e6af93-10ff-31cf-9e74-e1c5910088de | -11.52891 | -56.97857 | 2025-06-22 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f6dd60b-40d5-35d9-9d3c-9c44069c563e | -10.86512 | -53.76951 | 2025-06-22 04:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
