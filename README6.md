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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d442fed-21ef-3954-a75f-72ad01b9b840 | -7.70615 | -47.29649 | 2025-07-20 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24d48361-19ac-3a92-a544-38b8a482dea3 | -7.9966 | -43.69126 | 2025-07-20 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c26c8778-fdc5-386f-b528-ef32375bcf85 | -11.49643 | -48.07413 | 2025-07-20 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 526a4108-bdd4-3b06-912b-c2989f5579fc | -10.96681 | -45.10667 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 6db1150d-0ae8-3167-9295-16aedbf446cd | -11.83564 | -48.20706 | 2025-07-20 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06aaee6e-f6ef-3abe-909d-e435e8a392bd | -9.09987 | -40.4395 | 2025-07-20 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 88057bed-6f00-3f9f-9f92-958d7dd63389 | -9.32949 | -41.51446 | 2025-07-20 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6da10a3a-f883-3b86-b428-0b5eb0fd5855 | -7.75295 | -42.15873 | 2025-07-20 03:49:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 87f70557-32f0-354f-84c4-0b2cd5c66834 | -10.65849 | -46.80267 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8a14e612-69d5-32a0-baca-bbf3474264fb | -8.25857 | -46.36341 | 2025-07-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7b17788-cb1e-3956-b85c-b4301d2537a2 | -9.80322 | -48.56549 | 2025-07-20 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17f057cf-d54c-3dc7-bc83-149d1b07c197 | -10.97233 | -45.10253 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 23f75933-fd67-35e7-9f05-20a33059d72d | -11.82655 | -47.50505 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fee4db3b-e392-3b98-8d1b-81ecf9fa8bb1 | -10.97688 | -45.1058 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26db872c-47b8-3c67-ba2b-c664683ab70e | -9.53128 | -40.33388 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 039720d9-03b8-345d-a4a0-ffacb8d5e8eb | -10.66252 | -46.80236 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4e6b9005-09de-38df-a70d-b83f1ce58aea | -11.49706 | -48.07479 | 2025-07-20 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ecc85fe-1802-3d44-bf29-a03322c446d7 | -12.06018 | -45.78871 | 2025-07-20 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8148eb0-2cb2-3275-a6f7-b4a5dd5613a2 | -11.824 | -47.5103 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88131d82-e82f-3ad5-95cb-028535525826 | -10.96767 | -45.10427 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 8aced0cc-4a27-37bd-a13c-2c287047ae8f | -13.89955 | -43.87172 | 2025-07-20 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9922f328-adbd-349c-a37d-505bdab2b785 | -9.53964 | -40.32706 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 37cb6a05-f48e-30d5-bce2-1ec72edfd409 | -7.269 | -43.10099 | 2025-07-20 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4912b473-652a-3918-a0c3-9d80d05a6384 | -6.36861 | -45.38824 | 2025-07-20 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f571f9f-a7c4-31fa-a653-8b7faaf249c2 | -11.55691 | -47.09315 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3622da7e-03c3-37e9-b66e-e59a3000205f | -10.9668 | -45.10915 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 242f627c-95a3-3576-97c7-810a60138ad9 | -10.01082 | -48.22573 | 2025-07-20 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d992667-b2db-3836-8d12-fb11372b381e | -10.69416 | -46.81232 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3979fe5f-be0a-311a-805f-0281ef3b3d1f | -10.66884 | -46.79704 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4fe94260-7d57-3d14-b27d-738cb0564e8a | -8.00251 | -43.68332 | 2025-07-20 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee102975-bf4c-350a-892a-3629b94b2aa7 | -7.99294 | -43.68628 | 2025-07-20 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb83629c-7a2b-3b70-8d98-d3d3092c235e | -12.34418 | -50.32943 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9dbeae45-2298-3e5e-963e-8ff9ece6f29f | -10.66138 | -46.80861 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3ed6750-d481-38e7-9813-66aa13df9540 | -11.82591 | -47.50846 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66f86963-04f5-35fc-8547-56f9dfd011bf | -11.83062 | -47.50457 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77867660-8fc7-3838-a9d7-1ff48d4b3777 | -11.57339 | -47.0959 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c48fe396-da17-31ff-a73e-90c0afd52b8f | -10.70459 | -46.78526 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97ce3155-e3eb-3f00-9c8b-16a8c8b53c52 | -11.46315 | -48.16225 | 2025-07-20 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55ff7705-613b-3445-9743-7678cc15d368 | -12.822 | -38.41901 | 2025-07-20 03:49:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bb919e0-2c66-39cf-8f58-aebe4b286165 | -10.67005 | -46.79821 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cbdb4994-8ea1-37e3-b4a8-4f90cfde0b10 | -12.29358 | -48.78204 | 2025-07-20 03:49:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02b95667-5c5d-3ba8-b1b0-5f40bb61b477 | -9.61037 | -43.86176 | 2025-07-20 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1394413-96c6-3db2-b60e-c5f14812ba20 | -10.65676 | -46.80464 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1caf8c01-a6c1-3d51-94d2-cc3a2850c2c5 | -7.7615 | -42.15661 | 2025-07-20 03:49:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e6d89e2d-ae57-3bb3-a358-1d91c1516c98 | -11.574 | -47.09274 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18c4870a-633e-3fe8-b4f7-056d2bf86c33 | -12.28789 | -48.78081 | 2025-07-20 03:49:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59ff321d-8c49-395a-b023-2f01b09fec40 | -10.63405 | -45.23166 | 2025-07-20 03:49:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a70bf53c-f3c4-345a-98f4-aa54d4ae2f0f | -10.66828 | -46.80014 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d776498f-0d45-37ec-9445-9d76b50c9dd1 | -6.367 | -45.38911 | 2025-07-20 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42977dc7-af0c-3a4f-8d97-660b1276a109 | -11.63235 | -50.73691 | 2025-07-20 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5f6214f0-7fcc-39a9-97b1-9cd324a72632 | -11.49152 | -48.07374 | 2025-07-20 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 125a7f08-57f9-316c-bf26-8d43a09d0296 | -10.66369 | -46.8035 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 40a316a7-ae80-3ef2-b13f-222093ba2e5a | -11.81466 | -47.50976 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d08c74-9960-387e-b70c-159bb41876f8 | -11.57248 | -47.09611 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a727838-217c-3f6f-aa12-65028a9c24dd | -12.34842 | -50.32287 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 18adf8da-65ad-38e1-bdad-0d379296874e | -9.27234 | -48.22873 | 2025-07-20 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 89ad600e-4772-3e00-bce8-4ce89eb2048d | -11.3599 | -48.73147 | 2025-07-20 03:49:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ce3de9f-0092-3bfe-8d2b-87c54e46528f | -7.99735 | -43.68693 | 2025-07-20 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc951721-dd26-38ea-8acb-61e7579dd36c | -9.29424 | -40.36176 | 2025-07-20 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f417cfd-6ce6-36fb-a825-54e5e021f1eb | -10.6994 | -46.78438 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ce004d6-c3a7-3ae9-8bb7-4d3f8c38673c | -10.68216 | -46.79079 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 31f68333-cd0f-38b2-aec2-4e09e5f353c5 | -10.97602 | -45.11072 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd1389d1-83bf-3b32-8d5a-5fe82b037aa8 | -10.69932 | -46.81335 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40f2d46c-3fbc-3eb7-b73a-847dca5e34ff | -10.97142 | -45.10744 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 810fe441-47e4-387a-bcdd-1e684ebc2af8 | -12.35468 | -50.32417 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f22549e-4ec7-3c66-94ba-a79f6bdcf432 | -12.3515 | -50.32562 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 71e8f8c6-e814-3c92-a333-877eca987a5f | -9.62344 | -49.0232 | 2025-07-20 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7841a81-d149-35c2-aa06-e5076e3ba121 | -9.27311 | -48.22463 | 2025-07-20 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6b08699a-1775-3363-a42e-b088edab8f42 | -9.53898 | -40.33105 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 42.5 |
| e6942926-6e5e-38f5-9696-802e8bd7d6af | -11.67421 | -37.64565 | 2025-07-20 03:49:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cca1bdc4-8456-396a-acb1-66ef27ea6687 | -12.65949 | -47.09718 | 2025-07-20 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dc7e21b-df4a-33d9-8a39-1df7882c7570 | -10.67579 | -46.79615 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 66217557-3530-3f4e-a7a2-7b48b5d53c26 | -7.95802 | -37.1861 | 2025-07-20 03:49:00 | NOAA-21 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b94cd2c-da30-3387-9dd8-a7c10413281b | -6.36197 | -45.38806 | 2025-07-20 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed161c9d-73a1-3846-b432-ac1251055c83 | -10.67638 | -46.79303 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0086073-fb9b-332f-b2a0-a884258d6cde | -10.97141 | -45.10995 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 00194090-3697-3d54-a8a1-a6a6c57639f4 | -10.69294 | -46.81882 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eb36f3b-b66a-3758-a3bb-1ef6101c07bb | -10.63148 | -45.23372 | 2025-07-20 03:49:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 60047eae-1b6f-39ae-ab7c-d75bdeb5cc7f | -9.5425 | -40.33163 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 51762893-7ad5-3e48-933c-565b62702498 | -7.99369 | -43.68199 | 2025-07-20 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ad01823-4561-3a6f-a9f2-317de9d9cca4 | -12.36507 | -50.32309 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33be40ec-f9c7-39dc-8d81-5e949b041f5f | -11.49634 | -48.07859 | 2025-07-20 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1d6b585-5146-3868-bb51-6793bae061e2 | -11.83121 | -47.50954 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30958c2e-6bea-3c2f-9264-3114866c36dd | -10.68793 | -46.78856 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51ebc84e-a50a-3c9a-b5da-919907da8c6d | -12.37548 | -50.33584 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06b37496-7250-3cf8-a6c9-49e3f4f83269 | -7.48641 | -44.71796 | 2025-07-20 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df1df13d-24aa-3888-972c-e6d1a39f4838 | -10.64712 | -44.4832 | 2025-07-20 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68151cd4-56e7-3a9b-a19d-b78ed24326fa | -10.0116 | -48.22165 | 2025-07-20 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fafdb2da-32c3-32f8-8d68-870d8a4905c8 | -10.64551 | -44.48677 | 2025-07-20 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d20a2bd-51fd-3bf5-86b6-03a4caac9d20 | -7.2906 | -39.62703 | 2025-07-20 03:49:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a895700f-ea3f-3489-bcf5-e2895cf734dd | -10.66309 | -46.79924 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 08761b89-825b-3904-9ae5-a60fb0ce7b60 | -11.57307 | -47.09295 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d246742-7268-39cf-923f-a994dd8fb978 | -9.5343 | -40.3282 | 2025-07-20 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| a3effad7-eb68-31a5-84d0-302394a444ea | -10.6686 | -46.8077 | 2025-07-20 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 95a5058a-3009-3085-961a-6cd29f8c4edd | -10.688 | -46.7829 | 2025-07-20 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 402228bc-56e3-3650-90bf-8a2f01657ce2 | -10.962 | -45.113 | 2025-07-20 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 217a95dd-f2f6-3048-a634-d72af98b977d | -10.6689 | -46.7853 | 2025-07-20 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| c16ba3ad-33d3-37df-809a-e99d127b1ca5 | -18.02262 | -44.47475 | 2025-07-20 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0bf85bf0-288c-3d55-a06d-da6a06bbca06 | -19.4537 | -45.30569 | 2025-07-20 03:51:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab672b4c-b0c5-3c8f-b064-e3ac1ea8b667 | -14.79166 | -48.29769 | 2025-07-20 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
