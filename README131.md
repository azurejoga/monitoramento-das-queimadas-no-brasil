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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d217d4-cecb-33f4-9fc9-31c63bd0fe32 | -12.15253 | -50.05773 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 339637d0-934a-3cad-91c0-326650ed84e1 | -12.15215 | -50.06079 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 26c47099-6cdd-3e5f-b95b-1293c647157e | -12.14816 | -50.05093 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a440567d-e003-3429-8c0e-8dcfc5451863 | -12.14778 | -50.05399 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f10ea8f-b954-3c58-bb45-f36aad4e4fe9 | -12.14741 | -50.05705 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9983adbd-8c38-33a9-be3a-07985af6a7d4 | -12.14703 | -50.0601 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48c83d74-9406-354d-a866-05a8dcfb8296 | -12.14572 | -50.05019 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 833b2770-fae5-3e5d-a31c-86150285468f | -12.14532 | -50.05324 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecdc07c8-30a3-3b37-91c2-b74ecaf8e186 | -12.14378 | -50.04414 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0071ccab-f118-3a8e-869e-a8cb000e2754 | -12.14341 | -50.0472 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80605536-3156-3627-8914-3a932c71ffe0 | -12.14139 | -50.04343 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d30dfcbf-d9a3-3c14-b0f0-f6305a5c2f26 | -12.14099 | -50.04648 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dcb32869-e91f-3532-a872-438229ade9f0 | -12.13865 | -50.04346 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 135e2efe-4894-374a-9900-0d857a1979f8 | -12.13828 | -50.04652 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 055fd468-2aec-3703-9e69-809ba4a1bc7b | -12.13586 | -50.04581 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4843c3f3-000c-34af-a152-f3bdf9dd8b1d | -12.13352 | -50.04276 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f86c7f3b-7af4-3d36-a422-9945ab689d94 | -12.13315 | -50.04582 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61a3f086-3989-31a3-a3d9-b7d49da244f6 | -12.13113 | -50.04207 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1073ef4-ce3f-3b3b-ac61-db050798aa7d | -12.13074 | -50.04512 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d00146b9-e3dc-3f21-ab4a-b16962e08fbd | -12.12561 | -50.04444 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b94b5c71-a29e-3258-b8c0-6a61c0a24c22 | -11.15123 | -49.72577 | 2024-10-02 05:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78658258-dfc3-3ba5-9132-d6e6ebf42bf6 | -11.15083 | -49.72888 | 2024-10-02 05:10:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56eea1b9-c8e3-37fe-b760-23589e772a4c | -11.1124 | -49.60745 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 517c9d2e-33dd-38c8-9f20-16593fb6e711 | -11.10678 | -49.60992 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd891610-a59b-349c-916f-bcbaa7ed9543 | -11.10637 | -49.61306 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7009686-a1bf-3eca-b799-e678f590aad0 | -11.1024 | -49.60291 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5213b74f-7316-383a-9c41-33a61d5af489 | -11.10199 | -49.60607 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f032eb0b-fd55-3471-bdd2-7a88735eca6c | -11.10158 | -49.60923 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e5406f3-3283-3b84-8021-20b143ef0890 | -11.10117 | -49.61238 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2985581-9053-39c5-b00b-08f41cd19b8a | -11.09801 | -49.59587 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0256a551-318c-370b-9935-e0f23f74f30b | -11.0976 | -49.59903 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a01c7cf5-4043-3782-ada4-cd69040fa495 | -11.09719 | -49.6022 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02f763ce-76dd-3b32-b83d-bc66303180e8 | -11.09362 | -49.58882 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c522872-b9ef-3741-9677-b3d181e966e7 | -11.09321 | -49.59199 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8218cd08-7c48-3340-a312-25b07c1b0e19 | -11.09281 | -49.59515 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4c28a4b-4739-392a-aaed-aee528af4e30 | -11.0924 | -49.59832 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f48b702-d6f2-3713-971c-b51d348ab9b2 | -11.09199 | -49.60148 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2940af75-4dd7-3a1b-a6ee-aae227362f2f | -11.08842 | -49.58809 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d268e2cb-ff07-3122-b758-c467aaa8f2ce | -11.08801 | -49.59126 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cae926b4-efe3-3ec9-9e0d-33f041c7988b | -10.89655 | -50.09116 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44b3c35d-92cc-300f-ab72-157c193dc240 | -10.89631 | -50.13239 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc20cef6-2cc1-38c3-b8db-5c7dbb44c239 | -10.8958 | -50.09697 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be18863e-f700-3e95-92e4-25a76e6640cd | -10.89556 | -50.13817 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 242efde5-1852-3f4d-89eb-3a977cf3eaea | -10.89505 | -50.10276 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1299eedc-8e4b-3f70-8730-a6cdd33f5f51 | -10.89078 | -50.09627 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d47ee86b-ae51-368a-be7f-ec55539a41c7 | -6.42551 | -50.14447 | 2024-10-02 05:10:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce17714f-bc1b-32bb-bedd-13aa8bf6cf1f | -5.52068 | -50.04548 | 2024-10-02 05:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eff1a68b-d634-30f1-95d0-045654a5c610 | -7.80465 | -50.23312 | 2024-10-02 05:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61aabf8f-132f-373e-bfaf-15a0832982d3 | -8.33509 | -50.64194 | 2024-10-02 05:10:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acf07ea3-25b7-3094-9ebf-8815ad81fe59 | -10.43886 | -50.80475 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd1b2435-620b-3610-a45b-6f20c51feb37 | -10.43519 | -50.79623 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9def205-4b5c-3958-b0f2-69c6723fb25f | -10.43481 | -50.79899 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6239869a-47b3-3641-83da-77b88acf1d8e | -10.43449 | -50.80158 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c3f7b81-7a45-3c38-a08b-ba5684e30ef8 | -10.43408 | -50.80431 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f20c05bf-ec1a-33b7-af02-5e75c3852269 | -10.43382 | -50.80678 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 356627ec-3752-3cc8-813e-4e22a2eef09c | -10.52116 | -51.08468 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2667bf81-5b51-35db-8583-951ec0f0cf81 | -10.51968 | -51.08076 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a69b4376-b90e-3426-abf9-2845beb5a1c0 | -10.51897 | -51.08619 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bc183ba-8106-3f0a-9925-c3ddfff3be83 | -10.51653 | -51.08382 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7dc6fc36-bdbf-33a9-9358-8d84c07b87ee | -10.51582 | -51.08894 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a18f87e7-0ad8-3bec-816d-1a209737feac | -10.51435 | -51.08521 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4b7b839-d33b-3646-8f60-72c578dfd00f | -10.5137 | -51.09015 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4878f77-6187-38eb-8e98-2ad7e430b949 | -10.51121 | -51.08796 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75c4be36-7c6e-353c-b563-49f806320ae6 | -10.51055 | -51.09271 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e66a4c6d-c6be-383d-8fd9-712200967eb3 | -6.38467 | -52.70543 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d3381dcc-2a27-31b8-bd85-be7c610c90e9 | -6.38073 | -52.70482 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69834334-2aee-3d4a-9e77-019a59e93b4f | -9.06899 | -53.26939 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8880f288-9f52-3331-add1-d7119abdfe98 | -9.06721 | -53.25369 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e11c75bc-4112-39ec-b32d-bc9b81fb38d1 | -9.06648 | -53.25877 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dcabfe6-4c6d-3867-9409-198f6e29e3b1 | -9.06253 | -53.25822 | 2024-10-02 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85554eff-b907-3663-b7a9-db94151841d9 | -10.90746 | -52.4169 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd1b5f2e-923b-328c-ad21-643ccd9b6059 | -10.90373 | -52.41224 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dca36dc4-ed02-3fd8-b5b7-6b0895c1e029 | -10.90317 | -52.41631 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1c62b03-aa2d-390a-b1ee-36ba178834e7 | -10.90262 | -52.42036 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ff9e221-e288-3b7d-b804-e43974dd8027 | -10.89944 | -52.41161 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9c75b88-c541-341a-852a-0d04ccdb0d42 | -10.89779 | -52.42372 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8deac39f-7614-348b-80e7-8aa38a588c3a | -10.22995 | -52.72151 | 2024-10-02 05:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12c408fd-e128-36dc-8082-9f41528fd094 | -10.22941 | -52.72534 | 2024-10-02 05:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ad7a165-48d3-3048-b683-d5b2aa93c105 | -10.04675 | -53.4865 | 2024-10-02 05:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a81c528-6c30-3a62-beea-287a59d96a0b | -10.03287 | -53.44289 | 2024-10-02 05:10:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70901b92-5b9e-3e1b-8f5f-9004abdfdf0e | -11.84949 | -52.52073 | 2024-10-02 05:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e490b6bb-d7a2-38a9-8ceb-06520de58e64 | -11.08167 | -52.52061 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ed73afa-846f-370e-910f-9fb55f83210e | -11.08112 | -52.52463 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee82463c-1b94-3f0d-8034-b9f5a1636d5c | -11.07739 | -52.52006 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8eab6a98-d2ef-3a48-8c51-caa1403e3748 | -11.07685 | -52.52406 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4bb7044-ebc6-38a2-ba3f-49f61d82a4e8 | -11.07312 | -52.51949 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9c7d331-428b-358d-bc7e-2735d504b7bc | -11.07259 | -52.52347 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cef7b6ff-cad1-3154-b596-20247e202224 | -11.07035 | -52.52072 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 707a3133-7cb8-3ab5-a75e-aaf782a81460 | -11.06886 | -52.51889 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d9bf72b-a17f-3105-a1b9-8ed0a656700e | -11.0661 | -52.52008 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45fbbcbd-99cf-3453-a9a2-3f1c28289435 | -11.0646 | -52.51823 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf713ec4-f8f7-3684-b91b-155be9cb23d7 | -11.06184 | -52.51942 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d2636c8-7ba4-3256-be07-1f4955b16843 | -11.06034 | -52.51756 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a725fcc5-15b7-34b8-a3f4-544a3d820352 | -11.05556 | -52.50223 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e911230-d746-37fd-85c3-e971244639f9 | -11.0513 | -52.50161 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9c5d955-428e-395c-b107-38d7d99c6dee | -11.04759 | -52.49699 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aad2125-2188-30ea-95cb-e18303da6e3b | -11.04703 | -52.50098 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c009f8f0-2248-30c5-82e8-02effc784702 | -11.04389 | -52.49233 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a0d1d93-cfb6-3d4d-983a-281064096ab5 | -11.04333 | -52.49634 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 063b521f-dd53-39ca-bad9-f99d8e26567c | -11.03815 | -52.47099 | 2024-10-02 05:10:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README132.md)
