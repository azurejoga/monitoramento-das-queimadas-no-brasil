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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee8276c-4000-3312-84e0-bd357b6d8d5a | -2.7151 | -57.5109 | 2026-10-02 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 51e283ee-98a8-316c-9af8-160231871497 | -1.2082 | -49.2964 | 2026-10-02 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 46f77799-a7df-3aae-ae83-d0f7fa12a6c4 | 3.4341 | -51.2808 | 2026-10-02 15:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 5d4f5d8a-3461-3078-99b0-21d832834c5c | -1.1351 | -48.8501 | 2026-10-02 15:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 6f018cd5-de56-3a67-b580-4e63837eaf8d | -2.7151 | -57.5303 | 2026-10-02 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| aee3aa77-7fca-3e46-9f21-644ae0d91957 | -1.6036 | -54.7544 | 2026-10-02 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 63269fb3-f46a-38ed-a2fe-f55b98fce882 | -1.3192 | -49.1249 | 2026-10-02 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 74f61c94-73c9-340b-8877-08a8cd6ae38e | -1.1897 | -49.3179 | 2026-10-02 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| bc604ccf-b45c-33c6-b5b6-5cfa0863ca71 | -1.2082 | -49.2752 | 2026-10-02 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| bc38702c-402b-3934-907e-574b336d4688 | -1.3009 | -49.04 | 2026-10-02 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6f0abffb-9d0a-3778-951a-5ecaf72ac668 | -1.6219 | -54.7542 | 2026-10-02 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f17e953f-d4c1-3a55-bf13-1f8548c37baf | -1.4672 | -48.931 | 2026-10-02 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c6045ad0-01b2-3ae9-a4cb-cebb53e1b35c | -1.3193 | -49.061 | 2026-10-02 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 66b24c5d-4e02-3c5c-943e-41785049cd82 | -1.1713 | -49.2969 | 2026-10-02 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5db1cc40-63e5-30f3-8870-9788ece73921 | -1.3009 | -49.04 | 2026-10-02 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3f88b11b-e932-32f0-8164-c89f864c9026 | -1.1166 | -48.8504 | 2026-10-02 15:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f3cc86be-692a-353a-ac93-a9265bd9c58f | -1.3192 | -49.1249 | 2026-10-02 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8ddca348-ce5e-3006-830f-095ca7663236 | -1.1351 | -48.8501 | 2026-10-02 15:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| c2f4b5e7-afb9-313d-9fcf-81917ed827a5 | -1.4303 | -48.9102 | 2026-10-02 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 29f8033d-f27c-31ac-b407-2e46faaf32cb | -1.4303 | -48.9316 | 2026-10-02 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ccb3a5e5-7891-35f1-aa4c-933d8d82d73a | 2.5502 | -50.9526 | 2026-10-02 15:40:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 110.0 |
| f0b8f2d9-c0a6-3e0f-9e6a-4ab646f9886d | 1.8037 | -55.6051 | 2026-10-02 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2d08c19d-6ab4-3c2e-b845-2333988ec38c | -0.8584 | -48.6392 | 2026-10-02 15:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 9d3919f9-9c05-35cd-869d-05addea978d8 | -1.1715 | -49.1481 | 2026-10-02 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 02dbc769-c1ea-31c5-8f21-7e93f2df6257 | -1.4303 | -48.9102 | 2026-10-02 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 63148eb9-5021-3b6f-acd8-0e9df39cfdd2 | -1.3009 | -49.04 | 2026-10-02 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 18bb24bf-6395-339d-b8ff-1a2056595c9e | 1.8037 | -55.6051 | 2026-10-02 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 200.7 |
| ce774a71-d7e1-3332-8c5a-19efba4a59ea | -1.1351 | -48.8501 | 2026-10-02 15:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 32fd902c-7f6b-3eac-9721-c62a2c16fd17 | -1.4672 | -48.9097 | 2026-10-02 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a09295f0-9597-3dfc-904e-83ac37647e4c | -1.4672 | -48.931 | 2026-10-02 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 2fbb430c-eddb-3833-86a1-7333084cccff | -1.1715 | -49.1481 | 2026-10-02 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 74a012e6-8320-3793-9e84-19d40932a56d | -1.4487 | -48.9313 | 2026-10-02 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 28bcf81d-7c9d-3dc6-81d2-473e5f1b3fb3 | -16.42408 | -40.2512 | 2026-10-02 15:52:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| dd73c01d-4091-3b74-9fae-2f173a7d8776 | -14.78608 | -41.56314 | 2026-10-02 15:52:00 | NOAA-21 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 61bd948e-28f5-31e6-8d28-30b34605cd83 | -15.97542 | -41.44143 | 2026-10-02 15:52:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| b5df1f0f-1d01-3db8-aec6-580d523b03a7 | -13.87594 | -43.63989 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 4785bf19-59d9-36f2-826f-c9827100b51e | -15.17033 | -43.66999 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 17d2bab1-170d-3b58-bd61-051354bc3a3d | -15.3328 | -41.22554 | 2026-10-02 15:52:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| efcdf647-62c8-3be2-8fd6-5fa70936c5b7 | -16.15766 | -43.6305 | 2026-10-02 15:52:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a8ed1e6b-d36c-383d-93bf-4ac6684c9b8c | -16.42032 | -40.25585 | 2026-10-02 15:52:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| b06d73bd-1daf-317a-86ba-f76a6082a8f3 | -15.86631 | -44.28726 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| b1efdeda-5e36-3aaa-9617-e2c40bd21b47 | -15.91503 | -46.01156 | 2026-10-02 15:52:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 64d6e342-0c2c-371d-933a-8d771fff75a8 | -15.84335 | -38.95732 | 2026-10-02 15:52:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 7897eeef-8aa7-33e4-b10a-72f420ba7815 | -13.88188 | -43.64562 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 330.9 |
| ce0b789f-e062-3307-9de5-4dc1947d8bfb | -13.87112 | -43.64367 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| f90acc4c-697a-3230-b015-0c165ef05a74 | -13.39479 | -43.68746 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9c52aee1-8fa1-3534-bfc3-8395fdcc1458 | -15.13346 | -43.57958 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.8 |
| c2a1b761-f4a9-32d5-a513-c531badbd3ef | -14.262 | -42.11092 | 2026-10-02 15:52:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 99a8fdf3-d7e6-31da-94df-39d442f6d9e7 | -16.98501 | -45.47068 | 2026-10-02 15:52:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 62ba154d-095d-3ca7-98bd-6f36f8546f18 | -15.48161 | -40.76777 | 2026-10-02 15:52:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d702e60e-27c8-3dba-a801-011e0caabb96 | -13.79369 | -45.25618 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff4b3798-8175-357f-8f59-5670294e7cc1 | -15.85104 | -44.29542 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 50ef2f33-7bc1-321c-ab3e-8aa94598cbe1 | -13.95537 | -42.43024 | 2026-10-02 15:52:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d0885b13-1837-3180-beb9-d59d3d7fb26b | -13.88076 | -43.63613 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| daf336d2-2956-3271-87e9-f16e004809a5 | -13.88113 | -43.63929 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| dca04499-b3f8-3816-a64f-1a90d2f94d70 | -13.40034 | -43.68996 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6563008c-0862-39fc-b8b8-8a5805397c9e | -14.35329 | -44.72116 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0578bd45-adad-3b3c-9e0b-a1c2c869345d | -14.49441 | -39.54367 | 2026-10-02 15:52:00 | NOAA-21 | ITAPITANGA | BAHIA | Brasil | 2916609 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 7967f20b-e6bd-3bad-b69e-22ed8d061f66 | -15.77562 | -43.65297 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| ddb75608-5042-3e0a-81a2-03f864aa0868 | -14.53711 | -41.31248 | 2026-10-02 15:52:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 18.9 |
| bec2767d-4aec-332c-be2a-89674281a92c | -17.43695 | -43.6455 | 2026-10-02 15:52:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7787863e-5d38-3b21-adc5-7d82980c9bfb | -14.72416 | -40.90593 | 2026-10-02 15:52:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 649baff2-132d-3594-8cbf-e6aefe78bb40 | -16.48844 | -43.15502 | 2026-10-02 15:52:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d3bffe9-873f-319f-a617-d6cae6c24673 | -13.39517 | -43.69062 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5fbcd730-dd3b-33b3-8bbf-3ce6384a86d0 | -17.74729 | -42.22106 | 2026-10-02 15:52:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e1807af2-4228-301c-a7ee-0e5ecf3e7853 | -15.08311 | -41.16455 | 2026-10-02 15:52:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 128.3 |
| a0d10607-8956-38ee-998e-5fca7b0ed766 | -13.83062 | -45.26461 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9781196-3a4a-3741-a3b6-516165a567fe | -13.7971 | -45.23512 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8943e8bf-782f-36d8-b784-a68045a1e2f2 | -14.47682 | -40.71906 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| acc967f5-6f30-36d0-a6c6-d586e6aeee9f | -17.15792 | -43.04291 | 2026-10-02 15:52:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 95869466-1779-327c-9353-329380d9bc2b | -14.66318 | -41.62334 | 2026-10-02 15:52:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 80d75530-5429-3e21-9ac3-2351d31d1f3f | -14.47628 | -40.71483 | 2026-10-02 15:52:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 41a53d67-a9fc-3c18-902a-ccb12386ebd8 | -13.74942 | -41.10687 | 2026-10-02 15:52:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| d4af5c39-092d-3bab-b207-89dbd8375bee | -13.82485 | -45.26523 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9b0eff1-789a-3b7a-b7b3-72ac1c516c2c | -13.8038 | -45.24265 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| dab1d1a3-50d9-3d19-ae5a-041ff32f5120 | -14.44303 | -42.23996 | 2026-10-02 15:52:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f444e8b6-c8e0-3060-89bd-c84428a53286 | -14.14977 | -40.65223 | 2026-10-02 15:52:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e9b49508-11a8-3bbb-819a-2bc02d4d916f | -14.36498 | -44.72401 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8fcb2e1e-b1bd-37eb-acd4-7f061e0b4354 | -15.77489 | -43.64621 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 79dbd0c1-17af-3db3-905a-cb990e9a18a7 | -16.84828 | -41.786 | 2026-10-02 15:52:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 42449463-d0a0-31e9-a636-f78389939f21 | -14.02683 | -43.83502 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db803163-81b9-37cb-bde1-3f97afa47d5b | -17.30435 | -42.31421 | 2026-10-02 15:52:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 4053d4ad-a148-375f-8ff2-278aff9512b1 | -15.78198 | -43.64861 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 07e259da-53a3-33a2-93a0-897dbe720d3d | -14.70749 | -44.69589 | 2026-10-02 15:52:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6cb25c0a-8fe2-3589-9c7b-60bfd3e7b328 | -13.87668 | -43.64623 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 330.9 |
| b547b436-7571-3b1a-9862-72495b778ef5 | -13.39556 | -43.69379 | 2026-10-02 15:52:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 204d5807-6097-3289-907d-5644f13a719f | -15.17071 | -43.67335 | 2026-10-02 15:52:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 015d6f41-66f1-36cc-9169-249dc516012a | -15.27085 | -39.60759 | 2026-10-02 15:52:00 | NOAA-21 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 72bc4f12-04c1-3fee-8a36-ea1e65e94a07 | -14.33219 | -44.73566 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| afd50952-9262-3d6b-b8aa-45a36f2baba8 | -15.77664 | -43.64906 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| e0768f6c-caa3-3fcd-b788-3fbc904e0c69 | -15.14005 | -41.82614 | 2026-10-02 15:52:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 7141631e-1d04-382f-a574-f6c2cb4da3eb | -15.13985 | -44.05133 | 2026-10-02 15:52:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9d4309c0-d6f2-329b-9916-8bb1dc701c6c | -15.01761 | -45.17363 | 2026-10-02 15:52:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 86f31edb-697b-3a1d-a3cf-f6463f89fdc3 | -15.85618 | -44.29106 | 2026-10-02 15:52:00 | NOAA-21 | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1d2824c4-8713-34b2-96b6-de4570c3562c | -14.36541 | -44.72774 | 2026-10-02 15:52:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2b5dac51-74d4-3ca0-959b-d933c359aac7 | -13.87521 | -43.63361 | 2026-10-02 15:52:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6ff880cd-2ae7-322f-8c77-184805a8a8c0 | -14.276 | -40.76348 | 2026-10-02 15:52:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe70b769-4da4-3ec6-9fb1-9d8d2a22141e | -16.91198 | -43.22758 | 2026-10-02 15:52:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 23c54e15-7c9b-3f1b-a659-43e4a96b54cd | -13.83833 | -45.23842 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ca075374-17f6-33af-93f5-2ee62339bdbe | -13.79323 | -45.25217 | 2026-10-02 15:52:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README91.md)
