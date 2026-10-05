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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcb2fb8c-a502-3440-977d-10725cdad86d | -6.69431 | -45.24339 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a314bdd3-1149-3783-ad3d-1b120b2cdb40 | -11.07821 | -41.26112 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0416b5e9-476c-3dbd-9442-854f37e45678 | -8.54523 | -54.58214 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 502edc07-9aca-3afb-97ee-d89c93d472b9 | -6.3197 | -43.34671 | 2026-10-05 16:37:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| e928a58b-3525-36a8-b774-0da65abae929 | -8.15217 | -43.88346 | 2026-10-05 16:37:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fd5666df-a043-3446-8e3c-6923775a4209 | -9.40893 | -47.30599 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 90b248cc-f4e5-3454-81cd-41e96ae0018a | -8.0018 | -35.08557 | 2026-10-05 16:37:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d75aa4e2-d896-30f3-956e-3ffcc72dc133 | -6.85649 | -38.6736 | 2026-10-05 16:37:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a9665daf-887f-3105-94af-df1a2f30ae95 | -11.67989 | -47.2979 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5cfe1800-419d-3f72-9413-7c058e8f2e24 | -6.68498 | -45.22913 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 55d8b23e-3a85-36ab-8443-7e35f9d3d634 | -18.58706 | -41.28211 | 2026-10-05 16:37:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8df25c78-63dd-38e3-b810-2d81d4c44ba2 | -6.90025 | -43.67821 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 7c7a166d-1f20-38aa-a4e7-5576353a39aa | -11.85617 | -46.79813 | 2026-10-05 16:37:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c34272e-d777-392a-af49-14a3a99b06d2 | -12.51081 | -41.67931 | 2026-10-05 16:37:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 35918441-63ce-3d6e-8e41-4ee42297d66d | -6.69762 | -45.21918 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 6d719841-65d3-36d0-908d-b29c9ef74ce2 | -7.26712 | -39.30439 | 2026-10-05 16:37:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 10b153b6-c4ef-3254-9f43-5d389d146600 | -10.97274 | -45.42459 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| df045de4-3446-369c-a72e-d454e43162fd | -9.96599 | -45.5997 | 2026-10-05 16:37:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fc76bee3-91b5-3adb-88c3-95995216a8bd | -8.54047 | -54.58279 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4631868d-6518-3272-9550-2c9bb4ae3f78 | -11.71273 | -43.63826 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a50bdf0d-3802-34c2-a008-3a831eef2ba3 | -6.28272 | -43.08284 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0df33b69-550f-3f21-8dad-939d066b4b44 | -9.87282 | -44.81174 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6b274250-eb8c-3887-a2ee-88e4c94abd54 | -9.61375 | -45.82468 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5428da3b-64ce-3f1d-b7a0-2570e5bfb237 | -11.70405 | -43.43074 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7856e025-367f-34a7-a6f6-b8a5261c7239 | -7.87476 | -41.2566 | 2026-10-05 16:37:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3c17d883-f6d8-36c1-bdb7-91b642456d0f | -11.63854 | -43.62867 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf42eee2-8d14-3a77-b7df-ef7d771a9ca7 | -18.39439 | -40.7941 | 2026-10-05 16:37:00 | NOAA-21 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f9b4f465-3a69-3aa0-b56d-58868d865c46 | -10.12033 | -45.89175 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| e81659e1-9947-383d-b7b7-d6a1c260ef46 | -10.97664 | -45.44963 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 7e9987cf-1b59-3aef-8ffa-087bd159c389 | -8.49803 | -46.90232 | 2026-10-05 16:37:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e17f715a-86b5-36cb-acfd-b12726f4fdcf | -9.84052 | -47.01593 | 2026-10-05 16:37:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4173a031-eca7-30d5-9054-f1e0ddb8e92f | -11.08288 | -41.2641 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a6ce05d4-97b3-3963-8841-7f318441f19b | -7.48163 | -45.07596 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b415511b-44f0-3936-bba6-0e1b2ba7c3de | -11.88769 | -40.71819 | 2026-10-05 16:37:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 00935ee4-81f9-356a-9b76-6fddfdf5990a | -7.02812 | -43.43251 | 2026-10-05 16:37:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| bec35a29-4d9f-3f2e-b7ad-40225d42afdd | -6.61871 | -41.76931 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 9ab255b1-8cdc-3471-a8dd-896a38b3280e | -6.86826 | -40.24361 | 2026-10-05 16:37:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6a33d0c1-8ff3-345e-adc3-832f38bd641d | -10.97552 | -45.44248 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9ea4f278-dabc-314a-a8e0-3d9d0bab0a69 | -11.83518 | -43.5438 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d948ef8-0107-3748-a691-e6b92f9c17c3 | -6.90626 | -43.66793 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 660b6a86-719b-33d1-8093-439b4e286616 | -7.76469 | -40.27764 | 2026-10-05 16:37:00 | NOAA-21 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4b1fe311-5f11-3615-b2a7-87cb5f4f5ffd | -9.84407 | -44.78554 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| f3c2a2e8-2fe4-31ce-98a4-97748d8c5da1 | -11.10877 | -46.08504 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| da199eb1-dbf0-370f-80f7-87eec73af27a | -6.80579 | -39.29507 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 8ccf3134-9f68-3fbc-9771-d557cca02cd3 | -9.85956 | -44.79454 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| bafd0c9d-3ee6-3ec1-8b21-e7ac3c746824 | -8.03475 | -46.98341 | 2026-10-05 16:37:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6bc2d6d2-b1c0-310f-a109-546d4afe2b04 | -11.6392 | -43.63274 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dab8bb10-25b9-337e-8523-78cc8186725f | -8.66706 | -54.5434 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 22b2aa2f-e19b-3840-a95a-fb72e212ae16 | -11.68253 | -43.65454 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5a68ac7a-abfc-378f-a5fc-daa27eab1cf4 | -11.37844 | -42.55063 | 2026-10-05 16:37:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 97a1a1b0-029e-3a79-96fc-43b8f881d880 | -10.39343 | -47.52861 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6251ca27-fdf0-37a7-8943-720e661b0b54 | -6.69682 | -43.69355 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5fbc44a5-1bf5-3825-9647-bcd439bca929 | -11.75173 | -43.5443 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| fe0fbe7f-60e5-3c0b-9f00-3f6d64c7ccbc | -6.69943 | -45.23076 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d6e8cfa7-1d16-3e6c-9963-1a63de236055 | -8.52809 | -39.54786 | 2026-10-05 16:37:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 13.9 |
| adf83ebd-c106-356f-a9b6-01a2e1daa4b0 | -12.19641 | -44.65751 | 2026-10-05 16:37:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 677c4596-9b02-33c9-80c7-37022f1a5f77 | -11.85462 | -47.31018 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5fbb3500-b1b0-3d47-8c55-0f123eeb3593 | -7.65606 | -44.3757 | 2026-10-05 16:37:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a5631450-b26d-33da-a933-efef2837d8d1 | -11.83026 | -43.5359 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a49d7e6f-59b8-34db-b29c-e1123747248b | -12.86153 | -39.92548 | 2026-10-05 16:37:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 90554efe-2a20-3c05-9bc9-83558e56c56d | -10.49482 | -46.04802 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b048ad9a-7ada-3929-b701-3ebe4e5d32af | -9.15031 | -45.12691 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0c6ff12b-3ec5-3764-a725-31ec971935fe | -6.33992 | -42.55079 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fdb23030-3366-35ed-bcac-d76d74acfbba | -7.2372 | -40.2497 | 2026-10-05 16:37:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bbf903b5-5270-3514-a5cc-02f7e4d9cc5c | -11.67549 | -43.65574 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73e4bd08-2326-3f4c-88a7-41a7db16bac0 | -11.0034 | -47.86216 | 2026-10-05 16:37:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e85177c1-8bbf-3b18-91cb-535d9cc604ca | -11.07112 | -47.49543 | 2026-10-05 16:37:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 569eddde-819f-31d2-a1ca-628427b6fedb | -11.37471 | -42.55127 | 2026-10-05 16:37:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 20876314-aa88-3c6b-9683-b5c8f53043b1 | -11.82741 | -43.54066 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 644a2162-5697-3f69-8973-656f9861978e | -9.87761 | -44.84188 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61417ec9-4bdb-3acc-8d8f-8889e3a65cd7 | -7.49553 | -44.41765 | 2026-10-05 16:37:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 84e717db-70dd-3726-9f30-9eff617b0ebd | -11.2812 | -44.28732 | 2026-10-05 16:37:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 41f902c7-fb8c-3ae5-99c9-f448d8cee2e8 | -11.07883 | -41.26479 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a705d577-b0bf-3092-8fb5-0aba72f1370a | -8.17071 | -44.42018 | 2026-10-05 16:37:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 1dd92092-1378-32b5-a030-356092d73814 | -6.7223 | -43.99741 | 2026-10-05 16:37:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| eb264e4e-227a-365d-9979-fe56238f87ae | -7.5372 | -45.40325 | 2026-10-05 16:37:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3cbd18de-3766-3a7f-b268-c9472d270e7f | -9.74954 | -48.17341 | 2026-10-05 16:37:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 286380ab-37b3-3e00-a70d-4bce6c9a0ebe | -8.66026 | -54.56518 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 922a4749-980a-3567-bcba-d8535c32f357 | -8.73448 | -47.07111 | 2026-10-05 16:37:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 128361e1-f574-3e9d-8362-c0cc9b1dbe60 | -6.43018 | -43.72125 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4440f0b0-ed86-36f1-bbe5-4f6dadf6962e | -9.6193 | -45.83844 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6eebea7e-57f3-3a95-9de4-88d3af06f2ec | -8.60554 | -45.66071 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a4c79cc-4a93-36e4-909d-ec475512d862 | -17.89354 | -39.43071 | 2026-10-05 16:37:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 8c618cdc-f6ba-3efd-a6a9-c2baef964d2c | -11.20079 | -40.55093 | 2026-10-05 16:37:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f6d53720-8b1e-3063-bb98-470283f44ecf | -12.86586 | -39.92491 | 2026-10-05 16:37:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 35a66c64-e96e-3ad2-b760-f2c7a77ff727 | -13.00777 | -39.72706 | 2026-10-05 16:37:00 | NOAA-21 | AMARGOSA | BAHIA | Brasil | 2901007 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d2e33a3e-6c89-368e-b815-5470910fdbc1 | -6.91069 | -43.67181 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 63cb1af2-1b48-309d-bb79-b0768d2fa7f3 | -9.03074 | -45.16892 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2add319d-bec1-3702-8834-cba68c0cbecc | -18.52225 | -43.62743 | 2026-10-05 16:37:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 464d23a7-84ea-3ea8-93b3-ebdbaf26ddf2 | -6.70123 | -45.24228 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| b31a1870-68b2-3c1d-8150-7f90a96e13b5 | -8.6567 | -54.5468 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 01aa6af1-5aa9-315a-8643-0e66b75c3593 | -6.70349 | -45.23405 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4ccdd2b3-1f1f-36de-9a4a-aafd6e56ecb2 | -11.67836 | -43.65113 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11efa8e7-6826-38e2-9b50-d8a90a789036 | -8.53135 | -54.59251 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 554f79cd-02c0-33c6-bb6b-129bfe9de05f | -11.3479 | -46.67076 | 2026-10-05 16:37:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 97ddd537-46f6-3691-bad8-e9622421f620 | -7.19552 | -44.30781 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2582bf76-1227-3c63-acea-826669ff6555 | -7.53454 | -45.88028 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 71642c61-4efa-3edd-a1b9-7c12b4754fa2 | -11.37231 | -47.6278 | 2026-10-05 16:37:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b4f1622e-8064-3882-9918-7d63bc32ea74 | -11.44496 | -43.53136 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 15df2362-c54b-3393-9be9-dbd10d598fd5 | -6.69475 | -45.22358 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |


[Clique aqui para ver as próximas entradas](README85.md)
