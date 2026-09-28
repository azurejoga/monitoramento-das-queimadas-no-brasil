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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b07f35e7-baf4-37f2-b216-2142fedf4a75 | -15.16902 | -46.15183 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09c666a5-207a-3ac8-ab26-8e397b2decf0 | -15.25148 | -43.66449 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e9b9f2b-2043-3642-beac-f0813964c4cd | -18.54735 | -43.59221 | 2026-09-28 03:51:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 886e129b-b3b6-3d79-8111-8243d1db91d0 | -18.11039 | -44.38078 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8b5d8e2f-93a9-3737-b805-55d4cfa32203 | -19.14853 | -43.83027 | 2026-09-28 03:51:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 517c38d9-1c6c-34d4-acba-5661026ac1ff | -14.11545 | -46.2995 | 2026-09-28 03:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d4afb38-8a5c-32a3-8d5d-a9eccf0722b8 | -18.61392 | -43.36884 | 2026-09-28 03:51:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fdcb8c07-f72d-32ff-8731-dde201a7b727 | -15.40746 | -47.92468 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19e92c34-6002-3ef4-8864-b564fa95e7eb | -15.71503 | -42.51576 | 2026-09-28 03:51:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ff19a51-40bc-374d-b465-28830211fa1b | -15.16961 | -46.1488 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54bd9a7c-8c6c-32ff-80e6-c6d5dca4ff67 | -15.15691 | -43.61141 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 862bcfa2-98b6-3304-9348-767e5fc52098 | -18.12125 | -44.37027 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f216d4d8-b849-3dd6-b460-4bec12e2ccd0 | -16.78992 | -43.0096 | 2026-09-28 03:51:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e1be904-2468-39db-8a09-9e3fe215f902 | -14.7334 | -45.57838 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4dbb311a-3d9b-3b94-84bf-d4382d7deae6 | -15.14087 | -43.62576 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b562573d-54df-3b87-8178-7e6b6a2c6365 | -15.17111 | -46.15838 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f1da20b-e1ff-3a5c-9eb8-d057161442f7 | -18.09687 | -44.38183 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4410b1e-aaa1-3f5f-aad4-b8cb4cf16754 | -15.15184 | -43.61475 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60c1e645-7f7e-354c-af2f-24b7b57044c2 | -14.90246 | -49.49222 | 2026-09-28 03:51:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c1c5edd-2521-30de-aa9d-8eb85ed4d87d | -15.14676 | -43.61811 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4de625ef-1326-35b7-b240-48cc453ce845 | -15.16463 | -46.16432 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f85a3612-c950-3e0e-860b-33cbb86778d8 | -15.15419 | -43.6022 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 275b7c61-774d-3283-a4d9-4ab408879843 | -15.29176 | -42.77093 | 2026-09-28 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6066d28d-bbd9-3b31-9517-c9f02d17b24f | -14.08965 | -46.32016 | 2026-09-28 03:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 461acb27-f8ae-3423-b447-dddb3525f95f | -17.83551 | -44.39883 | 2026-09-28 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8087e837-cd68-3b94-a66e-fa3986eebba9 | -15.19166 | -48.43928 | 2026-09-28 03:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5461c8b-976f-3064-91cc-bd58f604e7d0 | -16.39193 | -42.56601 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0068e245-a393-3b35-b086-95ed78597d48 | -15.17298 | -46.14914 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 103ed44d-a956-300e-907c-9536723c27c0 | -15.17727 | -46.16354 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c6375da-2f6d-3186-b242-f1c5c4f2d3af | -15.16385 | -46.15134 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 877f97c0-f76e-3073-8aeb-b28d505cc434 | -16.35078 | -42.56842 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30e27f39-d0d5-3a40-ba39-9b517fb9c8e8 | -15.1716 | -46.16562 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4e299aa-7f90-3e0a-b8b9-345158f06384 | -15.17794 | -46.16008 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6744378-48e9-3387-9ab7-0bb06e616e77 | -18.10111 | -44.38289 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc491fb0-3b7f-3154-be2c-6d86a464b059 | -18.127 | -44.36333 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e8c6448-ad45-348e-b0b3-e1f1c34fd8db | -16.35475 | -42.56901 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 13089873-0d29-3360-b529-54ee3189d254 | -15.17414 | -46.15252 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d79d3bfb-73c3-3254-91dd-a686277b4db0 | -21.5207 | -45.11385 | 2026-09-28 03:51:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| aae8de26-dd85-3fab-a6b1-e0c6e71417db | -15.14755 | -43.6139 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e720572-8049-39ef-8621-8b4649bb4314 | -15.55807 | -47.91991 | 2026-09-28 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b0a70cb-7d86-38f7-8359-04ef520b19a6 | -20.35546 | -43.60591 | 2026-09-28 03:51:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 929f0fea-b562-3434-9f2c-da639938830e | -18.68547 | -44.60756 | 2026-09-28 03:51:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 292b97ca-1d1a-3b25-b639-1172211dbe23 | -16.20255 | -42.87524 | 2026-09-28 03:51:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1987b69c-1a95-3466-b7a7-1a8fafa7475b | -15.4058 | -47.90438 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c58553bf-34c4-323d-8d25-743c4ce5f08b | -16.38894 | -42.56 | 2026-09-28 03:51:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 314e0527-057d-38bc-9c2a-119d02f36f76 | -15.3461 | -42.16732 | 2026-09-28 03:51:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| adb4226e-0cc3-35f7-9a5c-8c7f0fd9f417 | -15.29696 | -42.76548 | 2026-09-28 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4599eba2-400b-37b3-b54f-57d8394c533a | -17.82511 | -44.38332 | 2026-09-28 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15a3f3d7-77f4-33e2-b206-186b7d79e221 | -19.14374 | -43.83331 | 2026-09-28 03:51:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2591746e-0f7b-35b1-a265-957cdac83a77 | -15.17615 | -46.15952 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7d77576-0e55-3ea5-bb03-bc99b7945613 | -15.16531 | -46.16098 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a33a3dd-8640-3140-b280-0f2089353d2f | -15.41081 | -47.90855 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| becf7398-696a-3838-b7a9-4a7270c0a3a3 | -19.14783 | -43.83395 | 2026-09-28 03:51:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cb99e98-0b73-39ee-99d2-b7763055f29c | -15.17229 | -46.16206 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f853f7c-7b3a-3838-a502-832145caf55f | -14.79746 | -45.95829 | 2026-09-28 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2eface24-8fbb-37d6-9f62-96b297e32087 | -14.7383 | -45.57942 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85ba2e75-6785-36fd-b2f9-81bf71f4644d | -16.78126 | -39.42531 | 2026-09-28 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 032c6ece-9a9e-3ab9-a9d7-530c024a6b07 | -14.52156 | -48.31152 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bc727878-8538-30b7-a2fb-da20f5739160 | -15.41207 | -47.93081 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff142cbe-8a50-3428-b2ab-bdbad891bc8a | -17.83119 | -44.39808 | 2026-09-28 03:51:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad1eb8ef-43b1-3ee7-b793-b53fb3ef8664 | -16.79054 | -39.41143 | 2026-09-28 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a2b3a050-9f72-3e7d-9dbc-a7c77173199a | -15.16161 | -43.58632 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8eceaf90-d69f-302c-9c53-c84eae305fdf | -15.40429 | -47.9116 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afc7b690-e721-3f82-b7fd-e8dfc30b5cdc | -21.51569 | -45.11705 | 2026-09-28 03:51:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bf820e9c-f5f7-3ce7-b402-5b12a49a66eb | -14.52479 | -48.31636 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 755a07ec-647c-34ec-a280-efeb953b7386 | -14.59839 | -45.60198 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24aa6238-239d-33fc-92c6-fb9d57ff7be6 | -15.14878 | -43.58376 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6cb5f614-2419-3ddd-89cc-51d47258fa4e | -18.10881 | -44.38913 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 858ecb32-a4a1-36b2-a903-1dab567df131 | -14.72334 | -45.57081 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3113928e-842b-3ab9-a509-c29910a2846e | -15.55893 | -47.91574 | 2026-09-28 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c26a3f3-30b3-3abb-81e1-85509524b154 | -14.10073 | -46.31906 | 2026-09-28 03:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b122355-876b-35c5-b9dc-988490d4abe2 | -19.1526 | -43.83097 | 2026-09-28 03:51:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44bb6d43-60e5-3c27-839b-ecd6ce37ab6b | -14.5274 | -48.31292 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea8d8418-9ba9-35b5-bf0d-4ff4a0446419 | -15.29119 | -42.77405 | 2026-09-28 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c25a0a15-4823-3a4b-b5ec-493ef0ffe0ba | -15.14516 | -43.62662 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1741fbc6-f099-3e7c-94eb-37741481fc82 | -14.89863 | -49.49333 | 2026-09-28 03:51:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81b75ff2-f873-35dc-be6a-929205c9a313 | -15.17474 | -46.14946 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb20a661-f146-31da-b393-8dae21c46f67 | -14.90136 | -49.49727 | 2026-09-28 03:51:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd52e299-ba1f-33af-8510-7046665c27b3 | -18.1019 | -44.3787 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6bce2d6c-ae36-3d41-b804-79efcc278e25 | -18.11544 | -44.37755 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a6240b04-9e0e-3d30-a03d-bd9a6e61cc92 | -15.19251 | -48.43522 | 2026-09-28 03:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1abc9ed0-c8dc-36c3-85b5-381ef2a95fc8 | -15.41006 | -47.91212 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92c63eeb-702c-302c-bfc2-d89766164ae2 | -21.51652 | -45.11285 | 2026-09-28 03:51:00 | NOAA-20 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 485bdafb-613a-32fc-b380-b1f414deb5be | -15.34521 | -42.17231 | 2026-09-28 03:51:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2194d275-2f50-3c35-b308-f879b9106679 | -15.21641 | -46.35608 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fe18648-9e99-376b-bf19-70e49f124d8a | -14.7184 | -45.56999 | 2026-09-28 03:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f87daaec-13db-31cc-960f-62ea2a0ea068 | -16.78527 | -39.42213 | 2026-09-28 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 043a277b-22b4-31cd-9943-932c80c7b62a | -15.16004 | -43.59468 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49e1d0a7-d702-376b-8494-4bd55136bd67 | -18.12278 | -44.36216 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88e5961f-0069-3b7c-a093-b448657aacde | -18.67626 | -41.45918 | 2026-09-28 03:51:00 | NOAA-20 | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 84ea06c0-7611-3193-b1ba-f251063f54d4 | -15.17292 | -46.15883 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2a31972-d460-3d8d-b5a6-24d5e111e723 | -18.09848 | -44.37334 | 2026-09-28 03:51:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94962a22-4e9f-3447-bb8f-0c3706d08c04 | -15.41306 | -47.92605 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3792648d-7430-3981-bef2-620d094a9a68 | -15.2906 | -42.77721 | 2026-09-28 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f99eb174-1b92-35b6-89f2-e3b001f258f7 | -14.51474 | -48.31496 | 2026-09-28 03:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c92224b5-27e6-32b9-9b0e-cf134aa5ef58 | -15.40839 | -47.9202 | 2026-09-28 03:51:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f04c7d0d-a810-3e3d-b88f-a7a3af38cf8f | -15.05239 | -47.23561 | 2026-09-28 03:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a3ef753-02d4-3cf6-b5ee-60860b5f02c5 | -19.77226 | -50.2965 | 2026-09-28 03:51:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9d17ac4b-9c11-32bb-b0c5-83ea6b04b2ab | -15.16083 | -43.5905 | 2026-09-28 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2980886b-3d5b-345c-b871-2e977e5fc66b | -14.79304 | -45.95424 | 2026-09-28 03:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
