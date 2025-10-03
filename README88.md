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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 681a3830-e160-3054-b7e5-8605c147d026 | -11.55696 | -46.99553 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70cd5371-9c5d-3e14-b83a-aff750ee9a2d | -7.12249 | -47.83054 | 2025-10-03 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7b8f7f7-dcfc-35e9-b35d-8f53642f2563 | -5.86224 | -45.73198 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bb19ea7-4134-3849-ae55-99b3c05f7819 | -11.10944 | -43.19291 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 60571b0e-f2ed-3c1f-a68b-4f0c28e99e8f | -9.93605 | -43.5816 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f0f20a0-78cb-321d-ab57-f9464dfcf8af | -6.20118 | -45.91932 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c687d84c-1910-3999-965a-8687aec94a30 | -4.65642 | -45.80105 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2e7c752-0a76-3cac-b427-04299b87d5a4 | -6.23682 | -45.34858 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67395368-3b91-34eb-8c3d-a5ddb1f354f8 | -5.79449 | -45.8536 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b93a14b6-c7c1-352b-987f-c3bf959e3226 | -11.89879 | -46.27255 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ab35cec-6c2f-32cf-b03a-12b63fbbd162 | -7.79395 | -47.38125 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d791b0e-9f0a-325a-ad44-6d0e5d89f99b | -10.88448 | -44.27847 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bd27104-ef49-39dc-9452-93296b78d474 | -11.61887 | -45.03238 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75a47c9e-2149-343f-9c82-1e67045e5ef2 | -11.6114 | -45.03097 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0b89723-762c-3b10-9af2-bb41c9b90acc | -6.04928 | -44.60986 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 264164c2-0980-340a-a0ed-d06230402f42 | -8.58951 | -44.78346 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bfc1d3c5-b666-3b30-943e-81daa0cfd933 | -8.24803 | -50.09228 | 2025-10-03 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6927c15e-50ea-3f91-8c27-7fba15e1c7fa | -9.06521 | -46.64817 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ddf3e89d-be62-3c6c-8ba1-c1cca298045a | -11.57732 | -47.67019 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ec1ba94-5e8a-354f-9362-03e6023c52bc | -5.34753 | -43.75996 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 815842e9-872d-3906-8807-b267e9a845d9 | -6.942 | -38.56864 | 2025-10-03 04:32:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14da2704-36d1-3df1-8755-86e504440434 | -4.31502 | -48.09637 | 2025-10-03 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b383e0cd-fb2f-37ee-ad1f-ee368e97623e | -10.10633 | -50.35752 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 823ce1fb-f751-30f2-9f00-ecd64eac0840 | -9.05503 | -46.64654 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfd2d1f3-fa52-3caf-badf-3833b06d4244 | -7.87857 | -47.34069 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f6dbcce-ac1e-3a1b-a966-4cfce7fcd9dc | -9.65427 | -48.20889 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff8e9213-8014-31f6-92d4-ad6b6a223285 | -5.62667 | -43.91394 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4678d899-e52a-33f3-bf37-149942b44da3 | -6.51965 | -45.73926 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3314006e-f970-3cd0-a047-edcf01c3cdb3 | -10.00756 | -50.23101 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cbb18aa1-4554-36ec-976b-521b498b3e28 | -8.71789 | -47.13545 | 2025-10-03 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ce85da9-1509-38cd-a5f9-82182f1e5505 | -6.61337 | -44.26139 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0307d1f-8b94-3fb5-9233-9c8f80fc2d53 | -5.60449 | -45.44909 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6868ae14-78e6-36f0-9320-24fea6779e40 | -5.49295 | -52.13764 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7dd5117c-5362-34a9-bc2a-1e4b8a90d154 | -11.45674 | -45.13365 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b18f4ab-098a-3c23-a208-ba165d8077a2 | -11.92245 | -46.28341 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b25fab8-6396-3173-bc4f-cdb80b0c46be | -12.29533 | -45.37035 | 2025-10-03 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 697e0f75-eb70-32ba-acea-0385cfa748e1 | -10.6504 | -48.48281 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ebf9ecb-5cb4-34d7-b084-3d0b8dd49e27 | -8.16908 | -47.00313 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c94cb3fe-aad4-3718-b7e6-9a7e0883fe78 | -7.29217 | -44.18379 | 2025-10-03 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecef0a75-abf3-3181-b2e8-af56f768b549 | -8.54315 | -50.15469 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 823962b5-58d8-3d44-9f80-704b674fb9b6 | -8.25233 | -50.57633 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a7f0511-81e1-324e-b685-a211e3b98fa4 | -5.63238 | -43.90107 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f2b42f6-5d5d-395b-afe0-f72bf0bcdba6 | -9.08334 | -46.76331 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 959ad3f7-16b2-327e-b3c0-4405183ce06c | -6.23768 | -44.22406 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 447a4da6-231f-34ab-8cca-b4fbd10dbe4e | -11.59295 | -47.65789 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3bba5a4-432e-3643-b369-118c2f2fc24c | -11.28327 | -47.73182 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb97899c-a953-378c-95ff-6be01dcc1a00 | -10.28449 | -50.29931 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0744a4c-786d-3f30-81db-609d0d8dc806 | -7.9099 | -43.53509 | 2025-10-03 04:32:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec1addba-8ac5-3bd8-8684-e6ab0e2e902c | -6.34938 | -44.30088 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdbf0c72-73e3-3c8a-a396-e6f40cd1304e | -9.98149 | -48.78321 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b54a777-6715-3fe8-86d1-2430d8301b92 | -6.30004 | -43.90842 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8c82d9e-6593-3721-a6f9-1750f3b9fe3c | -7.31814 | -42.87293 | 2025-10-03 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc90e0a0-b0e6-3190-beda-e325318a284c | -11.83023 | -45.0114 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fe7c84e-e4cb-3935-b13a-bea4f268a899 | -7.83484 | -42.86022 | 2025-10-03 04:32:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ee599b6-c916-32ee-810e-dc965e002b69 | -11.0513 | -47.80535 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee3115cd-bf45-3d66-bf6f-1c3ca48af292 | -8.27359 | -43.84071 | 2025-10-03 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23a97897-de66-3186-8756-a66671f5ea72 | -7.75171 | -46.24286 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8460a880-dd7b-3a08-a96a-df585095f477 | -5.13734 | -45.43751 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96d81b8b-c7ed-31aa-aed7-891e3fcc6921 | -8.24789 | -47.04103 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75da54e8-e10e-30a8-813f-0dcfb26817f3 | -7.15978 | -44.99174 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99f9ab95-6176-3808-9f9a-ecaa2669bcad | -6.38033 | -44.64444 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8e1b021-4676-37c3-9a68-5a88b9573f4c | -9.33191 | -45.68254 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f2ecd49-353f-3efd-b929-3c4e3138c3b1 | -7.7614 | -46.27085 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 6f22707a-be1d-387f-9e3f-93b6de07741b | -7.75117 | -42.55737 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 076296c9-f5bf-3e3f-b080-62a41a3cf4ff | -8.12598 | -50.23863 | 2025-10-03 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83660b42-7829-3ede-beb6-56cfdd53b3d4 | -9.42262 | -47.53914 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00eb2ca7-6e64-3497-8e55-b9f8ffb69f33 | -11.77922 | -46.82432 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23166b0b-9dd5-323a-9a18-2fd02de35fc2 | -6.70952 | -42.79911 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 303e5a20-fc57-343f-93fb-c64efc7fb17e | -10.96644 | -51.0841 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79cee194-b31b-3daa-b799-d3402d28a4e1 | -9.34122 | -45.71639 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3bffc08-0c16-38e0-9832-ca07752472a8 | -10.88688 | -46.73077 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 543641f1-3578-3a5a-91a5-1dcdda09934e | -6.04734 | -44.6473 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27d20500-e939-3f06-8d81-25f8bd2103c9 | -11.80377 | -45.00597 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 616d721a-6024-39f3-8454-726a1f529a19 | -11.10123 | -47.83148 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee741e4c-6fc4-354b-b6f7-6a4db3810706 | -5.38397 | -48.95404 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47ec9495-3546-3461-9eba-6d08bd7df832 | -9.06068 | -46.655 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 173e9963-248e-3691-ae60-46687a2265c7 | -7.75051 | -42.57645 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 53d9782a-8cc6-35c8-9e0c-c267ef0e106c | -6.53139 | -43.37324 | 2025-10-03 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e0ab1d3-68b4-3074-bdcb-fa3d85623b5f | -9.90407 | -45.96297 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fa8c205-8607-3558-986a-4477bda1bf9f | -6.06454 | -44.33139 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a92f9c7c-f43a-3f32-b4cd-f58afdf6f37b | -8.52018 | -50.03656 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97959454-026d-3c39-8c3b-cab6bba2747f | -10.34189 | -54.1941 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 967da7cf-1a16-3421-927b-1044ac6dd256 | -10.90234 | -46.72157 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81b6d3e2-9c97-3d5f-9889-ed7172a46c13 | -5.78137 | -45.75752 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d91ca05b-66f8-31eb-831d-2d71d5d92a3e | -8.75535 | -49.92708 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e012ea-780e-3262-a511-63b2f0a660fd | -11.23044 | -48.20428 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63b0d610-8b6a-3758-b6d0-9997406924b3 | -6.29451 | -44.41839 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8792510c-dcde-3278-8bf5-dcf3d4d535ca | -11.07686 | -47.70657 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0513da69-76c6-3a8f-970e-1e8a35e56ce6 | -9.94653 | -43.7542 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bd497156-7326-3de4-abc5-ea5f017b8fef | -10.96453 | -51.09572 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 898e0d67-2059-365d-8a30-c3e9c7a43d09 | -10.96581 | -44.32786 | 2025-10-03 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6ca7c25-9926-35cf-84ef-ce37250ec3a9 | -7.77955 | -42.5807 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ad9bacb0-4ebb-34b0-8121-d15a215001cf | -7.3092 | -45.26746 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7039d920-3258-362d-ab1c-dbbb35a06bb7 | -5.49495 | -42.77611 | 2025-10-03 04:32:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| feedd543-d4ff-3414-9f09-f2b4fc18d573 | -4.80643 | -46.81377 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e6ed410-635a-3af2-87b9-3ecad15b7719 | -6.65822 | -42.78419 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f539c2e1-329b-31a3-8d9e-c245f2b3f142 | -11.21818 | -49.95185 | 2025-10-03 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb64a587-910c-385d-8e50-909d717f1f67 | -6.865 | -39.28296 | 2025-10-03 04:32:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2685a58e-5d58-3790-b25a-cb3ada56e5ad | -7.75647 | -42.55027 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7ad6cf3c-8221-3a45-9cc2-de0bf62a8b2f | -11.13986 | -43.40333 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |


[Clique aqui para ver as próximas entradas](README89.md)
