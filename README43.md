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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2a4b710-928c-3c4a-9d7b-de908fa81d60 | -14.42387 | -44.87468 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f396fe2a-7f3e-32f5-91a0-0f1952ac38e5 | -13.7902 | -47.93534 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6821d504-5c28-3a9f-b084-a30cada32cd9 | -12.01406 | -47.95015 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54d55cab-bf19-330b-99c5-e9c53cd1ed4e | -13.35542 | -47.81772 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b618c7e-9a7e-3bcd-827d-fa4f7bd63abf | -12.74017 | -48.36192 | 2025-09-29 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4317a32c-099d-3f1f-bb91-f0ffa8d28e14 | -14.5754 | -48.27799 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| faa334d2-6aa1-39ae-950c-a09585eed1eb | -14.54622 | -48.44002 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2e178b0d-2001-3bf4-986c-9fcd7ff72c28 | -9.78334 | -46.93571 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3242db7-207c-3827-a2b3-eb5396733ed7 | -11.92169 | -48.04807 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e384280d-e132-39d3-821f-216d66be2b8c | -15.28666 | -49.50849 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb32860b-9325-3a3a-9c71-9a837a65ff02 | -14.44289 | -46.36214 | 2025-09-29 04:08:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5de2f557-aeb3-3b2b-8b67-bb327ff97d56 | -13.00019 | -49.43752 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3fd7b58f-de80-3375-95c6-68833144420e | -12.98068 | -46.28248 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b8ff050-acec-3a7c-841c-41010cce53d1 | -14.5651 | -44.97893 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1c35e44-0057-3636-8d68-7f1ab24dda7f | -8.42109 | -46.85662 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2dd9221d-e12f-341c-803e-cb8230f5a973 | -10.79942 | -45.36513 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9ef8535a-b124-3a28-afe8-3c53e779e289 | -8.81523 | -46.19839 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc8fcd02-dc8d-323e-a1c5-7e70e6c010d3 | -15.26361 | -48.75649 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 34085d28-9820-3ab1-9ac1-16962ceb3965 | -13.27097 | -48.45761 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6bd9173-7304-342e-bc15-fcd5125b50fd | -14.62296 | -48.28718 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92e7f47a-6e82-3e80-9f9f-280ddd4b1023 | -12.28202 | -44.10714 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d51da47-a14d-3a81-8450-c03d28b2254b | -11.37464 | -44.93815 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97c9108b-ded9-3796-a87f-88b314100595 | -15.87561 | -46.22312 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01426d64-4bef-3de3-9b67-c1bdb59c7983 | -10.38417 | -47.80082 | 2025-09-29 04:08:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df3ef883-e88c-3b40-8671-9f307d9796ef | -12.94684 | -45.16838 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcc395b0-7b31-314b-8694-90e2dfef5925 | -15.22296 | -50.1078 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea6042fa-58b5-3489-a1eb-876cb53bea55 | -11.65369 | -45.33282 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bec18019-8cc8-35c2-b15f-6b2fa2424221 | -12.77016 | -46.8542 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5830ebc-b1ad-37ad-8c2b-144447ed48b8 | -11.69432 | -44.40035 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccd297d9-e131-3a2a-bd60-90401bcb7e01 | -14.57407 | -48.23981 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b65b8ed0-38c6-34ef-9fb4-a909d13d60af | -12.42235 | -44.22067 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27ee2443-0c42-3eac-bdab-dac52c2084e5 | -14.74795 | -45.67525 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3013f376-334b-3894-b048-b7d9e563c0d2 | -9.77851 | -46.94015 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| acba21ca-d9b2-3f7f-a87c-57808f666da5 | -14.08844 | -44.09354 | 2025-09-29 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2676b39b-4b69-39f4-a9db-3563c2b29776 | -11.83466 | -51.79306 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 31703bad-c2f7-3c63-940f-3e7ed38c7db4 | -11.61955 | -52.8487 | 2025-09-29 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2788bf8-33b3-3420-8f59-5dfaeeabf968 | -10.40484 | -48.14809 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0437619b-c9ad-33d5-bc18-3b2299cd23a3 | -10.39991 | -48.15146 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 221445a0-408e-39df-a3f3-6b41bc8ca8f6 | -11.96794 | -48.04372 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54ea1152-eb9f-310a-9281-52c41a8b4e10 | -12.83482 | -46.88535 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b587494a-7c02-3b25-a035-ec2476bd4ed6 | -9.46859 | -45.49038 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a759c8f-fe4d-39be-b5f6-9407036e85d9 | -8.64363 | -44.83617 | 2025-09-29 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6a5aaed-9ce3-3e77-968d-ebf15ee7796d | -12.88229 | -46.99207 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dbebd39-1454-3156-96fb-d845fd80cec7 | -8.88665 | -45.04968 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ffac20d-31d0-3206-9509-28af69e68b09 | -13.75733 | -47.91458 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1754d30a-cd51-3366-896d-a412af8f2bf1 | -13.7385 | -47.88794 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32e5db70-2039-33be-bccc-eee7513b3da5 | -11.26623 | -48.93702 | 2025-09-29 04:08:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cde2018-a665-3670-ad36-dadcd32df19e | -12.80238 | -47.75385 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 466aac6d-8246-3186-9cd3-23a17705f531 | -12.87178 | -46.78389 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 151f548f-12b8-35fe-acb3-a3e87bbf687c | -14.67813 | -48.15424 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7586fcc8-f3f1-333e-a7d8-3c00bc694fcd | -15.27735 | -49.2537 | 2025-09-29 04:08:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecd65566-c446-3cbe-8be9-4654bdd33f00 | -15.11528 | -46.44399 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b800f654-70ce-34fc-a820-9a69ced5231b | -15.25893 | -48.75924 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6f2558c-d9d2-3d8d-bf16-cbc1d225d38f | -11.42708 | -44.95425 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 050ac706-0dd4-35c0-bde0-d2614e6f632c | -11.65723 | -45.33331 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f56f8c9-32b0-3101-b1d7-6b8b04e0d2ac | -15.29022 | -49.49289 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79e71aea-83f4-3536-a1f2-e11ab65c2d70 | -15.21585 | -50.09703 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 918780b7-dd3f-3d3b-9d4d-28df9b22894f | -10.40184 | -48.11539 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49e50f16-63a2-356f-b9cb-01ac276468cb | -11.9417 | -48.00588 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00028c77-35ec-3148-90cc-ae5c74fb38ea | -14.84217 | -45.57023 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e3666fe-955f-3fc3-aace-ade75160fb08 | -11.72165 | -44.42738 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01a542ce-ce8c-3b59-a74e-c19c5b032292 | -9.38523 | -47.61669 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b137b72e-e80f-3934-b869-f299d0d7ab31 | -14.54885 | -48.42538 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d6af442-8535-3845-8e85-f324594b33ff | -13.5535 | -47.26663 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0355569e-e86a-3c34-a10f-125ad486faae | -11.26878 | -47.19529 | 2025-09-29 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 7b088498-01d0-301a-9d80-14771d46faa1 | -12.6729 | -46.87666 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25d89197-0f68-34c8-acbd-06d6f7382869 | -11.86587 | -56.8843 | 2025-09-29 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2184add9-5f37-39ec-b1c6-c685a3f749aa | -15.24662 | -40.44573 | 2025-09-29 04:08:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5200ab71-723c-3ca1-a197-dc5ce99c7a25 | -13.54547 | -44.17265 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53ff6671-9845-3f70-bb0b-6428659c0931 | -14.8842 | -47.21629 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 764356fa-0d41-3938-9ead-1d5118c33a9b | -12.79843 | -47.75313 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc5c04b6-4e1e-3019-8009-31c53d181b1f | -9.08824 | -47.6236 | 2025-09-29 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7fd2664-1e9c-3138-a36d-740ff3719aac | -11.93782 | -43.92062 | 2025-09-29 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a74e9b2a-598f-3c8a-8a9a-183b00284da7 | -12.35153 | -54.15254 | 2025-09-29 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cdff6b5-37a9-3697-92bb-4a50d57a0837 | -10.79533 | -48.91485 | 2025-09-29 04:08:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16703350-84d7-3dab-b988-f73c6a88510a | -12.6573 | -46.92221 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e661436f-1b00-3f0a-8101-c760e9d5d26f | -13.63966 | -47.32839 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| adf5081a-605a-349b-9f46-90adca92216d | -9.99499 | -45.41205 | 2025-09-29 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 927cfe3a-5701-3557-80d3-241a1d215be3 | -15.18882 | -48.47628 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13936c36-452f-3a46-b1ba-bf56e062fd8e | -9.94191 | -43.63435 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d4d27cb-1be5-3f6e-a524-c17f741c8a4c | -14.82653 | -45.45216 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 812e54d6-0f80-3514-92f0-7eeae01ef190 | -13.76334 | -43.9799 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5424bce6-aa26-3791-8e94-05332ad01e8e | -9.96019 | -43.58532 | 2025-09-29 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b91edbc7-fd10-366a-997f-e63d48319d97 | -14.59035 | -44.99487 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4815816-538a-3843-8689-7ef9a5f57e0c | -15.86257 | -46.83291 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db69a85-dd86-3489-a503-fdc340ab6a2e | -15.54539 | -47.87982 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a249b68-13f2-38a5-a2a1-14b4e6602772 | -15.61146 | -46.25879 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c459da0-dcb8-3231-a99c-5aa0a5894840 | -11.98108 | -47.1278 | 2025-09-29 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d94d03d1-fef8-3422-8886-e905dee41ac5 | -9.43523 | -47.59822 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8e1f1b0-484f-3b38-ad85-c8cfec70b6b7 | -9.35683 | -51.48613 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff352c5a-0b2d-37fa-89d8-caa25cc40a0f | -12.02227 | -48.34571 | 2025-09-29 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5db5b25a-434c-3a9a-97b5-dd90ab560628 | -10.00579 | -46.69415 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23af2398-7f4a-305f-b79a-2ae7deb252fb | -12.86 | -46.96345 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a93bec8-e073-3f73-bd10-e98a54a222b4 | -15.16368 | -46.41835 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ccee8b0-d557-3ffc-9b38-b2f746a29478 | -13.24178 | -48.45504 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e149415b-3d15-3e24-a768-33a41171b9ac | -15.85739 | -46.24122 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7412fdc6-e1a2-385c-b71e-11b20f17a2b9 | -12.94075 | -46.77084 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c5301d2-1413-36e3-b420-88db2271de23 | -13.61558 | -47.30927 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f63c9593-8a0f-32b8-b2a6-bf678ded9010 | -9.86457 | -47.73739 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 713842da-9a87-30fa-b900-5d8731912de0 | -9.05768 | -46.73194 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
