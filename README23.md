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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca3ade30-de6b-3f98-8a5e-b680a3018cef | -15.32551 | -43.80289 | 2025-10-27 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d2327da8-1aa2-3761-bc01-2c62bab0c405 | -17.31487 | -43.61354 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b200cddb-2cd7-33cc-a511-1725436c8977 | -14.01957 | -43.26708 | 2025-10-27 03:45:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f1016a7-98a3-35f2-bf56-7cc6314a57c3 | -17.42618 | -46.86569 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 683cf302-28a4-3563-9baf-6e2b983cb361 | -12.31521 | -47.46636 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d4e5e2d-c58f-36d9-9ded-2874766682f4 | -14.64047 | -48.41486 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79a06c37-df9f-39c7-830d-a097864e2e6b | -18.00348 | -42.90555 | 2025-10-27 03:45:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba4a6e11-f9eb-395f-a0d3-ea2b50d207f4 | -14.63498 | -48.40256 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1be66ef-176c-3e71-a901-c5d3d41dbb9d | -12.32213 | -47.46241 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 947d5930-0aaf-39e8-9694-03bff43bd2e2 | -12.87073 | -48.65215 | 2025-10-27 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e04a788-975b-3cf6-9ce0-273844a2cae3 | -13.4787 | -47.46918 | 2025-10-27 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b792b606-165a-3306-9a30-14a698ef1273 | -17.4106 | -46.88906 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b609183-bf51-3725-a9b0-1f0eab3ead1a | -11.72054 | -50.24806 | 2025-10-27 03:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df558b63-d125-3744-9580-8df0f3984c20 | -15.2976 | -42.3892 | 2025-10-27 03:45:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ac937292-8496-38e4-b6ab-c27b94211111 | -14.56638 | -48.00096 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff334e86-086d-3f65-afe5-ed3dae5adc4a | -19.69395 | -42.26116 | 2025-10-27 03:45:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 74fcd794-61b4-35ca-94fb-8518c8da9cba | -14.44353 | -47.77775 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ce9bc86-d719-3655-b2a2-74dfd0b39f2f | -12.07761 | -47.98985 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dfa3801-780c-3df0-ade5-921cd81f7dc7 | -19.6656 | -44.66067 | 2025-10-27 03:45:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7c9704c5-6d96-3dcc-a4b6-71c067810b0c | -15.32399 | -43.80568 | 2025-10-27 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 84058810-90e6-38ab-81c1-098e1bd9d51f | -14.43737 | -47.77831 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 97a30bb2-9c44-3c40-bcec-91127fd84868 | -12.87296 | -48.65643 | 2025-10-27 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d182b14-56ea-3867-969a-0fb2f3a85890 | -18.63234 | -43.06534 | 2025-10-27 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 4b07dc83-ab31-352b-a6c7-ea8cc95bb8df | -14.99957 | -42.2779 | 2025-10-27 03:45:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fb78286d-ce27-340c-b065-0fdebc5826e3 | -13.55271 | -44.26196 | 2025-10-27 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11313375-ad9b-3b77-9eff-d40d2cea44a8 | -12.28106 | -43.75695 | 2025-10-27 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c3b1313e-78f4-35d9-9a28-9b4846f99637 | -12.0853 | -46.40307 | 2025-10-27 03:45:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d96c2097-430e-3e83-88dc-ae20b341d1e8 | -12.04939 | -46.38029 | 2025-10-27 03:45:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2e24e8a-3e48-355a-ae9a-47069ac18426 | -12.97267 | -48.39424 | 2025-10-27 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7893bfe1-9f6a-31fd-97be-dca6f5f00dbe | -14.63117 | -48.42111 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53ddbcff-2a51-3ea9-9ce4-05f9534048cf | -14.49292 | -47.89063 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2566763e-ea48-3361-b2ce-6d3eb14f502f | -12.5009 | -44.33827 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69ac3ffb-1fe9-344c-b181-94a0dfa0553f | -13.19871 | -48.43829 | 2025-10-27 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c324eff3-879d-3472-bebb-8e00f0b18254 | -14.63451 | -48.41341 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c20b9c1-096c-3253-a1d2-c32a41cbb703 | -14.63901 | -48.41346 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 785718a3-4472-31b1-8d51-5fb851c748c4 | -18.63167 | -43.0689 | 2025-10-27 03:45:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 883eb3bb-dae1-398f-8cba-f470542c7d72 | -12.31903 | -47.46441 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 65d7e42a-1814-3771-b633-1fbefe37556c | -12.33364 | -47.46637 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc0ba9db-4dad-3634-bd41-19c446582fc8 | -17.31609 | -43.65198 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c45a94c4-1a65-3a44-94b9-c0cf1f0ab810 | -17.50772 | -44.32655 | 2025-10-27 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9a307c5-a3d4-384b-8cfe-8661c9074373 | -12.49477 | -44.32443 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0a7d247-f1f8-392f-875f-5f0e1715c327 | -13.22105 | -44.55616 | 2025-10-27 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a65338e2-8408-30ac-b980-25f2a0b55e22 | -14.25401 | -48.1355 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa951f47-e3e3-3239-bb9a-73e7f78cf50b | -15.13671 | -47.94796 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cbd9e95-ebe8-36d5-9735-4fb3960c9c09 | -15.14934 | -47.94521 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ba1b850-bf76-31cf-99e8-2b0356dccc70 | -17.50674 | -44.33156 | 2025-10-27 03:45:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b87572f-131a-3353-84da-df32e087a35c | -11.72198 | -50.2412 | 2025-10-27 03:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90d4755e-f243-3bda-83f4-5ffd567e1d74 | -15.18645 | -47.22564 | 2025-10-27 03:45:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a94bc0cd-2146-32d2-adc8-abe0acf10130 | -15.12365 | -43.25818 | 2025-10-27 03:45:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 81fb7977-2f8e-370a-9504-4c781d41076d | -12.04862 | -46.38424 | 2025-10-27 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5e94be6-0a0a-3cb2-b22a-9c154154ab50 | -15.56122 | -43.03818 | 2025-10-27 03:45:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65e9cfdc-7d25-36a3-a515-5ce2bd5b88b2 | -15.14399 | -47.9413 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38ed1bcf-96ff-3f43-9f6d-e6d31deb8560 | -18.34829 | -43.96045 | 2025-10-27 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbb3c3a0-0d03-3737-a48f-73dbcdc35860 | -14.63156 | -48.42725 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 045cdc79-9803-3d63-9a84-1bf89cd41f2f | -18.58366 | -42.74363 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9fe75116-c0d2-336e-a6dc-5e993d910afb | -14.49786 | -47.89619 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f2d85a8d-a955-3be3-9f4f-93e3862d9628 | -12.3269 | -47.48605 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8aef6d58-eb19-3bb1-b8e6-7bbb76ca2608 | -17.23387 | -46.79832 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 222a9648-cf70-3c1e-a7c1-f69baf7b6c01 | -14.62332 | -48.37778 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8078e292-4149-337b-9892-b691da8cad45 | -14.45485 | -47.78146 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7eab232-5a6b-3cef-be28-72adb98840f1 | -15.96584 | -43.01827 | 2025-10-27 03:45:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b4b2746-faa7-3698-9dc0-cf67c2a884b3 | -16.81933 | -44.00919 | 2025-10-27 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3d41b32-e6f2-3dac-b4bb-f79d0d2c5f70 | -15.29208 | -42.94077 | 2025-10-27 03:45:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b005bdf7-0fd0-3a76-bb74-15634de3e7d7 | -17.32059 | -43.60619 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22ebfbfa-315b-3d78-ae18-d2c7c5e3f8ed | -18.34789 | -43.95948 | 2025-10-27 03:45:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 877a0071-eecb-3208-9641-31a2b5f13fcc | -12.50779 | -44.32837 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6abf4fc1-afe5-347d-b886-98357d6ab525 | -18.26487 | -45.36641 | 2025-10-27 03:45:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37774d70-3ad3-3e8f-a409-93cd38108dae | -17.42035 | -46.86779 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4aa208c2-aba6-36d3-bd56-131d9abd84e0 | -14.49862 | -47.89246 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e107099-cdea-3bec-ae76-893bf6ca2535 | -12.31623 | -47.46117 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76f758af-81be-3f96-a27e-693dcceb7de5 | -13.36461 | -47.40983 | 2025-10-27 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb93a3a7-69fd-37ae-bbc0-5e2ae8938050 | -12.32795 | -47.46403 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25bd5d9c-5bb1-31bb-b50b-c8fde8872578 | -17.08076 | -43.19226 | 2025-10-27 03:45:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8993165-8b68-3ce4-8c96-39e4d364da81 | -18.26756 | -45.3773 | 2025-10-27 03:45:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8244ce9-d38e-36d7-9eb4-93446db9d0f7 | -14.44777 | -47.7864 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4446d8a1-9ec8-341e-bfe9-39d9b15ee0f2 | -15.29894 | -42.3819 | 2025-10-27 03:45:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8236ba87-a3f9-30b8-9dd4-ad5ec52c7fee | -15.14979 | -47.94242 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7a3add3-7fba-393b-aa0d-98e661f19cb7 | -12.52373 | -47.56553 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8bc56225-c51c-3a25-8d5c-ff5a5bc6dc7e | -15.32485 | -43.80123 | 2025-10-27 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9e520f6-9c7c-3c7b-b366-898131d642a3 | -14.44965 | -47.77739 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7ef6d70-8eea-322d-8cc2-528eda019432 | -17.23844 | -46.79918 | 2025-10-27 03:45:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 906f1786-bfea-317e-9462-8ad73daa74b2 | -14.44435 | -47.77387 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6df541a7-fc30-3fd8-8925-7696497ce1ca | -12.86674 | -48.65482 | 2025-10-27 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1be7939-cfb4-3d02-aac7-4490ece3259f | -14.98212 | -43.55199 | 2025-10-27 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a38ef3c1-3dc9-3bcb-961e-8ad1957bebfd | -14.6355 | -48.40875 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 041a4564-c419-3ee6-8fe7-c2ca2608b0fe | -16.97347 | -42.64604 | 2025-10-27 03:45:00 | NOAA-20 | JOSÉ GONÇALVES DE MINAS | MINAS GERAIS | Brasil | 3136520 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 449455b6-9ef1-3c35-9b73-7b7a00967b0b | -18.51285 | -45.09224 | 2025-10-27 03:45:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7ec4d9e-2426-3e92-aca9-a817f777e9fa | -12.08449 | -46.40724 | 2025-10-27 03:45:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9df1bd1b-949a-37f9-b435-41d64de5cf3d | -12.5092 | -44.32718 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cb3cec8-5784-3c23-a8f1-92f49fded82e | -12.04089 | -46.39425 | 2025-10-27 03:45:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82e4fd93-f12d-3246-9906-5bf79fecc46a | -13.23231 | -47.99648 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed68b548-c74c-36b9-923d-169020519f4c | -16.62655 | -44.58608 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43fcfd71-bc8f-3170-850c-d0b8f8bf50e4 | -19.54881 | -44.1612 | 2025-10-27 03:45:00 | NOAA-20 | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 880e2c00-628c-3f87-a13a-bdde1a8d6c92 | -14.62241 | -48.41133 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dcbdb46-ba77-3f56-b2f9-5d56582a0936 | -17.16434 | -42.33537 | 2025-10-27 03:45:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67f956e9-93c2-330e-bf66-9a57040cda40 | -14.43849 | -47.77604 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae27b3e5-3736-3701-ae40-9f42ef408279 | -12.30607 | -47.45048 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f1374aa-0bab-36d0-8ef3-8a02b3801b9e | -13.65224 | -44.3097 | 2025-10-27 03:45:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f66080e5-cba8-3edc-be44-7b2fb2406db8 | -16.37529 | -47.4204 | 2025-10-27 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c71a7c1-663e-3132-852c-594dd6469f4f | -15.8666 | -45.25806 | 2025-10-27 03:45:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README24.md)
