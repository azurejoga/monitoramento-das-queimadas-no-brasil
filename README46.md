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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81eca4a9-e369-336f-85ee-c570295482f2 | -12.60635 | -46.94938 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| abf36b65-c961-3591-9207-303aeb853201 | -12.82827 | -46.01079 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efca0bb5-73cf-3661-980b-1b239cb76da5 | -11.34078 | -55.43006 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6509c8f1-deb5-30db-86fe-1daae3cb8e97 | -13.11332 | -57.16964 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b48c61d1-4203-34d0-8c87-1d28ebde0aee | -16.2344 | -51.12395 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df2273df-1eb9-3775-b30f-071d39ce2679 | -16.23499 | -51.12031 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5746750-e568-351f-b2bd-e2967b612d59 | -12.59586 | -46.92366 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ccc5296-baa9-35c7-a4ff-d52b6fafe2c9 | -10.966 | -49.56683 | 2025-08-16 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d789a7fb-7efe-35e5-bd34-1f034e8d6f91 | -12.58946 | -46.94305 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8bea45f-fc0a-31b7-b065-44b5c74a2c06 | -8.10862 | -61.19204 | 2025-08-16 04:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 562f3a0d-b9f2-391d-8bfd-8d15fb887734 | -17.61108 | -46.68139 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 820a2a04-da6b-328c-ab3d-9023fb787e42 | -9.51054 | -60.53265 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a38a5a8d-22db-3b39-840b-a313bc99dfc0 | -14.5862 | -47.93497 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3cd6280-4b17-358d-937b-96b66711df84 | -9.20141 | -59.63626 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e0279bf-ace7-3ddc-a5c0-d10188b2eba5 | -11.34437 | -55.43518 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02202ec1-7c5e-3e09-8a85-7756647ea496 | -15.50893 | -40.75385 | 2025-08-16 04:34:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4eb7d47-fb2c-3d51-9b19-0bf9fa1bdf48 | -13.48225 | -56.65899 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f260dcb3-220b-3c75-8db8-5219e353e446 | -12.60174 | -46.98071 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8f49631-cb2d-3c6a-ba31-abd77e2e6f20 | -12.56711 | -46.96434 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59fd6412-29ad-3b2c-82e4-d329846e1f64 | -11.54847 | -47.26754 | 2025-08-16 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e2870ac-b426-329d-97f1-a49192d0448e | -12.82917 | -46.00338 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8303f86d-9002-34ef-b571-3aee0eb675b6 | -13.65259 | -44.19712 | 2025-08-16 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b2b6c65-039d-3c8b-945a-1ab18d6f91ca | -9.16046 | -59.62407 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| beef59b0-9857-3a73-b463-3c665ba26b2b | -7.94346 | -61.75048 | 2025-08-16 04:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38ddfc94-e766-3b44-8873-67f9ccb9570d | -12.59409 | -46.93574 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ad45dfb-aa73-3936-9936-1d772d88d283 | -9.21765 | -59.66218 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bafd3151-b9dc-375f-bbdf-a6409c1c36b9 | -12.82586 | -46.00147 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5a3d62b-1bc8-3cef-89d9-64a69c0a84e1 | -12.59468 | -46.93171 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fce6643e-36ac-334e-86bc-3295dce6287e | -12.62242 | -47.8709 | 2025-08-16 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cafae921-d786-355e-884d-07c461de1772 | -16.2244 | -51.12228 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8eda948-9bc1-32b9-9410-0fcffdc847fc | -16.23655 | -51.13187 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e56ec535-ec11-3c10-aadb-45259fdc89e8 | -12.57117 | -46.96096 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3d9f43f-9e9f-3f0a-841d-fca44cd17221 | -8.9863 | -60.53226 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 602e4055-4579-3cc7-88d8-89bb9f91005f | -13.58424 | -46.97775 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e81c668-8fe6-30f3-9671-bf683f018333 | -13.87111 | -45.55855 | 2025-08-16 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b47a2872-7f45-33df-94f5-f2f22c55c96e | -12.58715 | -46.95882 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a83bbf91-ecb3-3eb2-a2c1-38c3d31398bd | -11.35745 | -55.43758 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a7a07db-7267-3c9d-b38f-71afac24d2d6 | -17.21355 | -49.58467 | 2025-08-16 04:34:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74cd44f8-eaa4-3597-b81e-bec1b0241d14 | -12.03228 | -63.33682 | 2025-08-16 04:34:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 198e6f19-660d-3603-a297-2477d73b03de | -12.60577 | -46.95327 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| acabd3bf-1994-3bfd-94c9-b4ac7fc0bd69 | -13.61247 | -46.9076 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4632154d-00c4-37d2-abdc-807e809e6a9d | -14.93501 | -54.71026 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3bb91c93-3978-3424-af77-ecf0a2a7983d | -12.59527 | -46.92768 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c06380ae-b615-3d4b-8337-4241ffb48fb4 | -12.6156 | -46.935 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 208003f8-e025-301f-965f-7e961e6f248d | -12.82788 | -46.01215 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 01799aab-884f-34f9-829f-c07cd84a687d | -16.10555 | -47.5582 | 2025-08-16 04:34:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e152f37-e22b-371a-9a6d-ff30a28d362a | -11.36181 | -55.43839 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b13c774-93d8-3f0b-bac0-0df86b0588f1 | -13.63706 | -46.91196 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29cc44bf-c4b6-3011-98c0-c7043b846914 | -12.82581 | -46.02819 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6df9f3aa-38cf-3614-83cc-a76ccfb954e7 | -7.95598 | -61.75962 | 2025-08-16 04:34:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5f55978-a3c9-3bf0-8f1c-c5293e60ab84 | -11.35847 | -55.40674 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3312bc64-878a-349b-9d99-c0728ffecbdf | -8.96972 | -61.68097 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5734e2cb-2162-38fe-aec6-cd3ecd8ec717 | -16.22773 | -51.12284 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af4f30c4-ab8c-36d4-a277-68fef6f191cb | -12.20614 | -47.24649 | 2025-08-16 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7869c22-f180-34d6-a417-c66cc6e0e84d | -8.98592 | -60.50035 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9a334cc0-dbe8-3822-9321-b3f1e9abb6f1 | -12.82487 | -46.00725 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c49a60-c374-3eb8-b8be-a1b7d4573086 | -12.56128 | -46.95567 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5b6bc5d7-a992-3f07-8ac8-6b7e23e2c166 | -14.06281 | -46.29542 | 2025-08-16 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c097ee10-3d9d-38de-bd8b-6aec26c2d5d5 | -12.59758 | -46.93631 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2fe64f41-8cf7-3c7a-b78b-74f53ff6ee82 | -12.99811 | -56.86881 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06f82f44-8619-3ef2-b01c-d3ffaa0d3972 | -16.7513 | -45.06234 | 2025-08-16 04:34:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 214143b8-676d-3907-9592-18d0cc917d10 | -14.97353 | -54.72156 | 2025-08-16 04:34:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 767635fc-1a2d-3a10-901f-1ca29438f21a | -12.46856 | -46.98093 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da6b4b19-0b9c-3473-8e05-dd86a086e280 | -8.98962 | -60.54904 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b6da3da-58c2-3afd-b1fa-e204fbae52fe | -12.82765 | -46.01516 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8acb1782-8e73-3d3b-9192-25f8748a81a5 | -12.58888 | -46.94698 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 778ee92a-3b66-3d8e-a0bd-19569635efae | -9.20249 | -59.64464 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9848d101-8ebe-3721-801d-af37acdb1bcb | -14.94088 | -54.70018 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cfc1f539-a7ed-3a38-9cdf-b10f212a3075 | -8.98532 | -60.53736 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ec65e6a1-1439-32e1-a572-c2c41d65cdb8 | -12.5642 | -46.95997 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bf7d733-eed5-3c58-9e9f-20602232bd42 | -13.5709 | -46.97065 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bfb86792-f1a5-34ea-a858-ff290faf6421 | -9.50053 | -60.53257 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a72cee3b-de55-324a-8eec-9b407b1ba154 | -15.57481 | -49.67272 | 2025-08-16 04:34:00 | NOAA-20 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5cc7acd2-c7da-3dcd-9aea-f911a7d6d0ca | -9.16557 | -59.62975 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 13bfee52-b93b-3db0-849e-f7ebbd0dc96d | -10.35434 | -49.92921 | 2025-08-16 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d66c260-c8f8-3aef-9ac1-edce44dad9bf | -9.15797 | -59.63718 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 30d9eb06-114a-3c60-9962-c31b96d2a08f | -14.86964 | -60.09122 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 28aeb571-e147-38af-b197-d4b52da84146 | -12.5555 | -46.97049 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b93c8ebb-7e42-303a-98af-685a67d6ce43 | -11.35977 | -55.42461 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c22fcc6-4e04-3072-aa21-380514658d04 | -13.44633 | -56.67379 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80b47579-ec61-3809-98db-070eb13438b2 | -14.9399 | -54.70562 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 885c9915-b040-3b1f-a3da-30c8d0a3e7de | -9.50657 | -60.55297 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99b13bec-0739-3ff3-abeb-27b9c56c4d3d | -16.22381 | -51.12588 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1785aea3-0b79-35bb-8cec-dc1165b6586c | -12.45743 | -46.99572 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb2b89ef-eadd-36e2-8093-ab9f4515979b | -13.42421 | -43.68243 | 2025-08-16 04:34:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9a2d86c-34f2-35ce-aa67-3b0e466fbaa2 | -9.16055 | -59.65611 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 705bd3ac-8731-37de-a172-861ad425920b | -10.5061 | -53.59068 | 2025-08-16 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47f2b1ed-c882-3ffa-898f-a9e01443a657 | -14.58961 | -47.93551 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80457d15-2f88-3b36-bbe1-68586308bbf2 | -13.13228 | -57.17344 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08c28b26-eb9c-3b7b-af27-bef8e4be85c7 | -14.97142 | -54.71062 | 2025-08-16 04:34:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94dab6db-18d8-3134-a778-caf5854e75bb | -9.15115 | -59.67294 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f801b2cb-5256-316d-aaea-fb3ae6fc3044 | -12.58655 | -46.93856 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4be2353e-0dfd-357f-b38d-ccad37c7ba7d | -13.13424 | -57.16287 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6faa34c3-6ffd-3711-a317-7f4cf5238f3f | -18.22827 | -45.22082 | 2025-08-16 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63ef1d4f-930f-3363-a9f6-cad07f6fbcb1 | -9.15201 | -59.63597 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b34fe8aa-2584-37ac-8e50-adadc2281f36 | -13.58484 | -46.97364 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50abb963-b508-3e93-b12f-87fd66fc0c2b | -13.5866 | -46.96161 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d977055-4df2-3e7f-ae2a-d16fcd8c2359 | -14.58962 | -47.91224 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff4aa2eb-75cf-36e8-9a56-56e9b64ee684 | -12.60984 | -46.94989 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f5604f3-9f0b-3e44-82d6-a0347fa47645 | -8.9869 | -60.4953 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |


[Clique aqui para ver as próximas entradas](README47.md)
