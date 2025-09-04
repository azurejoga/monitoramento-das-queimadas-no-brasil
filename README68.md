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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e09c6593-3a3b-30fc-9077-b1760396e05a | -17.613 | -43.76357 | 2025-09-04 04:55:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a5f571d-2d7c-3177-a53d-c4e026709985 | -14.28964 | -53.09428 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cac0fe0-dca2-38bd-a2d6-d28f1281c2ac | -12.97537 | -54.76105 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1159cff-969a-37a4-80b4-f1197613f9c8 | -11.62457 | -52.19297 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16f89602-7a40-35d9-820d-ee39fa13fe0c | -11.85393 | -51.45127 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf1d9c9c-349a-358e-8d9b-2846a2be39ec | -10.08936 | -54.76066 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 443b31a3-9acd-3e37-975b-f199f89663c8 | -15.15956 | -52.38853 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bcdf962-20b7-30d7-bb09-e78bd86c53a6 | -13.45168 | -46.94078 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d151da0b-bc29-3c00-bf4c-14189e79852f | -11.21098 | -55.0818 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bf5022a-8f32-3541-baf2-57d1705510c9 | -15.04481 | -50.08244 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ec203b1-48c3-3d68-a742-5b488afc993a | -16.00558 | -49.28011 | 2025-09-04 04:55:00 | NPP-375D | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff26349e-3e99-3244-97d0-970197b51b9b | -14.56881 | -54.55194 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cad70dee-2dc6-351e-a4c9-2b1da0f0c894 | -14.20091 | -48.08742 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b4eb611-0f19-300c-ab34-e364ebd14dfd | -11.19626 | -55.02293 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9051784-9adc-34ed-914f-f31c577c7728 | -10.48107 | -53.64539 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 589eaed7-2338-354d-bb00-05ac74144b0b | -11.6579 | -54.52215 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fe1b325-45c2-32c5-bebd-541b3c23be4d | -11.95336 | -58.73306 | 2025-09-04 04:55:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54e73107-bd79-349d-8631-b92af370fe60 | -12.11069 | -45.21213 | 2025-09-04 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d2cf321-acb5-3d20-8f9e-0e05103136d0 | -12.43926 | -48.71169 | 2025-09-04 04:55:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6594c7d7-cc05-3987-a2d5-132ce4533740 | -13.74533 | -46.94724 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92204501-8ade-306d-bf03-23df3ebd6f04 | -16.3105 | -45.70473 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21e5f262-0ad0-3413-81f1-5a9e7a264de0 | -16.46443 | -49.51586 | 2025-09-04 04:55:00 | NPP-375D | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1f7b397-93fc-3ece-8d1d-630f6f241672 | -12.98647 | -48.06811 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12d65013-fd9f-3cfc-b795-9b938a22d3ba | -11.24439 | -44.96004 | 2025-09-04 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32d9469b-326f-3e71-8f59-1a8d2edc8105 | -11.59224 | -52.15391 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d33dce3-6d8b-326c-a91d-0786ff03e1d7 | -17.17606 | -46.25592 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0bd8aa2-c3b3-3b0a-a1fc-62f371586090 | -17.73217 | -46.1676 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20ace1b6-668f-3a89-b943-df7126c1faf1 | -12.11584 | -45.21288 | 2025-09-04 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7290dcaa-b7d9-3393-8467-94334fa8d4eb | -11.63709 | -52.2019 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0af7b5e-6485-3012-a964-5a3cd8c1ea64 | -12.88724 | -56.95088 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2ee2166-ff28-34b7-8af3-6d92ef5000b1 | -16.31098 | -52.95245 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cec8d911-255a-3f2a-b687-5dd123e4bbd5 | -12.46302 | -48.0737 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3de7a6ae-4816-39f1-be82-b9a62783bb9c | -15.55178 | -48.39741 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c2d6ff0-413b-3788-83bc-41669017fa28 | -15.30579 | -52.75776 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dd7ef20-a8e1-3594-b6f5-35d8ef98ebad | -15.60965 | -52.89331 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 258755b0-917a-3e56-a694-90b5c41bce2f | -15.04431 | -50.05766 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46b334f3-1759-3ccc-ae2c-bb97dfa5b315 | -12.9089 | -56.99741 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03eaa092-cfca-349c-899b-5ac8fd2e99d9 | -13.09897 | -57.11391 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccf64aa6-e46e-398c-8924-66cb56a036bb | -10.09876 | -54.78846 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b818bf9-f6d7-3f2c-8a80-a482e6516940 | -15.74217 | -53.63085 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dcb8824-df5b-385a-9e8f-5dd81bb19e07 | -14.05856 | -54.01132 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2416178e-ad42-3f9f-bfce-f636ca4619b4 | -9.69357 | -56.73231 | 2025-09-04 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f356f150-a857-332e-8ab8-847bac7f4caf | -11.5894 | -52.14968 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6004f488-7315-3421-a9c0-581231db4cde | -11.58204 | -52.15229 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa4fcbce-8af4-3362-898e-e2a1d36565c0 | -15.74161 | -53.63452 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b198298b-6ae3-3ef0-b1c4-73c08b64ce08 | -12.90383 | -48.04671 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37666575-39ba-39b8-bcc6-9449d719d43c | -11.60322 | -47.78212 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5fa956c-bc1e-35a8-acdf-8df1fe497918 | -10.47609 | -53.63379 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 089f0916-a198-3b67-9cc7-35dfefb00807 | -15.05471 | -50.04006 | 2025-09-04 04:55:00 | NPP-375D | NOVA AMÉRICA | GOIÁS | Brasil | 5214705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 123167e0-2f40-36ae-8c91-f5effdc3c48e | -15.01063 | -50.04281 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22de0db6-3cc2-36d3-b1c8-32b6d11150a2 | -15.04364 | -50.06247 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0f796d7-1421-33d7-ac26-5cf5af2b7c81 | -16.31327 | -52.96069 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37d67860-05f1-3a1a-8028-19ce7cf8456b | -12.49284 | -53.8409 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5cacd5c-f299-36b8-bbba-9d08f60f9373 | -14.5199 | -53.14148 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbdf7721-37c6-34c4-8e49-6cd2000001df | -11.60287 | -47.75317 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 902d35ef-1e15-3d76-bb5d-3c4b993fc733 | -14.57172 | -48.05232 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 43e16098-5235-3e74-920f-563df6e80568 | -14.56937 | -54.54837 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30ecd026-634a-3b2d-bc41-0dcc9d144f8e | -11.63989 | -52.18339 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a1c1025-139b-311f-8873-4df8f6b5d066 | -16.96733 | -49.30506 | 2025-09-04 04:55:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abaf45e6-e219-3ff1-9ffd-8d7109e8b0ef | -10.11053 | -54.80163 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a5ad0ee-9e82-30d7-b58e-2e27b7f1b34f | -11.62801 | -52.19291 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10942fc0-b3ff-3849-bda9-2cd834f88da8 | -13.09827 | -57.11808 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59cdbc12-e7bb-3140-9e36-946c1275ae1c | -14.52555 | -53.1499 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e01a4824-3b9b-35e0-9958-8ac619e41acc | -10.48218 | -53.63837 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e810c39-9b86-3312-a42d-6ba4c40dbdc1 | -16.31727 | -52.95743 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52dc999e-0ae5-3b7d-8d1e-1d7d971dd2a2 | -15.41461 | -55.93846 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a24711fe-c6d0-394c-a25c-71d57679abeb | -15.17329 | -52.35399 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4553b68e-ac4c-3acf-8965-f1162e01b063 | -16.46798 | -46.86821 | 2025-09-04 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f816d233-d90d-3fd3-9cd8-df86101bce1b | -12.24193 | -50.14272 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b0574f8-3e15-3a0b-9ccc-58a8efb03635 | -12.90284 | -48.05406 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcf7487d-6f6d-355d-b797-a5d90fb558e5 | -14.5608 | -48.06713 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b82ea42-9ea7-34f8-9c9d-244a91175246 | -15.02048 | -50.02902 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e6b0030-5d05-3c51-8045-60c5ea3bd09e | -12.90434 | -48.04283 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96e1f875-5886-35d0-bfb6-dff38cf80b99 | -11.64729 | -52.20346 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3525a338-cc53-3c0a-92eb-8255a1098bbd | -12.17869 | -53.88423 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df67e2b5-25df-3587-81d8-baff3d52ef21 | -14.56774 | -54.53712 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c802fa9b-f912-3ef1-a587-f5f75b2220e1 | -11.58715 | -52.16445 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a324ec26-9733-34a2-924b-aac77dd814d0 | -11.53774 | -54.48776 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5efa7afa-ba8d-324f-819c-e8d099099bad | -17.04214 | -47.14097 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d20a445-fa42-3fe3-90b7-cdb242e4d503 | -10.87565 | -55.73878 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e4b6c16-9519-3f0b-b942-e554174ce616 | -15.41123 | -55.93785 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03130670-3c45-3e07-ab99-fc75a91e70df | -11.60472 | -52.14069 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b462466-969f-35b0-88f1-209c0c9ef3a6 | -14.9995 | -50.06607 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db0ad296-cb2b-3f43-a610-e16f41c5a661 | -17.15737 | -46.22496 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef984720-c3bb-3feb-9c67-b972a2cad755 | -12.88933 | -56.93847 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d2a99a0-0b81-3958-8dc3-dff0411f5d72 | -17.16133 | -46.24768 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6096ac8-c00c-369f-b34f-705488cde9a3 | -14.54072 | -48.0498 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64972ceb-e3a9-3b7a-85a0-1bb513c9292a | -10.09553 | -54.76545 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 532ec35c-ba7d-32f5-9195-16ab03d411a9 | -12.91468 | -57.00695 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc2266ed-de44-3616-bcb5-a10ef216adf2 | -12.18146 | -53.88831 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9c7c2ce-8262-3152-8b49-fd1eefa40014 | -11.36538 | -46.87487 | 2025-09-04 04:55:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ca35b48-f9ce-3431-9403-039b2a155d1f | -11.6847 | -52.20933 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68c397d7-8762-3f83-9707-ba1b53ed5433 | -13.00268 | -48.07782 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b3772c7-37ee-3713-9f7c-04705ac09aaa | -12.52503 | -53.80987 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21ae1ec3-f10c-3991-8eb8-09e25f8d8a29 | -13.29821 | -46.8437 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9f2e53e-c739-3897-9434-b1a5743ee69b | -17.0487 | -46.49162 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68ae631c-d63e-39ce-8041-02fbe752197b | -10.09612 | -54.76181 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16fe238d-ffc7-3a73-830b-7253943f40dd | -11.67899 | -52.17818 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1fcc0a1-be80-342e-821b-d77dee313e94 | -16.29618 | -45.68946 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa6973a2-ae29-350c-8b2e-46c104d9166e | -14.28821 | -45.22573 | 2025-09-04 04:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README69.md)
