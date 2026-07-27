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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70ddda62-8959-392c-a456-d8dbc8ef8cb0 | -11.89176 | -43.83161 | 2026-07-27 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 546fb644-3d15-3a7d-9114-873e1366eed6 | -17.40949 | -46.42212 | 2026-07-27 04:51:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc92701b-e36b-3635-bd0d-46055639c5cc | -11.49504 | -50.15892 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da764f00-ab96-3a7c-8f6b-dc01b8309fc3 | -11.49838 | -50.15945 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aa8a2df-27a3-30c1-900b-640a8fa39664 | -10.53638 | -48.62006 | 2026-07-27 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ae1c1cd-c4fb-3349-b8fd-6b193dc8e786 | -12.32927 | -47.1738 | 2026-07-27 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4b3426b-3c8a-3743-993b-d8f8baf1dfcb | -11.48613 | -47.53086 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77176ce2-2aef-3c75-9df9-1be19d2095b0 | -11.84481 | -50.22681 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bcd8c40-562d-321a-82e2-f9cc6890dbeb | -14.39108 | -58.87666 | 2026-07-27 04:51:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 573a6b4a-fdf2-3626-98e9-79848ada4e9d | -11.98872 | -45.56384 | 2026-07-27 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4882425-976f-3d19-9bdb-2be70146ce3d | -13.7008 | -51.88712 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e6b7c6b-791e-3d55-aca2-d3db584ceb1d | -12.30979 | -50.35845 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9bae00c-09f7-33af-be6d-72b123cee150 | -12.32035 | -50.37837 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 818542df-94a1-3ef5-a921-18e0754b0c83 | -11.46368 | -47.55719 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fbcacb3b-d18e-396f-8dc8-4d473fc6262c | -13.70022 | -51.89068 | 2026-07-27 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 677dcb8d-2b03-39c0-a96c-eda5ca887a3d | -11.49449 | -50.16246 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7762cf3-9908-3064-8d29-53c16b96ff64 | -10.54097 | -48.613 | 2026-07-27 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3794813a-cf6c-33a5-b730-e9dd82b3f0ee | -11.47942 | -47.55117 | 2026-07-27 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52bc73ae-0f13-354c-8ba1-da0a55a46220 | -10.53752 | -48.61251 | 2026-07-27 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e7519365-4fb8-364b-8dba-550dfed2302a | -10.83398 | -49.38929 | 2026-07-27 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dca31333-d74c-35e9-9a4b-fd1cbf3c695d | -12.32286 | -47.18946 | 2026-07-27 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98278cf2-facf-39dd-9ec7-bc4a66b4f730 | -14.23689 | -54.56418 | 2026-07-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1be4790-f717-3545-a1cc-60b2146ed2f9 | -12.29425 | -50.37051 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 385ea151-1c90-3d20-802a-e528e0f4c693 | -11.50893 | -50.17931 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bfc5b84-f9ab-30d8-b1b7-fde5654965a5 | -11.15379 | -51.20109 | 2026-07-27 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37818c66-99c9-3a93-86dd-714e83f3fc1f | -12.29758 | -50.37105 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c217f09b-8598-3ef3-b5d4-0db11010c66e | -11.50505 | -50.18232 | 2026-07-27 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce23087b-f4b8-3314-9baa-a133f9229e7a | -14.2412 | -54.56068 | 2026-07-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab757a1a-c9eb-3306-827c-062abd97775f | -9.47697 | -63.37584 | 2026-07-27 04:51:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d33576a-ce02-3b96-a221-e1149633b040 | -17.16307 | -46.83269 | 2026-07-27 04:51:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 824071de-7b30-3fef-bf64-e97e811e8abf | -11.98925 | -45.5601 | 2026-07-27 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 632b484f-774e-3356-bd74-95b204ccc215 | -14.36027 | -54.91344 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2ffbf1ac-6c2f-3d4b-80c8-04bf32e16e1b | -14.34933 | -54.93263 | 2026-07-27 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a13550fb-96d4-3a7f-970d-5bc2546de1db | -20.42091 | -48.62846 | 2026-07-27 04:53:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fccf2122-f035-324a-9691-5e667fe85faa | -20.41883 | -48.62544 | 2026-07-27 04:53:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b3c7993-3252-3b08-999c-7fd5217dd3dc | -20.06326 | -43.70063 | 2026-07-27 04:53:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e03c627-2358-3e88-8c70-9e43e22c5318 | -20.79152 | -57.9382 | 2026-07-27 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6e3444a1-c371-3c09-a6c8-5038ae2c92d4 | -20.56703 | -57.29021 | 2026-07-27 04:53:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 930b4c93-6a47-396b-a409-a49f7e14dced | -20.7876 | -57.93736 | 2026-07-27 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2a8cd3eb-b173-3bf7-8f8b-933824a99888 | -18.27026 | -50.34674 | 2026-07-27 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0736a17f-0e75-3db4-afad-296b545ef4c4 | -19.1048 | -44.34485 | 2026-07-27 04:53:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bb5ab62-d263-3ce1-b18d-7d410870c01d | -20.78659 | -57.94265 | 2026-07-27 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ef1c2526-ee75-35c4-a3d3-62f4ce409bd2 | -18.2674 | -50.34221 | 2026-07-27 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2f6b19ff-1205-3b3d-ad69-44983880d232 | -18.26682 | -50.3462 | 2026-07-27 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e0b8444a-c8dc-35d6-9572-4d6250c860d0 | -23.37561 | -46.93346 | 2026-07-27 04:53:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 80d0781a-1c86-387a-acf8-ef5398517fc1 | -18.27085 | -50.34277 | 2026-07-27 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e605f23a-b33b-3b56-8421-5ed358793855 | -23.37067 | -46.93746 | 2026-07-27 04:53:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a6a6ef86-56ca-39ce-bf93-410ae710388a | -19.11051 | -44.33873 | 2026-07-27 04:53:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59fe6585-a236-3303-800e-d36d83fb7575 | -18.26395 | -50.34166 | 2026-07-27 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8092766c-febf-33b6-bf5c-e9673566d807 | -18.26337 | -50.34564 | 2026-07-27 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e16bf2c4-9af6-3e3c-90b2-f4bc29b6c91a | -20.06352 | -43.69816 | 2026-07-27 04:53:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c94922d-2b70-326d-91c8-36eef9380314 | -19.10977 | -44.34515 | 2026-07-27 04:53:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4521f880-9235-3195-875a-3ae2a09c4339 | -10.9401 | -43.0355 | 2026-07-27 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| dd24208f-b8c1-3f9f-8114-116f91f3b0ff | -10.9397 | -43.0593 | 2026-07-27 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 237.3 |
| ea04cc04-1be2-3255-bfc4-2a0d66153bc0 | 2.81356 | -51.0653 | 2026-07-27 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ed03808-281f-3952-afe6-a4acfda4a8a3 | 2.81002 | -51.06587 | 2026-07-27 05:06:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19eedf37-7c41-3ea1-9696-8f54afe69738 | 1.681 | -60.13779 | 2026-07-27 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a88d5d3b-f76f-31ac-ac91-9f4d066296e5 | -3.21602 | -53.13662 | 2026-07-27 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d39357e-ac3a-3ce6-8ca2-9f6b285c0933 | -2.95141 | -50.32798 | 2026-07-27 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23c3aa84-c584-3be7-a45d-868879e4a4f0 | -2.80496 | -48.67132 | 2026-07-27 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cbb48fd-fcb9-379c-bc71-3ede13db3943 | -3.7272 | -48.87493 | 2026-07-27 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40668e0b-72f0-3a66-8c29-7197407b7f8f | -5.4223 | -43.42466 | 2026-07-27 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89ca1f6c-18ae-34cf-9d3a-2228f04910a7 | -1.54263 | -53.69651 | 2026-07-27 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 59d161dc-b6cb-3c37-9f3f-6127cb7790cd | -4.09852 | -50.4284 | 2026-07-27 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5df0c15-2642-3715-bc7e-9622bd801ea5 | 0.08125 | -51.09169 | 2026-07-27 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66fa4a24-05ac-33fd-a5f9-a2c603fffe59 | -2.76655 | -48.57346 | 2026-07-27 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2cfbf91-16c3-35e2-bcc2-f1e3a2efa968 | -3.25907 | -49.52613 | 2026-07-27 05:08:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf9e950c-d234-3727-9630-3d89dcd3653b | -1.39818 | -55.40361 | 2026-07-27 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78135dd1-7108-3bc1-aedf-bfb409f057f8 | -2.8094 | -48.67199 | 2026-07-27 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58212c41-d0e5-3351-b1ba-26c4ba619371 | -2.81006 | -48.66763 | 2026-07-27 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0226fa15-3d15-3658-be04-3c02dfae2ab4 | -3.21661 | -53.13286 | 2026-07-27 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2c1e51d-85cf-3b5c-a356-fba619054e9b | -3.92153 | -47.81799 | 2026-07-27 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07c4a96b-622a-3773-8cbc-69c32fcdf8bb | -3.95926 | -49.41827 | 2026-07-27 05:08:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f82b0040-a554-3307-af67-59bbe53102b6 | -2.85707 | -54.02004 | 2026-07-27 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cf1e3f6-6143-30e7-bd04-cface4878708 | -1.54654 | -53.69348 | 2026-07-27 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2a20ff18-dedf-33b4-9e62-212ce47cb5e5 | -4.09906 | -50.42488 | 2026-07-27 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bd7df30-25e8-34cc-a9eb-2fda89d47e55 | -2.95087 | -50.33141 | 2026-07-27 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1f31c6b-6359-3c68-ad85-f11ba883c8d9 | -2.80562 | -48.66695 | 2026-07-27 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acc87415-7a9b-3d35-9f21-f63c85caf8e1 | -1.54319 | -53.69297 | 2026-07-27 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 50348356-4ee6-3eff-9c6c-4003c0b38787 | -10.9588 | -43.0565 | 2026-07-27 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 4d0b4782-5a9a-3851-8e2e-2d58ed501165 | -10.9401 | -43.0355 | 2026-07-27 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| f1880682-1fab-30d6-9b4e-8fa176a659b6 | -10.5281 | -48.615 | 2026-07-27 05:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d032c630-bc17-3775-b39d-c26781524958 | -10.9205 | -43.0622 | 2026-07-27 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ccfc69c5-9029-3356-bfb4-977eee315b9a | -10.9397 | -43.0593 | 2026-07-27 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.4 |
| 6379b700-5a72-3ea9-8ac1-123825e0566c | -10.5471 | -48.6128 | 2026-07-27 05:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 65e8f961-93ca-34b3-b5ed-00fa7a5c752d | -9.47351 | -63.37147 | 2026-07-27 05:10:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0fc520c-2891-3b88-8bb4-39ef33ab1e32 | -7.16736 | -59.3111 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62a4b95b-fa77-3979-b475-7cae40bf483c | -12.32088 | -47.19466 | 2026-07-27 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8e760d44-dde3-3dbf-819b-e72b3789249b | -7.17458 | -59.31231 | 2026-07-27 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19171de1-6200-3f19-b9b2-e7788d7e5d72 | -10.94278 | -43.05372 | 2026-07-27 05:10:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 6b980368-8d09-3f13-bfda-ea08855c67c6 | -12.15389 | -60.80437 | 2026-07-27 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3894e95-caec-3dcd-a3b4-2c729f65864e | -9.63418 | -45.51968 | 2026-07-27 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31ed2501-c8f2-3d6d-a39f-fb207a89ecd7 | -11.43754 | -47.52906 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00c2308b-a832-38ad-810b-ff131a959cb3 | -11.4913 | -50.16349 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98da32e7-aca1-3ab9-a3e9-e3a527dec3f3 | -13.69187 | -51.91403 | 2026-07-27 05:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09af2fab-0228-335f-8b6d-2b4ce22c7613 | -11.49188 | -50.16087 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c63aa6f-0e58-30b8-b230-9fe516959ce1 | -11.45344 | -47.53508 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 018992e9-ee55-3c14-9e5f-b9e8628e751c | -11.46179 | -47.55708 | 2026-07-27 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ca628235-7ed1-3bcb-9d39-1e909bedf8d8 | -7.74063 | -55.34452 | 2026-07-27 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26c55912-2de5-3b53-8791-3ddabc917255 | -12.32226 | -50.37902 | 2026-07-27 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
