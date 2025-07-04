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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2f066da-6c21-3548-bca1-710fcf14ea72 | -6.2945 | -43.6659 | 2025-07-04 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| ce1788e5-32ca-3923-8af5-28f612c7c987 | -7.2403 | -43.1134 | 2025-07-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.9 |
| b312aa78-22a1-3eeb-bdb8-1c141acfa45f | -7.2219 | -43.0682 | 2025-07-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 7ab876f3-4d7e-33c4-be5f-ffe6726a28b4 | -11.932 | -45.389 | 2025-07-04 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| b2a6a797-714e-3ecf-ac7f-fd5a607567b8 | -6.2757 | -43.6675 | 2025-07-04 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 50c1b2f4-19c0-3b67-a728-c14373b5d5da | -11.9324 | -45.366 | 2025-07-04 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 95d2b3bc-50bf-3ccc-a920-8f26c1ff0e04 | -7.2214 | -43.1153 | 2025-07-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.7 |
| d7a55cda-c806-33f7-a3bf-db630f6134aa | -11.9128 | -45.3919 | 2025-07-04 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 6f2c1540-7ab6-380d-866c-d2c91943bc99 | -6.2755 | -43.6907 | 2025-07-04 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 060a210b-3619-35db-b795-f299511c90e4 | -10.5586 | -49.1337 | 2025-07-04 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 6dfb0b8f-fa28-3480-a856-0e7b2c67b01b | -6.6112 | -43.8941 | 2025-07-04 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6fc7c0e6-d298-3237-a061-349b37ae6e92 | -18.4486 | -54.6674 | 2025-07-04 01:10:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 55.2 |
| a6656d14-be85-3895-b426-69e86985a8c3 | -7.2405 | -43.0899 | 2025-07-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| 688164f4-2709-3f40-b610-79eebb122f8f | -7.2217 | -43.0917 | 2025-07-04 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 192.3 |
| f602d488-7977-3939-a443-db62ec5837e4 | -11.9132 | -45.3688 | 2025-07-04 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f8139389-8da6-3a8b-a340-922fd5808ceb | -6.2755 | -43.6907 | 2025-07-04 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 029b89a7-1999-338e-a9d8-f142af083a20 | -11.932 | -45.389 | 2025-07-04 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| cd3f164f-c984-364b-b19e-24f28465a551 | -6.2757 | -43.6675 | 2025-07-04 01:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| a6cff25e-39cd-39a0-bb4b-d96db5eec25a | -7.2214 | -43.1153 | 2025-07-04 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| dcaf8ab9-4f64-309c-8518-43ddab0d4eb2 | -11.9128 | -45.3919 | 2025-07-04 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 437186e5-277d-3027-b44d-b948aeaf5674 | -18.4486 | -54.6674 | 2025-07-04 01:20:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 59.3 |
| c02baaad-9dae-337f-bfc6-3f6a61e0174f | -7.2219 | -43.0682 | 2025-07-04 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 1283a2cd-b158-3dd8-b4d8-f5f02864914c | -7.2405 | -43.0899 | 2025-07-04 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 9b9f2931-f534-3aa6-9593-d5b94af2c712 | -6.6112 | -43.8941 | 2025-07-04 01:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| bc32f595-976f-3062-8f66-fc1e3f685177 | -10.5586 | -49.1337 | 2025-07-04 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a30d6c1c-7c3b-317e-a7c4-d568b5305801 | -7.2217 | -43.0917 | 2025-07-04 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 200.0 |
| 236d8cfa-e190-3a30-86d2-8711a60dbe8f | -11.9324 | -45.366 | 2025-07-04 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 27c8f1c2-e0a6-3982-b19b-a2bd3e05dcc4 | -6.2757 | -43.6675 | 2025-07-04 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 050af5ce-3efd-3ac6-b8a3-9e5e86d08886 | -7.2219 | -43.0682 | 2025-07-04 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.3 |
| b144e6ad-9ffd-3b76-aec5-678f2d82e394 | -7.2217 | -43.0917 | 2025-07-04 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 180.1 |
| 22d10ff3-24e2-3551-a545-b55bac037a0f | -10.5586 | -49.1337 | 2025-07-04 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 7bc4ea03-7042-3536-9612-caffd2cd3ccf | -6.2755 | -43.6907 | 2025-07-04 01:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 96280ff2-57a5-3267-9ca9-31fcb928feca | -18.4486 | -54.6674 | 2025-07-04 01:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 1cc4463c-e4c0-39df-9a63-f9c4e8e631d3 | -11.9128 | -45.3919 | 2025-07-04 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 2dc8bfb3-8afd-3605-ba95-2e0574ed441f | -6.6112 | -43.8941 | 2025-07-04 01:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 31327ac1-f36f-38f3-aede-e58ed0f09b2f | -7.2405 | -43.0899 | 2025-07-04 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 67069964-4364-3435-b212-0c656772fee5 | -11.932 | -45.389 | 2025-07-04 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| b4db67f7-6aac-3745-b900-b94434582ed4 | -11.9324 | -45.366 | 2025-07-04 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 539515f7-1960-3a95-bc8e-9ada607e82e8 | -18.66631 | -55.74926 | 2025-07-04 01:39:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 747e94bd-fc94-33b1-a96b-039f3eb249c0 | -18.45183 | -54.68712 | 2025-07-04 01:39:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 39.3 |
| e8333ba1-8c1d-3a9e-9cf6-a484ff2bf915 | -18.44748 | -54.66311 | 2025-07-04 01:39:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9c0e5d39-85e0-3fbc-ab4c-84112e32aa75 | -7.2217 | -43.0917 | 2025-07-04 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 550b8148-eac5-306d-b199-5fe5c4f67b4e | -7.2405 | -43.0899 | 2025-07-04 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 947f9c04-65a6-3f0f-b0bc-6be3eeba5358 | -10.5586 | -49.1337 | 2025-07-04 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 73385dcf-0712-3079-a0b2-91981ecd7a0f | -6.2757 | -43.6675 | 2025-07-04 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 07175b33-0269-37a7-b858-75ff52c1ad45 | -11.9128 | -45.3919 | 2025-07-04 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 4ea4dfb7-36e5-3d32-b917-0a09269ee430 | -6.6112 | -43.8941 | 2025-07-04 01:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a8ed72e8-52fb-30e1-b846-c27e65bf8312 | -11.932 | -45.389 | 2025-07-04 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| aacee147-e2f7-334b-bd51-634a7edf1b9c | -6.6115 | -43.8709 | 2025-07-04 01:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 15bcdbab-22c4-3d57-b3e4-33e3fd866d88 | -11.9324 | -45.366 | 2025-07-04 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3bff2c88-c94a-34bd-b938-5c60c2709855 | -9.62773 | -61.46535 | 2025-07-04 01:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 46a8ccf4-b295-3189-93f4-5f0b0d9b6f92 | -12.5787 | -56.9794 | 2025-07-04 01:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 1d545ade-d4fa-3ca4-8a8a-d41160d7d567 | -9.63198 | -61.46983 | 2025-07-04 01:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 071c1dc2-f3f9-3cd2-97a6-caabaa96bb05 | -9.53179 | -63.57925 | 2025-07-04 01:41:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 709c0f05-d895-32ce-8d49-834f53a2f058 | -9.51366 | -65.58938 | 2025-07-04 01:41:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1c116446-261f-3181-b111-4447a988c59f | -8.72085 | -64.17696 | 2025-07-04 01:41:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5676ae00-e7d5-3ec7-8636-05a9d674ce8f | -9.63038 | -61.45912 | 2025-07-04 01:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 24a87186-6c7e-375e-99a2-d25b475c2260 | -9.53053 | -63.57025 | 2025-07-04 01:41:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6f39d7fd-5fd4-3063-b6b5-0ae24ecbafed | -2.97921 | -60.98099 | 2025-07-04 01:43:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7dc62b83-b106-3dab-9812-59b9979f9986 | -6.6115 | -43.8709 | 2025-07-04 01:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 0ca12a7d-e3bb-32e2-a37f-db6fd8a77f11 | -7.2405 | -43.0899 | 2025-07-04 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 7cfa8116-dbc1-3135-9154-64461747d83c | -7.2217 | -43.0917 | 2025-07-04 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 7a10a5b3-ae59-35eb-a92c-387b0841eb56 | -10.5586 | -49.1337 | 2025-07-04 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 108c3233-7213-360b-974f-e12827a75323 | -11.932 | -45.389 | 2025-07-04 01:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 3b782eea-3ef0-36fa-8298-152f2f82b6f2 | -11.9128 | -45.3919 | 2025-07-04 01:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b1e0952c-3df6-3cb8-a5b2-69ba75c2a03d | -6.6112 | -43.8941 | 2025-07-04 01:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9b7d74b3-25b2-35f7-8a60-2679a9343c03 | -6.2757 | -43.6675 | 2025-07-04 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 5bc3e5fc-847b-3837-9419-cc50ecbe2a7a | -6.6115 | -43.8709 | 2025-07-04 02:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 9ee5802e-a605-3437-b986-7dd72b0c25a0 | -7.2405 | -43.0899 | 2025-07-04 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| dca2c782-2cce-30d3-b0cf-88c592e5b8c6 | -11.9128 | -45.3919 | 2025-07-04 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d6164e5e-67a0-3035-8377-41759d6cce23 | -10.5586 | -49.1337 | 2025-07-04 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| dc73406e-7f71-3e3e-97bb-ed7e2dcd3937 | -6.2757 | -43.6675 | 2025-07-04 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 202109f9-62bb-3d44-a5cc-44225c5f7423 | -6.6112 | -43.8941 | 2025-07-04 02:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f3c4aa52-6213-36e9-8dfe-ac556a8039a4 | -11.932 | -45.389 | 2025-07-04 02:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f7fa2647-2109-3c8c-97ec-67fae7369689 | -7.2217 | -43.0917 | 2025-07-04 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| 07160a91-6a2d-3c23-9c89-a431c817fb66 | -11.932 | -45.389 | 2025-07-04 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 614ec735-6ae3-356a-9c8a-7ea38b4ebdb0 | -7.2217 | -43.0917 | 2025-07-04 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| e50a5879-ad7e-31d6-a4b5-a33ae08c70be | -10.5586 | -49.1337 | 2025-07-04 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9db9b446-a9ec-3896-8842-c206f6aad38b | -7.2405 | -43.0899 | 2025-07-04 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 155d8781-5294-3cd8-826f-fbfec2866c0c | -11.9128 | -45.3919 | 2025-07-04 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 051aeb72-d92e-31db-84f9-5a480e07fd8f | -6.6112 | -43.8941 | 2025-07-04 02:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 62796be0-ab7c-3baf-8bae-a5e2e1b49035 | -6.6112 | -43.8941 | 2025-07-04 02:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ba1e7ea9-dece-39d7-83af-f049281a8fee | -6.6115 | -43.8709 | 2025-07-04 02:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 856dd797-8070-34b0-974e-44b567711e25 | -7.2405 | -43.0899 | 2025-07-04 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| ae4f3beb-e8bc-386c-8642-7c676af4f7c5 | -10.5586 | -49.1337 | 2025-07-04 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d4e7e85e-1779-3366-a4cf-f724e603e505 | -7.2217 | -43.0917 | 2025-07-04 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| fc31a479-6872-34d9-8751-34af8da2434d | -11.932 | -45.389 | 2025-07-04 02:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1c47127a-585b-3600-84dc-c50bfc7375f8 | -11.932 | -45.389 | 2025-07-04 02:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c08b1134-34e4-365e-878f-277dd9810167 | -7.2217 | -43.0917 | 2025-07-04 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.8 |
| bf0d50df-c208-35d1-9250-e71376550eaf | -6.6112 | -43.8941 | 2025-07-04 02:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| eaf65550-be2b-369d-9be8-bedaad470ce5 | -10.5586 | -49.1337 | 2025-07-04 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 24d4d8d7-a492-3383-bc1f-13a5716ed3ba | -6.6115 | -43.8709 | 2025-07-04 02:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 6782ec4b-f8e7-3f72-b736-538cecaf6129 | -6.6112 | -43.8941 | 2025-07-04 02:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c91e2e35-70fa-3efb-a961-92597faf3c09 | -7.2405 | -43.0899 | 2025-07-04 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 51.4 |
| 8263e7c5-f7c8-3a17-9d2e-30dd2b34f103 | -10.5586 | -49.1337 | 2025-07-04 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 7b111be9-a1c6-3866-8326-770dd418e8ff | -7.2217 | -43.0917 | 2025-07-04 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| df5036d8-9a65-328c-9b04-3cbd418b543f | -11.932 | -45.389 | 2025-07-04 02:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 46e05981-c0c0-390e-9a43-8bbdc6cad8ba | -11.9128 | -45.3919 | 2025-07-04 02:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 42d71df5-ddb2-3d17-b132-d303f5192f3d | -7.2217 | -43.0917 | 2025-07-04 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 2bb5e368-21f3-3d2b-86e2-812bbf5b64cc | -11.932 | -45.389 | 2025-07-04 02:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |


[Clique aqui para ver as próximas entradas](README4.md)
