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
| 1f4cb242-8424-3cf2-8536-e49b67fde698 | -10.08068 | -52.74946 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92a3b9db-8964-3097-a8dd-46fee747cd97 | -10.87737 | -56.43688 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d2b3f01-e9a0-3972-9115-433f5c4fce0c | -10.08128 | -52.74437 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 347bb9ea-b5bf-3e51-b3ad-bc8156cc5ecf | -10.12829 | -52.34707 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 110469df-442c-35dc-8cee-bbb47ca70d51 | -10.02699 | -54.31963 | 2025-07-01 05:36:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8bdc4c9-6326-316e-b53b-3cac239b15a9 | -9.23632 | -58.74181 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 506e6abc-4209-342e-bd16-85f55885a74e | -10.87472 | -53.76493 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c98c7d35-4969-3bdd-8a71-92ecdf98e086 | -9.70705 | -56.18557 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 846fcf86-e313-368e-9f02-f55d42303a8d | -10.08824 | -52.74007 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87a6e03a-87b5-3f61-b93b-d7a5e059c750 | -9.24363 | -58.75083 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a443808c-fbca-3b5e-b781-be43aad470c0 | -9.71249 | -56.18334 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 966e0c21-850c-3041-8a5c-53b896a86a2d | -10.29678 | -57.13598 | 2025-07-01 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 575ec191-da80-362e-be68-b51a0e96bf7a | -9.70163 | -56.18773 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0082fe60-6144-321a-abf2-a8c8d4c8578d | -9.65636 | -50.74661 | 2025-07-01 05:36:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0eda21cb-7b43-3043-b961-ebb283ce0aa9 | -10.12844 | -52.34247 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| deb2bf37-f36a-3265-bbe7-cf82610362e4 | -10.87582 | -53.75598 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17d4cff8-447f-37c5-b448-cce32d07a5c2 | -10.88588 | -56.45012 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f62ceb36-84d5-3254-9d2e-c1b8882ffb3a | -10.8758 | -56.44871 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2c83d1db-b27d-352c-a5f9-2898a8d6020d | -9.24108 | -58.73849 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72bdcd1a-d806-37ea-8086-be86df524f0a | -11.07174 | -55.37949 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5443070-18af-3ef8-a375-bc24966e7d65 | -9.11414 | -59.05101 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e6da61-752a-38e7-be8f-bed6a44d97b2 | -10.12128 | -52.34721 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6ef1d4a0-b333-3119-b391-c6718001feee | -8.66813 | -51.4713 | 2025-07-01 05:36:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df32ef9b-c878-37f7-b8c5-daf91c8b9d58 | -10.30633 | -57.13718 | 2025-07-01 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88f9b04d-4967-30b8-a395-40a223afe006 | -9.08997 | -59.47352 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b973606b-6eb6-3fc6-b39d-2ea56fc61fe9 | -10.29907 | -57.04408 | 2025-07-01 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da0d1f73-43a8-3819-9ced-2d90d981400d | -10.28244 | -52.83106 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0933f5c-ea87-3d67-ba19-b9ff5d1f9aa3 | -13.01236 | -53.42376 | 2025-07-01 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfedb66e-b105-3694-99f2-052c8e4b4d79 | -9.11003 | -59.05043 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86e5ccc1-88a5-3d05-aa91-a0a384659ba8 | -11.57876 | -54.57117 | 2025-07-01 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 983f1f82-2fa1-3e82-b421-1c1391739f99 | -10.88006 | -56.45536 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 335c67f6-d41f-39ac-b835-cbf6f1174b8f | -11.2019 | -55.9163 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b10af14-d0af-33ee-ba07-7d3702859a0e | -10.87363 | -53.77384 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6613b7bc-7242-34f5-bd9f-7ac25e607031 | -9.24418 | -58.74694 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60972bcd-2a46-3361-9b14-5e7503b69c0e | -10.12899 | -52.3414 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34b23a94-41d6-3834-a12c-3d6ea3759c76 | -9.23889 | -58.75406 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 958c1bdc-49ae-37f5-b000-3b6940042eb1 | -10.30156 | -57.13659 | 2025-07-01 05:36:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29087430-302e-36dc-acd1-c49c31a8088b | -9.28159 | -56.23928 | 2025-07-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 391756e0-5774-3c89-9a35-bd1f48c45c8d | -9.40079 | -63.25936 | 2025-07-01 05:36:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7928b484-2ef5-3fec-b7db-faa74e50d127 | -10.12764 | -57.77525 | 2025-07-01 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7772e17-5fe7-3e8a-b296-bcd8619c5c98 | -11.59899 | -65.14894 | 2025-07-01 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ae823e8-0b82-3986-8296-97d30903d496 | -10.88131 | -53.76111 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b4778c4-e40e-34a4-a86c-298a91dbf73b | -9.23267 | -58.73726 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f31bcdf0-a6a9-3a77-9477-60e0b52b88af | -11.6035 | -65.14236 | 2025-07-01 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dabe8d03-af4c-3e1e-8ba0-2ecab26b5160 | -10.87309 | -53.77827 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6b209cf-0c1d-3238-ae45-d26c4f06f2e0 | -9.24473 | -58.74302 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c63590b6-4f71-32dd-84ec-23615a7a1d54 | -10.86543 | -53.74079 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eff88b4b-06a0-3d65-80e9-8be2084f7160 | -10.93305 | -55.32746 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2706e6ed-0706-3fc4-be01-a79dce77c616 | -10.12179 | -52.34617 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 475180d6-39f6-3e80-8d04-3f4beafaae03 | -10.87418 | -53.76939 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03460e5b-185f-3e2e-9c33-a93767ea6ac4 | -9.23742 | -58.73397 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbbc3dac-a80a-3f0d-aac1-c867b42fdecd | -10.87155 | -56.44205 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f064051-1197-3d31-ae6f-e62f983c8611 | -10.1276 | -52.35263 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7eba782e-432f-3dcc-b9c1-43af161c89d1 | -9.11056 | -59.04675 | 2025-07-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11540e83-b9de-31de-ab5b-129ae8775ab0 | -8.68894 | -63.78104 | 2025-07-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d35fe231-3236-3db6-95a4-95eea98659a3 | -10.87527 | -53.76046 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c92958d6-1de6-331c-9e84-d9c689d30779 | -10.86814 | -53.76875 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04ed19b9-3709-3708-9fde-1b63b8244a75 | -12.62834 | -54.22564 | 2025-07-01 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f296d32-1a94-328c-9b39-bf7c249397f3 | -11.59954 | -65.14544 | 2025-07-01 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ecfb250-b73c-324e-9a70-bca0b399b5d4 | -9.24254 | -58.75856 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34e64c82-d249-39c3-a4a9-329301a8b2c8 | -7.91669 | -61.55987 | 2025-07-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 008ecba4-a4d8-3c07-8db3-495eedc181dc | -12.63484 | -54.22197 | 2025-07-01 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 102f2102-838c-3859-bad8-dfa5968c03e1 | -10.27938 | -52.83424 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a43731d8-b153-38bd-aacc-a105309d30cc | -10.13155 | -57.78058 | 2025-07-01 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fb04aac-a9f4-3443-a545-f4c2c4368352 | -11.19667 | -55.91549 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f6793f2-6f8a-3174-98e4-58aae26aa374 | -11.83059 | -62.76843 | 2025-07-01 05:36:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c041814-2beb-3138-a999-1975a5556118 | -10.93689 | -55.32755 | 2025-07-01 05:36:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfe41917-d249-3e1a-9c01-a06b96a2210b | -10.08189 | -52.73924 | 2025-07-01 05:36:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75d94e49-6422-3138-ade3-3b0ab619eb09 | -10.88084 | -56.44943 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1bcb32f2-7a30-33d4-84e7-e119752f6ddf | -9.24784 | -58.75144 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65a86012-b21b-3691-88de-8dc25087fd9c | -9.23469 | -58.75345 | 2025-07-01 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 602c960c-ba91-3718-962c-ec1e5dcc3fc5 | -7.91762 | -61.55942 | 2025-07-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e76c598-057a-326f-93b4-f1fb9a219120 | -10.88627 | -56.4472 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ad0a05e-e23c-3f6c-a23c-372307934fc5 | -10.89133 | -56.44773 | 2025-07-01 05:36:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a11bd322-0c2d-3dd5-a0b6-05bda1cf1bbf | -9.70745 | -56.1826 | 2025-07-01 05:36:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fc249c3a-e307-3ac5-a234-2c7678e6b7ca | -10.86869 | -53.76429 | 2025-07-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8368edb4-06e4-3309-853f-c8c8b8385512 | -6.2943 | -43.6891 | 2025-07-01 05:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 37d02692-1819-32fd-8ae5-0a93cee686c3 | -6.2945 | -43.6659 | 2025-07-01 05:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| c090aed5-66f1-33f1-a6ce-96d2874fbde8 | -24.73998 | -53.80888 | 2025-07-01 05:40:00 | NOAA-20 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 084030ac-c6da-3153-91a3-e26602319d9d | -6.2945 | -43.6659 | 2025-07-01 05:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e7bd9014-ff0d-392b-995f-e37d89bb0ed0 | -6.2943 | -43.6891 | 2025-07-01 05:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f663c373-64ec-39fc-a11f-7aff6b1e8671 | -6.2943 | -43.6891 | 2025-07-01 06:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 28c74e03-f5d2-3324-9298-c8e56a390790 | -6.2945 | -43.6659 | 2025-07-01 06:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b4e7411c-72dc-3223-a285-85a9bfbf7ec5 | -6.2945 | -43.6659 | 2025-07-01 06:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| b2e8f5e0-5220-331e-b688-b7c75fb1e945 | -6.2943 | -43.6891 | 2025-07-01 06:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 876abd4c-8158-3832-b609-7e86d95719ae | -6.2943 | -43.6891 | 2025-07-01 06:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b7f48d7f-4f1b-3680-b59e-add20e6a160d | -6.2945 | -43.6659 | 2025-07-01 06:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| a8a6c5dc-1908-38df-b02d-d8f4bf515c10 | -10.8775 | -56.44161 | 2025-07-01 06:27:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| e6de78d4-16e2-367d-b497-a9b374926ab1 | -10.12343 | -52.33534 | 2025-07-01 06:27:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2ee50966-5c61-31c1-aa65-855f59fb2604 | -12.62808 | -54.2164 | 2025-07-01 06:27:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.4 |
| f683115b-1969-31e4-a0cb-305935681c36 | -10.08118 | -52.7371 | 2025-07-01 06:27:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9efd78b7-dd91-3c8c-ac9f-3a7bd625b91d | -12.63005 | -54.21047 | 2025-07-01 06:27:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b2bdc9e5-0847-3897-b826-baa0c16259ef | -9.69639 | -56.18588 | 2025-07-01 06:27:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b42d5aa3-29cc-38ac-8ba0-fe7a4a509803 | -10.87617 | -56.45061 | 2025-07-01 06:27:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 754bf3e6-4ea2-3323-aa18-7af3eb24f431 | -10.07462 | -52.74401 | 2025-07-01 06:27:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 26026c19-ef67-370a-ba34-0bafa9c5c73e | -9.70657 | -56.17824 | 2025-07-01 06:27:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2c5056e3-5910-3deb-816c-e18026a1969a | -12.62849 | -54.22203 | 2025-07-01 06:27:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8699f455-ef44-3ae0-a4d2-675d1b39f055 | -10.11952 | -52.34384 | 2025-07-01 06:27:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6633f4bb-0818-3f3f-89c6-b643ef65b000 | -10.86865 | -56.44028 | 2025-07-01 06:27:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 80fc6071-7f0b-3921-a09d-2d58bd8362a0 | -9.70524 | -56.18721 | 2025-07-01 06:27:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README19.md)
