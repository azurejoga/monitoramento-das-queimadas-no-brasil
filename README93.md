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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22ec8acd-c284-388c-bf4b-5054870120e3 | -7.37789 | -64.35979 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 75fd913b-39e3-3fb3-b0b8-77c758978fd6 | -9.09045 | -65.72234 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f72dec-a018-373b-b2b1-be5e3e5b1c9d | -9.18457 | -59.52509 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d92376fb-7cff-3cc9-b64d-27c6c6fa0c00 | -7.52828 | -63.37798 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9e8bd5b-e4d5-355c-bdc7-9862ccab93f8 | -7.3881 | -64.34908 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a246dc3-8d7d-3401-b03c-06c817fbaa03 | -8.98768 | -65.43069 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7589567f-a257-3293-a49e-cab3641686b9 | -9.08645 | -65.72177 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1704f58-1048-36f4-ac83-7e9316175cf7 | -9.15209 | -60.78611 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b6a1f59-db50-32e5-8e04-42f657f6323d | -9.08065 | -66.06221 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4523da8c-0e06-3cbc-8671-bde0a29214f8 | -8.88843 | -62.46932 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e34f14a-a933-3ece-a4e7-a6e5f32d588c | -9.64332 | -59.6424 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19f386f2-e09c-31f4-912d-940fb720e0e6 | -10.42171 | -64.38166 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2911da86-540b-3c0d-a31a-c4e422dabf98 | -7.38372 | -64.3611 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e310818d-ab88-3043-b40e-cc1b3a35be1c | -8.51492 | -63.87893 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bb3544a-5eec-3529-a606-dc30dcd0dc6b | -9.19958 | -59.51419 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecbcc806-3c17-3f0a-87b7-13a97e742200 | -14.29809 | -60.36666 | 2025-08-26 06:03:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7431a31-8440-37f7-8969-2e6a60d46f1e | -8.88732 | -62.44037 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21d09774-bd97-3b24-b03c-14290260e5f8 | -8.74334 | -63.74977 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3fc8d13-c5b7-3f4b-9147-0fdd74f1ec88 | -9.16518 | -60.77261 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1695fb55-318e-35e4-ad49-1234e7048327 | -9.02401 | -65.70211 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d254319-e50f-3485-a551-70c3e2ebeee2 | -9.13824 | -60.77857 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecc06f26-2e1d-39d8-8050-087c6cba6b38 | -9.0722 | -66.06264 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bee5cb05-493f-307a-9465-636051f7358a | -9.16288 | -59.54997 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4871597-d293-36c5-8090-9fc15f96ec40 | -7.88358 | -63.01519 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dcbe7baf-1b9b-3e8c-ab65-d5e1b99d9e1b | -9.01863 | -65.69893 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0949028-eef7-3710-a6b4-ba5f93720de4 | -8.86513 | -62.45454 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 959802a3-5719-3a10-98d1-1342d7b6b9b5 | -9.17244 | -59.52349 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8b31c33-31bf-3450-b0ac-edd52ed48c34 | -9.19118 | -60.79155 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9478af1f-d431-3687-824b-668a714462cf | -8.86092 | -62.44822 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ca3e948a-0b51-3d11-9d6e-5d3b2e23f313 | -8.98413 | -65.42649 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb7d3ce9-2ac3-35c3-ad16-c67269bbe58d | -8.85173 | -62.44118 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 387335d8-27e4-3c4a-8e30-843d806a27b7 | -9.64382 | -59.6384 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3e3257c-f3b1-3b1c-89eb-f96c0d16c0a7 | -9.17302 | -59.51895 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31d18cda-227f-312c-9bad-15f195d019c2 | -8.57938 | -62.63718 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50cd4b56-4e7c-324f-a80f-82f7c4afcd62 | -8.97143 | -65.42828 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff734027-7db9-3a8f-b342-bf619a683208 | -8.98058 | -65.42229 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4830e364-1d34-3af2-8b29-d58f8f6c8752 | -9.642 | -59.64086 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6da5323c-a833-33dd-a53b-06cbc6d8d609 | -7.6575 | -63.52105 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b512c3b-cf2f-315a-b3e9-bf2f6d758fd1 | -9.00502 | -65.39654 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6b11a5a-a1ed-37c2-be39-8d137bb27da0 | -9.19902 | -59.51872 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad8da638-42c8-3028-bebe-d2704495fcb2 | -8.55646 | -62.6229 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e4e7689-4ba1-3f75-b273-40e9dfd9cebc | -9.02835 | -65.72906 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 283bd2cf-04e6-3e92-800f-de9d94fbbda4 | -9.00658 | -65.71007 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b3358e4-8081-3646-b406-cb3cdc496d9b | -9.18945 | -59.53504 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5622cc55-2617-3ae5-8068-a9ee83688972 | -7.55585 | -63.85527 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9888bd5-da91-3b30-a5c1-48f44cbccdd7 | -9.06572 | -65.72415 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53b818a3-be86-394f-8d94-10df2f42805d | -9.25036 | -65.62146 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2cab14b-fa7b-3fef-9f3c-7c88fd298b66 | -9.1924 | -59.51225 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcaa0c23-407a-334c-b3ec-e80c62cf6239 | -9.16091 | -59.51718 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e8bed39-a2b9-3c7d-be14-b9e2fe5a3076 | -8.10786 | -62.87621 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3f97223b-36a1-357a-bb4b-c3627c47ce4e | -7.88429 | -63.01022 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0da27ae4-8776-3fcc-bc7f-5d40e837d64a | -8.34383 | -62.92963 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ddf02881-f1b8-3c15-aaaa-a1cdbd1f1688 | -9.00858 | -65.40075 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e68478c5-058c-3a54-b01f-caf65bc3c8d7 | -9.05283 | -67.4575 | 2025-08-26 06:03:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b148c59-039f-368c-850e-cb3d629fb167 | -9.81036 | -64.28442 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05231079-b4b3-326b-994b-75e203fad34a | -7.37637 | -64.35192 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 65d260ff-0663-3f5d-9f76-f4c7a2d28797 | -8.91083 | -60.71983 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ab69b98-cab1-3771-ba33-958811d2e8b3 | -9.17185 | -59.52807 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec2dc6f9-bb8b-38ed-9e66-2a7abf3caa40 | -8.66742 | -63.86372 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 839cf459-af75-34fe-a2b3-5c0c1f2e1c82 | -9.18463 | -60.79828 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 640ea2a2-1936-30fb-bc03-fae1eba4eb4c | -9.00399 | -65.40374 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa200593-1d5b-3db5-9acf-f726eb7d8fe2 | -9.01118 | -65.38265 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca84d35f-3e56-3b89-96c6-82a024a7650c | -10.41932 | -64.39925 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d7a02d7-d887-3770-a703-2eef77af8ef1 | -9.18067 | -59.45941 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c894e6e8-502e-3f74-97ba-61992d0ded7a | -8.84607 | -62.43983 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 02e02e26-4209-39fe-b591-5bbe3de0b4e7 | -9.17905 | -60.79743 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6294fc69-4e65-3319-827c-0fbf35c2ad0c | -8.98692 | -63.6432 | 2025-08-26 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d9fda68-7747-3161-a102-f28784523910 | -8.88003 | -62.45663 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 434eafe0-0fdf-3ca5-9e3d-29b4870c460e | -7.39068 | -64.36167 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e2bc243-ac29-3c64-9dd8-bd4970ff29c6 | -7.57129 | -63.43629 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed12bdce-9e31-30d2-a9c6-997cc1f44ac7 | -7.77224 | -70.06464 | 2025-08-26 06:03:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32feb8ba-2abc-37b7-a787-939406c75b42 | -8.86894 | -62.42627 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bfa18bfb-33f7-3c45-b0dc-246d2f527d44 | -9.16066 | -60.78108 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77dcd5d4-9b14-3532-8a0c-45fcd41e92d8 | -9.18673 | -59.61853 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f77b16d3-0a69-3b54-acfd-d59d782db019 | -9.0857 | -65.72689 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfa435e6-959b-332c-938e-b5107eddaa1a | -8.9824 | -60.49652 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bef30679-bdaf-38e8-a1fb-e54d7e55c25b | -8.87737 | -62.43898 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4293c65e-1382-3025-a990-cd20441fbd9a | -7.56147 | -63.84727 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03d40b5b-07ae-38df-91dd-50418d6edabd | -9.31375 | -63.43539 | 2025-08-26 06:03:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c5db73d4-f2b8-3c0c-89bc-7d6dbcc1f21b | -9.07611 | -66.06322 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 319c2d74-5575-3baa-961b-370accce2917 | -7.3849 | -64.35316 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d073d87-2848-3f4e-975a-903a4267c122 | -9.25233 | -60.92448 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 019a1bd7-7e13-39fd-b416-cd177dc67136 | -8.99024 | -65.41273 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7c9024ba-69b0-37cc-a665-f841b93a025b | -10.39533 | -57.69815 | 2025-08-26 06:03:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1714d58f-493e-3f1d-afa9-b185513c8f6f | -9.26289 | -59.78778 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ef07a69-8d8f-376e-81ee-a3f9b994861c | -9.16183 | -59.46151 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7395f626-016b-342f-ab1d-c7ff08241cb2 | -8.63479 | -62.65162 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a45acba4-ae7e-32b2-91b2-604a1802741a | -9.15742 | -59.54452 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d0f94310-8244-3dae-ae34-60ad5965dfab | -8.54369 | -62.64318 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 268ce7be-4590-3097-9642-cdb40b2ff7bd | -10.41309 | -64.41176 | 2025-08-26 06:03:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60b26e24-024d-3a2b-8dff-279c15be9085 | -8.86742 | -62.43758 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e1ea82-fcb7-3ef6-8f74-475333e6f282 | -9.08463 | -62.66996 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e512238-8463-3592-91a7-85a5311bde26 | -9.79621 | -64.25555 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef1601c4-6c72-392a-934b-a0f1ec9437d8 | -7.38798 | -64.36172 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63681aa7-74bf-31a2-9a77-6c013fdf0054 | -9.17518 | -59.45393 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71a7e7af-0675-3566-baa2-3fd66e250323 | -9.23687 | -60.91756 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 337db756-83ec-3d84-94fd-5de98d239590 | -9.26887 | -59.78857 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 069be3fe-b842-374e-9aec-bb367585f8e8 | -9.02237 | -65.39168 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9811a071-d529-3021-b8a2-683e9a657a8c | -9.26238 | -59.79174 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f47c16fa-a1de-3064-bf97-9e61f1ad4faf | -7.53285 | -63.37859 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README94.md)
