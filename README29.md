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
| eb2a1724-0162-39f2-87fc-49813e5fae4f | -18.54277 | -48.22369 | 2025-08-09 05:06:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 71f8ffb1-7b89-3f49-8316-f8832876060f | -14.49325 | -52.11012 | 2025-08-09 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8287ecfe-f762-395c-a1c7-50ade3635a6b | -19.81082 | -47.06991 | 2025-08-09 05:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 11855974-c8f0-3a52-98a4-0e9e11e3c570 | -22.15049 | -49.45481 | 2025-08-09 05:08:00 | NOAA-20 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fc7e3297-f171-307a-9207-a22c3edf6a73 | -19.81131 | -47.06435 | 2025-08-09 05:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 9297eb68-0fda-352d-becc-acbf7d3ca019 | -19.45601 | -56.89137 | 2025-08-09 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| fb5262de-8ffe-360d-bc85-fe2976e5f9d9 | -20.50944 | -54.90516 | 2025-08-09 05:08:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f94e594-26ca-36d8-bb52-f9527ec83b84 | -19.81754 | -47.06473 | 2025-08-09 05:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 29.7 |
| e2ab24a3-98ea-37bc-abc1-434531d792ee | -22.14536 | -49.45024 | 2025-08-09 05:08:00 | NOAA-20 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8181db57-cf34-3553-94ff-bbb112ff56d8 | -19.81211 | -47.07119 | 2025-08-09 05:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 72318c41-d3b5-3464-8039-6d60ec6fb907 | -23.65178 | -51.62327 | 2025-08-09 05:08:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 283e532c-c524-3b5a-bcdb-275793bc0e8a | -20.47903 | -53.67624 | 2025-08-09 05:08:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75aa9c5a-e432-3181-8a52-01093fff51cd | -19.81177 | -47.05912 | 2025-08-09 05:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5fc72cc8-f206-32dc-8946-94c29d0ff1a6 | -22.15085 | -49.45097 | 2025-08-09 05:08:00 | NOAA-20 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fa966808-235b-3e49-ba0f-eec744eb04c7 | -19.81314 | -47.06026 | 2025-08-09 05:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 2af6afa3-0d0d-379e-ab6f-189c6b4e51b2 | -19.81263 | -47.06562 | 2025-08-09 05:08:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 355c465f-2ed1-37e3-bdd9-8552546ab61a | -20.47556 | -53.67626 | 2025-08-09 05:08:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa09a514-9f9f-3bec-a5ae-1907eb3ea7a3 | -19.8124 | -47.0634 | 2025-08-09 05:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| ad5390d8-e0a5-3ed4-a522-a2c39309ca80 | -13.6144 | -49.0079 | 2025-08-09 05:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e9c106d2-5717-30f9-b494-85f190bade13 | -8.9215 | -60.7297 | 2025-08-09 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 2b5b5164-0574-30aa-94d1-b4c6b1be3383 | -8.9213 | -60.7489 | 2025-08-09 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| acdb2a44-cac3-39f4-b469-c95cd6fb8c43 | -8.9399 | -60.7481 | 2025-08-09 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 04a8a8f9-e9ae-39b0-ab1b-612525d9faa3 | -19.8124 | -47.0634 | 2025-08-09 05:20:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a0b941e2-6fb8-3454-8d7a-fd1889627f1d | -8.9213 | -60.7489 | 2025-08-09 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 87971e8a-c317-3621-b649-cae1134272b8 | -8.9399 | -60.7481 | 2025-08-09 05:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 0d63ef95-dbce-36b7-986f-729a98f2d2d5 | -6.57274 | -44.56599 | 2025-08-09 05:27:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 531323e2-c09a-3f37-a435-606fbf767af4 | -6.62546 | -47.28384 | 2025-08-09 05:27:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 68704afc-5e9b-3453-b599-c0f57a22ad91 | -9.05732 | -45.07036 | 2025-08-09 05:27:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| c0462ebf-b88b-3925-880d-d93ab505a07c | -7.25393 | -44.6576 | 2025-08-09 05:27:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6e8edec7-0190-3d3d-b582-5cab0368f6f6 | -5.21604 | -46.07 | 2025-08-09 05:27:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 91a3e3ea-2d57-3729-a7d1-d610857bf655 | -5.42438 | -41.22775 | 2025-08-09 05:27:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7fdf8b8a-ae11-3229-a0e6-9d091cb596d2 | -6.1351 | -42.96874 | 2025-08-09 05:27:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 9ebd132e-0405-3e21-8050-2f4772e0353a | -6.13675 | -42.95825 | 2025-08-09 05:27:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 1d668df4-2161-3a95-a42a-9cd82684ff43 | -6.58329 | -44.56781 | 2025-08-09 05:27:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4b4998d3-65da-3863-bc59-97b96926d9c1 | -6.59054 | -43.39716 | 2025-08-09 05:27:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 87288ed5-73ad-3bc9-b8d1-8e581e96a79b | -6.62335 | -47.2885 | 2025-08-09 05:27:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 16b679ed-8c3e-3697-8929-c2fb370bf5d7 | -6.57068 | -44.57906 | 2025-08-09 05:27:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| afa4fbaa-ec97-3539-bd2c-be0c0d009c35 | -6.12722 | -42.95673 | 2025-08-09 05:27:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d1d8600c-f2f1-3b93-8960-49e9ef6b0482 | -4.10691 | -38.17681 | 2025-08-09 05:27:00 | AQUA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| fc7e6383-2635-3cfc-8f32-752173d58bae | -6.05352 | -43.74723 | 2025-08-09 05:27:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 32bbb8da-0db8-3b6f-b72a-721a49c777a7 | -6.59223 | -43.38619 | 2025-08-09 05:27:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5cbde281-00e0-387f-a9de-70e72b286257 | -9.07656 | -40.47734 | 2025-08-09 05:27:00 | AQUA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| bfe63a9d-b219-394e-96e8-b1a0e09af1ff | -9.05519 | -45.08352 | 2025-08-09 05:27:00 | AQUA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 7323f65c-d962-3d04-affb-b5789a518393 | -9.85855 | -44.68871 | 2025-08-09 05:29:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1743fe83-ea13-3365-aeed-23db4775c888 | -12.56464 | -47.1243 | 2025-08-09 05:29:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f27054da-9e56-37d0-89c9-90f35504bffe | -13.06682 | -43.82687 | 2025-08-09 05:29:00 | AQUA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 61a6149f-df0d-38e1-b689-5320f6c763bc | -11.74062 | -47.48835 | 2025-08-09 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 31c9dc22-ccc0-3004-a2b7-6c5dcdabca4d | -18.54197 | -48.20706 | 2025-08-09 05:29:00 | AQUA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 5323f5de-5c4d-3654-962f-cfc11bf04f22 | -19.73543 | -42.06678 | 2025-08-09 05:29:00 | AQUA_M-M | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |
| 42594276-cc22-37e9-b99f-32eef1c53e68 | -19.59074 | -42.688 | 2025-08-09 05:29:00 | AQUA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 88900a8c-36ec-3548-9519-dcb9d88d7b56 | -20.42312 | -41.69846 | 2025-08-09 05:29:00 | AQUA_M-M | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3da9ce44-59a2-3873-a025-c6fdd753ae11 | -19.81018 | -47.06143 | 2025-08-09 05:29:00 | AQUA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 132.8 |
| b4723c8d-1e66-3216-bf30-e8ff757f4da3 | -19.59959 | -42.6895 | 2025-08-09 05:29:00 | AQUA_M-M | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 64eddf74-bf93-36e0-b9c4-77eaead466af | -9.8566 | -44.70081 | 2025-08-09 05:29:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 44658bf7-e068-39c5-8809-4de32da1d4d0 | -19.85205 | -41.42598 | 2025-08-09 05:29:00 | AQUA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 3e6af47c-bf63-3e70-a763-d9c3507c43b4 | -13.04531 | -43.84361 | 2025-08-09 05:29:00 | AQUA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 319fcf78-7e24-330a-b547-a7455a72259c | -19.80808 | -47.07359 | 2025-08-09 05:29:00 | AQUA_M-M | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3a07488e-8ae1-3f89-83f6-ed4f502b6fb1 | -12.56483 | -47.1127 | 2025-08-09 05:29:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 66b9fdd4-caf8-3817-b80f-85991b1060ca | -11.93668 | -44.54274 | 2025-08-09 05:29:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1b4b2989-c0bb-33c9-9815-2e8b1ab5fad9 | -18.53925 | -48.22253 | 2025-08-09 05:29:00 | AQUA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 26d5fffa-4cc1-3e41-9036-c308923a2b77 | -13.06527 | -43.83673 | 2025-08-09 05:29:00 | AQUA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f4baab76-7a92-3b60-bfed-df7a44ab862a | -19.59211 | -42.67862 | 2025-08-09 05:29:00 | AQUA_M-M | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d69f49ba-f011-345f-9ac6-e38da7313a5a | -19.85064 | -41.43624 | 2025-08-09 05:29:00 | AQUA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.9 |
| 706c407d-41b5-3bd1-875a-fc002b77256f | -8.9399 | -60.7481 | 2025-08-09 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| e801d4b3-9d72-3b9e-a8c6-9a3a042dc3ef | -19.8124 | -47.0634 | 2025-08-09 05:30:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a9228ab5-7b17-37d1-af27-c7bc62c64c63 | -8.9213 | -60.7489 | 2025-08-09 05:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f94c21e2-0af1-35c1-9744-7a5d725efb83 | -6.5856 | -44.564 | 2025-08-09 05:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 4df19635-1113-3052-adcd-41efc42482de | -8.9399 | -60.7481 | 2025-08-09 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c491a2a7-4cda-389d-ae54-149416b704e0 | -13.6144 | -49.0079 | 2025-08-09 05:40:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c13a0b87-b1b0-3d16-a337-4bf746bcff54 | -13.6148 | -48.9859 | 2025-08-09 05:40:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 56f5811b-7db3-34c1-b2d3-caf24acd4b69 | -19.8124 | -47.0634 | 2025-08-09 05:40:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 67.9 |
| fd1018fc-b898-3501-a5c9-c2c00bdde10e | -19.8328 | -47.0586 | 2025-08-09 05:40:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| dd9e5aff-f3ec-3e73-97e0-f756a1603623 | -6.5856 | -44.564 | 2025-08-09 05:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| fd18a969-633e-3635-8e26-6ee95bdb4af7 | -8.9213 | -60.7489 | 2025-08-09 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e3079abb-da1d-37d2-8155-2847dbf4a01c | -19.8124 | -47.0634 | 2025-08-09 05:50:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 9233471e-d2b1-3f2c-bc3d-cb4fb57d654f | -8.9213 | -60.7489 | 2025-08-09 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 77bbdd45-b438-36d6-989b-d874cd60af84 | -8.9399 | -60.7481 | 2025-08-09 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 27ef9b9e-db81-331a-9ac9-e9a29cfa9c75 | -7.09593 | -59.19067 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 537fbeaf-4879-3672-9781-08a89e8f5e54 | -7.09043 | -59.18987 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9d5c866b-3a86-380d-bf23-b01723941f2d | -8.92521 | -60.73249 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cad3cfe8-2eb7-3df9-b099-3ebf85449127 | -7.08995 | -59.19345 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 25e10a45-8dd1-3842-af2c-3decf4c6e931 | -8.91053 | -60.54842 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb077cbb-3157-3feb-ba5f-a6970c91818f | -8.91879 | -60.60325 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7ab2950-21d0-3b2d-89c2-a1dbed239427 | -9.26199 | -60.77479 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ea76d7a-bed7-3c84-9231-4dd19fafde8d | -8.93381 | -60.74593 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d3a71317-009b-3d66-ad08-18d783a5fa61 | -7.40434 | -60.00471 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ab23fcf-ea37-3e0d-b31b-bdf85b00af2d | -8.92325 | -60.74741 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a186537b-04b7-301b-968d-70b13dca097d | -7.09091 | -59.18628 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c4ed40ae-36be-38df-bff7-f6adcfefa8f7 | -9.93984 | -60.46083 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6488536-cf83-3d8c-a7ca-3c63fb1faf98 | -9.93484 | -60.49979 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e887b97-f5ff-305f-9c26-c9e962ff625d | -9.26159 | -60.77782 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46d96def-eff6-3428-9cc2-fc9a5463ff67 | -8.92404 | -60.74143 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0638f47c-470a-34a9-83b0-b3627eb3c880 | -9.93817 | -60.4738 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98ad5187-af65-3b8c-81fa-6b2387043291 | -7.46738 | -60.41138 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7433a9fa-c474-30c9-a1e4-db580dbeda9b | -9.94219 | -60.48421 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0406adc-5dfe-332f-8b38-d16522cba179 | -8.93303 | -60.75189 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c06b7e02-ca63-3346-8710-33b3438de841 | -8.92794 | -60.75115 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 83a88bb1-6250-3062-afaf-d3217039e214 | -7.39398 | -59.99869 | 2025-08-09 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f92d6601-8501-3ebc-86d5-4f147b011221 | -9.92403 | -60.45878 | 2025-08-09 05:55:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28ad56a0-d471-3de4-afee-65b152a8237c | -8.92443 | -60.73846 | 2025-08-09 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README30.md)
