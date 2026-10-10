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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52a76e98-93a2-3387-b50c-66213bd82648 | -10.89865 | -44.83017 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bce96f25-7a01-3c20-80ce-e7819514fba0 | -12.73259 | -47.01304 | 2026-10-10 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3bb8e3d4-d0cf-3b13-aa45-b8be74c06abb | -12.22751 | -44.69575 | 2026-10-10 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e42145a-951d-3ece-bf70-d0089c1ac766 | -12.05546 | -43.40288 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b4ee36b2-24f7-373e-8212-98e92b195dfd | -10.46154 | -47.84342 | 2026-10-10 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c50f3d3-fd8c-333b-a476-c5f7b9f84fde | -12.78445 | -44.88691 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e1070036-d7a4-3b7c-bd48-7139f13b2a8c | -11.51022 | -47.60767 | 2026-10-10 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02fe8b3b-5374-3b8c-a0aa-e55c5cf34bcc | -9.51952 | -54.67597 | 2026-10-10 04:10:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7a96bf7-eeb4-3261-9961-40ba90212a8b | -18.09293 | -42.26543 | 2026-10-10 04:10:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dec7246f-64d5-3e9b-9e41-6395b7111cec | -11.86614 | -48.02523 | 2026-10-10 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c82ee8e6-0680-39cf-b68e-f54747caabf7 | -16.54958 | -40.62838 | 2026-10-10 04:10:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 19c15ead-3ee3-3341-b7a5-428a8405f832 | -11.84288 | -43.60607 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37d9ff16-1d56-3935-8d56-c1601796adfa | -14.05994 | -43.834 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6031b0d-e216-3dfb-9b00-6af4ab67747f | -16.58261 | -46.76909 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51477455-efef-3263-9d06-6735755c0ea4 | -16.82966 | -41.03216 | 2026-10-10 04:10:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 3a7c8701-0245-3569-812f-414bc86eab94 | -11.61563 | -43.60117 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6918af8-58f6-3789-b4c7-f215352dde62 | -13.2584 | -43.99586 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81cc2986-4c33-3136-aadf-895866d59dbd | -12.253 | -44.4293 | 2026-10-10 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1940b8ac-da86-37ec-b99d-da1401bed0f4 | -13.26721 | -44.00461 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f1dd57f-3ab2-3e58-8215-5ddf5c01a3d1 | -11.21084 | -45.22028 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88972385-02af-3888-b70d-63019b37ad5c | -13.46444 | -41.34918 | 2026-10-10 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 028712a2-e10e-365d-afb7-97afd0bd5f13 | -13.38089 | -43.88862 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ce892dd-753f-3aba-ac6e-fab7bdc19d8a | -11.62337 | -43.59518 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 463e119c-5c8a-3232-ae5a-e9f2e5d71bcf | -15.02536 | -46.26099 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b5ffb28-145a-302f-90fa-1403696343ba | -11.96021 | -43.48779 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f08d754-e96d-3c2e-8b76-6412027cdf68 | -11.83187 | -43.58981 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3a1f8cc-e661-3e4e-940c-4cc1077c0547 | -11.03005 | -45.43774 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d278f1f-4249-3d11-a8be-c5c0716c35a5 | -11.0188 | -45.41891 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4ec6f177-d185-3931-9784-dc16c5c3a545 | -16.24304 | -44.05849 | 2026-10-10 04:10:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fd0c875-29dd-3bb1-9dbe-64dcb902565e | -15.02497 | -46.25384 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fd5bc4e2-c8fe-3f8c-a43e-11a2712249db | -15.10211 | -43.63194 | 2026-10-10 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 211c7760-bc89-349e-8512-8c9f994bd74e | -10.46488 | -47.32828 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34d25557-f776-3e84-926e-e40049f78913 | -14.45844 | -43.9618 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5427bad-2476-3c72-a044-61c882222044 | -12.58571 | -44.13648 | 2026-10-10 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4dbee96-e659-3e09-94af-4efc2a7a424f | -11.98485 | -43.50668 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 742bdf6f-dd38-3cd8-87bf-6d1f8d3cde31 | -13.3704 | -43.89053 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d80e1b3-bed7-3a2f-bb04-7ea011710b8d | -18.26985 | -42.34838 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4cf2ac6d-1a0b-39ef-a0ed-cd1b8315afcc | -16.56155 | -46.80395 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a2e1a6d-c8f0-37c5-8a2a-28f223da98e6 | -13.17966 | -48.12859 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c79b1064-fe35-3279-92a3-1075042ad9a8 | -11.60166 | -43.68934 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b76437be-cad9-39dc-8109-abe511aaae69 | -12.02508 | -43.48801 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d7e7247-77aa-3ab2-a420-11a4c34e717f | -14.33986 | -55.02028 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d200619d-09a2-39f2-8601-05f8b66754ec | -9.96061 | -55.33171 | 2026-10-10 04:10:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e5e2ee04-a5ce-320a-84da-42c28e9fd060 | -10.83076 | -47.35994 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67228728-5174-3be2-87db-f60864783f9d | -14.4585 | -43.93997 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87167198-6f22-373d-a1c9-2aee6eaabbb9 | -11.61287 | -43.5971 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de71c8d1-c73e-33d5-8b8e-04b0f68685ce | -12.2127 | -44.83769 | 2026-10-10 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 588813cd-761a-342d-9d0e-75914a32857c | -17.93988 | -43.95222 | 2026-10-10 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3eeefea-bb97-3368-85ac-f6c2afd892a1 | -16.63586 | -40.5959 | 2026-10-10 04:10:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5ce312e6-ed2c-3ae2-892c-bd445dfce5bb | -12.38456 | -46.60989 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce08aa37-000d-32c7-81c0-5cdba5ab5a0b | -15.39729 | -41.90303 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 5a176f98-8f83-38ab-99d3-c95791a8a370 | -17.09794 | -41.56596 | 2026-10-10 04:10:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 19f8b53f-94c1-39e4-af9f-f26dea7f8a87 | -11.59846 | -43.62372 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b48f5fb-0153-351a-ba5a-b3a55d21ef18 | -11.9536 | -43.4867 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb978fb6-a2dc-3101-990b-41e19103948c | -11.95636 | -43.49073 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2d58075-b367-3754-a145-ebe506fc2693 | -14.97344 | -47.54346 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3df5b8c2-e02e-32c8-ac4b-c79e3298b4ff | -13.25047 | -42.25378 | 2026-10-10 04:10:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6f61f08e-d959-3511-acae-78600874a279 | -11.96517 | -43.47781 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd24f22-f6f7-3730-bfa7-4231176a4e23 | -11.96462 | -43.48133 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aeb4824-a15d-3e6b-8193-c25d8c7b839b | -16.12206 | -43.74572 | 2026-10-10 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9ec9518-1017-35cc-9b28-2b0017bd5771 | -15.34589 | -42.77731 | 2026-10-10 04:10:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc707b3b-be56-3fa7-947c-46c3752f82f2 | -11.84851 | -43.5274 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ab2561e-5cdc-3f19-ab92-c1212fa16b70 | -12.78463 | -43.89173 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07bdc3bb-368a-316b-af6b-052371f5ba42 | -14.44368 | -48.12572 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a56db032-49c1-3748-a706-7bb3f9ac3b0e | -11.95031 | -43.48612 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11a9a6bc-ab59-36d9-8c6d-d5875f9957e8 | -13.38807 | -43.88616 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf727d6f-4e0e-345d-b4cd-77f1525c7009 | -14.85372 | -44.19581 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a414e73e-560e-30d0-a809-8e12cb9a4711 | -11.225 | -44.83371 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1bc12b6-a03f-36b0-a8e4-86cfcea6406e | -17.94427 | -43.96766 | 2026-10-10 04:10:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb1c63a-e4e8-38b4-b9f8-abfc832a75b5 | -17.45757 | -45.07387 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e93b961c-91b1-3232-aacc-1c23bd05946b | -10.97863 | -45.19847 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27053374-789a-309f-bc02-70037dd4c335 | -13.39194 | -43.88316 | 2026-10-10 04:10:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 004cca07-7da8-3f80-bc5c-17ec00020b1a | -13.39334 | -41.33139 | 2026-10-10 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3a201d36-b3b2-38e1-83ed-32cce55702e2 | -11.68516 | -47.30168 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d0c72f3-8c84-3ff6-8093-81be709d41c4 | -11.73364 | -44.9479 | 2026-10-10 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4391d02d-2633-3ea1-aaf8-8f4a6e50865d | -17.46578 | -45.08645 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d40763e5-67a0-34d4-9ee6-e248e8f8e95a | -13.53017 | -47.42241 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a0a85263-9df2-338a-99ea-95881c41f802 | -11.56844 | -43.70575 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ef82ccc-d768-3eae-9f55-96cf413609a4 | -12.7737 | -44.8889 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90e13142-71e8-35ca-9f8f-0a0acd875a9a | -11.94866 | -43.47506 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8dbe157-044e-3f98-a1b1-b72102d78060 | -13.91899 | -47.8497 | 2026-10-10 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db572650-cfbe-32fe-afa2-41daa7b9b181 | -14.38705 | -54.97289 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c702a32c-62fb-3281-9000-b28935219b4c | -11.59667 | -43.6994 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83d83120-1e19-3962-8c44-6b694a12216e | -11.38194 | -55.15985 | 2026-10-10 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05a62d21-5b60-3081-981d-cc2f1f34f6b4 | -12.6979 | -43.0791 | 2026-10-10 04:10:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a7d9c099-4a06-3068-aa27-c1ae5ae57253 | -10.89825 | -44.81128 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16b2ccaf-cbef-3c90-a93a-7f5c86db30c5 | -14.87389 | -50.30382 | 2026-10-10 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fc9de657-9bc3-36f6-b975-7a69f2a35a41 | -11.0251 | -44.05653 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 801fe5bd-e9aa-358b-be1c-2edd81425fc3 | -11.56349 | -43.6941 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11b19419-357f-3f6c-a30a-26ca7c35bde9 | -10.89483 | -44.81067 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4574c162-3b8b-346c-bfac-3b1efc311fe6 | -14.44367 | -47.05873 | 2026-10-10 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb566cc4-220b-36d5-a5ae-84203c79d705 | -13.63241 | -44.42494 | 2026-10-10 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09a185c4-6a2a-3ba0-a224-91395adffd4a | -12.0351 | -43.38158 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0482ce94-1c9d-3af8-b7c0-fc7c97d5b89e | -14.44635 | -43.95251 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db68da31-139c-3ba4-8b8c-0806dafe351b | -17.45973 | -45.08168 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daefc7e0-37ab-3f91-8a9b-c0f1fe2918bf | -9.9111 | -48.12883 | 2026-10-10 04:10:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f4f9ad8-de2f-354c-bbfb-e13d7c8add6e | -13.50489 | -48.59913 | 2026-10-10 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0764c551-eb0d-377a-a3df-83399a3ab7f1 | -15.02601 | -46.2571 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 19c6e72f-0b28-3f76-9ef4-8dc5bc970176 | -11.97014 | -43.46778 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76e2b0d7-521e-3f51-b8e4-bd0b68267871 | -12.00976 | -43.43497 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
