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
| ac6ab865-414a-3999-9730-ba895e191477 | -11.94357 | -41.3293 | 2026-03-14 03:57:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 801ec691-2f9b-3505-a09d-dadbf6d4c5ba | -11.93956 | -41.3253 | 2026-03-14 03:57:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| bda57b26-9bc4-30e7-95a9-00f68c5c43ad | -10.66638 | -40.30155 | 2026-03-14 03:57:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef7b4aa4-e14d-3980-bcd5-19419820b337 | -9.86353 | -37.48927 | 2026-03-14 03:57:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d5dc5ec9-f668-3ce8-a75c-6bf2359972cd | -11.05407 | -45.3932 | 2026-03-14 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcf7520c-e112-3e80-84cd-6777172cd63c | -11.94417 | -41.32562 | 2026-03-14 03:57:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 89d5be60-942c-3a37-86ef-10e7bf5467e8 | -10.62334 | -37.05052 | 2026-03-14 03:57:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cc4f2c2d-4888-3989-b7a1-a3f4c4435d1d | -11.88631 | -40.9388 | 2026-03-14 03:57:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7228b7fa-63cd-30a4-9f57-07d54b7ccbc1 | -11.94019 | -41.32873 | 2026-03-14 03:57:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 8358b790-c3c3-336b-940d-e68b840ba32f | -12.02501 | -45.34321 | 2026-03-14 03:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 448ed24e-7a50-3b56-968b-14b5c4525502 | -11.77982 | -47.08941 | 2026-03-14 03:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7517f119-1d4e-372e-9ff9-cf41aa685004 | -8.16521 | -43.16452 | 2026-03-14 03:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50832b82-df65-3065-abf1-78802cbb1441 | -17.87699 | -40.02005 | 2026-03-14 04:00:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9c21382f-e443-3baf-beaa-321eabe54085 | -15.86558 | -38.99576 | 2026-03-14 04:00:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 21027663-431d-357b-9f4d-71930eb55ca9 | -25.23945 | -52.11899 | 2026-03-14 04:02:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f3997c64-0844-346f-8875-3e70354fdbd4 | -25.23806 | -52.12524 | 2026-03-14 04:02:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ccbcdb54-9bfc-31e7-b5cf-6daf6fd39922 | -27.68814 | -48.75423 | 2026-03-14 04:02:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9cb0539-eda9-3d51-9e49-cea25573c765 | -25.23176 | -52.13003 | 2026-03-14 04:02:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| c75d4f7f-0096-3cf7-a1ac-11c8c9110299 | -25.23042 | -52.13609 | 2026-03-14 04:02:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 8b111943-71cd-3a0b-a735-eb0b4de57fc8 | -25.24432 | -52.12059 | 2026-03-14 04:02:00 | NOAA-20 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 62fe545c-99e0-3b0d-837b-f1453d7b217b | -27.45438 | -48.45338 | 2026-03-14 04:02:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c9a7632c-837a-3d77-930b-77658e57e590 | -27.68534 | -48.74776 | 2026-03-14 04:02:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62213b19-bc3a-3a77-b221-d4bd2c379c69 | -27.68426 | -48.75327 | 2026-03-14 04:02:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dad2ff74-f12f-3126-9418-70ca0b38db9e | 1.09635 | -59.27257 | 2026-03-14 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd4cdbc7-72cc-3e45-af2b-702d6f2da763 | 1.08297 | -60.36385 | 2026-03-14 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 76b15ef1-06cc-3400-87d2-936fbb464965 | 1.08071 | -60.36412 | 2026-03-14 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 17978f7d-1485-385c-bda2-674fb8df6137 | 1.10366 | -59.28299 | 2026-03-14 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 969de434-647b-3599-aef5-03e2c9b6645a | 0.9086 | -60.30159 | 2026-03-14 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c777f619-84b7-3c74-b30d-c1a028cb0e8b | 0.91387 | -60.29615 | 2026-03-14 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| af7d6dcc-4290-3a69-b03a-ee04d3b7b6c4 | 0.91455 | -60.30052 | 2026-03-14 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe45a32b-b5de-3057-8e59-91b233dba208 | 1.09692 | -59.27632 | 2026-03-14 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8040023b-8ce9-3a64-879a-ab0cafa03e44 | 1.09808 | -59.27195 | 2026-03-14 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41a8fef4-5f09-3142-b8fa-73d649f0681d | 1.42602 | -60.07044 | 2026-03-14 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 854baf1f-0d30-3848-9cc3-b20d057e6445 | 1.09867 | -59.27569 | 2026-03-14 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 450c9a11-6534-3bfa-89aa-0fdda1e53cc5 | 0.9079 | -60.29716 | 2026-03-14 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 854ddaf8-80e9-35af-92d1-b550c2936d08 | -6.9841 | -47.08667 | 2026-03-14 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cbc8893-10f9-35e7-a2fc-af2f92044b0b | -6.98393 | -47.08467 | 2026-03-14 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb5e8b54-0a11-33ad-9b7c-9958db439c9e | -8.88045 | -44.77809 | 2026-03-14 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 206ad1f4-5ba1-388a-8ddb-3b85051ae10c | -11.94672 | -41.3302 | 2026-03-14 04:49:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 970e1d17-b1e2-36d0-9611-5d742f991ad4 | -11.94409 | -41.3271 | 2026-03-14 04:49:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 7266a7b5-5a47-3657-a2e0-a561b07444c8 | -12.02848 | -45.34223 | 2026-03-14 04:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41d289b4-3dc9-3022-9d39-e88eb037e8c6 | -11.78212 | -47.08952 | 2026-03-14 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eb62108-ba8a-361f-9ef3-e3b2e4ccbbf4 | -11.78519 | -47.09733 | 2026-03-14 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 496b6450-e599-329e-bea3-41792e4495c5 | -12.32916 | -43.65248 | 2026-03-14 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3525950-df05-3da4-a376-68e81634312a | -11.94354 | -41.33164 | 2026-03-14 04:49:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 3d2d8401-b6bc-3201-9128-eeb8a54c56f1 | -11.78162 | -47.09315 | 2026-03-14 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a75206b-29b8-3c92-89e9-c84b5da96d21 | -11.94723 | -41.32568 | 2026-03-14 04:49:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 7e216436-e54d-360f-8691-635f4e3f05da | -11.94074 | -41.32939 | 2026-03-14 04:49:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 09edcfa3-2b95-3350-9198-38feec2224f1 | -11.77806 | -47.08896 | 2026-03-14 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c1f8b7e-1c3c-3399-92b0-29311e1b3690 | -11.94125 | -41.32487 | 2026-03-14 04:49:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 5a55f25a-802d-365b-a9cf-aac2c11aa366 | -18.94128 | -53.44187 | 2026-03-14 04:51:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d6e847f-9c1a-3574-a2db-2d2d8e3ff9a0 | -18.93797 | -53.44131 | 2026-03-14 04:51:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1f117c0-4c74-3c54-9bba-b1ac033c9dba | -19.38338 | -52.16011 | 2026-03-14 04:51:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c27b531-5593-3540-ae0b-12fb97c295e7 | -25.23728 | -52.12911 | 2026-03-14 04:53:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e0d15d19-4fc3-351b-9d51-d1317fbcbd87 | -25.24211 | -52.12047 | 2026-03-14 04:53:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 3e9c6975-4549-3fd2-9c3c-b274e1f5289a | -25.23367 | -52.12854 | 2026-03-14 04:53:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 66507e99-514d-38cb-a9ee-e49288b6492b | -25.24573 | -52.12101 | 2026-03-14 04:53:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 82c29d26-129f-3097-a811-cc0667a16095 | -25.2415 | -52.12509 | 2026-03-14 04:53:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 482b6785-4a9a-3c1a-b5b9-4df77d9c97c8 | -22.03628 | -56.30653 | 2026-03-14 04:53:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33cb7602-4e9c-3baa-b5b8-fd2c425f652c | -27.68927 | -48.75152 | 2026-03-14 04:53:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ebbb7144-21ac-31a2-bd3e-d7ee01fac770 | -28.6679 | -55.98639 | 2026-03-14 04:53:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 2bb5da2d-a613-37ea-8da1-aa7d0e8aba0a | -27.82968 | -50.30471 | 2026-03-14 04:53:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eb932229-91fc-3c29-81bd-56b37fdb6017 | -22.03693 | -56.30266 | 2026-03-14 04:53:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d48b844-b702-39fb-ab5a-cf96936b55b6 | -22.03356 | -56.30201 | 2026-03-14 04:53:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3339843-3ef4-341e-96d1-f6c7b580ffb0 | -25.23306 | -52.13316 | 2026-03-14 04:53:00 | NOAA-21 | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 3cba28e1-3162-31ff-9717-ef058c9d56db | -24.08787 | -54.28911 | 2026-03-14 04:53:00 | NOAA-21 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a3dc2a21-80d5-3376-aa33-05186377f1ca | 2.31923 | -60.24032 | 2026-03-14 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1589a5a7-3ef9-3fc4-a0d8-4251fd8bb13d | 2.40126 | -60.23129 | 2026-03-14 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c370233-4ded-3522-b74d-2777c4fd6eee | 1.10329 | -59.28207 | 2026-03-14 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 923505c7-5296-35a0-b8df-e2951f35521e | 2.31074 | -60.23848 | 2026-03-14 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dba6cf3-5b85-3bcf-9640-264aa0615d25 | 1.513 | -59.93356 | 2026-03-14 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f56e46a-809a-3dc3-9c13-779aa8781a24 | 2.75093 | -60.42865 | 2026-03-14 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a028fd3-d3c5-3a97-9ceb-330665eff2ec | 1.0982 | -59.27388 | 2026-03-14 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4265340-d2e8-3d84-82ee-f6c4eb1cc347 | 1.10701 | -59.28149 | 2026-03-14 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d4e3307-0b07-3412-a072-fb57d93a38e7 | 2.31526 | -60.2412 | 2026-03-14 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c36d4ad-af34-371b-996e-b383631a932e | 2.31128 | -60.242 | 2026-03-14 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ce03946-4749-3b40-af5d-8a240954999d | 1.09888 | -59.27826 | 2026-03-14 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a9aa8b1-fde4-3df5-87c8-26e6d105cb8a | 0.91384 | -60.29798 | 2026-03-14 05:16:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1de360d-670e-3355-9138-e1fc1e4f052f | 0.68413 | -60.33435 | 2026-03-14 05:16:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2515038c-2b7e-37fb-ab35-9523fbafe43a | 0.68388 | -60.33767 | 2026-03-14 05:16:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14ad9459-2cc2-3099-9e3f-6c08da3da628 | 0.91307 | -60.29301 | 2026-03-14 05:16:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd5c8d50-5445-3799-9839-5567ddc1c2a0 | -18.93726 | -53.44126 | 2026-03-14 05:21:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 494ed9a5-3230-316b-84f4-f021b5fc7b88 | -21.37906 | -56.09251 | 2026-03-14 05:21:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88d51f74-1960-3656-ac43-af6f450113d1 | -22.03167 | -56.30446 | 2026-03-14 05:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08fa840d-ae0a-3254-b0e4-ea10677fcf84 | -25.24094 | -52.12116 | 2026-03-14 05:23:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 35504f94-53a6-3d34-bfef-e8b0c386a656 | -25.23431 | -52.13527 | 2026-03-14 05:23:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1f561220-192d-3787-bb9a-dc958e767b3b | -25.24626 | -52.12158 | 2026-03-14 05:23:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 040bac4c-286a-3781-b4d3-7c2cefa22c40 | -25.23498 | -52.12783 | 2026-03-14 05:23:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 2e676060-d86e-3912-9cfa-801820871fa8 | -25.24061 | -52.12477 | 2026-03-14 05:23:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 8e233bbb-be62-3301-999d-46e5f9090b07 | -22.03558 | -56.30499 | 2026-03-14 05:23:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 902ec798-d251-3f98-8fea-e75a49b6ba45 | -25.23465 | -52.13149 | 2026-03-14 05:23:00 | NPP-375D | CANTAGALO | PARANÁ | Brasil | 4104451 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| aa996cf0-ba03-3813-b07d-5ee7e1e758d9 | -11.94126 | -41.32148 | 2026-03-14 05:27:00 | AQUA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 39.9 |
| 8834452c-5bb0-36de-a5e3-2934d4abecfb | -11.94249 | -41.31664 | 2026-03-14 05:27:00 | AQUA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 32.7 |
| bfe50c84-8062-39aa-9cea-abfb4e62161d | 2.3085 | -60.24022 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d35af8b-6a22-3392-8184-7e553ce5ae5b | 0.91126 | -60.29837 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 091fd70e-cfd6-3079-a8d8-abf719523c5f | 2.31867 | -60.23878 | 2026-03-14 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e0f7763-3ad6-3b59-9c21-d838bcc3aa1b | 1.08352 | -60.36576 | 2026-03-14 05:36:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0eb416b4-a83d-3a5a-8e35-8a26ebdfc199 | 1.10247 | -59.2813 | 2026-03-14 05:36:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e716c9-5857-3609-b4c2-47fc32fcfebc | 1.10602 | -59.28074 | 2026-03-14 05:36:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc594ce8-574c-31e7-9f0e-3e166286173d | 1.10667 | -59.28477 | 2026-03-14 05:36:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
