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
| 378811aa-2601-3415-97ef-0a061fcfb2c1 | -15.21844 | -47.92089 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eab37c6e-91ab-375c-996a-a74be7891bc1 | -19.63287 | -46.1361 | 2025-10-25 03:32:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| acd1ecdd-ad6a-3e2d-b671-5077e176af47 | -15.56573 | -45.94252 | 2025-10-25 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b97bcae0-5527-3665-9cb6-5bef3dfa41e4 | -15.98622 | -43.90616 | 2025-10-25 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2b26d89-fda0-367d-83b8-addf45820cb7 | -13.34877 | -47.40536 | 2025-10-25 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce1d4983-e250-3135-9c07-0cd5b63e1cda | -17.38129 | -45.50373 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e51c8336-dabb-3d9b-9096-40dabdcbe80d | -14.74456 | -46.59832 | 2025-10-25 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c66722c4-3a9e-3db8-8585-740cf4755749 | -13.94476 | -43.81859 | 2025-10-25 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c517ae00-e807-3e2d-8b3f-89bdc0204be6 | -12.07014 | -46.39595 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f57107ef-fdd6-30f9-a4ea-c2ae406ddf5c | -13.32005 | -42.41986 | 2025-10-25 03:32:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d1be66ee-d88b-3984-9ee8-864ecef9aa76 | -13.44997 | -44.07146 | 2025-10-25 03:32:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ad7afe-f11c-3083-b7a6-26e108a4a492 | -12.08205 | -46.40586 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8de6215-f5dc-360f-a6b6-fa1d64a781bc | -14.9395 | -48.13135 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4215a9b7-3c02-36e1-9eca-03ba1b6f45d3 | -15.24404 | -47.93572 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9a7cbc2-b607-363c-b9b0-3522f9022cde | -15.30274 | -42.9643 | 2025-10-25 03:32:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c3f235a-9d65-37b0-b61c-539e30fa192e | -17.41999 | -46.87941 | 2025-10-25 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7545cf1-df5d-3d6d-a75b-d45ee1848493 | -14.89897 | -47.86803 | 2025-10-25 03:32:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 488020ba-e201-3caf-add9-580eef7f47e3 | -12.77954 | -47.381 | 2025-10-25 03:32:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5446ef9-450f-348d-8c95-bfb8f2f309cb | -14.15369 | -44.31687 | 2025-10-25 03:32:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31c7912c-6f14-34a5-99db-67cf7e60746c | -14.87366 | -48.08642 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 547eaf43-155a-34cd-a81c-ff494a31479f | -13.94374 | -43.81781 | 2025-10-25 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8162896-d73e-3586-ab37-59444876789f | -12.63925 | -44.3033 | 2025-10-25 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51cfd853-51fa-3b9c-9f5d-de32ca9b53ad | -15.23169 | -47.92896 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 38de1bbf-4800-39dc-b40b-cd083c10d9f7 | -19.62815 | -46.13158 | 2025-10-25 03:32:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6c354756-3c6e-33d3-b4b8-2056f71c9d7a | -14.86831 | -48.0774 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6f49a580-39ae-3e9b-a258-3f87d538f7e5 | -17.37729 | -45.49437 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7129fb06-b30a-3122-9154-85772dcab72b | -17.37761 | -45.49355 | 2025-10-25 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19ffd069-b4db-39b7-9ee7-9a56f0676d87 | -15.20327 | -43.78211 | 2025-10-25 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba68819d-5f3c-3622-ae5b-e03ba0c0c359 | -12.08619 | -46.41965 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| fc959b62-81d1-3298-8f6b-17248d8b763f | -14.87179 | -48.0949 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 220cdb79-de90-390e-9b22-2d4b9fb35372 | -18.78909 | -48.04075 | 2025-10-25 03:32:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 970916b2-dd95-35ce-869b-55a192dc8cce | -14.86832 | -48.09878 | 2025-10-25 03:32:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2a3cb949-16d6-3a09-9a3d-cf57b7e8491e | -17.46922 | -45.99391 | 2025-10-25 03:32:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89b7ce49-6c2a-3a1f-9ac3-17798743ebe0 | -14.20351 | -47.30397 | 2025-10-25 03:32:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68d0ef5e-4719-325a-8f5b-076dbe53b60a | -12.04699 | -46.40654 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d02248bb-1eaf-334b-8ea7-9b9b9bbc56b4 | -14.72093 | -46.61379 | 2025-10-25 03:32:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7362318-c2eb-3a1a-b664-a6e7a436b25a | -15.24542 | -47.93235 | 2025-10-25 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87fce27a-192a-3e80-8b76-c5900d8c9829 | -16.58658 | -43.50253 | 2025-10-25 03:32:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 555d6fba-e723-319e-9c50-7990d45b8624 | -14.44292 | -48.07169 | 2025-10-25 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfcf6622-1f9d-338a-9b9b-0d03b32b4202 | -16.2197 | -46.4789 | 2025-10-25 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce85e042-ab22-3537-a717-46bf20ecc5be | -13.31496 | -42.41861 | 2025-10-25 03:32:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d6ae082c-5c8c-3c16-9dbc-7a99765653de | -12.06222 | -46.40049 | 2025-10-25 03:32:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 419ed032-b323-3b3c-870c-4afdc037b51d | -22.28571 | -46.82903 | 2025-10-25 03:34:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5072e885-3d8d-3497-a54a-dbc83eb4aa1a | -24.30599 | -49.42396 | 2025-10-25 03:34:00 | NOAA-21 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6647522a-fd15-3b4c-be96-9b9f95c4b946 | -21.92105 | -46.5093 | 2025-10-25 03:34:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5deb0ac4-7260-30c1-8ec7-610f0661b64b | -19.76999 | -48.29403 | 2025-10-25 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8431fcab-91dc-364e-9081-75a23be49050 | -20.44046 | -46.58784 | 2025-10-25 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a860696a-291e-3bdd-ba23-e337a622935f | -19.33465 | -49.09048 | 2025-10-25 03:34:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f2967bf9-4d35-3dcb-957a-15c8788a199f | -23.76646 | -50.74463 | 2025-10-25 03:34:00 | NOAA-21 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0dd75430-b8f5-3879-b065-0dddf569b103 | -19.87673 | -46.97733 | 2025-10-25 03:34:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d02bcbc-26bb-322a-8322-e903428ed174 | -21.92404 | -46.52227 | 2025-10-25 03:34:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 1fafac6c-bf04-3b76-aeca-f41bb453ad4e | -19.76216 | -48.29819 | 2025-10-25 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d532c918-9c87-3bfb-a375-14abd13e2793 | -19.87224 | -48.32159 | 2025-10-25 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4f54d9ff-17bc-3abc-9314-98eb4468050a | -21.20515 | -46.72145 | 2025-10-25 03:34:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 788692d9-1917-3c16-9392-2def2db0855b | -21.92497 | -46.51815 | 2025-10-25 03:34:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 76ae7acc-ee55-37f2-9f32-6a583ec7733a | -20.82734 | -45.00109 | 2025-10-25 03:34:00 | NOAA-21 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f640bfad-35b0-30ca-8f8e-ea87203909b3 | -19.87552 | -46.98252 | 2025-10-25 03:34:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e21535e-57ef-30eb-a626-a271a7a4d64e | -21.2062 | -46.71684 | 2025-10-25 03:34:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbd81557-172c-3529-b928-99db24b7bd38 | -20.70046 | -44.25579 | 2025-10-25 03:34:00 | NOAA-21 | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 95c723d3-af35-3329-b62e-1169ae776ebb | -20.44145 | -46.58351 | 2025-10-25 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94f001f3-35d6-3807-a741-f0944a77ad7e | -22.36025 | -43.36926 | 2025-10-25 03:34:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 539f8296-a794-36b5-ab4d-ca5ddd1b6b28 | -19.88218 | -45.83099 | 2025-10-25 03:34:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b068ba8-f20c-3212-9cf2-49a2164fa0aa | -19.32791 | -49.08853 | 2025-10-25 03:34:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d6d2718-a4cb-3e72-a7ba-1de455040210 | -20.76244 | -43.22718 | 2025-10-25 03:34:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 539467f2-7e8c-3dd9-9324-7f61e605faed | -20.70389 | -44.25937 | 2025-10-25 03:34:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a18dc8ba-6763-3951-8640-a5e9c4bc5d7a | -19.76361 | -48.29206 | 2025-10-25 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a3ec9956-e513-3a8d-a87e-8b7f18c9bc62 | -20.70458 | -44.25618 | 2025-10-25 03:34:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c22a80b2-60de-3a16-95ff-5ea7cde0f696 | -21.37292 | -45.03167 | 2025-10-25 03:34:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cec65fa7-7ca9-3d5b-8e08-a54254cf9952 | -22.18572 | -44.13139 | 2025-10-25 03:34:00 | NOAA-21 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9f904b10-3cd3-3bae-9b36-9f92b0b9acae | -21.91654 | -46.52925 | 2025-10-25 03:34:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 216a2c7e-8f59-3cb8-a80e-3465708fe8a5 | -20.38518 | -45.91774 | 2025-10-25 03:34:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d6f178-53ac-31b1-9666-db83a49bd394 | -24.8094 | -50.22748 | 2025-10-25 03:34:00 | NOAA-21 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ca3f2d27-9040-3380-890a-05f8f673c0c7 | -20.76139 | -43.23232 | 2025-10-25 03:34:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 27bb1c35-11d8-31f8-8e0e-c0f694ea5a4b | -24.8077 | -50.22835 | 2025-10-25 03:34:00 | NOAA-21 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f9827d8f-31e9-3355-af5f-540d77894041 | -21.92196 | -46.50532 | 2025-10-25 03:34:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b5a866aa-e116-3e21-9292-7f4a685e42d5 | -19.75855 | -48.2845 | 2025-10-25 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1e128878-2c61-3a94-b114-e97467a70850 | -21.91748 | -46.52508 | 2025-10-25 03:34:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3dd04baf-4401-3fa1-9bd8-070f5231fe97 | -19.85361 | -49.06673 | 2025-10-25 03:34:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6409b34e-93e3-3276-b023-2d59a3750ec8 | -19.75714 | -48.29048 | 2025-10-25 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 027fa321-ce77-39a8-88a7-09bb6737873a | -21.89003 | -45.26936 | 2025-10-25 03:34:00 | NOAA-21 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| adbeea68-8e87-398b-9065-bb4016022438 | -20.39076 | -45.91903 | 2025-10-25 03:34:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54a18dfc-0b7c-3134-beac-704881253a0d | -19.765 | -48.28616 | 2025-10-25 03:34:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 41db6937-7f09-39bd-b743-2ef1e3586e2f | -21.92304 | -46.52668 | 2025-10-25 03:34:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| bd80b0e2-4d84-35e0-bd23-8a98e8c30401 | -19.84696 | -49.06467 | 2025-10-25 03:34:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9de2d765-5d54-3daf-928a-63ed71bb8929 | -19.87488 | -46.97928 | 2025-10-25 03:34:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a2e159c1-704b-3dd1-9cd8-1c28ba6a12df | -19.88133 | -45.83488 | 2025-10-25 03:34:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43e91d9a-e6e0-322d-91e5-17116100dd60 | -21.50109 | -44.26108 | 2025-10-25 03:34:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 08fe0bdc-0783-3320-bf90-5b66ebeac775 | -21.88481 | -45.26817 | 2025-10-25 03:34:00 | NOAA-21 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 60a61100-7f58-3da6-b631-6d2f49e9ec12 | -20.6998 | -44.25897 | 2025-10-25 03:34:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dc75af41-2166-3806-a290-c5fa6c683396 | -21.37218 | -45.03508 | 2025-10-25 03:34:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ba310cf6-cb7b-32c8-baa5-a5cd4664b0a2 | -23.3879 | -51.13161 | 2025-10-25 03:34:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4b8f98cd-3bfb-3c27-93e3-e3f54d72114d | -21.07071 | -43.63589 | 2025-10-25 03:34:00 | NOAA-21 | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| ad27994e-119d-3d90-9bb3-ba49e38eddb1 | -20.43489 | -46.58545 | 2025-10-25 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f91d0cf4-8246-3014-a066-3db1094a9128 | -23.89037 | -51.2432 | 2025-10-25 03:34:00 | NOAA-21 | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7b6e07fd-1753-301f-b3d6-a4c7eb4fa9a7 | -20.83256 | -45.00236 | 2025-10-25 03:34:00 | NOAA-21 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 803e956a-bee5-34ce-abe8-fb4a7d6a569a | -23.38996 | -51.12378 | 2025-10-25 03:34:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d17763fe-8b56-3dd1-aac0-f2faded18aa6 | -26.17059 | -51.74092 | 2025-10-25 03:36:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e1b8ba95-ef79-3061-9903-7c61e192992e | -26.17049 | -51.74092 | 2025-10-25 03:36:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 52de1114-b6f6-3449-a765-3748a88efa34 | -26.1726 | -51.73339 | 2025-10-25 03:36:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0c92b4e6-fb33-3d77-b132-17052ac73f84 | -26.17253 | -51.73342 | 2025-10-25 03:36:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |


[Clique aqui para ver as próximas entradas](README13.md)
