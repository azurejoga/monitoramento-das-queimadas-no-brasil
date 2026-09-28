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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12026f53-4693-3236-9b7c-ee5da39eb96d | -11.71731 | -43.46096 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 311.9 |
| a481c999-4b96-344c-984c-8701b835bb10 | -15.06903 | -54.59642 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0e5f37ea-2ac4-36ce-91ab-249bd505ec79 | -17.66812 | -42.01281 | 2026-09-28 17:07:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| eae10976-bb98-3d5f-853f-f7c49ba346b3 | -18.09136 | -44.3866 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 2f80f26e-3777-359c-991f-39a96de1e927 | -11.89635 | -47.02052 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 12e0e24d-6028-39be-9d21-f4c444c25ada | -16.07999 | -48.08374 | 2026-09-28 17:07:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d00f581-c7e2-3ab5-9ba0-0f69faec3d2c | -18.39691 | -42.55063 | 2026-09-28 17:07:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9badff70-5947-3e79-b0fa-21f57086c935 | -14.53643 | -48.31181 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f77c4604-785b-3891-940f-de74a6ffc10c | -14.98327 | -54.33969 | 2026-09-28 17:07:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ffd2b9d7-bfb6-33ba-9266-e2885592b0c0 | -14.3232 | -44.82817 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c39d6ec2-5385-3c3b-9e3b-99290722db14 | -16.06895 | -47.92758 | 2026-09-28 17:07:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 601ed060-ac0e-3c67-8623-a4306841a57d | -12.52035 | -49.9792 | 2026-09-28 17:07:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c9d03f00-d511-3d9f-a76d-95bc6677a551 | -13.07952 | -47.41414 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa87abf3-50a1-3a66-a93f-bd633e925045 | -13.81611 | -44.25055 | 2026-09-28 17:07:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0f4a6e52-f458-33fc-a8df-c2eb926e3789 | -14.0862 | -46.33308 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.4 |
| a768fe2f-bec0-3980-aed5-b6a10ddec03f | -18.40829 | -42.30632 | 2026-09-28 17:07:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c5c1813b-c3a7-3273-89cd-28cabf97f02c | -13.14775 | -48.54042 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 19f348e0-e89c-337f-94c5-cb3de69e3e0a | -15.77634 | -52.4556 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c610382c-b1e0-3900-b017-af96da11610d | -12.61262 | -47.31761 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 183a7dda-ac34-35e6-ab1b-69892ad54e80 | -16.1524 | -43.62903 | 2026-09-28 17:07:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5c626a38-03be-3163-a0d1-3658561246fc | -15.73818 | -46.03035 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 170.1 |
| a42552e7-6978-3425-a45c-19e3298a310d | -16.79074 | -43.0051 | 2026-09-28 17:07:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 446c38ff-e428-3091-85ff-2c21e3136955 | -14.31762 | -44.81218 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f439f83f-678e-30d4-b603-59f4f2069f8a | -13.15616 | -48.56396 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14dee5e1-3dd7-32aa-814a-8cb1d43804c6 | -12.98848 | -44.73788 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 18bf0c4a-f277-3cc5-bbce-6e42b844bc42 | -14.31518 | -44.81374 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3c125a21-014d-3b0d-b18a-061a982c684d | -12.4456 | -48.22255 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 55041ca1-0d2b-399f-94af-a921f4bef76f | -12.8777 | -44.81163 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cfafaad2-7a9e-3ebf-b7d7-89fc9dece9f5 | -13.48998 | -48.60511 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f039f982-7c72-3868-b27e-f888f8c027bd | -12.96888 | -51.08042 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a1b8d0a9-a4f0-38f9-b24a-8a1e9ed5efa0 | -12.44495 | -48.21903 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b9e74252-65f6-36a2-8c2a-386f9c8870c0 | -16.35117 | -42.57918 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 1a3c1942-96a7-3aac-a12b-8f1c3a1266d5 | -12.79857 | -50.5967 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ff0b1657-dfab-367e-b21c-d1d4ebfae243 | -11.39981 | -43.43318 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| fbb79417-ab6f-3d70-81c0-21ad8e29f110 | -15.83253 | -42.56192 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 64134241-5aa7-304b-9112-f8cfe0efe593 | -15.16795 | -46.14351 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f4520481-1acb-3907-aaa4-38f18d4822dd | -13.37619 | -44.01775 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 649e9bde-ca35-3e31-acbf-ff6e97291d3b | -16.12082 | -51.47007 | 2026-09-28 17:07:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9c1ab62b-574c-3281-927a-c204c65e1c93 | -13.04045 | -46.99679 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| db04ca2e-fcfe-31d4-a5b7-fa0285e5c734 | -13.20151 | -48.53495 | 2026-09-28 17:07:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5841aa01-473b-31af-b164-40197f345600 | -15.03982 | -48.03399 | 2026-09-28 17:07:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d1f6beb7-6ad7-3c40-87be-2fc879204007 | -14.23652 | -49.13132 | 2026-09-28 17:07:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8c0aedf-d492-3585-94bb-84ac10e70bfd | -15.74202 | -46.02166 | 2026-09-28 17:07:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1f2291d9-084a-3a05-a0a9-df0877886667 | -18.09254 | -44.39254 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| de36be5a-30ea-3676-aa3a-ba4369bb8db1 | -14.30852 | -43.73735 | 2026-09-28 17:07:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b8f91301-39a1-3c43-9c96-46d9e8dbe611 | -14.40261 | -41.02468 | 2026-09-28 17:07:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5629c216-0e9d-3720-be35-763edef586cd | -18.44075 | -43.95515 | 2026-09-28 17:07:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ffec8c23-2f60-329f-85da-c25abd829414 | -13.94038 | -49.0714 | 2026-09-28 17:07:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6fff24bb-b6a8-3b43-84ea-be8466808d78 | -15.15197 | -43.6136 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 43706441-43f8-3337-bbe0-2402a7939f27 | -14.00214 | -42.1049 | 2026-09-28 17:07:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f82adb03-dea5-3d0f-b420-f3843ba4530f | -14.80379 | -41.73399 | 2026-09-28 17:07:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 8a3cb111-6167-3331-82fa-a093d1d25eeb | -14.56489 | -49.15414 | 2026-09-28 17:07:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6e6a0ee-059b-38c9-9cc3-031342290ca1 | -18.6827 | -48.62352 | 2026-09-28 17:07:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 286.9 |
| d5985a71-28dc-3788-b704-485f56beda79 | -15.16493 | -43.62207 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f622effd-8f67-3ddd-b063-c17615a3ba95 | -15.89975 | -42.95293 | 2026-09-28 17:07:00 | NOAA-21 | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7c90fdeb-08b2-3f07-89fa-b72f05340acb | -11.89925 | -47.00996 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 63670be8-9ec1-335b-8bc1-c200f441bb31 | -12.61389 | -45.08159 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e28b0d12-faf5-3e37-a8d3-558d4060a7f7 | -14.48973 | -45.24014 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| bf26856a-edf4-32b5-908a-85a153c97a6e | -15.02799 | -40.97571 | 2026-09-28 17:07:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 5a2213f7-2036-3272-baab-26f5bbc0b388 | -12.09509 | -45.23526 | 2026-09-28 17:07:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 371d8e67-5db5-3433-a5d1-bc511db85df1 | -13.43867 | -48.62182 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f6d5a1b-c5d0-3226-9d3c-7e0e8590e960 | -15.54051 | -47.38271 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 110fc09b-ff6a-33fd-91bc-d311962afde6 | -11.35781 | -43.40555 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 461ab313-398c-36bb-af7c-cddda97bf09d | -18.43558 | -43.98088 | 2026-09-28 17:07:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d917737-cdd2-35ec-b236-5a95d3d82534 | -12.66482 | -46.98666 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f370babd-ae9f-36a9-9ba1-309a545c095e | -13.95185 | -49.2296 | 2026-09-28 17:07:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 32b0e750-ffe6-3174-9a37-1362d2a64e8a | -18.77009 | -45.10812 | 2026-09-28 17:07:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2aa1065a-b9d6-3429-a52f-8c51c71e8132 | -12.6361 | -47.29458 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| db1633a9-82e7-3230-8de2-61ab951e581e | -11.63829 | -43.48635 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9df862e0-c474-33bd-871b-2d8ea08b8ee7 | -12.89471 | -45.04346 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a3b465de-3366-3913-9187-fe73c9ea1ca6 | -14.6298 | -52.11263 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9879d3f2-c761-3f7a-b851-02e0dd7f8232 | -14.73501 | -41.37949 | 2026-09-28 17:07:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8a9243c6-e1a8-3f94-b7e9-136da21f8ffa | -13.35953 | -43.3472 | 2026-09-28 17:07:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| e11a43f3-be6a-38a8-ac3e-212f64a7ea9c | -15.08923 | -48.33172 | 2026-09-28 17:07:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| b3fdb663-528c-3206-ac2f-0badb6dded18 | -11.90605 | -47.02571 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 28d6bc51-6805-388e-9de9-66d2ba222bdb | -15.35355 | -40.11404 | 2026-09-28 17:07:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| edbcbcdb-2309-3895-b6a3-486ce6027ae0 | -11.2659 | -43.54436 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c92519ec-dccb-3950-810a-358cf33f6ac3 | -13.32129 | -43.94062 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f8f3d89d-d673-36dd-9482-0fb329a7a7ae | -14.63258 | -52.10839 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ca9dcabb-3ecb-3dfc-8ef1-3fbd61d2a0c9 | -15.26569 | -47.62551 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b03a0c9c-4311-3da9-839a-ad1fb69294ce | -12.74165 | -47.32741 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 62f84725-d1aa-30f0-b65c-8fecf3252aad | -11.89788 | -47.00726 | 2026-09-28 17:07:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6b22e3b2-4281-3b8d-aeb6-77f58becb84c | -12.68034 | -47.36121 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a7e8a8c4-df91-39c6-a0fa-d2d0a4beb1a4 | -12.69775 | -47.33001 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d87afa4a-8a24-3946-9651-dc1f9c0251a4 | -17.5361 | -43.68766 | 2026-09-28 17:07:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 07c86f00-1f3c-33e1-b0fc-5739d1b5b97d | -15.98878 | -43.27992 | 2026-09-28 17:07:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c13c8591-ac58-319f-9a26-829d4ef62202 | -15.68941 | -47.60709 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 40f25ca8-e43c-3479-a4a5-f3fb116ef9e4 | -11.66567 | -43.44482 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 24175796-66fb-35cf-9082-de7d2bc95b87 | -15.21127 | -46.17146 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 511d0e62-4f72-3698-89d7-6ec711c0d5e4 | -12.75781 | -50.6882 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 609cc74a-6f30-3d46-9cb7-608feb3fbb7f | -15.1541 | -43.62435 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 36.6 |
| c7fe9971-59ae-39c7-838e-f01bad4d3d08 | -12.70677 | -46.98226 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 17fd2209-4603-3738-97a4-09c580fec744 | -15.15739 | -43.61242 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 21.4 |
| ab5653eb-ac23-3144-a04f-252e612cb615 | -12.93738 | -46.64202 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| baa0b39c-f001-320d-a1d3-9913862021b6 | -19.44091 | -45.89042 | 2026-09-28 17:07:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54b235cc-b184-317c-a192-175667af0ee1 | -14.63771 | -52.11887 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 201bcb24-68d3-317b-84c9-94d0a3bb8ea7 | -11.77628 | -44.68739 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c79961b-7395-38fe-970c-25fbe1b15ef6 | -11.68316 | -43.44129 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 66c18d8a-7436-3a76-b5f2-3429f9722653 | -11.98898 | -41.9785 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 5eee42fe-9cf3-34db-98b4-60e56da8e738 | -14.72258 | -45.56609 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |


[Clique aqui para ver as próximas entradas](README141.md)
