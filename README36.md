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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 629f9453-0193-33ec-a9f7-0965ea118e8d | -19.18698 | -44.15425 | 2025-09-11 03:57:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b62ca736-757f-3763-b883-48b85c2dfcdf | -19.9545 | -49.27014 | 2025-09-11 03:57:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 85d20bb7-a0e4-399d-a109-c9df591f20e5 | -17.71092 | -44.43435 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2ad6448-863a-3d59-bcc9-bb8193ec8b1f | -15.14551 | -52.45409 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f354ad86-22d1-37ab-b17a-789519b51463 | -18.01069 | -44.45664 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4e28acd-d1da-3006-80dc-9585e1278926 | -20.11365 | -44.34672 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4a381c44-6e2c-3bf8-9220-cf6464a6cf03 | -15.73517 | -44.04284 | 2025-09-11 03:57:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ee8a796-76c2-3c42-8e7f-fb36c11fec25 | -17.39123 | -44.92746 | 2025-09-11 03:57:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f5b4e7e4-3a31-3ac3-84ca-9da847b42786 | -15.56507 | -54.75176 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24c0fe2a-2744-3424-b5c7-e4396c224e15 | -14.7134 | -45.34419 | 2025-09-11 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfab021d-90d1-387c-8baf-aa854dfb8b9c | -13.78854 | -46.28292 | 2025-09-11 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 244d60d0-e912-31f5-8ba8-f6212186fe05 | -15.14 | -52.41941 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 021fc890-cbed-345f-9137-250bca38d273 | -15.1616 | -52.43491 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b8c75ed-75bc-3c77-ac7c-22d67415b9de | -14.41619 | -47.32624 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2fb6e91-6a42-36df-9276-0e779b25feb7 | -13.84278 | -44.45906 | 2025-09-11 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38a361d7-f4c3-3ab8-a4f4-31c8bf4d78ec | -14.36649 | -47.30996 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a224f68e-f015-3f80-bd8b-039f2997f097 | -15.13111 | -52.43098 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40db6681-489e-3342-b87b-907f4c1e9706 | -15.13933 | -52.45285 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d7a895af-8b41-389f-81f2-838dc0561980 | -14.61763 | -46.35259 | 2025-09-11 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a38aaf05-983a-3cb8-b658-010fdd04a1b9 | -14.12436 | -44.3162 | 2025-09-11 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eca35d82-642c-3d95-ab85-64a63b079b29 | -19.71168 | -44.23531 | 2025-09-11 03:57:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a3b5fc0-7ca7-3250-863e-6842d881812f | -17.56547 | -44.55136 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4ac93fde-dc08-3528-90b6-4174deed380e | -17.95155 | -44.47682 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c35f6ea-257a-345b-9876-c537103eb5fc | -15.77822 | -43.13477 | 2025-09-11 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d2c0eb6-39fb-39d6-b2bb-5a50f590d4d6 | -15.12591 | -52.42519 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c901354a-627a-3d92-992f-bde120c0b954 | -18.56004 | -46.56839 | 2025-09-11 03:57:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9d18880-7876-34b3-92da-7380e99e4a7d | -15.14187 | -52.4409 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81079918-6d8c-3b4b-867c-409d99b1bffb | -14.93885 | -50.10503 | 2025-09-11 03:57:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| daf508bd-2ef9-37f7-9ac1-2cb4034c6496 | -18.82653 | -46.87263 | 2025-09-11 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54d154e9-97f3-3b7e-a0af-f80df4a5a7ba | -15.81708 | -48.95474 | 2025-09-11 03:57:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3467072c-70c3-30e6-b429-b561a525b9b7 | -17.95077 | -44.48125 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efd5b061-4075-3c16-aed2-03c874236d52 | -20.01259 | -44.23576 | 2025-09-11 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0e13e520-c827-33d1-bf78-f93ee46de477 | -19.23644 | -48.00526 | 2025-09-11 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 1b4d0cad-e5f2-326f-a248-eab851ed5ac3 | -17.94638 | -44.4851 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce4fbe8d-e211-3828-98ae-bb979cbed090 | -18.57438 | -47.41664 | 2025-09-11 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef15907d-4a0b-39e5-9bf1-9b2180c3e9e2 | -20.55057 | -47.62352 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e4af25b-22f2-3c4c-8ef7-9afd94764bb2 | -20.54306 | -47.61806 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07a2fc32-2e18-3693-a5e8-dd991f54968f | -20.00804 | -47.62343 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 556799bc-6132-3742-a251-85ecac60545b | -16.63045 | -49.76341 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a595761a-1f67-301a-b219-3139321d3142 | -19.99978 | -47.62142 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a76400cb-2faf-391b-a37b-dea56dd3ad37 | -20.57759 | -47.68399 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d5ff190-7a41-33e3-9f25-6e4937843398 | -18.60358 | -43.96907 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4f4c7ab-dd97-37e9-9023-e8f7ab114eb3 | -16.28363 | -45.68482 | 2025-09-11 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b657ad8e-5f38-3818-afa2-6a57c8fe7d45 | -20.1318 | -47.68377 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85ebb839-e2d5-3203-b3ad-c265b12a46ba | -15.22239 | -44.0485 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0c6e611-cf54-3e89-982a-ab00ea0e5762 | -17.47047 | -45.09797 | 2025-09-11 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 10873dcd-f93a-3a4c-875b-d6af8ead75c4 | -12.97315 | -46.7364 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5827fa6d-8194-31c5-836c-6c89417d901f | -15.16078 | -52.41227 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6824d006-14eb-3eb2-b21f-67dd0269fa85 | -15.2195 | -44.04344 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 751d5f15-c4a8-3d48-8241-b23b0212de55 | -17.50153 | -43.75335 | 2025-09-11 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20d59b8e-6d86-322f-9379-09c9626cda03 | -18.08241 | -45.42918 | 2025-09-11 03:57:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1dfc6e7-abf6-3e19-aced-896b2c997281 | -17.47338 | -45.10342 | 2025-09-11 03:57:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5951d44-79a8-3f2c-ba3e-af2d493a57fa | -19.01134 | -46.25122 | 2025-09-11 03:57:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 646ced5c-e0a9-30b8-b5ac-ad86a596a028 | -17.64769 | -44.75086 | 2025-09-11 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 771f1ddc-927f-33c4-8030-1958cac9d10b | -17.24433 | -46.75489 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f9a7287-0c6a-3f30-b5de-93ddd2bcb936 | -17.82655 | -46.74087 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28e0ef07-59dd-3848-b0d3-c176532eb367 | -17.99916 | -47.1055 | 2025-09-11 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99e5f088-b533-3056-9b99-dce4bcb0c678 | -18.91863 | -41.1184 | 2025-09-11 03:57:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b19996f8-a9b0-3aaf-a4d1-daceb0a597e9 | -14.61914 | -48.84985 | 2025-09-11 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4a2f502-bfd1-38a2-9514-31b55fd8c189 | -13.78765 | -46.28771 | 2025-09-11 03:57:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6d18c898-1c6d-3ef0-921a-fd6949f149ab | -15.22604 | -44.04916 | 2025-09-11 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e962d4e-04be-3770-9e75-87847fe91660 | -15.56359 | -54.75822 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3cb0e26e-7017-3db5-bba0-7aed29edcb93 | -19.67283 | -43.97332 | 2025-09-11 03:57:00 | NOAA-21 | CONFINS | MINAS GERAIS | Brasil | 3117876 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 790b6dc8-e173-3ef7-8dad-f93f6ab6b7fd | -19.2562 | -48.00344 | 2025-09-11 03:57:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d733fe78-8566-3b3b-9136-2294331e4b17 | -15.80192 | -52.27658 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 994d3384-ff91-378f-a91f-a3442d203e9f | -19.98911 | -47.63188 | 2025-09-11 03:57:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 74b920fe-a70e-359c-8ba8-abce4d643b90 | -20.1871 | -44.44957 | 2025-09-11 03:57:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ae5deaeb-a485-3bf2-a936-3ee1a337fb7e | -20.91146 | -45.28563 | 2025-09-11 03:57:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b96b4c91-2df0-3c54-9af6-1138a01ba8b4 | -14.66826 | -44.0563 | 2025-09-11 03:57:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c4026c3c-efb6-343f-8495-10a2817cae91 | -15.96018 | -50.22356 | 2025-09-11 03:57:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf17646-4aa9-3012-8c8e-36a1acc85602 | -20.39514 | -46.2741 | 2025-09-11 03:57:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f6ad3ba-c8fa-346a-891c-7a0672f7692b | -14.13532 | -45.39296 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1369fad-1e40-3370-80ac-8fee614237a8 | -13.01161 | -48.72343 | 2025-09-11 03:57:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1fe4d5a-d2eb-3a8a-802a-a48fc89ccb0f | -15.35067 | -47.2595 | 2025-09-11 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e303a4a-7f88-3896-bce7-0909106d98eb | -20.5187 | -47.63317 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 22822780-1bfe-3b29-a58e-f764fadd18e6 | -18.48751 | -41.20109 | 2025-09-11 03:57:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d23ec40e-d8ee-3025-bc7c-28bdd7b90e65 | -20.14759 | -43.66611 | 2025-09-11 03:57:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a6be698a-8e39-3964-8202-500b039180e2 | -15.87764 | -54.92918 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 24cc46c5-3dfa-3175-987c-acd498d76a39 | -15.80161 | -52.24872 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 311b3de4-94ba-37cc-b443-bfd53e078cc0 | -15.55315 | -54.74669 | 2025-09-11 03:57:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0751fbae-531f-3029-bec2-86919506ef05 | -12.96065 | -46.72932 | 2025-09-11 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87f2b700-5c0f-323d-b5c9-404d106d683b | -17.75265 | -44.49334 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d022d362-c4d4-38a3-80ec-c5c3aa248e01 | -14.51852 | -53.92758 | 2025-09-11 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 559e1789-4eba-3104-a746-cfbd3ee06261 | -19.95923 | -44.1497 | 2025-09-11 03:57:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2015a0f1-2f48-34ed-9db3-48691534bb86 | -15.79938 | -52.22981 | 2025-09-11 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ef48e897-2af6-3f1c-b937-4490b995bce3 | -19.46445 | -40.88425 | 2025-09-11 03:57:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38526572-3009-3957-b9b7-ecf86dc61708 | -15.22906 | -44.03155 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c77f2102-1d90-3a27-a74e-8def60e5df99 | -14.14331 | -45.3945 | 2025-09-11 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3a35bb6-4a67-3bea-8eda-8d156c477ef2 | -17.34185 | -46.70203 | 2025-09-11 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9209e5d8-1e09-3a38-9058-b9526d75edb4 | -15.19762 | -44.0395 | 2025-09-11 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf0f87a8-862a-3a65-b647-fac3df8ac89b | -17.68344 | -44.20035 | 2025-09-11 03:57:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ece51d8e-9eaf-3fec-8529-19d4eea45e79 | -20.12764 | -47.68289 | 2025-09-11 03:57:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9440c48e-f50c-358e-b81d-19c543e5d9e9 | -14.36978 | -47.29971 | 2025-09-11 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aec3032f-cfd7-3ce3-ac57-6ff53e07fa86 | -18.60845 | -43.96159 | 2025-09-11 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| fcb19f8e-adb2-344d-a7c2-750751899648 | -12.97842 | -46.73281 | 2025-09-11 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1af426b-93ec-35ec-9f18-a55a705305ac | -17.94197 | -44.48904 | 2025-09-11 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc595be0-954c-3eec-9b71-77e132181cd7 | -17.06886 | -49.67482 | 2025-09-11 03:57:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bffb45b1-0940-38b6-858b-771641234fb9 | -14.35819 | -41.86186 | 2025-09-11 03:57:00 | NOAA-21 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d86be732-6ea5-323c-9b89-15ceecb44947 | -16.63158 | -49.75786 | 2025-09-11 03:57:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 146ccc71-bc21-32ab-89b7-12b99eca47fe | -19.37236 | -43.27259 | 2025-09-11 03:57:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
