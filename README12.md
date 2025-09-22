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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40c9f0a7-1042-37e2-a505-6cef41b015ae | -7.36269 | -44.54781 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 827f9a55-61e0-302b-8132-b928c061d4e2 | -11.50036 | -43.57077 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0084dd95-d7fa-3939-9bfa-a5fff63af620 | -7.50897 | -43.68171 | 2025-09-22 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9645d03-14ee-3060-bac9-b15fadf55a71 | -9.99305 | -46.23709 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b0daad6-46b9-39e6-92d6-b1f70d43bdba | -12.98398 | -46.37381 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef5d5f53-cb28-3e21-9da3-4c9146f67db2 | -12.70722 | -40.47525 | 2025-09-22 03:49:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b575e739-1716-31cf-85bd-f8481fb0f39b | -7.02852 | -46.30865 | 2025-09-22 03:49:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a9cc4f1-8865-33b8-afb0-49df137a5366 | -12.96368 | -46.93964 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33c5e16e-3e88-3d01-8fb8-4b5fbf1e4f56 | -8.84745 | -46.15462 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7191427-d81b-3347-bf7f-982f85792179 | -7.22696 | -43.74801 | 2025-09-22 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04a4ce67-71dc-3503-9beb-af1743638b16 | -7.23069 | -43.75328 | 2025-09-22 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 85a49060-57cb-38d7-955f-819caf56eeb3 | -8.85258 | -46.15557 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81ecf02d-452b-36b7-8441-0eedf937632b | -13.96282 | -44.4267 | 2025-09-22 03:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f8fc1bd-1bff-3622-a84e-22408a678cb3 | -7.36743 | -44.5485 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2b7365e7-d7c1-3c12-8044-a76d4f65ee64 | -14.26795 | -44.37983 | 2025-09-22 03:49:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4847cdc-8856-3a90-a35a-feffdf23c1fd | -12.74114 | -46.83028 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9268f96-38e0-3681-97ec-ee99b346f568 | -7.80165 | -46.19181 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 676d42ea-822f-3eab-b81e-37437b4a091f | -12.43037 | -45.13305 | 2025-09-22 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3498867-0940-327f-8ce9-4b3854029cdb | -7.8023 | -46.18808 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ccdb6fe-7b15-3bad-9d91-8861375bf76e | -12.71501 | -47.71173 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47f6a800-77b3-3a06-96f6-d4521dc35875 | -4.03725 | -38.39249 | 2025-09-22 03:49:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6199165-ea02-3a1d-a34f-2e02298cef8c | -10.36709 | -46.05804 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a772309-6f77-315e-9c22-d4d044272ded | -12.43321 | -45.14318 | 2025-09-22 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b766f002-87f9-3c6f-9582-f918c02811e0 | -15.9591 | -59.3887 | 2025-09-22 03:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d9d83c3f-40da-3977-abfb-30e507f0fade | -15.8412 | -59.5199 | 2025-09-22 03:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| e57eeab1-f0ac-39e4-b94a-d8439922fcc3 | -16.0166 | -59.4432 | 2025-09-22 03:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ed5a8e92-2121-3603-91f6-ef7634bcf601 | -16.0163 | -59.4633 | 2025-09-22 03:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 836db29d-a8cf-3b55-9623-aabe936cd510 | -15.9972 | -59.4451 | 2025-09-22 03:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| a224163f-ac6d-3a31-9040-12e796ec67e5 | -15.9969 | -59.4651 | 2025-09-22 03:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 6f790951-b5c4-36fc-b749-aaa854fd00bf | -14.35108 | -47.78584 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38aefecf-d84a-3d7f-a5ca-626fae078b70 | -20.43869 | -43.67645 | 2025-09-22 03:51:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| da919b6e-7ff8-3337-9581-39bb352a6c62 | -19.86298 | -46.10424 | 2025-09-22 03:51:00 | NOAA-21 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95539189-349a-3167-b1bb-9a3fc4cd9851 | -22.70872 | -43.51706 | 2025-09-22 03:51:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 759a68d1-b06a-31ca-b358-5f0ed7e7f493 | -19.25067 | -46.54787 | 2025-09-22 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab224cf4-b014-382a-9501-d7a77980e910 | -17.0576 | -44.90809 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8d1fa93-892f-3442-ad73-eb1cee46116b | -20.26021 | -44.42108 | 2025-09-22 03:51:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fcdcb273-f38a-39df-8a0c-5ac84e8dd1c9 | -20.61198 | -46.07534 | 2025-09-22 03:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43fd4c06-f5b6-35c2-919b-ba27394ee410 | -15.16151 | -49.58833 | 2025-09-22 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d94a15d9-a8f2-37ae-9e31-d37a99b3432b | -17.05422 | -44.90356 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cf164ef-5ed2-3228-be05-dae86a6df663 | -19.70865 | -42.07641 | 2025-09-22 03:51:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a38022de-3840-3413-a037-044a2bca6d2b | -14.97478 | -44.41031 | 2025-09-22 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7378134c-b52d-375a-a731-42638ce9ef00 | -17.16623 | -45.95729 | 2025-09-22 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f8132e5-1e44-32ce-b343-e9088b4bc349 | -15.16237 | -49.58429 | 2025-09-22 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 749d3716-b848-3bfb-ae72-2b3a54c99a5c | -19.25004 | -46.54953 | 2025-09-22 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 322f8007-2176-3699-ba08-c517650db5d3 | -18.3827 | -46.47127 | 2025-09-22 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4e85fe7-306e-3f92-bcfd-6b72430263fc | -20.60859 | -46.07059 | 2025-09-22 03:51:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f610cdc-893c-3458-a01f-d1cbaf0f21ed | -20.13099 | -42.49007 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 96469dc3-5609-37b6-ba9a-c13647d2eafa | -22.70586 | -43.34738 | 2025-09-22 03:51:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7d3aaa8e-63c9-3945-8fe2-fc3b73590cc2 | -14.32767 | -47.79522 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dda6453-f953-314e-8d0c-e58b5c04db57 | -20.75506 | -43.35973 | 2025-09-22 03:51:00 | NOAA-21 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| acaa2a52-4800-382d-9121-0d7b6b05d829 | -14.68808 | -48.78328 | 2025-09-22 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2d6b653-623e-3961-ad8d-c484e148e9ce | -16.7059 | -46.94887 | 2025-09-22 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fc52438-3745-3634-b999-d6e2451f382c | -14.33189 | -47.79552 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f69e0e0-7a6e-3664-83da-6b839cbfff44 | -20.86674 | -42.24273 | 2025-09-22 03:51:00 | NOAA-21 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4e691cf-791b-39e4-85be-7e3806bcd6fc | -19.97794 | -46.85626 | 2025-09-22 03:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c5809ad-05f6-34e1-8b07-67cba1cf1756 | -21.63647 | -43.65299 | 2025-09-22 03:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 02ff53f2-08fd-3771-aa35-97b875fa5c35 | -20.73429 | -40.65693 | 2025-09-22 03:51:00 | NOAA-21 | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d328e42e-ef87-3854-9d18-a17c6ad7c0d4 | -19.81591 | -46.39779 | 2025-09-22 03:51:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82b7d557-f768-37f9-bc47-79b411b23497 | -19.43427 | -44.82135 | 2025-09-22 03:51:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1382e335-a1b6-3009-abac-7fa0ff9b3f74 | -14.44045 | -46.52053 | 2025-09-22 03:51:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 400eb61a-425c-33ab-8b56-b9c18597fbd1 | -18.98414 | -44.2285 | 2025-09-22 03:51:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4a024ee-9755-370d-aa0d-70a5395846e5 | -19.57835 | -41.65408 | 2025-09-22 03:51:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f17a3c99-639e-3bf5-887b-dedb2dd28ad7 | -15.16137 | -49.58264 | 2025-09-22 03:51:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| bbe91f6f-b8b5-3bd9-a209-d400de102669 | -14.96998 | -44.41333 | 2025-09-22 03:51:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7cb84ed-0590-38ee-b07a-3f3ae6c7a6f2 | -18.5488 | -43.84965 | 2025-09-22 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| babcc37a-4bae-392e-9631-48277da058bb | -17.42553 | -42.37293 | 2025-09-22 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f7ae43d6-a7ea-3b25-92b9-bdcc09531376 | -19.97891 | -46.85142 | 2025-09-22 03:51:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 143e1c4a-2998-3ef3-b185-c25fca6e838e | -18.37826 | -46.47059 | 2025-09-22 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 2b89efc2-ab33-3f33-abad-267cb91bd165 | -14.34464 | -47.79119 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2575ada-14f2-39a2-82b7-b7eed0ca164f | -14.35044 | -47.78905 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b24bf34-b062-3f86-9143-b688628d6fb6 | -17.06314 | -44.90117 | 2025-09-22 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2633666e-17e1-362e-b603-9848b67bee27 | -21.36751 | -46.17263 | 2025-09-22 03:51:00 | NOAA-21 | AREADO | MINAS GERAIS | Brasil | 3104304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54f4423c-da42-3f17-9e0c-830512d23d71 | -19.81163 | -46.39695 | 2025-09-22 03:51:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b0aa5fd-bbe8-3d50-80a8-1b569b277fbd | -18.87981 | -43.24784 | 2025-09-22 03:51:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 81616b1b-4e9e-3f9f-86ac-019c426bad92 | -18.39808 | -42.85576 | 2025-09-22 03:51:00 | NOAA-21 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d5c50ca3-82c9-35d7-b09b-cce8f45737e8 | -19.14042 | -42.662 | 2025-09-22 03:51:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9cf758b4-ef72-35ff-8ff4-d9d6694a3a93 | -14.33432 | -47.78894 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 469b2380-b0d3-3816-9036-e43e19c87b77 | -20.19264 | -44.6183 | 2025-09-22 03:51:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e46001e2-82e1-3201-94f1-9c254358ac37 | -17.6803 | -44.08101 | 2025-09-22 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 159f6f68-3bbb-36be-b676-61fc694a7282 | -14.97889 | -44.41107 | 2025-09-22 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8186c00e-a2f8-326a-a1ef-76b4d8391b2f | -19.03263 | -44.65071 | 2025-09-22 03:51:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bf2a1fb-96a9-3245-86d7-066a923854e4 | -17.07533 | -43.191 | 2025-09-22 03:51:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 958c48b8-69bd-302f-826f-fd194381a951 | -14.98301 | -44.41175 | 2025-09-22 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d906df-d0e2-3146-b742-352de971bacc | -16.73631 | -43.01953 | 2025-09-22 03:51:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8bfa4d8-a9f5-34a9-975a-ada31864ca5a | -19.91936 | -42.36812 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5378ec5a-e691-3b29-baa6-fccbcaeee502 | -19.92281 | -42.36876 | 2025-09-22 03:51:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8c7fa01d-5e0a-3dec-925d-22523469da1f | -14.33115 | -47.7994 | 2025-09-22 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b26e44b3-2b33-3b44-a5a5-cccb1fad7446 | -20.66981 | -42.2838 | 2025-09-22 03:51:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 15837573-f250-30e9-a6a4-129d6c490d4e | -21.64415 | -47.48761 | 2025-09-22 03:51:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b91ab6d7-9ec7-366a-9ce2-4340f0c7bac1 | -15.93622 | -42.19143 | 2025-09-22 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 43b5bf24-0d86-351e-9ff4-94179372ae47 | -21.62732 | -47.47947 | 2025-09-22 03:51:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2bf24774-450a-37ee-a9d3-43afee7901de | -18.37911 | -46.46611 | 2025-09-22 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 8f63ca56-05ce-3c4e-96d5-2d11f75a6ef2 | -20.18686 | -44.62817 | 2025-09-22 03:51:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f25a5f4-c8d1-33c0-b2d5-9029b684858d | -21.64848 | -47.48906 | 2025-09-22 03:51:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83f76453-7cc3-3553-9377-c4b17aa01156 | -19.88041 | -42.45786 | 2025-09-22 03:51:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ad6b21f-03a5-36ca-8591-5dea2ca745c4 | -21.63186 | -47.47988 | 2025-09-22 03:51:00 | NOAA-21 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c0684a3-9d2c-33b7-81ae-06d28f4afa77 | -16.7355 | -43.02407 | 2025-09-22 03:51:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3db0238-0bde-37f9-b94e-66d2df46862b | -20.87651 | -42.80688 | 2025-09-22 03:51:00 | NOAA-21 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6f3e7391-1902-346f-a65a-6614cd5dd321 | -17.97556 | -43.08159 | 2025-09-22 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9b909a32-467e-3bbf-9c1c-ec28b4b553c5 | -19.57496 | -41.6535 | 2025-09-22 03:51:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README13.md)
