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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47ac2d35-ec88-31aa-9be8-4597fab038ff | -13.39493 | -43.52766 | 2024-11-29 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a05ebc8b-2b14-3c23-9e38-ddccef65d3d9 | -19.33647 | -46.32386 | 2024-11-29 04:08:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac239404-d0ff-3b39-9c2d-3be139ebace9 | -19.33031 | -46.31875 | 2024-11-29 04:08:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b1de10c-275b-32f4-91e0-7a10c5602f7b | -14.12004 | -41.67802 | 2024-11-29 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aea133d2-05da-3638-b76f-d2564d2d12df | -19.33371 | -46.31937 | 2024-11-29 04:08:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bc18ff4-456b-3d9e-b8e5-fffe156689d9 | -17.57639 | -42.7578 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 04b43034-5176-3cb2-9920-60b904da417d | -15.50091 | -42.00936 | 2024-11-29 04:08:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18c735f5-70fe-3c0d-8212-1951dfd70b7e | -13.88056 | -43.07708 | 2024-11-29 04:08:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44cce717-83d6-3b65-a876-4d724a3d2806 | -19.30403 | -45.53797 | 2024-11-29 04:08:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7e7616b4-a4d0-3d90-9bb8-7f40b88fecf8 | -17.62507 | -42.75439 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22adec53-229d-3cfb-875c-650de367eb89 | -17.59516 | -43.19878 | 2024-11-29 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9337e2f0-2727-31e9-8ba7-1f5ca68c288a | -19.06176 | -45.88825 | 2024-11-29 04:08:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7ef37842-2739-3fa0-a7c7-204e1ce3e51d | -19.54705 | -41.13241 | 2024-11-29 04:08:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f3d87950-135f-3d9c-be48-100c9bb2c973 | -19.32965 | -46.32263 | 2024-11-29 04:08:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c3ce61b-b3e9-31c8-826f-ab914696fb5c | -17.09356 | -43.80594 | 2024-11-29 04:08:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 480628a8-d6e3-3a47-88b1-e39bbca1c631 | -16.0552 | -43.80165 | 2024-11-29 04:08:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b8f1627-f784-3bd8-be3f-dbfb111f6285 | -19.48098 | -41.61324 | 2024-11-29 04:08:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 51ab2835-5de7-3858-b2ed-c2d9ad3e442c | -17.76005 | -42.22374 | 2024-11-29 04:08:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 481cdf29-7c2c-3013-a7b2-d181371a884e | -17.5792 | -42.76207 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| f9ce8c9c-0420-3ae8-8104-a4d4bd2efcc6 | -17.60156 | -42.72763 | 2024-11-29 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eeeb43e1-4adb-3ba0-af06-4bed836ac95c | -17.62227 | -42.75014 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d3d294f-c2aa-303c-ad1c-851a07c10d85 | -16.10769 | -43.81369 | 2024-11-29 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4da982b1-b585-3c9c-9cef-62ef9da88a23 | -17.601 | -42.73137 | 2024-11-29 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3820aa7-896d-37df-b59f-b4dfed49cfab | -17.78011 | -42.80986 | 2024-11-29 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 674ec53a-d3b2-398a-bdd2-2d8c95771525 | -17.60436 | -42.73191 | 2024-11-29 04:08:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 282caa29-1b1a-39db-83d6-51d87aa243b6 | -16.19196 | -43.71037 | 2024-11-29 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f775bcce-a391-3354-b7bf-7d33a4d5f22d | -15.96362 | -38.92374 | 2024-11-29 04:08:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b373021d-fa21-3112-9279-f946edf71715 | -17.57975 | -42.75836 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3f32c75e-fe11-33a3-97d4-bfbd8a79d2cf | -17.58031 | -42.75463 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cffca40-ff82-3c41-852b-0eab7e43f310 | -16.68069 | -43.88378 | 2024-11-29 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fede7be-7bc9-3905-a157-2ebdf10fb2d4 | -17.16582 | -40.67699 | 2024-11-29 04:08:00 | NOAA-20 | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e7ce9973-ce1b-3ce0-be25-0a8dc8433054 | -15.96433 | -38.9186 | 2024-11-29 04:08:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9dea892c-9d58-3657-8ab3-505038586e80 | -19.66555 | -45.8833 | 2024-11-29 04:08:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b00a64ae-4812-3ad3-a22c-b9c6a5f55205 | -17.57584 | -42.76152 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9bb47cff-9e13-373e-a86a-b4f8bbfea4e0 | -15.96786 | -38.92131 | 2024-11-29 04:08:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 18438105-fbfb-32ab-a0a3-26d48056f1a1 | -16.51888 | -42.69126 | 2024-11-29 04:08:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05212058-cb07-3622-b298-d4ff58fb860c | -13.39549 | -43.52411 | 2024-11-29 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ad22729-b5c2-375a-8f93-016485353eb7 | -18.92843 | -39.9151 | 2024-11-29 04:08:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b02b334-1081-3ffd-bb29-46eb1ce719b4 | -19.67103 | -45.89207 | 2024-11-29 04:08:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc589fca-3eef-3210-8adb-06e0b4d5edba | -15.96393 | -38.92074 | 2024-11-29 04:08:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fab9dd78-72ff-3c07-9331-849ada0441f6 | -13.88112 | -43.07354 | 2024-11-29 04:08:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 449abb6b-5a5a-3968-91c2-99a9603ee5ca | -19.33306 | -46.32325 | 2024-11-29 04:08:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd178ca9-180d-3327-baf6-93ba1452109e | -19.7164 | -40.35453 | 2024-11-29 04:08:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a77f1ec4-24ad-36da-b765-fc05d6f7dcf8 | -16.86506 | -46.23613 | 2024-11-29 04:08:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 470618d5-624d-36ee-bc3f-71a1f36d5112 | -17.75272 | -44.95903 | 2024-11-29 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb10036-cc6e-326a-9bde-895a3c8e64b4 | -17.20844 | -39.86784 | 2024-11-29 04:08:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1741d6f7-ac32-3642-a68c-2aabc21fc95f | -19.48073 | -46.53005 | 2024-11-29 04:08:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0e1bf96-9971-3894-af36-336e856b5195 | -19.0584 | -45.88762 | 2024-11-29 04:08:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5b4a2e9-d72b-3ab0-849d-0d324949291d | -20.20494 | -41.43694 | 2024-11-29 04:08:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6931cfa3-90a9-36aa-a945-df74a842613f | -17.58255 | -42.76263 | 2024-11-29 04:08:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0e4cc52e-c6bc-3887-8eda-450fb64bfdb0 | -17.3847 | -42.65857 | 2024-11-29 04:08:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bce789ef-29a3-39c4-a69f-4fadd8cc8f3e | -2.6684 | -48.7767 | 2024-11-29 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 177.8 |
| 32d2e8f7-74d7-3d47-aa90-091ff9920058 | -2.9844 | -53.3022 | 2024-11-29 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| ee54471b-c261-3655-9794-4d72962f9efd | -2.6499 | -48.7772 | 2024-11-29 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 139.2 |
| eb5e923a-1db0-3415-a2dd-8e14e0b45235 | -17.5805 | -42.7483 | 2024-11-29 04:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| aa531095-5b4b-339d-acb6-318823b84e95 | -3.259 | -53.6388 | 2024-11-29 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5614204f-2af0-35b3-bcb3-bef9a925ec97 | -1.6997 | -52.433 | 2024-11-29 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 9e6ee282-83d5-3884-96a4-4be8552bafec | -1.5897 | -52.2915 | 2024-11-29 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d0103c7f-e5d5-3a10-bf7e-879f97a2425b | -2.966 | -53.3027 | 2024-11-29 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| bec84c04-29ae-3197-99e4-fab5a23e8322 | -1.092 | -53.3954 | 2024-11-29 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 008b055f-83b6-3a5a-970e-e61ed6bc1f2e | -1.6081 | -52.2912 | 2024-11-29 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 6c7c67b1-2d3e-313c-b153-69880280591c | -2.966 | -53.2824 | 2024-11-29 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 65103f96-89b3-3fe7-abe1-43a65640876c | -4.4405 | -46.5754 | 2024-11-29 04:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 590a23ce-6853-3250-98d0-e6618531c40e | -2.3419 | -46.8781 | 2024-11-29 04:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 5733e243-70c6-3d7c-bacc-b39703e5fdf7 | -1.6997 | -52.4535 | 2024-11-29 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 5f24e7ef-80e7-3c00-9f0b-a210d1db1bd9 | -2.6683 | -48.7981 | 2024-11-29 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 68b0ad98-8aca-3bbc-85f9-0f639013bd64 | -2.6498 | -48.7986 | 2024-11-29 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| ae40f923-2897-3a6c-84b9-d2060828438d | -2.9844 | -53.2819 | 2024-11-29 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 210.9 |
| d2bd1742-dccb-3149-81f0-b1c02426fdac | -20.93741 | -41.66121 | 2024-11-29 04:10:00 | NOAA-20 | SÃO JOSÉ DO CALÇADO | ESPÍRITO SANTO | Brasil | 3204807 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| edec4ed6-4287-3b6f-9282-9536d2eed2fc | -20.45742 | -46.15058 | 2024-11-29 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 239decca-59b7-3792-b127-c40b97780811 | -20.2391 | -46.40623 | 2024-11-29 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88ccc305-0f56-334e-b0cd-2ffa2a17ada5 | -21.87737 | -46.45565 | 2024-11-29 04:10:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ff08a674-a77c-3cc4-aef2-aa639c6b5403 | -21.87401 | -46.45504 | 2024-11-29 04:10:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8822bfdd-a341-3d4a-8179-15f3875a8587 | -21.30604 | -43.79224 | 2024-11-29 04:10:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c08c8ec-cbf7-3c62-a53f-fbbcca86a6c2 | -21.4028 | -42.95324 | 2024-11-29 04:10:00 | NOAA-20 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61fb66b6-0dd1-3849-b938-454de818a183 | -21.17953 | -43.97932 | 2024-11-29 04:10:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 90a897d7-1cbb-3067-8864-73052a4d9a34 | -20.76441 | -46.77158 | 2024-11-29 04:10:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b895b6c-6a4c-3656-9420-6d0d1ad7a0fb | -21.73079 | -45.53367 | 2024-11-29 04:10:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 70e85d8d-6d74-3d3b-bb13-2216d641a202 | -20.90083 | -43.82169 | 2024-11-29 04:10:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 00226f9c-b619-3f3a-8ff2-b5d61fd607de | -21.19389 | -44.93704 | 2024-11-29 04:10:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d41d7cfd-b652-328a-b715-2fc8abd26e45 | -21.6247 | -43.46779 | 2024-11-29 04:10:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6b50bb25-0db5-301d-bb18-bd4244e7e1fd | -20.86495 | -43.70364 | 2024-11-29 04:10:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e705be4e-4841-3564-8ab0-5dfe9b51145c | -2.6499 | -48.7772 | 2024-11-29 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| ee6bddb1-e2d2-3af1-8e5a-b85dde9c47ba | -2.9844 | -53.3022 | 2024-11-29 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 7bcc8afe-0532-36c1-83c5-51c434cab449 | -2.6683 | -48.7981 | 2024-11-29 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| de2fb98d-d98d-307e-b422-34a9d2bd8601 | -1.6081 | -52.2912 | 2024-11-29 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 7727e1a7-1e99-321f-967e-0a5aff5b6bf2 | -4.4405 | -46.5754 | 2024-11-29 04:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7247aa22-09ad-3743-8f55-cf312417e5b1 | -1.092 | -53.3954 | 2024-11-29 04:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 9f34abe9-ca04-3096-8708-ca19c9324e76 | -17.5805 | -42.7483 | 2024-11-29 04:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 674ab20a-1f8b-3a02-8f19-df4048097f02 | 1.2171 | -55.9471 | 2024-11-29 04:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e9566ac3-ea40-3f89-bc7a-606a5c326d06 | -1.6997 | -52.4535 | 2024-11-29 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| d4e9812c-8c9f-30b1-a006-a85b11f8a06c | -2.6498 | -48.7986 | 2024-11-29 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 062f6227-be3e-375b-bd2e-c1ee9d5b2be5 | -2.9844 | -53.2819 | 2024-11-29 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 0d6adc6c-ad1a-38aa-b9da-a024a6dd567c | -2.3419 | -46.8781 | 2024-11-29 04:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 249315b7-8a21-3191-9872-64e3b65e9fde | -2.966 | -53.2824 | 2024-11-29 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 4bd04c90-97a4-3fd2-a4d9-226bc224530b | -1.5897 | -52.2915 | 2024-11-29 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9242914a-c3c8-3525-8df4-65429ea64e71 | -2.6684 | -48.7767 | 2024-11-29 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 6ed4bd21-efbe-3876-a3d4-0686bfc119be | -2.966 | -53.3027 | 2024-11-29 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c86748fa-46d9-3696-9c13-b15307df4166 | -3.259 | -53.6388 | 2024-11-29 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5432d1fa-4493-3137-8156-8f62c52a7c6d | -2.6684 | -48.7767 | 2024-11-29 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 146.2 |


[Clique aqui para ver as próximas entradas](README38.md)
