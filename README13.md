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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 942ecd3d-691e-3e66-b21d-9315548a553c | -10.50235 | -58.86106 | 2025-05-20 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6fbf330c-e00b-3155-bfba-de406d748606 | -8.74655 | -49.74819 | 2025-05-20 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f18b333a-e702-328a-9e57-ee85bc646de0 | -12.12605 | -54.66353 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a506f85-76f9-3fe7-8747-4e0d646e955e | -11.08818 | -54.77452 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1715fd0-2d36-3eac-a4fc-cc0410ea03b7 | -12.1267 | -54.65861 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1585dcce-f198-3ee0-be18-3673e8626b34 | -12.29399 | -52.47322 | 2025-05-20 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c0ad5f90-c849-3629-aba6-a78b05ff76dc | -6.95914 | -55.28156 | 2025-05-20 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba248a0f-12b1-315f-a5c4-1d503ff7220c | -9.03032 | -48.94236 | 2025-05-20 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7322408-a441-35d2-9144-f56a42464c10 | -9.03677 | -48.94341 | 2025-05-20 05:23:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12ce91a5-e67b-3628-aee2-cfc1c8261e75 | -11.66453 | -54.93883 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cb80f6e-ba9b-3d75-a6ec-48cd7f5a294b | -10.3102 | -59.56644 | 2025-05-20 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 912ec97c-e805-3042-ade7-cf816635c314 | -10.36373 | -47.97755 | 2025-05-20 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75a6984a-9893-3062-a181-fbf14c19bb5b | -10.76337 | -57.23011 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78fe5a80-8bd2-3992-8feb-a1e900406cac | -11.82208 | -57.81701 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1959d306-89f8-3e8c-a44b-48d39d879fc0 | -9.65565 | -67.2392 | 2025-05-20 05:23:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 393557fe-6456-3627-9b14-c3823a28390c | -12.13532 | -54.66484 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8966e8f1-f62d-303c-8c7f-1fb1ae68c9fd | -16.23034 | -59.64832 | 2025-05-20 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af78e18e-9f39-38be-81e4-34c72f6ee36b | -10.36445 | -47.9713 | 2025-05-20 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4671f56e-5ace-3c57-b5b3-912224b26f53 | -12.27396 | -57.26439 | 2025-05-20 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4c92bfb-0c28-3a5c-ad88-b61bc832768b | -11.88451 | -56.41724 | 2025-05-20 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9004e1ad-fb6a-3d7b-9377-b127ba63c2c7 | -10.50159 | -58.86158 | 2025-05-20 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db5f901a-1675-3569-bd96-95ca6d467799 | -11.08529 | -54.77225 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95a88208-0ee6-3122-a23d-b84449aa07d1 | -12.29356 | -52.47668 | 2025-05-20 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8cc8da8-96dd-30a1-992c-5c50f278cbeb | -8.16755 | -61.47641 | 2025-05-20 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93ad3a39-4494-3755-af7f-a98c77c1256e | -10.27254 | -59.5381 | 2025-05-20 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74726a01-3349-3b8e-a5d5-dd730fd2a8d1 | -11.23401 | -49.4912 | 2025-05-20 05:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26d5e706-76a7-3fed-95de-daf1ce54406e | -12.29937 | -52.47393 | 2025-05-20 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 732d4bb7-68d6-3f37-b73a-c7da57455010 | -12.27786 | -57.26496 | 2025-05-20 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ec4e2c8-415a-3b70-ad68-9f78b1830dc8 | -16.22971 | -59.65261 | 2025-05-20 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b38ccc3-df25-3171-a611-2f1ee211839c | -10.35681 | -47.97631 | 2025-05-20 05:23:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d036ebaa-0afe-323c-a201-e58611ce2e8a | -11.08016 | -54.77623 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51522c3f-1959-34a2-8517-241f726df5f3 | -11.36306 | -55.11908 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14de500f-1443-3eb1-93db-6f70b3fd84dc | -10.68503 | -57.59253 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de119186-71aa-3207-ad74-b2926f850193 | -10.76654 | -54.78085 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72077e86-6d4a-333a-82ab-73a017432a59 | -10.82613 | -56.95436 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a331b39-7edd-31bc-978e-3bd6de452f9a | -11.2955 | -53.97734 | 2025-05-20 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3356400-2052-3593-bfee-99a4f6b08b0c | -11.34096 | -57.67427 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9bed01-f3b6-3c93-b4ba-715489b035f5 | -9.2465 | -63.28683 | 2025-05-20 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b4fb66c-a168-3545-ad53-d2933b4fb7db | -11.23337 | -49.49644 | 2025-05-20 05:23:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72a039a7-f567-375d-9a2a-f63be2d8cced | -11.07913 | -54.77316 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6614bc92-db46-3bcb-adc6-89f8a0af674a | -16.40026 | -58.16746 | 2025-05-20 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6b284dca-5b4d-3730-a776-40ff56bd6d84 | -12.02864 | -57.10323 | 2025-05-20 05:23:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25f1538f-c4a6-31dd-b767-1158a8450f11 | -12.13134 | -54.65926 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8019d68b-0f6b-3dd8-9ed6-33e8e63795b7 | -8.7521 | -49.75367 | 2025-05-20 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2cc221bf-8597-31cd-bf89-2befbe203633 | -11.08366 | -54.77384 | 2025-05-20 05:23:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50010ce7-7c7a-3a65-9358-da883c753e74 | -11.56994 | -54.56289 | 2025-05-20 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0a231def-d4c7-3a12-a28e-3d93bc4383fc | -19.06306 | -53.46006 | 2025-05-20 05:23:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a97badd7-cf11-3b89-b2b3-e26aecf73841 | -11.35035 | -55.11279 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 457d70d1-ac58-38fc-bda2-fc1bd1fa9a7a | -12.2886 | -52.47247 | 2025-05-20 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4c84c34f-9caf-316f-aeec-fd7afce42a3f | -9.41443 | -58.32953 | 2025-05-20 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 334c4fa0-777c-3dfd-a9ee-7da9ca168c53 | -7.31296 | -46.9687 | 2025-05-20 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66b12ef1-80e2-328f-be0c-90a7ac8dbcda | -10.81763 | -56.95811 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 279157e1-3b97-3f08-8f22-99d071e5a3e7 | -10.76021 | -57.22472 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e17e8c01-3b1b-3b78-a15c-a9c7a6f13762 | -9.35887 | -57.54088 | 2025-05-20 05:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ccfd873a-ec11-35db-a9fa-6a197470b85f | -11.66843 | -54.94397 | 2025-05-20 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0594066d-b744-3ec1-b908-2468f4d94eac | -10.75953 | -57.22954 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa20da3d-9be0-3f13-9b9a-664d2d3a7143 | -9.92984 | -59.92925 | 2025-05-20 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e95a0f07-9f17-38e4-a751-3f85cdda604a | -8.74647 | -49.74754 | 2025-05-20 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30550b37-4f43-35d3-b5ea-6f1c554830f3 | -19.11023 | -52.68819 | 2025-05-20 05:23:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fae0faa-246a-3619-afa1-315f6f2d953a | -7.92708 | -61.55666 | 2025-05-20 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5fac570-cb43-354d-af7b-ea32e79aa50a | -9.24244 | -63.29005 | 2025-05-20 05:23:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b27f8d5-4a4b-3f4b-82e5-9416445f8a16 | -11.29503 | -53.97755 | 2025-05-20 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8e7ba3a-fff2-3431-9373-72ee6235e3af | -10.67033 | -57.63432 | 2025-05-20 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ea3bbbc-517f-33c2-a8eb-0b3256e8287a | -19.10981 | -52.69228 | 2025-05-20 05:23:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c86b9f99-074b-3924-9f57-79ded648f627 | -12.13068 | -54.66421 | 2025-05-20 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10e993a6-d05c-302c-8d83-2f8a91e1be48 | -20.95259 | -56.6111 | 2025-05-20 05:25:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d480c1ec-05cc-3e2c-a90e-579a4e7e9f1d | -20.94858 | -56.60533 | 2025-05-20 05:25:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c47c724-eaa0-33ce-a1c5-bcac866e386f | -12.83693 | -62.01666 | 2025-05-20 05:25:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6891bc69-2458-3137-bcbd-34f384eb8818 | -13.04884 | -53.71875 | 2025-05-20 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd429d66-fc03-3695-b974-599076bbbafb | -14.03279 | -55.13699 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a449306-7a48-3278-98fb-7223df988abc | -13.09042 | -52.28351 | 2025-05-20 05:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f26acb8e-d59c-3d49-9003-5f51818f767d | -13.04356 | -53.71912 | 2025-05-20 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35baba16-7ce4-3b6c-a764-0ef415e33179 | -14.03319 | -55.12963 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f67ef72-4bfe-3aca-b858-0c13e2549c70 | -13.66367 | -53.93231 | 2025-05-20 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14b0a199-aa14-3119-976d-0145cb3505a0 | -14.02294 | -55.14062 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 043068ab-b99a-3512-bc80-7b2d8915165e | -14.0338 | -55.12468 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 370cab31-73f7-3d07-8d8b-c8e3b5852d70 | -20.21994 | -50.75505 | 2025-05-20 05:25:00 | NOAA-20 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7914f9e0-1cf8-3150-a939-da8792ec3089 | -12.83361 | -62.01612 | 2025-05-20 05:25:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af5a8199-c9eb-36e3-b5d9-2ffcc93af956 | -12.46887 | -57.18593 | 2025-05-20 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dffb2fc5-f19e-3447-a900-8a7d967f877c | -20.95317 | -56.606 | 2025-05-20 05:25:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67e685f1-5606-3480-a236-88f50800159b | -14.03473 | -55.1222 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2c1bb711-b179-3713-8c67-d46340d12e79 | -20.95374 | -56.6009 | 2025-05-20 05:25:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae27c9d7-c054-3d00-a553-1059cf622b23 | -13.04307 | -53.72406 | 2025-05-20 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 666c1751-b4bd-3510-98a0-b1828a02b841 | -11.97455 | -63.52991 | 2025-05-20 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c7531ec-cc01-3665-8e27-dc5190315cfc | -14.02486 | -55.12586 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ee187ce-c9b1-38bd-96c9-7197a174599f | -14.03011 | -55.12159 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be2349a8-df15-3153-a457-d50c6a6f845c | -14.03441 | -55.11973 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c642e6a-fd95-35d6-8831-26bdab21291c | -13.04382 | -53.71819 | 2025-05-20 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18facbfd-a742-3434-8d60-eb9055833f18 | -14.01897 | -55.13505 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f431444d-a6c1-3d89-be36-528bc5de986e | -20.18233 | -55.0072 | 2025-05-20 05:25:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 369bea9e-38d5-3d4e-b281-e0f383315f76 | -13.04858 | -53.71969 | 2025-05-20 05:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77280f7b-199c-3266-82b6-0793e2d41374 | -12.685 | -58.13026 | 2025-05-20 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ed7021d-1dbb-3549-84ad-e8adf80c12fd | -14.02754 | -55.14126 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3714fe3e-0e37-3d59-921a-322fd6c0013a | -14.03408 | -55.12713 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b7b4a6b-ec6e-338f-bcee-a049a6de2ec9 | -13.09594 | -52.28421 | 2025-05-20 05:25:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 96b7702d-f499-3683-9f43-352054db0552 | -14.01834 | -55.13997 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a40db193-274d-3e11-bdea-eedab18e44df | -13.48663 | -60.3784 | 2025-05-20 05:25:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56adf13f-5c3a-386f-8958-009a39eeca5f | -20.18266 | -55.00404 | 2025-05-20 05:25:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a02e7564-db0a-391b-b361-73ad81c0a438 | -14.03344 | -55.13206 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36de0dbe-8f5b-3a52-8094-d9a8962af25a | -13.61384 | -55.45684 | 2025-05-20 05:25:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README14.md)
