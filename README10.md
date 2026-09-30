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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e9d8524-cb67-3d81-857c-a7046dcdd5bd | -3.23143 | -46.94844 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1070ba8a-681f-3c64-a691-5a45b56d5c19 | -3.10712 | -50.28456 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9137cd46-7426-3989-b26a-6f44e2c24435 | -0.48192 | -49.13171 | 2026-09-30 03:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312da917-0175-34a7-8400-e12a3bbbf32f | -2.73442 | -49.41827 | 2026-09-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 604fea84-62df-36af-90b3-ed49cc0645ba | -3.74927 | -46.1387 | 2026-09-30 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8b89645-294f-3d39-8d2c-1839e6174d8d | -0.66995 | -49.25033 | 2026-09-30 03:53:00 | NOAA-21 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c528dd9d-3786-367e-a8e9-9c8adb8e7731 | -2.99114 | -51.03365 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d43e644-7169-37b2-a94a-33de9ca751ad | -3.2278 | -46.93763 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e04cf2e6-bb62-3456-a72f-2c69f9534a94 | -3.22197 | -46.93981 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d135fb01-57a5-36b6-862c-a672fe5f901c | -3.41879 | -48.33723 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92ed8015-d1ec-330b-aee3-bf050e5296d1 | -2.98892 | -51.04648 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 84a145b7-d37f-3646-a523-b1fb31a30e82 | -2.97845 | -51.02507 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 08d16d4d-f7a3-3473-a3c2-f724042c7dcf | -2.97854 | -51.02437 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6bc60e90-6e5f-383d-b4e0-9f257182f518 | -3.24976 | -50.11849 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 94391185-a7f1-388f-922d-64e26ad515ce | -2.37746 | -47.60669 | 2026-09-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e10fb88f-6f7f-3aa3-9208-e90490e29e02 | -3.22246 | -46.94597 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2080636-07ac-3a8d-b0e9-e6bcf3545491 | -3.22252 | -46.93656 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f5b84d07-07a3-311b-b0d2-e7b10a8b3303 | -2.98222 | -51.04475 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4370a132-a7b7-3275-8c33-64d9e55b2bdf | -3.10152 | -50.27784 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 781688f4-24f0-388f-80ba-0a52cace5b90 | -3.23953 | -46.93284 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6773044e-b571-3bc1-84a7-9bd97edb169a | -2.9682 | -51.04314 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 61dcc557-f776-384d-8330-ccc3b3f297af | -3.80774 | -42.55506 | 2026-09-30 03:53:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82df6e69-e7ff-31f7-b365-12b45d3ff899 | -2.97955 | -51.01874 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 406b44f7-d284-3ff7-9735-dd938e9e1daf | -3.183 | -51.2375 | 2026-09-30 03:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b70069a2-ad08-3bda-bdfd-48cb89f902c3 | -3.22669 | -46.94418 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68a2cea6-dfd5-33c4-90dc-f473e912e2b7 | -2.9695 | -51.03602 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ec8bab84-5b5b-3d20-92dd-e9991d207367 | -3.23519 | -46.93481 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2edf6de5-dd0d-33b8-96d1-159a01297209 | -2.97057 | -51.02963 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 36fdb9c1-0897-3ae4-ac47-0eabec171e52 | -3.23087 | -46.95173 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cedc40cf-b06c-307b-92c4-3d50339503db | -1.59637 | -45.81281 | 2026-09-30 03:53:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35e879db-7cd8-3568-954f-125cd268286f | -3.23366 | -46.93527 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0acb0a2a-e41a-3064-981a-3c776a2379f4 | -3.41875 | -48.33833 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d313a6a3-a37e-39a4-87d0-b114b8d2e6f4 | -2.38374 | -47.60369 | 2026-09-30 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87ddb111-42da-3fd9-b2bc-ae4591afb174 | -2.99004 | -51.04003 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b2a0e538-da36-3aa4-8bdc-e8a33c5c0aa0 | -2.96842 | -51.04245 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7f1fe19a-4574-3e59-87f4-ab5264ea9ad4 | -2.97641 | -51.03713 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 32f28e9a-ba78-3bce-9090-f60bd49d3007 | -8.72296 | -47.59184 | 2026-09-30 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8684b671-3d02-3670-b178-0fa82f71bb7c | -8.98076 | -44.17717 | 2026-09-30 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9489fbd0-ac01-35aa-bfbe-12147b3976ac | -10.7121 | -50.84302 | 2026-09-30 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fc15082-5ca1-3d81-852d-c20530387c29 | -11.16071 | -44.76992 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e522520d-172c-3e73-b30c-6825b040310d | -9.66375 | -45.12499 | 2026-09-30 03:55:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f6c1aa0-e480-3558-b611-82ac23baed49 | -10.28695 | -44.61894 | 2026-09-30 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b02eb4-f14d-359e-b3d5-ac73067e0de2 | -11.35182 | -43.35263 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1726efa4-1925-33f4-a7d7-e9248b3a1ed4 | -7.01186 | -45.30288 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aa966dc5-c2dd-3937-b4be-c6b270a12a4a | -7.54216 | -47.1222 | 2026-09-30 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 091a2ad7-fc33-3bf4-ae0b-2595f47c3634 | -6.96287 | -40.33992 | 2026-09-30 03:55:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cc2ee4df-2ab6-37cc-a13f-d59608396fda | -6.41602 | -43.46428 | 2026-09-30 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 155d611e-820a-3814-8f1a-357f21c48fe8 | -9.01099 | -40.9994 | 2026-09-30 03:55:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| db55f60e-64e0-39df-9c89-e912763f95c2 | -10.70697 | -50.8372 | 2026-09-30 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 599c47e6-0d69-30d6-8be1-995a995a1b80 | -5.03103 | -43.56865 | 2026-09-30 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bae4255d-fa64-35ea-98c2-f89d98703cf7 | -8.34824 | -45.9813 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 619874f7-7d9a-3a5d-8ccf-ffca0375b05e | -8.33476 | -44.16341 | 2026-09-30 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce3cbb54-b445-387f-9a7b-0dc6462df48d | -6.30402 | -43.60635 | 2026-09-30 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e480f0eb-4d1f-32bf-908c-6a0da35d86c1 | -7.51377 | -45.09247 | 2026-09-30 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f5fe2d6-587c-33b6-a4dd-e8b8b3669acb | -7.84799 | -45.82045 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 805d373a-0a6a-3f61-b924-a75b34d252c2 | -11.40931 | -43.4175 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 17d1be67-03eb-3d9c-9bf8-4d46a25a0946 | -6.28882 | -43.6475 | 2026-09-30 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afd95933-456a-3b15-863a-ef3fba8d92c8 | -5.97643 | -46.60859 | 2026-09-30 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b46e744-8b65-342a-9a66-479603215903 | -11.42922 | -43.49292 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7e22116-779a-3cd6-9351-684c49191ef4 | -9.86505 | -44.94713 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23094c78-7156-3840-8a62-c8ad4a1841c3 | -11.39015 | -43.37296 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96542ed3-785a-3002-81bc-344e967f903c | -11.16351 | -44.77776 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0280daf6-156e-3039-8237-cf9d6314c2bb | -11.18817 | -45.11873 | 2026-09-30 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a97e023f-a213-3b88-9196-738fbb55c60b | -11.43255 | -43.42894 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0e64ee6-45a8-37dc-8c56-5cebc16d9fb7 | -10.7131 | -47.83004 | 2026-09-30 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02fff34e-15e4-36d3-8d95-719512c43a42 | -10.78317 | -47.25481 | 2026-09-30 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 15e21342-4b7b-38e0-8ea9-d2b677ae2891 | -5.74249 | -45.16471 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef2f17e3-9c41-3c3d-a77e-38cbdc612cb8 | -11.2575 | -43.53651 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb1f94cf-792f-3f7c-9b9f-7bd158ad3eb4 | -6.33243 | -51.16283 | 2026-09-30 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 761255a8-faa3-39fc-985a-30e570b3e9a3 | -11.17962 | -44.78055 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f5eb65e-16f7-349c-b7d5-1c9369b269d3 | -11.35258 | -43.34819 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb98e8da-bed7-3c71-b2ae-f131a9d4d096 | -7.49703 | -45.80186 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ffedd49-bfbf-37a1-964c-16455f9845b1 | -4.29788 | -48.61041 | 2026-09-30 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7322d0ea-52c5-31f0-9575-08881bc52eb9 | -10.90291 | -43.85859 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e1803c3-ddaa-304e-a533-f783e67e9f33 | -11.16534 | -44.76708 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b091adae-d84b-3469-a304-6a85b4c1d3e7 | -10.89919 | -43.86442 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76fbe6a9-79b4-3f27-b399-e94153f3fa6b | -11.67941 | -43.50537 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 654c2ec1-89a9-3917-a159-254df1c76112 | -10.72333 | -44.42446 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6edd437b-af53-3b35-babc-2364efa58590 | -7.8335 | -45.81917 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7a77dcef-aeb7-346b-8812-b8f5b01f7279 | -7.84627 | -45.83015 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 4f6e8b36-5871-3de6-b4ad-64827f1a28aa | -9.76977 | -44.82155 | 2026-09-30 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b681553d-f601-3b82-92a0-cc86e4a036c4 | -5.09649 | -46.0412 | 2026-09-30 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bad46ca4-eadc-3b49-aa03-8c2e35b2f8cc | -4.81344 | -46.84932 | 2026-09-30 03:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c631ea11-bf55-3777-9192-1be652156c10 | -7.01262 | -45.2984 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4f5b400-4d7f-34c7-95f4-3980ca946b99 | -11.17224 | -44.82379 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 9c8b7053-b055-3888-9ea3-de2fe4065a46 | -7.82809 | -45.8233 | 2026-09-30 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7aaf8c1d-0c9b-3221-ad65-e280a6e73105 | -7.00663 | -45.30654 | 2026-09-30 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 194bf324-4a20-39cc-a08b-edfe98626b6f | -10.71299 | -50.83841 | 2026-09-30 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebf9def0-394d-3383-a90f-395775227538 | -11.39663 | -43.47066 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6ce16f21-e6ae-32fa-bdff-ca97143a0cf4 | -6.32808 | -51.16017 | 2026-09-30 03:55:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 98064b6e-90f5-3a8c-9263-a969d7f79450 | -9.09797 | -47.16405 | 2026-09-30 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60263449-090b-3694-a92a-33f510a2a8f9 | -5.72969 | -43.51231 | 2026-09-30 03:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4688d7d5-0fba-3abe-8cca-2067db65af46 | -11.17559 | -44.77987 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bb62986-c4d4-3132-b6e3-154d75f1b8cf | -5.74659 | -45.05819 | 2026-09-30 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5e16c83-c8d2-3df2-98ac-7aec238fa56d | -9.8241 | -48.22119 | 2026-09-30 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 493c0458-559c-3f0b-8e2e-da5f7aeac6fd | -11.43842 | -43.43916 | 2026-09-30 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4ddae2a-ec56-3ef7-a41c-33140c2d66f7 | -11.16946 | -44.81576 | 2026-09-30 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| fdd7cd38-c42e-32d0-8381-46bdd539edfe | -9.92384 | -50.22613 | 2026-09-30 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 99b80b0e-bec6-3089-a4d0-8676fb0ced2b | -8.98476 | -44.17794 | 2026-09-30 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70d7b7ae-9e67-371c-9f43-2286bf806185 | -7.08239 | -41.73698 | 2026-09-30 03:55:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README11.md)
