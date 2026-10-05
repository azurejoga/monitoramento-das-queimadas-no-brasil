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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad6ab386-9036-3859-a8ae-57ad81899c9e | -11.47455 | -43.40416 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 369d0c9e-e3ec-31e5-940f-e1ba50dce439 | -6.85705 | -38.67673 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 7c4509f7-b1f0-375b-970c-aed315a15eff | -10.54016 | -46.45326 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 88a876a2-05c7-3522-8831-231b20a17891 | -9.79299 | -47.78214 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ec987ff-f101-3ab4-a179-bc4dae3f3b47 | -11.76834 | -44.92379 | 2026-10-05 16:37:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2928d2c2-3b39-373d-b3c9-8221a317c44f | -8.53028 | -54.57898 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ffe95790-44ba-3fc4-b55a-0150f2b84e86 | -7.53118 | -45.88081 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b204f920-38ab-3c7a-955f-d8958e05e355 | -6.87371 | -41.57907 | 2026-10-05 16:37:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 28.0 |
| f16d48dc-a467-3506-b5f1-8289fb6885ff | -10.40115 | -47.53469 | 2026-10-05 16:37:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b71d74d3-6d91-3424-aa01-603d85e8c424 | -12.34813 | -47.06518 | 2026-10-05 16:37:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c7effb6d-ee46-3084-8928-8fec566893d1 | -11.03199 | -41.28366 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 9f5b80c5-9c9d-3dcb-9dcc-9c83eb6f89a4 | -5.91102 | -38.05563 | 2026-10-05 16:37:00 | NOAA-21 | TABOLEIRO GRANDE | RIO GRANDE DO NORTE | Brasil | 2413805 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b887d8f6-d820-3fa7-81dd-6c1467d33da1 | -7.90098 | -44.18745 | 2026-10-05 16:37:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9003ddb1-a999-35c4-afc2-54d751294931 | -8.65959 | -54.56742 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 51d927bf-4515-37a6-bf10-ce6d85cf5dc8 | -11.82387 | -43.54119 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81549acf-dc72-3372-bb29-bf80be3851ba | -7.17664 | -41.99769 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9baea50f-641b-3fb3-b6ee-2e583efe255d | -9.81721 | -44.79335 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5a36282a-f694-383e-9867-bd68e1c705e5 | -6.70183 | -45.2461 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| c4eea30b-1af5-30be-927b-60cdfac1da58 | -7.18313 | -42.01162 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b630e556-efdc-3e00-914b-20ee41d967f2 | -7.19911 | -44.3072 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 1ffbb5ba-d0ac-3031-b283-430fabe73ebe | -9.15148 | -45.1343 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 2a77c5e7-a194-3c8f-84d7-0d52fb8a66c4 | -6.73477 | -39.12249 | 2026-10-05 16:37:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7bffe373-6827-322f-808c-46d2104894c7 | -9.79632 | -47.78163 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d32783b-ccfe-3906-8c31-ea95c755413e | -7.18254 | -42.00798 | 2026-10-05 16:37:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 234ed34f-b136-378e-88af-f0ad01c504b1 | -12.19787 | -44.65765 | 2026-10-05 16:37:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7b30957d-f22a-3560-922f-167c0af330c5 | -11.67656 | -47.29842 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 58162aea-a64d-3271-8e23-e6e1420815e1 | -8.6469 | -45.83811 | 2026-10-05 16:37:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8781961d-71a2-3f9e-9fd2-9cb46316b92f | -9.76239 | -44.80212 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| daadecc0-a726-3b87-8bae-67ef0fd9f8a5 | -9.0892 | -46.47955 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 39b032f4-797b-30f4-aaa6-6fa3229636ae | -11.48384 | -47.00866 | 2026-10-05 16:37:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c17687ed-9dbb-347d-b351-1b4c48f285a2 | -11.81168 | -47.36127 | 2026-10-05 16:37:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8de227f7-c74b-371d-9254-94a25341de78 | -8.54115 | -54.58795 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ae7f5370-4eda-364d-9426-139f4e19929b | -6.33415 | -42.56582 | 2026-10-05 16:37:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 98825967-133a-3972-ba82-5bde330fc544 | -6.322 | -43.34408 | 2026-10-05 16:37:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b0e0b639-11df-3347-986e-9908706ffa0a | -11.34737 | -46.66726 | 2026-10-05 16:37:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 661fc246-0a0e-39be-962a-4ea1e25ee200 | -6.88017 | -43.67216 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 878a8bd7-694f-3a8f-878f-1f926e535189 | -6.59519 | -41.57852 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 4fe4deac-7e21-3916-8608-66f4c0ebc4e8 | -12.62589 | -40.46132 | 2026-10-05 16:37:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cab5e184-c0d7-3bd5-a6cd-a1ec559e0f61 | -6.70228 | -45.22636 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f6c515a9-2ce1-3bee-8a60-d6a630cb8b66 | -13.52041 | -40.9109 | 2026-10-05 16:37:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 28fd2d5a-4a50-3d07-9ad7-86d632483ede | -9.91684 | -47.70097 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 205c6a2e-1264-35ad-980a-32778b8f20b2 | -8.03562 | -40.55814 | 2026-10-05 16:37:00 | NOAA-21 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7df6b1ea-cc49-3324-80b7-6261171b8552 | -8.27758 | -39.07382 | 2026-10-05 16:37:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 4e3fc07d-cafb-3fe8-801f-39479efa7f97 | -11.02731 | -41.28068 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 22d4f1d3-ffde-362b-9bbf-7935a18f0805 | -10.30255 | -40.10961 | 2026-10-05 16:37:00 | NOAA-21 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a393a8d3-0d8a-379b-b997-f015a738e089 | -9.75896 | -44.80267 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de740a99-6439-3b34-a459-454f401e5be3 | -7.24292 | -44.01728 | 2026-10-05 16:37:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 30f5d490-64af-344b-b8e0-fdea2dc33756 | -8.53775 | -54.59895 | 2026-10-05 16:37:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 8750e5b2-3453-3253-a65f-173437df9ef9 | -7.10292 | -42.53884 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b29abd62-4aa5-3b58-bf4f-b8124d64c4ff | -10.96215 | -45.40061 | 2026-10-05 16:37:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 44bee5c6-72ce-3cea-b088-bd59274a80ab | -6.8115 | -39.29852 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 396af4b4-0b81-3a1a-8e92-0123eb480ca7 | -9.86959 | -44.83556 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fc44a6db-35fc-3912-bf77-d6c01352d321 | -10.53355 | -46.4543 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| beb2d63e-d419-3cd6-ba5e-8c30d26aae12 | -7.47637 | -45.06522 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 00013663-3801-3973-a6c5-278a89fb9071 | -5.68642 | -36.70919 | 2026-10-05 16:37:00 | NOAA-21 | ANGICOS | RIO GRANDE DO NORTE | Brasil | 2400802 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 93b4df22-83ce-328a-9c1e-4cacc69a597f | -6.95413 | -43.21963 | 2026-10-05 16:37:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 240b91d7-5fe0-3413-a399-aef94527c105 | -7.28347 | -42.41568 | 2026-10-05 16:37:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 5bbf9e11-4d17-3021-98d2-3529c3645c2b | -13.60318 | -42.49548 | 2026-10-05 16:37:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 8a73c7e9-2a8a-341a-b8d1-4633c311bf4d | -9.0432 | -46.8903 | 2026-10-05 16:37:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7142ade3-b862-36f0-b3c7-c71b398c2492 | -6.70409 | -45.23789 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| cc57c144-ed82-3f7a-b587-563bc52a8daa | -8.43309 | -39.54179 | 2026-10-05 16:37:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d8b95e72-0bad-3aa7-b897-d8f295a77764 | -10.34147 | -40.07036 | 2026-10-05 16:37:00 | NOAA-21 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8b346780-55ac-3383-b605-4f5a7b527123 | -6.69491 | -45.24721 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 0252eacf-bcde-3d37-8978-5722d568aae4 | -9.61654 | -45.8206 | 2026-10-05 16:37:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 736b8675-f0e1-3f92-b621-cce85122ae38 | -8.62441 | -44.9071 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1754db61-52c1-34d5-b5cf-7190a485c42d | -6.85611 | -38.68029 | 2026-10-05 16:37:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ff9d8d34-1de6-3127-a0ef-ad8a4cc2f050 | -9.76864 | -44.79723 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1d2dd50-b3e4-3e12-86b7-8f5fa2a98bd2 | -13.32734 | -39.07113 | 2026-10-05 16:37:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| 3789c4d9-66a6-35e5-84be-f6215fe2044f | -11.67613 | -43.65973 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 393f99f9-b667-3aeb-907c-7f36d6b0e055 | -9.62042 | -45.82363 | 2026-10-05 16:37:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 805fa9a3-9e14-3a44-be0a-6bb0308b5455 | -11.17167 | -44.61193 | 2026-10-05 16:37:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 71be4453-a17c-3e2b-a679-a90a76921aee | -7.29659 | -43.79195 | 2026-10-05 16:37:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 32b4f29c-1c6e-37bf-8c71-1bfa2cef2896 | -11.09927 | -41.26081 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8142b576-c075-33d5-b5e3-b2ce2f04dd9c | -9.15772 | -45.12962 | 2026-10-05 16:37:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| f81fc152-a135-3fa0-aa5d-16916865041a | -8.64746 | -45.8417 | 2026-10-05 16:37:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fb592018-b2e5-3f62-bc85-568a222928fd | -11.09099 | -41.26271 | 2026-10-05 16:37:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| aae18312-53f4-335c-9f78-a8ece3b4d31d | -9.03133 | -45.17262 | 2026-10-05 16:37:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 384ef875-c26c-38a4-95d3-6b8ffad22ab5 | -9.41886 | -47.30446 | 2026-10-05 16:37:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff44e4f7-3787-341b-b98c-afd12047e9ea | -6.37757 | -43.63933 | 2026-10-05 16:37:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f9e9753d-e6a7-3677-b38d-04fb33240f15 | -13.32637 | -39.07447 | 2026-10-05 16:37:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 676284b8-cd86-390e-90c0-872f6d80658e | -6.70168 | -45.2225 | 2026-10-05 16:37:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f839e088-a918-3af1-9c41-8ab6d65f762a | -6.61451 | -41.77008 | 2026-10-05 16:37:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| cd5d95e3-1b4d-3f56-a6aa-16423090e60a | -10.5097 | -46.05648 | 2026-10-05 16:37:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8f9342cf-3d69-36ca-b526-e61458f0e40f | -8.49856 | -46.9058 | 2026-10-05 16:37:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 647363de-771b-3ccc-8e2e-ba3e80e209d3 | -6.9137 | -43.66663 | 2026-10-05 16:37:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c9c3bb12-deea-3102-8692-903cbcad201a | -10.36568 | -45.0215 | 2026-10-05 16:37:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 893b0a00-6efe-3d0c-a4f2-dca2457ff3b5 | -9.87419 | -44.84246 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ebf2a8ec-eb7c-3e9c-8b3e-871f01431cb2 | -12.62523 | -40.57841 | 2026-10-05 16:37:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f71b624a-e5d5-37ce-abed-5f4cb5949fb5 | -9.75237 | -48.1693 | 2026-10-05 16:37:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 57f248f0-6e09-31e4-a49e-a2716847fa9d | -8.15472 | -43.88211 | 2026-10-05 16:37:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 29017b34-9310-3fb1-b113-b07389598e7c | -9.7755 | -44.79614 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a8abcecc-d1c2-3458-8338-a68a56112657 | -11.63215 | -43.63393 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 890459c1-5c6e-35a2-9b35-12c983f80bc6 | -10.44453 | -48.32541 | 2026-10-05 16:37:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 308b8cd7-0d09-35d9-a1a8-b6cf20e46b5f | -11.68381 | -43.66251 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 3f0bbe84-3ba9-3a10-ac28-062582034c6d | -6.53758 | -39.50703 | 2026-10-05 16:37:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 25.2 |
| a8b30474-8889-3ebc-8549-0b6e341abb3c | -8.36566 | -38.01176 | 2026-10-05 16:37:00 | NOAA-21 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 14.6 |
| a3ab21c8-9246-3367-ad96-36ed607fa99d | -7.19976 | -44.3113 | 2026-10-05 16:37:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 7658f05f-70ed-3838-a716-5e1bfc7a9ef6 | -10.48319 | -47.24335 | 2026-10-05 16:37:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2267a582-574a-39a6-8ea2-5d845a26a0d2 | -9.82466 | -44.79605 | 2026-10-05 16:37:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 399afc42-e0dd-3310-b3b7-534fb5ea17d1 | -11.68029 | -43.66312 | 2026-10-05 16:37:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |


[Clique aqui para ver as próximas entradas](README88.md)
