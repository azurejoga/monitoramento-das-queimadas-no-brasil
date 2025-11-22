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
| 4df273d7-3732-3f40-a9e3-0c1263774e10 | -4.0382 | -42.5129 | 2025-11-22 01:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| ce174c73-089a-3bc5-917f-1b72f34cc372 | -3.257 | -45.4709 | 2025-11-22 02:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 92.4 |
| fd3850be-2433-364d-ab0b-ffc263ec4a6d | -3.2756 | -45.4702 | 2025-11-22 02:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b119b358-824b-3bb0-b7f7-97c6e74e2c5b | -3.4507 | -47.6289 | 2025-11-22 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ce91bcaf-f697-3523-a5a2-cbb0ef1db725 | -20.6358 | -47.4322 | 2025-11-22 02:20:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 2e3d1858-efc9-3100-aa90-8c0954cd78c6 | -20.6152 | -47.4371 | 2025-11-22 02:20:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 28fe3eca-ba25-36ab-89ea-aa598c24cbf2 | -4.038 | -42.5365 | 2025-11-22 02:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| ae16e6a9-b9c4-3eee-9c3f-de58027513cd | -4.0382 | -42.5129 | 2025-11-22 02:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 328487f7-156d-35f3-a07f-244ad40e3ac3 | -7.30076 | -35.15842 | 2025-11-22 03:04:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 00f89248-edbb-3c85-9d40-6bba7038637f | -7.30553 | -35.16277 | 2025-11-22 03:04:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 71e98cb8-c9d7-36fc-8548-71729a1aa90e | -8.24448 | -35.0188 | 2025-11-22 03:04:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9c64f081-9a20-3a9f-867f-c7804f4f3d9e | -7.30614 | -35.15934 | 2025-11-22 03:04:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| a5e6aa1f-f7f0-3bc6-b2b7-29db8cb99410 | -7.30675 | -35.15591 | 2025-11-22 03:04:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| c6fef323-42f8-36fc-a8f2-5e20b7f10644 | -8.24388 | -35.02206 | 2025-11-22 03:04:00 | NOAA-21 | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 250e1dbb-a8ae-3ac4-a421-24a1d7d39efe | -21.07236 | -43.32932 | 2025-11-22 03:08:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 234d54fa-fc44-3902-b4ae-3a6172364314 | -21.07053 | -43.33655 | 2025-11-22 03:08:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| cee423c2-a522-3677-bedc-f55ea503cc62 | -21.07166 | -43.32895 | 2025-11-22 03:08:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| b6a6b39e-657b-3cda-bf8c-895e68a287f1 | -19.62592 | -41.84885 | 2025-11-22 03:08:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fe116071-0964-352c-bdcc-984477b6b8f9 | -19.62595 | -41.8503 | 2025-11-22 03:08:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 572e7585-785e-3f90-b708-13aff4b28475 | -21.06989 | -43.33614 | 2025-11-22 03:08:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| cb04885c-dded-34ce-8570-31762cc18859 | -3.26957 | -42.21017 | 2025-11-22 03:32:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 549505c4-d9ce-3893-bd1b-c594fd974b45 | -4.03136 | -42.52431 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f1534497-7919-35f2-882f-30cce0daa5ac | -4.03838 | -42.52214 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 4108b969-48a7-33d3-ab1c-4f48f395d8ad | -2.69664 | -45.11165 | 2025-11-22 03:32:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34c3f814-ffcd-34c6-8e75-de01fdf42a5a | -3.46018 | -40.81986 | 2025-11-22 03:32:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f0205b6-20e5-3386-b1bb-a08bffa1a33a | -4.1455 | -43.69411 | 2025-11-22 03:32:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1d8710b5-60dd-360b-9b08-94806d3cf4b0 | -4.03918 | -42.51754 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| b20782e0-45ec-3a77-8d5c-d27c75200d95 | -4.0277 | -42.47214 | 2025-11-22 03:32:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bc817674-45d2-3b08-9739-6461d75ffe38 | -2.69789 | -45.10432 | 2025-11-22 03:32:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1027ecd-4d31-3d1f-8346-d49e93091788 | -3.26277 | -42.21376 | 2025-11-22 03:32:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cf8332f-bcb6-3bd9-ad1f-1fedf19ac440 | -3.26881 | -42.21468 | 2025-11-22 03:32:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b5c3f62-3eea-33b5-9779-7bc9e1182d6a | -2.69844 | -45.1094 | 2025-11-22 03:32:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9294eb9-7861-3111-bcf8-2982298916f9 | -3.62068 | -41.99425 | 2025-11-22 03:32:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6be099bd-9996-314a-aea6-1fdf2c3482ef | -4.03291 | -42.5151 | 2025-11-22 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 01c4b830-65c0-384d-be9e-9d8874eb17d2 | -3.26354 | -42.20926 | 2025-11-22 03:32:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7c8a882-1e6f-32f7-b6a0-993572d99197 | -4.03314 | -42.51644 | 2025-11-22 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 5b835aff-fe08-3351-ab60-f812b469c607 | -3.46076 | -40.81636 | 2025-11-22 03:32:00 | NPP-375D | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8866b7d9-e5d0-3cef-bf69-7cefc571d94e | -3.61995 | -41.99853 | 2025-11-22 03:32:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e92b201b-2dbe-3ab0-b35f-2484a2da202c | -4.03233 | -42.52103 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 7d1b09ae-f403-34d7-b052-a5df10fbf1a6 | -4.03676 | -42.53139 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7cbc5a61-27de-3cc4-abaf-0715639e9241 | -4.04525 | -42.51857 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 82c15df9-c377-30b2-83a4-9918a49dafbb | -4.03757 | -42.52677 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 2cd8972d-e6a0-38c1-8efd-1e1342c75607 | -4.03214 | -42.51971 | 2025-11-22 03:32:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8395e1cd-5137-3af2-901f-507860970c8a | -4.02692 | -42.47672 | 2025-11-22 03:32:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cd126eb9-15ef-3847-b1e9-ffa53b726a08 | -5.50802 | -35.50244 | 2025-11-22 03:32:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 58ab96aa-ea78-335e-a9cb-cd430d955f30 | -4.03999 | -42.51295 | 2025-11-22 03:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8bbe6ef6-04a1-3d02-b448-360a96071d7e | -3.82194 | -41.1169 | 2025-11-22 03:32:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8fa988ae-c7a4-31dc-8125-36a11a90440c | -5.221 | -37.50095 | 2025-11-22 03:32:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3701dbbd-241b-3631-88cf-c0593eab6a8a | -5.1127 | -40.73294 | 2025-11-22 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 615d2ac2-04b3-3a21-9dbc-4a51fdf7b268 | -5.43012 | -40.66569 | 2025-11-22 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 525018da-3c7d-3c1b-9f47-9fccd931d978 | -9.97244 | -36.04726 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| fd5b3143-050c-33d0-b265-e8b55aea687f | -7.28372 | -38.91428 | 2025-11-22 03:34:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d49fe57-e846-3a51-8bce-54fb656d6b0f | -9.96446 | -36.05036 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 877dc905-5e1a-3601-8666-8474be0ed46f | -5.9392 | -39.23569 | 2025-11-22 03:34:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1977c678-50ec-333b-b143-0be01ba7a66e | -6.35276 | -39.84797 | 2025-11-22 03:34:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| da7ea81d-ca90-3471-ba41-67ce28a304b2 | -10.28814 | -36.32469 | 2025-11-22 03:34:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3d335c89-e632-3c59-853b-40b0ccc6371a | -9.97033 | -36.05999 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dabea6d0-0eeb-3c54-bb70-febe4cb38882 | -9.97467 | -36.05636 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e0a8e78a-fd45-3710-be96-846224c9a646 | -5.42956 | -40.66886 | 2025-11-22 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be6a5ee5-d588-3e5f-82da-4bb1f338159e | -9.97174 | -36.05149 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 17d84618-c304-33f2-b1c4-0578a093174f | -8.85118 | -35.15839 | 2025-11-22 03:34:00 | NPP-375D | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b915a428-a70a-367b-8e5b-e096605457f7 | -6.67727 | -39.50295 | 2025-11-22 03:34:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b0671c9-7c9e-365e-81e1-02fb212c5682 | -9.12435 | -35.75746 | 2025-11-22 03:34:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| af2ff542-268c-3c39-9e54-19e684607977 | -5.11328 | -40.72966 | 2025-11-22 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c72618a-c563-3c4c-83bd-c4e9de75d9e9 | -6.77926 | -39.11552 | 2025-11-22 03:34:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fbdd89cd-ac26-33a2-9c47-6ad60efa1695 | -8.2072 | -35.25462 | 2025-11-22 03:34:00 | NPP-375D | CABO DE SANTO AGOSTINHO | PERNAMBUCO | Brasil | 2602902 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8605d479-5d5c-3964-99e2-9329bd9edd76 | -9.97104 | -36.05573 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 542c2655-5e2f-310c-b940-4fd028ff0c38 | -5.43068 | -40.66252 | 2025-11-22 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e54ca4f9-015e-31d9-af12-eb910cbf19a9 | -9.97537 | -36.05213 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| be2c9a8b-b02f-33b9-a0e0-aceb0df73ad9 | -9.9688 | -36.04668 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| c06f44d4-57cd-3b52-b125-436f335cce17 | -9.97397 | -36.0606 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| ef39cad9-e4d2-3cd4-b6b7-6f8b79c978a1 | -6.35761 | -39.84906 | 2025-11-22 03:34:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81548801-f0f0-3e9d-9a2e-c4bc6a5bc189 | -9.96376 | -36.0546 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c2e6eb5f-73d0-309e-a7e5-c87c264a7dc9 | -5.93834 | -39.2407 | 2025-11-22 03:34:00 | NPP-375D | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a6799beb-b9ec-3739-9375-7b7949fb5f39 | -9.97525 | -36.05486 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6a6bd835-5ef0-3c4a-b7aa-46c6c7a83df2 | -5.1074 | -40.73203 | 2025-11-22 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eb919cf5-83ff-378c-a4d7-88872f9c2baf | -9.97597 | -36.05063 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6b8ff49d-8e41-356b-a96e-5516440e3d67 | -6.73187 | -39.04157 | 2025-11-22 03:34:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7cff95ce-b4f9-3609-bed3-17caf2322785 | -7.28822 | -38.91519 | 2025-11-22 03:34:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fba1a6f9-ba73-3b00-b7a8-25fc4d5da836 | -5.5695 | -39.83961 | 2025-11-22 03:34:00 | NPP-375D | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 017fd747-0c81-38ad-9d18-6d925af5cea8 | -9.12074 | -35.75684 | 2025-11-22 03:34:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ae840a8e-1c95-3e79-b338-1682a4401581 | -9.97452 | -36.05909 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d25822f2-27e9-31d1-aadf-436e1ab30ad1 | -9.9681 | -36.05092 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| efadeee2-dcd3-369f-908c-53a0842d13ab | -6.84968 | -38.79153 | 2025-11-22 03:34:00 | NPP-375D | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ee94b095-ec9d-3144-bda3-37132f47b9cc | -6.30821 | -39.59667 | 2025-11-22 03:34:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 83dad592-bec8-3a67-af36-28761ec3455f | -9.9674 | -36.05517 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d91863ab-9de9-3bef-b950-6315e68222c7 | -9.12143 | -35.75265 | 2025-11-22 03:34:00 | NPP-375D | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a8a9b3da-9717-347c-9e98-0c1aba2e5bac | -9.96669 | -36.05944 | 2025-11-22 03:34:00 | NPP-375D | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 133ef53b-0e32-3783-af83-f86b7dba3256 | -17.07607 | -46.59845 | 2025-11-22 03:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00e4967b-4cc1-3354-ab2f-662f935ebe11 | -16.46621 | -46.42719 | 2025-11-22 03:36:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eaa8423-d107-35bc-b3a5-ab924843f994 | -16.46509 | -46.43223 | 2025-11-22 03:36:00 | NPP-375D | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ba10f90-3cc2-34b2-a62c-aa8c0a63746d | -17.5228 | -39.69234 | 2025-11-22 03:36:00 | NPP-375D | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fc90378c-ce26-3e10-802a-46f2155349db | -17.0699 | -46.59694 | 2025-11-22 03:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68720bd1-873f-377e-a120-484d20f32db2 | -17.07138 | -46.60099 | 2025-11-22 03:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 788c29ed-823b-3fcd-807d-37ff45c881ec | -17.07248 | -46.5959 | 2025-11-22 03:36:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0f0d470-b8ce-3674-9acd-56c1dde3e045 | -18.68062 | -40.6325 | 2025-11-22 03:36:00 | NPP-375D | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e647ab75-097e-39ed-843e-28e4747e1154 | -17.68323 | -42.18319 | 2025-11-22 03:36:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 31bbfce2-ef39-3b6a-a981-41e7e3c366da | -23.23558 | -51.28429 | 2025-11-22 03:38:00 | NPP-375D | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7fc5dd6e-05d3-362f-8fc8-834f605302a2 | -24.36964 | -49.18595 | 2025-11-22 03:38:00 | NPP-375D | BOM SUCESSO DE ITARARÉ | SÃO PAULO | Brasil | 3507159 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 45e12ff5-f61b-3a98-8459-c7042fea9333 | -20.65821 | -43.44491 | 2025-11-22 03:38:00 | NPP-375D | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README3.md)
