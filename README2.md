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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44aa3785-f7cf-3263-8161-c86f83aad15b | -17.7784 | -42.11272 | 2025-12-25 03:40:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 41e8aac9-02ff-3241-8e4b-3734896395d7 | -18.59226 | -46.55545 | 2025-12-25 03:40:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a8ba633-05b2-32cb-9962-7f40d3cf5767 | -18.59164 | -46.55201 | 2025-12-25 03:40:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31bdec88-0eef-3c2c-9e11-eaab4383e92f | -21.00565 | -41.54781 | 2025-12-25 03:40:00 | NOAA-20 | APIACÁ | ESPÍRITO SANTO | Brasil | 3200508 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fbdba5b3-db15-3b03-be7a-ba7ba1bae252 | -23.36042 | -46.39663 | 2025-12-25 03:42:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3d6a81c4-7bde-3f27-b11d-6d02dc40a78a | -23.09174 | -46.23798 | 2025-12-25 03:42:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6e99cdb8-6d32-3848-ad50-53bb66ec22ae | -22.77547 | -45.5252 | 2025-12-25 03:42:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2de409f2-eda1-3529-b888-aee24ba36728 | -5.50924 | -40.566 | 2025-12-25 04:25:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 91b23647-e4af-35e4-9d96-b8a3928dd9fd | -3.55289 | -41.62944 | 2025-12-25 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10cba765-1362-3cf3-8fab-cbc57de78f82 | -3.55359 | -41.62478 | 2025-12-25 04:25:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 65cfd502-1a29-34e2-9a6a-ca08229301b5 | -3.72642 | -38.54725 | 2025-12-25 04:25:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bc98e67c-48d9-3999-b6ab-36c7d1aff4f9 | -7.21155 | -35.28849 | 2025-12-25 04:25:00 | NOAA-21 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32698765-0e39-3dbf-a7e3-01fcccd64ce7 | -5.11034 | -40.74268 | 2025-12-25 04:25:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e490ea36-cf2d-3031-9bcb-9b9d1585978f | -7.2122 | -35.28371 | 2025-12-25 04:25:00 | NOAA-21 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d70ba881-b374-3bec-991d-504c0ca6f7d1 | -5.37093 | -35.4511 | 2025-12-25 04:25:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d6eadf93-c757-3580-aa63-e6922aa2bc6d | -11.75027 | -43.32455 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 61d9d12d-b06c-3fac-9713-c41cb2c07675 | -11.75726 | -43.33049 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46cadc47-d850-35e1-834b-526634d24eab | -11.75546 | -43.31549 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac795766-0959-3b10-9806-62d8c1ccce61 | -11.75793 | -43.32568 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f575ea6-a0dc-364d-b541-edd469b60f19 | -11.96799 | -44.21159 | 2025-12-25 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9924ee95-4053-3808-8015-dfca0f121a19 | -8.2793 | -55.11254 | 2025-12-25 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 287a4d81-7e93-3f23-84e4-cf63dd6a8589 | -12.51345 | -46.30207 | 2025-12-25 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2ecdbf6-0ea1-3e45-86c2-59534873cb2a | -11.75343 | -43.32992 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 501db98b-9e39-3edd-a9b8-e9c376af8378 | -11.84261 | -43.78864 | 2025-12-25 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6772ae5a-c2be-3984-bcb9-ac53137e2aeb | -12.91029 | -52.52085 | 2025-12-25 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a50e217a-25e5-3a42-be4f-ebbb5c4f8d54 | -13.37812 | -44.38056 | 2025-12-25 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 050972c8-4971-33ab-8517-26f69e129078 | -12.51491 | -48.37514 | 2025-12-25 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| aa2df3ad-ac2a-3f83-a886-7c8846df3a7b | -11.84568 | -43.79375 | 2025-12-25 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73cacef8-1dcf-3c33-bebd-67a6f3440cae | -8.27966 | -55.11106 | 2025-12-25 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 692bc5dc-87da-36ab-814f-7340fb616781 | -11.76109 | -43.33105 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0712d743-00f6-3b99-9846-3c81ce70c646 | -11.7541 | -43.32511 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8d50842d-587f-306b-94b2-abcc362b388f | -13.5083 | -44.43336 | 2025-12-25 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ae3207f-ba67-3d98-a8c5-e9297b8d399b | -12.51822 | -48.37569 | 2025-12-25 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8ab0221-c2ce-391a-95c0-b189135eb2d3 | -13.37748 | -44.38496 | 2025-12-25 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6febfc6a-e101-3cfd-a042-056544801d8d | -12.90639 | -52.52015 | 2025-12-25 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83a7a0e6-5dda-308a-a1c9-58c18fd9b675 | -12.09009 | -43.76766 | 2025-12-25 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66f39ca5-f020-3617-b6d0-cdd01527d6ae | -11.76176 | -43.32625 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51887da6-2ee9-3e36-b270-09cbf7109841 | -11.75095 | -43.31974 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e838a82f-7034-34a7-b32f-418f889b9845 | -10.02664 | -42.30605 | 2025-12-25 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c0b50b26-3c0b-3887-8cfa-30bdd8c59fcc | -12.51159 | -48.3746 | 2025-12-25 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cfe749d-65d0-31b5-b349-d7cbd4b60594 | -8.27481 | -55.10886 | 2025-12-25 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5349b697-5519-30dc-813b-779cd33452a5 | -8.27428 | -55.11174 | 2025-12-25 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9a94a83-e4cd-3b53-8f3d-5d730de393be | -12.90249 | -52.51944 | 2025-12-25 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ed4aebda-f976-3e2f-bd23-036d83dc5e9f | -8.27982 | -55.10971 | 2025-12-25 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c77fab4-b934-31ad-be4f-bd6452ef7161 | -11.75163 | -43.31492 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a2a5f8df-5239-3cb6-bca6-d541880397c4 | -13.28449 | -43.95636 | 2025-12-25 04:27:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caf37806-7017-36fa-807a-b4cc7ffb9691 | -8.27465 | -55.11023 | 2025-12-25 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5828f3e-334d-36e1-92d9-4f73f9b49a04 | -11.75478 | -43.3203 | 2025-12-25 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2fcfff17-470a-309e-ac25-5f3652123243 | -12.51401 | -46.29842 | 2025-12-25 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0d75948-52d8-3e0c-8072-9befe45e69a2 | -19.63255 | -44.73253 | 2025-12-25 04:29:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 686dfeb8-c51b-332d-9e95-a4ddf96248de | -20.09353 | -40.22212 | 2025-12-25 04:29:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f2b3f289-310d-3b60-af09-7bf9a8a7fbe8 | -20.38075 | -41.70983 | 2025-12-25 04:29:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 35c4f2ea-ecd7-330f-b0a6-b177f43851ea | -19.53752 | -43.61265 | 2025-12-25 04:29:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a732fc79-9b32-3d88-9880-cd1af760b668 | -15.96403 | -57.24 | 2025-12-25 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ae7ab64e-bd9a-321c-8975-0458e4470ef5 | -17.01656 | -47.25575 | 2025-12-25 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8da1532d-f989-3ed6-8bf3-0c754e59a9e5 | -16.65711 | -43.55753 | 2025-12-25 04:29:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8b7eaec-8117-3246-9751-2d0c9f82cae2 | -17.3132 | -44.92739 | 2025-12-25 04:29:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 189da5b2-e217-3ea8-8d63-2423cdc7b0bf | -18.06123 | -44.40522 | 2025-12-25 04:29:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4278992-581f-3aa3-bcd9-fbf3ac6c2c6f | -14.70737 | -48.90073 | 2025-12-25 04:29:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08552992-d52a-31b2-983a-19fe0bad2f70 | -17.01712 | -47.25199 | 2025-12-25 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| bc6bbe7c-1e2b-356c-a613-d8bf42e6272f | -17.79424 | -46.98835 | 2025-12-25 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c6e3d90-0292-3b78-904a-356b681fa4f5 | -19.2107 | -53.43712 | 2025-12-25 04:29:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8ca5ac5-5cce-3662-ab07-1e0a2f3de7b2 | -15.96848 | -57.24382 | 2025-12-25 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd04f2f9-83f2-3a71-877e-a656f838e64b | -17.79436 | -46.98881 | 2025-12-25 04:29:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 437ccdea-a736-3253-9c21-b9d1b7bc75f8 | -16.74837 | -48.79246 | 2025-12-25 04:29:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b82142b2-7000-3f53-a454-5ce154237d43 | -19.11706 | -49.05949 | 2025-12-25 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f6fac84-44ff-3c14-b82b-01a5261eebe2 | -18.84045 | -47.68244 | 2025-12-25 04:29:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cdef474-6543-3113-8180-7534f32eb46d | -20.09879 | -40.22275 | 2025-12-25 04:29:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ea48af81-c632-3c68-8d67-111d2d40bfaa | -21.07758 | -46.56649 | 2025-12-25 04:31:00 | NOAA-21 | SÃO PEDRO DA UNIÃO | MINAS GERAIS | Brasil | 3163904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1e633d42-909f-39c4-9218-d03a9a32057a | -21.26182 | -50.29907 | 2025-12-25 04:31:00 | NOAA-21 | BIRIGUI | SÃO PAULO | Brasil | 3506508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3eda725c-7f22-313f-b8fc-78f0bf8159e2 | -23.44789 | -47.21222 | 2025-12-25 04:31:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 89c6a18a-9734-317d-83b2-17c88d845d45 | -22.5311 | -48.73066 | 2025-12-25 04:31:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 901bfa73-4697-3d77-a656-0f09783f477a | -23.56644 | -47.55864 | 2025-12-25 04:31:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 996184af-5312-34f3-8d41-f0c77e8c310c | -22.84665 | -43.08354 | 2025-12-25 04:31:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f93e2881-363b-388b-aae0-afe25aab1eaa | -23.32866 | -46.7401 | 2025-12-25 04:31:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b615ef72-8696-3b9b-8ef1-f4b47e3698b1 | -23.09485 | -46.23411 | 2025-12-25 04:31:00 | NOAA-21 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6d20bfce-c6ca-3a06-98f4-2eea9bab05e4 | -22.71555 | -43.30295 | 2025-12-25 04:31:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 42ff24ed-f42b-31d6-8919-1f8f2fe7e33b | -23.56605 | -47.56081 | 2025-12-25 04:31:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b2f3ff77-33fd-36f6-a675-60a5dac6e87b | -25.2595 | -49.6709 | 2025-12-25 04:31:00 | NOAA-21 | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e498f4e-1b0b-313d-88de-eb568efb2425 | -22.77766 | -45.52262 | 2025-12-25 04:31:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b3496f70-8da2-36ce-aeb2-3f15ad10dbcb | -23.39675 | -46.28558 | 2025-12-25 04:31:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 142e37bc-2bf7-381a-a875-28b9577a7396 | -21.759 | -53.14421 | 2025-12-25 04:31:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67cdd766-8bee-3eb2-9992-ff71bedb5862 | 4.11709 | -60.7722 | 2025-12-25 04:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 891d0b3b-b982-3436-9b38-668dccbfcc07 | 4.11765 | -60.77607 | 2025-12-25 04:53:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4fd74b0a-2f14-378f-9529-5231c76ff224 | -11.75211 | -43.31606 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cb4ec8d-b1c5-3741-affa-7674cad3498e | -15.52021 | -51.85874 | 2025-12-25 04:57:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c9d1726-6cec-3053-9749-201d51413174 | -12.9012 | -52.51993 | 2025-12-25 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7325c3e9-9fa1-3580-a7cf-9a8a49b7b07e | -11.75112 | -43.32458 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3cd612f2-ba73-33f3-a877-4c58ec3fd07e | -12.30083 | -57.37336 | 2025-12-25 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19d5f75b-b07d-31f9-841a-f5145264914d | -12.90461 | -52.52047 | 2025-12-25 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9cc4836-67ea-336e-8720-045324c52f50 | -11.757 | -43.32535 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10a123f2-6d2b-33ff-b075-0cb926573cca | -11.7565 | -43.32961 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e882f922-ed25-322b-8c1e-03024753a4d1 | -15.51304 | -51.85764 | 2025-12-25 04:57:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a04ee76-210d-3e97-8b95-bb0010b3e093 | -11.76288 | -43.32611 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a959ea00-010e-3437-b213-e253c7944894 | -11.74782 | -43.31343 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dcaf026-5846-35df-8dca-27a731f85cc4 | -12.90176 | -52.51618 | 2025-12-25 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c769dbf4-ac86-3e1b-ae72-f3aebfee4dfe | -14.70775 | -48.90018 | 2025-12-25 04:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39d21918-27a9-35d9-a67c-d6e0df1b99f7 | -11.75264 | -43.3227 | 2025-12-25 04:57:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35c03a11-2066-30e3-9515-842fe4a42e62 | -12.90518 | -52.51671 | 2025-12-25 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d74bd6d-6d71-3359-893e-8d00a360df4b | -11.84237 | -43.79083 | 2025-12-25 04:57:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
