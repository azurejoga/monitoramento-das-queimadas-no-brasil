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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcb02041-dc17-3c6c-b1aa-981191f24a30 | -8.1417 | -43.66083 | 2025-09-14 04:40:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e221f8c7-8ea4-3f27-b168-cb8aa1ad3f41 | -13.93372 | -44.85324 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 6e4685fb-0d3d-38eb-baab-07538d3855c2 | -12.78323 | -48.01925 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 13822501-543d-350c-9914-077d27a88795 | -11.45735 | -50.76601 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f42e496d-2aa7-3905-804e-734f45555304 | -11.44165 | -50.47251 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6a5c408c-f3ef-3a86-920d-7db75076ce87 | -9.24734 | -45.66267 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3926a0c1-70db-3872-89b4-4c529e6c1d76 | -10.35029 | -50.4904 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d17385b2-5688-3dfe-9eff-18d295138974 | -11.87063 | -50.49158 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91998569-80ca-3aba-a040-f55ac1f99644 | -10.92182 | -45.57811 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a63d4f9a-97a4-3bc1-abd0-961675d092e3 | -11.46618 | -50.7961 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7815ee2b-1819-32ee-a4fd-7e557295f2d6 | -12.9475 | -48.02946 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f132c429-9c1c-3ed4-81c1-356276597a08 | -11.34463 | -50.83344 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55f965f7-d943-3c8a-bb44-bd1427f3ed6b | -12.9624 | -48.05283 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a4f457e-5892-362d-b291-5adfa609e55e | -8.94994 | -46.18449 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 324f1ace-0aea-37e9-ab41-e38998f35aaa | -12.95213 | -47.97159 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0152f39c-c343-36c9-885f-71441c63cf75 | -12.72674 | -48.03165 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77ae7762-fada-31b3-a42d-f5aa14f739fd | -11.11565 | -50.68923 | 2025-09-14 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30f24dbe-e788-3499-aa4c-d110e84b5f58 | -11.23505 | -47.62883 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8fa55e1c-9811-32df-824e-8025b37e6c27 | -8.64194 | -44.04007 | 2025-09-14 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82a8d46a-2ef0-37ed-b8ce-11600637a36c | -12.57623 | -45.65975 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3227326-6757-34d8-b305-e79f39b49297 | -12.04299 | -46.54824 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c97ef42-4fc8-3eb4-b92e-b3ce633a5a4c | -12.757 | -45.94477 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3eaa23cb-e417-3338-8fe4-99c14299733d | -7.85148 | -46.09884 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29b6b0d7-e433-31e8-8b48-bf73d46da805 | -7.56949 | -44.381 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d909a3f0-2d1c-39c2-8a0c-61f478036506 | -11.44416 | -50.7854 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f36141a-09cf-32ab-a5ae-85a56f3e4bb8 | -7.21835 | -43.96983 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ff0dedb-37ca-3fdc-97e0-a2a6132c1e03 | -11.86678 | -50.49457 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95581908-ea7a-3026-8b73-5c5ebcbcd1d9 | -11.39018 | -47.34227 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9f7b875-67fa-3584-af5c-391bcc2cfc94 | -9.00024 | -45.76268 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91080e2b-bc72-3c90-bdaa-dca0920febea | -11.24122 | -47.62884 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4484042e-f476-3229-a142-d89571f494e4 | -11.45395 | -43.56538 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 38356d5c-256f-3312-8a8f-1829d428f964 | -11.45954 | -50.75201 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5e9277d-696a-3553-a6d6-63e89a106e28 | -10.37286 | -48.24044 | 2025-09-14 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 955c16e1-a218-35f6-af79-1ac4d7daf165 | -8.41153 | -47.24518 | 2025-09-14 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81e4ae19-e593-366f-8a61-3402f0486c54 | -11.29739 | -50.82942 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d62ffe9-1bbe-3824-9735-18520dc70a3e | -12.78146 | -48.00636 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 34d19ac5-63c2-3506-aefa-cdf533f0c15d | -6.68992 | -45.51985 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fb8e4805-ba5b-3fa1-9af5-d42c82846825 | -11.45681 | -50.7695 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e52904ef-ae35-3d1a-9bff-4c56842c3407 | -8.08306 | -44.51097 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b4ee52f-36c0-3bd6-9c16-5aecc1e7e95a | -5.7356 | -49.30158 | 2025-09-14 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1c2d768-c995-3a76-80de-97d64f296069 | -10.76209 | -46.47189 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16503953-e1ee-3f4d-b35c-11f1d9b08e47 | -13.92877 | -44.85698 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c13344b-1c26-3be6-b27d-5712da08dc8b | -8.76932 | -46.04404 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bb33cbad-a215-37a7-824d-788912325532 | -11.48544 | -50.80278 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0667389-35c0-395a-8a27-48a40ef378c4 | -12.81495 | -47.95227 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e13d3db0-cf4f-3ce7-a9c8-72fa37db8193 | -11.48543 | -50.78127 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbe20daa-5424-3b63-9be8-44ab00f7cb99 | -11.46396 | -50.76707 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f00cdaec-6f92-31fe-b77c-b892f7e9327c | -10.13361 | -47.18978 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f29dc2f4-dcf2-37a1-8b08-89f2017b3927 | -12.78263 | -48.02337 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31ddc0d2-2260-31cf-8c58-a541b3832378 | -11.40087 | -50.45164 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aca2134-91b5-38d3-bf38-b3163672e6d4 | -12.04205 | -46.54568 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5042a4b0-8206-3518-93aa-68dff9dda752 | -8.76516 | -46.04637 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5470482b-c63c-3a19-a20c-333d9fe10838 | -5.23561 | -56.01818 | 2025-09-14 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15d13481-0b63-325b-b2b1-9007bbd6b554 | -11.44965 | -50.77194 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83faf499-91c2-37fc-ba7f-7764477eb9bb | -8.96118 | -46.18641 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9a57a0b-7efe-3ddb-8fdd-382ac88e3ffe | -7.27238 | -48.67267 | 2025-09-14 04:40:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d829bd4-2422-3f42-b91d-1a3d863921ae | -11.46231 | -50.77756 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45c92041-8497-3092-a35c-c7459f3edbeb | -8.80869 | -47.13205 | 2025-09-14 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96753f41-1443-345f-93d2-306781c25da1 | -9.62349 | -40.61615 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 419755b8-c855-32a4-bace-0d170fc02989 | -7.31212 | -43.91909 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4656bf7-24e9-39b7-b5f8-d35037c2c1de | -11.49037 | -50.77131 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| edd477cf-3291-307a-8ab0-59d023b7dfe2 | -9.8609 | -46.4679 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2cd300d-ae26-358e-b2c0-175f62850772 | -11.46756 | -48.69815 | 2025-09-14 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| af96cd87-9bbb-334d-942d-86673463478b | -10.75943 | -44.7744 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdf0da7e-93fb-369a-8270-76cd72edb60c | -11.86348 | -50.49404 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff33987a-5726-3f31-8ac8-af8af1a38b1d | -6.56154 | -44.47277 | 2025-09-14 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eb64093-15a2-3001-af95-df348e16c78b | -11.9143 | -46.52762 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 572dc310-465a-33c1-8ab6-228205384c82 | -12.96832 | -48.0117 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9b3053c-9126-3ed9-bc09-398367c551cf | -11.45626 | -50.773 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26458ac2-6c7e-3b2b-8562-5ac2b32625ba | -12.78488 | -47.98286 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fefb6307-c80f-3b83-ac92-8847c92387e2 | -7.61243 | -46.70367 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d852d667-599a-3ba6-8dd5-39ed174b897a | -12.93076 | -47.95159 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 859b7171-a946-39a1-a2b6-d24cb6d2e73e | -11.49645 | -50.79738 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ccd8e50-0d43-39ab-b827-239625932e2c | -11.39443 | -47.33849 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18eb9267-7b84-3e14-99b8-5c91f51a86d3 | -11.44141 | -50.78137 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 275cd912-8e85-302f-8a15-4a660a1ebe0d | -11.40857 | -50.44569 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fe1b6be-a163-3609-a961-9d15b51ce5fb | -11.47551 | -50.75816 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8db51fe3-2205-3966-9505-2ff4e4d2c3ff | -11.48156 | -50.76272 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6497bd60-7217-3715-bbb9-e52a42173250 | -7.48027 | -46.12617 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b220761-65f6-37a8-b25a-32c59abd28a7 | -7.51523 | -44.37659 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6482956-7f2f-3554-9ac8-e87e5516e5e6 | -12.93373 | -47.9563 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 998e4848-38b8-3130-a546-1aaf39657773 | -11.4656 | -50.75657 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3c08724-9356-33c8-ad4f-6e47c8e4a2a7 | -8.19063 | -45.57306 | 2025-09-14 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21eb7f54-7700-359a-a2de-3836b90ef857 | -10.7626 | -44.78252 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5154a115-dee4-32d5-8794-a6d0a36ada4a | -10.3522 | -48.82005 | 2025-09-14 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 479fa481-3898-301c-bc3e-be744527485e | -12.91022 | -46.54854 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8bb3bcc5-1668-3e14-a220-036e9db68436 | -10.90032 | -45.46502 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 305554cb-0b87-3e0c-bbf7-10328178bc47 | -10.35468 | -50.48396 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 532d15a3-5e37-36a4-8236-c46f929eef60 | -10.90123 | -47.20665 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e71e5efc-b30b-3eb3-a11b-846c3bf8140b | -11.48873 | -50.7818 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bef49d47-cf6d-3daf-a7d3-2e6dfdf4155e | -6.8831 | -45.62869 | 2025-09-14 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd6dd042-a1fc-385f-8e4a-0e7586d7fa9a | -11.48488 | -50.78477 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c2a42d6-2564-3d8a-be6b-1eddcd202089 | -8.98517 | -45.78498 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9774e7c-ae34-3493-9a27-8346358ad959 | -9.85584 | -46.4764 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a704739d-4e0e-3066-b2d1-0af3d8615147 | -12.7309 | -48.02806 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 2a72ee26-ceda-36fc-ae48-95ad680ff8d7 | -10.13075 | -46.1549 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb753f8c-2ca6-39a8-bbe5-4361af875797 | -11.665 | -46.51132 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0526ef93-62df-3a2e-821a-18adb2fbe820 | -12.95929 | -47.97269 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3f9013c-03d7-3e0c-9eab-452850efcdd2 | -10.40838 | -48.60891 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fbf59c5-160a-3e3e-8bd9-44e4e0c9fa67 | -11.28898 | -51.10084 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README40.md)
