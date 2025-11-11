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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6687b352-6786-38d1-9d04-c3201d9a1736 | -3.56867 | -45.83601 | 2025-11-11 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b49371e5-a08f-3c0b-a52a-30f0fb346ca2 | -2.11351 | -46.91485 | 2025-11-11 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9c8a80aa-8797-38a5-b117-3e0f0a2318ff | -3.41537 | -44.08715 | 2025-11-11 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d57f428-0a28-337d-a17d-45946a481180 | -3.78497 | -47.75103 | 2025-11-11 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f1e8437a-5c96-319c-bcd1-2064a7e0c753 | -2.94982 | -45.16607 | 2025-11-11 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 7882eda0-9077-32ab-82fb-479c7b25140d | -2.44497 | -46.30562 | 2025-11-11 00:15:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54073c93-ab68-3c41-8ddd-97e2b5a373a7 | -2.87606 | -45.42769 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 056d1bb2-2982-3319-9bca-9ba622cf8137 | -3.64905 | -45.89644 | 2025-11-11 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70c73d55-876f-3fce-b4f2-ea5a0460405c | -2.66212 | -45.42205 | 2025-11-11 00:15:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dde5e9ac-85fd-304c-bed2-63e4bce47790 | -0.91211 | -47.55352 | 2025-11-11 00:15:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a28044f2-0b92-3dbd-8d40-056342a243ad | -3.09386 | -49.27708 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 801839f3-c6d6-3798-82a2-2a529427ddc0 | -3.89114 | -47.1815 | 2025-11-11 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 80794dcd-fbbd-312d-b7e7-bf93f5d70e8d | -2.64562 | -49.21074 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ca012388-8f0e-39ef-85e6-c1a684d7f680 | -3.78632 | -47.76092 | 2025-11-11 00:15:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| fd0828d5-215f-3416-9580-4eb820c405f7 | -3.49093 | -46.28111 | 2025-11-11 00:15:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1792c3d1-5a0f-3028-a586-1fc2eed04295 | -3.41674 | -44.09676 | 2025-11-11 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d9e74fea-4c46-39d7-bfad-14cda6c0a86e | -1.64179 | -52.04951 | 2025-11-11 00:15:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 71d99a1c-054b-3265-bc25-901c39ba3964 | -2.81037 | -45.48833 | 2025-11-11 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f02c6fe7-f8a2-38d6-9e46-cbf38e6f6968 | -3.43214 | -42.423 | 2025-11-11 00:15:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f569893c-4801-3a4a-aaa0-4f5a7cec87da | -2.31343 | -47.09422 | 2025-11-11 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b7e4fc40-74c7-32b9-b7e1-7c62d30f3468 | -3.49803 | -45.86077 | 2025-11-11 00:15:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 46601849-575c-3eb5-bfba-e98420c048b4 | -3.43243 | -44.07495 | 2025-11-11 00:15:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4f48fa3e-0fa5-3166-9990-95a1f0e69203 | -1.64532 | -52.04353 | 2025-11-11 00:15:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| d6983807-c0d2-3244-bebf-ed500e495e36 | -4.2552 | -48.57428 | 2025-11-11 00:15:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 801955b9-f64d-31b3-888a-38b35e63eb6c | -2.71545 | -47.4052 | 2025-11-11 00:15:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 79f6ac0b-5a05-33a4-a3c7-51493faf8311 | -3.49215 | -46.28995 | 2025-11-11 00:15:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a07d48b5-5d86-39a8-a799-7fd47d0f98f5 | -2.93966 | -45.15838 | 2025-11-11 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 86eb409c-e343-3dda-b695-4616aaa2e11e | -3.23906 | -50.05954 | 2025-11-11 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a368ee59-274b-366e-97d4-10549c396746 | -3.60558 | -42.85962 | 2025-11-11 00:15:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 194e9143-e5bd-3ff4-9eb3-b8ccf1b1b7fa | -3.45288 | -45.53509 | 2025-11-11 00:15:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b81444dc-82d1-3856-a06d-2fa2c602326e | -2.65712 | -49.22077 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 67b21770-a0f7-301f-ae2c-10c3a8ac484c | -2.14891 | -47.37037 | 2025-11-11 00:15:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 61c2113d-e4bd-3c0b-a51e-4618c7e9fe34 | -2.62439 | -49.20848 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| a85d4e50-2edf-391f-8a11-2f095b8f2ea9 | -2.86595 | -45.42006 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b451b1e8-a7c8-3093-abcd-2f3eba7135c5 | -2.31218 | -47.08517 | 2025-11-11 00:15:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aa483911-767b-30b1-ac00-2da3a9f9daf9 | -2.83695 | -45.48459 | 2025-11-11 00:15:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cce0f27d-2860-3bf8-a9aa-1a7a56943331 | -3.69285 | -50.18718 | 2025-11-11 00:15:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d0822ccb-61e6-3087-a8b1-b757b09b18c6 | -2.92091 | -45.29449 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 9638b755-7787-3bd1-a11e-9e610d57485c | -2.63593 | -49.21846 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 01e05ab4-66b7-3af3-abf8-160e67b74c6b | -2.85619 | -45.42767 | 2025-11-11 00:15:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 114a6bb2-7d3e-3faa-9e0d-052fad781ffd | -2.27059 | -47.84854 | 2025-11-11 00:15:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0abcea1f-09b0-3f10-8d2d-a4f42dbfc047 | -2.94857 | -45.15712 | 2025-11-11 00:15:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 4ebd7f57-0849-3604-8c9e-1bc840fcb629 | -3.1411 | -45.28152 | 2025-11-11 00:15:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00bbf07c-137a-368e-aa96-39f0879de81b | -3.48685 | -54.0327 | 2025-11-11 00:15:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 50311820-0f76-3c6e-8773-1af24f5a12f0 | -2.15476 | -50.70546 | 2025-11-11 00:15:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 135e03d1-ab10-3345-9b22-b3dccdfd1f91 | -2.64714 | -49.22213 | 2025-11-11 00:15:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 84aff9ad-8c47-36f7-bef6-fc77c369a291 | 0.54 | -50.76247 | 2025-11-11 00:17:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c8e0b60b-1323-3f9a-8934-0d5d17fa8410 | 3.53219 | -51.78029 | 2025-11-11 00:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e3e2d9d5-4466-322e-aadd-f3e99d1737af | 3.53039 | -51.77422 | 2025-11-11 00:17:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6d542a42-7408-38b1-891e-622e96f0be8a | 0.53566 | -50.75597 | 2025-11-11 00:17:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 144e9fab-ff09-36c8-94b9-a3b61f54bbca | -2.9232 | -45.3037 | 2025-11-11 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 816c3dc3-e32f-3019-8590-4dd46e3d5fc0 | -3.9554 | -43.7773 | 2025-11-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| d603934d-24c7-3a13-8b2d-fda431ccf75c | -4.9036 | -44.3208 | 2025-11-11 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 513cc591-a867-383e-86df-be3e0571e010 | -19.7223 | -58.0491 | 2025-11-11 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 9b14c441-aa09-3bdc-bbf0-9d53180d0aa0 | -3.9552 | -43.8004 | 2025-11-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 42c61ed1-58de-3a08-a9ea-d7d1d19d323e | -2.9233 | -45.2812 | 2025-11-11 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 527c0d04-4256-3310-a24f-075ee62520a3 | -2.8669 | -45.4406 | 2025-11-11 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 17ffbad5-937a-352c-9fd9-d1170c922c6b | -2.9413 | -45.4155 | 2025-11-11 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| f5c7f55b-42ad-30c6-808e-b68955c56057 | -2.8854 | -45.44 | 2025-11-11 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a8bea7c4-0d3b-3e8c-90f5-c3c454dac833 | -3.9555 | -43.7542 | 2025-11-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| a397072a-4ff9-35ea-a123-a4b2b8e755a8 | -19.7219 | -58.0699 | 2025-11-11 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.0 |
| 1927bc58-2f62-32fb-b08d-5c08ba433e86 | -3.974 | -43.7763 | 2025-11-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1248143d-acfd-31a9-a726-fae081b0cc30 | -3.7837 | -47.7677 | 2025-11-11 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| f7f03877-1f4f-3a0f-a39f-0a07e3faebf9 | -2.8855 | -45.4175 | 2025-11-11 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 306d6f3d-8d99-31d9-8475-d94d38c7ea06 | -4.9034 | -44.3437 | 2025-11-11 00:20:00 | GOES-19 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 688bae70-df4b-36f0-8747-a37f73701056 | -19.7424 | -58.0465 | 2025-11-11 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| ec2b90d0-cf97-381a-b004-4336aac7bcd7 | -4.7204 | -46.4497 | 2025-11-11 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 4ffc4c2c-3e54-3333-a20f-d193608dc3e1 | -9.9828 | -44.4581 | 2025-11-11 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 2245e17c-cdb2-3c42-8eab-97c5a693decc | -2.867 | -45.4182 | 2025-11-11 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| c6df81d5-82c7-3397-9683-3b53e6e8ba55 | -10.4885 | -44.9465 | 2025-11-11 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c0e891da-12d4-34df-9c53-38d00307b555 | -3.9739 | -43.7994 | 2025-11-11 00:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 292fd525-997c-300e-8218-0d153f40c9dc | -19.742 | -58.0672 | 2025-11-11 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 271120a6-e571-3700-a80a-6cd45961d170 | -10.5076 | -44.944 | 2025-11-11 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8cfcc2fb-8e68-359a-9044-19c173137af5 | -10.4885 | -44.9465 | 2025-11-11 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 6ab02eb2-1eed-34ba-a533-ea53bfbaab8f | -2.9227 | -45.4162 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c7723afe-bb16-3c7b-b188-ab7431d8269f | -2.9228 | -45.3937 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 07ab3612-c79e-3e85-8629-845e42481a8b | -10.5076 | -44.944 | 2025-11-11 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 590c85c2-f557-3c85-8685-03d88cc59d0e | -3.9552 | -43.8004 | 2025-11-11 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 1aa44bff-b8bf-3391-9c4d-487894c92d43 | -2.8484 | -45.4188 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d9d73179-958f-3fbe-9f02-8ef72d84c8af | -19.7223 | -58.0491 | 2025-11-11 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| a26bc55f-6efa-3ba2-8b61-512b0401d063 | -3.9554 | -43.7773 | 2025-11-11 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| c6fbd6bf-5069-310d-8536-268c444ecd46 | -2.8854 | -45.44 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 113.1 |
| f8927455-1a78-3428-acbf-0b7243824cfd | -3.974 | -43.7763 | 2025-11-11 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 523f0147-854f-3467-9961-f18f5997e9b0 | -2.9414 | -45.393 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0bbdde7b-5e0b-3ebb-ad8c-d7c30cb9806c | -9.5534 | -40.3254 | 2025-11-11 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.0 |
| c9558f4f-e439-3353-80c7-6cfa0828df52 | -2.8855 | -45.4175 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 935c18ce-85fb-35c3-bea0-bcd87082050f | -3.9555 | -43.7542 | 2025-11-11 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| f04ed960-fe09-3f96-ad94-ab1d464a5f63 | -19.742 | -58.0672 | 2025-11-11 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.5 |
| b8f30e61-e391-3f7f-be11-a1a77157b895 | -2.867 | -45.4182 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 234.7 |
| 9a85b233-ed75-3726-b289-e87056b5d989 | -5.6436 | -41.0629 | 2025-11-11 00:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 0616127a-c4fa-3046-a24e-d886b4188eca | -19.7424 | -58.0465 | 2025-11-11 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| ab30eab6-fb33-347f-9a35-dc612a5e4d24 | -2.9413 | -45.4155 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| edaa56cd-e4b8-36c2-ab0c-03281c3e2c78 | -4.7204 | -46.4497 | 2025-11-11 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 6e4cc3c2-6735-397f-8103-d34d3a262116 | -19.7219 | -58.0699 | 2025-11-11 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 9ae00c0f-695f-3d61-ad1d-7d1781a485b1 | -2.8669 | -45.4406 | 2025-11-11 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 1174955f-1eb8-3c41-a537-ec5b9e90832f | -2.9414 | -45.393 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 81da2626-bb78-3543-a0b6-fe2057868faa | -3.9554 | -43.7773 | 2025-11-11 00:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 52635ad9-5bab-3ff5-8856-1bc208c02ac0 | -4.5862 | -44.3172 | 2025-11-11 00:40:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| d072bde9-5586-3531-8ff9-58aa85447c87 | -5.6436 | -41.0629 | 2025-11-11 00:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 10b98ba9-9b67-3cbf-a9b5-9b2e1ee5d64d | -2.9228 | -45.3937 | 2025-11-11 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |


[Clique aqui para ver as próximas entradas](README6.md)
