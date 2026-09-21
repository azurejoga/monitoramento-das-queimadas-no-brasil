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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da328327-0df3-3952-b608-8284aa8b1c7f | -6.2831 | -59.9394 | 2026-09-21 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f5cc6278-8b4a-3686-9a75-6c4636f4a178 | -6.8263 | -55.5421 | 2026-09-21 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 3eaf2bce-7e7c-3e20-b866-62a39bed93ff | -7.8632 | -70.5959 | 2026-09-21 15:50:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 122.2 |
| db84e7dd-a09c-30e0-b5d3-682684fb3e2d | -6.3011 | -60.0154 | 2026-09-21 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 137e4849-a5ff-3808-ba3b-51e3086dd5c0 | 1.2609 | -50.9344 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ff4cd457-9ab9-3d58-94f1-39b7db7eca1f | -10.6881 | -50.7297 | 2026-09-21 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| f760d282-6786-398f-be65-a5cbe18a8348 | -3.5893 | -59.0773 | 2026-09-21 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b83a187f-75c6-3d8f-806f-54716e2cd144 | -10.6889 | -50.6658 | 2026-09-21 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2c98c777-9c89-3129-b25e-64c97de8ffbc | -3.3504 | -59.4465 | 2026-09-21 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 28dd6b72-d0c2-371e-acf9-9a4d2ac4328b | -2.9157 | -57.7983 | 2026-09-21 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 129.2 |
| aa5ac933-82c1-34f4-ae48-410bd04574f2 | 1.2978 | -50.8715 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 46ffd069-eea0-32a7-a0ac-fee239bc58ab | -6.8448 | -55.5411 | 2026-09-21 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 897488d3-03f2-36b2-a53b-e3064623852c | -6.4671 | -59.9711 | 2026-09-21 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 88501188-e6b3-3441-96d3-61ef575b2597 | -5.2168 | -56.1096 | 2026-09-21 15:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 189d37fc-e6fe-3291-89b0-5503afe5574e | -2.9526 | -57.7006 | 2026-09-21 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0373aad6-1234-39e1-aecf-b0566e21451f | -8.7706 | -45.8567 | 2026-09-21 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 58ffa61b-a75f-3353-a47a-1a4c1440cdc8 | -1.2267 | -49.2537 | 2026-09-21 15:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0a23d83f-8ccc-3f0c-adec-cda94c2473c1 | 1.3351 | -50.6001 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 55ed084d-81cf-3fef-8434-69c7c33b2942 | -10.3916 | -50.2916 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| d4b02ee8-0ec2-33dd-8fb5-7542c2894d47 | -10.6697 | -50.6891 | 2026-09-21 15:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 233fcb88-e911-3161-95d1-64e3fa455496 | -17.95798 | -44.0124 | 2026-09-21 15:58:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c1d443b-bbc0-3f6d-9949-095d41d5ced0 | -14.64662 | -41.28514 | 2026-09-21 15:58:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| c6de84ac-62ae-3518-b836-e685c0df22a8 | -14.10787 | -40.72509 | 2026-09-21 15:58:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 7e0755cf-56b9-34fe-ab10-db7de5f7c909 | -14.43854 | -41.28101 | 2026-09-21 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6ba0700f-9585-3499-aab3-e8fc338d0657 | -16.03062 | -44.78706 | 2026-09-21 15:58:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7aa05bba-ce2a-3001-a2af-4257fd6ffef0 | -17.95694 | -44.01051 | 2026-09-21 15:58:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 00211b45-40ff-3d17-a491-85cd9766a4c4 | -19.23728 | -40.08911 | 2026-09-21 15:58:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b9552ae4-aded-3b90-9ba1-4cdac3cc07f7 | -19.12234 | -46.59948 | 2026-09-21 15:58:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 39.1 |
| bb200c78-0aef-3ac0-8acd-68c55338f8a1 | -16.23986 | -41.3854 | 2026-09-21 15:58:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 5d5334b2-b948-3f4d-bbf5-74d33ed1264b | -15.83976 | -41.62296 | 2026-09-21 15:58:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| ffbe7434-d47b-333b-b83a-536857fd2a1c | -16.18474 | -40.66892 | 2026-09-21 15:58:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| 38d57a3c-8ec2-3201-bc6f-8c4ee07bb37e | -16.88649 | -39.15498 | 2026-09-21 15:58:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 1f1bb9ae-4a39-3baa-949e-3d395825c761 | -17.08009 | -46.16386 | 2026-09-21 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 28b6ee99-9c99-324f-8659-1c00f29d274e | -14.9032 | -41.09929 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 70a6094e-1a43-32f6-8a5f-c03126f2d66b | -15.42894 | -41.24218 | 2026-09-21 15:58:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0d0afc16-0791-30d6-b89c-d2dbfc86d1eb | -16.44132 | -42.25258 | 2026-09-21 15:58:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c79d3823-b9df-3129-a4ff-add12fdffa65 | -14.62882 | -41.40547 | 2026-09-21 15:58:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 6e4f2286-c3d1-3eb2-8ca1-71c71f426873 | -15.26267 | -47.60622 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| d62651e3-dca6-32f8-b6d4-1dbf95b2436e | -15.46107 | -48.41218 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0a72c86e-ad77-37e3-a14d-07cda04eaa97 | -16.57115 | -43.38802 | 2026-09-21 15:58:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| dc4a8a67-107e-3971-a464-9caf3f606e16 | -16.24368 | -40.41434 | 2026-09-21 15:58:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 56bf48c1-9c3e-3965-87d5-65f6a705280e | -15.25594 | -47.60132 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 745b0737-22a4-3db2-9aa5-71d67e86e68e | -18.9386 | -40.02788 | 2026-09-21 15:58:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| ba906d14-c12f-3b5d-ad53-bf8217cf2599 | -14.96226 | -39.70947 | 2026-09-21 15:58:00 | NOAA-21 | FLORESTA AZUL | BAHIA | Brasil | 2911006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 875d97e5-d267-3d12-be08-86117337ffd1 | -14.67686 | -45.68506 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d1ab9edb-f0e7-30cb-829d-1008e23ad497 | -18.86115 | -44.10346 | 2026-09-21 15:58:00 | NOAA-21 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8d16e7c1-9840-36b7-896c-fe7a4de4f789 | -15.16277 | -49.17227 | 2026-09-21 15:58:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d8c66a02-8a37-3451-b6d0-c48fee6b6cba | -14.77547 | -40.71228 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 2c8755c0-c9d5-32ce-b811-cfec2323272b | -14.49326 | -40.30037 | 2026-09-21 15:58:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 85e610c8-6597-30a7-ba92-79840591672e | -16.88283 | -39.1555 | 2026-09-21 15:58:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 36.6 |
| eef485e9-4c13-3280-87fc-71df42afe734 | -16.47316 | -46.09687 | 2026-09-21 15:58:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 666fa6a5-493d-3b62-9877-3199756304f7 | -19.43155 | -41.08426 | 2026-09-21 15:58:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 822b4e08-b6e4-3bf8-a913-65c348dec537 | -17.08053 | -46.168 | 2026-09-21 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 103f0849-a83f-3d42-a77f-aaca91d5a184 | -16.79505 | -41.16517 | 2026-09-21 15:58:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 87ca979a-c3f8-34e8-86e8-a509578eed9f | -17.31716 | -39.62846 | 2026-09-21 15:58:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f3758ee0-b1aa-3d4b-979b-5c1393af2dfe | -14.66441 | -45.67208 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 5d580dd0-b609-3b37-9c1b-e784e6ce8301 | -17.85983 | -44.41166 | 2026-09-21 15:58:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 235069f4-ae6a-3c21-bfaa-14375f97eab7 | -14.10536 | -40.72244 | 2026-09-21 15:58:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 00da1e14-1500-322f-a242-bff2cec67052 | -18.8905 | -46.84053 | 2026-09-21 15:58:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ea369716-7257-3c49-aec5-5f2e18b27898 | -17.85946 | -44.40841 | 2026-09-21 15:58:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c628b9c2-c848-3d05-b49e-19ecc6a1f667 | -16.37996 | -45.10645 | 2026-09-21 15:58:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c9b60d28-f5de-3be9-a862-cdc15ef0153c | -19.59301 | -45.01312 | 2026-09-21 15:58:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 367c621e-a2e0-3597-8178-315563ed235e | -14.81853 | -43.91982 | 2026-09-21 15:58:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 0b3f9852-2164-3fb6-9502-428014bee7af | -14.79488 | -41.12637 | 2026-09-21 15:58:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1701fd2a-4f84-3a81-93cf-013df7fefed3 | -17.83968 | -42.6153 | 2026-09-21 15:58:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| a37d0dcc-8af6-3f91-9cf8-ec06aa870cfa | -14.86849 | -41.02183 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 0bcafa4a-38a8-3369-8dc8-7e87d4353897 | -15.69461 | -45.3587 | 2026-09-21 15:58:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 345549b4-ebc5-34f1-b468-583a1fd799c6 | -16.57177 | -43.39316 | 2026-09-21 15:58:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8b693444-c411-387d-8ce2-632798f83bf5 | -18.89008 | -46.83922 | 2026-09-21 15:58:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 39397ab2-35a0-3e6b-9384-29fb0efa24c0 | -14.98183 | -43.09119 | 2026-09-21 15:58:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 59ad3cf6-12a8-3883-a685-894cefe843df | -15.19387 | -41.12568 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 73cc405f-a412-3713-87cf-1d05cc40a8f9 | -15.60992 | -48.31841 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6886eea4-a5fd-3e3c-b8a3-7cd7d2619ac8 | -18.83059 | -39.99625 | 2026-09-21 15:58:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d5da6994-e616-32c4-9ffb-fb204aca5212 | -14.90964 | -41.45831 | 2026-09-21 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8fb218d0-aef5-374b-b937-087aa5ed208f | -16.37615 | -45.10799 | 2026-09-21 15:58:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 956e2d7e-25eb-390d-b1e7-a237d56532cf | -15.28063 | -42.25851 | 2026-09-21 15:58:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 6cd2bdf8-f33d-3c48-84f2-312e2ff0afd2 | -14.6528 | -45.66625 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| ed321ba9-04cd-3c31-8a08-3949ab50c9c7 | -15.61706 | -48.32441 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 62ccedd1-0aaa-3dd8-ba28-9dbc40a21f94 | -19.36065 | -44.86857 | 2026-09-21 15:58:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03c77b41-fb34-3d59-bb39-ebc27c0e3357 | -18.37048 | -43.0431 | 2026-09-21 15:58:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 59dfc7cd-9eff-33c5-8057-5b558ae13296 | -14.6532 | -45.66978 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8f3976a0-ec1a-3726-9ead-1d9866423fc0 | -20.10581 | -47.81796 | 2026-09-21 15:58:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 73e0e8bf-5b70-3f63-8881-3fe1badf7108 | -15.90953 | -41.8628 | 2026-09-21 15:58:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f467d9c2-8397-31f6-87e6-60de37ba891c | -14.6536 | -45.67332 | 2026-09-21 15:58:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.3 |
| fdf08ae1-332b-3bd0-a033-31190d790287 | -16.28739 | -40.598 | 2026-09-21 15:58:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| c96cf03b-d7bd-396d-90db-f7e99080fbb9 | -15.45695 | -48.43333 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6ee3235d-38ed-32fe-be61-d57fa4146d3c | -18.7118 | -43.21688 | 2026-09-21 15:58:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 9534becc-3fe0-3381-98c2-a17e44944046 | -15.69499 | -45.36211 | 2026-09-21 15:58:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 55dfb597-3846-337e-99cb-fd3410599463 | -18.34822 | -42.97624 | 2026-09-21 15:58:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 5bf3940a-aad8-30b8-9737-15b94c39146f | -15.25541 | -47.59677 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 53bc610c-9bbd-3810-a24a-79c54d0409a8 | -14.69644 | -41.94363 | 2026-09-21 15:58:00 | NOAA-21 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a5a3c72d-9c44-38da-905d-cc823faca5de | -15.85563 | -49.90705 | 2026-09-21 15:58:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3e2b5fc5-ee34-36f9-a113-d5ea095e1c74 | -16.4369 | -42.25304 | 2026-09-21 15:58:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 241e804f-d403-340a-98d7-2a53bc681be4 | -15.40849 | -40.93198 | 2026-09-21 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| d2f798b3-391a-35e3-80ae-ba36826dcd01 | -14.57 | -41.39767 | 2026-09-21 15:58:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c7619a4c-6446-31ff-ac9a-e2d2de5e0e4a | -15.4399 | -40.42023 | 2026-09-21 15:58:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4dde9fb1-a56e-36f6-be17-80842b83e29f | -17.95761 | -44.0092 | 2026-09-21 15:58:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e0348c24-8cdc-3fb5-9115-ae54b75c3c94 | -17.80716 | -42.73939 | 2026-09-21 15:58:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 57ff28a7-8b66-36f5-a6f5-e824701f7505 | -15.26214 | -47.60105 | 2026-09-21 15:58:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| dd43106e-9a77-360c-af24-4220a4830995 | -15.15892 | -48.16032 | 2026-09-21 15:58:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |


[Clique aqui para ver as próximas entradas](README147.md)
