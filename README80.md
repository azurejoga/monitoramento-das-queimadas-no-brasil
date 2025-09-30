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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d217e97d-49c1-3e00-bb85-54caf4e32c2d | -15.60319 | -46.25436 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4af5ca4e-abb9-3c52-84ce-5d5413b51928 | -17.73401 | -46.67177 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e490d8bf-0387-3022-bf7b-1761a23c7ab7 | -14.55439 | -48.25782 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd25c7d1-9b91-397f-8edc-1dd6ee1f5ca9 | -19.33044 | -43.81528 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9572fd5b-03e5-3c08-be97-c7f30dc7d2d8 | -14.71321 | -48.25328 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8591ed1-27a3-358d-8ed8-20dc192d6355 | -14.64765 | -46.96017 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a6027d3-2677-3b97-81fe-6b30d7942edc | -17.0965 | -48.56752 | 2025-09-30 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 016cb6e8-7499-3498-a1cc-38dbccfd3f93 | -19.86446 | -44.55759 | 2025-09-30 04:42:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| aebb6e3d-2227-3a37-84a8-978e1441fbf9 | -15.27815 | -49.27163 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd58fec4-bad0-3acd-80f7-a31ca729648f | -15.17088 | -46.42003 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bc66eba-127a-3669-bca3-2e1365f2b53d | -16.49876 | -46.04083 | 2025-09-30 04:42:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dea20cd1-6494-304a-b1db-9c5a452413c1 | -14.57072 | -48.22091 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf050794-aca1-365f-8338-82a61e69d3dd | -15.25038 | -48.74502 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a45c6dd-7fe6-3121-b054-f058f9e7d4cc | -15.20902 | -50.09506 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bdb20da-ea3d-39af-94d2-36a2df04911e | -14.58378 | -48.22071 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 807e4b6f-28c7-32dd-b229-b864174df233 | -20.6145 | -46.06854 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d3ec8c50-96d5-359a-a72a-da6e2d887dd5 | -20.99955 | -50.01176 | 2025-09-30 04:44:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 00342c01-0907-3a77-bcdb-cea065e94efd | -21.44569 | -50.54187 | 2025-09-30 04:44:00 | NOAA-21 | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0f320553-6736-3757-b11f-f8650b592d93 | -21.7407 | -44.61539 | 2025-09-30 04:44:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 707de094-cf0d-3f3f-9c0b-02a135086149 | -20.5988 | -51.61025 | 2025-09-30 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d67f750-59e8-3ba3-b08a-9d1c1569de26 | -22.63199 | -49.04322 | 2025-09-30 04:44:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b9f8500-51a5-3c4e-9858-41b18f689bae | -22.3359 | -49.48396 | 2025-09-30 04:44:00 | NOAA-21 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6089f837-3cca-3c6a-aa81-62ec43b88e7f | -21.33732 | -46.7261 | 2025-09-30 04:44:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39e53802-033a-3b40-ada0-430b61dfac1b | -22.173 | -46.73969 | 2025-09-30 04:44:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 00210b39-1958-3c95-8b25-a5b241fd2c16 | -22.51874 | -44.59949 | 2025-09-30 04:44:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3f4cdc76-bbb0-36db-ad67-18257a9a75e1 | -22.51259 | -44.61018 | 2025-09-30 04:44:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 88b224f0-a3be-3b1b-91cc-156844440827 | -22.84752 | -45.4463 | 2025-09-30 04:44:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7639644-78c8-3e00-a025-22d92f3bca9f | -23.52957 | -47.07306 | 2025-09-30 04:44:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ffd6624-1c2a-3699-b6f8-a606abf262fc | -21.0891 | -45.33814 | 2025-09-30 04:44:00 | NOAA-21 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7b363c5d-97e6-3cd5-a2dd-c332136aef83 | -21.72911 | -45.27205 | 2025-09-30 04:44:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e936e322-161e-3562-a2be-55890de00b23 | -21.22836 | -47.13505 | 2025-09-30 04:44:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f90fafd3-9bef-350c-886d-6a3baf63b4b7 | -21.89343 | -45.75638 | 2025-09-30 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e02d5d1c-d483-3e13-a9b0-e0bed2371e74 | -22.09943 | -47.80585 | 2025-09-30 04:44:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bb4cb62-7f3c-39cd-9cc1-582293cfdc68 | -21.89367 | -45.75232 | 2025-09-30 04:44:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3d1bc55-5522-3ff0-8617-e2e396b41a06 | -22.389 | -50.03627 | 2025-09-30 04:44:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 36d8a10a-4eea-3725-bcec-db680a23d8d3 | -22.08705 | -55.97016 | 2025-09-30 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93d4e354-5ffe-3206-ae5e-e298233e1545 | -22.62822 | -49.04254 | 2025-09-30 04:44:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21ac0430-285a-3f4c-a178-c86d80376b6d | -22.33282 | -49.47887 | 2025-09-30 04:44:00 | NOAA-21 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 777466bf-1fdc-3b5a-87f5-ddb48a50155c | -22.38542 | -50.03562 | 2025-09-30 04:44:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cc159203-c84b-3408-a75f-7c8ec524e311 | -21.31665 | -46.75354 | 2025-09-30 04:44:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 2b2fd746-2d57-339c-9ae2-abf3fb3cabbe | -23.23257 | -46.77818 | 2025-09-30 04:44:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8b7b59ac-94e8-3641-86e7-cefa3f8f3de2 | -24.40833 | -50.68076 | 2025-09-30 04:44:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1cd83490-478a-3b05-a3f3-e1917e701a81 | -21.22418 | -47.13454 | 2025-09-30 04:44:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e38a7e6e-6e61-3b5c-a2cb-34db5345e5c7 | -21.0443 | -45.68653 | 2025-09-30 04:44:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c84d5ec-3243-3ce1-9e09-793296b7ac77 | -21.6256 | -44.05849 | 2025-09-30 04:44:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5843d1a6-6f18-310e-bb89-5abdcbcc1981 | -23.16233 | -45.72495 | 2025-09-30 04:44:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6dbaf47b-7493-308f-be9e-fbec018fbb29 | -21.00309 | -50.01231 | 2025-09-30 04:44:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b4337b61-aedc-3a3e-aa89-883f9b9386a2 | -23.19943 | -50.94388 | 2025-09-30 04:44:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 213e8896-a628-3b15-99e5-19bb0ff774d9 | -22.52306 | -44.60675 | 2025-09-30 04:44:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 5f7eec2c-c851-3784-8517-5a4bd3743adc | -23.32968 | -46.86739 | 2025-09-30 04:44:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1878c2de-aca3-3252-9f19-976297d1a310 | -23.88934 | -50.80706 | 2025-09-30 04:44:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13599c17-64d3-30ab-a455-4850d9da076a | -21.46941 | -46.702 | 2025-09-30 04:44:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8a498bac-8985-311c-b2df-a722534d0707 | -21.04503 | -45.68419 | 2025-09-30 04:44:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c9246f38-9e19-3c73-96ee-bd94b887bfca | -22.62571 | -49.03207 | 2025-09-30 04:44:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17622568-f970-3fb1-bb14-6ce027aa588b | -22.3365 | -49.47942 | 2025-09-30 04:44:00 | NOAA-21 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4334d57c-8987-324d-b31c-f677b0acf977 | -22.09402 | -55.97167 | 2025-09-30 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 94e50227-55bf-3dc4-98e2-fa5043ae8f58 | -21.38951 | -43.71737 | 2025-09-30 04:44:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 0126384d-4c5f-332d-89cd-a43af95afa86 | -21.22883 | -47.13112 | 2025-09-30 04:44:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 474851ea-f033-3e78-9764-51e662c6fdf0 | -21.22466 | -47.13056 | 2025-09-30 04:44:00 | NOAA-21 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 56281afe-1cb2-3dfc-9769-1496ab9b597f | -21.62016 | -44.06104 | 2025-09-30 04:44:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1114baea-e8ec-3bcd-93b1-63470f60e251 | -23.50114 | -47.43003 | 2025-09-30 04:44:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b1ffef9b-1e59-32d8-9c30-11c4251ec20d | -21.0944 | -45.33317 | 2025-09-30 04:44:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 591105c3-56a0-3479-aa60-124c2bb9e8af | -23.20291 | -50.94447 | 2025-09-30 04:44:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 55a26c0a-4b6f-3970-88b9-3e6bd9532020 | -22.09054 | -55.97091 | 2025-09-30 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fd378075-808d-3cfb-937b-d6254b3b5bf0 | -23.15709 | -45.72961 | 2025-09-30 04:44:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 252fa090-ab81-3d26-bc06-e46eb49db27f | -22.37222 | -49.97022 | 2025-09-30 04:44:00 | NOAA-21 | OCAUÇU | SÃO PAULO | Brasil | 3533700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c5e471fc-8ded-3c27-8a9a-51fc419a10ab | -21.47189 | -46.70427 | 2025-09-30 04:44:00 | NOAA-21 | CACONDE | SÃO PAULO | Brasil | 3508702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6ba23076-b0e6-36cd-b9b6-4ec0e2f41a92 | -23.88871 | -50.81175 | 2025-09-30 04:44:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5f9220ca-dffa-3c80-a0e0-ed7a0b9d78f1 | -21.04451 | -45.68898 | 2025-09-30 04:44:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c03847b0-563a-3f2a-9609-c5ea0b5bc983 | -20.99601 | -50.01122 | 2025-09-30 04:44:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b70f399-5b1a-3a79-916c-252ea9afc333 | -21.93468 | -42.79488 | 2025-09-30 04:44:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e17b1d3b-ff03-30b6-9a20-49db3272a5c4 | -21.3843 | -43.71679 | 2025-09-30 04:44:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| af173c5f-706e-3260-8c2c-009f49ec6411 | -23.15241 | -45.72899 | 2025-09-30 04:44:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 53f5f613-08d5-3ef3-bc51-ec5f60b36a59 | -21.93434 | -42.79858 | 2025-09-30 04:44:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6b4c7fa4-a7d0-3a07-8a31-d59d450bc104 | -21.15965 | -43.61659 | 2025-09-30 04:44:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec269fb2-4675-3301-83bb-3d473231af4c | -21.40828 | -43.89756 | 2025-09-30 04:44:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b1666df-4934-3010-8063-f248ababf5ed | -22.09327 | -55.97592 | 2025-09-30 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7622579-b5ca-3e84-8e03-b86bb5b12da0 | -21.89829 | -49.58094 | 2025-09-30 04:44:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b445047d-2b8f-3dd1-bef0-6cbb7d92df23 | -20.91189 | -46.39567 | 2025-09-30 04:44:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1ad6c7bc-2602-3e43-bd19-ec10847be19f | -21.09203 | -45.33528 | 2025-09-30 04:44:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0fce94fc-6b3f-389e-a2b4-79276ce5183d | -21.61507 | -44.06027 | 2025-09-30 04:44:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 859f7912-1cfd-34b3-bdcc-3f97f162e7a1 | -20.99582 | -47.02117 | 2025-09-30 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b2b126b-50ee-3581-a221-27441d90aaf0 | -23.15765 | -45.72438 | 2025-09-30 04:44:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| dd6de4e0-f4e3-39a4-9bec-b45da835b06f | -23.23206 | -46.78265 | 2025-09-30 04:44:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f61394be-45aa-33fb-bbe0-633e8c3e559d | -21.09035 | -49.82214 | 2025-09-30 04:44:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9e092bc9-6154-365f-8373-d36ff921d12c | -22.31023 | -49.59399 | 2025-09-30 04:44:00 | NOAA-21 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 944bfe5f-42a0-31b4-8e61-ac74e0fea2db | -21.04485 | -45.68176 | 2025-09-30 04:44:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0befae34-2c3f-3740-b866-07a5dca0a061 | -21.25916 | -43.85344 | 2025-09-30 04:44:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5849060e-99eb-3a7b-893c-defe63c83b84 | -21.31863 | -42.87645 | 2025-09-30 04:44:00 | NOAA-21 | ASTOLFO DUTRA | MINAS GERAIS | Brasil | 3104601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 00672bb6-ab63-3cb2-aabf-186debbdc672 | -22.35615 | -49.47294 | 2025-09-30 04:44:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 145ce3e7-1f97-35c1-ab61-dc9a54448d15 | -21.32041 | -46.7584 | 2025-09-30 04:44:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc094d01-839e-3d5e-b197-e4dd5dc48dfc | -21.33681 | -46.73033 | 2025-09-30 04:44:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 046231cc-510c-3669-9768-9346b494ffbf | -22.76398 | -45.78784 | 2025-09-30 04:44:00 | NOAA-21 | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3590bba9-f0ad-31db-8667-0986f1be503f | -22.38185 | -50.03498 | 2025-09-30 04:44:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 41bfea0f-f46d-3537-97a9-9583431c4d29 | -21.09147 | -45.3405 | 2025-09-30 04:44:00 | NOAA-21 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7c15f073-58a9-37e3-b756-2e88a7fabf0c | -22.52246 | -44.61259 | 2025-09-30 04:44:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 3d580540-81a1-3516-94b6-ebeec8d4eaa7 | -21.08969 | -45.33296 | 2025-09-30 04:44:00 | NOAA-21 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3e364501-ed2d-3015-adf8-c26aa1ebb19e | -20.99691 | -47.02338 | 2025-09-30 04:44:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2bea79b-ba01-3ecb-929b-8f9ef5661c10 | -23.56407 | -47.55606 | 2025-09-30 04:44:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1f3c6097-6473-3993-8bde-ac33bb0a17bd | -22.79636 | -50.19704 | 2025-09-30 04:44:00 | NOAA-21 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README81.md)
