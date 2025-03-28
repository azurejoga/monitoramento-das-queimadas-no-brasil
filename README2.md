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
| 9d067e8d-69f0-3879-bcbd-d1d74efa36ec | -8.11267 | -43.12753 | 2025-03-28 03:34:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e65b82c7-c964-3eef-b09c-ae6fc37fa025 | -12.45156 | -41.46332 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 90ad3954-4bca-324c-8175-d81305432512 | -9.71508 | -37.83918 | 2025-03-28 03:34:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 347cf8da-0820-32e5-b79c-dac2dabae9fc | -12.46458 | -41.46022 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 23.9 |
| e6fc111b-644c-3190-9333-cbbce73ca154 | -10.99895 | -40.4824 | 2025-03-28 03:34:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5a0d8317-b2aa-3231-9c8a-188f3557613b | -12.45767 | -41.4547 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5fbd31d8-ebad-3cd5-b9db-973ce8092c68 | -12.44968 | -41.46631 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 01d55bfa-f565-335e-99f0-d76e6e01b971 | -12.46895 | -41.46136 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4444568c-090d-3710-bd55-7b76300faef6 | -12.45519 | -41.46869 | 2025-03-28 03:34:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e309920d-9677-3e7c-8951-0e3b4d0374a9 | -11.06185 | -38.43724 | 2025-03-28 03:34:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29968278-2939-35e8-8301-74abe1c41e63 | -5.22054 | -43.51959 | 2025-03-28 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5380ca2-2972-3dba-886b-ce262d4b9f2e | -12.76678 | -45.40818 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9ec6fc2-725c-3f71-a4e3-cff903555e14 | -12.79912 | -44.97057 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3525df0e-3282-3d18-b600-362f2323356f | -12.79206 | -44.97704 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b653022-cbb6-306e-b86b-18358bd62a61 | -12.75809 | -45.4151 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e30c4768-5324-3ecb-b339-ca0c40ed1768 | -12.7995 | -41.51173 | 2025-03-28 03:36:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c0294029-40a6-3770-ab14-c43a2184cbaa | -12.76594 | -45.41228 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c051b324-6f97-3273-bb55-100b5c2365fd | -12.75237 | -45.41395 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18f3f485-b994-3cdb-aa98-8e2029fd70d9 | -12.7589 | -45.41095 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7022a126-ed8c-3fac-aac7-9e719c1c15d0 | -12.77112 | -45.40918 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86276618-ebc1-36b4-9fe2-ceb9e8e15233 | -12.79282 | -44.97324 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| baf53efd-9969-3ac5-bb6d-4ea27148db4a | -12.76461 | -45.41211 | 2025-03-28 03:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e404b9d-90f1-3c4d-919d-170e0465c2d4 | -13.37884 | -40.67641 | 2025-03-28 03:36:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b98aa33e-0d6b-3da9-8d36-ff8a42e021d3 | -20.65657 | -48.45232 | 2025-03-28 03:38:00 | NOAA-20 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| acd1af3b-5b47-3b54-abc6-3af73ebbc7cc | -21.64129 | -48.65118 | 2025-03-28 03:38:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47c37c5e-9d1e-3c72-bf07-e85fc4118118 | -19.60405 | -40.62697 | 2025-03-28 03:38:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b0f98986-3994-39ac-b8eb-c17aa8d676b4 | -22.78649 | -43.75873 | 2025-03-28 03:38:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e2f0fe24-ea19-3bcd-ada6-0fe2620a6969 | -21.64234 | -48.64658 | 2025-03-28 03:38:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b858cab-fbfe-3418-8258-3478a0d75994 | -20.65554 | -48.4568 | 2025-03-28 03:38:00 | NOAA-20 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b4077e2b-d0e4-30ae-81b6-4fbe268ebb9c | -20.13587 | -50.72426 | 2025-03-28 03:38:00 | NOAA-20 | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9a5bcf94-2b32-3536-8af5-61f9a54821e8 | -21.64531 | -48.65081 | 2025-03-28 03:38:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be5bec06-b131-3fd6-8f11-220caa45103c | -12.4697 | -41.4541 | 2025-03-28 03:40:00 | GOES-16 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 1bfc0d78-072d-3d50-9052-4d0e63c401ae | -6.25131 | -43.78046 | 2025-03-28 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67644de2-25fa-3931-9c45-0c3ae13c73b3 | -4.81445 | -42.9876 | 2025-03-28 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b55bc67a-50bc-3b76-a7c2-f6dc6c5a93e2 | -8.89014 | -44.78122 | 2025-03-28 04:25:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07865b05-ada8-397c-a7c2-0e097cff7bb1 | -5.22288 | -43.5164 | 2025-03-28 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82430c03-94e9-3bb6-b639-1498e4bbe3d1 | -8.11376 | -43.12687 | 2025-03-28 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b0318ac0-18b5-3458-9b4e-fc072909827c | -5.92591 | -45.53656 | 2025-03-28 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 792651b4-9866-3df8-ac2d-4ab7406435f5 | -5.22928 | -43.52135 | 2025-03-28 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bea5193c-aa91-30f5-8ee2-e872461d102a | -4.67567 | -43.25393 | 2025-03-28 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87d4fe99-95ed-3108-911e-e3efc33152e9 | -6.51549 | -43.63468 | 2025-03-28 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b01f2437-ea9e-372f-b1fb-fbaa08137ab0 | -5.22987 | -43.51747 | 2025-03-28 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fc6c8ea-5065-393c-9bc3-b0d28e9f579d | -5.21938 | -43.51586 | 2025-03-28 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cd98bc3-4e77-3755-9acc-70b11796d7e8 | -9.7167 | -37.8385 | 2025-03-28 04:25:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e06fbf3-2446-3dea-9e03-db27ee471aa1 | -5.67671 | -45.21529 | 2025-03-28 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba0e1ec1-a27b-3046-917c-95be81553f6d | -3.94316 | -47.98512 | 2025-03-28 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34471e09-67af-3f4e-ad9d-ca12a21d4eb8 | -5.67725 | -45.21179 | 2025-03-28 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3c45c95-cabf-3430-88d8-0e6313f87375 | -9.97903 | -37.91249 | 2025-03-28 04:25:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f510fa6d-12f7-3895-a3f7-5734497d34eb | -9.71092 | -37.8412 | 2025-03-28 04:25:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b0de3ce9-ee43-3248-9212-7b41efee0c2f | -8.11744 | -43.12742 | 2025-03-28 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ff22d76b-725c-3987-895a-2517f4360ea7 | -10.53974 | -44.67038 | 2025-03-28 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06333ccb-9d23-32ad-a393-dfc52b58697f | -16.68134 | -43.88315 | 2025-03-28 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76c2ac7a-ee07-33c4-ad28-fc568eb4de47 | -12.46205 | -41.46704 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 88cea962-1dd7-3f40-a907-4dc3bd90f3f7 | -12.77142 | -45.40977 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91e8973a-a7ae-30e7-9fae-7ac442ce0f17 | -12.76391 | -45.41258 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98600249-ec60-3946-9709-1cb8894247a7 | -16.55374 | -46.72974 | 2025-03-28 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81676a9f-cb44-3326-85b2-1bc126b21d88 | -10.54384 | -44.66695 | 2025-03-28 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03e133ca-5e2e-300e-bde2-4e21d7f72cc4 | -16.2859 | -39.2538 | 2025-03-28 04:27:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4dac4c64-9b79-3ba0-8f4e-efe7cc1bd931 | -12.46263 | -41.46272 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| fb5ed365-8a99-3be4-b14e-343d6befb7ea | -16.2863 | -39.25028 | 2025-03-28 04:27:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a7770051-44d3-3ae9-9772-58545285fd33 | -15.57092 | -47.85507 | 2025-03-28 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc802a72-a0f5-3069-8876-19b2c1bf52b8 | -15.85924 | -54.13142 | 2025-03-28 04:27:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0b04e06-cf44-349c-88df-654b28747ef6 | -12.76795 | -45.40923 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fffbc339-1c17-30c0-ae3e-028df6756b9e | -10.36346 | -44.83652 | 2025-03-28 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b24be35b-8c57-3846-945b-471fa2ad3276 | -12.7989 | -44.97491 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4dd129c-e80e-372e-946f-5449d9afde2c | -12.45334 | -41.46621 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 21.2 |
| a3ad848d-81b5-3498-803e-d77afe04d8d4 | -12.45929 | -41.45465 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 922146a2-e6b7-3ce1-8c1e-d771ecd36271 | -12.46147 | -41.47147 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 02d477b5-c093-375d-bf53-0e7cb35ab976 | -12.45389 | -41.46204 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 3b186253-686b-3cb8-b7f7-c8693d714c5b | -12.79536 | -44.97436 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f83c6e34-b251-385f-a4d8-d067c9a1f532 | -12.45878 | -41.45852 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c2f1cfb3-7aaf-34e3-8cec-3c5ac8965796 | -17.6776 | -42.74451 | 2025-03-28 04:27:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 678fac4e-ea67-3c8f-a99a-5f28c21c3672 | -12.7564 | -45.41537 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0361f1a7-c8f8-32ba-b70c-d30244bc3fab | -15.94959 | -52.3183 | 2025-03-28 04:27:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c89ef088-93ec-36f2-abb7-fa79209460d1 | -12.45769 | -41.46667 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 7f090b59-103f-311d-a5a1-2c5eaa53ecc3 | -12.79948 | -44.97085 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7f8a033-dca4-3da9-8ea3-347acdf35a88 | -12.75697 | -45.41149 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e43fc53-0080-3ab8-a8d9-97fe388e1c1a | -15.8569 | -54.13168 | 2025-03-28 04:27:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 741347b7-0ca1-386b-a5c8-82b4236dc7a0 | -12.79628 | -45.38565 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d175d4c-77f6-3bd0-b682-9cd5df7c7467 | -10.35999 | -44.83598 | 2025-03-28 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be7e7c8a-6cf4-31a1-b140-b86fa66f766d | -15.0807 | -48.94552 | 2025-03-28 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3a717fc-565d-324c-8696-005239a82b8b | -10.36289 | -44.84039 | 2025-03-28 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a20cb88-7844-3f0f-85ec-ec2865f41c5e | -12.76044 | -45.41204 | 2025-03-28 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6e341cc-e498-3f96-bfc7-9703197d85f3 | -12.45826 | -41.46237 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f985b94f-b72d-3682-97af-d6172f6802d6 | -12.45441 | -41.45818 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 6bb472fa-6348-31a7-bb7e-066bc2f2b28e | -11.9757 | -40.29402 | 2025-03-28 04:27:00 | NOAA-21 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd1d7693-01eb-3ff5-bd7c-d1130ef23b91 | -12.80129 | -41.51101 | 2025-03-28 04:27:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 602a00a4-a225-3d6e-848e-116183f0068b | -12.46315 | -41.45884 | 2025-03-28 04:27:00 | NOAA-21 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 672f3340-24bf-3bad-80b0-39bf0cc494f5 | -22.36139 | -47.05236 | 2025-03-28 04:29:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca215b7c-8d7f-3bd3-a058-64e7dd52c916 | -20.65807 | -48.45639 | 2025-03-28 04:29:00 | NOAA-21 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c58f31eb-6066-331f-aa25-e2da694f5d6d | -20.66142 | -48.45694 | 2025-03-28 04:29:00 | NOAA-21 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38512fa6-226f-312b-bb5f-4243a432f7f2 | -21.64441 | -48.64973 | 2025-03-28 04:29:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f1740c73-03af-3a22-b330-513f13de37b1 | -18.33476 | -54.2705 | 2025-03-28 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03d68831-ace0-322c-ad7b-519dc1e6f914 | -18.82727 | -53.43455 | 2025-03-28 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c08315c9-a457-38d4-8782-d5fdeb889fb4 | -19.89265 | -48.35411 | 2025-03-28 04:29:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d441e9a-5249-3721-bede-b5e5b4b4cc3b | -20.61386 | -55.70677 | 2025-03-28 04:29:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5d4c966-e204-36d6-a385-8f2fa2cd68a8 | -20.61304 | -55.71097 | 2025-03-28 04:29:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f067365-1250-3d29-80db-af955630383b | -22.89581 | -49.24081 | 2025-03-28 04:29:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b077a49d-02b1-381a-af0a-1c932ce983d1 | -19.89209 | -48.35783 | 2025-03-28 04:29:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8348be0d-df77-3120-aad5-aafec88e13be | -18.83109 | -53.43345 | 2025-03-28 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
