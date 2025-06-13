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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12213df1-d8e1-3acf-842b-de02e4eaa636 | -10.23918 | -52.2345 | 2025-06-13 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0cf08f02-e9d8-33d2-8533-f3cb31cba86f | -11.37454 | -55.112 | 2025-06-13 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07c09633-dd03-374c-9bfb-b8ac96b3de62 | -10.69773 | -49.49539 | 2025-06-13 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 963a8c4b-b0c3-372e-b4d1-a1e85233fc89 | -11.98754 | -57.19656 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9201b9a8-5b33-3177-bae2-d391ca54b126 | -9.40296 | -48.42725 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b1bb5e5-6021-31f9-b6d0-328f814d7df1 | -9.66885 | -48.7637 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1e6bde5-1cde-3788-bb21-560ca380b23f | -9.19207 | -61.84898 | 2025-06-13 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96217cd3-c958-33cb-aff3-5d3c442f4aee | -11.56299 | -54.56865 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 32e12e43-f878-3eea-9d46-a73ae1d4b72d | -9.67336 | -48.76603 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0dfd712d-3351-3f1f-b1c1-b42d0515ffd8 | -7.92454 | -61.55579 | 2025-06-13 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 458b7c12-727d-33bd-a7ed-9bbebf9e78e9 | -9.87897 | -61.39951 | 2025-06-13 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 564d7130-c479-3ea1-94f9-31be804bbac9 | -11.80752 | -56.96672 | 2025-06-13 05:23:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bfafa10-9631-3164-9c9e-ca574f07dc90 | -10.23341 | -52.23709 | 2025-06-13 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3aecfe91-8124-3222-9672-77d96121eb4a | -10.27749 | -60.53668 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dc6992c-c949-37d7-a813-649dc88e185d | -9.67266 | -48.77198 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 533c63e8-8087-3c5c-b6df-4471ff37cf05 | -10.63954 | -49.42344 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9a407fa7-defd-32be-b715-1ba8e4539887 | -10.27531 | -60.5509 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff355c1e-8f60-358c-814e-6f4577393f9b | -9.6847 | -56.9914 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b4512e6-0adb-34d5-aa55-004c734815da | -12.20225 | -54.26874 | 2025-06-13 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fa576a5-f50f-35d3-ae50-99fe737d22ae | -10.65437 | -49.41859 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8aebf8b4-c11a-3aa1-a3f5-6c173dc37220 | -11.81964 | -54.50503 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60f5e6b6-9ddd-3f87-a26d-cb5f84769408 | -11.74919 | -54.71701 | 2025-06-13 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7292243-2097-3629-90f3-a3c960a07bb9 | -10.93212 | -56.83785 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| bd812251-1d1d-372b-88b0-b0daba32da27 | -11.87757 | -52.29942 | 2025-06-13 05:23:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1c5da97-b5f1-3cf6-9127-6f10e6dcfdf5 | -10.9242 | -56.83669 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ed59f37c-2d97-3677-b749-b817f7811d87 | -11.74457 | -54.71636 | 2025-06-13 05:23:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2201ae7d-e360-35a0-9c10-21500d85f9c6 | -11.76954 | -54.37348 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dd11c62-74d9-3699-9819-20e170269552 | -11.91718 | -57.47197 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ee182ab-ac91-316b-bfa6-0971cce4a5c1 | -11.36656 | -56.55497 | 2025-06-13 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b88569-eef2-3f75-8c51-054bb583bb09 | -12.12861 | -54.66676 | 2025-06-13 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 957cfa8e-b89a-3f93-8f8b-f291c39d8d0d | -10.917 | -56.83036 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2130c41f-c40d-3071-8cb4-0f8813180a01 | -10.6473 | -49.42323 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2008de3d-3755-3252-a6d6-c0dfb047c170 | -7.84518 | -63.89328 | 2025-06-13 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9f70e9c-bb02-363f-83ae-4cfae01f28ba | -10.93608 | -56.83842 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 588bf069-4867-33e7-8015-afe64a9e76da | -10.92024 | -56.8361 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 95ff9171-828e-3375-9aff-dc2c84ce3bcc | -11.64708 | -58.0139 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4dd1d0d-e2e7-3b0e-9c5e-a0cd8cd9e1a3 | -10.8686 | -54.30713 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 317a4942-1fb5-3e3e-b832-2c3ffe811a17 | -10.29949 | -57.13807 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa821c45-8774-32ee-a021-924b4dcd1e45 | -9.96381 | -64.97643 | 2025-06-13 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c20ae38e-9fa0-3407-91ad-0419cd048601 | -9.40067 | -48.42423 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8bdfdf8d-09c6-3ea6-b74f-27de549aa4dc | -12.13327 | -54.66743 | 2025-06-13 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ad0c324-dfe5-345d-991a-99d74bd85cb5 | -10.65373 | -49.42421 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 028d2dd6-46d0-341f-b4ce-c5ead03e2ffd | -10.8639 | -54.3065 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9459504b-f410-32ff-ad07-8186384848d1 | -10.80683 | -55.87197 | 2025-06-13 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25e16aeb-54da-3f64-81bf-d00b4db304da | -10.36806 | -57.22337 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68468949-0013-3d6e-aaea-75c094678852 | -10.29686 | -57.14413 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b129fdd-dcd4-3a68-b5b9-1b5519c7a1ec | -10.63961 | -49.43328 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 205e8e05-85ce-3068-b047-39d24eef8a84 | -12.28767 | -50.10958 | 2025-06-13 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d4816dde-1848-3433-b766-f126ae08f75c | -11.13063 | -54.21831 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 884ac257-242f-3589-a88d-ff96e2769e60 | -10.64023 | -49.42779 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 35aaa7fc-a7d7-37cc-86d5-15a91d02d5d3 | -11.56765 | -54.56932 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5f33d60a-f704-3f1b-be8c-b6e16a32b4d8 | -9.40664 | -48.43123 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3a5b53ab-248f-3925-8a34-f0abbdff3ef5 | -11.13089 | -53.95005 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b4e8d83-505f-3aa6-b66b-e18ce6a059b3 | -12.40929 | -54.178 | 2025-06-13 05:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b63bcf03-b935-3809-8291-374299406b18 | -10.65307 | -49.41984 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 341aa228-6b43-354a-a022-838a5700987c | -7.86073 | -61.50582 | 2025-06-13 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d265e31f-ba25-37ef-b8a5-5d2536d3943c | -11.80355 | -56.96613 | 2025-06-13 05:23:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dea76a7-1c03-32d6-9e20-33ede577ab9d | -12.29398 | -50.1104 | 2025-06-13 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc639cd1-aee1-3fb0-ab53-32a365fd670a | -9.39394 | -48.42324 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57feba17-0584-3997-b54f-170358d79612 | -10.36596 | -57.23787 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b449b79-fdb3-3cd7-b04c-590c8f3df634 | -11.37901 | -55.1126 | 2025-06-13 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6f48c3d-d148-3fc1-9b9e-e3931bfc67ee | -10.92168 | -56.82574 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 781ad25f-cdba-30f8-8206-89cd2fb4ef83 | -10.27362 | -60.5397 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4629e6c-12bd-3535-8f0a-6406fd6dbfd4 | -11.5723 | -54.56997 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8890e9b-cb96-3d13-89bc-38c6fffba5fd | -11.81026 | -54.50369 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d4480fd-b8e6-34eb-a498-7bee2e38dc8c | -9.4097 | -48.42815 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9a4dbcfd-19a0-3e62-9765-0ca684f5377a | -12.28407 | -50.10972 | 2025-06-13 05:23:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7d4db5d-05ad-3520-bddf-e03e6c08fb6a | -10.84497 | -53.77553 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31450dc7-ac3e-3f0e-9048-1ef6bc740f81 | -10.36735 | -57.22824 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 00a4770e-80c7-33fa-9c82-35957a7760ae | -10.27695 | -60.54023 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14ef76ca-33de-3195-814d-b6224f737a2c | -11.92104 | -57.47251 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17210863-8b53-379e-8bde-b728f6dd7011 | -9.24976 | -57.53694 | 2025-06-13 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 703c5a00-ecf9-3a3e-948f-da24bb97ee54 | -9.39624 | -48.42617 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84169caf-7696-3bdc-9d3c-60b5de9fb278 | -9.41042 | -48.42203 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f4080374-5467-3440-b58f-f0a7b8a8b5dc | -11.37962 | -55.10806 | 2025-06-13 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e378016-fa96-3a8d-9fe3-278a13f58d2b | -10.36667 | -57.50124 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a244b43c-e858-3922-8054-c994156a0bd9 | -10.60229 | -52.82932 | 2025-06-13 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92a010fe-431c-3701-9437-c53a93adf6a0 | -11.914 | -57.46647 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 466ca6eb-6471-3aac-bf41-6b8e16296a1b | -9.41415 | -48.42595 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1f7fcc7-44a1-3c9e-ba48-67b97656ae6e | -9.22239 | -62.47196 | 2025-06-13 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 95914f55-6b11-36d8-a781-ceb470f3cdd6 | -10.63887 | -49.42902 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b46e82fb-7d55-3f90-8981-6a7a72110519 | -10.93285 | -56.83266 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a4a0af13-3dcd-3c8b-97bb-7879a3b5a7ba | -10.91953 | -56.84121 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6820354e-dd79-3377-beb0-6ae76390b874 | -10.79206 | -56.29113 | 2025-06-13 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d0a9640-e0bc-33bd-adea-1e033fa1f686 | -11.13408 | -54.21794 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0165019d-4265-30dc-8480-b76aca812324 | -9.96307 | -64.98079 | 2025-06-13 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3126d2f8-54b9-3b8f-bb60-ad34fcc971c4 | -10.1873 | -49.50018 | 2025-06-13 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cde0064-4454-3e3d-a453-a07466a4ed8d | -11.12606 | -53.94941 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5a628e4b-c591-36c1-a99b-73b0e7f8dd9c | -9.40387 | -57.55066 | 2025-06-13 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 98cb2f63-7f8f-3aac-8e0f-5ec0197e0790 | -10.29878 | -57.14293 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f05d3b7-3c8e-365b-aa50-481ee70e37f6 | -11.92173 | -57.46757 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79af567b-059a-363d-8cb0-daf315a21c00 | -10.37049 | -57.23366 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6235c4a-30f4-3315-bb90-6f9280d15179 | -11.78765 | -54.78138 | 2025-06-13 05:23:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4b2436f-304c-3228-94e0-24dab9d8b6c9 | -10.84191 | -53.77449 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f28232c-7412-3dfb-a85f-de5183017ff6 | -9.88227 | -61.40004 | 2025-06-13 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef1f3cde-e52b-36b8-89ff-8c8462ac5ddc | -9.25042 | -57.53249 | 2025-06-13 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4bdcb2a-54f2-3177-a3f1-15b84e727aac | -11.12535 | -53.95485 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68cd7db6-2c66-34ae-ae99-fec59e2f3401 | -10.65309 | -49.42982 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9e6d53c-afc2-33be-a3d5-a19e1db14ad1 | -10.0561 | -59.35912 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aee304d-6b14-3c7e-ad2f-044b7f924aa9 | -10.36666 | -57.23307 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README20.md)
