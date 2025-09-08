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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5a78755-cbb6-3387-bd8c-20e96aa67cb6 | -9.16778 | -59.37974 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19b7b884-8ed1-3ea4-974a-88d29df8ca61 | -12.94532 | -54.80334 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10bbefae-7ef0-3132-b363-bd9163e1b683 | -11.02368 | -45.92764 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6baec56-0615-35d3-a20e-90b1c1be92d6 | -6.82987 | -52.79727 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 949d8c20-5c55-3526-8bad-d79eb4b7b8d6 | -12.60843 | -56.97855 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c4e2c41-72bc-3441-9bc9-a4eee1534363 | -6.20161 | -53.26065 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3060a0e-90cb-397e-80a1-ecaa1aa7c8e4 | -10.56625 | -61.23336 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ab1c2f9-ccd7-33a0-9bc0-e4e67ff99807 | -7.43084 | -49.26385 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b16b14ca-bce3-3078-acdf-7d6bb0ddf216 | -12.20031 | -53.90918 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd890290-52f9-3728-b351-9666f948b115 | -7.59705 | -61.59698 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa738641-a979-3329-b52d-ceecc0daf6cc | -7.78234 | -50.75384 | 2025-09-08 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 68f0b050-5153-3786-8b21-5705e86be60f | -9.99683 | -51.66862 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90c798e5-d267-32e5-9f47-d1bfb9707d2a | -8.88157 | -64.21664 | 2025-09-08 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 56c583f0-d20f-3a49-84ed-aecbb793d457 | -6.80989 | -52.8113 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f685865f-1e73-3065-ab1e-326a423f5ead | -10.51265 | -57.79707 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 433cd962-cab7-313e-99ef-57d9d165abed | -6.87654 | -47.90862 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e01f9b42-d719-38a7-9882-26daf4e17478 | -10.15854 | -61.14068 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 446d67f6-c1f9-37ea-9571-d97f0d0f324a | -10.14225 | -46.21145 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5050c55-57db-3fe9-96a5-f195909bf136 | -11.18477 | -55.04924 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26b654a3-221e-3545-8950-2eb42dc5d466 | -9.99607 | -51.6745 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 762174d8-6f7b-3bba-8d64-f8b63f815bf6 | -9.69883 | -57.803 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05c79284-9ed3-3ec6-91dd-e6fb2e99c9fe | -10.17603 | -61.13989 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d961249c-2db1-39e7-a0a6-9e0fdf525338 | -12.62065 | -56.97161 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32d8811f-74d3-35a5-9ef9-8ea2572546c7 | -6.96379 | -62.93708 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8070c3f-8080-3c3c-bd5e-1f08beab6070 | -7.81617 | -52.13523 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 943915d4-636c-31c2-b3c8-00bc616f2042 | -11.03515 | -45.95623 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d8dd3010-61e4-37f3-8297-1a44838b51f3 | -10.51089 | -57.80853 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92f9b53f-e753-3400-8f81-72e0cef8f2b1 | -7.43137 | -49.26006 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5fbd61c-8fa9-3245-af0d-63fb1dd4bfff | -6.54579 | -54.98845 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8841cd1d-cc47-3787-acb3-3be139bb43fe | -9.87569 | -46.53144 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b32a89fd-b5bc-3bde-a7c9-52f89da3ab32 | -9.28453 | -56.90167 | 2025-09-08 05:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d9d0829-1ae3-3df6-8db5-811bfb48489e | -9.18857 | -60.76822 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c969047f-bc35-37f0-8c71-e3a2fe2a3f84 | -12.92805 | -54.77322 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3167d57-a609-38c8-86be-257383846cf0 | -11.18428 | -55.05275 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 872004e7-b953-3402-b810-4864873eb0d1 | -11.20235 | -55.0121 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32b5b3ef-24aa-3096-8967-3ddd433d5b60 | -11.85794 | -51.05621 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9d9c58e4-a6e7-305d-830d-094769b695f7 | -11.20285 | -55.00857 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c16c034-33f7-39c2-9130-c320753426e5 | -11.86582 | -51.06204 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a1dea196-28d4-30a5-8512-6fc9d995d143 | -8.20009 | -50.14146 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fda720ac-3bd6-3612-a2dd-e80ae5582fac | -6.83368 | -52.80174 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bad65f83-1baa-37e2-811f-1a5833b47139 | -11.8691 | -50.96908 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b3b4b01-ee5c-3f34-9fe3-14600240c692 | -13.54391 | -48.11698 | 2025-09-08 05:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5dd51dc-0979-3947-b1c6-b14998fbb94f | -8.19429 | -50.14396 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06ed8c61-2274-3374-b3c0-1866f787c5a0 | -11.41209 | -60.60244 | 2025-09-08 05:21:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c3c5e20-3aae-3293-a980-42dcffebba70 | -12.94166 | -54.7989 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3943e18-8ff2-325b-b0b7-ede48d85e48d | -6.95549 | -62.94038 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e065ec59-2918-3873-8d19-32844067b49f | -10.15119 | -61.14318 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cfc4410-d996-3535-98a2-c7dfdd34b65b | -11.38419 | -50.33984 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ff5c7e3-58f2-38ad-addb-de638918128b | -12.82168 | -52.88644 | 2025-09-08 05:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0e32744f-5648-3240-83fd-e6a7beb69f3b | -12.63164 | -56.97324 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c2e1d22c-f426-3bd8-a065-88faeed8cadf | -7.22268 | -46.21083 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 86c7674b-43f6-3284-900c-b725f60b08c4 | -7.82897 | -45.42788 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dde05eb1-5108-38a6-95b9-fd6fdd212fd8 | -12.89641 | -47.99453 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1269dae-03ab-3fe5-b46c-0b532d2916bc | -7.47507 | -61.59426 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04a2323b-a21d-3f0a-907b-7413ca51958b | -6.28397 | -53.42689 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72a0aca6-34e6-33be-a54a-324a949e1aa0 | -8.8793 | -69.34579 | 2025-09-08 05:21:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b3e9d16-1066-390a-9ce5-4759ba58470e | -6.82501 | -52.79968 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9aaf2a5-accb-3336-a508-d9d3133209fd | -9.94174 | -60.14674 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76718dc2-d78e-329d-9dc8-c03e45235ed0 | -7.66089 | -47.95049 | 2025-09-08 05:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26b3cff3-5190-3261-a325-18e26dab711f | -11.86502 | -51.0687 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ccaa6a33-337a-3ccc-98bb-7d75f9cc5ff8 | -10.4152 | -60.74254 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe15d48b-66c1-3030-997c-cb48964e4334 | -11.21091 | -55.0098 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2592495e-601e-3d0e-a8b2-ee7495c8c5d3 | -9.4589 | -60.49979 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b368f0d3-f08f-36b8-b005-22bb696dd91d | -12.93277 | -54.76998 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27b01821-ac7c-3ee4-bc9d-b04fda286db4 | -6.9487 | -62.93454 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93089d8c-d7b0-36e2-a7bf-36088d82ee6a | -9.97055 | -55.0463 | 2025-09-08 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af50fa6e-830f-3e3f-b055-1b127f1c9383 | -7.8316 | -45.42933 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8def0df2-ebea-32f0-a458-a46616ee670a | -12.63403 | -56.98251 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85859823-13d6-3b82-81e8-52641e0b2292 | -6.22051 | -49.41935 | 2025-09-08 05:21:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80ea700c-fbf0-3c86-8d50-41f03e49e2d8 | -10.28793 | -48.79837 | 2025-09-08 05:21:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4dcd7892-1d99-38c7-9f55-4d740b650ea2 | -8.88898 | -51.0535 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fe85b89-bdc9-31c2-a5bd-9ca717bdfe3d | -11.21141 | -55.00626 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b83f403-3ccb-390f-b6e4-3504ea36f9b0 | -11.87164 | -50.59858 | 2025-09-08 05:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d75f5994-b73c-30e9-9da8-bc7ba262aa26 | -5.88862 | -52.09682 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8dde82c-7fed-3de0-a770-5600345ea2a4 | -10.0499 | -59.36234 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7314baa4-f60f-3cf5-8e23-eff2db90f5f5 | -11.38517 | -50.42143 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ef22854-a87f-3f02-b42f-47f7dbd245bc | -12.95056 | -54.79628 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79bf69ef-bb84-3cdc-ab08-351a1db92b50 | -11.78167 | -60.89249 | 2025-09-08 05:21:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ba001ef-3e35-385f-9e45-f86a245d7b0a | -6.86388 | -47.91317 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2161f764-3d70-352b-9797-515ac973fd5c | -10.17662 | -61.13626 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a28662ed-0ea2-35dd-afb9-d8efd5f6680c | -6.62733 | -53.35006 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60f8ead5-54e9-3010-9600-95062f0ce362 | -8.88949 | -64.21806 | 2025-09-08 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a853130-18ec-3177-a459-2fcb9bf70a84 | -6.82444 | -52.80378 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 130835e4-a3b8-3b0b-b4e3-a72564c44a6a | -9.96059 | -51.20428 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecf10eca-63fc-31e4-a73e-8516925e8709 | -9.96023 | -51.20708 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e83223aa-972d-3789-9be9-d042e7914182 | -8.88466 | -64.22247 | 2025-09-08 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e76650f-5aa7-3b24-a5cc-0614e46a9cf5 | -10.17266 | -61.13926 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc9a9d02-a7a2-34d4-b91a-8b53efdaec90 | -9.94896 | -60.14429 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a3fdc8d-f691-38a9-8379-8d841aba6ae0 | -11.0367 | -45.94232 | 2025-09-08 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c84b923-984c-30cc-b007-bf39967afb26 | -10.46511 | -53.60775 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f047ce3-bc08-3047-8c8d-a5c70f84f59a | -11.1953 | -55.00375 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8a732181-4c2a-3a2c-986b-a14f5a8cb822 | -9.96522 | -59.59698 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 336a8a20-acdb-3f6f-9ddb-3a8b4be9f2b3 | -9.98389 | -51.68312 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0e3b81bd-3e03-39ee-98f0-9848fc259c28 | -10.77084 | -59.84832 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c51909e-6874-3940-9bfc-5b98f6568a10 | -9.19906 | -46.04953 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 92bd3961-45d7-355d-96d9-8dfb23d70b84 | -9.60962 | -55.01299 | 2025-09-08 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f0b5a2e-2f50-36a3-88de-db1bd2093c4b | -7.67492 | -50.28986 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a982bbcb-3a75-3d10-9ac6-7c67a029f28c | -6.27564 | -53.42567 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a69f7249-5e1c-39c5-8171-d4f653e257db | -9.20146 | -67.55389 | 2025-09-08 05:21:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2acd0700-3e1e-3ef3-95b8-79346fdca694 | -6.15455 | -53.68734 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README85.md)
