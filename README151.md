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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae59850a-5a79-3fac-ab33-7022bba6e1f4 | -17.88967 | -57.58545 | 2025-10-02 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 0b401c12-91ea-34d6-89f9-3af06361f303 | -18.61364 | -45.3964 | 2025-10-02 12:40:00 | TERRA_M-T | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f4067f0a-1c60-3205-b4bd-6ca544986d03 | -18.17876 | -53.27419 | 2025-10-02 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2be93fb0-72be-3171-a000-08cd52314320 | -18.21521 | -53.344 | 2025-10-02 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 82605733-b4b3-3db0-901e-a232dc95f0b8 | -18.60249 | -45.39016 | 2025-10-02 12:40:00 | TERRA_M-T | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 2dbe9dad-0737-3431-a51b-23a15fa4e5dd | -18.17744 | -53.28374 | 2025-10-02 12:40:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5b559cb2-648e-3abd-9795-ef9ffef722f0 | -18.85608 | -45.23406 | 2025-10-02 12:40:00 | TERRA_M-T | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 3fd57530-2746-3a47-b91c-295dbdab3c3f | -18.86193 | -45.22909 | 2025-10-02 12:40:00 | TERRA_M-T | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| b3bf87a0-e3a1-3187-863e-a3f289360920 | -18.0067 | -49.58092 | 2025-10-02 12:40:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c57acd0b-b6a3-30f0-b265-4d5ad3f09205 | -18.18574 | -53.29128 | 2025-10-02 12:40:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 00c3edbb-5215-3dc2-98de-5dc99492398f | -18.20622 | -53.34263 | 2025-10-02 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 49a0384b-bd7f-3d9c-83b5-5ba967f76426 | -18.66196 | -46.02504 | 2025-10-02 12:40:00 | TERRA_M-T | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 27.0 |
| c9404b6e-4a3f-35cc-a08f-3908d3f53f4a | -20.27256 | -54.8323 | 2025-10-02 12:40:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2ecb221f-f499-3c5a-b0fa-ede4f1a42d6d | -20.27391 | -54.82292 | 2025-10-02 12:40:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| cdb46e40-2511-3bfe-9db0-96ab8a327429 | -19.76972 | -47.95304 | 2025-10-02 12:40:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 75aa5963-7beb-3743-a11c-387ded67d345 | -19.93996 | -46.96083 | 2025-10-02 12:40:00 | TERRA_M-T | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c7f6864f-e791-34fd-81bd-331d2ea21dc4 | -18.00714 | -49.58701 | 2025-10-02 12:40:00 | TERRA_M-T | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| eec0ae2f-63b2-3010-9815-5ff80ac2dc89 | -22.56929 | -46.76503 | 2025-10-02 12:42:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.9 |
| 4452ddaf-cc9f-36d9-a797-adb897cffd32 | -22.56666 | -46.79362 | 2025-10-02 12:42:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| b59f551e-b9f7-3a4b-a773-e307438fff94 | -22.56936 | -46.77149 | 2025-10-02 12:42:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.9 |
| 15c4f6f0-23c2-3c3b-8cef-27caccbbf98b | -21.50606 | -46.71119 | 2025-10-02 12:42:00 | TERRA_M-T | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| 5d40758b-02b8-39cc-ac9c-e4eb8b58b23f | -22.5669 | -46.80037 | 2025-10-02 12:42:00 | TERRA_M-T | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.2 |
| f20c5c8a-0ad5-3bd9-9548-1992f2c599a9 | -29.29798 | -51.50997 | 2025-10-02 12:44:00 | TERRA_M-T | CARLOS BARBOSA | RIO GRANDE DO SUL | Brasil | 4304804 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 1f863240-db94-36f2-ac65-26fb707b2f6b | -29.2976 | -51.49852 | 2025-10-02 12:44:00 | TERRA_M-T | CARLOS BARBOSA | RIO GRANDE DO SUL | Brasil | 4304804 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 77f78347-4bfd-3ebd-a6c4-b2957fdc4c6e | -29.29978 | -51.49279 | 2025-10-02 12:44:00 | TERRA_M-T | CARLOS BARBOSA | RIO GRANDE DO SUL | Brasil | 4304804 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| b660ba92-f741-36cf-8889-5de30ba9807a | -13.1739 | -47.8317 | 2025-10-02 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 47eb08e4-a9b7-36c2-ac9e-1742688b051f | -13.0119 | -45.1988 | 2025-10-02 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 2c2d54b7-1219-32e3-8ee1-ea19abbcce7b | -15.3067 | -45.0713 | 2025-10-02 12:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 643f3cdc-d0d8-30e8-b154-a8a42017f957 | -8.2105 | -47.0084 | 2025-10-02 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| e9225642-eb38-3a9c-a00f-2da558908dc0 | -14.3709 | -45.9403 | 2025-10-02 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 429a6fc6-5a24-36ea-a093-2c2f45252d10 | -14.1917 | -46.1552 | 2025-10-02 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 015aa274-69f8-3a96-9d0e-c6d52b64c384 | -14.2924 | -45.977 | 2025-10-02 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2e6c468a-1eb6-3718-91a7-86302592c4ef | -9.3392 | -45.7039 | 2025-10-02 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 17125228-43a7-3c35-9b39-42fc411d7b4b | -9.9372 | -43.7187 | 2025-10-02 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| e05ae805-76fa-30bd-95e6-ef02fa1061f1 | -9.9182 | -43.7212 | 2025-10-02 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| e649ddb3-b071-3478-a2b9-474accfa1faf | -10.0906 | -50.2154 | 2025-10-02 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b12488bf-8769-3e3b-82e3-45dcc4630b35 | -8.5596 | -44.6724 | 2025-10-02 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| f6427c59-806e-3aaa-b128-a812ca182f17 | -11.9085 | -47.8745 | 2025-10-02 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| ac5be19a-54ef-33b2-b4fd-0ae2c5f097a5 | -15.2542 | -49.3104 | 2025-10-02 12:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| a023faa4-34d6-3226-bced-a00f7ae8976c | -8.1513 | -44.1397 | 2025-10-02 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 376eff08-2052-3b73-bfa8-1f65d3574492 | -13.3131 | -47.5876 | 2025-10-02 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| a876e904-c3a4-3dcb-8c0b-4906ebeda204 | -14.3704 | -45.9634 | 2025-10-02 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| dea4e3a9-a1be-36b5-a465-635046835efd | -13.1542 | -47.8568 | 2025-10-02 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 37a44e50-497f-3c70-98ca-b964fbf757f1 | -8.6722 | -47.6924 | 2025-10-02 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 4d60a9b8-c5a4-3ed4-b182-05c0d20b6837 | -8.8929 | -46.6072 | 2025-10-02 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fbaa6ed6-ae63-3fd4-9d6a-39ba63f86d73 | -13.1735 | -47.854 | 2025-10-02 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| c1ae85a6-1973-3d2b-a522-5f9e77d465a1 | -14.4757 | -48.4137 | 2025-10-02 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 903f40dd-fce9-397f-8892-df723c72021c | -14.3139 | -45.8811 | 2025-10-02 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 266f273d-e790-396f-a6ad-7db2f0a59b8d | -9.4272 | -47.5722 | 2025-10-02 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 29254632-b68d-3f5a-a5ea-5748d5738ec0 | -9.9178 | -43.7447 | 2025-10-02 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| b1bef810-10a4-3c43-bcde-e24dfee814ef | -11.8426 | -45.0336 | 2025-10-02 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 456bddaa-b2bb-32e1-a0b3-e11d721e714a | -9.9365 | -43.7657 | 2025-10-02 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| f0e5fafd-2cad-3874-9d5a-ad909a05215e | -7.7755 | -42.5152 | 2025-10-02 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 155.8 |
| 2b644d21-b5c4-3073-b6b1-a72d8cd7d6c2 | -7.7947 | -42.4894 | 2025-10-02 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| b72aca88-7630-3fcc-b768-d34bcbe02540 | -16.0417 | -50.8959 | 2025-10-02 12:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 7fc2a74e-86d5-32eb-a982-5134b482efdb | -9.4086 | -47.5521 | 2025-10-02 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 8ebd27bd-f8ea-368c-91ce-48f3bbb936b1 | -13.1932 | -47.8288 | 2025-10-02 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 54e4b2e3-61cb-38d0-9f0c-bdb039dfb82d | -10.9367 | -46.6843 | 2025-10-02 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| f668777e-bbfc-3402-a0c4-1bfb56ab3ce5 | -8.5599 | -44.6494 | 2025-10-02 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 302.4 |
| 94536f09-f265-3738-b1cb-03fb6860e125 | -9.3389 | -45.7266 | 2025-10-02 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c72e565c-974c-30fe-8bcc-b572b535dea0 | -8.541 | -44.6515 | 2025-10-02 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| e47eb07c-831f-36e3-aef4-e34441246db6 | -7.7941 | -42.5369 | 2025-10-02 12:50:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 146.4 |
| e020b5d5-128a-3418-b66c-eac8d302021d | -9.4083 | -47.5742 | 2025-10-02 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 6362f0e3-9ba0-3621-8bcb-30cf5b7b7ebe | -9.9567 | -43.6927 | 2025-10-02 12:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| ccdb8e09-b09e-3db4-9540-23faf8bc049c | -7.8882 | -47.281 | 2025-10-02 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 61ea30c3-e472-38da-b140-4ed230249379 | -8.5201 | -47.8386 | 2025-10-02 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 0cdaa4e1-328a-32d3-a336-f9c5f2d7e648 | -14.5747 | -48.3089 | 2025-10-02 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5f0903eb-d9da-36c0-9ed6-8e1ea85877ff | -9.3364 | -45.9079 | 2025-10-02 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| f122c65e-6e0c-3909-b1cf-2baf991c617f | -8.6911 | -47.6906 | 2025-10-02 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 72c9af0e-0ea4-3453-97fe-9b3dd1bf0644 | -7.7944 | -42.5132 | 2025-10-02 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 171.6 |
| 35f7badf-8bbc-3851-978f-e0c9b579f5b3 | -8.5204 | -47.8167 | 2025-10-02 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ace25ead-7bac-3d29-be55-f24c1b62a143 | -9.9563 | -43.7162 | 2025-10-02 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 39dcea27-49da-3e55-8ddd-ce727e16ae27 | -13.7864 | -48.0524 | 2025-10-02 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1cf2e90f-65c1-36c8-8e92-c5571aa77fea | -11.8234 | -45.0364 | 2025-10-02 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 9c671376-df6c-3eb1-a299-08f8d331f143 | -11.9272 | -47.8941 | 2025-10-02 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 1f784322-0559-387c-a9ef-9cfadb2754a7 | -11.9276 | -47.8719 | 2025-10-02 12:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 266.5 |
| 6c189cd9-0dfc-3ff2-bea4-4a5c813deba2 | -7.8879 | -47.3031 | 2025-10-02 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 676865b0-22d2-34c1-aff7-e70cea453406 | -15.2738 | -49.3073 | 2025-10-02 12:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3e1e8e7a-f12c-3919-99ab-81ef60706da4 | -10.8237 | -46.6088 | 2025-10-02 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| cd160621-362e-3eda-a4eb-cac06b9f3f87 | -13.1743 | -47.8093 | 2025-10-02 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 58344e0d-9e40-331f-8b05-66c9210ca5ac | -12.6729 | -46.851 | 2025-10-02 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8b1a8f24-cbd9-3920-87d8-8fb764993cdc | -14.1921 | -46.1321 | 2025-10-02 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| e4b96df1-cc4c-3048-9ac2-d6633a3ccf34 | -14.5937 | -48.3281 | 2025-10-02 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a2456085-b04c-30f2-81b8-c85799dcbb22 | -9.9369 | -43.7422 | 2025-10-02 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 4708b95a-bd2a-33ae-982e-e369f186927f | -14.8212 | -45.8143 | 2025-10-02 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 2698db6a-66ce-3177-bb4d-55f1cbc6d103 | -14.2121 | -46.1058 | 2025-10-02 12:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 4e1ea24c-de3d-3918-b871-f7ba809b515b | -8.672 | -47.7144 | 2025-10-02 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 82d23074-579b-30db-b65a-5ba8a91a3984 | -6.7816 | -45.5703 | 2025-10-02 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| c77492a8-dbe8-3b3c-a779-03548e0ec2e9 | -14.4753 | -48.436 | 2025-10-02 12:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 10567892-80ad-3316-8251-61999062b061 | -12.5001 | -50.2453 | 2025-10-02 12:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 41195b65-3539-328e-b18f-08861b801972 | -8.1702 | -44.1377 | 2025-10-02 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 71d98006-de08-33c7-a686-ee2b35122a33 | -6.7814 | -45.5929 | 2025-10-02 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| dd1b7833-deec-3405-8a01-1d7f6690e0fa | -9.08 | -46.7215 | 2025-10-02 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 02405cb7-5e12-3ee0-b572-0d76ee2448ef | -14.425 | -46.1381 | 2025-10-02 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 707d720a-c1bb-3f7f-a511-ef07cc6b4db6 | -8.6908 | -47.7126 | 2025-10-02 12:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 0057ece8-1363-32c6-a85d-3cb81674fa37 | -8.2094 | -45.5301 | 2025-10-02 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 08f66f72-2bcd-3724-b7cb-2abf1b618d9f | -9.0431 | -46.6585 | 2025-10-02 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f5204027-601b-3b3a-aa38-b3def5317f5c | -9.336 | -45.9305 | 2025-10-02 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 379.9 |
| 64b3b4cb-9512-3464-a036-1cad26632a33 | -11.1746 | -47.2805 | 2025-10-02 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0ef20358-dd5a-3219-8b2f-aab26ba58e2a | -7.7752 | -42.539 | 2025-10-02 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 225.7 |


[Clique aqui para ver as próximas entradas](README152.md)
