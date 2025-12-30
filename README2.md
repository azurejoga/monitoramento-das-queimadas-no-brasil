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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0f4a063-6096-301f-b9be-be3d359ee4a7 | -4.345 | -44.1247 | 2025-12-30 02:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ed5d9051-5f68-333f-b7d4-af2a113a2c71 | -7.54481 | -35.18253 | 2025-12-30 02:51:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| f631241b-cbad-3efe-9e1e-7b6fe4cb3900 | -7.54382 | -35.1879 | 2025-12-30 02:51:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 60e4f843-bbee-32ae-9c4d-d133cacd7648 | -7.54462 | -35.18444 | 2025-12-30 02:51:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| a80d878c-eb6b-3439-802e-4bdffa00ff15 | -9.91094 | -35.96622 | 2025-12-30 02:53:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 33ab5d7b-adbc-3156-80bd-a428653f1f00 | -9.91204 | -35.96064 | 2025-12-30 02:53:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| ae613502-2b03-3b24-a142-f4e239730475 | -18.832 | -51.6099 | 2025-12-30 03:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| f41a905d-2673-3d6c-a8b1-175d85c64991 | -11.7589 | -43.3136 | 2025-12-30 03:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 421be0d3-adce-3c6e-9945-ec0d4c26364c | -18.832 | -51.6099 | 2025-12-30 03:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 7221b0d1-52a4-37ca-9d24-42cb618a5815 | -3.89737 | -42.55898 | 2025-12-30 03:21:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aa7844b6-2abd-3a31-891d-17f898932f95 | -7.15406 | -38.66777 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 046ad3d6-c9ac-3c10-9072-4f1506a32213 | -6.23332 | -40.29994 | 2025-12-30 03:21:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1fde3b37-0cee-35a8-a8ea-a2bbfc65a879 | -5.48877 | -38.05128 | 2025-12-30 03:21:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 015a0020-d9cb-3366-a9a5-b75faf8af394 | -7.55 | -35.18069 | 2025-12-30 03:21:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5b7323e-a56f-3183-8eba-3c62ea308b45 | -6.24246 | -38.42307 | 2025-12-30 03:21:00 | NPP-375D | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 88749d87-3bd7-35d1-8192-b58a3332d3b3 | -7.14796 | -38.67024 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f44c0b13-5f39-3058-8d90-79c90cbba5ee | -9.89255 | -36.03006 | 2025-12-30 03:21:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2942c1c4-400b-3e1b-a4e5-d88625e5653d | -9.89285 | -36.02735 | 2025-12-30 03:21:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0f61a1b-134f-3fa6-821c-2d7fef6405fe | -5.48817 | -38.05471 | 2025-12-30 03:21:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3346a501-faa3-30a0-8b2f-ebecb1b1b473 | -6.99117 | -38.93885 | 2025-12-30 03:21:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 662fea6b-5bc0-33c2-810f-d169c3cd56f5 | -6.70887 | -35.41496 | 2025-12-30 03:21:00 | NPP-375D | DUAS ESTRADAS | PARAÍBA | Brasil | 2505808 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb02ed78-1061-361a-9a12-665ef77cb7f0 | -5.48936 | -38.04789 | 2025-12-30 03:21:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e68f6c17-1319-3413-853f-7f34c8dc0a13 | -8.30296 | -35.21944 | 2025-12-30 03:21:00 | NPP-375D | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29b9eb97-4ff6-37b7-8430-6f6bcffb7dbb | -7.15498 | -38.66329 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d13a6ddc-3d36-309a-bcfe-f5b8314dcf0d | -7.14829 | -38.66926 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 70121c9d-c6d1-300f-a57d-3d0f2a6c438b | -6.23446 | -40.30049 | 2025-12-30 03:21:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 56fc850a-daa2-3d5a-84a9-bfc203de439e | -7.54572 | -35.1799 | 2025-12-30 03:21:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3729689a-96e5-371b-b799-b9f47fa518c2 | -5.1433 | -39.47296 | 2025-12-30 03:21:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 307ee69e-69b4-3b88-940d-93658c8f07ef | -7.1486 | -38.66674 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3dcbd34-be34-32bd-abde-5200af9d1d0d | -6.23946 | -40.30114 | 2025-12-30 03:21:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65656e3d-6d69-3e03-a49d-d8c633c1350f | -8.3299 | -37.71113 | 2025-12-30 03:21:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f31b0c2-9f8e-333a-94e6-7c6a6b3d6694 | -6.99291 | -38.93981 | 2025-12-30 03:21:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a63086be-69ab-3aef-b157-33372df5898f | -8.78428 | -35.74793 | 2025-12-30 03:21:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f323a292-5c98-3fc5-96d6-77a177405c7e | -6.11629 | -39.80458 | 2025-12-30 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e664eff5-d1ba-33f0-8a65-a5f6cc8cb9e1 | -5.95145 | -38.63164 | 2025-12-30 03:21:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 30392696-f0dd-3202-9644-702f7d4717f6 | -6.24164 | -38.42469 | 2025-12-30 03:21:00 | NPP-375D | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 62d1d024-9c1d-3321-9db7-0d1c8eba3dc1 | -7.14891 | -38.66576 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 06760cb2-11f9-3ede-86d5-39d03bb1a8e0 | -6.11708 | -39.80027 | 2025-12-30 03:21:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9fb353dc-46d1-3f47-a264-1d1a6198ff8f | -5.84836 | -35.31799 | 2025-12-30 03:21:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7360c157-28a3-347a-8cec-0d23708b35b2 | -5.14003 | -36.36683 | 2025-12-30 03:21:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 9e88dc27-fff0-3d8a-a882-bbe73d548c02 | -6.70961 | -35.41066 | 2025-12-30 03:21:00 | NPP-375D | DUAS ESTRADAS | PARAÍBA | Brasil | 2505808 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 113a4710-a94c-3ac6-a471-7740ae41898e | -8.32488 | -37.71016 | 2025-12-30 03:21:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9eeaa91-45e7-3e3b-a714-c59342973adb | -9.88895 | -36.02502 | 2025-12-30 03:21:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c48f15f-71b9-39dc-b16c-63bff2fdf29d | -5.95703 | -38.63253 | 2025-12-30 03:21:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e2c4dca7-b9d0-3d68-ae5b-069de8ae43d7 | -9.88849 | -36.02653 | 2025-12-30 03:21:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ddaea594-4972-38cd-b0a4-c8260e4b9798 | -9.89332 | -36.02582 | 2025-12-30 03:21:00 | NPP-375D | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 06c8be9e-e27a-378d-a654-500f0129030a | -7.1547 | -38.66427 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ddbf0bde-6610-373b-b97c-99fbcc1e4f75 | -6.24306 | -38.41975 | 2025-12-30 03:21:00 | NPP-375D | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0e75b49-de99-3350-a0da-3b731181805d | -6.24221 | -38.42139 | 2025-12-30 03:21:00 | NPP-375D | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c0b04e84-8376-3cc2-b52a-f2a21ca2b35e | -7.04093 | -38.26233 | 2025-12-30 03:21:00 | NPP-375D | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d59d3940-dacd-39a4-8893-0ba7b2d4b95f | -7.15437 | -38.6668 | 2025-12-30 03:21:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 842ccfe7-ab6a-3ca5-b9c7-34d49b791e7a | -13.47878 | -44.02058 | 2025-12-30 03:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d1c29237-4560-3055-ba81-2db595c43645 | -13.48015 | -44.01439 | 2025-12-30 03:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aaed32a6-8990-3a70-bbb6-c3b2208c673b | -13.42771 | -43.86018 | 2025-12-30 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15c6ee5c-e872-37ab-a818-a0acbd82fa7f | -15.13606 | -45.28457 | 2025-12-30 03:23:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f09b7903-b225-3863-a678-8eb99d302716 | -13.47951 | -44.01295 | 2025-12-30 03:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c13bcf2-1b48-35f7-bef2-5feac382b6cd | -13.42758 | -43.85471 | 2025-12-30 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b57ba980-82c2-3ec2-9ed1-04cbf0cd80cf | -12.10427 | -38.00021 | 2025-12-30 03:23:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ea17127-e479-3c7e-ab43-fac89e88afa8 | -13.42906 | -43.85398 | 2025-12-30 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d684a90-0e4e-35cc-9894-91f2fb615079 | -12.51388 | -43.69134 | 2025-12-30 03:23:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cac9823-4e21-3d1c-9dac-f94c7b7da749 | -13.47135 | -44.01787 | 2025-12-30 03:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d53e0c2d-9e99-34a8-bb9c-b74872e92f88 | -15.54519 | -42.9484 | 2025-12-30 03:23:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5339f6eb-e09e-30cc-b677-c183e96a0954 | -15.12742 | -45.28996 | 2025-12-30 03:23:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c3eae76-e372-388f-b4cc-bcdbff2bc3c5 | -13.47268 | -44.01167 | 2025-12-30 03:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b17a4679-e122-3cfc-952d-b616856091f3 | -15.129 | -45.28295 | 2025-12-30 03:23:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21f0fdbf-7883-392d-bfce-a770073d1742 | -13.47818 | -44.01913 | 2025-12-30 03:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aa6d287d-64f4-345a-a618-6f627161b1ba | -13.42627 | -43.86092 | 2025-12-30 03:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8e7a7d8-8533-3c81-bd74-0f99787c220f | -12.09948 | -37.99921 | 2025-12-30 03:23:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a11bb8bc-c996-313a-aad8-0273dd741186 | -21.15727 | -43.08026 | 2025-12-30 03:25:00 | NPP-375D | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7717ac8e-0c26-326f-97bc-f41c002c2bb8 | -20.53177 | -40.94035 | 2025-12-30 03:25:00 | NPP-375D | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1ff8d4ab-2a0f-3f79-95df-a5992fa303d7 | -15.13074 | -45.29079 | 2025-12-30 03:25:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be5fbdf8-d336-31f1-91a7-413409c8020f | -17.2423 | -41.34624 | 2025-12-30 03:25:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34180db4-2f3d-3031-a393-ab90ca1d5b9a | -22.02808 | -42.30977 | 2025-12-30 03:25:00 | NPP-375D | MACUCO | RIO DE JANEIRO | Brasil | 3302452 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 13207816-359c-3854-98a8-3546fa241090 | -21.15432 | -43.08139 | 2025-12-30 03:25:00 | NPP-375D | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f38c88af-4c63-32a3-9b76-bea447c087d7 | -20.53224 | -40.936 | 2025-12-30 03:25:00 | NPP-375D | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6061dc29-5b1b-3945-9b15-13302c93608f | -20.50513 | -42.46972 | 2025-12-30 03:25:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4b88b2e4-1e86-366e-a700-adcd6a04cc66 | -20.50418 | -42.47408 | 2025-12-30 03:25:00 | NPP-375D | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ee70ef93-6c4b-3cc3-a334-eb80fe7a6829 | -22.02742 | -42.31277 | 2025-12-30 03:25:00 | NPP-375D | CORDEIRO | RIO DE JANEIRO | Brasil | 3301504 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cd17cc1-0408-3782-9cff-16681956ed52 | -15.13238 | -45.28371 | 2025-12-30 03:25:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b10ff90b-4055-36fa-8b5d-6e116b6f4e5a | -21.15351 | -43.08506 | 2025-12-30 03:25:00 | NPP-375D | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d734d4ce-d374-3b5c-b865-6a87a7cd0726 | -16.0114 | -41.68128 | 2025-12-30 03:25:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6399848e-c7c6-3f42-b0fa-16bf67489833 | -21.15904 | -43.0866 | 2025-12-30 03:25:00 | NPP-375D | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 76eb91dc-83ff-3f63-86d1-4db175f8c3e6 | -16.00574 | -41.68007 | 2025-12-30 03:25:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1b1a5c98-c354-3eff-9c36-d1e9806c812e | -21.15989 | -43.08274 | 2025-12-30 03:25:00 | NPP-375D | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 18f63bd8-2c32-3907-a724-8b8b0a18da9e | -21.15641 | -43.08402 | 2025-12-30 03:25:00 | NPP-375D | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 77dba137-4d79-3007-96aa-f4403ceb93a8 | -5.46187 | -40.70116 | 2025-12-30 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2b65e69-9706-3d89-ada4-8055f575a98a | -6.70908 | -35.41318 | 2025-12-30 03:42:00 | NOAA-20 | DUAS ESTRADAS | PARAÍBA | Brasil | 2505808 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd2cbc7c-110c-3c0a-8462-c97870b44356 | -4.60598 | -46.59678 | 2025-12-30 03:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 601cfc44-c31e-3c6e-80b7-31e05d460dec | -5.48786 | -38.05122 | 2025-12-30 03:42:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6a778159-9fc1-3f9e-80b3-8f56bea162d6 | -3.54807 | -43.61003 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ddfb074-441b-3f4a-bb3a-5673e9bb25b8 | -3.55488 | -43.60153 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f63c72ab-cde5-300d-866d-37d756f5c455 | -3.39343 | -42.10934 | 2025-12-30 03:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3fe527a7-5f73-3c03-84e7-3be45892a75c | -4.07897 | -38.25656 | 2025-12-30 03:42:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24ce3069-ce75-3396-9660-88053b1084c3 | -5.14033 | -39.46769 | 2025-12-30 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df717358-d7ba-3d44-a101-ee00a17e296f | -5.94562 | -35.62164 | 2025-12-30 03:42:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 749538eb-7ccb-3e1a-a369-c14c8c80502e | -6.24323 | -38.42243 | 2025-12-30 03:42:00 | NOAA-20 | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8e0b399b-8846-3044-b298-b1fa235b9574 | -5.68839 | -39.0427 | 2025-12-30 03:42:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f68fd4b2-040d-3c41-ac52-e3fed4080764 | -3.39374 | -42.11058 | 2025-12-30 03:42:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4d518e01-5104-3f68-85d0-e0d50aed2d16 | -3.54282 | -43.60905 | 2025-12-30 03:42:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ec37b3f-4fe0-3e14-9132-fa97febc35d3 | -3.8976 | -42.55955 | 2025-12-30 03:42:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README3.md)
