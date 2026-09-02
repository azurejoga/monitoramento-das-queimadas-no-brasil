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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec451065-37cb-3a08-aa40-6eb1ba8e38c0 | -11.36143 | -45.41433 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91934cf6-c1f3-36ab-b741-1419fed23d4a | -8.45035 | -54.69796 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d37daea3-4587-3b1c-9064-96f43877156f | -9.70538 | -47.2009 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb6eb5af-63b2-348e-907a-2dbfa3c04e0e | -11.67839 | -46.73634 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50c29953-e7b5-38ea-8f47-67d1bafccd41 | -6.94803 | -56.45374 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 833dbfca-dad8-336d-bacf-2e9e99228849 | -10.04733 | -48.68922 | 2026-09-02 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1ab449d9-882e-332f-8d45-674dd302a49e | -9.45777 | -56.74108 | 2026-09-02 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1cf9f42-810f-3249-b711-9c5431ba3b77 | -12.13847 | -47.1375 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 267cb7b6-af56-3adb-be7e-ea2265a32b7d | -11.91603 | -40.66279 | 2026-09-02 04:21:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c24da89d-c001-3e5d-a227-d55b13ede9c9 | -12.12865 | -47.09177 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0d52789-54ce-35a9-81be-9ff0e88b5636 | -9.72031 | -48.13998 | 2026-09-02 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d629f41-bcfd-33c6-ad38-e2536974affc | -11.12078 | -51.53259 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39305e0d-8298-3e03-9c90-e93324a600e2 | -8.4681 | -54.72291 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2d42d6e-50da-3778-bb57-5ac973621e7b | -11.667 | -50.19459 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4391ec2d-87b4-3ce9-8ab1-b786f5336127 | -7.41349 | -49.73762 | 2026-09-02 04:21:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6245be47-1156-33f7-a151-f04e8e8202a3 | -11.31027 | -45.17121 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8da8d028-7527-3647-9223-6e1078a68cbb | -10.04375 | -48.68867 | 2026-09-02 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 364e8a8c-f19f-3778-af88-51653cfca972 | -11.12146 | -51.52877 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc946a79-ce1e-3f3e-935c-da8a936f9222 | -12.14572 | -47.13501 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61209064-f78e-3e80-8c71-1e2794ed8901 | -8.48449 | -54.70807 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 3f851ee1-6032-3e99-b569-10690da75300 | -11.82933 | -46.05729 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f9f842f-99a0-3350-ba98-b3c94b4c6d6b | -10.90351 | -45.34136 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77fa8079-9fdb-3fcb-92c5-81a13858c58b | -14.97466 | -48.11986 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2848373-6962-39d0-afc0-b209aab21ca6 | -11.91733 | -45.09118 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2b09df4-d693-3574-9619-71acc596e561 | -15.6771 | -45.89458 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0019536f-e424-3ac3-9a5b-a1d6d04c3827 | -11.66485 | -50.1845 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bec33ca4-d4bc-303d-8787-f4d370d971c7 | -8.48199 | -54.70726 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 29e81099-6645-38c3-9375-9078a9734dd0 | -9.3923 | -51.68806 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48d76e16-9e5d-3bad-9489-d4facd280b7d | -8.44822 | -54.74076 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c6a1f8e2-fc2e-338f-8f18-2a4a85ab0601 | -12.64627 | -47.08866 | 2026-09-02 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16c5da4c-cbdb-397c-b00e-dc7b9b72f97c | -8.4418 | -54.7146 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d937d03e-d80a-353d-86d2-9feaadea8d1a | -12.14458 | -47.14217 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3bb237d7-f633-32c3-a54e-ed66d4f8b647 | -12.1315 | -47.07389 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 592b021c-79a3-369d-a8a8-70a048de722c | -8.12498 | -54.9582 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 069a9f8d-954a-3991-bac6-9d2e76320fbd | -11.35268 | -50.62936 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3245d020-ef55-35cc-8869-82adc560b9c5 | -8.50202 | -50.3011 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee19e884-89a9-3913-b285-fd1129e23ca1 | -12.64294 | -47.08811 | 2026-09-02 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 335ae788-6569-3d0a-94c3-dafd9017d6f6 | -11.12494 | -51.53332 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bbac766-aabb-35af-bdc3-1a43d2ec5166 | -9.66649 | -46.52896 | 2026-09-02 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22421b14-9f6b-3c9d-a4ec-9147412f8e87 | -11.34399 | -50.63304 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5182880-5ea4-38de-83c6-b1bab18d80b2 | -10.74611 | -54.032 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd04dfd4-ed21-3e64-bc9d-c51a3c135243 | -11.66106 | -50.18384 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cebb572b-f7fb-381f-8b0c-aee73835f60c | -9.46465 | -50.31115 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c297a4c5-5ea5-3f5f-b3e1-bcb0b33ca00b | -10.44241 | -46.72087 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b02b5ba-a022-324b-80ab-51362ada02ed | -12.09026 | -47.09647 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abfe67d4-b483-3059-a72d-cbba954addc8 | -8.45259 | -54.71642 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb378c39-9c2d-34a6-8ee9-65e1c97d0bc9 | -10.71864 | -46.22255 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fc8b917-d38a-37a2-a13b-c956204b4ef9 | -10.78216 | -44.76088 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| bd25148b-f4bf-3200-9045-a9d91bf92da2 | -9.15405 | -49.97701 | 2026-09-02 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b7fd9b7-c673-3fbf-86f9-afd066d7a4fa | -12.18048 | -47.08543 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e537a3aa-be1a-3314-9032-1b6c9f98322d | -10.32471 | -49.94685 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4405b5fd-c553-30e6-b5ff-c22a46640738 | -13.76189 | -45.39893 | 2026-09-02 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85324528-c197-3316-b7e4-f16d2b02409e | -9.93828 | -53.99043 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08ab01e7-17f9-33a1-af2d-bbe8df4b8ca1 | -15.3441 | -47.04318 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7e9df7a8-0f1f-34ff-a2ca-d0325b4c96b1 | -11.3257 | -50.5987 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5870e81-8096-3898-9c2b-5bc0a61fd1c5 | -12.13962 | -47.13033 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8f7e8ba9-d38d-3bd2-b875-602128dc26d2 | -12.17199 | -47.09891 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a793d9f5-951e-32ea-8f0e-1d6b034e3c54 | -8.76937 | -46.43869 | 2026-09-02 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff3818e3-76dd-3a20-8321-0011ffb00da0 | -11.01991 | -48.38163 | 2026-09-02 04:21:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1633a584-df36-304f-9261-85fd1b448f54 | -12.34948 | -45.66213 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cdf0b67-4170-3b9a-b0fc-11604c8fbbf8 | -7.55414 | -55.00025 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eabec133-8a5c-3562-adad-4c9df5c45191 | -8.48011 | -54.71783 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| dc9b4744-8436-3ed9-98e3-815ab6917f32 | -12.14321 | -47.06481 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b23ea236-34b7-320f-a5c5-6ebd818aebd7 | -8.4671 | -54.71196 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56171bbf-0baf-3a6a-8604-0a68b81a28d8 | -12.13321 | -47.06317 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bbd954e9-083f-39c4-90c5-d69ee19a44e6 | -15.34797 | -47.04016 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e790fcc0-e373-30a9-baae-dad60b86b594 | -11.72239 | -47.63128 | 2026-09-02 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9baf7cac-f310-3fdb-80c8-11dd751a4773 | -11.83319 | -46.05431 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a7b57a31-a921-3105-91c5-e6db7f3c8774 | -12.46918 | -41.31629 | 2026-09-02 04:21:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f386e217-8518-3724-8d40-b722a6ee5456 | -11.83304 | -46.74742 | 2026-09-02 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a23f62ee-4760-355f-93e9-f72364076d44 | -10.99836 | -45.0785 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 836cf81c-064e-3c21-b2ce-247c7be7f9c8 | -10.74985 | -54.06783 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a425bbbb-a819-3e15-8535-4d6d025b7a7f | -10.32171 | -49.94146 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 183dd656-5946-3d85-9c90-af0d9fc96ce3 | -11.66481 | -50.18691 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bfab3762-e946-3e8b-8982-5ed13e4ddf3a | -11.30918 | -45.17831 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d6e2d31-3e5e-3a81-bf22-bbba406b0f4c | -15.34073 | -47.04218 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51755cc7-bcec-32b2-9ffc-46109256b139 | -14.80566 | -42.39212 | 2026-09-02 04:21:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 129417d2-83b4-358c-ae5d-dfc5d3320c18 | -11.79598 | -47.67728 | 2026-09-02 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 558e8d23-d528-37eb-b916-f4b2a77822ce | -12.12768 | -47.05495 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c81c3ea9-ed03-31e9-93f3-076c353f0378 | -11.14797 | -51.57299 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44050dec-8e38-36b3-9c23-bfd1415e9bac | -11.00168 | -45.07901 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 587149b4-7721-36c6-821a-294d5a6379d0 | -8.70722 | -52.36594 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 347ab1d6-abbd-345e-94c4-cf2ef222e127 | -15.07476 | -47.99033 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd62885a-1587-3ae4-932a-44255f6cb787 | -11.16962 | -45.5993 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46e964c4-f687-31b1-84c6-471e5b84e0d1 | -9.14655 | -40.50817 | 2026-09-02 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7051083d-fb33-3af4-af25-c815fa047348 | -8.46986 | -54.72699 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b58361fb-6e33-34c6-961e-d70799440d64 | -11.31468 | -45.16462 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cabc374e-3e27-35d6-b63f-f14a4677337d | -13.41364 | -43.8753 | 2026-09-02 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 31a7e7c5-ce0d-360f-83b5-8c2645d3a930 | -11.05198 | -51.52488 | 2026-09-02 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e5caaca-4ba5-3e77-a208-a3f914603026 | -10.78884 | -44.76196 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4892d0d-384f-39c8-b3a0-0e4d4fbe1f06 | -10.35201 | -49.97108 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00dda77d-96cc-33be-8c99-ee3f66ae710a | -11.48276 | -45.0892 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3bdb0258-0769-3381-a08c-6c75bdf6ab1f | -10.7488 | -54.07362 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9d34f01f-b083-33bb-af7a-72acc23552df | -10.78774 | -44.76909 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fa22f9c-783a-30a3-ac1f-14fc07e51cc0 | -10.43851 | -46.72387 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ef47703-e9e8-3372-8c4e-b927d073bc31 | -9.94329 | -53.99126 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21dcb5a6-6f0d-32bc-beab-72edf95118e2 | -8.45322 | -54.71288 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16a0d001-2e63-3241-a600-b21e260c6bc6 | -6.14906 | -57.75005 | 2026-09-02 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e735e850-889a-330b-a338-ef94e1b72a35 | -13.41014 | -43.87476 | 2026-09-02 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3961101d-71cb-32ac-b1eb-25a8906f1c8f | -12.08014 | -47.11687 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README23.md)
