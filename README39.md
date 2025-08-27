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
| 72b4dcd3-ad2c-3373-ac5e-4a90a540ef9f | -9.58448 | -55.37642 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b75e36a-2419-36cc-9ee7-f0fe8fda99ad | -4.69798 | -56.07115 | 2025-08-27 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5e32e3e-de0a-3971-9253-4cb5b7f85795 | -6.16521 | -42.61639 | 2025-08-27 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4ce73b2b-c17a-3a5e-8cc5-0f6fd021a370 | -5.481 | -41.41577 | 2025-08-27 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6888cf8d-95c3-314d-b4d1-ca5137699269 | -7.29538 | -44.52093 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce0096d3-47a1-300f-bf73-75a19a4e1564 | -7.73314 | -50.29669 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b6bdf99-4874-3ded-ad9c-9fc1f5bc8452 | -10.31354 | -46.75773 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 795f691e-40fa-31da-b2c0-c798fdf5b6fd | -5.94747 | -42.49622 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 325231eb-cf1c-35d4-9104-18842bc585fb | -10.70808 | -47.10038 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86d77a0a-1784-36b8-b31d-431fc37090e9 | -10.7694 | -46.38095 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddfd4af7-b511-31a3-a5c0-7993a47acca0 | -10.493 | -51.61146 | 2025-08-27 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 915f6209-db45-3290-a3d0-706d2f42201b | -7.40161 | -44.05585 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10f7de7c-de21-3976-a4e7-0c7ff66c9e02 | -11.25728 | -44.97251 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e87e8fee-d35d-3805-9a5a-d505f027c591 | -11.2389 | -45.46992 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9404a4ea-27a4-3028-b78d-0375b25d0b8e | -5.75943 | -53.77303 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4310ce72-7f7f-3553-b5f3-ee1f9dd5a1c1 | -5.12319 | -43.20682 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0fd7945-d228-31ac-a066-35067f6913d8 | -9.16343 | -60.77366 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1732468-a42b-3b5c-a2b3-de326643d990 | -9.58838 | -55.38319 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9165438-b4bc-36c8-811d-5048b9fe1e58 | -9.16773 | -59.45958 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc13c810-66dd-383d-9e18-185d9fe6a5f9 | -7.64123 | -44.96261 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07740c6d-578e-36eb-9d2c-b0700d1afee8 | -4.96598 | -55.82757 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15d014b0-5492-3113-aa27-e0f6bceeb077 | -9.26158 | -50.23142 | 2025-08-27 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7253db9a-bc3e-3543-8b92-4b1354d34817 | -6.78266 | -44.3027 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41fd4361-a879-382b-b565-04b6a9f23e03 | -7.53153 | -50.53342 | 2025-08-27 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b18b9fa-bb8f-3afa-b9b2-4b66378b0c77 | -8.12824 | -55.36889 | 2025-08-27 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bede4938-8077-3d0e-88fe-1d85425f8e08 | -11.24914 | -44.9792 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7de8d6c-bc94-34c5-9560-b119693142ad | -10.78198 | -47.062 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0792fd1c-088e-3d4c-afc9-15a4ff55ba09 | -5.75606 | -53.76552 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4237808f-75c8-36cc-aa2e-cafafd3699e7 | -7.64837 | -42.67317 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99f9c13b-4547-3910-b292-c32fa82d4e38 | -8.89931 | -60.77007 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c62fd42-8938-3147-a99a-ecc72c0e8a6e | -5.47407 | -42.59591 | 2025-08-27 04:25:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d32c40b0-ebeb-325b-8a40-be9b62dcddfe | -10.85621 | -47.32472 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40890e19-408d-330e-ac38-5be81236ab69 | -4.55673 | -55.9618 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 312c3474-4a6a-3ced-9943-3e0a3f4356b2 | -7.88591 | -45.86779 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7a6a483-4251-3f09-8665-6aacdf2353ab | -7.26515 | -44.55816 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a98a88b3-96e6-3a40-866a-e25491dc92f9 | -9.18611 | -60.80652 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 60c7ddf2-37bc-31b6-a4a5-cd1f3262eae1 | -9.56865 | -45.74302 | 2025-08-27 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee5797a-a04c-3f27-9f06-2b2361b4d00a | -9.2735 | -56.90836 | 2025-08-27 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6d78017f-89eb-3ae8-b4d8-edfaf2d03643 | -4.95616 | -55.81794 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc4cf8fc-904f-36b3-951e-cc29038cdd07 | -6.29824 | -42.80333 | 2025-08-27 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37b03b95-2b99-30f0-af10-fd59f2ff891e | -6.32039 | -43.60662 | 2025-08-27 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3347a41c-744c-370c-8d4e-455eee0a099e | -10.77922 | -47.05797 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 653fb70a-62ff-37e4-bb51-efc98991da65 | -4.31377 | -48.10073 | 2025-08-27 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c8101108-351a-3b07-8041-45a2e0ab5ce0 | -10.08113 | -47.26464 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c2424e4-e089-3f00-8b15-4015fca3d458 | -7.16988 | -43.84509 | 2025-08-27 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef9a4477-1b51-3db4-bba3-2eecc61d423b | -6.24739 | -60.02822 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2812adba-c060-37ea-90e8-355f6bb8cae7 | -8.4536 | -43.67381 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 430e5fdb-660a-325d-865d-b8991951a68b | -7.58612 | -46.22163 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dd5d92a-e669-38b6-bf13-0210faf9e31b | -9.09794 | -49.5751 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 178bdc3e-03ac-3ccb-ace7-8659b8d424e3 | -6.90192 | -43.13481 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e568d7d5-3950-35b9-9605-585b263538ab | -6.59381 | -43.14522 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cde1a42-3776-3208-86da-9a68fc80ec91 | -9.26305 | -40.41975 | 2025-08-27 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c24804a3-64f9-3e4d-a429-dacf866fd5f3 | -10.77608 | -46.38196 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8dde05e-fe83-3848-afa0-c0b33ce793ac | -7.12493 | -43.68864 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b5739ec5-7b22-398d-bfaf-68672610c0a0 | -9.22578 | -60.92261 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7be67243-179b-3f10-bdc6-5fce6db8d1f4 | -7.74781 | -50.27679 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d44474da-d680-3bc5-b004-fb9c71c21e18 | -4.31031 | -48.10017 | 2025-08-27 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 2b74f7bc-3fd1-34eb-9d0a-b7958a4b7105 | -4.20829 | -47.34954 | 2025-08-27 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 335f17f2-e481-3cd1-ad51-38ded50f2ccf | -11.64833 | -44.86686 | 2025-08-27 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92075e24-3928-3762-abc9-a4668c276fd4 | -7.70466 | -45.76797 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a58a58dd-e48e-3187-9f0e-39353f3d2c53 | -11.24381 | -45.48166 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2ec94b47-a9c7-3375-8127-1ae524697850 | -9.17008 | -40.5994 | 2025-08-27 04:25:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 397e14d8-2f63-3096-9a46-393506a6619c | -4.95745 | -55.81038 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d18aae62-1205-349d-b4c0-d9f05ecab286 | -8.55878 | -51.35878 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d306325c-89b3-3df0-8eb4-22daffad5b31 | -6.65251 | -53.19051 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e44f64a2-0d7f-3e79-9e95-8169e23acb73 | -5.87422 | -42.41368 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 589f1477-a823-3967-8cd9-6f67356f6d77 | -6.49397 | -44.68114 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff11855d-1be5-35ee-96af-9c6b30bb91e6 | -8.08817 | -45.01517 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a122c08-78db-3e9c-9380-927c35c41736 | -3.74092 | -49.0492 | 2025-08-27 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 711955d3-a556-3657-b651-d16cacc4efe1 | -8.85613 | -47.17097 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ac6e6ec-6a30-35e9-9c62-dd0736f8bf51 | -4.9611 | -55.82257 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b765433-7f34-3b4b-9668-c1c8f0d66db8 | -11.25901 | -44.96084 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f4ab9af-96ef-359e-a091-16a72f1292a8 | -6.49342 | -44.68476 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6bee7ae-0ecb-330e-a038-9fe3b086e7fd | -10.71911 | -47.09497 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 649a19c0-91d3-3e3d-832d-3134ce98f972 | -6.88295 | -44.40233 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3934a15f-6c8d-3243-b29b-9a95aa63ea0b | -8.2543 | -45.11588 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aa5bcf4-a59a-3816-b75b-277fb873f79e | -5.11609 | -43.20568 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9fc94f09-b7af-362c-a2f0-536e01d8ecdf | -7.44406 | -46.13128 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795f4ab2-a984-32ad-928f-882d707c8c5d | -9.58285 | -55.38515 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb47d5e6-715c-33b1-9183-665db2df9701 | -6.81601 | -58.97346 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8ced4cd-ce3c-3394-95cc-d00e7cdaa4dc | -11.15406 | -44.7919 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c63e67d-e7bb-3236-9bd6-93add6f7f77d | -3.80388 | -51.26214 | 2025-08-27 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b887e54-20ce-3b46-903e-11fef0202c75 | -9.59038 | -55.37361 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54da1bd5-8b37-313a-9ed0-12abb5d7d70a | -8.42741 | -49.6169 | 2025-08-27 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54bf1a64-e40f-313a-8a69-9df6311d3334 | -7.65424 | -42.65985 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 09082d51-37f4-3055-94a6-6c3fc2e3549a | -6.83781 | -58.96582 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 67921d7d-6385-304d-a93b-1395fcf8e72a | -11.03872 | -45.52005 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c43bd7c-3b4c-3694-b65b-fa5ad0b7aa08 | -6.6193 | -53.32801 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb7d1257-8037-3862-a5c5-6a4fde5302b8 | -9.42021 | -48.25301 | 2025-08-27 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da62a516-e031-3d08-ac74-1475387ebbbc | -8.45234 | -43.68212 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b87491ca-9bd9-36c1-9a62-44011c8be100 | -8.48343 | -43.65553 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfa9bf5b-5826-3599-bf0e-8a8a86cb9159 | -5.54163 | -51.05761 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbf9bb41-f7e2-34d3-bf31-f975d884fb0f | -8.68491 | -47.20094 | 2025-08-27 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55c381ad-46f9-3bfb-ad4d-364d787cdfe8 | -6.76919 | -59.67736 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33a3bea8-b8fe-33e3-9793-33d25454aea1 | -8.45908 | -43.66188 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1fff4e7-0882-3a7c-9c97-e3b842074515 | -8.09441 | -45.01985 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6216025-911c-3feb-9264-ba1bab520972 | -6.19215 | -43.00898 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d825e37a-aa42-3106-a46f-a767e62adb91 | -8.07508 | -44.9869 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6953be59-9688-38b1-8bef-fc34fa5f7111 | -10.7748 | -47.0429 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3c5d7247-cb27-3b71-9dae-f5aa4db56b30 | -9.1727 | -49.62789 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README40.md)
