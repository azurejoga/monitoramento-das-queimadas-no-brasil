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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8337cef9-9413-3cb2-9074-6f43adcbb069 | -12.4189 | -46.949001 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fdee6fa-0c39-3b3c-b09a-36d3678f5aa5 | -12.4157 | -46.935101 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e72586b-4803-3171-baaf-9b3de4878d0c | -9.151 | -40.107498 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| cbed85d3-0b8d-3508-b9cd-b20449e1a39d | -6.5915 | -59.892899 | 2026-09-24 00:38:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3357d48-9cc5-35e3-812d-5aa792376f55 | -8.4582 | -51.478001 | 2026-09-24 00:38:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b87dd76-2a72-3531-ac77-84e09f8d645d | -8.4539 | -45.912601 | 2026-09-24 00:38:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c02d97b-4102-32cb-8ced-aee553be000e | -11.9487 | -50.739498 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca72b8be-d359-3bf4-8df8-054d62931bad | -14.9606 | -47.536201 | 2026-09-24 00:38:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c196fdb-60c2-3c21-ab4e-b1ceb39fee5e | -3.0449 | -46.926601 | 2026-09-24 00:38:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d595d25e-0d9c-3038-adfa-df4a47f8d023 | -7.3997 | -40.564201 | 2026-09-24 00:38:00 | METOP-C | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| cee1c92e-a4c4-34b4-a96b-6e1af7150b9c | -15.4744 | -47.910198 | 2026-09-24 00:38:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9341ee31-9431-3bae-b8cd-2d999d36fd3e | -7.2739 | -46.7854 | 2026-09-24 00:38:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b31cd688-94b1-3f7f-849c-027165146781 | -10.9389 | -43.841499 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c78fd05-a94e-3ab4-9467-33f4bc341493 | -6.6011 | -59.8909 | 2026-09-24 00:38:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39e67b2f-8df2-344a-8f5d-c165b5ace836 | -9.8552 | -48.509499 | 2026-09-24 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46c93be8-c4cd-349a-9a6c-cd59886531e7 | 1.6034 | -55.950199 | 2026-09-24 00:38:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8a88cb4-4c66-33ff-a94a-621f558aee15 | -8.9258 | -45.943501 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d5959b9-0bf4-3631-aa37-e1076aa0b596 | -12.1306 | -47.360401 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f9bb871-d76e-3a20-a432-e7cbc5cd3830 | -9.5773 | -40.324799 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fffe8ab5-fd00-395d-88b1-d4adc65d6998 | -15.2362 | -43.257301 | 2026-09-24 00:38:00 | METOP-C | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 7cb5c6c0-372e-37c3-a21d-41e08345db61 | -12.1518 | -47.362801 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf2e8542-9787-30b6-ab6b-09a1d0767d4a | -6.7778 | -48.663502 | 2026-09-24 00:38:00 | METOP-C | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 395fd9bb-3e58-35ec-abac-8c123a4565fe | -8.9338 | -45.9338 | 2026-09-24 00:38:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ffc2917-634c-3f8b-954b-7b04c1e6b2fe | -9.3973 | -40.306702 | 2026-09-24 00:38:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0df678cd-9ac0-3594-aa86-6651bbdec096 | -7.2706 | -45.534302 | 2026-09-24 00:38:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47a333e4-64d6-3f09-b898-7d16601151eb | -13.0592 | -47.411999 | 2026-09-24 00:38:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e88238b-511d-3ef3-ab3f-5814d7d6b660 | -6.4042 | -46.1982 | 2026-09-24 00:38:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 807dd676-bc10-3053-9adb-665a521f9ae4 | -10.0993 | -46.016499 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a0782fd-ee57-32f2-a6dd-673059c65230 | -14.959 | -47.528999 | 2026-09-24 00:38:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a0125243-4184-3e37-abf8-974bb5809a5a | -10.0878 | -46.0116 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7fafb783-17d6-3d47-960f-5da0473ddb6c | -12.1031 | -50.742901 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 435ed21d-f431-3e05-ad2d-bdbb28bcb944 | -9.5955 | -47.772598 | 2026-09-24 00:38:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3cbae87-d729-3e57-b0db-c21cee9c13d3 | -10.0962 | -46.047798 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67bbeb15-2417-3cf7-8ab0-78100cd5295d | -4.304 | -49.118301 | 2026-09-24 00:38:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe10b5b3-0fbd-3e0a-9b84-aab936ee7029 | -8.1141 | -54.8106 | 2026-09-24 00:38:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6906c93f-8559-32cf-9972-7bac1477c5c3 | -3.1481 | -54.593498 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb61baa3-f517-3537-b924-dd45fa12d6e8 | -12.0482 | -50.296001 | 2026-09-24 00:38:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 387a2778-cdd5-3c77-bd3d-a13e7dce9c79 | -9.1876 | -49.112701 | 2026-09-24 00:38:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2475a3-36f9-34c6-bd9f-50252942f764 | -2.1188 | -49.528702 | 2026-09-24 00:38:00 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee91d3a-7f81-35ff-a933-1b4e3d1ec5be | -10.941 | -43.850201 | 2026-09-24 00:38:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae439f1c-477f-375d-a5b5-f137136ac66e | -3.7025 | -54.1856 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5339e3d1-a333-31c7-a0cf-5b71847d3511 | -18.880899 | -47.1763 | 2026-09-24 00:38:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a1a0c35-3c43-3a88-ae00-ee4bb86689bf | -4.1142 | -51.088402 | 2026-09-24 00:38:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6068f819-f201-3ca5-adc5-f6e04f034a00 | -9.0139 | -49.8088 | 2026-09-24 00:38:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c25ed38d-60ff-36d8-ae5d-de30eb480814 | -12.173 | -47.365299 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b893ff44-e7a6-3823-a442-f71c69f052e1 | -3.1455 | -54.582401 | 2026-09-24 00:38:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae27b44-97d9-3f8c-b740-c3feb6b246e4 | -5.5778 | -42.718201 | 2026-09-24 00:38:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 91b7b54a-5273-3a61-ad68-e7f77fab4665 | -7.6732 | -45.490002 | 2026-09-24 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bceeb9ca-bf55-3f88-84e4-d500b5de6e70 | -3.0372 | -50.431198 | 2026-09-24 00:38:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e04162-22af-32f2-9ed4-bb466570eb8a | -9.2721 | -48.618801 | 2026-09-24 00:38:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fecdf319-45c0-36e7-b69c-b02c085a36f0 | -12.3993 | -46.953602 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84a262f5-28bb-3ab4-8ae1-3702c5104b57 | -11.9427 | -50.759201 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee9c28c0-0ab7-3810-85f6-05cd595b0228 | -7.3998 | -44.769901 | 2026-09-24 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c222d018-922b-32bd-a944-f83bc62baca4 | -3.7147 | -54.194199 | 2026-09-24 00:38:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5c3ed3-652d-3a7d-92be-a1a1def87ae6 | -9.6782 | -46.693699 | 2026-09-24 00:38:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 919e09f6-2d37-36c0-b13f-28ea4e2a2d09 | -5.2278 | -49.235199 | 2026-09-24 00:38:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 280308ae-7659-3310-85b7-9a48ff1ab5b2 | -10.2792 | -49.950901 | 2026-09-24 00:38:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ecee3d8c-465a-3bc2-b59d-4b831a4f1bcb | -10.0929 | -46.033298 | 2026-09-24 00:38:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f89bb29e-27b1-3fd1-a9c5-9e77bfb3962f | -12.0817 | -50.7383 | 2026-09-24 00:38:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22510fab-e1c1-3eda-9551-dc78bd46bc54 | -9.2596 | -47.340599 | 2026-09-24 00:38:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2668007b-2720-3ab9-8964-f1a70019979c | -4.0172 | -52.069302 | 2026-09-24 00:38:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa55ef63-efc7-375a-88e3-c5dc5827a819 | -10.2038 | -44.1381 | 2026-09-24 00:38:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f87b0bdf-e68a-3c7a-a4ef-8226d47095a6 | -2.3838 | -48.528801 | 2026-09-24 00:38:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c4668d-100f-32da-a1e6-edf98e3c4044 | -12.1322 | -47.367298 | 2026-09-24 00:38:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 214c8696-377d-36ef-a434-0faea95a721c | -6.1303 | -44.596802 | 2026-09-24 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ea68535e-105f-3bc7-9b77-3e9d8213248d | -6.9183 | -47.656799 | 2026-09-24 00:38:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4aae68db-ed36-327e-98ed-693ade3be974 | -6.0032 | -44.1059 | 2026-09-24 00:38:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d307ae85-d4cd-3e29-aa29-3cf287c15ace | -12.4173 | -46.942101 | 2026-09-24 00:38:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8720f711-0072-3f06-b2ef-d1f45ef0c4a5 | -6.4371 | -59.924198 | 2026-09-24 00:38:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12a8283f-859e-3717-9348-72d8039ddbb6 | -11.78466 | -50.95777 | 2026-09-24 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bc37884e-0c24-3270-b77e-8904447affc4 | -3.48914 | -59.19813 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 06081d3b-1f64-3b96-8228-72dd56950150 | -10.90083 | -53.94355 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 419d71f7-ef4d-384f-834a-4f01555e4d59 | -5.86068 | -60.15825 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4b4411b0-06c4-3ae0-b37e-5909d96c277f | -3.96175 | -59.34591 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 1524d516-f9e4-36ff-b80c-5f651f6e56c0 | -3.45456 | -58.22698 | 2026-09-24 00:39:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 72524ad4-71a8-31c8-8fca-50dd04df6056 | -4.42794 | -55.07399 | 2026-09-24 00:39:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ce72582e-4646-3609-b29b-3e672b4125af | -4.10357 | -54.48601 | 2026-09-24 00:39:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 21d10c4e-0b29-35af-a7ad-8979d1d126d6 | -6.46539 | -59.99463 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 85970308-2ed2-3553-8db8-fd16931349c9 | -3.83314 | -59.3581 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 03ab0472-c0f8-327f-ba83-ebc8a02d69c4 | -11.59665 | -58.505 | 2026-09-24 00:39:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fdb04fd1-7c8f-3a4a-ada5-508222b65cef | -6.33834 | -59.95227 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad4bad8a-7ef5-3ac6-83f4-4ea9cf972358 | -7.64142 | -57.645 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c207fd90-63bd-3d6d-aa68-c75bfb7853b6 | -5.92125 | -59.92679 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3d8f741b-2377-3222-b94d-1f08066f8fae | -3.23549 | -54.32993 | 2026-09-24 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 4efcf0cf-b2f4-3fdf-85f3-279c9be9c74c | -8.15638 | -49.54927 | 2026-09-24 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| da788554-3728-331a-8068-5709edbf89e2 | -9.85211 | -48.51701 | 2026-09-24 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| fc157f83-5ffd-304a-a850-151d86946dfd | -7.91917 | -63.47589 | 2026-09-24 00:39:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 95bdd4c1-bdb6-305e-bd86-ecb242955077 | -12.10486 | -50.7556 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 6f549e20-a26f-3f23-972f-b547336524cd | -5.40782 | -60.21547 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c2b12bd7-a2bd-3405-838f-667308cfc434 | -7.44658 | -63.62445 | 2026-09-24 00:39:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| a4f363fd-deb8-3b02-b8bd-3c0d76b235e1 | -9.0222 | -60.51967 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e7447e2e-c2a9-337c-8c2b-d64cb33a22aa | -7.52082 | -61.47447 | 2026-09-24 00:39:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 276c7a9d-474e-30b9-b91b-261615fed178 | -7.58949 | -57.6684 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f5a4051-d9e0-3628-8ef1-5466a5a51ca5 | -4.51903 | -56.07906 | 2026-09-24 00:39:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 96c3651d-cd69-392d-accf-fbb622cc308d | -3.90168 | -60.59224 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| db3f5abc-63df-30bf-833e-9e36a09df3de | -8.21854 | -64.10038 | 2026-09-24 00:39:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 58c79117-2428-348b-90dc-6605e7c9189d | -6.34878 | -57.76335 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bcfbd3f5-63be-336b-b7bb-1dd35f776854 | -8.50277 | -57.60805 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7bb8b5be-dc3f-313f-a198-2b2f44d80992 | -6.62088 | -59.91542 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ee704705-c2b4-3fde-b13e-d6de76dbb4e5 | -8.12208 | -54.82585 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |


[Clique aqui para ver as próximas entradas](README17.md)
