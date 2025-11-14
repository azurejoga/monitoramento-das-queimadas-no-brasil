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
| 30c1b19e-fbb0-38d7-aeb1-5dc39764d2c8 | -18.7083 | -43.01056 | 2025-11-14 04:25:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bceb2aa8-413c-360a-bcf1-e6bc183fefcc | -5.42044 | -44.80817 | 2025-11-14 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a965e2ae-3ba7-3146-a754-4de576a9b711 | -4.7074 | -46.44768 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f52df816-237a-3cba-a5e0-b4a1cc6270f5 | -6.15248 | -48.04604 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1878d7d7-a875-3862-a130-94b5ad999d27 | -11.85517 | -49.21973 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 41fdf342-6d11-3acb-bb4e-ba3987f63fcf | -4.68413 | -45.85641 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4549913-6b0f-3bfa-bac0-fab4a290b6b6 | -4.67539 | -45.80281 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75c8fe6a-6d90-3deb-ba3a-29a50272a3d4 | -6.21034 | -47.26315 | 2025-11-14 04:25:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42c5cdcc-9511-3126-9f5a-38a8e60fb9b8 | -5.72826 | -42.35556 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 35de6755-cc4a-3dab-b7a8-115a1f9f084f | -12.67241 | -46.7476 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5edbaa6-a2db-3c22-aa99-4dd9dd7a6a1f | -11.85807 | -49.22467 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3f29b9d3-53ee-3b83-a8c9-27bc7d33e568 | -5.59247 | -45.17443 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 161796b1-7a0a-3de2-89d2-3d2897288cf4 | -17.97033 | -47.2507 | 2025-11-14 04:25:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1c889ef-bed0-386e-90ec-d8f0130bf5d1 | -16.58715 | -42.21524 | 2025-11-14 04:25:00 | NPP-375D | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3fc6a536-c29a-37bd-bc7c-5c212ac2ff0c | -6.48299 | -43.75697 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4823784c-7ff3-3965-a83a-d88cc864b026 | -4.77246 | -45.5863 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e96a562-70ee-3c78-9cc5-6049dd69cc74 | -5.41291 | -43.26121 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7fc2afa-b3eb-3cf1-b71b-e8a4bdad5543 | -4.75108 | -46.39662 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1c4ec77-e692-3f99-9abb-b56882f87453 | -4.68798 | -45.00596 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 321b57c4-a3be-355f-bc25-142afe388ded | -6.44508 | -45.66243 | 2025-11-14 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69907dcd-fce7-34a9-a3c1-03ae2d859096 | -4.55686 | -46.68733 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f293c045-3dc9-315a-b8ab-1fd06a757c68 | -6.08074 | -41.62531 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5ab4529-bf06-333b-9b6e-f00ed3b65a3e | -5.54501 | -41.81624 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 31466f46-267f-3915-98e5-303167f74890 | -12.62471 | -48.40395 | 2025-11-14 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69d46e82-765e-3aff-bfc9-c9c01157bd28 | -6.06728 | -41.73938 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be1a2199-cce2-35b3-a4f6-c871d38bafea | -6.14225 | -43.70742 | 2025-11-14 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2afab32a-2945-3809-a10a-6e44a38c272d | -12.70872 | -45.42811 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05c0c7ec-f043-3d57-80ad-8fe965a3764b | -5.36855 | -46.29031 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f0cdbe0b-7c3f-3d34-95ff-3708594fe37c | -6.67061 | -41.66175 | 2025-11-14 04:25:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c79f459-7cd9-3a40-b7ac-7e0b93872d04 | -13.7272 | -49.13638 | 2025-11-14 04:25:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c946374-5854-35bc-a6fa-007bd825c6d6 | -12.66461 | -46.75361 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a841bb4-daf6-3031-b777-433a3bf5f106 | -6.97545 | -41.63922 | 2025-11-14 04:25:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aa2aec22-9fca-35fc-a789-4680188c6fa0 | -7.11026 | -44.0675 | 2025-11-14 04:25:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aef073bc-6db2-35e8-8284-830796aa4840 | -4.70679 | -46.45147 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 69f4f730-4f22-3c46-b1eb-b70427e2bfb5 | -14.70036 | -46.61957 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 578a1fa1-bca3-3df2-9ea4-8d3fbc8558a6 | -7.37583 | -42.58931 | 2025-11-14 04:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6eaf1492-8cc1-3bb0-adfc-cfbc5a4796c2 | -6.14439 | -48.04931 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ecea8a4-7c55-3d77-beac-02d6ca28fea2 | -6.28189 | -41.74839 | 2025-11-14 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| daccdfa5-5e71-3415-b139-7615e60a5f66 | -16.35396 | -46.00713 | 2025-11-14 04:25:00 | NPP-375D | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a133246b-25a9-3854-a6fc-dbe67b764d16 | -16.47304 | -42.17705 | 2025-11-14 04:25:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5ed636cb-487b-336e-aaa8-d2e2d46c16d3 | -6.14736 | -48.05415 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbacf046-9571-3582-93fa-c80b12d5765b | -4.11374 | -50.06003 | 2025-11-14 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5323812-f520-339d-a1ce-b40f20208c88 | -16.82828 | -45.44981 | 2025-11-14 04:25:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ccb6c81-bcb7-3a7d-8a34-35271879366f | -4.53427 | -46.39804 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d21fa827-31ad-3529-b193-d2bcdbf5c84c | -4.57825 | -46.71048 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0156141-a525-3655-aebf-3894345c3834 | -14.70368 | -46.62013 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1db8ce3-1b23-3f7e-b7f3-a9521614fd62 | -5.84262 | -38.40281 | 2025-11-14 04:25:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76836708-b7e5-32f0-a7e1-34a5fad84fdf | -4.68743 | -45.00944 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2dee166-1b9d-3a0d-8b16-0b0142f380cd | -6.88179 | -42.85414 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7222e773-b083-3ffb-9042-fd7f222b2e0f | -5.99907 | -47.18568 | 2025-11-14 04:25:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2dc28c4b-556c-3b77-8da4-2e553921ba85 | -14.91745 | -47.36059 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ead51862-bfbb-3e9f-a633-040bf5a4ff82 | -6.83142 | -43.16024 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 96d4846d-449e-3fe3-b4d2-d45cbf71a82e | -4.21984 | -49.11955 | 2025-11-14 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 067d26c7-2eed-3138-839a-31c2c5ad5783 | -13.39478 | -46.72083 | 2025-11-14 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b12e526f-ffb9-387f-ad47-af9002f6ff0f | -17.96701 | -47.25013 | 2025-11-14 04:25:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29848355-eee2-30c4-9f08-c83256767d66 | -12.72039 | -45.41901 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 38d86d7d-c7ec-3ea3-9882-7330ee81fa02 | -6.09943 | -41.59878 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4ecbf980-ea7c-332b-a72c-5b28cada5909 | -3.52906 | -52.79933 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48714da1-4df7-35fc-a02e-b4f99f6c7fec | -4.69852 | -45.68092 | 2025-11-14 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b460e6-64b7-3838-8a0a-2b1cbc9319a8 | -6.13244 | -41.69589 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a87581d9-d6ed-358d-9476-2a67fa857696 | -12.69149 | -45.42899 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ea8d5a42-e016-3a36-a96a-ab8e803f76d0 | -5.93181 | -48.1377 | 2025-11-14 04:25:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f577b1e4-6b59-3a5f-b4ca-5a53a1a557c1 | -6.09454 | -47.9244 | 2025-11-14 04:25:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5e120d8-a8ef-3626-85e0-5f0a8fa942e2 | -6.48971 | -47.01039 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8906d191-863b-3abb-8ba2-58a4517fc676 | -6.0209 | -44.32835 | 2025-11-14 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ba92a16-7964-3b3b-9a15-4a587be2d732 | -12.67856 | -44.14733 | 2025-11-14 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c24bc1a2-acb7-37ea-b95f-5896bf4d9a7e | -16.37579 | -43.03914 | 2025-11-14 04:25:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bce746f-891f-3842-84c5-b391c4f5b2c4 | -5.42356 | -43.2592 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72ab5a18-ddc9-3a05-b145-c7aa9da2c83a | -4.64503 | -47.94859 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6268d7d-2b67-3f39-8d3e-f9de6ede6772 | -11.85008 | -49.22768 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3db88ac-56a3-3146-ab4a-b00595ce9b9a | -5.25425 | -46.17732 | 2025-11-14 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22ba93ed-0b06-33d6-8082-51ac4cb3f71c | -5.90186 | -43.64129 | 2025-11-14 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2461489c-65fc-3820-925e-c3d2a2736319 | -12.01577 | -46.76748 | 2025-11-14 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfb436ed-6ff1-3028-a36a-ddaeba4d2175 | -6.88823 | -42.07309 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f0d8df6-d82e-3afc-959c-0bad6873f923 | -6.99364 | -42.78209 | 2025-11-14 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b07d45da-59c5-3b4f-8fe1-26260e47aec1 | -11.99118 | -44.28929 | 2025-11-14 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bde26ee3-179c-3168-a6fe-00a35d11250a | -12.13698 | -48.01488 | 2025-11-14 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e74f64ea-1459-349a-bba6-400e80ddbb54 | -6.09854 | -41.53102 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97338368-0d37-3b44-b6b4-be85910eefd9 | -5.06832 | -49.8763 | 2025-11-14 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2387641e-f1b2-36a2-b67c-0e0e512b61fb | -4.32641 | -48.63329 | 2025-11-14 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55c82efb-f635-3f37-98f4-d8b20772da01 | -12.45558 | -43.74252 | 2025-11-14 04:25:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caf15b88-0c05-3372-a470-d84d4a5f3289 | -6.07952 | -41.63339 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9e5fd9ed-a0d6-38d2-8869-2c80cbcbfb45 | -5.78841 | -43.73899 | 2025-11-14 04:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb411baf-5327-3a48-94e9-a899e3c8ea55 | -12.7165 | -45.42205 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4b9f4f44-0495-3bfc-a42c-66b18077425f | -14.77267 | -46.67537 | 2025-11-14 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 902a5477-ef18-3581-bedd-dd32f4bc98ec | -6.06853 | -41.57781 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c91c1fce-63c5-3893-aae4-b12bb31d4642 | -5.58381 | -41.0956 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 217c58a1-97c9-368a-9d83-d36c48c23911 | -6.10993 | -45.68144 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 282fca36-1d7a-327b-9a00-0b7d46d3850e | -12.41458 | -44.18507 | 2025-11-14 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf8b94be-bb7b-377a-a75b-efb38b51d797 | -5.65334 | -41.07793 | 2025-11-14 04:25:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 694bd317-34f0-3878-9fae-c4ac52349e50 | -14.6998 | -46.62314 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c483f866-5191-32bb-96a7-fda10ea5d8f4 | -6.39389 | -42.3161 | 2025-11-14 04:25:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 604a4f08-e866-3c13-be27-df30f1b8c92c | -13.27474 | -44.25898 | 2025-11-14 04:25:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22d2ff5b-9556-3bee-bd19-8cfd460e33ed | -5.3484 | -46.76622 | 2025-11-14 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9e2e27b-1fed-3d50-b1a6-1cf7a1eb3c58 | -11.98777 | -44.28875 | 2025-11-14 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdd04803-d27a-3765-a0f1-bedb7a7adc5d | -11.80779 | -44.25728 | 2025-11-14 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f198c631-2391-3744-9fc2-b09b42e7843a | -6.47288 | -48.37169 | 2025-11-14 04:25:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e471229a-0e72-3780-a72e-9a517cc0e5a1 | -7.05614 | -42.22872 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 24c40ecf-e98a-3d42-86be-b96d2302628b | -6.06788 | -41.73534 | 2025-11-14 04:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ec330ce-28fe-39cc-97d1-17c440d2caab | -10.63808 | -51.76467 | 2025-11-14 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README37.md)
