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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57b99cb2-f10b-33f6-b9e5-1f37dfe316b0 | -23.73145 | -54.93375 | 2025-09-21 04:12:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7fd94b8f-04b4-3421-a623-5a876a80f9b7 | -22.22583 | -56.00696 | 2025-09-21 04:12:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6b1c2137-a101-3419-9d45-c3a624adbbd1 | -23.14625 | -47.62641 | 2025-09-21 04:12:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bdacdece-39f9-3560-9a85-f04fbe929702 | -19.96327 | -42.11307 | 2025-09-21 04:12:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7927c6f3-1d9e-3ab8-898c-6d18425bc365 | -23.48288 | -45.42955 | 2025-09-21 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6b9dc530-8c9e-3baa-a5ff-cb5384b1433a | -23.21852 | -47.03185 | 2025-09-21 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 5271284d-652b-32fa-b26a-7a7ed591aea8 | -18.74323 | -53.32833 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01401d07-7952-3cde-8f73-6e820f03eb66 | -23.71359 | -46.46777 | 2025-09-21 04:12:00 | NOAA-21 | RIBEIRÃO PIRES | SÃO PAULO | Brasil | 3543303 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0c7e32dc-49f8-30b8-9545-c6bfd97906df | -19.83665 | -57.29552 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 95afe776-fd07-3c9e-b153-72f248d35ca8 | -23.28809 | -46.67349 | 2025-09-21 04:12:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ff74cf69-4b83-3db9-92ea-40ecce678dac | -20.54001 | -56.1492 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c9a3367-d36a-3941-b165-0d3203cb70f4 | -23.43506 | -47.60655 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3716788-cecd-3992-8f8f-be7f26dd1432 | -23.41421 | -45.71696 | 2025-09-21 04:12:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5716d7b7-2eef-3108-894a-c9ea59e8651e | -23.1596 | -48.08115 | 2025-09-21 04:12:00 | NOAA-21 | PORANGABA | SÃO PAULO | Brasil | 3540507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c911802e-b066-3672-a29b-37a2d4e7b70c | -19.79987 | -46.67936 | 2025-09-21 04:12:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ad3028-597a-3151-a5b2-18a90742df5b | -22.13606 | -53.85368 | 2025-09-21 04:12:00 | NOAA-21 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 70f3590c-24d0-35f9-89da-bfb9bed19c7b | -20.56281 | -54.65778 | 2025-09-21 04:12:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64dab5ef-193b-3e37-b6b3-698f862659cd | -20.54026 | -42.26957 | 2025-09-21 04:12:00 | NOAA-21 | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| add0645c-ca23-318a-862c-e6bf3bf91dfe | -23.14557 | -47.6304 | 2025-09-21 04:12:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 71f2fd5f-9b3d-3d91-ba97-e013978c9604 | -23.01396 | -45.42675 | 2025-09-21 04:12:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6d58a55-e755-3542-ad32-572e8096d8af | -20.16423 | -44.76789 | 2025-09-21 04:12:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd854c36-f835-36e5-80d0-a1493f7e053b | -23.15975 | -46.64501 | 2025-09-21 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 69cb3718-02f3-3508-8f6b-7e744ae71292 | -24.75249 | -48.82112 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6498f38a-f37a-3f9c-9e9a-481a71a12540 | -22.64012 | -48.25877 | 2025-09-21 04:12:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6fa5765-cbd2-3a3d-bb90-934d71045407 | -23.28746 | -46.67731 | 2025-09-21 04:12:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ddea319-315f-35c6-8707-604226fd6df0 | -23.32504 | -46.10888 | 2025-09-21 04:12:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b16fc9ca-068c-396f-9612-ab9cc769d0ef | -23.41479 | -45.71322 | 2025-09-21 04:12:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 17bc8506-7e5b-3ac1-ad9b-2e5c2d805f8b | -19.90767 | -44.71268 | 2025-09-21 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 155cb5af-5537-397f-868f-1944de28f608 | -23.87436 | -47.83927 | 2025-09-21 04:12:00 | NOAA-21 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d6d34770-95f3-372a-968e-5eb71cb883bf | -23.4209 | -45.71832 | 2025-09-21 04:12:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 79721ffe-1be7-310e-99d6-4e4e6633b195 | -23.42242 | -47.61683 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f7133ada-5fc4-3aed-b39b-1fe3359d8a4f | -22.46866 | -48.22121 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 21d1a071-ef16-3da4-83dd-bfbb6dd7ad5f | -19.85135 | -57.30001 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 166fd0c7-1e9b-3397-afbf-481b288d988b | -23.44806 | -47.61274 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bdd5d590-10e5-3264-9668-d8bf950405df | -23.42583 | -47.61745 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| cd3e0d75-3aee-3638-91f9-cdadbb6bc039 | -22.29921 | -48.49825 | 2025-09-21 04:12:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73843302-91ab-3d31-ac45-6ad58e5ad8f2 | -23.01454 | -45.42302 | 2025-09-21 04:12:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fc7cc93a-6471-35d1-855b-c52cfa58e465 | -20.54097 | -56.14499 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a4aa9b1-4976-354d-8a70-bd5dfdfa3127 | -22.13841 | -53.85585 | 2025-09-21 04:12:00 | NOAA-21 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d5f0c675-a3b3-3f82-aed7-ebcf35c6195d | -22.96572 | -46.58207 | 2025-09-21 04:12:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0d1ccef8-863a-35ba-86db-8dfaca30e1bd | -22.17253 | -46.74076 | 2025-09-21 04:12:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7526e8f8-e7b8-3730-a162-e5ccb85e219f | -18.74414 | -53.32743 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ea7a9ad-ffaa-3306-adf8-aa0943511bc3 | -20.13393 | -42.49017 | 2025-09-21 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7da69ec4-2b81-3b56-8b0a-4530c095445f | -19.83776 | -57.30207 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f7ad47ed-7d9c-3410-ba3f-4fc724855a6c | -23.24257 | -50.85787 | 2025-09-21 04:12:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 4eab6d41-a309-3322-ad62-edd2833145ca | -22.30004 | -48.49926 | 2025-09-21 04:12:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0ad3be34-fd30-3eb5-b5d7-d7b119d8c493 | -20.25084 | -44.36229 | 2025-09-21 04:12:00 | NOAA-21 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6a895d87-4ecc-31db-8d4a-a518d6b5c749 | -22.70387 | -51.56132 | 2025-09-21 04:12:00 | NOAA-21 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e8b69ba2-d370-3b7a-91f0-748ec590bf52 | -18.77043 | -53.34846 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 685a5cd6-01c2-3e7a-8184-1fd3adc341aa | -23.37506 | -46.02956 | 2025-09-21 04:12:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ae9f3f8c-5fc1-3695-acd7-9536aca1ea5a | -19.91041 | -44.7169 | 2025-09-21 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ee8b59f-1ffa-3d71-8559-3295b3b4d751 | -22.18638 | -51.43145 | 2025-09-21 04:12:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8592ecc3-19cc-3870-a232-8f6153b57c2a | -20.53374 | -56.14896 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe229e04-87d0-3106-bba5-7bf17186f357 | -23.21916 | -47.02799 | 2025-09-21 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ce02012e-fca2-34ed-bc48-ef8514e05dac | -22.98771 | -45.78956 | 2025-09-21 04:12:00 | NOAA-21 | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0fa801d8-b3fa-339b-a7b4-5cd63a392e2a | -23.73079 | -54.9368 | 2025-09-21 04:12:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9150a518-f704-386d-b51c-e20d995d2cc5 | -22.96634 | -46.57828 | 2025-09-21 04:12:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3349b386-18f4-3b67-b27a-4cb2cf0cb58a | -22.49874 | -47.54068 | 2025-09-21 04:12:00 | NOAA-21 | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d6251374-9121-3338-bad2-60bfc43861e1 | -22.47291 | -48.21766 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b3fb0961-fd37-35fe-abfd-b4b788a837a2 | -21.30295 | -44.63997 | 2025-09-21 04:12:00 | NOAA-21 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1f957986-a80d-3224-bf16-962b7da07ff3 | -23.18159 | -46.70018 | 2025-09-21 04:12:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c515df6a-e69f-3c7a-ab74-7a1c1ecf27ba | -19.80392 | -46.67612 | 2025-09-21 04:12:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dee2dca3-9962-38cc-8fcb-7ea1b88561f7 | -21.22014 | -48.32407 | 2025-09-21 04:12:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7dd1c848-2f18-3bfd-8dc6-46791c9e38ef | -24.75692 | -48.82028 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5e0b6bae-7826-3cf5-a2d2-00731f438d44 | -20.59714 | -42.87124 | 2025-09-21 04:12:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 150f83a2-e9e0-378d-864e-0791d589601f | -20.60478 | -56.72153 | 2025-09-21 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a09e3075-a61c-3084-ad8f-af297e193b30 | -23.44466 | -47.61212 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d665c019-9691-3a84-9e05-c7e50d79d2f5 | -20.14145 | -42.48706 | 2025-09-21 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a6725def-5136-3060-8efb-a5d9977e37e9 | -23.32868 | -46.74021 | 2025-09-21 04:12:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd135064-b44e-31bf-8623-04a6c40deeca | -22.70544 | -51.55319 | 2025-09-21 04:12:00 | NOAA-21 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a0059b7b-775f-30f0-b57e-6d0785b35949 | -19.663 | -45.35617 | 2025-09-21 04:12:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0850ea1b-6033-3416-9565-6cffa9fbb540 | -22.47441 | -48.20914 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 766364bb-fe4b-3715-ba21-9413fdc4dfad | -23.53283 | -47.60938 | 2025-09-21 04:12:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 60539f72-d07b-35fd-afd2-240854f936b5 | -21.69566 | -44.26779 | 2025-09-21 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 551391c3-e254-3e04-9478-8b8d7b69de4d | -22.70466 | -51.55725 | 2025-09-21 04:12:00 | NOAA-21 | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 69b5286a-cf1d-3e22-8907-e7d377d3a5a9 | -22.47216 | -48.22192 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1918a7c0-f27e-38d8-a9eb-056adb798faa | -23.47906 | -47.2775 | 2025-09-21 04:12:00 | NOAA-21 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43b1ecb1-630d-3f96-b63b-c956fe50111f | -22.38316 | -50.04239 | 2025-09-21 04:12:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41a8cecf-308e-3184-8cec-bb28b86ec4ed | -23.08702 | -45.54688 | 2025-09-21 04:12:00 | NOAA-21 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d471bc04-421b-3516-93d7-58ee86f05289 | -24.6884 | -48.33191 | 2025-09-21 04:12:00 | NOAA-21 | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ef5c139e-2ebd-3002-93c7-437ef24ee5e5 | -23.477 | -47.26898 | 2025-09-21 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0bab9e09-ba48-3f7b-9b56-114a54486286 | -21.12269 | -42.98848 | 2025-09-21 04:12:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| df4f0612-ec8a-3078-a5bd-44f1edf2b364 | -22.46585 | -49.01624 | 2025-09-21 04:12:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5a7ff4c-bfdf-32b4-bf14-3ee144d6bbdd | -18.74385 | -53.32535 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 292b2d94-d23b-3698-beb6-903295d76081 | -23.41819 | -45.71397 | 2025-09-21 04:12:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0b82a1b2-f3e6-3fdd-bf17-278db13bdb1d | -23.01785 | -45.42362 | 2025-09-21 04:12:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1483b3cb-88a7-3485-8ac0-168f145b9f26 | -22.61822 | -47.70893 | 2025-09-21 04:12:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ad999458-bca2-3c54-9d9a-4a3f46be29dc | -20.12702 | -42.489 | 2025-09-21 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ec4667bc-06b2-342f-9c2e-4ad7d2b0ca72 | -24.75423 | -48.81507 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 29fd6d2d-3b9c-3074-b70f-de445f4e8f4b | -20.5404 | -56.14622 | 2025-09-21 04:12:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37af6db7-8960-3e8c-9712-74dcd68995bc | -22.1874 | -51.43066 | 2025-09-21 04:12:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0e36a337-745b-32eb-a228-7115981946bb | -23.14284 | -47.62576 | 2025-09-21 04:12:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3e8afee-0a5d-3771-84fb-a8cf984df2f5 | -18.73853 | -53.32934 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa450549-1bb8-3ba4-995e-5c07d5e71d09 | -24.75773 | -48.81577 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 1b2872ca-8fcb-3578-98c3-3ab8dc7856bf | -23.42208 | -45.71083 | 2025-09-21 04:12:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b69e418f-655e-35a0-9ec5-19f6c18606ed | -23.40299 | -47.46159 | 2025-09-21 04:12:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dec341d1-2849-35cf-9481-f55b192b1d18 | -24.75677 | -48.81728 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1f0bc8e3-7357-31f2-b1fa-b0bbd15b21b9 | -23.5315 | -47.6173 | 2025-09-21 04:12:00 | NOAA-21 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43764f07-f336-36f8-aa0b-cda7d5b6882b | -23.16308 | -46.64564 | 2025-09-21 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 719d2e44-01ed-3069-bf7a-e2dcdc35bdf1 | -24.75327 | -48.81658 | 2025-09-21 04:12:00 | NOAA-21 | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |


[Clique aqui para ver as próximas entradas](README19.md)
