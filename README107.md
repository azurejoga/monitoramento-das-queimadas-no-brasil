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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ab87ad3-ad6a-3c2c-a31b-d0f2bd70c5f6 | 1.6749 | -55.9225 | 2026-10-01 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ef4539df-91f1-33af-958f-f739bac6dd7c | 1.8036 | -55.6447 | 2026-10-01 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 410ba663-5b67-35f2-825f-07b96b5abaf6 | 1.6749 | -55.9422 | 2026-10-01 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9049ec06-34a9-3921-8d81-49645b9d7507 | 1.6566 | -55.9227 | 2026-10-01 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| daa1de32-d23e-33a1-8882-ac8afadc92fe | 1.8037 | -55.6249 | 2026-10-01 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 07a2c817-497f-3b9b-a199-d82947542793 | 1.8221 | -55.5851 | 2026-10-01 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 10acf1d8-4698-3c16-b4a8-be7f57268e54 | 1.6566 | -55.903 | 2026-10-01 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 26643ce4-b9d6-3fea-a8c7-d9d0c2ffb25a | 1.8769 | -55.6239 | 2026-10-01 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 30adbec4-4a26-36de-8c9c-f546db00bce7 | 1.7853 | -55.6449 | 2026-10-01 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8e8048a7-ff0c-35cb-a7fc-f299307f541a | 1.2613 | -50.6845 | 2026-10-01 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9c1d51fc-3e74-3485-afec-3d46f11848af | 1.8769 | -55.6437 | 2026-10-01 16:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9cbe3918-4b4b-32a0-b889-fae516dc72a3 | -19.69471 | -40.93543 | 2026-10-01 16:09:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 2f14b249-7e82-3fa8-a3df-04651f0e22cb | -16.99599 | -45.46103 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0779978a-f1ee-32de-8062-762d466632ce | -19.12429 | -40.3485 | 2026-10-01 16:09:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ca345c38-fe8e-3854-88aa-a0d59bd152b1 | -17.59164 | -46.79338 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d7fe2558-734e-39cc-a9b3-6a4f5466079f | -18.34793 | -40.05434 | 2026-10-01 16:09:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 147e0dd5-2c65-311e-9702-0da1065314f4 | -18.61975 | -45.13096 | 2026-10-01 16:09:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 659a1c45-d9e1-3637-80fd-852d6220aca1 | -17.94655 | -40.01638 | 2026-10-01 16:09:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 963b9f47-dca9-3913-97eb-5066adf3542b | -18.22685 | -42.89883 | 2026-10-01 16:09:00 | NOAA-21 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3bf7483a-c9b3-38cd-b566-d18d80baf5e7 | -20.08203 | -42.28327 | 2026-10-01 16:09:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| c1161497-ba94-315e-b37a-b8308920361a | -15.86591 | -39.12689 | 2026-10-01 16:09:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| c997807d-34d5-3d3a-965c-85ba9e6b8454 | -16.26145 | -41.32328 | 2026-10-01 16:09:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a93eca7d-1603-3486-b788-80e36f0a0832 | -18.83008 | -47.42651 | 2026-10-01 16:09:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9666a526-02a0-3552-a716-645d20d8d46f | -18.26281 | -42.23495 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| 478684b8-8fad-3564-9b6f-e95172dc151b | -20.77079 | -43.82441 | 2026-10-01 16:09:00 | NOAA-21 | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| daa788de-fa79-3714-a368-2a3852597caa | -18.34116 | -40.05541 | 2026-10-01 16:09:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 7769a412-bfba-36b5-a4c3-7ba286e89ffd | -17.61446 | -44.33293 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63defec3-5dbe-36fb-bc09-94b97d5c6ee0 | -16.85003 | -45.44195 | 2026-10-01 16:09:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c8f6d9f4-b8a7-3236-8a20-b2c5cf392aeb | -16.97366 | -41.93541 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c14e8396-5d3c-3914-a246-a6a31583b07d | -17.09251 | -46.81944 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5c6806d0-74f5-342e-a8ab-73268982345b | -19.69118 | -40.93596 | 2026-10-01 16:09:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 572ad70d-6e57-38fe-8782-3c82c1fd4d88 | -17.88459 | -42.24687 | 2026-10-01 16:09:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.0 |
| b752a6f8-f05a-3ecc-adcc-3b85c6baccde | -18.97051 | -41.04847 | 2026-10-01 16:09:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 73d7478a-50c7-38ed-9503-c3850eb3e9f8 | -19.51883 | -47.20124 | 2026-10-01 16:09:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b191b8a-13e9-3457-b00b-20cd2be3c569 | -18.53976 | -42.16383 | 2026-10-01 16:09:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1cc139ec-7097-3905-96c8-423bae8d1c90 | -20.77499 | -43.82384 | 2026-10-01 16:09:00 | NOAA-21 | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 7f0d4da9-09d9-3519-8f30-76056cdcf79d | -19.12486 | -40.35249 | 2026-10-01 16:09:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| ffba3a19-8117-335e-8937-65368c332c0f | -18.29929 | -42.25357 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 008d6f15-4bf3-3fed-a78b-066a339bb3f3 | -17.30413 | -41.73602 | 2026-10-01 16:09:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a99f7484-62d8-3b67-bb3e-3de970cf250c | -19.082 | -40.34726 | 2026-10-01 16:09:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dc12bb29-d55e-301f-8a19-acdb64a8ddcf | -19.03536 | -45.65718 | 2026-10-01 16:09:00 | NOAA-21 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| dc5a7228-ab9d-34db-b21d-89f6598c1db9 | -20.06886 | -44.6039 | 2026-10-01 16:09:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3a3a1a5d-64c8-35ce-af56-72ad67b55b9a | -16.62801 | -41.70036 | 2026-10-01 16:09:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 6fc9a5a5-0a43-3d40-9ad1-5393cb5f3b16 | -16.79994 | -40.80302 | 2026-10-01 16:09:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 851cedaf-a9ce-3b63-936f-f296c4cab851 | -17.67339 | -41.42955 | 2026-10-01 16:09:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 97a4b199-3be4-3560-af02-0c86c722cac7 | -16.84947 | -45.43744 | 2026-10-01 16:09:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| c41bef6a-efbd-3cc0-9605-8ff303ffd735 | -17.00363 | -41.18116 | 2026-10-01 16:09:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| acc1f886-36f6-3703-aa40-9e6fa6e4e0a7 | -18.96557 | -41.19609 | 2026-10-01 16:09:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3e77567c-7d9c-3623-a994-6013d716210a | -19.25754 | -43.97154 | 2026-10-01 16:09:00 | NOAA-21 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e95bfd6b-1982-3295-a9ad-a0f071198819 | -16.90347 | -42.1075 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 85d5826e-a17f-3090-b076-fac8a5723e13 | -18.81866 | -43.53709 | 2026-10-01 16:09:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 955dfbed-2e9c-39ab-9605-a0e2161c786d | -17.50521 | -39.20914 | 2026-10-01 16:09:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b1b483bc-c3b8-3a7d-9f72-8775c29a897f | -17.65529 | -48.20473 | 2026-10-01 16:09:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9e5b2455-8fd7-3b7e-859a-be1ad04ac3c9 | -18.20049 | -42.32303 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 185636a2-0ded-3ce2-8783-c2374a0fe0f5 | -18.27189 | -42.19046 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 95435b92-76d0-367c-aa04-cf2217818521 | -16.50864 | -41.28775 | 2026-10-01 16:09:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f155d193-9e09-347b-9505-164aa159e3a2 | -16.97219 | -41.93849 | 2026-10-01 16:09:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 00842a2b-42f6-353a-929e-e0a8565e4fae | -16.76991 | -43.95604 | 2026-10-01 16:09:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 163480cd-1f02-3fa0-b209-8e445727ca5b | -16.99577 | -45.46806 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| eeb8063c-6858-3bf2-b6fc-845ffaa89a12 | -19.68008 | -40.93374 | 2026-10-01 16:09:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 9e41f8ed-6a26-3461-93a7-064108f8eec5 | -17.88753 | -42.24767 | 2026-10-01 16:09:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.2 |
| 47d2ef7e-1bb5-32e2-89bc-e1f1a357bafd | -18.39981 | -43.03514 | 2026-10-01 16:09:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ae65930f-3151-3611-bb5b-bd12ce7ac51f | -21.43997 | -47.03771 | 2026-10-01 16:09:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ecff6e92-29f5-384b-a740-e735f5ca0792 | -19.65619 | -44.89813 | 2026-10-01 16:09:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 95529eeb-8f49-36eb-952b-a34a9a473319 | -17.43524 | -43.20839 | 2026-10-01 16:09:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db0c367b-af61-39ae-a945-ae76c7ab792e | -18.86019 | -41.06023 | 2026-10-01 16:09:00 | NOAA-21 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 7e78ed0d-03bb-3f42-b484-067a4ce59e2f | -17.32914 | -40.73618 | 2026-10-01 16:09:00 | NOAA-21 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 61f8cdee-da87-3918-aba6-9067e61c4ad1 | -17.58974 | -46.79812 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| cbae667f-48fc-31eb-af7e-2fe5ebc65486 | -17.59231 | -46.79908 | 2026-10-01 16:09:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cf97c007-a876-32dd-b3d0-0672bb462158 | -17.00075 | -45.47204 | 2026-10-01 16:09:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 59b41d17-530d-3437-88a3-23547230d98e | -16.87184 | -39.26538 | 2026-10-01 16:09:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d0463e55-163f-3492-ab55-335fb08f093d | -18.60237 | -43.49661 | 2026-10-01 16:09:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 8294900d-f63c-318c-b491-855c0c11af1e | -20.64146 | -43.48655 | 2026-10-01 16:09:00 | NOAA-21 | CATAS ALTAS DA NORUEGA | MINAS GERAIS | Brasil | 3115409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 2f196ba9-8474-3872-be61-1ba6bcc8d843 | -19.10797 | -41.50314 | 2026-10-01 16:09:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 574a4e30-2772-35cb-81b8-110899a4a209 | -18.60541 | -42.63862 | 2026-10-01 16:09:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 5ad00b05-d9ce-30aa-b874-9bb5d306fdc8 | -17.09934 | -39.92625 | 2026-10-01 16:09:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| cb593c60-ccda-3ca7-9fb0-935eb8f2a765 | -18.11169 | -44.55165 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d1bb0ce8-deea-3bd4-856c-f4aa80829d3b | -19.18575 | -46.11627 | 2026-10-01 16:09:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f1f3346c-19e0-3648-9374-698858ebb56e | -18.3523 | -42.79343 | 2026-10-01 16:09:00 | NOAA-21 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2be02d82-281c-3e05-83df-c6fce025f795 | -16.80489 | -41.13293 | 2026-10-01 16:09:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| dbd592e6-07b8-3db3-a590-4743f3e0ba83 | -17.62288 | -39.22354 | 2026-10-01 16:09:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4bd8fbf9-becf-309d-9e87-826c22632119 | -19.29578 | -40.57812 | 2026-10-01 16:09:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 81c106c5-e3d7-3e6f-8486-6133796e992e | -17.32083 | -41.54203 | 2026-10-01 16:09:00 | NOAA-21 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c12edc26-8d77-37a7-be08-be7af65509c3 | -18.05881 | -41.5029 | 2026-10-01 16:09:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b27850ae-ff4f-3f28-982f-bb4c81a20ad0 | -18.34171 | -40.0592 | 2026-10-01 16:09:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 4ed24187-3cb4-3d70-917e-4640f8103281 | -20.7666 | -43.82498 | 2026-10-01 16:09:00 | NOAA-21 | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 953dca00-7e95-3981-acaa-9f5f8385e107 | -18.60478 | -42.63379 | 2026-10-01 16:09:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| ef4ad96b-2533-3152-b740-b9e0f38bf4d2 | -17.70163 | -44.33693 | 2026-10-01 16:09:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 7cfdc369-080a-3bb1-9457-894cab669604 | -19.06954 | -40.01572 | 2026-10-01 16:09:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| d9b44594-4d26-339a-a24d-20af6935d851 | -17.88694 | -42.24319 | 2026-10-01 16:09:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 6dce9e39-5183-37f7-bbdd-a8ceca6fcd81 | -18.17267 | -42.45576 | 2026-10-01 16:09:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5d0cc2cf-fa09-3408-ae31-657e2e1722a6 | -16.78902 | -39.85141 | 2026-10-01 16:09:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a4085b5a-e647-35c6-b0b2-fda420a9bd11 | -18.58537 | -40.76995 | 2026-10-01 16:09:00 | NOAA-21 | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 9f72e953-973f-3daa-9f9f-e76708baf0de | -18.59139 | -43.55387 | 2026-10-01 16:09:00 | NOAA-21 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| b13b6fb1-5e0c-3bf1-bd6f-a1e153692d11 | -19.88156 | -41.2178 | 2026-10-01 16:09:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bc96f7dd-a09c-36e4-9277-105e298a4f17 | -18.09323 | -43.73303 | 2026-10-01 16:09:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9844edd5-fee2-3fc3-9dfd-13e6c1085035 | -17.44255 | -41.63903 | 2026-10-01 16:09:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| c247fc5f-cedb-3686-8362-6122fc0c1743 | -17.39407 | -41.62961 | 2026-10-01 16:09:00 | NOAA-21 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1ef972a7-0380-3f53-9aff-b57d738012a3 | -17.89121 | -42.24709 | 2026-10-01 16:09:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d5d1adea-8b76-3172-ada7-9e07675ae7bd | -18.10406 | -44.55996 | 2026-10-01 16:09:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README108.md)
