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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04955155-bf37-3f6c-930d-110e60464d60 | -8.35597 | -45.97588 | 2026-08-19 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0d0c1814-a22c-313b-bfe7-03ead36cda83 | -9.11703 | -46.04176 | 2026-08-19 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2ae1bdb-ba40-300c-a588-246ef1e71d97 | -9.39293 | -48.24707 | 2026-08-19 03:45:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb96e9b3-6d2e-3731-adc0-9b36ba896e83 | -11.10844 | -47.27222 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d64484d2-d1ca-3726-8a15-eee9e11b3cb2 | -13.40758 | -43.86771 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7924a1bf-0325-3671-b142-d53330d87c83 | -9.8152 | -46.63178 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79a064ad-f6b5-3ee6-bd23-00db9759e1ef | -11.486 | -45.10762 | 2026-08-19 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a665d45-e4bf-31dc-b156-a87827c6e1dd | -13.85183 | -42.21498 | 2026-08-19 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 78e21560-ce88-3e72-9f11-e30edbe6c30e | -7.95452 | -44.63989 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d414e73a-34d2-3588-8d6e-b6e3f3f02136 | -7.94987 | -44.63571 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54de129b-929a-3cc6-ad88-b9320d247668 | -9.73956 | -46.83977 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a419bf9-9fe0-3c95-84c8-2c907e7289d8 | -7.21754 | -43.28897 | 2026-08-19 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2423896f-4239-38ed-a2da-ebb181356279 | -7.95404 | -44.64288 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3815e619-c507-36b8-8d07-87c5f020bf7d | -13.41348 | -43.86657 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb78962b-bcbe-3e99-b818-aaacc2927b01 | -7.9546 | -44.63968 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65d2ce9b-7580-30d0-9a53-f5bfa7641959 | -11.11303 | -47.27105 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd2d34bd-c175-33af-843b-8fcc31e9e395 | -11.11436 | -47.27318 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8d4af2a-bb92-32ab-b1d2-8834e732125b | -11.12295 | -47.28256 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ed53c26-d7cb-3f04-9602-49229d94f673 | -13.41296 | -43.86385 | 2026-08-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40effbdc-e905-353c-9c39-c29f672796c1 | -7.21949 | -43.28751 | 2026-08-19 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c3883be3-fcc6-3021-b03b-13557996c6f4 | -12.24268 | -43.16065 | 2026-08-19 03:45:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ab0c5486-4fa3-34f0-ba1d-35032db3816c | -7.45306 | -45.14008 | 2026-08-19 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b59fe40b-3b25-3304-9c0d-404c4da2b56a | -9.72607 | -46.78875 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6401a728-a4b2-3549-b233-3a47da0f5fe9 | -9.73366 | -46.83884 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 211bbedb-0213-37ed-8e30-803b8bbd3790 | -7.44699 | -45.14246 | 2026-08-19 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bc5e6e4-c3b8-33e6-bf40-a18ec1e93609 | -7.02106 | -45.90058 | 2026-08-19 03:45:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 909c690d-117e-3b29-ab14-e363b5623729 | -7.94882 | -44.64174 | 2026-08-19 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e5e1fec-46f6-3196-9862-72476f6516fc | -11.11522 | -47.29063 | 2026-08-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c66b5afb-b5f1-316c-b1b2-2c07ea31b1f1 | -10.7689 | -42.08759 | 2026-08-19 03:45:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cae55c3c-ae9a-3b81-8020-6fa862ddb19c | -6.40148 | -46.63421 | 2026-08-19 03:45:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bf74106-d41b-3d59-91e3-77c8dd0fe171 | -6.90544 | -43.25459 | 2026-08-19 03:45:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a11b835a-4bfb-3c16-8ee1-06da0c5c58c7 | -9.73046 | -46.79235 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b571249-4480-3ac2-8314-22d95cefc025 | -9.72541 | -46.7871 | 2026-08-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36f38102-6383-34ca-a706-98e7c8ccc6ad | -8.55888 | -47.4132 | 2026-08-19 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42ebf80e-83c6-39fc-967f-9b151dd92a05 | -10.28947 | -48.22974 | 2026-08-19 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85d8c54f-c15a-3df0-9da7-dffe8569575d | -8.35523 | -45.97979 | 2026-08-19 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8d37e263-224d-3b98-9f20-9e3ee6135c76 | -19.6696 | -45.90994 | 2026-08-19 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 22e842ae-9d86-346c-a4f2-724bb7a37ec0 | -18.58632 | -41.32358 | 2026-08-19 03:47:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0eac1e4b-83fb-3627-91a0-66b220cac4cf | -20.41428 | -44.08899 | 2026-08-19 03:47:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 584a7088-3e54-3449-9a4b-93556e964c74 | -20.58447 | -45.93911 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de548541-5214-38f5-a023-9fd3a78b3fc2 | -17.93833 | -44.43726 | 2026-08-19 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f8a95f4-3223-3b30-a82a-d11fd2aeb7cf | -14.4915 | -45.67082 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec71dc13-5335-3cf1-a550-38206a55e168 | -21.4008 | -45.95041 | 2026-08-19 03:47:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 91312136-3191-385a-b66c-393d34f51216 | -20.29623 | -46.48485 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7341e837-8e4f-3ef8-93e6-59cd99d6727a | -16.86554 | -43.23902 | 2026-08-19 03:47:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a244e71-a5a0-3773-a87b-2601eb834fa0 | -15.06458 | -45.32767 | 2026-08-19 03:47:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47740487-4bab-33da-9150-3714f509a1b9 | -14.45839 | -45.62778 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d98c8531-8eaf-31b5-8e48-3ba8c16ba3ef | -19.67058 | -45.90496 | 2026-08-19 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81dc4bc8-fa1d-370e-abbc-c78949c8cf56 | -18.59625 | -41.33038 | 2026-08-19 03:47:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 77964f5d-0d34-3b6b-88d8-a3d1836c30d1 | -20.8802 | -45.29308 | 2026-08-19 03:47:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c10ca682-4603-300a-a053-0bc40dc75401 | -14.45285 | -45.62969 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 452a4bda-c85a-335f-bea2-e834d830edce | -20.2992 | -46.46616 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8e93e53-8a0f-3d6b-85a9-593dd4b4fd56 | -14.45341 | -45.62675 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d774b0d3-9ff5-33b5-8b09-e6b5accb1d2f | -15.00968 | -41.94732 | 2026-08-19 03:47:00 | NOAA-21 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48a14de7-b0f7-3746-b0ca-de459c41c135 | -14.49208 | -45.66787 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 539a27e3-af25-3622-b312-72bb99f39cfc | -20.28337 | -46.47151 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61e63481-d8f2-3157-8479-fbcbdd2a04d2 | -18.0057 | -44.46798 | 2026-08-19 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950e45e4-8ff6-3aeb-a120-270da7c86a1d | -20.30202 | -46.48071 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea2e9492-94f4-3791-939a-4cdd968f070b | -17.35672 | -39.74427 | 2026-08-19 03:47:00 | NOAA-21 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cc1055cc-6d0b-309e-9453-46d75ec4be2c | -19.66812 | -45.91179 | 2026-08-19 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2ac02b78-ee8d-30b4-baba-92e3853dff55 | -20.48563 | -45.24248 | 2026-08-19 03:47:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f01a6f3b-5f66-39ae-8e14-c8210eac7c5b | -14.46338 | -45.62879 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 43057de9-f4a3-3003-9de0-9740f022de51 | -20.29976 | -46.48795 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b0f11a75-473a-3a17-9add-2617319ea719 | -20.58003 | -45.93767 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 598ea116-af42-3fc8-9c8b-cd90218dba0e | -19.67279 | -45.91245 | 2026-08-19 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4aec2d76-d141-3603-bd45-f41c1ab59b8c | -15.88569 | -40.9336 | 2026-08-19 03:47:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| dcd0c408-4a28-3b9b-ad9d-916021e1c4cc | -20.18539 | -45.4053 | 2026-08-19 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e66cff0-efb0-38e0-b1c0-8aac35163223 | -16.50313 | -48.83639 | 2026-08-19 03:47:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f06dd3d-2c4e-3959-9690-c959ec9fe4ec | -17.95058 | -44.4438 | 2026-08-19 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37376f38-c5a8-3827-9968-2e7398b7e8f5 | -18.03008 | -43.01242 | 2026-08-19 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8d36c2d8-de61-3423-b28c-b59ababfdc6b | -21.39537 | -45.95414 | 2026-08-19 03:47:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fcafcb89-4efb-3e6a-b4be-e27449588b46 | -15.90506 | -42.65928 | 2026-08-19 03:47:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 76f96b19-088d-3afe-ba7a-f72a64cdb9d1 | -15.43919 | -41.38508 | 2026-08-19 03:47:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 62925cdd-81f6-3de0-97c3-e83fa1fb1ad3 | -19.87959 | -44.05119 | 2026-08-19 03:47:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1968f181-588f-31a7-9f12-43f75979ac9f | -18.59266 | -41.32967 | 2026-08-19 03:47:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 90a105bf-8ad9-39cf-8d3f-7aae7b9dee0c | -14.48158 | -45.66924 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b45f5c76-c23b-31dd-a623-f4ab074527dc | -20.28899 | -46.468 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa03f730-4e4d-3a16-9ab6-14e207c92f76 | -21.39845 | -45.95115 | 2026-08-19 03:47:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| dcfae553-3b21-3545-a464-2f900fb84292 | -21.23115 | -43.9964 | 2026-08-19 03:47:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ebda136-9d08-30bf-b9b7-560a56b6e346 | -20.32695 | -42.4059 | 2026-08-19 03:47:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d68cba4f-a3f7-38b6-9a54-076c6a475449 | -18.81392 | -46.74944 | 2026-08-19 03:47:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48e56073-bbde-3c86-9c24-a126074bf7b2 | -20.29735 | -46.47948 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cc740a94-3134-34cc-a722-54cc73ce3070 | -20.32946 | -42.40405 | 2026-08-19 03:47:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 06a17024-dbc3-3891-abef-0192074ed3f2 | -20.58119 | -45.93185 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3566295-1d39-3cf2-8538-97e251737d14 | -20.48998 | -45.24342 | 2026-08-19 03:47:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2a5a6675-09bf-3317-8ed8-962a4d193594 | -17.66006 | -40.24021 | 2026-08-19 03:47:00 | NOAA-21 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b2fe495-4a9a-3702-9e23-52f3accda066 | -15.44293 | -41.3858 | 2026-08-19 03:47:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4b6d8e33-4968-3c4a-9ddb-1ff926e6af7c | -17.92135 | -44.33826 | 2026-08-19 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 968516a5-86ea-383a-8503-bcbf13591e27 | -18.84031 | -42.00034 | 2026-08-19 03:47:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6a7aeb74-446f-3871-a9e1-ebda7fd858d4 | -14.4865 | -45.66982 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 088733b4-7467-34e2-94e3-1f1d5f092f83 | -15.07334 | -45.3257 | 2026-08-19 03:47:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b225260c-2f20-394b-8262-0580fcb4af66 | -20.58869 | -45.91799 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 367bb8d9-3a28-343f-8bca-6e6567cd6ab3 | -20.19072 | -45.4015 | 2026-08-19 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1694062c-d879-3326-95de-e95cd1428eac | -20.28435 | -46.46663 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d861d264-74e6-3981-b664-6e6ebb3ba583 | -17.98934 | -48.54701 | 2026-08-19 03:47:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a64c5f01-fbc0-311f-97b7-24b30c7499a6 | -20.3009 | -46.48611 | 2026-08-19 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 33148d75-51bf-36ed-a094-6a199c419ef4 | -20.58413 | -45.9172 | 2026-08-19 03:47:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa6aba5d-638d-3f22-822b-8a4bba8252c9 | -18.58272 | -41.32298 | 2026-08-19 03:47:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 77cca401-a912-3ae5-8bef-481783bda6ac | -14.45398 | -45.62381 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27d922c1-4078-334b-88da-b307f365c57d | -14.48151 | -45.6688 | 2026-08-19 03:47:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README21.md)
