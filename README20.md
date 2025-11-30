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
| c043d4ef-4265-3ec0-87e8-40e4c0b07106 | -23.54977 | -47.207 | 2025-11-30 04:50:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 50cbd18e-105a-399c-b1ef-6bed252c510e | -24.07482 | -51.05427 | 2025-11-30 04:50:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9a91ed21-5252-3f6d-800e-844996e8179a | -23.78827 | -53.06324 | 2025-11-30 04:50:00 | NOAA-20 | CRUZEIRO DO OESTE | PARANÁ | Brasil | 4106605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ff3e0eb6-0636-3f16-9741-f382dc383727 | -19.93178 | -57.43989 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 94d1e148-0cdf-3529-ad58-d8546cc12647 | -19.84365 | -57.77277 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 5043790c-d3aa-31ad-aed9-60907b3db598 | -21.17627 | -49.18228 | 2025-11-30 04:50:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e37872b3-db02-3b55-a372-01cf98545104 | -19.8416 | -57.7631 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4ca47c43-1602-3b3b-a783-6661dd5a7492 | -21.1533 | -48.61518 | 2025-11-30 04:50:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 20e65c86-a10f-3ec5-80b7-80f3f70cc65a | -19.85659 | -57.78465 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 437e1053-1620-3d19-9688-44555c8a49f5 | -20.18739 | -52.38161 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6562d657-2bc2-30ae-8dcc-c81eac08ec7d | -19.8449 | -57.78695 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8362761e-eb43-3a7c-88fa-5ff533219e54 | -19.9267 | -57.44783 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 85248a64-dbfe-3739-a626-6be9e293449e | -20.18113 | -52.37658 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f4613b1-771c-3a1f-b6c4-20b4e3e243a0 | -19.98084 | -47.84246 | 2025-11-30 04:50:00 | NOAA-20 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c92fdd53-f021-39f1-bef8-23060076ff53 | -23.59982 | -50.88887 | 2025-11-30 04:50:00 | NOAA-20 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7017c415-61be-3b53-96c9-96652906269e | -21.17676 | -49.17847 | 2025-11-30 04:50:00 | NOAA-20 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| faf9b7b4-8268-3e16-b7fd-973a0e93d604 | -24.07431 | -51.0578 | 2025-11-30 04:50:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6d131f9c-afa7-3e88-9a4a-410408027ed3 | -25.23422 | -50.76354 | 2025-11-30 04:50:00 | NOAA-20 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4d624d6e-b30c-3375-ab04-9352500023a6 | -21.14981 | -48.61372 | 2025-11-30 04:50:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 717dac0b-2f46-3a9f-b518-0e00aeca23f9 | -19.92745 | -57.4435 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e2a729a2-e907-3318-98ad-d5cb0f2dd145 | -19.84602 | -57.75936 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| abe651f8-9730-3ef9-a2c4-20e53bbc77d6 | -19.92821 | -57.43918 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f56c332d-a1ee-3ea8-8ea6-79a26f441daa | -20.1834 | -52.38494 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb686f80-9459-3bc7-9a05-b91a5e19aed5 | -19.84854 | -57.78768 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c1cf71cd-9f27-3e68-a4b3-a84435da6166 | -19.91336 | -57.41837 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 07c1e050-8674-3ded-aa33-82aea76015f6 | -19.84239 | -57.75863 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 66519cfd-a7b7-3eff-af69-451e2f3cd399 | -19.85944 | -57.78986 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9f32efd2-5e6a-39a7-a18f-7d5012e1a57b | -19.8558 | -57.78912 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 728ad73c-95d1-33bf-8078-67a0ef884acd | -19.33709 | -54.17246 | 2025-11-30 04:50:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b451c83e-0171-3697-bc2a-cc1f4f08a010 | -22.84626 | -47.21189 | 2025-11-30 04:50:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c6661f28-2fe6-3843-94a1-9f8421040d2a | -19.3332 | -54.17552 | 2025-11-30 04:50:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93a4a857-4a7c-3040-9c7f-f5f00807028d | -24.07419 | -51.05927 | 2025-11-30 04:50:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 87cea44c-5a01-3bf8-b972-46c140374f6e | -20.18682 | -52.38551 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 639a50c6-8878-3bc2-a801-d155f570232e | -19.97648 | -47.84192 | 2025-11-30 04:50:00 | NOAA-20 | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ecb27db-6788-3e36-8c0e-40ef8b6975d6 | -18.93174 | -48.48639 | 2025-11-30 04:50:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bf0f6be-51da-3807-b21e-d536dd9a9cbf | -19.33378 | -54.17188 | 2025-11-30 04:50:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69819583-a362-3e7d-b423-5d11dd6741e3 | -19.8457 | -57.78246 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3d8d9eae-b82a-3698-a191-d31bec34bdcf | -23.17898 | -45.66277 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d24a307-1093-33ff-a560-918cfeedebe3 | -19.92764 | -57.4212 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2a14fd0e-1c75-3087-b1a1-6aba4d57c271 | -19.93396 | -46.72797 | 2025-11-30 04:50:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66d17846-3b29-30b9-a8cd-5f54623ee1a9 | -20.17713 | -52.37992 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44fd2c02-5727-3b88-889a-3437cb955205 | -23.17996 | -45.65886 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 03ae65ed-20ac-395f-b7fb-432fc6f47c21 | -20.19024 | -52.38608 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f29b08ba-386d-3711-96a5-158807d3cf5e | -23.54918 | -47.20712 | 2025-11-30 04:50:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a31997b9-ebfa-39f2-a688-bbcfcac0fc8c | -19.90979 | -57.41766 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2f3834a6-c09b-381a-949a-43d63fdfdb1d | -19.84285 | -57.77725 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 44cb2d99-ecd8-3c4a-81c8-1e48ceae6736 | -20.99944 | -49.30625 | 2025-11-30 04:50:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e7ad3cd1-9605-371b-8cb4-1abab185819b | -18.93585 | -48.48697 | 2025-11-30 04:50:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64d5e33a-ed00-3c0a-a6dc-96e90c45953b | -19.86386 | -57.7861 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7c798c2f-1187-38de-8843-5fd0b442dc00 | -20.17771 | -52.37601 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff095af8-c191-3c71-ba6b-82e814725e56 | -20.18055 | -52.38048 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6691875-eacb-306c-a195-f3ad599268bf | -22.49252 | -46.93758 | 2025-11-30 04:50:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6890a8f-3053-37ae-b7ce-23559a2d14ad | -24.53633 | -48.91791 | 2025-11-30 04:50:00 | NOAA-20 | APIAÍ | SÃO PAULO | Brasil | 3502705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a1408ad2-ead9-3cb1-b9a4-723d0b591231 | -19.86543 | -57.77714 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 8786b505-46f3-3b01-8989-9ce1eb73056f | -19.08884 | -48.5897 | 2025-11-30 04:50:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29b3788e-197a-38c8-88ff-067a611af8f6 | -19.08836 | -48.59344 | 2025-11-30 04:50:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b741072-85b6-3c0e-ab06-bfdff3672e04 | -19.86465 | -57.78162 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| a066798c-60b4-3e04-a9b9-2d67e88ccf57 | -19.85217 | -57.7884 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7890bd03-cc53-35fa-9bcb-98601b9b729c | -19.92238 | -57.45145 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b7e8f29e-0e78-385e-babb-862860ae79ca | -23.18513 | -45.66008 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60880b4a-9df8-338e-950d-ca8824f398b1 | -21.24253 | -44.71593 | 2025-11-30 04:50:00 | NOAA-20 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a52f8869-0f1b-3498-a049-9d33f8ba0cfd | -21.14911 | -48.61454 | 2025-11-30 04:50:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a6e9315e-03d9-3c42-8a72-5a8a72a23077 | -23.15473 | -46.58704 | 2025-11-30 04:50:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b00bae0-9f2a-3bf2-bdf3-59cc68c2ade3 | -21.53365 | -49.52824 | 2025-11-30 04:50:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 45d20eb8-d971-37fb-80e0-4642b81a1187 | -20.19707 | -47.45425 | 2025-11-30 04:50:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b87baa10-25ea-3bbb-8c9a-c59192748bc1 | -21.00346 | -49.30682 | 2025-11-30 04:50:00 | NOAA-20 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3e1d58f4-e9b1-3d1a-b9c7-2aa9cf859002 | -19.84206 | -57.78173 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 07272d62-0e92-3f9a-afd4-ecf3f9634cd6 | -19.09293 | -48.59031 | 2025-11-30 04:50:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 069ee978-f025-36df-ac0f-e0ce4d8f16e2 | -19.83922 | -57.77653 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f27cbd69-30a5-3aeb-a4e7-da90e43d0b0c | -23.18484 | -45.66319 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c2dfa49c-5e27-39ba-ac51-5ef280028337 | -23.13057 | -54.88115 | 2025-11-30 04:50:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 435eb5c1-0b44-3a10-98a1-d56079f24a4b | -23.18414 | -45.66405 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cd4bb36c-7bb5-3aa6-9405-8dfb6a54561a | -23.18444 | -45.66098 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b39d5d44-c87d-32eb-817c-7d3d5a3d4689 | -19.63495 | -47.66953 | 2025-11-30 04:50:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72ace464-f31c-3601-862b-6cb8c600af47 | -25.05617 | -51.8886 | 2025-11-30 04:50:00 | NOAA-20 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 18b40af8-78c7-3a8b-8a7b-7bdbcf4131bd | -19.92313 | -57.44712 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 603bf7d5-cf62-3a90-abe6-ca2be5a7164f | -19.09244 | -48.59407 | 2025-11-30 04:50:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50dd83c8-947f-31a3-a028-22f3c525a72f | -20.59856 | -52.46121 | 2025-11-30 04:50:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e2294b1-5742-34d8-b46c-e1b7593c93f4 | -23.17929 | -45.65977 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5a2fdee0-e03c-3970-9b51-fe5d7aede781 | -23.17968 | -45.66189 | 2025-11-30 04:50:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 97810be1-fc83-3761-83e1-6ae42cd67800 | -25.23811 | -50.76418 | 2025-11-30 04:50:00 | NOAA-20 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bf543789-585c-3213-a40d-ea043c7e740f | -29.50013 | -51.81994 | 2025-11-30 04:53:00 | NOAA-20 | TEUTÔNIA | RIO GRANDE DO SUL | Brasil | 4321451 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 48034987-c08e-3193-923d-5513fcec5597 | -29.1083 | -52.20204 | 2025-11-30 04:53:00 | NOAA-20 | PUTINGA | RIO GRANDE DO SUL | Brasil | 4315206 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b5ea5242-9f4a-31f1-9fad-09806a98125b | -8.1633 | -43.2055 | 2025-11-30 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 93234837-c077-3fc9-9d4a-6771624c76d7 | -12.0195 | -49.2659 | 2025-11-30 05:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 45c5161b-47c0-3c0a-bb0d-4c9ba48b873f | -19.8675 | -57.7808 | 2025-11-30 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.2 |
| b8bc8d9b-e401-3de1-a529-95fcf4fd90cb | -19.8473 | -57.7835 | 2025-11-30 05:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.1 |
| 3e7ba63e-3290-3cc3-a330-4de7a27bfebc | -8.1633 | -43.2055 | 2025-11-30 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| bc2488fc-7f73-3162-b2ba-6ec8ff5bc036 | -8.1633 | -43.2055 | 2025-11-30 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 621e03d5-a3a1-31db-92f7-145582b6e02e | -2.60255 | -49.26554 | 2025-11-30 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c83f400f-3953-3dff-a8e1-724641844e22 | -2.51091 | -49.10314 | 2025-11-30 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 37c084b4-afd8-3b50-b110-b93c85eeb84e | -2.51496 | -49.09878 | 2025-11-30 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72f71b91-d119-3d65-bf1b-db31dc98dd2b | -2.51192 | -49.09615 | 2025-11-30 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 887b3426-a0f3-390e-b26a-cb733bfcf59b | -2.5139 | -49.10575 | 2025-11-30 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52fa7f35-2909-3615-9987-9269e7934723 | -16.80027 | -53.77583 | 2025-11-30 05:37:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bbfc7262-e21a-37c9-865b-621f3dc6d79c | -17.5027 | -57.1501 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e1a9e25b-b41e-3e10-800c-347f9ec69028 | -17.50792 | -57.15077 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9892458d-f780-3a56-ab5e-77f7a45189cf | -16.80191 | -53.77763 | 2025-11-30 05:37:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da41ca37-ce14-3cd4-80a1-8925a1c9fc8c | -10.23086 | -67.68883 | 2025-11-30 05:37:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b373b96d-866e-3204-a2a6-47ec2f2527b1 | -17.49011 | -57.11462 | 2025-11-30 05:37:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README21.md)
