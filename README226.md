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

## Dados Diários - Página 226

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9f800c7-6f4d-3523-a667-c12d1f469df8 | -18.22352 | -42.31327 | 2026-10-08 15:39:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 9454e60f-2be7-3a76-ad7c-7571f9bd432d | -15.85578 | -40.80314 | 2026-10-08 15:39:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| e2b794ea-ce0a-38e3-b7ef-10bbb4715e2f | -14.49658 | -40.7168 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 936cbe63-3394-369e-a0e0-4423f1e0113d | -16.95416 | -40.05633 | 2026-10-08 15:39:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| d6dab932-97e3-3272-a7ae-3aaa274452cc | -15.7033 | -40.59165 | 2026-10-08 15:39:00 | NOAA-21 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c5bc9664-cb83-3156-970b-be3af83f8c86 | -14.46089 | -40.81681 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ebf6b07d-9028-3646-a3b6-68963598d05a | -13.18711 | -43.50213 | 2026-10-08 15:39:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 680e5c93-73f6-34e0-80cf-0ceef6fd9ceb | -11.61137 | -43.65651 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f57c47e6-4c86-3d9e-8cb3-5d512756214e | -15.38844 | -44.33823 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| a37a3e7a-229d-31b3-bd6b-d9032467edd0 | -15.33968 | -41.04456 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.2 |
| 4447b119-4ebb-3e1a-94c2-3f09390e4749 | -15.40131 | -44.33094 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 76e84a57-dc98-3f5b-9fac-a91d8aefd17a | -15.03186 | -41.39464 | 2026-10-08 15:39:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4d813873-6cff-3695-8f0a-855d7f7ff8c2 | -14.79182 | -41.61193 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 9d361753-853f-3505-b33b-4a3036d1cb41 | -14.52216 | -40.65836 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f44e14f2-4c4a-3391-87c3-eee19c555ed8 | -11.59934 | -43.65505 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| c946e9ba-a6e1-3837-b4df-0a35ee5d5a70 | -11.64728 | -43.68781 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 391460a0-8ac5-3dec-b2f6-58844efc9abe | -15.11096 | -43.62729 | 2026-10-08 15:39:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 7eafdf6b-6afc-3731-b244-ebc054d8b711 | -11.77427 | -45.53934 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 097110fa-a693-3bff-9623-0c1f0037170a | -15.39712 | -44.32836 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 34f9e810-5203-3c2b-9a58-012f1c890420 | -13.54585 | -40.70562 | 2026-10-08 15:39:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3a1674d1-f401-3cef-b2e1-21b7d083d67b | -14.19168 | -41.24762 | 2026-10-08 15:39:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 05e0be9d-f06e-39da-adab-41e9de6ae809 | -11.47522 | -43.39854 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9c659110-5254-3956-b713-32d840a786d6 | -15.79349 | -44.6782 | 2026-10-08 15:39:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 56a1bdae-a191-3aa4-9249-0eec47789c97 | -16.45127 | -41.27209 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2284622e-f87a-36ed-ab44-5d45d9b057e0 | -17.10814 | -41.34683 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 271341e2-2d91-37dc-a77c-4fb3bf3766ac | -17.11077 | -41.35376 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| bbe89551-77ac-3520-8421-ecaa9a1f6b46 | -13.2975 | -41.51341 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 31.9 |
| 8e325ca9-84da-36b4-8a36-241110a1da3b | -14.73488 | -40.29148 | 2026-10-08 15:39:00 | NOAA-21 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| b9a1917f-3e1c-34a5-b81b-511aa8efd2fd | -11.6358 | -43.59541 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 004b38b4-9265-3526-b512-7c123f6ba4ae | -12.17992 | -44.81081 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 39ff4016-182c-35cc-944d-40f88e0b6329 | -11.82019 | -40.49289 | 2026-10-08 15:39:00 | NOAA-21 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2fe6bcb4-0bcc-37ab-b84c-789c56d9fa65 | -13.45927 | -41.92273 | 2026-10-08 15:39:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| dfe7d042-dc6f-387c-9dcd-77fcbb143556 | -13.29836 | -41.52053 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 89.3 |
| c4f0a381-4763-3713-a60e-771720e47d6c | -15.95512 | -41.0905 | 2026-10-08 15:39:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| a47d2dd4-a0db-3603-b67c-d22db0c360bd | -12.18987 | -44.8136 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 69c8b48c-6c85-3866-b7a5-5d00b3ddb7ec | -13.38585 | -43.4826 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| bcd594c6-f67e-348d-bab4-dd0b921dc057 | -11.5959 | -43.67909 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d868e162-6305-338b-9053-6179fbe59240 | -11.76585 | -45.52285 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0303a626-8387-3f4e-8e51-1dee2c50a772 | -13.14692 | -40.21928 | 2026-10-08 15:39:00 | NOAA-21 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1ac14d14-c753-3ba4-b944-44f01a1a44d5 | -15.34009 | -41.04816 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 41.2 |
| 1e624779-0111-3386-bed4-427430bfbc75 | -12.70909 | -45.8234 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 0fee39c0-763f-342d-b86a-8b7e3227a1a4 | -11.76875 | -45.54796 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 523cb4b5-e32b-3a71-bf00-2b28d080f2d4 | -13.74389 | -40.09817 | 2026-10-08 15:39:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 269d1b60-e8dc-33b5-8309-ae3cbbd2d585 | -14.4667 | -41.24926 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 552fccf6-3fe5-3f58-9749-f635157d8cd9 | -14.46051 | -40.81355 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 3b19db27-4120-3dc9-800b-06fdc48023a6 | -17.12486 | -39.51571 | 2026-10-08 15:39:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f1d559ce-f73d-3a94-a063-a91ef55898e4 | -11.74792 | -43.64201 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5675585e-5bbc-3cd2-a2a1-f15c00ebfeb7 | -14.67321 | -40.80858 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| ff36680f-f27a-32ab-a09d-30762e307ac5 | -12.24094 | -44.7505 | 2026-10-08 15:39:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 2c871ed3-f1f7-3c42-9496-166ce1a6b346 | -11.61448 | -43.62406 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| bb98b9f7-cbb7-3cbf-8663-6f9635bcebf1 | -14.2414 | -44.4355 | 2026-10-08 15:39:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0ca50467-cab7-3adc-aae1-4e438b6b72e6 | -14.67391 | -40.49728 | 2026-10-08 15:39:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 4940fbe9-0909-3dc8-8404-1edc11333852 | -11.97251 | -39.04476 | 2026-10-08 15:39:00 | NOAA-21 | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| accac405-c7a6-3213-9aff-1bf283ecd203 | -14.99714 | -44.0565 | 2026-10-08 15:39:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 82897d7f-8e56-346c-b189-2ac3374856f0 | -14.57364 | -41.66429 | 2026-10-08 15:39:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 40.9 |
| ce2b634a-db27-3224-9e3a-1a0e24b0c4b7 | -11.83393 | -43.53065 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0b2014f9-11ad-3df1-a9e3-e4198fbb4297 | -11.82322 | -39.19439 | 2026-10-08 15:39:00 | NOAA-21 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 4cf25e62-e664-3ed3-babf-43a85fb8fd5a | -16.01411 | -40.65856 | 2026-10-08 15:39:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 75bccd26-9f46-3098-8000-2e6ad332053e | -13.29285 | -41.52124 | 2026-10-08 15:39:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9a098363-8dd7-3c38-b3a4-b58af697b4d7 | -11.45582 | -43.39116 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| eecc1652-4c55-325d-a6b3-d2cdf30695f9 | -15.56809 | -42.90092 | 2026-10-08 15:39:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 47f78c18-8751-3222-860b-83da55197be3 | -11.06096 | -39.50864 | 2026-10-08 15:39:00 | NOAA-21 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4d7d1a9f-ac13-3b57-a65c-b4108057cad6 | -14.43093 | -41.13902 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 46.8 |
| ff38c5d1-a0a0-3a89-815e-c1d6598ab8be | -11.75499 | -45.48974 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| d60da78e-ce25-36c3-8d53-904adced0265 | -17.42844 | -40.41856 | 2026-10-08 15:39:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| a9e8a4ea-f8c3-325f-a397-dec3fd40d7a1 | -14.466 | -40.72277 | 2026-10-08 15:39:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 898bfeba-4b09-38bf-a343-9ecb93a41db5 | -14.20274 | -41.84282 | 2026-10-08 15:39:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a8fa1350-f4fc-359a-895f-c1f11f5a4fd0 | -12.18662 | -44.81015 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 23dd14ec-2414-31e4-b7df-a2707af34355 | -14.60409 | -40.01912 | 2026-10-08 15:39:00 | NOAA-21 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 40af2926-ed45-366c-a885-0b8f097f1bb2 | -13.02026 | -41.04772 | 2026-10-08 15:39:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| da3d48d6-9c52-3b51-bc55-b877f335d30e | -14.41012 | -41.29356 | 2026-10-08 15:39:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 46.2 |
| b3309687-a6c4-37ea-a67e-ad776c0bbfe7 | -14.64628 | -41.25194 | 2026-10-08 15:39:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dddf7dfb-2538-34d7-81be-b4b4985f706f | -12.17647 | -44.81492 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 53237088-1baa-399f-a40e-18ad586cbf79 | -12.21472 | -44.81937 | 2026-10-08 15:39:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fdbd8dc2-ec9d-3da0-957f-ad223d21f2b5 | -15.38905 | -44.34425 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 29.4 |
| e0d23039-8325-3fc9-918d-964185236a39 | -14.1094 | -40.27073 | 2026-10-08 15:39:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 660de85e-ec06-30fe-a38a-47de1f793af3 | -11.76161 | -45.48776 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 3f945294-88d3-320e-ac3d-e1386ffb452d | -11.59427 | -43.66525 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e5d28048-7424-3305-99b0-3417cc105996 | -15.40193 | -44.33702 | 2026-10-08 15:39:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1026216c-d0b4-3f7f-8699-b7ea1eebbf72 | -11.32497 | -39.48414 | 2026-10-08 15:39:00 | NOAA-21 | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| f7a25bb2-40ca-3de7-ad73-0b7b4c5e7a96 | -12.25716 | -44.42275 | 2026-10-08 15:39:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f8fc257-7c89-3da3-a621-340d2aecc8d7 | -11.75575 | -45.49635 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 8382e2c2-3200-390d-9707-3714f3ec3237 | -16.82849 | -41.04287 | 2026-10-08 15:39:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 21a9aa97-5607-3827-a060-2d973aca2225 | -11.62066 | -43.62334 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ade68ee2-c66f-3e32-aa78-f4cb47f66a93 | -14.86187 | -40.87993 | 2026-10-08 15:39:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| 9af5361d-634d-38d1-aad7-bf30e989c57a | -13.38948 | -43.47843 | 2026-10-08 15:39:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| d9f68dbc-0314-33c9-8487-fe7fdef1b8f1 | -15.56693 | -42.89717 | 2026-10-08 15:39:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ee119803-cd3d-353a-89f4-91dc4b886ecb | -15.10585 | -43.63016 | 2026-10-08 15:39:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 45901d0e-3821-3d19-804e-fba65c67a27b | -16.35741 | -41.27958 | 2026-10-08 15:39:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cea21bc4-4ed8-3510-9abc-9f700897f97f | -11.77294 | -45.59164 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| db27206b-8967-3af1-ad3a-17dab6871708 | -18.25992 | -42.1795 | 2026-10-08 15:39:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| b6e775f2-64a8-3fe8-83e5-55a4ce5ae00c | -11.6103 | -43.6469 | 2026-10-08 15:39:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| d6e8e9b1-dc1e-3725-a021-55145a30279d | -15.95591 | -41.09782 | 2026-10-08 15:39:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.2 |
| 78ad42bf-5c22-3db8-a05f-582abec7f6e3 | -11.77028 | -45.56118 | 2026-10-08 15:39:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 71433bb4-2581-3a82-9ca7-2a9c6d5263ec | -16.90155 | -40.89083 | 2026-10-08 15:39:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5a1dd9ba-ed74-33f3-9a37-cbb92fa066aa | -12.0358 | -43.38741 | 2026-10-08 15:39:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 80064ffa-be70-3503-87cd-051eb4ac4899 | -16.85577 | -40.56941 | 2026-10-08 15:39:00 | NOAA-21 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 397a7a88-4586-346d-b4cb-4debbef5f078 | -12.7083 | -45.81609 | 2026-10-08 15:39:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 307b1b2d-3573-35cf-824b-d8a1d75ad360 | -16.97791 | -41.23025 | 2026-10-08 15:39:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.9 |
| 9c73d31d-b56d-39d6-b451-d1b1ad812c64 | -13.74217 | -43.51485 | 2026-10-08 15:39:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |


[Clique aqui para ver as próximas entradas](README227.md)
