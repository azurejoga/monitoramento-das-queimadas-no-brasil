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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb64e036-be5d-3e48-92fb-2b4867c77583 | -5.12398 | -55.94921 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d47764da-3da2-3158-b325-72170b8416c4 | -3.0849 | -50.56913 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f85af0cc-c1a6-34a1-9a2e-0668cbc10ac7 | -5.13398 | -55.93586 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 362da38a-9e1a-3e6e-bfd2-ad0d5b7a761d | -2.63955 | -54.69033 | 2026-09-16 05:33:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8f2be98-0e79-3b64-bdd2-b0bfa63dd308 | -3.74073 | -55.94613 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 191492a0-9c46-3254-978c-7207e60bc8e2 | -2.95694 | -50.40802 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 210a645e-ac7d-3705-b17a-804c603b07c3 | -2.63315 | -54.18645 | 2026-09-16 05:33:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4c5485b4-f334-398a-b9b3-25b2ce6e02ce | -5.46249 | -60.22256 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aa850bc-c3d8-3d32-9267-5961feac4b80 | -3.07615 | -51.19961 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23661d9d-f35c-3843-996c-7e12102fbc12 | -3.71501 | -60.61752 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8ef5693-ca40-3615-ac7d-5f3dd80912fc | -2.10233 | -52.05103 | 2026-09-16 05:33:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ace07945-daa2-33a3-b751-cff4a1854dae | -2.91611 | -50.41956 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 493e0f88-0848-3120-8bcc-ec8d612d9b6c | -2.91328 | -50.40133 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f9e5eb0-d506-3552-ba19-17c8ce09ff89 | -4.83981 | -55.77043 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c6c223-b54c-32f3-ab28-1788d380dc03 | -3.58552 | -58.54571 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c58ef828-b997-34b1-8425-e392a5589857 | -3.07999 | -50.56493 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e34dc9c4-4d08-32d9-a571-0b70fc0d7c9a | -3.4246 | -58.23608 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 666fc60f-980b-3611-8c85-2476c86ec26c | -5.88965 | -52.08978 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e61c51e5-6c73-3d6f-8531-cff155f2526e | -3.59458 | -59.06678 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 650e865e-0cd8-3034-928e-8cde515ac3cb | -3.81201 | -58.89848 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1f554ff-a1ed-3444-a078-0db260d35bf6 | -3.17559 | -61.11005 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63af48bf-dbd7-36e9-9843-b96f54667208 | -3.18291 | -61.10756 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7d70e01-6258-3677-91ce-056c019f6a42 | -3.45912 | -57.99265 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 953e2373-861a-316d-881f-5dd8fe0051d9 | -2.92156 | -50.4204 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ee8344e-ddbb-3cbc-9546-e48551d5d08d | -5.49176 | -60.16679 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90fdaeb7-0862-31c7-a872-2830866c610e | -2.95149 | -50.40714 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 685b2006-bc27-32eb-9c15-04dd589a1fd0 | -3.43393 | -57.97352 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4c24fcc-05c5-3bdf-9173-84e92b28a297 | -5.99389 | -52.10567 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72ea826c-8240-3229-b45e-8b9118b3fb25 | -3.17677 | -60.08813 | 2026-09-16 05:33:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21e0a146-3ca1-3529-b99a-215615e2d411 | -2.90313 | -50.43176 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0595c647-44a7-3822-ac10-203766d73cc1 | -3.84806 | -59.33172 | 2026-09-16 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ce85195-304d-3b9a-844c-702dab68005d | -5.75301 | -57.59832 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef1c1f63-6dc0-3a2d-b6d4-9bba8d8a1cbb | -6.01743 | -51.7956 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15069888-9ead-3d45-a08e-678534e867ed | -3.42575 | -58.22878 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c1eb983-3695-36ef-855e-eda0f90ebf37 | -6.78508 | -48.65984 | 2026-09-16 05:33:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eb27e5f-016f-355f-87e8-5a11fad283be | -5.48781 | -60.12707 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3768b74b-1869-3651-b153-e5f8f8bb48cd | -5.48449 | -60.12655 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 79f03e77-9fcd-3046-b120-7b5a23bfca81 | -3.7011 | -60.6189 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2258295d-92c5-3e9a-a464-8015cd57faba | -3.58947 | -58.54265 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba6c7de0-aa4a-31bb-b891-d344b5e3269b | -1.28407 | -55.71879 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3988b61-0672-32a6-866a-f85061d86774 | -2.90573 | -50.41441 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f18c193-5c3e-380e-81e6-bf9fea8c6d7d | -3.3738 | -61.33267 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dedd55c0-4d4a-3e5e-9530-aee4d73bac96 | -2.91066 | -50.41872 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a9a2433-ce0b-3dd9-a517-a4f5eeec42fd | -4.99727 | -55.94156 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b583229a-436f-3b80-8d70-c565297753bd | -5.13481 | -55.93272 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c1fb462-f8f6-3fa0-a02e-7d1a404dcd70 | -6.07717 | -57.86136 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d9aa132-3ceb-3dc3-9482-e173dc09f9fd | -3.45283 | -57.98787 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e98d8c27-88ad-30d8-9caf-c09229d9a355 | -5.14096 | -55.94209 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8b152e5-f1df-38db-97f5-fec7b405faa3 | -3.42519 | -58.20999 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a750900a-fa55-3945-831c-a217af866e04 | -2.96401 | -50.39839 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 508932e9-46f7-3215-8030-19a65c26b5d3 | -3.59285 | -58.54318 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86071dcd-9ce6-38cb-bd17-16b9c2981b86 | -3.59341 | -58.53959 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a33fbd1-4c28-33bd-b9c4-aeb2accdacbd | -3.81257 | -58.89494 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f3962a6-960a-3ade-9bbe-2dc291bfe4c2 | -3.59059 | -58.53547 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cc15e95-4bab-3b09-ad0e-a21c4210dbd5 | -3.38649 | -50.39183 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24dfdb64-9415-3b3a-875b-1b3ab31594bc | -5.86076 | -52.03725 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b87f53e-f04f-33bf-ae2e-f6268efd0127 | -3.81537 | -58.89899 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73b9db31-ee44-369a-b4ab-5a50d8eafff4 | -2.94497 | -50.41326 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09409287-b798-3e6e-b75c-77efdf921188 | -3.37387 | -61.31052 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee70507a-c361-3309-a8db-a3ca6b4ea7a9 | -6.28467 | -56.03614 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7323b28-76e3-33fd-93ba-3fd9452010d6 | -3.18234 | -61.11112 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a817073-6e12-38f3-aa2f-37098e514204 | -4.53435 | -55.62418 | 2026-09-16 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 897e663c-3f22-3578-89ab-73ea00f1dceb | -3.01697 | -51.33985 | 2026-09-16 05:33:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0fe35d5-4e56-3d7c-99ea-00ff5332dc45 | -3.04499 | -61.26976 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db1ab436-34f2-3136-8d58-e3e7a232a4e5 | -3.11007 | -57.68386 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e6a95cd-6a42-3fa1-847a-ca69db20d2c0 | -4.43984 | -55.51514 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4070b60-dff3-3fef-a73c-877889c5bc49 | -3.39378 | -50.45431 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b77b0869-c859-3c12-9867-5c619bdb771c | 0.14752 | -60.39405 | 2026-09-16 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cafff529-9ed9-319e-8721-4d24d7247b00 | -3.39777 | -50.76378 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 512ea553-7206-3217-a31f-5b7c2834a9d6 | -2.91171 | -50.41179 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc754977-9cd2-356e-a977-d08ac9b5771c | -5.14255 | -55.93407 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5868ef3-b4e0-3978-9483-442cc5d02c53 | -4.46449 | -55.06012 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25f6fee9-edcd-39cf-91cb-582a2025f943 | -1.28547 | -55.70997 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94734c0c-7b3e-3860-89fd-ad8b41f73f0e | -6.36946 | -55.13403 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18615062-4695-32ee-8018-a8ebd9a93bfb | -4.51919 | -54.94773 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e560880-ec86-3a62-ae8d-d89237d61c76 | -3.51357 | -60.41478 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33b5d91d-e87c-3b45-880f-83f9a0f97324 | -3.09828 | -52.2076 | 2026-09-16 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0afa47a0-d476-3a9f-80c2-bf4b415b6066 | -3.72834 | -60.5982 | 2026-09-16 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3244f293-c5d1-3c73-8fe9-2162abc0b1cd | -4.33958 | -46.61059 | 2026-09-16 05:33:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ded5d245-c5e3-38d9-b832-26005e84d4ee | -5.75362 | -57.59429 | 2026-09-16 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fee0a444-bcbd-30dc-b9a0-8e28f22b4bf2 | -5.15176 | -55.92553 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6d1a72b-af0a-3eca-a8a2-d29c97169fdb | -3.38461 | -61.30854 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2effad9-3e9e-3900-9b10-5a1a2901a61c | -4.52462 | -54.96684 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b801e6f-700f-304a-805c-361642a94e08 | -2.90625 | -50.41093 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 695e93f7-d4ca-3f2e-8a50-fcd8b3d5d4c6 | -3.29312 | -59.46201 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc80a5c3-58b2-3a32-940e-3d82e645eea6 | -5.07816 | -56.24629 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8306c3a5-9fa7-3619-b08e-bab1c1089a66 | -5.14483 | -55.94268 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f978b69-c002-3d55-ad53-663e1951d8c5 | -5.09945 | -47.61779 | 2026-09-16 05:33:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 15d18eb1-da85-3b3c-b5cb-e2e597e4862d | -1.74294 | -55.25414 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3175b0ef-ef4b-3fb1-ac22-b08a8331e85d | -3.07949 | -50.56829 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2f24b6b-1bab-3dab-8794-df49fadeadeb | -5.14958 | -55.94022 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 915b7171-0341-311e-98a5-1e060b0f17b1 | -3.72296 | -58.87372 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c3244da-c41d-3af3-8f54-944662ec6a77 | -3.57566 | -55.5974 | 2026-09-16 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec03c800-ad72-33fe-b8cd-73e4b11c9707 | -3.18177 | -61.11469 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 629fb27c-76c7-3cd1-b5f1-411846a79c9f | -5.23995 | -59.98468 | 2026-09-16 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ab0ee3e-22dd-3257-8f03-cd3fb64c8f0c | -3.32865 | -59.44616 | 2026-09-16 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb56211-2e84-31a1-a663-90047957650a | -3.58664 | -58.53853 | 2026-09-16 05:33:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce82c742-8571-3ed4-b8b8-038eb8062603 | -2.8633 | -49.63152 | 2026-09-16 05:33:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| baa5bc44-34f5-3479-908a-3bb57ba5035b | -3.19392 | -61.21197 | 2026-09-16 05:33:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b4e5c7a-0f7c-3a37-ab00-52e83bea1ee3 | -3.69604 | -58.8806 | 2026-09-16 05:33:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README54.md)
