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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d3741c0-5c13-3cca-a3c2-bfccdf29944b | -2.82862 | -46.67457 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d45d0e7-4c55-38ab-a46a-6b62432bbba2 | -1.73472 | -53.02861 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 87c9c59e-d10d-3ee0-87e1-7f7578f7dda4 | -1.45234 | -52.6714 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 469f3edb-2433-33ab-8482-45606d613d17 | -2.62124 | -48.18054 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5c8741a-1ef4-3faf-9fd1-e3ba4079b1e6 | 0.36992 | -53.81643 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 720c5056-7b21-3192-95dd-aa842ee07368 | -2.26619 | -45.46173 | 2024-11-20 04:25:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be039805-91b7-3ec3-88d2-c23f63131787 | -2.21272 | -46.34958 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f3c2f37-2721-3013-b149-dfb1606b0b37 | -3.09044 | -45.9814 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 089aa969-22d8-34d8-8dca-c7c60e06ee21 | -2.39366 | -49.06405 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ff67cff-9484-3f07-9417-bb4b79973bbe | -2.14658 | -49.53697 | 2024-11-20 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 554e1fd6-1539-330f-b237-997904029d1c | -2.61165 | -48.21906 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af387f58-4b0f-391c-877e-18ba2e94b525 | -1.51617 | -52.08947 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ef25094c-381a-3db6-91e9-20f6303de4d0 | -2.56271 | -46.547 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4b3d401-64db-3cd5-ad99-9b7d0c08dbcb | -2.36314 | -46.19188 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bc9c5f1-5266-3222-ba23-0ab8047812ed | -2.24758 | -46.82167 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5ae29b4-d68f-33ec-a584-aac52dc8657b | -3.00168 | -45.43658 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 091d2db8-e80e-3f06-a838-bc0082a16a6b | -1.54131 | -52.04731 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea3df43b-badf-3c6e-9f41-33828a1439fc | -2.08148 | -52.11112 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e05ffa5a-f3ed-3d5c-98ea-f72beda0ab5b | -2.18221 | -48.93283 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e0b3818-66f7-3647-ad99-3c3df9c25b49 | -2.74867 | -48.57171 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80b9e422-7039-3919-81e0-b4882d8fc16a | -2.62738 | -48.55804 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e633f7c3-36bd-3124-815c-f05a31bbcde9 | -2.79042 | -48.60283 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5657699-57c0-3c54-bd09-57c2e86fb3e6 | -1.39097 | -55.17673 | 2024-11-20 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b861910-92a4-3334-bc94-ed57ff1d3482 | -1.20409 | -51.98103 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab79f40c-d15d-3c3f-978e-1ba39470a4de | -1.46258 | -48.19646 | 2024-11-20 04:25:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41afe173-2bee-34f8-9824-5e437c7917e2 | -2.53141 | -47.51975 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2e3e104-7d59-3ae5-ab7e-a172c525dff7 | -1.71157 | -52.48826 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4db9481d-6447-35cc-9150-b26fe35e5b8f | -2.12097 | -48.55388 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e25e760c-fb12-3f3d-b4d0-aeba8c270cd2 | -2.82474 | -46.67756 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c55cd2b-eb00-30f3-a69c-b38b25f8ec19 | -0.19025 | -51.63433 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fd33aa2-bfef-3f0c-ac45-dd2d7ca1c201 | -2.49326 | -49.02689 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1c650e7-de99-3310-9158-d447d3ed3735 | -0.33876 | -51.7455 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 057dc50e-bdfe-328a-934f-3e0523f48e71 | 0.64423 | -50.73352 | 2024-11-20 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47758c94-325b-3812-9b48-db939deff46c | -1.64439 | -52.6718 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 324b7cd1-e0d8-3a34-9142-b7a2c81a75d5 | -1.46096 | -52.67779 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3135138-4d91-3d09-a601-b743e4372390 | -1.25181 | -53.36586 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| dcaa0393-e4fa-3474-bafd-c1dc13f9f908 | -2.16832 | -48.92344 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d39006f8-a14d-3a5c-a8aa-5c0a54175d70 | -1.14083 | -53.66829 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3de4a54-51a7-3a38-9bdb-db514374b619 | -2.72748 | -49.34801 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ce5ca63-6937-3a4a-8702-d6f0afbdde9c | -2.22361 | -46.47602 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc2f2d4d-ae9d-33f2-b89a-a22394bd3d99 | -3.23339 | -45.56388 | 2024-11-20 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9135f03a-8966-33cb-984f-dbd4c47bac64 | -2.28121 | -48.40768 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d033539-8194-39c6-8972-928867fbdba9 | -0.90556 | -51.73021 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6853bae-bc18-363d-8a7c-02140b3166a9 | -1.4499 | -47.11748 | 2024-11-20 04:25:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2334dd48-5bac-335c-8bb1-1322aca0b19f | -3.59062 | -43.62359 | 2024-11-20 04:25:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5213e0c3-0a46-36b6-a189-040998d69e9e | -2.62036 | -48.21576 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a4f6775-7d2b-34f8-abe2-584c44ea181a | -2.70497 | -47.97616 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c646c26f-6401-308e-96db-18cbf3ffaaf5 | -2.08895 | -46.40115 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fd81786-63b6-3532-96a0-50685f2fa996 | -1.85699 | -54.2771 | 2024-11-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 14e22728-8237-3cb5-b099-4526a617ef53 | -0.9061 | -51.78422 | 2024-11-20 04:25:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76936a87-4d35-3cf3-9428-4c5e8c1c3dd5 | -2.6218 | -47.97155 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd0a4fb9-a8f9-3906-940e-eb1d142caf97 | -1.26042 | -53.36552 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 280b04d6-448f-385e-a478-2bf4461acf27 | -2.40222 | -47.64817 | 2024-11-20 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c776e00f-7a2c-32ba-81ef-f642bc32e527 | -1.38857 | -52.5601 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7a82607-7c89-38cf-8ef3-80ee908851bd | -0.10851 | -51.43621 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27a57715-88f0-393b-a205-03a873e1b0a4 | -2.72517 | -49.33864 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d4531f2-c9c0-3619-b249-da24f2b44a82 | -1.25547 | -53.36477 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 776f478a-88b6-334e-87e1-f9e6ecb95e45 | -2.79879 | -45.99543 | 2024-11-20 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14aa2765-3f93-3bba-a72c-1c5446eec9c4 | -2.68342 | -46.18911 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcd03615-edf4-342c-a6b0-0833bb0e31c5 | -1.20747 | -51.75988 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 652f90fe-d71e-30a2-b0be-31fc5a9fc81d | -1.13852 | -51.68427 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ddb5c9b-d273-33f9-897f-116925f0a3e7 | -2.28968 | -46.87532 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41adbbbc-c847-3078-b785-0f4f43826b87 | -3.22721 | -45.27737 | 2024-11-20 04:25:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ba00f1f4-c895-3483-aedc-ac7bb2391862 | -2.66135 | -48.48104 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 540ddf2c-0d67-353d-b1b2-8b014cfe0468 | -2.82768 | -45.13401 | 2024-11-20 04:25:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82b3a135-9578-3fc5-89dd-640c78b2680a | -2.7516 | -48.57631 | 2024-11-20 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9653d07c-0dce-3074-98e7-b14dab65133e | -2.50974 | -47.23241 | 2024-11-20 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adb84733-5a2f-3e1b-93ac-b517983466bc | -2.60586 | -48.21014 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 537355bf-72de-31d4-bc4d-0f6b14d4af38 | -1.26526 | -53.40785 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f235ccaa-26d7-3c05-9b23-e515a6ecd2d3 | -0.11291 | -51.43691 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ecb126a-3d2b-3d4d-ba5c-a5f7f278179c | -1.47833 | -54.45135 | 2024-11-20 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0da0bd28-e15f-35b3-8d50-f8974101e56e | -2.48963 | -45.71122 | 2024-11-20 04:25:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc69bad3-4355-379c-be86-4fd9881c4add | -2.79033 | -48.10244 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b0d8cba-4d74-38e0-b6f3-283c3a2f50ba | -2.62388 | -48.32875 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 678129ef-3b04-3b47-970c-92396628f73b | -1.24857 | -52.03325 | 2024-11-20 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58c3756e-6a01-36b2-87c6-04bfe21f0dd7 | -1.64908 | -52.67253 | 2024-11-20 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1fc3b558-8f57-3531-8bbc-bc09214278c3 | -2.64094 | -46.56982 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 73a3e128-2cee-35de-b982-0db150cd313d | -1.23058 | -51.78574 | 2024-11-20 04:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3c1d657-4425-3984-8219-4c3a6c94ea35 | -2.31765 | -46.85049 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf6a244b-b017-37a4-8d8f-1e2a599c5d7f | -3.17818 | -46.44058 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1557c434-a2cd-3ead-889b-91e99d15a5cb | -3.08875 | -45.97058 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13870ed7-18c2-34ee-bc0c-b2dd454dab5b | -0.77921 | -51.75734 | 2024-11-20 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df73ab73-ea0e-3d15-ac5f-037424d04a9d | -2.16299 | -46.38461 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0197b33d-26ea-3fe2-a668-eb5a67831f2e | -3.32558 | -43.08164 | 2024-11-20 04:25:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0ae56a2-cd01-309a-bfbc-aaeb8ae29ed1 | -2.58152 | -46.03577 | 2024-11-20 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6f9def7-280f-3a1e-8903-67c1f5d32ded | -2.61577 | -48.21568 | 2024-11-20 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74fea37d-632f-3577-90ae-83416a3a2566 | -0.79646 | -47.79573 | 2024-11-20 04:25:00 | NOAA-21 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05da46dc-a472-3bdc-a012-b9b5fb9e884b | -2.69135 | -46.24691 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 02191ba4-de12-3072-93cd-9505dcdd1ee1 | -3.08598 | -45.96664 | 2024-11-20 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c68d49-264b-3440-8529-8d4ee1fa86bc | -2.8336 | -46.66458 | 2024-11-20 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87510972-5eb4-35b1-9f67-6044404f26fc | -2.24982 | -46.82928 | 2024-11-20 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37794a21-e6de-3132-ad3e-18311a1d4361 | -3.13198 | -45.91042 | 2024-11-20 04:25:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9889ed2-3a1c-3b7f-9873-57cc2cd6c827 | -1.90485 | -48.67351 | 2024-11-20 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f609d57c-1ddc-3a92-944b-d61964b5213d | -2.2175 | -46.4715 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f316fc0-2492-396f-b7be-1050a0332d1e | -2.69127 | -46.07388 | 2024-11-20 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb137915-0423-3d8c-b03b-245abbe3d20a | -1.58628 | -50.43883 | 2024-11-20 04:25:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a09e91d-6885-3c8f-b83d-61972cc6e6bc | -2.19126 | -48.40298 | 2024-11-20 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 29bee146-5c8d-3ee9-a00b-0ef659531cb3 | -2.22252 | -46.483 | 2024-11-20 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf429dfb-5315-3fc9-9937-fb10d97313f0 | -1.88562 | -50.97001 | 2024-11-20 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5a566b1a-c7db-3c98-b347-54b163cbe5b8 | -1.19639 | -53.67741 | 2024-11-20 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README22.md)
