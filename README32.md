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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7828d3b-01d4-317e-b79e-9bbbcdc0b521 | -3.0384 | -59.9108 | 2025-08-06 12:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 96af2729-2042-313c-9474-6b15666286da | -8.9038 | -60.5962 | 2025-08-06 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 39af4151-09d5-3d49-a12e-3aa86993899d | -8.9041 | -60.5577 | 2025-08-06 12:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| c0080915-aade-340c-abc9-72545901ab80 | -6.2789 | -45.2716 | 2025-08-06 12:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| db2dcd50-6b8f-3c5a-9c40-992c1ce7b421 | -8.9039 | -60.5769 | 2025-08-06 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 323df30d-beaf-39fc-b1f1-191f22a02e2e | -8.9227 | -60.5568 | 2025-08-06 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 42f7a200-6338-3f6d-a9a4-3eb94ee71a92 | -8.9224 | -60.5953 | 2025-08-06 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 103a0ece-11e7-33c2-8d8e-8bc944d15e42 | -8.9038 | -60.5962 | 2025-08-06 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 6604a055-35ab-3d48-a088-7b8a72f10798 | -6.2792 | -45.249 | 2025-08-06 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 6bfe298d-c1a5-3ca9-aff7-4b418cecabdd | -8.9225 | -60.576 | 2025-08-06 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 7ea6c187-bb01-3dcb-88d4-ff78b5a2d380 | -6.2789 | -45.2716 | 2025-08-06 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 8772b0d2-5b90-30a7-b8c0-b3c133172923 | -8.9041 | -60.5577 | 2025-08-06 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 79d2c0fe-826e-386f-87c1-aa78d16a8f66 | -8.9227 | -60.5568 | 2025-08-06 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 63d192d5-9cb2-3d4d-8d9a-362b432c7c93 | -8.9225 | -60.576 | 2025-08-06 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e9d40d31-cf1f-3980-a690-603552bdda7d | -8.9039 | -60.5769 | 2025-08-06 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 947d6bb9-971d-34ad-a6ad-16e5b731e06e | -8.9224 | -60.5953 | 2025-08-06 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 5cc2cdd1-e3ed-378f-99e1-80e6fd3fb013 | -8.9041 | -60.5577 | 2025-08-06 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 947ba481-ad1b-3eec-9edc-3f54394997d8 | -6.2792 | -45.249 | 2025-08-06 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| ac919650-d107-3a13-932c-0e95c1d1a5c5 | -6.914 | -43.6816 | 2025-08-06 12:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 0f5c8f43-e6b9-3bc0-97c6-335e156f224f | -6.2789 | -45.2716 | 2025-08-06 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 248.6 |
| dc92bac5-6b88-3811-90c3-dfb651ea035c | -8.9038 | -60.5962 | 2025-08-06 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 1f6200df-e50b-368d-94ad-9a0edd2fcee0 | -3.17844 | -49.45167 | 2025-08-06 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 879d84c9-fbb4-38d3-959a-65373f05d8d9 | -6.2602 | -45.2731 | 2025-08-06 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| c0a59649-9608-39d0-bfcc-77e89404add0 | -8.9224 | -60.5953 | 2025-08-06 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| b3e76422-2d69-3281-9790-1559489d36eb | -6.2792 | -45.249 | 2025-08-06 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.6 |
| f7c5d247-622e-31ce-8959-63bd7b86dc14 | -8.9227 | -60.5568 | 2025-08-06 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| c4ac43cc-a772-39e8-9c2d-7d5a68df5f01 | -6.5007 | -45.5705 | 2025-08-06 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e4e800c9-ef29-3428-9848-ffb2170b93f0 | -8.9038 | -60.5962 | 2025-08-06 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 2b334fd8-ffd8-3abe-9359-26aaf9bedda7 | -8.9041 | -60.5577 | 2025-08-06 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 4d2dfd1c-6c2f-3296-a73c-e334e2183823 | -6.2789 | -45.2716 | 2025-08-06 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 48583d7f-9c00-3a18-b0fa-36f755d4a7c3 | -8.9225 | -60.576 | 2025-08-06 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| fe3df60e-dd0f-3822-8f3e-c9c4e907ed9a | -8.9039 | -60.5769 | 2025-08-06 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b262e154-84a1-3140-93c0-6fcf6ca93321 | -5.99492 | -52.283 | 2025-08-06 12:51:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b64a8c96-60d2-3065-a8a6-ca6da697b13f | -8.83937 | -47.6063 | 2025-08-06 12:51:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 7cb92d20-b109-3cdc-9a55-8a42694e7c01 | -8.53313 | -47.47238 | 2025-08-06 12:51:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 4dfb77f4-d304-3e28-a3e8-c72061a60571 | -8.92353 | -60.72952 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 36ff537d-5dd7-3473-96eb-7d1dc8e150e2 | -6.95088 | -50.45232 | 2025-08-06 12:51:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b0798ce3-73b2-3148-b9a8-c4f2a38b595d | -6.27326 | -45.26285 | 2025-08-06 12:51:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 300.0 |
| f5c3eb67-97fd-38b1-ad7d-1d7bd6324a58 | -6.50715 | -45.57217 | 2025-08-06 12:51:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e52bac5b-c4fc-3b4a-84a8-827d1727d38c | -9.47168 | -57.8485 | 2025-08-06 12:51:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| bb5453b2-17a2-348e-814e-d1da8d8eaa2d | -10.79787 | -46.5055 | 2025-08-06 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fd6b5e8d-2df4-36d2-a8f3-f0811ecece20 | -8.91014 | -60.54539 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| d44a77c5-62ba-39a4-ae6d-adf5ed497ea6 | -8.84424 | -47.62416 | 2025-08-06 12:51:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 7c7f2bc1-3135-324a-8994-54bc2fc28304 | -6.41319 | -53.36917 | 2025-08-06 12:51:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 00a1bc63-c9dc-3877-ae91-3a6e65bd94a1 | -8.83045 | -47.62236 | 2025-08-06 12:51:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5a30c501-52b9-3283-a0c6-17a79c6c10ce | -7.50434 | -47.17408 | 2025-08-06 12:51:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 1a961098-b183-3384-b4df-3a5ba4a05715 | -8.53095 | -47.44075 | 2025-08-06 12:51:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| e3c2e587-421f-34d8-8aa6-4532d8b3575a | -8.91892 | -60.72275 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6b802c5a-a2ec-3b36-8d5b-6b3aec072ee2 | -4.02647 | -48.06962 | 2025-08-06 12:51:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 54955aad-93a6-348e-bb9f-7e5d6cd0f527 | -10.29649 | -56.45096 | 2025-08-06 12:51:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6503eb50-a89f-34ad-8023-3e98add27413 | -8.92064 | -60.74708 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| a490ca07-1eea-31b3-a29b-b8abb2614e21 | -2.98366 | -54.50473 | 2025-08-06 12:51:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a70e5b3f-73ac-3e9a-b250-d56555394150 | -8.91934 | -60.56421 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 791166df-a57a-3d99-ba22-bd99a2ded2fa | -8.90744 | -60.56236 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 1d6b0482-e04d-3979-94d1-bbcd55d1da57 | -7.98019 | -55.3088 | 2025-08-06 12:51:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| be633029-ca85-3739-8ea5-4ad4f11e5510 | -8.41068 | -47.445 | 2025-08-06 12:51:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8cadfa98-8cb2-3627-b15a-3f9d9b348db4 | -8.91665 | -60.5812 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 3d8476d5-4248-3505-b325-9487a0563a36 | -8.91617 | -60.74031 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| bfd62b01-f11b-3513-a054-e84f5b56c104 | -9.46204 | -57.847 | 2025-08-06 12:51:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d72871e0-0798-36e3-a44e-4b31b8507272 | -8.83658 | -47.62989 | 2025-08-06 12:51:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 2293d328-6389-31d4-baee-03d1aeff54a8 | -8.90204 | -60.59623 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| e6e1072d-a605-39eb-969b-502825ba3350 | -8.91398 | -60.59809 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| c25ecbdd-018e-3d89-87c4-66b40c3dc61e | -8.92203 | -60.54725 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a8358254-eaf7-3d56-97dc-96b10c6feba2 | -8.90473 | -60.57933 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a0e7e726-e10b-3a29-95e1-197387615a72 | -10.6052 | -52.84147 | 2025-08-06 12:51:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| f5db6d66-13fb-336e-b684-2fce6a3aa4ef | -8.53607 | -47.44833 | 2025-08-06 12:51:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 21af264f-ba19-3a6f-b5d9-1fb52c897384 | -8.91343 | -60.75784 | 2025-08-06 12:51:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d3c49b3b-0ae7-32cc-ad33-0b94e7fef325 | -10.80234 | -46.49994 | 2025-08-06 12:51:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 7bcf932d-0323-3e7e-ad35-b40bbd4a26da | -13.2533 | -47.00354 | 2025-08-06 12:53:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 42.5 |
| be34c4cf-9a63-31d2-86ba-670f3e41e3e7 | -12.53985 | -47.15929 | 2025-08-06 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2332d1e4-7f82-3957-93d3-108c2e629b02 | -11.64505 | -50.1482 | 2025-08-06 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8c0db038-9177-3c66-976e-75e0e86f3b28 | -13.07053 | -56.85982 | 2025-08-06 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d07772ac-7ed8-31e4-b7d8-12167e6842e4 | -12.54217 | -47.15218 | 2025-08-06 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 2cea69b3-116d-3d11-a696-b6e1b27cbc1d | -13.50381 | -47.73898 | 2025-08-06 12:53:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 59bd436e-b977-37f0-b31e-1b07732806f9 | -11.62864 | -47.72067 | 2025-08-06 12:53:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5d98677b-6178-36bb-8042-c44a16ced02c | -13.07945 | -56.86118 | 2025-08-06 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 4dc2c641-52fd-3431-94d7-86d5fcae86ab | -13.06161 | -56.85847 | 2025-08-06 12:53:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 9b031731-4b8c-33d2-a971-aa9f754c3f41 | -11.48634 | -50.30453 | 2025-08-06 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| a0a2076d-b591-3562-861f-39cbc49e41e7 | -11.48834 | -50.28848 | 2025-08-06 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| fc54a509-f637-3f79-af56-673d9ce85a92 | -11.18874 | -51.45472 | 2025-08-06 12:53:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b916de69-786c-3c21-9250-91620ada8b23 | -11.60152 | -50.20971 | 2025-08-06 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 421f0885-7a9d-323f-aad1-63684fe0caf7 | -13.73957 | -53.87992 | 2025-08-06 12:53:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 54b2de10-9258-3977-a6ab-6239b6a12bed | -11.65199 | -50.15548 | 2025-08-06 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f312bf2a-23d6-39a5-bb2f-d550d364c0e6 | -10.37432 | -57.6601 | 2025-08-06 12:53:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 36870921-413f-3db4-b079-b3a0c07cbd44 | -11.77108 | -47.53073 | 2025-08-06 12:53:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 0bc3a281-d289-312e-91cd-06a6ec11330c | -16.34852 | -50.35467 | 2025-08-06 12:53:00 | TERRA_M-T | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 1243364f-d403-3677-b356-18c31ff11f9f | -10.37587 | -57.64985 | 2025-08-06 12:53:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| f2a3eba8-b3b9-3d09-863a-e26d76c14203 | -11.72748 | -47.52503 | 2025-08-06 12:53:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| a91187ae-0436-3f83-99d2-5f8cf005694c | -6.2789 | -45.2716 | 2025-08-06 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 39ba205f-8850-3057-ab3c-e025428390f0 | -6.2602 | -45.2731 | 2025-08-06 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7a408918-7c7a-3279-9242-1b7771083085 | -13.0728 | -56.8729 | 2025-08-06 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 926c81ae-23c3-3b29-be8e-9b75f3f071a4 | -13.0731 | -56.8527 | 2025-08-06 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 18c4cebd-3a42-3d6b-9863-f6284c8fb29d | -13.2472 | -46.9905 | 2025-08-06 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.4 |
| e6f734eb-8b4f-3aae-8bbf-c7ee41378463 | -6.2792 | -45.249 | 2025-08-06 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| d0bdedf1-8140-3c9c-b1be-5f0e9cf53c02 | -6.2789 | -45.2716 | 2025-08-06 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 216.5 |
| a08d6dd0-1305-3288-896f-610d98f28b58 | -6.2602 | -45.2731 | 2025-08-06 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 188ae0dd-bc28-384a-a56d-2ffa6a48441d | -6.914 | -43.6816 | 2025-08-06 13:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 15b842f4-8109-3301-8390-2dac19168c63 | -13.0731 | -56.8527 | 2025-08-06 13:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 0c636383-5d45-33e7-8636-d8b247fdcf49 | -6.2792 | -45.249 | 2025-08-06 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 08ff9acc-fd40-355b-a059-b2d5875b10c4 | -13.0728 | -56.8729 | 2025-08-06 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |


[Clique aqui para ver as próximas entradas](README33.md)
