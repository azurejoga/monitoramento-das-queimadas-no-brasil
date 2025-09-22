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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d9ca0a3-a96c-3167-a548-791ba952293b | -22.2857 | -54.9191 | 2025-09-22 00:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 113.8 |
| c9f57186-ace0-38f7-b42d-5201870edfb3 | -11.6436 | -52.8605 | 2025-09-22 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 2c158a82-830f-3cdf-8455-b603118a9722 | -10.4129 | -46.142 | 2025-09-22 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1460b2d0-4e06-3c2d-947d-b4aaa6a608bc | -20.2533 | -55.5172 | 2025-09-22 00:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 135.0 |
| ae2e0ebd-4dde-3095-9871-1d17466904db | -20.274 | -55.4927 | 2025-09-22 00:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 335.3 |
| b69c88a3-2d3a-3de6-8488-fcd1cbd92060 | -21.1683 | -48.8425 | 2025-09-22 00:00:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 106.5 |
| adc66779-915b-3f48-9a7d-d134d618644f | -11.6249 | -52.8416 | 2025-09-22 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 6536c068-2f9d-3cd7-95a1-fc620a4f1a90 | -20.2735 | -55.5141 | 2025-09-22 00:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 6601734e-7413-3e8a-b1a4-521ca07ea3b7 | -11.6247 | -52.8624 | 2025-09-22 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 61ff17f6-997f-32af-9d08-2582310af6bd | -7.4291 | -46.39 | 2025-09-22 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 92d5892e-224e-3ad4-89fa-a1c8d92154c5 | -4.3012 | -48.0917 | 2025-09-22 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 04b1a454-970d-34d8-a301-b4894a5126a0 | -19.6274 | -57.7504 | 2025-09-22 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.8 |
| c4ef83d7-a84d-39d3-99f2-3b4ac9a975b9 | -20.2537 | -55.4959 | 2025-09-22 00:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 214586f8-7b7b-3fcd-b46c-00df78b17197 | -19.6679 | -57.7243 | 2025-09-22 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 910dc159-fc1c-34b5-9094-9d336f978d29 | -4.3197 | -48.0908 | 2025-09-22 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| c0dc4cd0-83a8-3610-8944-e538a27e3a80 | -11.322 | -54.3359 | 2025-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| a4951c58-458a-37d7-90f7-05b6cb01186d | -19.6278 | -57.7296 | 2025-09-22 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 4ca3e3cc-6e0d-3977-b014-2e1771bec1ac | -11.3406 | -54.3547 | 2025-09-22 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 12d98d20-4de8-394f-9639-11cb7a2820d5 | -11.6439 | -52.8397 | 2025-09-22 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 6d350e8f-3014-39ed-bd52-61d700f13c7a | -10.4447 | -61.3434 | 2025-09-22 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0bc22b05-21d2-3d14-8589-2a808cb3d4c3 | -18.399 | -42.8644 | 2025-09-22 00:00:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.7 |
| 8fa4aa7c-04cf-3cc5-972a-bf8659795c6a | -22.9255 | -48.1819 | 2025-09-22 00:00:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 06ec6803-aa6b-37aa-a612-24c3f578fb5a | -19.6482 | -57.7061 | 2025-09-22 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.4 |
| b354c816-aadb-3fc9-be48-4815ebca6469 | -4.3196 | -48.1125 | 2025-09-22 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3542f91d-1d4e-3dce-aef4-4735113d6f30 | -11.3217 | -54.3564 | 2025-09-22 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 6a129333-78d3-38d6-acf2-42998329fac5 | -21.1896 | -48.8145 | 2025-09-22 00:00:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.9 |
| 9140bc24-bd15-3cc4-939c-f230e8207f94 | -7.6596 | -61.1297 | 2025-09-22 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 5b720102-e912-32c3-b43e-5780cd3de62a | -19.6478 | -57.727 | 2025-09-22 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 53045a13-28bf-3d19-80a8-f48399fefb63 | -10.4132 | -46.1194 | 2025-09-22 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0c1a564a-0bec-3ab8-9477-7fbd885496e7 | -21.1889 | -48.8377 | 2025-09-22 00:00:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 160.8 |
| 77f47f0b-e33e-3fbd-bb5e-9b1ece779337 | -19.6475 | -57.7478 | 2025-09-22 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| f10eb5c1-f829-3f48-9c46-be5a6da88296 | -21.1676 | -48.8657 | 2025-09-22 00:00:00 | GOES-19 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.7 |
| aab54d24-db27-3bf0-ab54-98dc7c72f4f2 | -21.8351 | -53.9546 | 2025-09-22 00:00:00 | GOES-19 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 109.9 |
| f3a93eca-d8af-3469-b912-1f8c911929bb | -21.2102 | -48.8098 | 2025-09-22 00:00:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.9 |
| f2e1cba3-8766-3bc9-9187-f338686cbb14 | -21.2095 | -48.833 | 2025-09-22 00:00:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| 6859f701-6ae5-3419-a9b8-890b326c391d | -22.265 | -54.9228 | 2025-09-22 00:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 9c7b100a-3dd1-323a-aea6-386c86dfae1d | -7.8068 | -46.1772 | 2025-09-22 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2ee93001-24ac-363d-939c-d2501461d581 | -4.3198 | -48.0692 | 2025-09-22 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 947d4b70-55c7-30ad-9e56-7163002b8b66 | -19.88275 | -42.45737 | 2025-09-22 00:09:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.0 |
| 8acdb9e4-4c75-3b06-91f6-79e10414e31c | -17.51925 | -40.15472 | 2025-09-22 00:09:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 511a05af-6c90-3468-84d2-763e9dea9622 | -18.11031 | -44.26691 | 2025-09-22 00:09:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c1ebdf76-5f01-3ae3-a0d6-53c6b46b8917 | -15.53695 | -44.32101 | 2025-09-22 00:09:00 | TERRA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 12.7 |
| f23669c2-9c93-3467-929c-c7634bda1362 | -20.51676 | -43.96026 | 2025-09-22 00:09:00 | TERRA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 570ef960-652c-3378-bdf1-ec0101f5033f | -16.39574 | -42.25443 | 2025-09-22 00:09:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 71d99b12-219f-3c20-a30a-39d1715271d7 | -19.85091 | -42.21333 | 2025-09-22 00:09:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 5eb87eca-c4d8-36e2-8fc8-904bfa4fcffe | -18.10064 | -44.26829 | 2025-09-22 00:09:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 56165051-1571-3814-b884-02bd7adf6722 | -19.30587 | -42.68478 | 2025-09-22 00:09:00 | TERRA_M-M | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cc0ceb82-4d14-3ecd-9402-51616844f091 | -17.97853 | -43.08091 | 2025-09-22 00:09:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| e894ccd9-8129-3397-84eb-5fa62a7ebf42 | -19.58348 | -41.65479 | 2025-09-22 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ac274854-ffe3-3fbc-a921-a004ae302283 | -20.18988 | -44.6198 | 2025-09-22 00:09:00 | TERRA_M-M | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bf024bde-195c-3862-b123-20cefb5f7d97 | -18.54607 | -43.84806 | 2025-09-22 00:09:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c5f55fc9-7691-3d7d-88ca-a9319d4d4646 | -17.13961 | -45.91722 | 2025-09-22 00:09:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 946e6740-8e4e-3a8d-9b64-02f4dc78db16 | -17.0577 | -44.90391 | 2025-09-22 00:09:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 46c6383b-1b4e-39ea-b961-3dc3d8763d51 | -20.50338 | -42.21066 | 2025-09-22 00:09:00 | TERRA_M-M | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| eb8eb7e9-17e8-3ee7-8c40-e6fa2c52a417 | -21.17277 | -48.85008 | 2025-09-22 00:09:00 | TERRA_M-M | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.8 |
| 57ad0bdb-ba8a-3989-bfeb-0c692779f8bd | -20.12624 | -42.48955 | 2025-09-22 00:09:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| d3fe2ff9-d1a3-33b5-a5c5-39b2caa838e7 | -21.19872 | -48.82061 | 2025-09-22 00:09:00 | TERRA_M-M | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.8 |
| ec209e50-7b69-3ed5-99ab-c7078d7e62ec | -19.88404 | -42.46735 | 2025-09-22 00:09:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8376e8a3-c848-3270-ba15-a9a80be6d977 | -19.875 | -42.4688 | 2025-09-22 00:09:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 58382b40-d147-3b82-97c4-fa2fc2021f2b | -17.08526 | -42.86131 | 2025-09-22 00:09:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c109ad88-10b7-316a-bedb-38095216beb4 | -17.08399 | -42.85165 | 2025-09-22 00:09:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 081dca2d-2cdd-3c08-962d-683988c3a9e5 | -20.0417 | -44.06796 | 2025-09-22 00:09:00 | TERRA_M-M | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| fd7dfb33-32bc-3643-b547-7091fba13df7 | -17.10602 | -45.90788 | 2025-09-22 00:09:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 13343ca3-b969-3dea-bd36-ba93debaf1fc | -21.17468 | -48.71762 | 2025-09-22 00:09:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 49ab0798-312f-349c-9cc0-b42499513eff | -18.84621 | -42.19732 | 2025-09-22 00:09:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 8fa8efbc-4ff3-33d9-a34c-137b5c8c6f42 | -19.59986 | -42.97039 | 2025-09-22 00:09:00 | TERRA_M-M | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e60362b1-5352-3f78-8bbb-2a33ebd56aa9 | -19.70415 | -42.08047 | 2025-09-22 00:09:00 | TERRA_M-M | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 9d0d9b0b-ad6c-3752-85ff-ccae67828982 | -21.14433 | -48.85342 | 2025-09-22 00:09:00 | TERRA_M-M | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| c1202d67-5dc2-3670-a27b-38cfd1028a35 | -20.50694 | -43.96139 | 2025-09-22 00:09:00 | TERRA_M-M | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 26cf48fa-79e7-3734-bcc0-bf001312c782 | -18.40131 | -42.86883 | 2025-09-22 00:09:00 | TERRA_M-M | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 381f8405-c7f2-3e82-ae93-051a7f7f2b1c | -16.07128 | -43.47426 | 2025-09-22 00:09:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 84139fe1-ac54-31d9-8824-c988549f2f9c | -20.6701 | -42.28986 | 2025-09-22 00:09:00 | TERRA_M-M | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 8dcc08ef-2748-3599-9950-6dd3270bfed6 | -18.84749 | -42.20695 | 2025-09-22 00:09:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 90a056f5-e1ac-347f-8be1-137dfaed8284 | -17.05766 | -44.90964 | 2025-09-22 00:09:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ae7179c-c9c4-300e-b16d-99fb82c37aff | -15.56923 | -44.42346 | 2025-09-22 00:09:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 15.9 |
| ea375015-9847-3638-9913-e53b05d01c71 | -21.0979 | -43.12457 | 2025-09-22 00:09:00 | TERRA_M-M | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| f8e70da1-1d05-3c10-9d67-fd24bf6a7eed | -21.3389 | -48.68849 | 2025-09-22 00:09:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 234e1daf-6002-33fe-8cf5-369dadd973b1 | -17.52065 | -40.16439 | 2025-09-22 00:09:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 74ea39dd-e711-3998-98dc-12ab8d4b6bd3 | -17.16594 | -45.95578 | 2025-09-22 00:09:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a3a5aaba-9951-3c04-97ca-61a43372011f | -19.84964 | -42.20366 | 2025-09-22 00:09:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2558b6e9-8844-3cf3-8b9e-b4b558dd327a | -21.00703 | -43.36535 | 2025-09-22 00:09:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 4954c729-6957-39a7-8e66-5ddc015b69b5 | -18.84494 | -42.18775 | 2025-09-22 00:09:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.2 |
| ee31dac8-c4cb-3467-aa8c-0dacd760d9da | -21.00567 | -43.35419 | 2025-09-22 00:09:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| b685d934-6156-3fc8-bb9b-c30a99c135e3 | -21.14061 | -48.85902 | 2025-09-22 00:09:00 | TERRA_M-M | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| d09f17af-ccc0-30a5-9651-aa7a0fc7ccd1 | -17.55937 | -44.92668 | 2025-09-22 00:09:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7b5899e8-4765-3a50-aea5-7b14086af772 | -20.62613 | -41.19835 | 2025-09-22 00:09:00 | TERRA_M-M | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| bd22066f-d426-3f69-b53e-d8b75f328410 | -19.1376 | -42.66266 | 2025-09-22 00:09:00 | TERRA_M-M | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 03b7f854-3d48-39af-93ec-78de38eb50f4 | -18.83604 | -42.1893 | 2025-09-22 00:09:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| c4f7b021-bbba-367c-8df2-073c60c71d9a | -19.87372 | -42.45888 | 2025-09-22 00:09:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 3f29baa0-e13b-38ff-9c2a-6928e3fbfbad | -21.20128 | -48.84757 | 2025-09-22 00:09:00 | TERRA_M-M | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 8d894124-e6cf-3241-bd1b-cbd829c36067 | -19.57264 | -41.65281 | 2025-09-22 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 8959ba56-fcea-3406-a8a2-a13df9ab21d5 | -19.57392 | -41.66218 | 2025-09-22 00:09:00 | TERRA_M-M | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 2b018d33-ac8b-3ebe-bedd-b40408a3b5bf | -19.70287 | -42.07087 | 2025-09-22 00:09:00 | TERRA_M-M | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d817c438-0c0d-31a1-b891-6afd21f5049a | -18.40001 | -42.85895 | 2025-09-22 00:09:00 | TERRA_M-M | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 146.0 |
| f990ca6b-4988-38f1-9474-90fdfc70a266 | -18.39872 | -42.84907 | 2025-09-22 00:09:00 | TERRA_M-M | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9042e293-6c67-3a54-8f9e-243a7b0e3def | -11.6439 | -52.8397 | 2025-09-22 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| ea3b5f5a-07b0-32ac-8a3a-1e392da9b35b | -7.4291 | -46.39 | 2025-09-22 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| f8ab401b-0136-35f8-8c0a-58af6d68747a | -22.9247 | -48.2057 | 2025-09-22 00:10:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 61bf57e9-9629-365c-bcb5-b115f006808f | -22.2857 | -54.9191 | 2025-09-22 00:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 5f0cc233-9edd-3ff4-b9fe-b91e71542b28 | -21.1896 | -48.8145 | 2025-09-22 00:10:00 | GOES-19 | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |


[Clique aqui para ver as próximas entradas](README2.md)
