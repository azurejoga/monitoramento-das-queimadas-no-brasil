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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 912f47b3-78ca-346f-9e1d-3bdb0289a4ed | -14.18259 | -46.28885 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2e375f75-38ff-3330-9d9b-ce4c9639601a | -11.38657 | -50.47586 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c72368dc-f851-3144-a217-97ef6cecbcd9 | -20.45102 | -46.43694 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6dbc94a-e972-3676-810c-fec438c5377d | -10.76378 | -50.54703 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 20a0e00e-ecb9-355f-9431-648a5b561ed9 | -18.89164 | -47.05737 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a57ba0a2-0a5d-3fdf-9796-e493fe4a2762 | -17.44522 | -49.23515 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ab6cf37-e22a-315a-a4b1-4815e6ae61e3 | -11.84206 | -50.58606 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 44d73958-71d5-3964-b1f1-2e7dce8d19fe | -13.9126 | -48.22156 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaa6046b-a137-3622-9581-50d38e524a0a | -12.13423 | -44.83785 | 2025-09-13 03:47:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795c1b90-02ad-39fd-9041-1d5dd33e0a4a | -16.64493 | -49.77704 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a49a857e-2f98-3b02-9a94-adb5c8c4be11 | -11.13381 | -45.23336 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4eb96185-def1-32e2-a1ac-75d7ea1a9e96 | -18.62106 | -44.26488 | 2025-09-13 03:47:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16ba862a-0025-3eef-94b4-e0fca1877481 | -12.82869 | -47.95448 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 092316a5-cc22-3b03-89e1-7f5307e762e1 | -17.41038 | -49.24595 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f7d6ebd-c6c2-3c8f-9300-2c213af0faa2 | -14.68614 | -43.66784 | 2025-09-13 03:47:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da22c8dc-4f03-37df-b175-17cfa7674b2e | -16.33101 | -51.54742 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7ca16250-8bf8-3e57-960a-81e318c44d17 | -14.28762 | -46.08523 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 31eced02-cbd2-3739-99b9-9b03bb4b2164 | -11.62373 | -46.6061 | 2025-09-13 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47607924-0992-346d-9598-8eeb6fcd38b0 | -11.1411 | -45.30982 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e8bd930-aed4-3113-b9ec-2d9e7bd85302 | -10.77415 | -50.5338 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97ee7381-3497-3fec-af92-5505a4709af5 | -14.2287 | -46.29652 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f6be27c-dc60-3f81-a490-8ee6c582f1ca | -11.83586 | -50.55822 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 02a3702f-3d80-3e7c-b5c7-e21f894ba0a9 | -11.70922 | -46.5585 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4330c88-5d72-36a5-bd66-69b1b754f52f | -17.27308 | -47.25068 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 495af1e4-7350-38e4-9d0a-28c87335179a | -17.34023 | -46.67004 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06481f3c-6a32-3b71-b142-ea68ffe2ead9 | -9.00304 | -45.7829 | 2025-09-13 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d76edc1f-fc0c-3153-911e-adcbd65e3167 | -14.21229 | -46.27798 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e5396b25-bd19-3031-a82c-7a02c2b678cb | -17.28159 | -47.25109 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6201fb4-6e4c-32c8-bb53-adb32e2d1696 | -9.96315 | -50.30199 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dcda24d3-853e-3576-b110-514ebf1cd0bc | -14.17669 | -46.26304 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 549d592a-c626-3c96-8b2f-ac673a386715 | -13.91167 | -48.28729 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f57da697-6106-3447-9315-6227ae6aa5c2 | -13.92019 | -48.27643 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c4db7b91-8791-3c29-8711-52cc2f2cd891 | -16.3294 | -51.54295 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56ec7f2b-23d3-39dd-bc00-67a290531fc8 | -14.18549 | -46.27421 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 78be1c41-5a1d-396b-9952-fa15a4266270 | -20.02054 | -47.64889 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fa4a2f5-fb36-3b95-abe5-15ba75d0cd09 | -11.70608 | -46.55415 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13a211e3-1939-30de-93b9-e2c1349bd0f6 | -7.43128 | -44.41235 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9af6378-114f-379c-962b-7be254018daa | -10.77296 | -50.53373 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c2dc3fe3-e84c-3de9-ac39-e05f888edc8d | -14.22735 | -46.28545 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 2bdb45ae-ee11-3763-9ddb-0cc9c4c9f0e1 | -13.00898 | -44.11473 | 2025-09-13 03:47:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2629a9b9-2df4-35cc-8cad-5c85c584c50d | -14.19145 | -46.2719 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 00eb292d-9674-3cc1-993f-d455fd333cae | -11.57059 | -50.57925 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 466265b2-641b-3fac-a321-eca8e0f7642d | -13.88712 | -48.28428 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63c00aae-49b8-3977-88a1-4b9a8920e71b | -11.84802 | -50.55756 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b2d64900-862a-383f-adf7-7afd4fa3af33 | -9.05146 | -47.03413 | 2025-09-13 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eba7b8fc-43d7-399f-b598-eb4ac479f1b4 | -18.00135 | -46.92645 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d567f10-84c6-369a-8214-6195dde4becc | -7.43067 | -44.41573 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bd246701-6fae-34db-af1b-d23c98532498 | -10.78995 | -45.99723 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b9252c-f638-3680-9650-6bbe7713b77a | -19.6527 | -45.87191 | 2025-09-13 03:47:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3f42caa-d262-38ac-897a-07f1875ddb8f | -12.80083 | -47.99475 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5b5ca52-589d-3064-8459-e519ce1159a1 | -14.17729 | -46.28778 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cfd33261-fddb-36f9-901d-96bde8753286 | -16.79466 | -51.36107 | 2025-09-13 03:47:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f62954e6-fd80-3439-9df4-2de5ab2ab385 | -12.9043 | -47.95302 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0cd5e2c-924f-347d-8562-30a6def12c9b | -14.21741 | -46.29773 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 7fc66f4c-3abd-35f7-b224-7e85d4b5613f | -11.70433 | -46.55343 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 954f1c0f-3a70-309f-8294-b18cf8fbc3cd | -12.95228 | -47.99733 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfab96ac-20c7-3c08-bfbe-7cb94afb5484 | -16.64359 | -49.78912 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49a98072-2bd2-3b0d-931b-40209d87e8dd | -20.02098 | -47.64918 | 2025-09-13 03:47:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbe55c56-52ba-3275-9ed5-4297050d2cce | -14.19012 | -46.27862 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| eb377a33-e4fd-3727-b2b4-72de31e7eb16 | -17.28833 | -47.25743 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ce8ccb3-a3b9-3ebf-8737-59b0d718d38d | -13.15071 | -47.13804 | 2025-09-13 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f2df31a-352a-31df-8a59-b5f6ef1cfa32 | -18.05623 | -45.45781 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b3429db-ce7f-312f-a8ce-7f54988f33ce | -10.22785 | -48.63665 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fca9dc1a-d65a-37c8-9c81-797997eeb47e | -10.7876 | -44.78133 | 2025-09-13 03:47:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffd35647-8044-3063-931a-2b00563e36ec | -11.44021 | -45.62702 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4765930c-9433-3271-ac87-4fdf69665f73 | -14.22997 | -46.3003 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56a7b1d7-a0b9-3285-8f6b-7f0048b6ec15 | -11.44814 | -45.6311 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf2f8475-05ff-3554-a4cc-4ccc407d8ca8 | -19.97822 | -46.92764 | 2025-09-13 03:47:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be1e1a98-d13e-3566-b153-6b8efd1c58f5 | -11.3588 | -43.50002 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c659e4bd-180d-314b-9f7a-71c923f401ca | -12.83521 | -47.9485 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 58e7f291-d7e8-3eb7-bcd1-0547d317c4ea | -10.33314 | -48.81587 | 2025-09-13 03:47:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8598ddc-645d-3fce-a39b-378c11901727 | -11.73706 | -44.21502 | 2025-09-13 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f387dab3-0d7d-38eb-8207-ad1a22dd339a | -11.15427 | -45.2398 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 328c9219-d3b3-3541-abe1-d8cd01c94c37 | -12.12956 | -47.59975 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 980d9970-17c4-3940-84e5-55cfbc1bf2ee | -12.82777 | -47.95431 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 34701ad1-5fc9-3941-9b03-f4d076c02ad6 | -8.1727 | -42.43657 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf51ff5d-3856-38d5-9263-e783aebd24b4 | -7.44533 | -44.39464 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 178d6084-7573-3a82-8963-c539f42db108 | -13.89464 | -48.24784 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90c75407-a31e-3a6a-832c-556794405904 | -11.48395 | -43.61695 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b40e0303-7450-31eb-8d36-b0dbf5cd9285 | -18.06764 | -45.44921 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6eddf2b8-240d-3a48-9a26-7457323240c5 | -13.88393 | -48.26926 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a142be1-631d-3401-9bac-d21d6fca9870 | -12.84566 | -47.93303 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c91c6fad-0fde-3bc8-a372-c8202007963d | -14.22009 | -46.29446 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| dcf20a14-3145-31b9-858a-6ad87366687c | -17.42827 | -49.2266 | 2025-09-13 03:47:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55d624d0-8356-311b-8324-83520375b957 | -17.12884 | -48.48273 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b31568d-ded5-3c66-b066-dfd89e6f5cf1 | -16.56095 | -49.22516 | 2025-09-13 03:47:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c86abc18-7afb-3580-90c0-93fbd3df6861 | -14.21602 | -46.25896 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 577491eb-3d21-3b65-ad4a-0f7e0e99e356 | -12.09121 | -44.87354 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5222b4ef-e96a-3a2a-96f0-3c11d40c7f41 | -11.33597 | -50.79034 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bc4b980-084d-31e5-a906-d5d67c6b5ad4 | -14.18786 | -46.29008 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 328837b0-7622-3b3c-8b2f-dba3695bc146 | -13.24675 | -43.76577 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fc3c2b3-b4ea-3f92-a403-61a1ef27df5d | -11.43241 | -43.55586 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 928face1-e857-34ba-87ca-f85871e18e36 | -11.86874 | -46.76039 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 676046fb-6527-3be5-9663-c8dcd1265c45 | -18.89671 | -47.05859 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35f2440c-f567-3d3d-adaf-1ca681aa8ec4 | -14.21682 | -46.28296 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8f6c980a-d261-3760-a873-8dd0fb31b2b8 | -12.10374 | -44.89004 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4068d7d-5e66-32eb-ba38-4f30ae76c7a1 | -14.18182 | -46.29277 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6ad8b9ab-f6dc-3b83-9995-a255ea9e8d49 | -12.6566 | -44.23917 | 2025-09-13 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64eaea85-0948-3852-ab3c-733e27d1d3af | -10.76851 | -50.52485 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 26a3700d-624f-3e8e-a1e9-425d3ebb7acf | -17.41847 | -49.24255 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README35.md)
