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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea021da1-e38d-32d8-ac3c-5a8065cec5fe | -12.6108 | -57.00613 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 307a49c9-84ab-3ea2-9578-2919aa2652d4 | -12.92592 | -48.08099 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32e97390-2855-3d3c-99d8-d67a4e19c9a3 | -14.8139 | -48.37876 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce80f6c9-2a36-37d1-bee6-bc59d482ead4 | -16.29057 | -52.96114 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7359b94e-d055-32f3-99bc-7e0f3ed684c1 | -15.60262 | -52.683 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5192d6e7-ed10-327d-bafb-c297c4592936 | -14.81061 | -48.37337 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67273c7e-4821-38cf-8a86-b117a330fd26 | -14.39904 | -51.66288 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51870e16-a8c4-3ad0-8878-9679d78e9f18 | -15.14939 | -52.35889 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2bd5a6f-9b68-361e-a2a4-e274df326293 | -14.52894 | -53.29145 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66459b1a-bb61-3245-ac1a-da0e745c9f13 | -15.54989 | -48.37127 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6ffb52df-1a12-39f2-a3cf-bde79f607cfb | -11.86824 | -52.4283 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba4c0ad1-7406-32ee-9d7f-f35eaf48084b | -16.29774 | -52.95866 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5582201b-6b9b-3b45-821d-f4e786d4904c | -15.01018 | -50.05789 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| df8d7157-8bc1-304b-bb0a-03cc33d4363f | -12.93543 | -56.95873 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66276206-9c5e-38d9-85ac-1c70f9e96f86 | -14.59436 | -54.58304 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7aa29abb-088f-378f-a24f-43365731f4a7 | -13.72874 | -46.94426 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 649037ea-08ef-3d6d-a470-dcbc40f0df35 | -12.88337 | -48.03836 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f9e62d9-996d-3265-a73e-706371569d4c | -11.6613 | -57.35275 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6e4c060-2f33-3879-be7d-2b3ffa2cc790 | -13.69954 | -46.93791 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7d1c258-c141-3ca5-8d1e-e557e49e474f | -15.55437 | -48.34789 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d776dfe-b660-310c-8e63-05b27ed96724 | -14.25748 | -51.22753 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de567668-a4e6-3791-a90b-214f0a07c08e | -16.2983 | -52.95508 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e5bfc5a-1f35-39b2-b84a-ece35a2801a4 | -15.02632 | -50.04727 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8e3a54a-edb4-355d-aed3-13503e18a533 | -13.33037 | -46.82831 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a109490-ae67-3be7-b95e-a4d0095ca819 | -15.12563 | -48.17526 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 580a8ce5-ff38-38c2-8e1c-2edeb301fade | -14.30836 | -53.09139 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 483a16b3-e975-3dae-8307-fea8b811dbec | -16.41138 | -45.65158 | 2025-09-03 04:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec1a2444-4c91-30a9-b59a-7bdb8d248382 | -12.89348 | -56.95156 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40b4e4c1-1e64-341c-bfe8-57e07570af6e | -14.81244 | -48.21451 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3621f7e6-7fd3-33bf-9b79-e772545a0292 | -11.86108 | -52.43074 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2258de2c-c544-3012-b9c7-8e5839ba5505 | -14.81454 | -48.3739 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f6fa55b-0dc3-3a2d-ac9c-d90fa3c4ceeb | -13.00055 | -48.11621 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1811606c-b09b-37cd-8c39-2b4626fd9add | -14.33087 | -60.34441 | 2025-09-03 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 774d716f-3f63-3a35-aa16-39b35e879013 | -11.84463 | -51.41613 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa6f6f2b-19fa-35c3-a082-5c80d4047077 | -12.79029 | -47.66862 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfd51c6e-c4c4-3fa8-889f-71927f476062 | -12.02511 | -50.59801 | 2025-09-03 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2206cdec-9302-3b71-afbe-6130c1974368 | -15.5504 | -48.34727 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3c3362d-451c-326b-965e-756d9a93e633 | -12.93973 | -56.97291 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7c93c56-6416-3157-b1d3-885dbb0f3cf4 | -15.00126 | -50.05346 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ed5b300-10a5-3d2f-a0d2-9e3f5081e012 | -14.81455 | -48.34367 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d06207e-0717-36c4-8e68-d0833ec65fa5 | -12.96313 | -48.07096 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 331ca39d-5666-3318-bb1b-92ff1dd0c6a6 | -13.53447 | -47.01236 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b029f13f-0c90-3c54-a606-c581d3a8ee42 | -15.11904 | -48.16377 | 2025-09-03 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285574f2-96d3-3783-86f2-68c32f3dd0b1 | -14.57793 | -48.05202 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17aafaff-c8af-333c-adbf-51553dc6aebf | -12.29685 | -50.00842 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e62ab28a-080f-366e-95fd-ecd4d9070081 | -14.3045 | -53.09439 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a229263-648e-3b11-9d48-54c26d0d45e7 | -12.16922 | -50.1272 | 2025-09-03 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fe0850b-9f69-3506-ae91-0f4088b44450 | -15.19316 | -52.34022 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e69191b-71d1-3f67-9ac9-8cffb6cd2b32 | -15.01617 | -50.06739 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d397fba-73ed-343d-88e5-c3bd6bdab826 | -12.5146 | -49.57653 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2346ef8-f833-3939-b9f9-bf5d124b4344 | -14.78577 | -48.17247 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a541982-4576-3444-8e0c-77a1b8b4e40e | -11.83215 | -51.56401 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e58b0f2-f09d-3451-af95-2f7857d9ffb1 | -13.45497 | -46.92876 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bf2b811-adee-3d56-8776-849e883e075c | -14.56813 | -48.06433 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c53d0157-ae7e-3d88-81bb-d785747bb236 | -12.96108 | -48.08572 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c513b5c8-bc54-372d-910c-8d35d5c9bbe1 | -14.40975 | -51.70582 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b37246de-3ba1-3725-8549-7098f3bbdb72 | -12.63336 | -56.99015 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e96ed507-ae94-3bf0-8f84-e72db77caed4 | -14.2688 | -51.22162 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a70a601-0fb2-38da-8b5b-bb880d4db95e | -11.85462 | -51.41779 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b40c01e-8bdf-3ca8-9158-a9772f31ed94 | -11.31878 | -55.21965 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac746cc7-b621-307a-af40-8372e70dc8c0 | -13.01948 | -56.87448 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60abb7c5-963a-354c-930e-306a9ac9583a | -17.53108 | -47.57685 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1ed8367-5c3f-31c2-800b-fc03c6a8a0fa | -12.79222 | -47.65455 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82be1140-a359-388f-a560-868c096c5df3 | -14.98243 | -50.20819 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33cf9f9e-dced-3a9d-9a18-e5158ba865cf | -12.92341 | -57.0065 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b115caaa-3236-370d-9254-d9e840fa4cfc | -12.91638 | -56.99375 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f9eac7c-370e-3fb6-b2e3-f228441e9999 | -12.91764 | -57.00891 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 447402bc-9392-3bbd-a2d9-95d5b098c24f | -15.575 | -48.31553 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35980f94-3744-330c-8e62-13a11856dc69 | -13.49712 | -51.8084 | 2025-09-03 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 420c75ef-4d3f-3c6d-93ca-ee37f1150480 | -11.41964 | -55.18122 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a731da7-3c5b-3877-9b8a-1b9a13b04c51 | -13.53025 | -47.0118 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31409e28-366d-3781-8f6d-2b2a31b6f1f2 | -13.27783 | -46.83298 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea8b1a02-b869-336d-a076-f41904bdd012 | -12.85492 | -48.1846 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 827bc33b-5584-3a9e-8480-4e06c8ecd923 | -15.7393 | -53.66116 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c49ae49-31a2-3dc8-9708-6811db810598 | -15.75245 | -53.68536 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 631cc95b-2202-3dac-8b87-15760e41f8ba | -14.32378 | -53.10119 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bec707fd-6159-31bf-9531-9a927cd4bce0 | -12.29267 | -50.00422 | 2025-09-03 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d39acf78-bbf2-3c7d-9cd7-5b6054038feb | -12.4861 | -53.82824 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a2a2d3-4147-3c3b-833f-7fd7b7841928 | -15.00364 | -50.06232 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7989f61-35a3-3d27-9c1a-b0192a3cd0e0 | -13.7339 | -46.93792 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc766ed0-ef89-391a-a94e-fb450283332b | -17.53056 | -47.58107 | 2025-09-03 04:49:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4bce20b1-4d65-3a7f-aa8d-e53a8228a623 | -13.09843 | -57.11829 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 256ed7c7-3669-3255-87c6-fb9b19aeeafa | -15.55213 | -48.36434 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5f874151-6831-330e-ac0c-dbc82b7cedc2 | -14.41142 | -51.69485 | 2025-09-03 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c71a2bca-1acf-3243-88fd-9ba110409fc8 | -15.74527 | -53.68781 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1b8408b-275a-313d-8a32-75a0b20cea23 | -14.80292 | -48.22501 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50c0bcdf-41c7-3fa1-afd4-c46ed233270a | -14.58286 | -48.04567 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d630582-f36a-3b93-b684-38f4f65e49b8 | -12.92044 | -56.93157 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 283abbd4-93d5-3e8b-82cc-961ab3df1da5 | -13.35841 | -46.33957 | 2025-09-03 04:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 858a8b4a-220e-3d2c-a0d9-5720aa8a8f58 | -14.98069 | -50.19516 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab0f372e-817e-3c06-87c5-0dd84ce288a1 | -14.98493 | -50.21176 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f07cba89-82c6-3c2d-bf4e-399f22e4aa6f | -14.90642 | -49.62321 | 2025-09-03 04:49:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ccb2d86-2b79-353c-839d-fa55b31469c1 | -14.56676 | -53.02855 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 855be07f-c929-3f20-ab8c-b1444f0313df | -15.38005 | -52.78251 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b7a25b7-b13d-3c0a-bce5-3c9f0b8d0bed | -15.15216 | -52.36311 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cf46ccb-186b-3bc0-b29b-8d0ed43a56df | -11.66298 | -57.35296 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccd6b5b6-a5a5-30aa-be3a-f0dafa6cc7f5 | -14.82175 | -48.34981 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95132424-a524-32d9-8cf4-b2aa92630e56 | -13.70338 | -46.87739 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e613591-0ab1-34f3-8d34-d93ddeece001 | -12.62315 | -57.00338 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d382e011-2fbf-39a4-b4ae-00f579f05058 | -15.74197 | -53.68726 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README78.md)
