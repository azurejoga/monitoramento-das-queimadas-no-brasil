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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87edd9ca-ffeb-3825-ab2c-752bff517f90 | -10.5746 | -37.03445 | 2024-11-06 00:15:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 1951a43d-6b98-30b1-b58e-eacc13e8049e | -12.87226 | -41.76451 | 2024-11-06 00:15:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ce33da05-5930-3aa8-b14a-5c86689224c3 | -10.24281 | -36.32436 | 2024-11-06 00:15:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| dbbc331f-3267-3012-bfa9-c011a1b6b1b2 | -9.38038 | -35.66851 | 2024-11-06 00:15:00 | TERRA_M-M | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 7182ee1b-45ab-39b8-bf3a-aa3856114168 | -9.38194 | -35.67896 | 2024-11-06 00:15:00 | TERRA_M-M | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 0b56380d-de8b-3472-a230-8b96da9059ba | -9.88918 | -42.08538 | 2024-11-06 00:15:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 1ba70ca9-3015-340d-991b-7e76cf823396 | -11.18201 | -41.99079 | 2024-11-06 00:15:00 | TERRA_M-M | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0a77f3d6-a0a9-3db9-a241-dd39c0d815bb | -10.6039 | -36.97747 | 2024-11-06 00:15:00 | TERRA_M-M | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| ded8543f-80b3-3fff-bb1f-5652b250f5cc | -8.54491 | -35.08443 | 2024-11-06 00:15:00 | TERRA_M-M | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 772d0e45-d483-35cc-a225-372105344848 | -5.65553 | -45.93839 | 2024-11-06 00:17:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 8d9b51d3-ad7c-3129-814d-84c1c2ae7cbd | -6.13392 | -43.98896 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 32526cfd-1a00-3dd6-8762-072336391bb1 | -3.71219 | -41.68616 | 2024-11-06 00:17:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 137.2 |
| b08ba555-33b6-3a47-b9a4-4edaa958cb63 | -5.54645 | -35.57988 | 2024-11-06 00:17:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 2fd25b1a-94fc-34b2-b428-ceee436261ed | -3.80213 | -44.03724 | 2024-11-06 00:17:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f0746c57-df93-32fd-8a68-fee78f574d75 | -5.06686 | -44.2368 | 2024-11-06 00:17:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 79b1d4f6-60d2-3c0b-8079-3b4cfdc0fd6b | -5.62258 | -44.19075 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b696b268-438e-38c8-9ae0-2dfcf69887e1 | -6.05543 | -39.43505 | 2024-11-06 00:17:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8820449d-991c-3a65-99b3-12f820d3fa7c | -5.63429 | -44.18936 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c9d656bf-ff47-39cf-9d65-e95167b28dfb | -3.80038 | -44.02825 | 2024-11-06 00:17:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a05a6f2e-a88d-378d-b595-bb212ef9f176 | -5.98604 | -45.36934 | 2024-11-06 00:17:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 55f98bb0-d7db-3f8e-87bc-c23dcb4cd79a | -6.92363 | -38.13224 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e1816bc7-1e32-3f8f-b7f6-b6f86285b6ee | -5.55655 | -35.57839 | 2024-11-06 00:17:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 57.3 |
| e1852b37-53ae-3f20-a802-050654035898 | -2.39643 | -46.1797 | 2024-11-06 00:17:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 31af75be-fd2f-38b5-a2f6-cccd8e27fc1e | -5.5592 | -43.71389 | 2024-11-06 00:17:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 008f6022-f32b-361f-9c2a-afcfda26569a | -4.69085 | -45.64951 | 2024-11-06 00:17:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| b6a0b883-a32f-33d4-b84f-1418de5870b8 | -8.50328 | -42.08736 | 2024-11-06 00:17:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e36f37bc-31a0-3150-b1be-036b945f010e | -6.14135 | -43.95578 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 675337b6-5d85-34db-bfcf-97512bae3e0d | -3.54296 | -40.72271 | 2024-11-06 00:17:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 529fc30a-2d27-3638-a431-4e0e55ca9133 | -6.48607 | -44.6813 | 2024-11-06 00:17:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 431fbd79-3117-3517-a02d-78f0c1744057 | -6.51078 | -44.67819 | 2024-11-06 00:17:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 66a71223-c496-3e7a-bb68-3279d35536b1 | -5.54601 | -43.70062 | 2024-11-06 00:17:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| de16f637-b4bd-3415-85ba-b1bfe8e6fc64 | -5.0301 | -43.60939 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 8c052136-85e3-367d-aa67-b798f4698d3c | -8.77251 | -38.3694 | 2024-11-06 00:17:00 | TERRA_M-M | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 66b835d8-3a7f-3d40-a7fd-d55f73c8a904 | -6.75905 | -39.25957 | 2024-11-06 00:17:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2d4035b5-005a-32b1-b803-878cb4f676c4 | -8.50492 | -42.10024 | 2024-11-06 00:17:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 86d869d8-67d9-3692-9aa3-864a6bd5e8dc | -6.69864 | -43.06286 | 2024-11-06 00:17:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5e33177e-a126-3631-9418-b0333e9c0241 | -7.07075 | -39.99101 | 2024-11-06 00:17:00 | TERRA_M-M | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7a27ed52-cff0-3e35-836f-966b5ae2bab4 | -5.55725 | -43.69921 | 2024-11-06 00:17:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| c4bd48b5-16e7-38c5-99dc-4cbc75e39c8f | -5.58138 | -35.82181 | 2024-11-06 00:17:00 | TERRA_M-M | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 8d209edc-9049-309c-bbc1-1db74fec2944 | -7.43418 | -42.88136 | 2024-11-06 00:17:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6d1ab17d-bec9-38f1-8fa5-e7caf6babd7c | -3.97128 | -48.15858 | 2024-11-06 00:17:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| e89732b4-ffd6-3294-a29e-8d54ed4ddc89 | -5.64638 | -40.14635 | 2024-11-06 00:17:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b52b5afd-70ce-3b40-b5ef-f246f51aa4b3 | -6.48843 | -44.69976 | 2024-11-06 00:17:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8b46c744-38e9-317d-9c7f-7b646b4244f3 | -3.5417 | -40.71346 | 2024-11-06 00:17:00 | TERRA_M-M | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 904f7a6e-19a7-3c5f-88db-405291b1226f | -5.32133 | -43.06548 | 2024-11-06 00:17:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 42d4bcc0-ed21-3ef9-a796-1baa7704a57d | -4.14196 | -43.57757 | 2024-11-06 00:17:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 715b4eee-b286-39a1-9801-cc36ffaf9bf3 | -4.33205 | -39.37044 | 2024-11-06 00:17:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a72d6825-3210-391a-b241-342b6dc1c478 | -6.49843 | -44.67982 | 2024-11-06 00:17:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 150.7 |
| b79fb84c-ebf6-3bf5-89ca-c4b82284aa3b | -8.7907 | -40.75436 | 2024-11-06 00:17:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| bd70f902-4ad3-352c-bdf2-098f8b4bd6c1 | -3.60709 | -42.86147 | 2024-11-06 00:17:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 1219853d-4a03-3272-b5f3-2f6c317a4372 | -4.13293 | -43.59284 | 2024-11-06 00:17:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 78414ff4-d9e7-36e2-a7fd-984edb64404a | -5.5913 | -35.8203 | 2024-11-06 00:17:00 | TERRA_M-M | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 724a61da-5fe1-3784-b861-87529dee223b | -5.88872 | -39.23533 | 2024-11-06 00:17:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 154e2d4c-7858-3b0f-8d3c-5617ffb646d9 | -4.33965 | -39.36037 | 2024-11-06 00:17:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 71871bff-0fc9-3cd0-9943-1641a764620c | -7.50262 | -40.53012 | 2024-11-06 00:17:00 | TERRA_M-M | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 494f3bdf-eb4b-3a9e-8675-5fccb1455448 | -5.97891 | -46.32482 | 2024-11-06 00:17:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fcea8496-485a-36d6-af73-bc256ab2962c | -3.80241 | -44.04291 | 2024-11-06 00:17:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93da6cf7-1324-36fd-99c6-d42af9e528e7 | -6.67099 | -37.45107 | 2024-11-06 00:17:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 09f3d7bc-9f8d-3be5-9378-58fcd6d012e0 | -8.77127 | -38.3605 | 2024-11-06 00:17:00 | TERRA_M-M | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5864cffd-4a0f-34f0-a881-4c10dbaa0f91 | -8.47283 | -35.29432 | 2024-11-06 00:17:00 | TERRA_M-M | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 1b064021-c725-3f26-a233-63d058e26b50 | -7.33471 | -35.06786 | 2024-11-06 00:17:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| ed304eda-9d79-36ae-84c4-d3c3ed4df954 | -3.68541 | -40.15241 | 2024-11-06 00:17:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b32b26fe-0dcd-3e4f-a60c-7a3da7642e03 | -7.43593 | -42.89497 | 2024-11-06 00:17:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| fa57bdee-06d8-3270-82a7-373ce42f06d0 | -4.68959 | -40.68867 | 2024-11-06 00:17:00 | TERRA_M-M | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| bf11670c-4d7f-38ee-9fec-e970476a2ff3 | -5.32902 | -43.08527 | 2024-11-06 00:17:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 51c3bf5e-c6d1-39b4-a01d-61af4677e736 | -7.78961 | -40.264 | 2024-11-06 00:17:00 | TERRA_M-M | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2293b046-c93b-3084-9d85-153ffb6e9d02 | -5.94571 | -43.77461 | 2024-11-06 00:17:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2c02ba6e-d05b-35da-a690-05498d02d929 | -7.67821 | -42.6397 | 2024-11-06 00:17:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6599de16-d2d0-3bc0-9dc9-d0a5b301ec73 | -5.47817 | -44.86377 | 2024-11-06 00:17:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| efa515fe-940a-3d4b-b36f-2731d9143d1b | -4.65605 | -43.82175 | 2024-11-06 00:17:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 38524e3d-f2ff-39d4-a6af-f8eaed2ce509 | -6.50086 | -44.6986 | 2024-11-06 00:17:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 13292a0b-5476-3c33-a080-6b0fddc89117 | -6.12231 | -43.9904 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 082f6bf8-31c0-39b8-b8bc-cc71ec12faf1 | -3.86133 | -41.03178 | 2024-11-06 00:17:00 | TERRA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a1133eea-2d06-3d18-858f-58b85bc20f8e | -6.10869 | -43.97627 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 22392d2d-46ae-3eed-bc35-7ceca003b368 | -7.49971 | -43.83306 | 2024-11-06 00:17:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0dc74224-3585-337d-99a4-a2f64876c395 | -5.90997 | -42.90387 | 2024-11-06 00:17:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 66ff4086-6c85-3570-aaf8-78ad6adabe8a | -6.75885 | -35.26444 | 2024-11-06 00:17:00 | TERRA_M-M | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d001d949-c03e-3ec7-acd4-6332f7619c3f | -6.12025 | -43.97453 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 12efddf7-0c51-309e-bcc4-c84715ad0399 | -5.15503 | -43.77756 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a8f276de-3fc4-32ec-b41e-243f1e7c6e57 | -3.54837 | -47.38105 | 2024-11-06 00:17:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 4ce75cca-26d5-3951-82c3-fcb1fa678095 | -4.33082 | -39.36163 | 2024-11-06 00:17:00 | TERRA_M-M | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 53a7db76-426a-3411-9c69-640d9fdec743 | -6.1391 | -42.55655 | 2024-11-06 00:17:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 0eada9c0-45f9-338f-9d94-0b8cc75f55c8 | -5.66903 | -45.93656 | 2024-11-06 00:17:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| f806a378-effa-37cd-b6cc-09da3192f8c2 | -6.09844 | -43.96788 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4b452955-3699-3b32-adf8-e7d5dd1c2bbc | -4.09607 | -44.25978 | 2024-11-06 00:17:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 924a07ca-88e9-3dd8-9466-0aaf16efc78b | -6.4889 | -39.97709 | 2024-11-06 00:17:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 13.4 |
| ad849753-e57a-3093-b30f-059ad8249414 | -4.12928 | -43.56535 | 2024-11-06 00:17:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 26a2db93-ccd5-3d37-999d-8b6072189f5b | -5.8961 | -39.61563 | 2024-11-06 00:17:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 95d6c00f-2671-3856-ae33-0137675a5a56 | -3.31904 | -40.03728 | 2024-11-06 00:17:00 | TERRA_M-M | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| b914da9e-13b7-3a8f-8ea8-782fc3dbe85c | -6.6112 | -43.69044 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 81dda11d-ff78-32c8-92d0-a5f0b2b8432f | -5.22289 | -44.91618 | 2024-11-06 00:17:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 054fb357-51dc-32ea-bd56-25e680e271a2 | -6.70265 | -37.47813 | 2024-11-06 00:17:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e37ab5fe-f52f-3a1e-81a7-b0d062748d59 | -3.53225 | -40.91015 | 2024-11-06 00:17:00 | TERRA_M-M | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6318c1e3-c2bd-3676-a3a1-6f2dcdddebe6 | -6.48832 | -47.47395 | 2024-11-06 00:17:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 268.0 |
| dfa8c391-65f0-3200-8e10-f42e01121094 | -6.50764 | -47.50258 | 2024-11-06 00:17:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 4731baba-1e20-3bd6-8ee3-d383cb94d97b | -6.49666 | -39.96663 | 2024-11-06 00:17:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e965da38-655d-34c2-bf5d-6ff1fb363f68 | -4.55608 | -48.0075 | 2024-11-06 00:17:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a3423e6f-674d-3216-9b8c-f99c481fabc7 | -5.02824 | -43.59502 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| dc2764ed-3626-3505-a18a-bf1ad88c6030 | -5.32731 | -43.07211 | 2024-11-06 00:17:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| aa78d584-c892-3b96-b412-4035faec0105 | -6.32467 | -39.51586 | 2024-11-06 00:17:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |


[Clique aqui para ver as próximas entradas](README4.md)
