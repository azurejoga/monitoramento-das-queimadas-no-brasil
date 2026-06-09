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
| bde2ec03-e60d-3f7e-8349-647ccb3daf9c | -10.84939 | -53.74933 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43179246-3f51-311b-944b-b91e9f7f24e7 | -7.37596 | -49.8593 | 2026-06-09 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f81ec14-3ba4-376c-8dd9-1f6973d2edc5 | -8.72266 | -48.07479 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5af612b-3a18-3d49-a7dc-ba7dbdd669d0 | -10.40784 | -44.93741 | 2026-06-09 04:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e96ce872-5c47-377b-8b6e-a66e8db5c44c | -11.58648 | -58.50935 | 2026-06-09 04:49:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccbf0619-2d06-3915-8252-e6a9ab95e035 | -11.44602 | -55.10944 | 2026-06-09 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4869fba9-c724-3df2-b083-6411019c4a9d | -7.59651 | -46.46871 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 74b649b2-45ee-35d7-a5fa-edf846d16ae6 | -7.59321 | -46.47389 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b64c29f-8fb6-3829-b1f9-fea676165b65 | -7.90162 | -47.08686 | 2026-06-09 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 210df7b4-b6ea-38b1-bfaa-d64d49df4c40 | -10.90428 | -49.34808 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2aaa178-9900-3c8a-bd73-6c743332e3a6 | -9.31794 | -45.49144 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e5f3f9f-84eb-3cc2-8b63-d8c68e49b2d4 | -12.33373 | -51.22689 | 2026-06-09 04:49:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 13f78a4b-a5b3-3408-af9c-f06010497779 | -10.85369 | -53.74579 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cedce24-8170-3883-915c-fb5062d9e001 | -12.47079 | -55.13776 | 2026-06-09 04:49:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2159769-128e-36e0-9fc8-663be0a5b223 | -11.54363 | -52.78318 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d8556081-1508-3814-b848-70816cb85f22 | -10.64135 | -49.382 | 2026-06-09 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 67098314-001b-3887-846e-3852561ff2d5 | -12.67353 | -54.58322 | 2026-06-09 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c8e00c1-9f5b-3aed-a549-70115c70795a | -12.48204 | -46.27275 | 2026-06-09 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54f82485-72b1-3dba-9a49-ee33a33969d4 | -9.07932 | -50.61172 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ebf10ab-d228-3126-8fd3-0990f0d12567 | -9.78747 | -47.43845 | 2026-06-09 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cecea68-91db-3857-951a-52a0b1ce9d48 | -10.85078 | -53.74104 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba32e5b9-b160-3f4b-aa34-ea6faf4e2310 | -12.43884 | -58.47295 | 2026-06-09 04:49:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 996fde94-6fa5-38c6-8677-b78368444d6a | -9.07378 | -50.60364 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 696f57fb-0179-3957-a4b3-3fa4f5bb406d | -12.43415 | -58.47203 | 2026-06-09 04:49:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38c024c6-ef62-3c9d-9d59-17272a3387e6 | -11.4774 | -57.11915 | 2026-06-09 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c18ab05-2370-36a0-b624-d2666479f4ff | -14.39941 | -43.80239 | 2026-06-09 04:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f42a53fc-5da1-3703-8fab-b0968cd704a5 | -11.03174 | -44.31761 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee0c8b5b-5ca4-31ab-9d36-9f36b7d720bd | -11.5477 | -52.77996 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aac64f5e-3742-3a25-8d92-245354098e60 | -15.63007 | -42.48822 | 2026-06-09 04:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb84d5c7-c263-3dbc-8958-23aa0456592a | -9.62189 | -49.02739 | 2026-06-09 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b05eda79-ca48-373a-811c-5fba3fe7d8fa | -11.47817 | -57.11483 | 2026-06-09 04:49:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34750177-b9d5-3165-bc3a-6094f4a44747 | -14.30245 | -49.2415 | 2026-06-09 04:49:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29e7e903-2a74-34a8-add9-1ae23756469e | -12.10185 | -45.82913 | 2026-06-09 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26f6e887-046c-3d0f-ab5e-d5fce8823cd6 | -11.57206 | -54.57998 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97a6cf6d-fc3f-3b0c-9ab6-e2fe52dcde33 | -9.3002 | -45.47297 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20363299-8ee8-30b3-a387-c818564eb8c7 | -11.33323 | -51.38997 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69388f33-7b9d-31ca-92cc-12a7228fbb08 | -10.45411 | -48.12404 | 2026-06-09 04:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01b2a7d0-e423-3b0d-834b-3f7fe449229f | -10.91844 | -54.11258 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b66779fa-6ac2-37e3-8140-2c5c9ab49341 | -12.36477 | -47.892 | 2026-06-09 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6489a02-f417-3b7a-981f-d2abbdb154be | -10.42583 | -49.4445 | 2026-06-09 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b456dd2c-8972-398e-bf0c-c3b99431d2ce | -9.30345 | -45.47876 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c38156ad-6b9f-3b73-a75b-03d8af00b6a6 | -10.85868 | -53.73813 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b91734d-85da-311c-ab98-f19cedce41ad | -9.33827 | -47.91232 | 2026-06-09 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2312f91-b337-3fe1-9446-f499710be67f | -9.07767 | -50.60068 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36fa5309-a25e-3e73-98fe-e992150a3dab | -9.08433 | -50.60175 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39b6e75e-d8ac-3a2a-87b2-b775b162e8ef | -11.3321 | -51.39707 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 786d2b68-0779-395b-8688-86c04eac1fa4 | -10.97773 | -47.74294 | 2026-06-09 04:49:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| abbde3ca-e6b2-3be9-9c6b-77656c76024a | -12.84981 | -44.39202 | 2026-06-09 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f4b7f18-78c0-3f3f-a6d3-4a0be450c6e7 | -11.33153 | -51.40062 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e06b597-6f71-3017-98cb-c72cbc564caa | -11.44986 | -55.11013 | 2026-06-09 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6be7762d-87a8-31c4-8299-f4e80f339bfe | -9.33768 | -47.91624 | 2026-06-09 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9afba367-d0f5-341d-b7c3-dc8ca07859bd | -11.57578 | -54.58068 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a4fbc44-a3ae-3bfa-bc87-288014afa984 | -13.25379 | -44.39399 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8f9c9ead-a94a-3b30-8527-cbc2440949b0 | -11.95778 | -48.53282 | 2026-06-09 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fcf98f2-d3f9-3c80-ac70-721a67dedc40 | -9.07988 | -50.60822 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 640aa37e-1527-349b-9989-20e7b44f362b | -11.61778 | -55.18491 | 2026-06-09 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b1fbd2-68e9-3822-97c7-945d75135f72 | -10.71345 | -56.24697 | 2026-06-09 04:49:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ca5d1f9-81fc-3a14-b684-d29e9c114083 | -15.79833 | -42.02419 | 2026-06-09 04:49:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8ce5bfe-e7c9-3613-be9e-38f2ed21cbe3 | -8.54985 | -48.17282 | 2026-06-09 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f3bb09-7bdf-3ca5-bad6-bffc3f76fe17 | -9.07711 | -50.60418 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f184c6e8-c1f2-3f08-ac7c-152ffddade1e | -10.64417 | -49.38614 | 2026-06-09 04:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7f4e661f-dd18-324f-a939-d44f6fe6f87e | -13.36576 | -43.20098 | 2026-06-09 04:49:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3dd0cbf5-e649-3c5a-980c-863b0c8d8c4b | -11.02849 | -44.31961 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00ed7084-5004-3909-888e-5a111cc5b041 | -7.37762 | -49.84886 | 2026-06-09 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7231fd69-2e44-3f8c-ae8b-5a2f4bd99992 | -12.05749 | -49.75826 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b497263-7147-3940-9eb2-8a46d0abaa10 | -10.88127 | -49.54128 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 113a83ec-afd4-3ad6-a666-9581388cbe44 | -13.25318 | -44.39877 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7d1a448a-6727-33c8-ae60-88c11bf75c52 | -7.59388 | -46.46956 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f81aa4e6-a947-374e-9ffa-f7941e053402 | -11.54707 | -52.78375 | 2026-06-09 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7bc9d3b7-177f-3fa2-ae3f-b1776ee1fdb7 | -12.05637 | -49.76553 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f1c4e24e-02c6-3855-8cb9-9ec076f64cf6 | -9.52232 | -49.5811 | 2026-06-09 04:49:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 090f79ae-bde0-319b-8679-7a22d4b47b5a | -12.48534 | -46.27821 | 2026-06-09 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4f5d53e-dda2-3378-9ac5-6c2ec29a5156 | -11.8317 | -49.4383 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f729bf4d-7687-3070-99a9-53a764b29ad7 | -9.30745 | -45.47931 | 2026-06-09 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 939f0650-c32f-3241-a820-4292fcda9842 | -11.26487 | -53.96678 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5b9d00b-265c-3c07-814c-8942cabd661c | -12.47385 | -55.13667 | 2026-06-09 04:49:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45009807-cb8c-3ea9-8506-8631dfb5bb9c | -9.11123 | -47.96255 | 2026-06-09 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f3d08f-5fab-3053-94e4-b3a2e02436d1 | -7.5969 | -46.47445 | 2026-06-09 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05291342-7cb9-3d0a-b597-507b02724122 | -9.07045 | -50.60311 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d61c5350-f4f6-3df4-9fae-e27b4dfe9415 | -7.91407 | -47.10144 | 2026-06-09 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9215e96c-c444-36dd-86a0-2b0275105f80 | -13.25734 | -44.39732 | 2026-06-09 04:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 01b3afe9-183a-3e90-9d48-976a99669e93 | -8.74342 | -49.46641 | 2026-06-09 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5eed7cd4-bf3b-3b5f-9ea9-96c6f85ec990 | -9.78387 | -47.43792 | 2026-06-09 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9c533ca-96d7-3b26-b3bb-5597f7f746f9 | -12.0558 | -49.76916 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44c372d6-3fc9-3d68-957d-eb7f074d2510 | -10.89301 | -49.35376 | 2026-06-09 04:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdd5114f-309e-3faa-9d40-92d187f9315b | -11.62896 | -55.00943 | 2026-06-09 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 070e3112-864a-3856-a1c7-6a613035fa8e | -12.10119 | -45.82819 | 2026-06-09 04:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ff11f9-3273-327b-8b9c-426a90b1fb53 | -13.11076 | -51.71923 | 2026-06-09 04:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cc776a5-ac4e-37a6-bbc0-4313d24ad9d0 | -11.78404 | -47.33294 | 2026-06-09 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23a32d3f-bd1d-3413-a980-23c74a7d78da | -10.57262 | -57.32283 | 2026-06-09 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc137eeb-b975-3b74-91a0-851221ea362e | -11.57501 | -54.58521 | 2026-06-09 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5567fff-d674-33ec-8931-809cecfd9417 | -9.74844 | -48.22221 | 2026-06-09 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc288519-b59a-34a3-a35e-08cd1ee43900 | -10.77551 | -54.10034 | 2026-06-09 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 961335f6-f52f-31f9-8f04-7c7117df96c6 | -12.85279 | -44.36909 | 2026-06-09 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f425fc25-e219-3ab2-bf83-02657de8f198 | -9.07599 | -50.61119 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 200b9f09-3d44-3e7b-8853-68b1e016f1a0 | -10.4292 | -49.44504 | 2026-06-09 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cb8f326-f576-3a1b-9710-7698caaef59b | -9.79342 | -47.44781 | 2026-06-09 04:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1da11b0f-880f-30f1-9d80-e4d15d352c11 | -9.22149 | -48.56869 | 2026-06-09 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79827cee-50bc-367e-b4eb-a6c81d41b330 | -9.071 | -50.5996 | 2026-06-09 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| aca0582d-b49a-30e2-9b68-6f7e7f9ff37a | -12.05243 | -49.76862 | 2026-06-09 04:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README11.md)
