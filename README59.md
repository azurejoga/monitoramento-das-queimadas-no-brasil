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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04f45fff-057f-3ad3-b4bb-09b06516c4e1 | -10.68031 | -54.15119 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0819d9a-628b-3741-b774-72554cf37dda | -8.37406 | -54.72435 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8ef67311-8007-3df2-b8f4-98050cfd5d41 | -6.79628 | -58.79119 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c5701ff-bced-3dec-9e33-d1141646b982 | -8.80577 | -46.9073 | 2026-09-15 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5840351-9e1f-3803-aec2-b60e38ad7ad4 | -6.82885 | -58.64693 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c11f930-e2e2-3671-a953-f7c675dde853 | -6.74055 | -59.43385 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fb3e42e-96c1-3f72-bcf9-1ecfc0f8f6e6 | -8.54751 | -54.7114 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4547b873-f98e-3054-aca7-bf69566b949b | -5.91019 | -52.10493 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fbdb865-ab6f-3289-a8f0-df56039ea398 | -6.79959 | -58.79171 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63a916fc-504a-3858-a030-a16e306cf710 | -9.22122 | -56.57162 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dedb906e-0348-3c82-b228-9950e02f833f | -6.85017 | -55.53768 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d49c3f4-e3e5-3d0e-a7a9-fe3fb41f20b2 | -9.41429 | -62.71164 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0f71626e-12cc-3737-be40-db3de1048bfb | -6.84884 | -55.54662 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b36b2298-bd01-3c03-a036-e19db0dd164e | -6.74386 | -59.43437 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d2f412f-3b10-3b9e-8a7c-e4eae5d6eb1f | -9.3592 | -50.10762 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fdabb2d2-718e-303c-95c1-a04011f2bf25 | -6.92119 | -55.63649 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 867c5768-df41-34cd-8a22-c87fc415e5a4 | -9.36472 | -50.10836 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3cc3c552-5a05-3b15-872f-4b0304bc6743 | -6.20533 | -57.77654 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21cbfde1-ecc2-3f76-a00b-a68f7732cc86 | -7.61493 | -47.29106 | 2026-09-15 05:18:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df494c55-7658-3f63-86d4-6cd2df2f3f61 | -10.81033 | -46.2168 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6576f480-244e-3966-bd8d-9db15a030fe7 | -6.07656 | -57.86195 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e4080578-b2de-35f4-848d-2e98b989bd9d | -10.256 | -57.6972 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f636acc-b599-3e5a-ac70-ae19d495d4cb | -5.08222 | -56.24654 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9efa0c24-c5e7-32bc-9618-04af56026555 | -9.03913 | -60.52191 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e8b136f-0a15-3b11-b6d0-2b4f80340934 | -10.66267 | -54.15295 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43e018e0-fb19-394a-8c26-9e6fc3f4e354 | -6.84686 | -55.55993 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd35fc75-3a91-358a-80d4-12d8ea95d073 | -10.50725 | -53.5681 | 2026-09-15 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 085ab4ef-b5ef-34d1-8a56-a321dcf36924 | -6.10242 | -57.69444 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0859ba22-ab59-30a7-9cc9-9e4dd34f5a3f | -9.41587 | -50.10289 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f288f20b-e50d-3393-8e17-1a6b9956d19a | -6.68747 | -58.70337 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc2a317a-5063-3636-b647-c241224ef5af | -6.13634 | -59.87901 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4db150f1-2adc-3135-9b9c-619d4a3470b7 | -9.84982 | -65.17815 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79c7180f-6abb-3d4e-9fc7-392551ba96b1 | -6.79682 | -58.78772 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 562d8b2e-3006-3f8d-beca-e5a188853840 | -5.37283 | -56.04874 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b466f16-e73a-37d0-97d6-cdd724f6e836 | -9.35536 | -50.1367 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afc3fac7-6d3a-352d-af14-302c4dfa6ece | -5.97494 | -55.35905 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ada9291-33b6-3a4e-8003-8134634432b7 | -8.11803 | -54.80313 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdcd8c39-93f9-3271-8393-2d43bde4eb0d | -6.82831 | -58.65041 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbc5ae7c-7fd4-3db7-9ab2-fb249afac2cf | -8.542 | -54.69267 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc8c8606-02cb-3295-b482-cfed9c3d4a2b | -10.67386 | -54.16681 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a3a7325-e925-3d5d-8515-93d0dc454d19 | -10.57646 | -47.73532 | 2026-09-15 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f90581b-4610-393d-a8e5-aa22e141ae2a | -6.69239 | -58.69347 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5ee54f8f-f51a-3780-a0e9-95e48269b8f9 | -10.30292 | -54.16834 | 2026-09-15 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d8b3d034-21f6-3c1b-9ce9-ace14d6e4d25 | -5.07812 | -56.2499 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a20bd52-160e-3226-8b25-b48146cd411c | -10.8884 | -51.56028 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a9ef4fe-5ffd-3387-8e2d-0445182ff301 | -8.08827 | -61.79866 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 341c087c-5365-3b85-997b-1879abb71961 | -10.23232 | -56.25977 | 2026-09-15 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8554575-2fd5-3119-8b5e-6451bdbbc1c8 | -10.8855 | -51.56006 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42ac5d93-7b92-3cce-9d16-a86e2d2bd720 | -6.13732 | -57.68179 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d050019-7b84-3e5a-a5f6-25103f09cd83 | -6.11228 | -55.82049 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f712677-be39-34b3-b379-a96a7aa379ea | -9.0124 | -61.00969 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5033aedc-75ad-31c4-aa52-68f9e2aeaaf1 | -6.43713 | -58.14575 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a0119b1-a310-34ea-bcbe-b74c57602471 | -10.65459 | -58.76304 | 2026-09-15 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 272e22cf-aacb-3022-a90a-b9f11606956e | -10.88366 | -51.5565 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5330bf9d-b38d-3485-9d49-fddebda2ea5d | -10.50664 | -53.57248 | 2026-09-15 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 986970b5-b59f-3ee0-8955-98a2edb72db2 | -9.36017 | -50.10031 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4dab3e63-a748-326d-90e5-ef9f99b9b321 | -9.88399 | -47.77399 | 2026-09-15 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed0a5208-4b59-3de0-8aff-40de061cec1b | -10.86541 | -46.3093 | 2026-09-15 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88a50c6f-fcde-3532-94f4-e62836cb829d | -6.68639 | -58.7103 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95ed02dc-67dc-364e-bf0b-c63ecaab40e3 | -6.10744 | -57.68419 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d18cc1bc-6767-3917-af06-dd9ad5d5f7bb | -6.31512 | -59.9537 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9149398-e741-377e-b1d3-e2d90caf624f | -8.53506 | -54.71306 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 927985b1-481e-3685-bc46-959d443a5665 | -8.40893 | -54.72626 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdb7a743-dd2e-38b7-9936-6047e0f15115 | -6.88139 | -59.64083 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c87b9dbb-63d8-39de-a51e-301e77be6c39 | -8.46773 | -50.77119 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e91a6b6e-edf1-3c22-9509-2ed91c4e104a | -9.2665 | -59.63663 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bee056fa-c6f2-34ab-ba1d-cfab8bf1924a | -6.28165 | -56.0426 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5974c017-24e2-39c9-a2d3-3048ae1c9496 | -5.13196 | -55.94093 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b33f512-4293-3032-b562-32d305d8e10f | -6.07287 | -59.97975 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9949a10-fea2-3054-8ca9-ab41518a0f07 | -6.14186 | -57.6972 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e87d3a41-bce0-30ae-a8a6-17f43718d2a0 | -10.67604 | -54.15057 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89b21b42-09c7-3852-80c1-f4c0ca93442d | -9.01911 | -61.01075 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1c267cf-f128-3fb0-81b1-ef3d3b2f03e5 | -6.11025 | -57.68828 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 438028da-b663-3e39-82d1-77e97bb02beb | -6.7444 | -59.43092 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feb5fd1e-fa84-3ddf-9484-c83dccafb23a | -9.87812 | -47.77596 | 2026-09-15 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 943f9503-f54d-3f5f-826d-4525e487f2b6 | -10.88113 | -54.01458 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a019154-d446-3c4c-a577-478519b15668 | -9.45707 | -56.70515 | 2026-09-15 05:18:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a7b0d99-869f-3226-9e69-443c192e1b71 | -8.53954 | -54.71017 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67b4a1d1-d5d9-3e4a-98ec-3bb567335540 | -6.15789 | -52.79497 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c1fe4f7-a918-336f-ac49-40cfb5c8730b | -6.11246 | -57.67395 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc0708e1-0998-36dc-85ef-d34849b6614c | -9.71997 | -64.90868 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb802247-34fc-369e-9982-8413ccda6951 | -10.80021 | -46.21192 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bd5434a2-7a88-3134-9c70-e62b1f603a50 | -9.26595 | -59.64011 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdd906c3-86ee-3f9d-bef1-3f4df029b261 | -7.21841 | -46.13985 | 2026-09-15 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a1f5ae89-a1ba-3a40-a40c-8fc0b71fc196 | -10.89861 | -51.56178 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcc3d3a6-bd38-3229-965e-b2cbe042ea6d | -6.84447 | -55.55053 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| af9b8034-9fb4-3665-9269-2cf9479ab4c1 | -9.67808 | -47.8975 | 2026-09-15 05:18:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d6d04de-9242-3f89-9a58-83298a9da743 | -10.58312 | -47.73478 | 2026-09-15 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a6d4aab-8c50-343b-af66-22e48133abfb | -6.13247 | -59.88198 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a088c4af-eed2-362f-b0bc-dff7efb02267 | -6.13302 | -59.87849 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f970bada-5fc2-332c-8466-5cf0173a24a5 | -6.55583 | -51.19648 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01e67393-fc63-3934-955c-f69e66f67129 | -5.13489 | -55.94561 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41c0a0c7-1a3b-37d9-9500-3866707b526b | -10.67494 | -54.15872 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f813227c-ae9d-3597-a547-6b063c8afe7b | -9.25626 | -48.54517 | 2026-09-15 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 440f33c7-4c83-3ac7-9f77-91098162a6c0 | -9.41493 | -50.11021 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0df31dd3-5887-3ef7-8909-58fbbaa1d6c0 | -5.13784 | -55.95021 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04de0768-afb9-3570-bf1f-ccd2268eb70b | -7.2285 | -46.16365 | 2026-09-15 05:18:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a29d4a61-208c-3d99-ba95-4e6b2c63b2b8 | -6.01682 | -59.94582 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75952e73-d663-3b2f-a1a2-b5231d49128c | -8.40832 | -54.73061 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 837d0ae9-ec60-316b-a422-cfc6fef2f3c2 | -5.45317 | -60.21905 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README60.md)
