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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfb8f850-1671-3d0c-b9f1-b9983623af9c | -11.70917 | -54.5421 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 38d71bdf-f853-3b0f-aab9-1672ed8de9c4 | -12.19825 | -50.55571 | 2026-08-29 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d76719c9-cda5-3455-93df-3a455919cf9a | -10.74787 | -42.10408 | 2026-08-29 00:07:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| bcd6c728-3908-3f48-81b4-0a2b860d5c08 | -8.606 | -54.83617 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 7481bfeb-ae92-36ea-8143-06f4ce9da656 | -14.26793 | -57.03465 | 2026-08-29 00:07:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 8333a06e-134e-3902-9c98-a2f7b0ae6769 | -14.27965 | -57.04024 | 2026-08-29 00:07:00 | TERRA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 9118961e-eaf7-3129-a2f5-40c7728131c4 | -6.49914 | -53.25814 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| dc3705a5-c0dc-38d8-8d06-e2e49abe9606 | -6.48805 | -49.91015 | 2026-08-29 00:07:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 169b4117-94c6-394a-8448-d5818ac470e1 | -8.95087 | -50.79905 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 104a6d6c-93f0-3455-8d5b-df4145661fc4 | -8.79339 | -49.99604 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7612590f-4a3e-3ff1-84c1-41c560ac5126 | -6.01393 | -45.80709 | 2026-08-29 00:07:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3a46c113-66d4-3c5f-b098-aec36e66ac1e | -14.19578 | -52.86383 | 2026-08-29 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2d0c3b24-fe5c-35b6-8ac4-a8fae8559ae3 | -11.18998 | -51.28601 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7896d34c-df24-3d5c-b2e2-88e7aa307591 | -11.2185 | -51.29177 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 00bd30e5-5019-35b8-8fec-eed7386a58ee | -11.2688 | -54.02046 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 587de934-6fa7-3e52-b244-8d9e9c0d0bf9 | -7.28752 | -49.96532 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8178f1ca-bafb-3f01-b14a-e8768292fcd7 | -11.01196 | -51.39733 | 2026-08-29 00:07:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0faa4b1d-456d-3b2d-a676-2a27f1ad6680 | -13.16997 | -55.66321 | 2026-08-29 00:07:00 | TERRA_M-M | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7460e71c-fd94-3635-bf49-c3bdd7f0a936 | -12.22381 | -50.54268 | 2026-08-29 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 328a1068-25f9-3b02-927e-81e6e70136e0 | -7.28888 | -45.86123 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| adf62809-dd18-3211-96a0-2d0a5973b8b2 | -10.9197 | -46.61778 | 2026-08-29 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 99302c9f-9190-3383-a75f-2fecd03c50ce | -7.27715 | -45.86951 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| dc9bf2ed-8111-3b87-8ba1-7714ce068005 | -14.17204 | -52.84124 | 2026-08-29 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7716191c-8c8d-35fc-a797-f3cfef21d57d | -9.29645 | -47.62705 | 2026-08-29 00:07:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b0095942-00c8-3b0b-8c6e-b717a21da859 | -7.28821 | -45.8678 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| dd2a5389-9b09-3146-8848-327610b23ae8 | -11.04603 | -57.23751 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c9d74718-9e5e-33fc-b361-d27fb9db81fa | -9.20751 | -51.54052 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6fa639cf-22ca-36b4-9977-671856df9582 | -9.96897 | -53.94165 | 2026-08-29 00:07:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 1f09cc16-35ae-3126-8763-61129fc8e86c | -7.50502 | -55.27374 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8f8fa036-6037-3536-903f-30a42d5543a4 | -11.48979 | -46.95026 | 2026-08-29 00:07:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9b9de9b5-1d2b-3043-a496-5e9af4d934a9 | -8.50357 | -49.55972 | 2026-08-29 00:07:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7abc9351-37f5-3c51-8ee4-49a48961693e | -11.72048 | -54.54068 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| feb81c24-4174-3c02-ad24-e1c76456f9dc | -11.26381 | -54.01308 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 828386f7-3341-34b6-8637-c0f43e3bef67 | -11.96852 | -45.48663 | 2026-08-29 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 20e8b9eb-a79d-3efa-8d5e-de2e53058890 | -10.89995 | -46.62075 | 2026-08-29 00:07:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 1257fa12-cdb8-3d23-b1dc-b86ef7a5095e | -10.7556 | -54.05344 | 2026-08-29 00:07:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 3d684f25-9906-3ea6-8407-20da403f3bf9 | -9.70007 | -46.55395 | 2026-08-29 00:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 13a33ee9-9e55-3e57-9416-c8370bbf90d2 | -11.27047 | -54.03421 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 6a5e307c-bbb6-33af-ba89-b6c5e28cfaae | -9.96405 | -53.93641 | 2026-08-29 00:07:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8104e16f-e836-30bd-96a4-8b487e1ea6f6 | -8.59676 | -54.7653 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 009dc005-614c-3322-97c1-a604c2c694c5 | -7.49567 | -55.28993 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 7a02350b-8d40-3306-ae44-e2e7368b2d90 | -1.25665 | -55.70812 | 2026-08-29 00:09:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 91215428-468e-38f5-a125-aa465cd2073f | -5.03398 | -51.94226 | 2026-08-29 00:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 65207f93-e8e8-35f0-9b41-1ce020332981 | -5.88733 | -57.79427 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1d35fddf-4128-3ec2-994e-ae516138fc5c | -3.44004 | -52.76147 | 2026-08-29 00:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a1eafa18-eb40-3ad5-b78f-ab6ef49de764 | -2.50351 | -48.12797 | 2026-08-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d4ccd598-142e-3a0d-a533-51d2a28dcce1 | -3.82626 | -52.4159 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 76987141-7f12-3d4f-99a2-ac122569eed3 | -6.73752 | -55.45869 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 287.0 |
| 633f9760-b8a3-334d-93fb-e4bdfd5582fc | -5.78609 | -52.32696 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 50638793-7abf-3675-928e-d04556a8021e | -1.2015 | -47.76493 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| c87d32ae-7b03-3198-b9de-fc848fa9ce1b | -5.88624 | -57.7552 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 176.4 |
| d0394aa2-1c2e-300d-9dcf-30245c2b0cb4 | -6.28056 | -53.1419 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 91750987-3bd4-3e8d-a4e5-934c0d165a04 | -1.20735 | -47.76991 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 02a2775d-6460-311b-805b-3ccc9cd2fcfb | -6.54966 | -55.23816 | 2026-08-29 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e51dd615-a5e1-39b0-8ccf-94126edf4547 | -6.55145 | -55.25237 | 2026-08-29 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f1e4de6f-49a1-3833-aea0-0afd6cddbd2e | -3.33308 | -52.52073 | 2026-08-29 00:09:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 93582c71-ca45-3ec5-bcc6-6640eb14fa2a | -4.91934 | -48.98883 | 2026-08-29 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 40d33138-7132-3cb5-bcc7-50b3ae396bc9 | -5.87579 | -57.77911 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 511702d8-a354-39fe-94b1-1dd75e17c20a | -4.28382 | -48.1973 | 2026-08-29 00:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5a34f8b5-8b9f-3d7d-951f-6229e1a7ab7d | -2.72995 | -47.04554 | 2026-08-29 00:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c61691ed-45be-3849-bf5a-a3007d3fa51c | -1.19963 | -47.75199 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b7dc0e23-4835-3444-a93f-94e338a8f5ed | -3.97644 | -41.52463 | 2026-08-29 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 52434f71-82d3-30db-999f-637ccb37fca4 | -5.26056 | -50.96741 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e5b57a37-e251-385e-8101-41fd2d514151 | -2.49342 | -48.12936 | 2026-08-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a5ef1eef-4176-391a-98c4-c42533df4737 | -5.89525 | -57.74886 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 68e2c39b-30f6-3f5b-85eb-1144d5cc344b | -5.31923 | -47.0509 | 2026-08-29 00:09:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d9ae06c7-e054-3970-8412-97121037b140 | -3.16349 | -54.62681 | 2026-08-29 00:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| c2169795-e8de-3bfb-b994-c7e9d67ceca4 | -2.59958 | -49.33741 | 2026-08-29 00:09:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8b06fad1-e0da-34af-8450-2f9b35a98a26 | -3.75141 | -53.36113 | 2026-08-29 00:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| cfdc428e-06b4-3fb8-b25a-835ad046fb5d | -5.16578 | -45.43227 | 2026-08-29 00:09:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b33e60eb-4757-3e9d-a168-61711be46df1 | -6.5864 | -55.44567 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| db83cdb4-3f0f-3b10-846c-bdedaa11def3 | -3.93669 | -59.33475 | 2026-08-29 00:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| a12a681d-b0d7-3e46-8e65-17c39a7c5321 | -4.70044 | -55.66895 | 2026-08-29 00:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a6003d0e-90ad-37a0-aaa5-07f4705dc09d | -6.16023 | -57.78627 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 6136e825-7d26-315c-b6e9-537d241e52ba | -5.22917 | -52.02258 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b3df2c10-24be-3b08-8317-8539cab18064 | -6.5863 | -55.43933 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9ea57da6-c41d-3996-b3e2-8900537e383a | -6.32484 | -54.74234 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3d557272-df05-398c-876e-178e30c3eded | -6.15201 | -57.79382 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 0bbd2c15-1dbb-3b3f-8b7b-2f62863f036f | -3.82502 | -52.40682 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4d8f36c8-0273-3c31-af18-dc52f3f4f78c | -5.36964 | -50.57027 | 2026-08-29 00:09:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa4b1cfb-93ab-3f42-ba66-42932964b938 | -2.98768 | -48.95211 | 2026-08-29 00:09:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9a2c979e-1ecc-35d5-85a5-181d6ec71f9a | -3.87301 | -48.04068 | 2026-08-29 00:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f8606f66-9ecd-3ae3-b8d5-cb4205d0c795 | -2.49509 | -48.14117 | 2026-08-29 00:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0b21a681-6dca-398c-8b0a-e3d2dc251e68 | -5.9789 | -57.68772 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8445ee98-a31d-34bd-b8cf-fc68837fe8af | -3.15353 | -54.62819 | 2026-08-29 00:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 6ddcd647-c875-3d93-b46a-6c125c060cc7 | -6.17371 | -57.78459 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| bed62240-b53f-3d8f-bf51-87c33db1569e | -3.8746 | -48.05189 | 2026-08-29 00:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 05196c6b-0e91-3b95-9382-995adebe3741 | -1.20558 | -47.75694 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 735d8a43-1222-33eb-8f71-5d29cbf039a9 | -5.29328 | -50.94494 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 98b4f0ca-eb33-3e33-8649-198067ccbc26 | -6.28095 | -53.32787 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eeb9d74c-f6d7-384a-9bab-c488a956116c | -4.05882 | -56.28856 | 2026-08-29 00:09:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| bfa1644c-c391-3c80-bc36-76cae0e5f1e2 | -6.32652 | -54.75535 | 2026-08-29 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2d077a4b-3244-367e-b135-abbec9b26afb | -5.29208 | -50.93618 | 2026-08-29 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f262530e-5bd3-3bce-b8ad-cb7c35d84c87 | -5.89796 | -57.77037 | 2026-08-29 00:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| e1e5bd89-62be-3df1-9e2b-49608a24718a | -5.03276 | -51.93327 | 2026-08-29 00:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 30652454-85c0-319b-a2f0-75651586f617 | -5.33514 | -45.16455 | 2026-08-29 00:09:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| a8bf288f-de0d-3c27-b9dd-f196e1f748e4 | -5.30878 | -47.05235 | 2026-08-29 00:09:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 86e121b5-030d-36e2-86bd-960968ed3fa2 | -6.75581 | -55.68782 | 2026-08-29 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c806deac-669b-3898-b8c4-2728ef590229 | -6.54826 | -55.24467 | 2026-08-29 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 1ba8bf47-b7a8-3578-9495-8426aabf1b9e | -5.04287 | -51.94104 | 2026-08-29 00:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README5.md)
