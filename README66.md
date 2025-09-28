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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab62ec90-aedd-3ea5-af21-b39a02f712bd | -11.41521 | -44.91151 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 543f3b66-8ff3-36e8-b062-dbad65ad0028 | -7.03345 | -44.77446 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e747843b-9619-3950-8208-7f80a3a3d772 | -9.96831 | -46.61161 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e670829-2751-33f8-a71c-90f39f279584 | -6.80644 | -46.39681 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddebcb84-cfe6-30ee-8524-b70af1c35f8a | -7.13329 | -45.5052 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e87542d-8467-33b7-bb53-e5a93fcf7aea | -12.00391 | -47.97925 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d32c91c-9910-37cf-8c63-14087ebfc20e | -11.9579 | -47.90668 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3596ea22-3a5b-35e0-96ef-139bcf8f4164 | -12.91606 | -45.18929 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5f40915-5a6d-32a9-96ff-f5a8168ce2a8 | -11.43212 | -46.64949 | 2025-09-28 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd83f845-d090-357b-9ddc-51cd6944add9 | -10.41765 | -48.14887 | 2025-09-28 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e001ff1a-9b36-3fdc-9034-bc3a417a21a3 | -6.57098 | -45.10031 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8228e7ea-6f7a-31af-b299-1e4df7efff53 | -6.47765 | -44.24665 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adb55462-f12c-3c1d-af6b-0a9892474d9c | -10.54008 | -43.62951 | 2025-09-28 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf485162-8605-33c1-b102-8f57b2ec0057 | -6.4041 | -43.95442 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a484f4a-8d8d-3cb9-8d1f-12b5d16c88a8 | -5.77414 | -43.70204 | 2025-09-28 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8bfbb86c-9b59-340e-81fe-72ed4ec55cf2 | -6.61193 | -44.94623 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5c17c07-4a41-36c0-8a6c-0ec3ae2f465e | -5.98146 | -44.12713 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3cc79420-c159-33f6-ae16-69ec63a3d392 | -10.90858 | -45.73757 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e882ebec-53ab-35db-b399-5801fb4b04fa | -6.60665 | -45.09128 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8477954f-f281-305c-be17-dd23aeab9abe | -11.96763 | -47.99518 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3ae08f-00c3-3f4f-95a0-3e477e79814d | -6.4367 | -43.51038 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a92dee8-9d5a-3056-b0e9-59010b781fdf | -5.79501 | -45.72325 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aae09e0-0977-3b49-bf52-6c01ee766102 | -11.97855 | -46.5868 | 2025-09-28 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c73810d-aad9-3349-85d8-7ed8ae068d83 | -6.07168 | -44.47214 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddcf7bad-979c-3e81-a472-116cb18c5c98 | -7.85829 | -45.29097 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39c91f3f-b49f-3045-a3e3-a60ce57ed3d9 | -9.54218 | -50.78112 | 2025-09-28 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b1f5f2c-38a5-34d5-b045-ca8dc6da8724 | -6.98566 | -42.3904 | 2025-09-28 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05cb9b4a-5d1c-327e-8756-498d105f23b2 | -5.50692 | -44.91381 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a59c7b-e790-37a2-86f5-1850fd66c2d0 | -12.69049 | -46.87513 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4245b504-b331-3c02-8073-bbebfb38b17a | -7.82039 | -45.14581 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94e5f757-489b-32a5-84f7-21f92d94291f | -12.94997 | -45.15393 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 65e8d9de-558f-33cf-b3e0-42a21c6c6c17 | -10.94186 | -44.30378 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da4cb3b9-140a-389f-8150-f2f3f07ebcdf | -7.14716 | -45.50378 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b529751-3323-3907-9607-4a25a6f59558 | -12.92659 | -45.16661 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 538a9d33-9f94-3225-bb39-79028eb2bdbd | -11.39057 | -46.98235 | 2025-09-28 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0e392bd-5727-3f89-9bf1-2d0549e0662d | -5.45054 | -46.61444 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a95f3b3c-16fa-3a5e-9271-e197821af0bb | -6.21665 | -44.78232 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54e9a898-3b69-32af-99a3-4469981739b4 | -12.02012 | -47.92035 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3fc8b4d0-122d-3716-9b13-daa65bf9fa67 | -6.48681 | -44.25558 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38e0e571-709a-30ea-91fd-51c462d5952a | -10.51659 | -51.9465 | 2025-09-28 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde61c5e-bbf6-38fc-972a-4c544922eb61 | -7.7538 | -45.74918 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3df809d8-9d37-32e6-8a4b-0572d5a8ad1f | -5.92128 | -45.84971 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b7b4cb3-b773-3de1-b309-e9c77a9cd779 | -12.90152 | -45.16682 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7450db5d-920d-3e31-8f4c-27661380382c | -8.20425 | -44.39843 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caac61ca-2aec-3425-8730-69ed331fa485 | -11.78917 | -44.8727 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32002cae-963f-3c69-a32c-dd2f236a5094 | -12.90093 | -45.17078 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2981ddb9-e370-3e5e-a6ba-8a8422da4753 | -5.97548 | -43.30971 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d1f4cec1-8af2-3bb9-a7f7-ae45aa6a9ef6 | -11.36252 | -45.0507 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b0c6356a-f53e-3079-8c9d-98cfbaa6b80a | -11.65152 | -48.27065 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3038a303-8aac-37e3-86a8-39642a1b0117 | -6.69183 | -42.74307 | 2025-09-28 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 06ad9c95-ab2d-3134-92e7-847e3ad0f928 | -7.81222 | -47.01614 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7133a8a3-621c-3956-ba8c-1e64feb10263 | -6.49081 | -43.65532 | 2025-09-28 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9e6dc9f-0b1e-36e2-a7fa-8aeb2075211b | -7.24505 | -44.7658 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c9aeef7-f7ef-31a8-bf78-f06d3d98b611 | -12.01244 | -47.90455 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aadb289-979c-39de-b813-4598b3996029 | -6.57767 | -45.10134 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83cde49a-955d-35a7-be50-7a5cc209a474 | -7.78088 | -47.0219 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00798261-e7e9-3870-b38a-51d74fa191d7 | -5.48692 | -45.10877 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c28c79df-9c24-3776-a1b5-4714a0d5e36c | -6.27497 | -43.62465 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b582d91-d3ac-3a40-8ee1-084683ce2137 | -12.90502 | -45.16736 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 251b1a8b-5a64-3178-91cf-6c43354083a6 | -7.27894 | -45.81074 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b378cc54-d85b-3c34-b344-9b9bdc9ac3fd | -9.87671 | -45.93604 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4a57ff9-582c-3418-8a24-64049ad15ec5 | -8.42619 | -46.8507 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8200066b-c4f7-3f9c-8bdf-5b4d602193cb | -7.86793 | -44.56441 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50244757-4182-3e2e-9966-1017643a034f | -12.94131 | -45.11596 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9f84b7f5-5fbc-3197-91fa-31c32172b6d3 | -8.83057 | -46.00409 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 335ef3e0-094a-3735-8f14-6bd1bf3e1622 | -7.30625 | -42.95391 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0fccd6c6-595e-38a8-bdf0-1684ef03b77c | -7.62907 | -43.79934 | 2025-09-28 04:25:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c6eae2a9-6f02-31c1-8091-21164c8b8edb | -7.76043 | -47.00074 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f931dacd-6ac1-39d0-b555-4135741d96c9 | -5.90933 | -42.94407 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d2ed93c4-d1e8-350a-8519-352073a5571d | -11.4833 | -51.44905 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dd56d30-c7fd-3fa6-8fe5-104b2085f5d6 | -8.65916 | -43.99051 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ad445d4-7c7a-3846-90a0-516e952f98ba | -6.06739 | -42.44984 | 2025-09-28 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0dd34f8b-cc23-3530-9d69-1dc1cfd76e6e | -8.28891 | -45.44852 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0431440-4bb8-3973-a0e2-da2921e93912 | -7.75767 | -45.74619 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf459418-4c20-39a2-a8a4-e28bfb86004d | -11.99441 | -47.07196 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a3948f7-22fa-35f7-affb-cc83d9698aff | -7.92569 | -42.67365 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 685a99c7-731b-39c7-be5f-59d61f067995 | -5.35834 | -45.97292 | 2025-09-28 04:25:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5111a5f-53f5-3ccc-aa73-d4554a652cb3 | -6.70935 | -44.58396 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1d56a46-1ca3-3bf1-897c-787f51a8fe07 | -6.06487 | -44.86204 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11e00289-2c47-3867-ba75-f06ffbffc395 | -7.13717 | -45.50221 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9a35777-0c73-344d-94c3-602a17568201 | -11.71797 | -44.42827 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61cad912-34cd-3879-bbf6-0e5726d1dc0a | -11.39107 | -46.93558 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee5b9cf1-e42a-34dc-83f2-418e55007d75 | -5.98545 | -44.12399 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 68749a0b-715f-357f-841f-db422ee29495 | -11.59783 | -44.33529 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c472666-2a3d-385c-baeb-b6e4938bf2be | -6.05828 | -44.75839 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99aee6ed-58e4-368e-b9ed-7071028fc031 | -7.70568 | -47.6815 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e9847a-b158-32d4-8153-84d57cff4163 | -9.30927 | -45.67217 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3182ed00-73be-3ce2-87ad-686361d3e2e4 | -7.74662 | -46.9807 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0373381-b038-30b1-9030-58a2d563c796 | -8.46465 | -44.59993 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d63738de-7c14-3f89-8cc7-cfe5bd67ae83 | -7.78199 | -47.01492 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16f2c2fc-9d2a-3305-934e-c35e662f311e | -7.76042 | -45.72865 | 2025-09-28 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1248139-18a6-3734-a785-dffd5bca20da | -12.95056 | -45.14995 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 61f0c6dc-34e9-354b-97f2-871d6c51aad1 | -11.98668 | -47.05626 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 388aa83e-5b2a-356a-9b7d-63f829fc9d46 | -11.36765 | -44.9681 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11613542-adae-3020-9b42-6c3a47719d56 | -6.08661 | -49.397 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e6e2f4b-6576-3168-ae22-e53197c17c3a | -8.24939 | -46.67988 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d242ce9f-39a6-310b-83a2-f30d5a658e2a | -6.98709 | -44.69301 | 2025-09-28 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5d37c1b-3a69-3006-b33b-0f2f1ceb61c9 | -5.96886 | -46.45124 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eef2f10f-63d4-3b10-96c3-2e4f1cd3da67 | -7.74717 | -46.97721 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95467adb-b1d7-3bf9-b31b-3140ace97b44 | -5.55667 | -46.28679 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README67.md)
