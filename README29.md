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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd1993ac-2635-36f3-b58b-0e7c6c79477f | -15.54906 | -44.34275 | 2025-09-30 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cedec810-0e58-35a7-9ca9-3dc81213a048 | -14.57355 | -48.21579 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b5bc223-c652-3259-9d18-4219fdc1cf5b | -17.7114 | -46.66847 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed172ee1-2d9f-3391-b787-4bbf4d31256d | -16.42607 | -47.03242 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac57dea8-dd58-395f-8b36-8d8a99b5c32b | -17.47201 | -44.04444 | 2025-09-30 03:49:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ae3eeb5-9316-375d-94bf-8e8b6c992e05 | -6.30605 | -43.4721 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 252d9a0a-b4c2-3b1f-afb3-9a7a9925f946 | -6.05123 | -42.45536 | 2025-09-30 03:49:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 93f6e59b-044c-31e3-90b3-1fc2f6cf0fcf | -13.21416 | -50.95521 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 63dc3947-6e41-37dc-953d-990254871ba1 | -13.78614 | -48.01188 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95873d63-aa52-3d52-9df3-e74ddd28dc88 | -7.51705 | -45.44355 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a28e2a65-72a7-38fd-957a-c47ec4c1eea2 | -15.55106 | -44.35504 | 2025-09-30 03:49:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 418f105f-6fbe-3b05-9a5a-251e3906907a | -16.24665 | -44.05722 | 2025-09-30 03:49:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7d6e7ac0-4af1-373c-bcbf-1e323c37b083 | -6.72412 | -47.20566 | 2025-09-30 03:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65e74701-3b43-3633-849e-45e1a07fd434 | -7.55828 | -42.41584 | 2025-09-30 03:49:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 052b92b9-50d6-309d-96f3-d63d4dad45a8 | -7.05052 | -45.20369 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 577df5f3-0cca-3a8c-b7ff-db9d83c57a8b | -14.04285 | -44.95893 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0a563e1-94d0-3907-9fb9-92007f109a20 | -12.22224 | -43.75047 | 2025-09-30 03:49:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c907219-da20-3abf-8719-20372eb599e2 | -13.36799 | -48.16661 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 675b2ba4-750a-3eff-8370-61dbe740a3de | -15.91705 | -46.20433 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bb0d45e-2cb5-3383-8b54-8e79a8fb2674 | -12.79557 | -46.89126 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 531239fb-a5e6-3e59-843a-47c6965bbeb0 | -15.27952 | -47.86535 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c7359c5-4f74-3cd2-8262-66e82812c950 | -12.847 | -47.02176 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38e4e3b7-7308-3e19-8f39-695cea32c54e | -6.25101 | -43.63085 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26492590-b5ac-3ba7-a8e0-91609de34f1f | -13.6551 | -43.35702 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ef842ae-dcb4-3209-bbd0-7e20518ee531 | -15.26593 | -49.50398 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2d717ff-8b92-3cb7-9507-5871376222c0 | -13.80925 | -47.47879 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55a205d9-ecc8-3178-b168-b860fa47b2f4 | -14.7091 | -48.1641 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5115b4e2-25f3-3bf0-ab4f-3e3ac4d31482 | -17.39304 | -47.1487 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 22d30762-9cc7-3360-8e68-0dada129bc5a | -5.77383 | -42.8512 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e2854da8-f4f3-3094-a625-db2e88c38c2e | -15.14841 | -46.43846 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a36cfa87-8518-3d00-be09-14991cc59ac6 | -7.29686 | -42.8633 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bcf74680-091b-330f-a562-0cbfb48ab231 | -13.00238 | -49.44449 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 89945463-1720-3b7e-8c2c-f7d6b8dfa5a0 | -5.9694 | -44.12919 | 2025-09-30 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdf1e04a-6271-3300-9fe7-19dda499df48 | -14.53019 | -48.48555 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 14752593-c358-35e0-8720-22baaedfe558 | -15.27566 | -47.85437 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fdf6a1b-73fc-3e25-bedb-5cc0123534c0 | -13.72758 | -48.67361 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab6acfc5-5a91-3efa-b2f8-f45f8893235a | -12.46181 | -47.96492 | 2025-09-30 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b98d752d-356a-3cbc-959e-3d3df4a2cfcf | -14.70825 | -48.16837 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e8861fd3-c9e1-31df-bebd-21c208422801 | -12.22697 | -47.79594 | 2025-09-30 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a99c9c4-bb8d-3efb-84f8-578f109a149f | -5.74653 | -42.87915 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b7162608-a9bc-35cc-81c1-2abea8ccb09f | -13.56896 | -48.07185 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0219483-5f56-3532-99bb-054a4f8a4591 | -11.88275 | -48.05131 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b843c038-3197-3404-be96-e825bd109e2a | -14.78317 | -48.30749 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b3a37f6-78cb-3c7d-8559-079a561665d3 | -7.28399 | -42.86118 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 64e40082-6869-32fb-9f6d-056c721ed67b | -5.22195 | -45.22895 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aedb66e7-797a-37ad-a9e6-486cd876d02d | -7.01616 | -45.22129 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77c6378c-fa9a-3523-8a95-56084b025d0f | -7.28105 | -42.85237 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8022c30-b1e3-3297-9d61-3bfd5101860c | -12.85273 | -46.88376 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 741492ba-52d0-324a-aae7-8ea6eda30df7 | -5.82795 | -42.79831 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e402851c-fafc-33bd-8723-034c0b9b9915 | -6.36884 | -45.6413 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db5ab0d5-eb7d-3e39-bfae-594bfea550ad | -13.38819 | -48.06241 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9869762f-87ae-3bbf-b5e9-f0d48280c251 | -13.74092 | -47.90252 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ebf6ee5-fe9c-3eae-a3f9-2cff62bb9a0d | -14.7021 | -48.17125 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5701ddb4-6ff7-379f-905a-34e66cab11b5 | -17.39517 | -47.13806 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb761590-02ef-3f67-800c-90eebe16532c | -14.58912 | -48.27773 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f51de0b6-f1e8-3e08-91e7-fc50a12876c5 | -13.56499 | -48.06333 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c1a1597-d014-3286-a63d-75c3b01e1bcf | -13.36985 | -47.31385 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9a82c4a-7ff8-37ad-a6af-b733d03eeba7 | -15.3989 | -44.9846 | 2025-09-30 03:49:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39d50dc2-dadc-3558-9eea-0d41355f674a | -13.49381 | -47.40127 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a836693-ad36-3423-9705-3a1a9cbdd9c9 | -13.59832 | -48.0369 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27a759af-9231-3887-827b-8f9d7afc6743 | -15.6237 | -46.25615 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4c80f3c9-d623-3b37-8abe-268402c11dcf | -17.02823 | -44.98928 | 2025-09-30 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0658d6a6-8cc2-315c-87b0-55fe9215dadf | -7.04417 | -46.42435 | 2025-09-30 03:49:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd87e791-95e5-3c09-8076-c54a3669f74c | -12.81626 | -47.00559 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21f954fe-2377-396b-8004-e3b6919aac8b | -13.3859 | -48.07425 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2e932e0-db99-3caf-ab7f-3ada14eee0e9 | -14.62379 | -44.95287 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be71124c-1b60-3304-ab75-f2057c246e15 | -11.8927 | -48.04819 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79f3c4e7-60d8-3f1e-a0af-4a1219143fc1 | -14.73856 | -45.66668 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| faf55268-de58-3fd5-9b7b-44688cf9235e | -6.82307 | -48.71207 | 2025-09-30 03:49:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a496320c-2bf1-3ff3-bb4b-8d755ca03a45 | -15.05169 | -46.98606 | 2025-09-30 03:49:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccbdefac-5bcf-35c0-aa9c-811e0beb376b | -17.16945 | -42.83827 | 2025-09-30 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f0cc0122-8229-3de2-ad4c-317e74867d71 | -15.908 | -46.22604 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 667c4ed7-7d23-3b40-901d-444ff75141fb | -14.22297 | -41.59124 | 2025-09-30 03:49:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90af57fa-6fcc-35b6-b799-38dd805eb22d | -12.7828 | -46.9026 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bbe0e99-f9a2-3cbc-b218-ca109c9cd6e2 | -12.9272 | -47.13853 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa6e66eb-0e78-33b5-88c3-cdc2446918fa | -12.83676 | -47.0195 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf727594-d089-3bef-8d40-c4db4aca7fc5 | -18.06322 | -41.67532 | 2025-09-30 03:49:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 40d6639a-4c5f-3423-a759-97ac36423ccb | -5.31215 | -44.79248 | 2025-09-30 03:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| caec9b14-ef40-33ca-9574-9c7f08c08630 | -15.47051 | -47.93953 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 473f5027-e629-3ee8-9794-a636c63d7111 | -13.6519 | -43.01374 | 2025-09-30 03:49:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96594ca7-6859-39b4-80de-eb550dc730ba | -12.77634 | -46.85397 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a732b15-0ac9-399e-8b20-72dcb345978d | -15.02596 | -42.33565 | 2025-09-30 03:49:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 169033ea-6803-3156-b2af-15440a82dd9e | -12.94018 | -46.75792 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10756b24-feae-31bf-a082-260688775fba | -11.19473 | -47.21679 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 197f1572-153b-384c-ab1e-a0a18e681074 | -12.23247 | -47.79684 | 2025-09-30 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9964fba3-bfd1-323e-aa36-157dddd7224d | -18.05551 | -43.65776 | 2025-09-30 03:49:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 646760f2-a9eb-3a80-b1a1-0df4935a1926 | -13.23419 | -47.31559 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a41b5003-a0cb-33cf-ba12-45ba2c589362 | -18.46351 | -40.56618 | 2025-09-30 03:49:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 04e56c9f-c999-32a3-aeb2-2f9e914eeb35 | -5.7634 | -43.8397 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dd49312-a48a-3dd1-81d5-15f1a8511b3c | -11.21277 | -47.20965 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d8c01d6-6773-3434-b5e6-02adac0f632b | -14.51802 | -48.43342 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc521003-1b1e-3475-aae8-c0dd986f2463 | -13.82211 | -47.49623 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0673871b-0108-365e-88c8-ca02f041249c | -6.53625 | -42.8327 | 2025-09-30 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0a64af6e-5840-3549-873d-d0494424416e | -6.323 | -44.13293 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8d37ad3-a528-3a39-a3af-f08887c4130a | -11.73578 | -46.85089 | 2025-09-30 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0721930c-3548-314f-8384-6dfae10628f8 | -19.30892 | -43.81194 | 2025-09-30 03:49:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a77aa741-f68d-3914-bd3f-18c9c9b0b26f | -11.79094 | -47.6081 | 2025-09-30 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 624e2189-ee44-3db4-9a8a-b5cb8eb088ea | -14.5626 | -48.46616 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e45e9e63-c9ef-3a80-b351-d7496cc4b699 | -5.70602 | -42.64094 | 2025-09-30 03:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a05b830e-81aa-3be2-be8e-7d58d0e7225c | -14.17034 | -44.30951 | 2025-09-30 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README30.md)
