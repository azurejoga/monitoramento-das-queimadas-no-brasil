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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a8c2642-d1c7-30b7-ba2b-eb1a2a257e01 | -15.00987 | -40.98806 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 0a64faf4-4b8b-30f9-8167-f2192a5125b4 | -14.87598 | -41.71239 | 2026-10-07 15:58:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 89917c51-709d-3092-8d02-c2c979f84269 | -16.84917 | -40.59698 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| 6ca7df08-95cb-3b00-b6a4-325366f2665a | -17.01876 | -41.03828 | 2026-10-07 15:58:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| c9ef77c1-8484-3913-924a-e6c2125a041d | -15.10915 | -43.63216 | 2026-10-07 15:58:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 23.8 |
| fb360c80-43a5-3f79-8f54-9d7d6fbf1b33 | -17.02127 | -45.91964 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 68990a8b-cdfe-35cc-a04d-5659a6824c92 | -16.14214 | -43.51982 | 2026-10-07 15:58:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2322c5c5-9b75-3963-baea-aaa8b45e2c77 | -15.17856 | -41.58423 | 2026-10-07 15:58:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3e648fc8-27da-3dfb-80b5-839a85ec8fcd | -14.40931 | -41.34299 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 4b7f6a6a-8b21-3373-916a-54b8a966bd7d | -14.76657 | -47.15305 | 2026-10-07 15:58:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5fee3893-35ce-374e-8a34-53f74bc204a8 | -17.19429 | -43.52496 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 85f100a4-f17e-311c-8f86-8e2a5ab4eca4 | -15.45035 | -43.95513 | 2026-10-07 15:58:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d5bbb5bb-0ed3-3637-a0c3-67b99fdcc598 | -17.44425 | -44.72322 | 2026-10-07 15:58:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f250a0fc-9da4-3237-bb41-447d5707d124 | -14.78965 | -42.62525 | 2026-10-07 15:58:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1b78da11-c82e-359c-86f6-fe4ddd9dbd2d | -14.36024 | -41.28035 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 104.8 |
| ea94c577-eb80-34cc-8a32-8915b70d62c2 | -14.34924 | -39.3588 | 2026-10-07 15:58:00 | NOAA-21 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1f62bd5e-f50a-380f-906f-abf42c0e437e | -16.97847 | -45.47189 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 32b88f17-1220-32fb-9502-c05aaa784bc2 | -15.56996 | -44.52076 | 2026-10-07 15:58:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c569a5f1-a65e-334d-9234-ea43925214bc | -16.85613 | -40.59966 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| 6f8f2322-d757-3359-a2cd-a38db26fa86d | -15.99645 | -40.98397 | 2026-10-07 15:58:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 50992eb3-e8e2-3482-8c5d-d0db71b91f00 | -14.12661 | -41.37334 | 2026-10-07 15:58:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 42.6 |
| 6fd3f1f8-109e-3eac-90ec-4972c4222fd2 | -17.01562 | -45.92023 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| d46e697f-25e2-3b4a-a657-c05dac67fdcd | -15.11431 | -39.92569 | 2026-10-07 15:58:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| a264c2d4-9acb-32d9-8290-dbc2f41263ed | -14.83037 | -40.83867 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| ceecd206-5762-32ae-908d-d3f4553bb2a0 | -14.35405 | -41.27726 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 99590fde-065e-3b02-a835-42877d09f6af | -16.05304 | -39.84155 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| c1654e3c-dc7c-3ada-87d9-d09e3ada2531 | -16.72474 | -42.0485 | 2026-10-07 15:58:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 16ff2a48-96c9-36ad-8c1e-1f1a935fd18d | -14.3376 | -41.36757 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 818c3361-a925-3507-bab1-6e9310631696 | -14.24156 | -41.39575 | 2026-10-07 15:58:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 35.3 |
| d1b0e25a-bdd1-3be5-a727-d53a08865684 | -14.56917 | -43.83808 | 2026-10-07 15:58:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f1e5a8ba-6fb0-3b7b-8f72-df3ed0712192 | -14.75595 | -40.94297 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b08c4735-7bf1-369f-9a0c-e128775afbfc | -15.53693 | -41.24614 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| bf84d310-73de-3276-950c-206b01f27b5f | -14.43366 | -40.62517 | 2026-10-07 15:58:00 | NOAA-21 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 14148eba-d439-344b-8a5f-fd6ca931ffd3 | -15.97398 | -44.88074 | 2026-10-07 15:58:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 292e9edc-5cae-3430-8364-b2d09690fb14 | -16.04836 | -40.64949 | 2026-10-07 15:58:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 8298ccde-1bd6-334e-af20-b78b5cea2838 | -15.2594 | -39.27829 | 2026-10-07 15:58:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1654b25e-544f-3348-9177-b590cd0ceeb6 | -15.48359 | -40.76187 | 2026-10-07 15:58:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 7b57d490-2bb4-34a8-be4f-e318c4afc526 | -15.41963 | -43.70352 | 2026-10-07 15:58:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4c992a2f-cc96-31ac-9db6-0a67aa082737 | -16.17319 | -41.68716 | 2026-10-07 15:58:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| f84ec97c-e533-3069-bf0e-22dde43def68 | -17.44391 | -44.72224 | 2026-10-07 15:58:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b00f7b15-acb4-3d73-afe4-62b29316f81c | -17.63843 | -46.12317 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acb45732-e144-3cfd-a35c-da620b3c9892 | -16.7859 | -43.90317 | 2026-10-07 15:58:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c08ef4fc-9f83-3c98-863b-01295035fb37 | -17.52556 | -45.4617 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7fb56805-d691-393e-906f-7a6b64b5e7fd | -15.39152 | -41.69886 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.3 |
| 8782d9fb-b00a-3e2f-851c-70af7b8e3de5 | -16.85647 | -40.59099 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 8bf0b658-7461-3e31-aa10-9e127a9e1636 | -14.15266 | -42.18534 | 2026-10-07 15:58:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 97aef9e5-2be4-30cb-9081-f9c7a3266939 | -16.85714 | -40.59609 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| dde88ff0-b7cf-3b94-93ba-0af45e4fa769 | -17.49857 | -39.31092 | 2026-10-07 15:58:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 1b7a1d7d-1b52-396f-8175-832090101cc1 | -15.99957 | -38.92693 | 2026-10-07 15:58:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| d53c9cbd-0595-3106-82b1-cc24ac42f86c | -14.35623 | -41.28092 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 316.1 |
| 23b348ba-b260-3663-a9a0-02b2e3616318 | -17.9838 | -43.9249 | 2026-10-07 15:58:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e82d94b4-dcf7-30a5-8b72-c001f1557dde | -16.23715 | -40.35355 | 2026-10-07 15:58:00 | NOAA-21 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 4f030a29-0e02-3154-b5da-1d693aaa97a2 | -14.43461 | -40.80893 | 2026-10-07 15:58:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| cdedb30e-e569-3a5e-903d-27c3716a40f6 | -15.71908 | -43.2759 | 2026-10-07 15:58:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 96aaf0e8-75de-376a-ad56-a0bd99e04de4 | -16.98197 | -42.10522 | 2026-10-07 15:58:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 54d94d1a-62c8-32be-9226-fd06bebac99a | -15.14851 | -47.18776 | 2026-10-07 15:58:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c066c917-bf36-3d51-8ba3-2041c22b06e2 | -15.11389 | -43.63159 | 2026-10-07 15:58:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 5e206c74-f36c-36ff-add9-cae34fdb3a7c | -15.34297 | -41.69673 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 7f4b6509-6e89-3df7-85af-610cb6ccb272 | -14.3553 | -41.27371 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 369.3 |
| cc49c4bc-f410-327b-8b90-491baa323836 | -18.09693 | -42.5756 | 2026-10-07 15:58:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 60b5d331-6a25-3571-a3c4-8f5f0e742635 | -14.82988 | -40.83642 | 2026-10-07 15:58:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| c42a0f1f-b992-3c8e-8253-47eb6e3da120 | -14.1877 | -40.46244 | 2026-10-07 15:58:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 84650226-4de2-38b1-939f-9af62e37f9f1 | -15.11805 | -39.92516 | 2026-10-07 15:58:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d4ae813a-5ef0-38f8-a516-d094cc9f3edd | -15.0257 | -39.39314 | 2026-10-07 15:58:00 | NOAA-21 | SÃO JOSÉ DA VITÓRIA | BAHIA | Brasil | 2929354 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a69b81d4-4d35-338c-83c2-566ff59da4eb | -14.19658 | -40.64388 | 2026-10-07 15:58:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 2bb2b314-32d5-33f2-a709-dd982afdb4d4 | -18.77196 | -41.88929 | 2026-10-07 15:58:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8d96a56f-ee05-3d7e-9aae-da320d8db9bd | -16.05867 | -39.85491 | 2026-10-07 15:58:00 | NOAA-21 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.5 |
| 1fd38aed-f4a4-3f3e-b231-1bee3326ce03 | -16.14238 | -43.51713 | 2026-10-07 15:58:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ff3f8774-923c-3c3c-8fbd-c78bff41913c | -17.01477 | -45.91225 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7150aa42-8203-34e9-9900-cc4f3113af30 | -17.20193 | -45.09657 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 7c76d022-456d-38f2-b789-0250a4094800 | -14.04328 | -40.45205 | 2026-10-07 15:58:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| df915612-c762-3c56-b5a2-311698db5e38 | -17.49697 | -39.87674 | 2026-10-07 15:58:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.4 |
| b31a6abb-67ee-3f0b-88fc-16e83a2eb5fb | -16.89502 | -40.87682 | 2026-10-07 15:58:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0edc39a4-2b69-3e47-a76f-f9dafc736f20 | -15.33544 | -42.76621 | 2026-10-07 15:58:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a67cfb32-ad63-3628-acee-b49effe42e89 | -16.9288 | -42.10769 | 2026-10-07 15:58:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| 27396d4b-d1da-37e2-9d7e-c80ebf9b74dc | -19.49469 | -44.92394 | 2026-10-07 15:58:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b999c414-6aa3-3e9b-bde0-c52e9bd2f459 | -18.04143 | -42.54117 | 2026-10-07 15:58:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1e9c9abc-19f3-3018-b9e0-f7c457a5b406 | -17.52044 | -45.46609 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| caa161d1-7312-3b4d-aa51-394af67d8908 | -17.01957 | -45.90373 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 89d451ce-6234-3e37-8e8f-50f4ddf82547 | -17.41892 | -39.81718 | 2026-10-07 15:58:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9ede3d85-68d9-314a-92a5-e591c31ea795 | -14.79549 | -41.95811 | 2026-10-07 15:58:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d2eed508-eb96-3302-acf7-77263534ee45 | -17.52051 | -45.46428 | 2026-10-07 15:58:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1da59f2c-6765-3325-91ea-89598156af88 | -18.0451 | -44.56887 | 2026-10-07 15:58:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea15ccac-416d-38fe-abe7-fb7805dd0def | -14.773 | -47.15686 | 2026-10-07 15:58:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2928cd5-c1fd-3cf3-9972-617220cf359b | -17.43241 | -43.64561 | 2026-10-07 15:58:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 980c3763-3393-3779-9579-bdd27fb6f54f | -17.20231 | -45.10011 | 2026-10-07 15:58:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2c4e5523-1b8f-34c0-b784-3a8c50fc5c08 | -16.85315 | -40.59652 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| c30e7541-6d03-34a2-9668-c7fb84e09ac4 | -15.39252 | -41.70679 | 2026-10-07 15:58:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| bf0f22d9-780d-3d68-86e7-901644e94715 | -18.18151 | -42.3422 | 2026-10-07 15:58:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| bc212763-3e67-3091-a6c0-738e0de8de4a | -14.45662 | -40.94481 | 2026-10-07 15:58:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b39fa269-9fa0-3194-b87e-6c34b80b5f08 | -14.35929 | -41.27305 | 2026-10-07 15:58:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 6b944253-4e9a-36e7-819f-15a681492392 | -17.02779 | -45.92707 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 62.0 |
| c32631fc-d3c1-3f68-9816-05e3748e2d06 | -14.31701 | -43.81339 | 2026-10-07 15:58:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f89c3f9f-df71-305b-8f01-d08cac36f755 | -17.19785 | -43.52308 | 2026-10-07 15:58:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86acb01d-a061-34c8-88dd-8687b2823f3d | -16.85247 | -40.59138 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| d41c13fa-5026-3791-814e-2832631c9bb4 | -14.74272 | -47.46366 | 2026-10-07 15:58:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 011bff8b-c441-3920-8079-a554572048f5 | -16.85084 | -40.58976 | 2026-10-07 15:58:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 9d6c6700-73da-3a66-bd19-d68a37fb6b1a | -17.01435 | -45.9083 | 2026-10-07 15:58:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1a9d6a4e-b809-3ea6-b164-9c030e30cbd7 | -15.88955 | -40.72116 | 2026-10-07 15:58:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 7b3bc50b-afae-3ca0-82ae-6d97a472d596 | -21.65487 | -41.35426 | 2026-10-07 15:58:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |


[Clique aqui para ver as próximas entradas](README146.md)
