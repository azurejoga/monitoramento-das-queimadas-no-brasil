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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a3f92fa-a66e-3297-87de-614c29c858f7 | -19.82293 | -48.23766 | 2025-07-20 04:19:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b43cc267-62b5-3d22-856e-0472bfed78c9 | -23.20606 | -48.99449 | 2025-07-20 04:19:00 | NPP-375D | ARANDU | SÃO PAULO | Brasil | 3503109 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f0ad243-48c6-3382-8598-3d5f93e008d1 | -19.89847 | -45.04202 | 2025-07-20 04:19:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f68ab52e-e5b2-3aa1-8738-91ce2f2e5d2c | -21.08092 | -50.62629 | 2025-07-20 04:19:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51b30e7a-221e-30a9-bad7-b9933a98eaec | -19.02052 | -54.66191 | 2025-07-20 04:19:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4216b62-1768-3cf9-bc81-3d20bb138002 | -22.13211 | -43.19051 | 2025-07-20 04:19:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d9b73bd6-3681-34b8-b3c1-55c67a10972a | -20.06189 | -47.58589 | 2025-07-20 04:19:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4cfa924-93d3-3855-bc9f-b931382f4748 | -19.16036 | -49.12331 | 2025-07-20 04:19:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd68d4eb-1af1-3fa4-99cc-a6b7df22aced | -19.89904 | -45.03827 | 2025-07-20 04:19:00 | NPP-375D | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d70d71ea-a19b-3028-915a-8f655ed5873c | -22.42959 | -45.45245 | 2025-07-20 04:19:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| af68eb05-0d01-3818-bc38-169f04e44127 | -23.37748 | -46.3339 | 2025-07-20 04:19:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b73a4e72-fbbf-3f15-b00e-3a2482fc7ce0 | -23.3383 | -51.9023 | 2025-07-20 04:19:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| a9731bb2-c6c0-3d21-9c39-f2e82a587cb2 | -23.33729 | -51.90768 | 2025-07-20 04:19:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 9459c241-5f40-3af5-92b6-db253816bb6c | -21.94841 | -47.42235 | 2025-07-20 04:19:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 109b8139-1b08-3340-93f0-9d4390c626f4 | -22.13944 | -43.19178 | 2025-07-20 04:19:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e8f8ed95-c012-380f-a1ec-0cd716814ccb | -23.2524 | -47.11741 | 2025-07-20 04:19:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9d3fdc74-6872-35a4-8e5d-ee1162a0cf7a | -22.13576 | -43.19124 | 2025-07-20 04:19:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c52682cc-75a4-374e-93ed-7e9b96f27ecb | -21.13922 | -43.95768 | 2025-07-20 04:19:00 | NPP-375D | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b67f9ae-f1dd-3429-9b86-0519cae919dc | -20.05789 | -47.58908 | 2025-07-20 04:19:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cebe3786-5172-3b25-a25a-ebf7f57f0f3d | -22.43685 | -45.47355 | 2025-07-20 04:19:00 | NPP-375D | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 744ef382-fad2-331f-b932-b8d34b449696 | -20.1004 | -43.90894 | 2025-07-20 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0b6cb481-9763-30e8-b230-0e60401db152 | -10.6689 | -46.7853 | 2025-07-20 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7af16d38-cb67-3fcd-b1fe-c77d47f8ed4a | -10.6496 | -46.8101 | 2025-07-20 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1848fe1d-8a00-3047-ae67-54ddc4307aac | -10.6686 | -46.8077 | 2025-07-20 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f9fb637b-c2d2-3d0b-85c2-4f2307f1f4cd | -29.98037 | -51.20438 | 2025-07-20 04:21:00 | NPP-375D | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| d344436c-26c9-32f7-af5a-b296c83e154d | -10.6686 | -46.8077 | 2025-07-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 5e84c72c-a1d4-391e-9a7d-b25396ce098d | -10.6689 | -46.7853 | 2025-07-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| cbfeafd8-503d-3a76-a61f-a2e287c1c430 | -10.6496 | -46.8101 | 2025-07-20 04:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 670bb60f-3a62-3100-8017-ace9e13bbed6 | -7.27551 | -50.33149 | 2025-07-20 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71186c98-9618-368f-a50f-d53f0d8bdd32 | -3.79181 | -41.00646 | 2025-07-20 04:38:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bab6d89c-3275-3855-bbb9-26ebdf95179c | -7.995 | -43.69056 | 2025-07-20 04:38:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88c1da38-2457-3995-9557-54d574dbb9dc | -7.25494 | -60.12318 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed074925-8c2c-35d2-b260-54bed8fd92df | -7.92497 | -49.68174 | 2025-07-20 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfda5d66-1df4-3f0b-810b-36eeb7603a1b | -2.9154 | -48.2457 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f339d72-8f26-3a21-826e-16fbea0e567f | -5.58597 | -44.8931 | 2025-07-20 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a80e3639-2827-3b72-baa8-74f852fc1917 | -8.08811 | -50.11219 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 34ac8060-f6a3-382d-be69-5c9c853917b2 | -8.07709 | -50.09623 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7abbc973-4688-357b-9094-428a495569dd | -8.35643 | -46.64404 | 2025-07-20 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a18bd3ea-87c7-3c28-b9cc-7c9fe7dedae4 | -3.1133 | -47.00735 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2af4c91-4f0d-3449-9aa3-25280732a9d6 | -9.63806 | -40.6012 | 2025-07-20 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 669dcf31-d4c2-3317-a831-5d7ca885f87c | -3.11214 | -47.01469 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 629a298e-d2a9-3fd2-9db4-1fbdafccdfd7 | -9.5445 | -40.32704 | 2025-07-20 04:38:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d9929047-4b7d-3e9f-ade9-ee941fed11a1 | -4.07506 | -48.04168 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9ffc3d6-82b8-3e8c-88b9-bb48b74fbbd4 | -6.92557 | -44.83386 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aac5cc3e-a28c-3154-be0e-79d80c941469 | -5.62667 | -42.30111 | 2025-07-20 04:38:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 07406fd1-af52-3abd-b9c9-3827b34cf876 | -7.70964 | -47.2933 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bda59935-f9ac-369a-b18a-b24ff9d5ea15 | -4.59806 | -43.31628 | 2025-07-20 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f24b8307-1bf2-3dd7-9871-01564053c26e | -7.25989 | -60.12864 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44b66fc1-9221-3b98-b852-3780f042cfd9 | -6.92156 | -44.83344 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40450c31-c71f-38ae-8842-8bfc84e65b21 | -7.26619 | -43.10554 | 2025-07-20 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1e58c058-1be3-3000-ba50-356c2e2647b9 | -3.31685 | -49.04175 | 2025-07-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f902a31-d2c9-3681-8b1c-11ce2cc1312c | -3.59003 | -47.52108 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 985ddb21-cda8-337c-ac76-ff16c2def3b6 | -3.91796 | -42.41628 | 2025-07-20 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8093c2b3-5138-323e-9108-d578a5f2f149 | -5.63063 | -42.30655 | 2025-07-20 04:38:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| caa4ce59-664e-3f53-9e77-1ebd3aa0f2d1 | -7.26299 | -60.11802 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e7800ce-2c2c-352b-a78f-0351b465b46f | -2.44406 | -47.32707 | 2025-07-20 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85e44e12-a065-34da-bac9-fcd0daf10ebe | -4.0756 | -48.03818 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2ed18f-d63f-336a-af11-ce9fff592d3c | -6.81021 | -43.80618 | 2025-07-20 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 972b189c-3cac-3c03-af89-17e8f1648036 | -4.12759 | -47.65819 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f93b80ff-3677-3aa5-a6d8-c7407d995925 | -3.10874 | -47.01417 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c555bd56-b9d3-3e9a-9ccb-43d6c95b8f44 | -2.91209 | -48.24519 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 385a3c36-5de5-3f6f-8c6b-14bc8da0b431 | -4.07839 | -48.04221 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 683667fa-9c11-3b36-badf-f0442ec160b0 | -5.87496 | -45.21054 | 2025-07-20 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0a00fe1-66b4-3bab-b706-d549fee9c228 | -2.98056 | -49.10507 | 2025-07-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b50c4219-240b-3275-9504-87941bd4529a | -3.03995 | -47.86341 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 003236b0-c4fa-3ff8-b3e3-e37bf63ed999 | -3.51607 | -47.2108 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 704b31b5-44da-3d7b-88a8-9e6ad99635f8 | -4.59013 | -43.31099 | 2025-07-20 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06c11204-f282-33c9-89b6-6436b57a4e1e | -7.22988 | -44.12638 | 2025-07-20 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da5564aa-a215-3101-bef8-b7435a28f6cc | -7.17033 | -44.09362 | 2025-07-20 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abc936f6-4f61-3b99-9803-233cde12625e | -6.92854 | -44.84117 | 2025-07-20 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06fbd2d8-d188-339c-9c04-2f9edb86de24 | -4.59439 | -43.31162 | 2025-07-20 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 194f1931-3417-35cd-ae00-593c72064286 | -7.70672 | -47.28888 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b0f0d70-25ae-390d-96c6-c54a4e64536a | -7.27495 | -50.33496 | 2025-07-20 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df427c7-431e-3d8a-955e-112df8f22c79 | -8.06882 | -50.08428 | 2025-07-20 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5010c0c1-64a6-3f2b-a207-7ecbed4a9a15 | -7.25728 | -60.11689 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6702a6e1-1aef-32a8-9955-30b9a97d360b | -7.48465 | -44.71127 | 2025-07-20 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4831ffff-add3-36c2-b74f-4b35f24b2407 | -6.36614 | -45.38792 | 2025-07-20 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76d1f4b3-cebd-374b-9973-445642a22b28 | -7.26782 | -60.11727 | 2025-07-20 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77c3566b-e43d-3957-93ff-ec423e695de9 | -5.65444 | -44.35257 | 2025-07-20 04:38:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39ced35f-f51b-370d-ab8d-14096aec8b63 | -5.03637 | -48.51997 | 2025-07-20 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dccdf746-fb26-36c8-b670-b9f00704a1fd | -3.58666 | -47.52056 | 2025-07-20 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c4e54aa-3992-3f3e-b8c5-0be63311541c | -6.86323 | -47.81577 | 2025-07-20 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd5c0a60-0957-3469-b992-39d3fb9cc076 | -6.86266 | -47.81947 | 2025-07-20 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b1b687d-4fb8-3017-a7ab-0b8834d24f9a | -3.65426 | -48.32261 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c036f42e-525a-3c43-af1e-5984047113f0 | -3.90898 | -42.41494 | 2025-07-20 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 35c1ba3d-b9b7-34a2-8fbd-995328f48243 | -3.10533 | -47.01365 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2d73dd9-0733-31d9-b925-685785f0599f | -7.42373 | -44.2772 | 2025-07-20 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 951ead62-13da-33c6-b201-ae81fa052846 | -2.58531 | -51.92143 | 2025-07-20 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60e9ec40-efde-3455-aaa7-77cc206ea7e9 | -3.88149 | -44.39169 | 2025-07-20 04:38:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b89294c-68e8-39dd-a2df-689dca03a207 | -3.94175 | -48.09327 | 2025-07-20 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e2f4b2-cec0-3af0-af4d-bf85887ac723 | -7.70262 | -47.29226 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7a5f50b2-714e-3adf-aee0-b8042afa3097 | -7.69619 | -47.28722 | 2025-07-20 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b79516e-b0ed-3eae-8945-7f4e0582baf9 | -8.07632 | -49.90792 | 2025-07-20 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0c47142-f061-3570-aa03-de8a9d88fdac | -8.26024 | -46.36002 | 2025-07-20 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c66cba67-af1a-3b3d-bac9-31708a85f4ce | -2.98386 | -49.10559 | 2025-07-20 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 829201de-6e77-30c8-b19b-7b5375f70668 | -2.91263 | -48.24173 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2273d10-a121-313c-b4f5-91e606a40bd2 | -3.03608 | -47.86638 | 2025-07-20 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| b1f7ca18-4903-3322-a32b-3a2837ed88af | -7.99995 | -43.68705 | 2025-07-20 04:38:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deec96b5-f6b5-3470-9973-437c141eb283 | -2.90547 | -48.24416 | 2025-07-20 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 545103e5-60b6-3bb5-be17-631ac59e54fe | -2.4435 | -47.33064 | 2025-07-20 04:38:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
