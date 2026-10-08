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

## Dados Diários - Página 225

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 143ac534-d9b8-39f6-b9c5-ab7d2cf5a7c6 | -14.36878 | -41.17652 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 0b2b0012-1691-38c2-89ba-8907d6c2c9b0 | -13.93595 | -42.35647 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e4429fbd-5c80-3b46-810a-661ae696a3fa | -18.26031 | -42.18341 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| bf387d70-586f-32af-89f6-38a321f0af9c | -12.15381 | -42.26485 | 2026-10-08 15:39:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c8741f9e-fa93-3fd3-8e72-5ed0ac77b986 | -10.7693 | -38.49746 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7fa04e3c-850f-3cb6-ae90-d376e2c26de7 | -13.3483 | -43.96667 | 2026-10-08 15:39:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7f9642b7-0cfb-3025-a035-0492fefa6607 | -11.63027 | -43.71271 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a16a75ff-6af7-3ad7-aef6-ad42c2bc68c7 | -14.25781 | -42.43752 | 2026-10-08 15:39:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 59.5 |
| c26fbbf4-dabe-3c64-9966-5a70e254f512 | -14.77422 | -41.14389 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0b1d9c97-48b8-34dc-aebc-f87d67e4a0eb | -11.74694 | -43.64312 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9ab3d1c9-3044-350a-b50e-ba67a6ab9b7c | -12.17387 | -44.8176 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 7bdd9ed7-5f86-3907-a122-1cb684404558 | -12.71466 | -45.80828 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 57d751a9-9441-3676-bce8-94055112e2de | -12.18392 | -44.66092 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 6b9b78ca-c5e4-3095-b24b-4ce9548297dc | -17.42612 | -40.41844 | 2026-10-08 15:39:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| b8b9ee11-7099-3481-9d39-d698b6290484 | -11.35695 | -43.14914 | 2026-10-08 15:39:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 1d3cd435-5211-3140-a1e0-145bbd211e85 | -18.26095 | -42.1816 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| c7f9922e-7829-3804-8065-64aa4b720858 | -14.48246 | -41.80487 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b0493879-9aa0-3ff4-8a67-598712694a57 | -11.61487 | -43.63179 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| e640e1b7-45b5-33a2-a836-3fcb135eee7a | -11.61736 | -43.64812 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 491871e6-cbe4-3156-aa28-afac4fc6086c | -11.23832 | -44.02164 | 2026-10-08 15:39:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2d2805ff-695a-3d36-b3e6-4fe5220223c6 | -11.75596 | -45.50029 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 0e24e118-33e2-3d3e-aeda-c0cb5ac7ac8d | -15.03972 | -42.49469 | 2026-10-08 15:39:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 98a24ce7-186a-32ba-a4c2-cdc5e3a01c07 | -12.18481 | -44.65286 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 8811ccd4-f42a-3ace-9b57-cfbced03c6ee | -14.15422 | -42.09975 | 2026-10-08 15:39:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c77aac04-430c-32e1-a9da-d3d51dbb410f | -14.82122 | -39.40233 | 2026-10-08 15:39:00 | NOAA-21 | BARRO PRETO | BAHIA | Brasil | 2903300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| f3e37104-d078-384d-8154-008db018cc18 | -15.53946 | -41.72265 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 95bc16fb-7534-3751-85de-c03c1bab2343 | -14.30041 | -39.20668 | 2026-10-08 15:39:00 | NOAA-21 | ITACARÉ | BAHIA | Brasil | 2914901 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 9fa8e687-e73f-3a5f-8d9a-ff01979c9c3d | -15.5164 | -42.64983 | 2026-10-08 15:39:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 23b17940-95a1-3ca0-9764-4eeb3c4fbffd | -11.72774 | -43.64 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2a0084a8-a2d3-362e-8bda-3fa64b959bae | -12.17715 | -44.8209 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| 56c9f29a-2d79-3bc7-abb2-3a49711ae4a7 | -11.63015 | -43.5981 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 97eb1607-e00f-3465-9efd-fcaedb9f1da9 | -13.68773 | -39.93093 | 2026-10-08 15:39:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| df8b021b-a0ca-33f6-8e26-adf7126eb314 | -16.15953 | -43.63921 | 2026-10-08 15:39:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 12e878a1-dc44-3a29-8a9c-d1da0977057e | -11.93613 | -40.35867 | 2026-10-08 15:39:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a7d72e22-87a1-3710-afa6-ee6e0a76078b | -15.62905 | -40.1267 | 2026-10-08 15:39:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 88428c79-31e9-3801-9d97-9b96f3e6abb5 | -14.09626 | -41.20116 | 2026-10-08 15:39:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ec41c957-ee6c-315f-a5d9-2f4dd9cee376 | -16.45444 | -41.27052 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c61f63a3-37df-3cf5-9f76-bbea65951670 | -12.17323 | -44.81157 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fa542705-ab70-3cf8-9fdc-d351c5c2be38 | -13.36238 | -43.87139 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 17fe42ba-8e33-3aa1-a765-59a22fce8edc | -11.84019 | -43.52962 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d3f69c2f-e600-37e4-83e5-ff4a51f582c1 | -16.31344 | -44.56184 | 2026-10-08 15:39:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 177.2 |
| e0a4ef3b-3192-3482-828c-3df914987323 | -11.78421 | -43.53172 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2e7cb9ed-861d-3bd2-b1b3-ace713dc3222 | -11.62442 | -43.07594 | 2026-10-08 15:39:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9c2272fc-199f-30b3-8e4e-060ff909e274 | -15.62978 | -40.13304 | 2026-10-08 15:39:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 8c59b2f9-4e6c-34af-96e9-e78b32c864a0 | -11.45528 | -43.38656 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| a3f1f24c-04c7-3ca4-89d2-48abcb31965a | -12.24028 | -44.7446 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 8d7196aa-a18e-3223-93d0-47b7e1f898ae | -14.42414 | -41.51313 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 511d0c93-8abe-3a09-95b8-0357406d2d1f | -14.79454 | -41.61291 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 29.1 |
| dd158e16-b217-3f19-b6b4-081167b6a972 | -11.32788 | -39.48533 | 2026-10-08 15:39:00 | NOAA-21 | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 9cd686f5-fafb-3017-9378-1675123a9edc | -11.61941 | -43.6165 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 382.9 |
| eae5ebce-0edf-3533-a306-c52f6c97d459 | -12.29486 | -40.49357 | 2026-10-08 15:39:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 243bb162-12f0-3874-ad94-7dfe6c80b613 | -15.3977 | -44.33441 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 467a4a8c-e1f1-3b93-85c2-c4b79fbad0b8 | -12.03521 | -43.43931 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 17a1e119-315b-357b-ae64-bd7ed3b71afa | -11.47466 | -43.39388 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 501d24ee-fcb7-35cd-82dd-61b54adcffe4 | -11.79094 | -43.53586 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7f6ce4c5-c450-3d6c-85af-1058ccab3c0d | -14.47021 | -40.72201 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 656c0569-2cbf-310e-9c71-07f9041fa54a | -14.06034 | -40.94527 | 2026-10-08 15:39:00 | NOAA-21 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 365e7e3b-c0fd-3d0d-93b5-e9198a057928 | -14.98722 | -39.502 | 2026-10-08 15:39:00 | NOAA-21 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 9e169a24-06d3-346b-a749-1eb6f7f8b62c | -14.98497 | -39.49918 | 2026-10-08 15:39:00 | NOAA-21 | ITAPÉ | BAHIA | Brasil | 2916203 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 403bccee-2e05-3919-8cb1-0d6e7c54d652 | -12.23894 | -44.73262 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8dcc4e3e-6371-3174-9d16-d7bdc15b2734 | -13.02188 | -41.04961 | 2026-10-08 15:39:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2f5685f3-76f0-3cc2-b559-34628f50bebc | -13.34184 | -43.96732 | 2026-10-08 15:39:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0e4b5446-12f7-3a12-9808-fd9c5f5ae050 | -12.04168 | -43.43934 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 571f14f2-f43d-370b-bad2-3dce29a81ad9 | -14.46558 | -40.71928 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 20a84e93-ec07-3ce7-bed5-d4ece5843fab | -13.73538 | -42.66544 | 2026-10-08 15:39:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 52587cff-cd1a-36e2-b8b5-036059a74497 | -17.10508 | -41.35469 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 58f44500-f79d-3f0b-8a34-52c93d03171d | -11.62675 | -43.68149 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| eed8e97b-7fd2-37e8-9b40-266b8cefcbcf | -17.0274 | -41.97676 | 2026-10-08 15:39:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8aedc451-db9c-3f6c-a641-ba3f2abcb334 | -15.60307 | -40.50416 | 2026-10-08 15:39:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 1066b511-53d0-3972-8bab-d8187d639fc5 | -14.85846 | -42.06837 | 2026-10-08 15:39:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 0219962b-4bca-3275-aa75-684e0ae42e78 | -12.81838 | -41.05331 | 2026-10-08 15:39:00 | NOAA-21 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ddc44fe6-c880-386c-bc75-2424aa438642 | -17.22189 | -39.3821 | 2026-10-08 15:39:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 9881a815-9a67-3513-a8bb-bd2dbc2e049f | -11.60496 | -43.64949 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b3076b8f-ec2f-3465-999d-762bb733f5ae | -11.62852 | -43.68892 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d9c1e103-1f45-3ef0-bbc8-a0808cbc844b | -14.47224 | -41.24895 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 373fdde2-0c76-3913-8139-8adc29728842 | -12.18056 | -44.81679 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b31f4c0b-e056-3fb0-a321-58b1393e4687 | -17.06742 | -40.02132 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b1e9fd35-a79c-3bb3-b366-636a4943472a | -11.62223 | -43.68895 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b8bb18bf-11fe-3320-9bf8-5b890693d6a6 | -11.62735 | -43.68677 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 63f2e922-cfe2-39f7-91a4-edef82bccb17 | -11.60439 | -43.64465 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6f7c9090-540d-36fe-a8d0-b5bcff5a0791 | -12.03462 | -43.43433 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| dbf3c19f-c439-3906-b8d8-e61c78688ab1 | -12.15953 | -44.74665 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fe9efd90-99fd-3d88-9550-1ac14c88d6f8 | -11.63102 | -43.70967 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 38215edf-9b30-3197-9a3a-1566724e9691 | -11.77187 | -43.53306 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 120a080f-a972-301f-82e4-2bf0fc139fb6 | -11.99478 | -38.03968 | 2026-10-08 15:39:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| f3b01392-8359-3ba4-989d-bbd676ff6064 | -14.60577 | -40.02152 | 2026-10-08 15:39:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 237efa3a-96c8-39b3-b9e2-7d4105ea2d6e | -11.32939 | -41.98584 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ea2cc9c4-2cb7-37c4-b163-3fccf54c0a59 | -14.55847 | -44.0793 | 2026-10-08 15:39:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 616845dc-aab3-33e4-b7e1-b75079b35d4b | -12.18328 | -44.65508 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bc0ff723-677d-3746-9cbd-e5a2210c65e3 | -11.77256 | -45.58086 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| eb7e38cc-f5d5-375a-bde9-1c819a0b3339 | -12.18926 | -44.64837 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| df0f32dc-9ff5-3e27-a54b-1b9fc59bdd1c | -11.97312 | -39.04951 | 2026-10-08 15:39:00 | NOAA-21 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| f500dc37-aa78-36ed-890c-9903144e3a5e | -14.66942 | -42.48529 | 2026-10-08 15:39:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 25.0 |
| 4d2e34ce-ac71-3781-a638-652cbfd8f74e | -14.75857 | -39.81291 | 2026-10-08 15:39:00 | NOAA-21 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.4 |
| d7935032-f770-35a1-b21c-a5814890e65f | -14.52638 | -40.33413 | 2026-10-08 15:39:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 999c8bbd-621a-3704-a618-ae0fd90d88e6 | -15.39095 | -44.33506 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| ed6bd973-a0a8-3950-a8e8-ac5763a230d5 | -13.96497 | -44.8579 | 2026-10-08 15:39:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| fcdc274c-e652-348f-844e-3313ff774894 | -15.82898 | -45.40153 | 2026-10-08 15:39:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 52c0e32a-9b2a-371a-8921-dce735d76032 | -12.22123 | -44.63419 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 435abb95-35c6-33dd-8ec7-d9641b6ad17a | -15.39518 | -44.33758 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |


[Clique aqui para ver as próximas entradas](README226.md)
