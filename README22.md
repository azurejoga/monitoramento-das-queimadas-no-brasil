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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d7f4623-0b1d-3a41-971b-d153ac59be16 | -10.7514 | -60.73304 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de634149-5177-3bee-89dc-af7239dc94e1 | -10.7531 | -60.71607 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97c69b4b-663b-3dfe-ab5f-772724c53382 | -10.74691 | -60.72114 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc9642d3-bd91-3592-89ee-31c2d85e7a16 | -13.43336 | -43.827 | 2026-09-06 04:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98b8be2b-a27f-39aa-9251-11ecdfad2a44 | -15.0891 | -52.52057 | 2026-09-06 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b6d51ff-29b7-3ff3-aeaf-e07c11ce2b7f | -13.75627 | -51.65752 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6da7a0db-c9d8-32a3-a9b4-ee4ac99766db | -10.75465 | -60.71511 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15ae62aa-fb2d-3f24-92af-71f3cca009d9 | -13.77134 | -51.64872 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 35d3b657-1dda-3d51-accb-994057eb72f5 | -13.33709 | -54.05532 | 2026-09-06 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38a4d2e0-4c1e-343c-91a8-095492c63068 | -15.09236 | -52.52079 | 2026-09-06 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf1563b2-06d8-38c8-bcd5-656f51b74163 | -15.49 | -51.2832 | 2026-09-06 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee15a3ee-34f8-30a5-8622-e97e8f581a7f | -10.74348 | -60.76694 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cfdf7f0-4c38-3e77-8bca-ba2e56e2565c | -14.26842 | -51.95375 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94a42c4d-2302-3b98-a0b7-3bb295ead6e5 | -12.71802 | -43.2036 | 2026-09-06 04:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f1dc927-499b-3560-8c95-9959afea3a71 | -10.74851 | -60.72015 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d1d6976-4ed5-39d6-8fe7-fc5b85bf4d54 | -10.74748 | -60.71814 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1523eb4-3f90-37e6-94ff-481eec232b61 | -13.78025 | -51.63522 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7b9b210e-d191-36e6-9d2b-d0a8ff64e99b | -10.74432 | -60.77217 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f0329af-473d-3e2e-840f-8ab262acec20 | -13.43667 | -41.88734 | 2026-09-06 04:49:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 57379a23-34f8-3a51-a6e5-fbac093d8778 | -17.43281 | -40.02453 | 2026-09-06 04:49:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 1613cb3c-d9ef-3adf-9fc8-1fcc5165791f | -10.74543 | -60.76605 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25b0a0c2-eb89-38f0-961d-807d38bdab9e | -15.71595 | -43.69804 | 2026-09-06 04:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25c46ca8-8620-373f-98ad-fc66730dcdd2 | -10.7451 | -60.71021 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 13cd6a53-1874-395c-8e80-6a1424c19caf | -13.43128 | -41.88185 | 2026-09-06 04:49:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 45267947-4d87-3640-be77-eb4ad829f203 | -13.80207 | -51.64987 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf5baf73-b7ae-31a7-be61-e4744bd54042 | -10.75519 | -60.71215 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 07f79252-e2aa-3f50-bb17-82d76926c45d | -10.75759 | -60.71999 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ade3dbb-f184-35aa-9a79-9123157d453c | -10.75411 | -60.71807 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b721a815-4c8d-3aec-b18c-901453330600 | -15.70685 | -56.12254 | 2026-09-06 04:49:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68ca876e-72db-3dd0-9db0-758ea3770eea | -16.64099 | -49.53078 | 2026-09-06 04:49:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0148e7bb-5332-3814-97f7-ebae1741dffc | -16.40369 | -49.20255 | 2026-09-06 04:49:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1023db83-d3b5-3b9d-9dde-c26c676507c1 | -13.76298 | -51.65858 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 75cc9430-7b5f-3443-adc6-aad1c5b103d0 | -10.74798 | -60.77091 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 505c0fef-d59e-3eea-9523-d7afd04db25a | -10.74455 | -60.71319 | 2026-09-06 04:49:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 135105b5-77ae-345e-9537-47d8c91f3442 | -11.72728 | -54.57033 | 2026-09-06 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b959cd1-10bd-353b-994b-efec4a95434e | -13.76798 | -51.64819 | 2026-09-06 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 960065c3-c00e-3edc-99d6-a22f21466079 | -13.33374 | -54.05477 | 2026-09-06 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10e84e35-19d4-34f4-8400-3430332bb259 | -5.3646 | -56.0249 | 2026-09-06 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 739df296-648d-303d-b545-8a85b9950175 | -5.3645 | -56.0447 | 2026-09-06 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 2c868f43-3327-3056-975b-3dc898dcb691 | -10.7492 | -60.7097 | 2026-09-06 04:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| efd7c6aa-7713-3db7-8a40-942d5a7d1800 | -5.1423 | -56.2703 | 2026-09-06 04:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 706038f5-bdf0-3ffb-b159-2c76c50404a0 | -17.952 | -50.36323 | 2026-09-06 04:51:00 | NOAA-21 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c297593c-e678-3d7e-bb54-bc68e5f126e0 | -19.04503 | -56.69229 | 2026-09-06 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ea0fbfbb-07a0-3679-8f77-b439aad7b817 | -30.80733 | -52.81034 | 2026-09-06 04:53:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 048c374a-0ace-377b-8044-a90262012cf6 | -5.383 | -56.0242 | 2026-09-06 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d330db2f-2c46-3f9e-9b92-466de080815b | -5.3645 | -56.0447 | 2026-09-06 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 18356429-7b6f-3ea2-9aa4-c6cced0b7b4c | -5.1423 | -56.2703 | 2026-09-06 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1ba66dde-bd1b-3764-ae5b-0751a6788eb3 | -5.3646 | -56.0249 | 2026-09-06 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 8b48ce9e-45f0-3550-afbc-e75d9dba073d | -5.3645 | -56.0447 | 2026-09-06 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 1149044f-8e93-3516-b282-4e84f917eb46 | -5.3646 | -56.0249 | 2026-09-06 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 32405cff-78c3-3154-8097-df68bc396bc1 | -5.1423 | -56.2703 | 2026-09-06 05:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bd0e8a41-1ebf-3c73-8be7-6f2663cf4f39 | -5.3646 | -56.0249 | 2026-09-06 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 32e9d58a-6946-3968-9f63-d4b3d2ab95c8 | -5.3647 | -56.0051 | 2026-09-06 05:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b623ca15-9376-3052-abf9-78abf3241b72 | -10.7492 | -60.7097 | 2026-09-06 05:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8e3d90d3-afd4-3205-9140-bef160eb8578 | -2.29545 | -48.59298 | 2026-09-06 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| febd79de-946e-3fbb-862b-364edc5e4c19 | -1.86401 | -47.97939 | 2026-09-06 05:21:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 716e1eaa-ff33-381f-83df-343d5426d363 | -2.30124 | -48.58832 | 2026-09-06 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fad5706-00b6-33df-a375-6ff1e2fcce57 | -2.29606 | -48.59379 | 2026-09-06 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c68516a-a34a-347c-b15f-6901bd07d2ab | 3.22941 | -60.48751 | 2026-09-06 05:21:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d2eb57e-3043-3119-8a1b-79fd67241b49 | 4.20086 | -59.95641 | 2026-09-06 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8ba931b-5d84-3df0-9bf8-352d752d92d4 | -1.1999 | -47.76115 | 2026-09-06 05:21:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 120ac845-7600-3211-9a60-bc5f288226c0 | -2.2977 | -48.58288 | 2026-09-06 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea45258-3631-3ff2-bfa6-0fa9e191abd2 | -1.18627 | -53.82591 | 2026-09-06 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a78d12cd-4a5b-3c2f-8443-4e28f77f3394 | 0.83103 | -51.18063 | 2026-09-06 05:21:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8b7521a-ab4d-3722-a8f3-2cdde983c3ef | 0.86988 | -59.6799 | 2026-09-06 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2be7e3c5-dd60-3056-bb48-4a563382fda5 | 2.45088 | -50.77483 | 2026-09-06 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a9a94af9-043d-3d6a-9198-0221ef5fa2a6 | -1.2055 | -47.75898 | 2026-09-06 05:21:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dd6beb5c-898a-3a5a-a06b-35b7ce52df32 | 4.19735 | -59.9604 | 2026-09-06 05:21:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb5ff59d-d7e0-3833-a786-44387d8b3b59 | 2.38436 | -50.76487 | 2026-09-06 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df879ee5-2fad-3fb2-adb0-8a9dc845ccbf | -2.17292 | -48.80156 | 2026-09-06 05:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d732d4f2-b496-3cd8-b1c9-c010b9a8a7d7 | 4.36079 | -59.75103 | 2026-09-06 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 340b3340-e048-3b90-bc43-8b17908564f0 | 2.37957 | -50.76046 | 2026-09-06 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e78082f8-f15e-3907-961d-b402c511ecad | 2.30774 | -51.66521 | 2026-09-06 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fd0ec99-8da0-302a-82fe-00fe5a56d024 | -2.2963 | -48.58757 | 2026-09-06 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a61c39d0-a510-3112-9ca5-25c490ada708 | -1.20036 | -47.75816 | 2026-09-06 05:21:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 693e0e48-3524-30c5-99b4-d7b63480bcaa | -1.20503 | -47.76198 | 2026-09-06 05:21:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eeeffeb7-c0a1-3edc-a49b-0f318aeea026 | -1.42726 | -53.76059 | 2026-09-06 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9484d4bd-1f73-38b0-997a-2d64910522cc | -1.02214 | -53.72276 | 2026-09-06 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc192a28-bd38-3e3e-ae55-2fd9903b0c33 | 0.30466 | -60.44506 | 2026-09-06 05:21:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1117ad2-6480-31d3-a4ee-e568b24943df | 1.77221 | -56.08007 | 2026-09-06 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8dbde3b5-4105-30ce-9ea1-0cc02e6e7bbe | -1.86913 | -47.98018 | 2026-09-06 05:21:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d1d7174-1688-322a-849a-aea3f6a042b9 | 0.97714 | -59.38136 | 2026-09-06 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ba5ca5d-0a91-355d-b4a2-ad89f77f97d0 | 0.87365 | -59.67931 | 2026-09-06 05:21:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7470a4c6-e9cf-3243-b2e7-5db8d1683e2b | 2.30699 | -51.66065 | 2026-09-06 05:21:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e39eddf7-3028-3d6b-be7d-9667a683551b | -2.29687 | -48.58838 | 2026-09-06 05:21:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c7acd8f-db38-3396-90c2-09063aec730b | -1.18276 | -53.82542 | 2026-09-06 05:21:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55e3dbf2-da84-3dfd-96b7-1d765660f626 | -5.33272 | -56.02687 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6ae41aa-e958-3b12-b652-99c4ab85f972 | -5.98683 | -57.68781 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e98f8cb-96ff-3165-8693-0d7b9a13a03d | -4.92007 | -55.80989 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7beebe3f-e0c7-355d-97d7-966d1152177e | -5.13864 | -56.26849 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6445a454-f8fc-36a0-8caf-f32538b54c2c | -5.3674 | -56.0356 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a257b92f-3c3d-3e05-9fec-1666affefa8d | -6.07111 | -52.255 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cf5d9863-93e7-3d6a-a099-2b559f1214fc | -5.36008 | -56.01622 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86d83c44-1b8c-3cde-931e-4948d9ac1473 | -5.34393 | -56.02134 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78eac190-9a4b-353e-9624-dd8043840b97 | -2.86562 | -50.46227 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40167831-76e9-3b12-a4d6-0204a2dd61d8 | -3.12379 | -57.69196 | 2026-09-06 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 373966e2-74ff-3c6b-a517-c0004289eea7 | -6.06065 | -57.79548 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f764af82-677e-3678-b9e7-b2b784bf6a6e | -3.38029 | -59.41699 | 2026-09-06 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54019604-f310-3703-a6f0-9cff9f197c79 | -5.1459 | -55.95817 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 668c5fc4-821c-394c-b0fd-1789b1c599f8 | -1.26908 | -55.6637 | 2026-09-06 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
