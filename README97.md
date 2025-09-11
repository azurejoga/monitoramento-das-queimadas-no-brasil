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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83557f6a-b3b5-354f-842f-0365393050e4 | -9.75837 | -51.05547 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9d19886-3fd0-3271-a4ab-4c3b80fcff4a | -12.94767 | -54.74406 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bda8d746-cc5c-3953-ae70-33dbae885f23 | -9.75342 | -51.08723 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5474c785-ae98-3d89-a72c-c281538a4dfb | -12.92892 | -54.79257 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3edb26a0-9032-3556-b282-f2601634a4e6 | -9.98892 | -48.37957 | 2025-09-11 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e960f936-6162-38f2-a32d-6730ce363472 | -8.08387 | -54.74028 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8da68f3-9537-340b-88dc-bc22d5e0b8f1 | -12.40726 | -63.80952 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adf83478-6a98-375e-b9e8-458394b72f33 | -14.5037 | -53.94406 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15990c07-13ec-3c43-b010-225e00a96243 | -14.89227 | -55.84488 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55c7ada6-80a4-3251-ab3a-366bb7a9013d | -14.35808 | -47.29808 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10d9ec4f-5faf-3c18-ab07-ba07b8a65cca | -12.53345 | -45.34 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 0a145fa3-6967-32d0-83d4-248a6573e2ac | -14.72777 | -55.61499 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b805190-b22c-3cff-9cbc-7265f4a2a1ac | -12.61766 | -56.95897 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f75ac398-0ff5-32a2-834b-a9fc6b1210f6 | -9.7473 | -51.08275 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e4f1939-e26f-3a67-a422-3a5f677cfaa5 | -11.47581 | -43.68493 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79f118a4-ee11-372b-b8b2-9e41ad1a7d03 | -12.85435 | -52.9381 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f7b9f3-a11c-3321-8fa0-d59baa5cfe04 | -11.87682 | -58.81299 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e38c547b-47f3-3596-a399-deefc2b51282 | -10.7428 | -48.17967 | 2025-09-11 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97faaee1-7f0a-3b5f-a3a2-c3b1b0debf10 | -8.5835 | -50.79556 | 2025-09-11 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48722519-91ae-3546-87b5-98ce7b6f97c6 | -12.8576 | -52.96043 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db1d3202-b9bc-3b78-bddb-fc29c4ba1ad6 | -10.65012 | -48.63125 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc7964ea-10f6-3bc3-a7ab-e8b56ec7b4cd | -11.34794 | -46.49614 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e90d64cd-3809-3f03-ae77-0fd91226d3c4 | -9.75188 | -47.85245 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 471b7031-fe91-3840-8e82-db99c0bd9d2d | -11.68733 | -46.89991 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9011f026-c0d8-33de-a6a2-8e6a8f2c7077 | -10.38024 | -50.5223 | 2025-09-11 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91402447-feed-350d-9016-886aa2428e5a | -8.52126 | -54.76896 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 005cde41-3852-352a-b917-ac233eef9bd2 | -12.86849 | -47.9603 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a6404db-2f7c-3db2-a211-fa67e6eff9c9 | -11.77124 | -46.48635 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86688a68-b636-34b7-a3ab-2f55cc1aa405 | -8.56696 | -51.35781 | 2025-09-11 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ced2bb34-146d-34b7-adb8-24bdf2970574 | -9.88937 | -51.88716 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18d364dc-bb92-30a2-8593-053aee8e3451 | -11.47622 | -43.64221 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bd01ca95-397d-3180-9a98-ecf6f2e2639d | -10.5705 | -52.02553 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17e41ce8-d600-3459-9206-a109a9174b80 | -14.39902 | -47.30807 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1586e397-1c67-3f17-a7c7-7c5f54a0ea0c | -14.56519 | -48.76855 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 476b9dfc-b496-386d-892c-6d177346d956 | -9.08998 | -49.85012 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190d5655-120d-3e76-825b-d2954985fb61 | -12.84934 | -52.94817 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 108ac71c-b603-35b8-a030-ad3cff1be524 | -13.24689 | -51.77834 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 686fbfdd-93ce-385f-b2a4-ba0591d40faa | -15.11566 | -52.39753 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d567a90-6d76-3c63-8d37-0c03a28a91eb | -11.47724 | -49.26809 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0604650-e0f7-384b-947e-ca7e895d38a1 | -10.00679 | -51.72353 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4559c0fd-bf4c-3b41-b777-d6704ff1c951 | -11.36921 | -46.55892 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ffdfe20-15cf-3f98-84bb-0765a42a0eb6 | -13.58693 | -47.70424 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 91a3b03a-08e7-36d3-a0e8-e521a315320d | -9.0245 | -49.77541 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 933ad77b-65b4-3f03-a4e7-18b5ea64ff27 | -11.48114 | -49.25946 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3477ccf-741a-3dbc-bb62-15e61f3dcfb0 | -16.30019 | -50.06102 | 2025-09-11 04:46:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7cdbe997-6088-3a86-a954-a16220318c83 | -12.97055 | -54.75599 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6219c68-1eec-3c28-9c5e-2917f9f989a2 | -9.59926 | -50.91866 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71edefc9-51d9-39a9-9a28-073c7484b9fc | -10.38982 | -48.57411 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aacb4ea9-053a-3e50-8c89-2f65e786987f | -8.86929 | -49.55296 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7043e30d-f757-3507-acc9-fd2d7f153247 | -11.71796 | -50.63716 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 64ee209a-1c26-398e-a67d-3fed48a68302 | -9.38579 | -46.772 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e42bb8a-38d2-3fab-bb09-e70c3d56bc13 | -11.49145 | -43.68407 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80e340e6-d397-323b-aac6-18eef18cfc26 | -16.06396 | -49.96753 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b81f6c1-e34b-3352-b14b-96ac2fd11978 | -10.17128 | -46.18328 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7b51d2c-0fbc-34f5-a109-ebc8cfa8cc5e | -15.11954 | -52.39449 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38c5db82-1f2e-3383-9e28-6cf9b659bf6a | -10.27395 | -48.83078 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dae55c31-671f-3883-8ea5-f649e4941730 | -11.15258 | -45.29328 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bc177c2-8219-349f-bbc1-5c401880981d | -16.88864 | -45.82957 | 2025-09-11 04:46:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 904e7bf8-3cbe-334a-a1bf-8110c3304ce2 | -9.79896 | -51.09783 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94cc0798-2aad-3b00-9ac9-6078e24a2289 | -15.13794 | -52.44919 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47588ed8-0782-359e-9e10-8924c9a918f4 | -15.67495 | -47.03292 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b9cb38ed-18c6-3471-a6ed-9a03e91c23e7 | -9.79194 | -61.52412 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31256df6-a481-323e-9535-ee702fabb7bd | -15.89288 | -48.18321 | 2025-09-11 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26cb35a4-5197-3d01-9a4b-f27fbb8232bc | -15.02439 | -48.05052 | 2025-09-11 04:46:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c62fc5a-8147-3651-864a-03945e0ec734 | -12.47543 | -47.48851 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1916ac2d-82b8-348a-9e53-e9841fcae2ea | -13.29508 | -43.75686 | 2025-09-11 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a2bc47e-ec10-3ccd-8782-1aaee402d8d0 | -11.19184 | -48.36585 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbaf12e8-ec67-3373-945c-4c75c049be43 | -11.48364 | -43.68983 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1699f89f-9b88-3f09-be77-214e5dd068a5 | -11.43377 | -49.29077 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73e64eda-3be3-3497-84fd-874d11a09839 | -12.94297 | -54.81504 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b0598c3-7632-3244-926e-665060c81231 | -14.71172 | -45.34373 | 2025-09-11 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d4d96b2-ccda-3757-861d-6345d74207a0 | -15.52616 | -48.56365 | 2025-09-11 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c0120a2-1102-3e29-ab94-afafd6f93a5f | -11.14954 | -52.0365 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59bd79ee-98c7-3099-b7d2-30aeabaa175a | -12.00984 | -47.5841 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 4bb883a3-e1a5-3dfd-a927-196be311fd17 | -12.22021 | -53.87733 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 429a9c4d-53a2-3508-b951-412b0a298b4e | -10.87497 | -49.64394 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b16dec4d-d031-3ebb-b1c5-c2dfdd6bdaba | -12.39437 | -63.81116 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7b7457a-c95b-31ba-80bc-09178ed06530 | -9.46151 | -46.73972 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52cbb2db-f42f-341e-b077-86bbc6a25dc8 | -11.40186 | -45.59645 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 186ac88e-478d-3438-ad01-3331f6ee27ca | -11.06937 | -51.33093 | 2025-09-11 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dfdf0d4-6f9a-362d-99a5-bce581fc6372 | -14.4751 | -46.35818 | 2025-09-11 04:46:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10fb0feb-8f6a-3d5b-a8ee-f76a34722757 | -14.2824 | -54.7594 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 423a96e2-6b58-38f8-9694-be5fb835ea0b | -9.51362 | -54.63779 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dbd431b-e09a-3631-9902-619455a59a63 | -11.48915 | -43.66224 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc0b9324-b355-34f2-9ae4-b80ad2bba6ce | -15.22117 | -44.05115 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b6d8838-0cbf-3a51-bb7e-4b502cd58016 | -11.65777 | -52.23711 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20a150d7-ea49-3ac4-8752-ed356dbdaf9b | -14.49811 | -49.10484 | 2025-09-11 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf269789-9cda-3f74-886f-5e74dd0a293a | -15.13572 | -52.41942 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daadd259-269d-3261-9ae7-93f0354a0f97 | -11.43725 | -43.58156 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8cb64f2c-24bd-3542-b4fe-0d0b3bd45148 | -9.08657 | -49.84959 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d99c4b20-4b62-3d64-84cd-f8f03d73dad5 | -12.84046 | -52.96122 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1e4a689-64f5-3c78-bb9d-e9efdf156ab1 | -14.41754 | -47.32735 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 398b0f8c-c5e1-3884-a759-8481461050ec | -10.00512 | -51.71252 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1ffbdec-a07d-3e3b-9c6d-50feb46f6417 | -11.47817 | -49.25481 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 695e3dbb-f3ad-37b3-af41-9059f7291285 | -9.79121 | -51.10389 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c076b2a-bffc-3aaf-9241-426b5cec04d4 | -9.45605 | -46.42347 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 018b5b4b-8ba9-3167-9657-648e22307b87 | -9.5158 | -54.64676 | 2025-09-11 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba5cfa6a-32f7-3fb2-b809-74a23163af1e | -11.49464 | -43.65995 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09cb59de-8211-34e2-a6da-7072e8dc6418 | -11.16224 | -52.0415 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c605bd9f-f510-350b-89fc-efc5d3377fad | -9.38273 | -46.76483 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README98.md)
