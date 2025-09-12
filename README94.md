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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e4462ca-c757-31a8-9b72-97246e5a9362 | -22.68455 | -45.51999 | 2025-09-12 04:29:00 | NOAA-20 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| adcf68fe-6872-3967-91de-1068e2a6d0ef | -22.19315 | -49.59324 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0d0eb7d3-6650-3143-b004-3946a37d5b71 | -23.74112 | -53.31073 | 2025-09-12 04:29:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 39159509-c741-3c37-9f92-0c2c7dcc01a2 | -20.57226 | -43.77752 | 2025-09-12 04:29:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6f83c4ca-e127-3999-9b82-a3e8c061e49d | -19.98369 | -47.61729 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bbfc540-9106-3423-9254-bd0cb0725b23 | -24.91358 | -49.76281 | 2025-09-12 04:29:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a35e13c7-91a9-38f9-a1fa-d747c8656757 | -20.56015 | -46.93001 | 2025-09-12 04:29:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8c909b7d-40d3-3f9f-9af6-70307bdd8cde | -22.18868 | -49.6001 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0be47b55-bc5b-384b-a9fc-334fb7fa99b2 | -23.13505 | -47.48061 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2ee41a3b-c7b5-375e-a1be-d4ac386a9bdf | -21.96053 | -47.54818 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acd655ec-df28-3849-87bc-6e8297ecdab4 | -23.39686 | -46.71284 | 2025-09-12 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8c106edb-2ac3-3cac-97e3-bd44e872a699 | -22.19547 | -49.73158 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 55f3c44e-5c7e-3340-b44e-5248e32eb31e | -20.60349 | -46.90281 | 2025-09-12 04:29:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3f86b127-6acf-3de0-947f-5a62217910ea | -20.16037 | -46.59618 | 2025-09-12 04:29:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9b0da59-5618-3f35-baf1-a57cb970eb63 | -21.32195 | -45.01073 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c39d6cb7-7046-3dd1-b927-cf1ef77bbc4f | -23.02628 | -47.27716 | 2025-09-12 04:29:00 | NOAA-20 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 91768c1d-30f0-30ff-8539-b332d35513ac | -22.19647 | -49.59384 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 426bc9f0-5aa5-3288-abd6-73ddb72dca60 | -20.01313 | -47.65417 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a1b4097e-e414-34ad-bfe7-e7240df436ae | -23.43274 | -47.0239 | 2025-09-12 04:29:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b2100fd0-1885-32e5-a288-1cd581b05e5e | -23.11215 | -47.49001 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 18a8addc-cbfb-3717-b6bc-d938cc0d51c7 | -23.46978 | -47.66122 | 2025-09-12 04:29:00 | NOAA-20 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 21b7e987-f63f-3413-b850-939f6a5d4478 | -22.69678 | -46.2252 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 940e4763-d6f2-3b6c-9f9d-6ba123a0de49 | -23.38661 | -47.01156 | 2025-09-12 04:29:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0a16e90e-70b8-3c56-92f1-874fcdc23808 | -23.38615 | -46.22971 | 2025-09-12 04:29:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 22b56416-79a8-3db9-b7c3-5a199c650368 | -21.62754 | -46.7965 | 2025-09-12 04:29:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 75896416-4370-360c-bd29-fad95c8205be | -19.98427 | -47.61336 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48d5654b-5ff4-315b-95be-5b23f40d857a | -23.11742 | -47.50375 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| b899ea95-014a-30c6-b5f1-131a75e32b7c | -22.1832 | -49.59145 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 108d14d1-150c-3620-b367-eaf084ff51f0 | -22.19489 | -49.7353 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4e76204a-c719-3fa8-8a9b-c2934c6b8cc1 | -21.18455 | -47.52843 | 2025-09-12 04:29:00 | NOAA-20 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b7891b4-2ae7-347d-8db9-7e33e4df4b10 | -21.94605 | -47.55003 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f55b2692-21ba-3727-8f79-0cdf131389af | -21.3265 | -45.00637 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 7f275a13-0418-3435-bad7-5a438ef5bcf1 | -23.32566 | -46.54745 | 2025-09-12 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 516ab702-f957-37ae-895e-8433342bbba5 | -20.55664 | -46.92941 | 2025-09-12 04:29:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b856b1b0-b571-395c-b183-2902eaa3d82e | -21.95815 | -47.56467 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e65e9456-aeea-3144-94a6-176d1e92498f | -23.31629 | -47.31435 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4aaf0a34-1ce3-372e-9ca4-0adc7f678c1e | -20.3644 | -49.97189 | 2025-09-12 04:29:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d398d3d3-cb16-3dee-943e-6f7ec6c32151 | -22.19605 | -49.72785 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3e7f1fb8-b0d0-3dc4-b37d-b4ce33fabafd | -20.1278 | -47.68341 | 2025-09-12 04:29:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1e6c4f2-6012-38d3-b9e3-e6cb39e42906 | -22.18478 | -49.60322 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d6a90b7c-b252-3b35-bb4d-3937d5079fbf | -22.65125 | -53.12012 | 2025-09-12 04:29:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 761117e4-e714-36ae-98e8-2abfa96d72bb | -19.78584 | -48.28454 | 2025-09-12 04:29:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40ec0994-bf80-36e7-a184-638f32d90b94 | -22.19783 | -49.73465 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e70a1275-7cf3-3c97-acbc-bb98df0e112c | -20.01258 | -47.65792 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a91e1474-243f-3655-ac37-34c402ed99fc | -23.30906 | -46.61663 | 2025-09-12 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bbdb6334-154f-3ed5-815c-d8e0bba28904 | -21.31809 | -45.00983 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9e33e288-7527-319d-b741-1bf0bb3094ad | -22.70466 | -52.63204 | 2025-09-12 04:29:00 | NOAA-20 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b4f80636-a488-3945-a558-47a92e5a3c36 | -20.14713 | -47.38644 | 2025-09-12 04:29:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87ea351f-b953-3a08-8f0b-686d5a010ccd | -19.95313 | -49.26668 | 2025-09-12 04:29:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4ffa5a72-2873-3a45-81c9-7cee41ce8ac9 | -20.35393 | -48.39956 | 2025-09-12 04:29:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 343b6500-a670-3002-8d63-3d0238c183e0 | -22.18709 | -49.58832 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 04409c0d-1b3a-34f0-9fd8-71b75fd33fa7 | -21.94953 | -47.5506 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3a2ebba-1485-391c-8fe7-cc97f57c5a31 | -22.39699 | -46.75592 | 2025-09-12 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4d78031f-6d1c-3ca2-b84f-4c168df4021c | -19.9984 | -47.63588 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 537e0c83-a005-317a-a3df-f2dc658d97f6 | -23.53885 | -47.14334 | 2025-09-12 04:29:00 | NOAA-20 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae1fc12a-bb73-3c80-9607-043d8b09ee26 | -23.30806 | -47.34812 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c785a733-d2de-3390-b1f3-259952999f10 | -21.33619 | -45.02353 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4fd575fd-3b09-329f-b507-931057bf8391 | -22.33653 | -48.81353 | 2025-09-12 04:29:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0424dbc0-1459-3ef0-9ea5-ca7938bc02c2 | -22.67249 | -53.1245 | 2025-09-12 04:29:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 57c46d1e-8812-3257-83d8-dd563bf3387d | -23.19131 | -49.65088 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d452be34-0900-32a1-9841-8f1011a19d2d | -21.76083 | -47.2819 | 2025-09-12 04:29:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fdeb6f71-21a9-3e8d-8bf8-0045b024232e | -19.9695 | -47.59504 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faf03aa2-99aa-3892-bf82-0bd062fcf3f0 | -22.19431 | -49.73902 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f4f22d1c-5dda-3083-8125-953573c7a085 | -20.00114 | -46.92641 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96056f3d-f3d9-393a-bb70-fd02e85838f2 | -21.94488 | -47.55822 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc446990-3e23-3579-9ea2-a6904d22bea4 | -20.00349 | -47.64862 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1c17cdb-3c8c-3aa3-95d0-45ba16eb1892 | -25.05584 | -51.89063 | 2025-09-12 04:29:00 | NOAA-20 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 49d55b0b-0222-3545-9c2b-e85f3a6fbce1 | -20.00464 | -46.92696 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dced8a2-d68a-3783-8087-5ddffe8e88bc | -19.97513 | -47.62798 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b427f84-6118-33b5-b4d1-0584181bba29 | -20.3529 | -49.95843 | 2025-09-12 04:29:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5cebcf2-ba40-3e8e-a5cf-2c5752dd3fe9 | -21.65034 | -50.10853 | 2025-09-12 04:29:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fdb60572-8d96-3130-842e-4aa9cec5423a | -20.3528 | -48.40707 | 2025-09-12 04:29:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c867224-046c-372c-869f-5cb3b45ca259 | -22.19099 | -49.73843 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| accddf4b-d42d-352a-ad9e-c13489e09aa6 | -21.33418 | -45.03891 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9edbedf5-1ce3-3caa-93ba-ec416a778189 | -23.32508 | -46.55187 | 2025-09-12 04:29:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6228bd53-b5ca-349a-b215-67b88581db9c | -20.36772 | -49.97248 | 2025-09-12 04:29:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 404bb299-7689-3129-95c1-6e7bde37b976 | -22.52674 | -45.09647 | 2025-09-12 04:29:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| f32f9150-a303-3549-83fb-c852eb48e6de | -21.96628 | -47.55759 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a8096db-9289-3020-96f5-76e6b1410f84 | -21.45291 | -56.15776 | 2025-09-12 04:29:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c22423ad-8200-30cd-bdc8-921dbc2e8af1 | -19.97235 | -47.5994 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 756b29f9-856f-349b-91e8-ae0a29737919 | -21.9634 | -47.55291 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a12606-8395-3958-b6e4-62ec8b5b18c2 | -20.29658 | -46.57163 | 2025-09-12 04:29:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1560999-0003-38c0-9ea9-f33fa858418c | -21.33332 | -43.50888 | 2025-09-12 04:29:00 | NOAA-20 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0a0ef9fd-e52c-382f-83e5-44295d3d4d05 | -19.99499 | -47.6353 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b20f056b-d2cf-329b-a343-77e639b0c8cd | -23.13617 | -47.49828 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 315cddc1-2c27-3b68-9363-4fe05704d540 | -21.18917 | -47.52099 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7a555840-afb6-3eef-9195-5954623e8c7e | -23.11331 | -47.50743 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 9b6d8e5e-eff5-3af7-9196-21f1ddd029ae | -19.99824 | -46.92178 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 706dd45a-0464-312f-8898-976b85ed9e5c | -21.69414 | -49.983 | 2025-09-12 04:29:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b19f6a4-ae41-3d4e-8f52-06d76f7643ad | -21.19433 | -47.53414 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb77fdbc-fdae-309f-93f7-0b0a2607781a | -23.83908 | -51.07555 | 2025-09-12 04:29:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1aaae475-e60a-3187-a125-3ab5d6250ad0 | -20.0018 | -47.63646 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7188296-8564-3aac-865a-71c14bd0dcab | -23.49267 | -47.26583 | 2025-09-12 04:29:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| cc80518f-d2e9-32ee-be28-87e65ea6110c | -21.32718 | -45.00118 | 2025-09-12 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| faaad05d-d4fa-3fed-a4c2-e7d67b2f3cb5 | -23.14425 | -49.6505 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f82cb65b-e947-3904-90b7-98a3afb6d9cd | -23.219 | -49.43089 | 2025-09-12 04:29:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 3e7ed056-f12c-34eb-9c75-6f7b27ae9bf6 | -23.22198 | -49.42717 | 2025-09-12 04:29:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2225495e-3653-33e0-b689-fb192c23d627 | -20.0001 | -47.64798 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7c12a27-3a4c-36d5-8551-79135b0bf406 | -23.3222 | -47.32422 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3e52ddd3-8070-324b-97f1-ddda9d0cb738 | -22.69866 | -48.69173 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README95.md)
