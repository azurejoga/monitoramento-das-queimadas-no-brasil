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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2eb98af-964a-355f-9bd1-2ed80d167534 | -19.94591 | -44.71709 | 2025-02-14 04:18:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b31c1eee-fbe8-302b-88da-cfc8246d2350 | -20.76464 | -46.76924 | 2025-02-14 04:18:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9ef6956-1432-3794-89a2-881cb0a01fff | -21.6155 | -43.58706 | 2025-02-14 04:18:00 | NOAA-21 | EWBANK DA CÂMARA | MINAS GERAIS | Brasil | 3125002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1e871b89-40fb-34f5-9b01-a750626f6661 | -19.96944 | -44.21579 | 2025-02-14 04:18:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 83ff0cf5-17f7-3249-afbc-b94e80d1129e | -22.67604 | -42.8582 | 2025-02-14 04:18:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8be927e8-6e3e-389d-bc3e-27df117385ed | -19.85093 | -43.84428 | 2025-02-14 04:18:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b2a637c3-ba15-3127-a214-c38d7c676fc5 | -22.80185 | -42.3234 | 2025-02-14 04:18:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 00ea9cdc-3c74-3bdf-8e07-9495507de580 | -20.18242 | -42.28119 | 2025-02-14 04:18:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a1502a7a-9178-36a0-9195-498bae7d4b9b | -21.61094 | -48.46131 | 2025-02-14 04:18:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d306263d-8e17-3230-8e99-b4b6cb6d442e | -20.41893 | -43.55189 | 2025-02-14 04:18:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 07fbe564-7b36-315f-a5a6-c042953dacca | -22.67947 | -42.85202 | 2025-02-14 04:18:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 619346c2-2efa-30c2-b213-deb63bae188d | -21.08211 | -43.08414 | 2025-02-14 04:18:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 99875285-7062-3ea1-a8be-98c199fd5342 | -22.54093 | -48.81301 | 2025-02-14 04:18:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9913fb72-d254-320a-8dab-ef13a38adc2a | -22.83968 | -42.75189 | 2025-02-14 04:18:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9bb5c904-6b0f-3718-bcec-488956aaa91b | -20.41834 | -43.55347 | 2025-02-14 04:18:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 685a26fc-ad4c-30ce-9832-0df608d60bad | -22.67883 | -42.85684 | 2025-02-14 04:18:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0b0a9bcf-c294-3e0b-b375-7287d8db433a | -22.92161 | -45.41397 | 2025-02-14 04:18:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e6b41f4a-bbfa-321e-a43d-0c2a8c8ef99e | -20.57884 | -44.5743 | 2025-02-14 04:18:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e11da33-82a8-3e09-9c53-4d42cd470db4 | -30.15087 | -52.02426 | 2025-02-14 04:21:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| eb86f8ad-9e6f-309b-8096-df10765899ef | -29.86547 | -51.16388 | 2025-02-14 04:21:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 3458d618-4434-38f5-81d1-bf90211e4062 | -29.87382 | -51.15685 | 2025-02-14 04:21:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| b829d630-73b7-3a2d-86c9-1800cf5bf943 | -27.52592 | -54.44968 | 2025-02-14 04:21:00 | NOAA-21 | NOVO MACHADO | RIO GRANDE DO SUL | Brasil | 4313425 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b44ee34-3e43-3f22-843b-e478177a290b | -29.77872 | -51.17713 | 2025-02-14 04:21:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 672d48ae-c02f-3e60-91c5-ffa2ae4e6550 | -10.64138 | -44.48838 | 2025-02-14 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 854fa80b-5f36-3c8e-8c31-3de70792b6fd | -10.77204 | -44.74488 | 2025-02-14 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b11016e7-a521-3213-bc3a-4fb2944159a7 | -12.33252 | -45.6367 | 2025-02-14 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57dfbcc5-b145-3072-91f7-49f79cb57d62 | -12.49901 | -46.34045 | 2025-02-14 04:40:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e94f5d9b-0485-3746-8049-a93e71c3edac | -11.96261 | -44.66115 | 2025-02-14 04:40:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 121d8352-6d00-3e0b-81b6-c6527b3747bb | -9.04416 | -40.07994 | 2025-02-14 04:40:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83013296-acfc-3b8b-b01d-aea7849dc62c | -10.76834 | -44.74023 | 2025-02-14 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f757853-7be5-3ea1-a5ff-96b974edca74 | -12.32332 | -45.64284 | 2025-02-14 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0032dba1-905d-3ffd-bd74-d681fd50680f | -9.03845 | -40.07922 | 2025-02-14 04:40:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 435a9dfd-1170-3bc9-acf8-d7d67fbc54d2 | -12.33202 | -45.6404 | 2025-02-14 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0ebfeb6-1403-337f-a24c-3b0caf417445 | -10.64943 | -44.4938 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f53aa31b-9df2-30e4-ba70-c3d759cc37d3 | -10.8637 | -44.79327 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62fda223-37b1-3365-a3c3-35c8393ec3cf | -10.65074 | -44.49303 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13dfaa1a-801c-327b-84f8-4a26ac7443ac | -10.6421 | -44.49176 | 2025-02-14 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97ed316e-7867-34bc-a9ef-f3defe6ec313 | -12.33353 | -45.62927 | 2025-02-14 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 504afb18-de2f-3f2c-9390-ae36fb25f609 | -12.33302 | -45.63298 | 2025-02-14 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1062e99-91d1-3ad8-84ff-40aa5e48a6bb | -10.64642 | -44.4924 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f0315a1c-d2b1-38ab-8286-b1d8152650fe | -10.64511 | -44.49317 | 2025-02-14 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c447025-3daf-37f6-a9a2-6ac2144ca8f2 | -10.64629 | -44.48484 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 696d322b-b788-3567-8a6d-e18e51f18c53 | -10.77151 | -44.74871 | 2025-02-14 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec702478-82a3-39c5-a70f-4b05e0ffce61 | -10.49968 | -46.18852 | 2025-02-14 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7213c67b-cd6d-32d8-b824-00d86192f429 | -12.32892 | -45.63236 | 2025-02-14 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b808618c-ce84-3048-a6ca-02220e829341 | -10.76782 | -44.74404 | 2025-02-14 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f04009-d7fa-3884-8bf1-89dbdaa1a527 | -10.6457 | -44.48901 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| edd6fdeb-d8c1-3ea3-ab48-2fe89a9d9b90 | -9.94358 | -44.24313 | 2025-02-14 04:40:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b54fbcb-05ad-370a-a32a-bd8fc9457385 | -12.32742 | -45.64347 | 2025-02-14 04:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 931b83cb-bd59-3e96-8b55-fdc6f117fedc | -10.64266 | -44.48759 | 2025-02-14 04:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae3c02b6-76a9-3ea5-a43f-3459138038bc | -10.86794 | -44.79388 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f789785-0ca1-346e-95ea-cdb7608af1c0 | -10.65018 | -44.49719 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae224f00-936f-3834-8d2c-b5ddec5d160f | -10.64698 | -44.48823 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66d17c65-b59e-35be-90e7-3bd0a0bd6dcb | -11.96204 | -44.66537 | 2025-02-14 04:40:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ad852bc-9eed-3efc-8f84-55d3d9fe2962 | -7.30666 | -46.20315 | 2025-02-14 04:40:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab1a75c4-caeb-3ab2-8f1d-6fd6aabe3734 | -12.85146 | -43.82462 | 2025-02-14 04:40:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c3bee0-493f-386a-a37c-d1c64cf43a4b | -6.61799 | -47.90749 | 2025-02-14 04:40:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edb432b6-c477-3ce4-92e2-02094e4cc1f3 | -10.86739 | -44.79787 | 2025-02-14 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a3a9304-c6f4-3b59-a8e6-e8bdc2d2c6f5 | -15.23826 | -51.45763 | 2025-02-14 04:42:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0666656-f4e0-3369-ad5e-e198b556986a | -16.10862 | -46.20245 | 2025-02-14 04:42:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ba0835c-5a56-36af-a3d5-03562e93f608 | -15.57064 | -47.85403 | 2025-02-14 04:42:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6db09a48-9239-31e3-b424-df7e0959c5ae | -15.07928 | -48.94587 | 2025-02-14 04:42:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 847be186-7caa-37d7-b9ff-63c8d1d907b7 | -16.73761 | -45.77064 | 2025-02-14 04:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 578386ef-5b21-32d1-9724-14bdc85c2b67 | -14.28017 | -47.41128 | 2025-02-14 04:42:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7d0cd07-66ab-31e1-b3ac-e539dbcee9d3 | -15.55854 | -46.28027 | 2025-02-14 04:42:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e010ad9c-a0d5-32d7-8a00-a2d57d8c7fed | -18.90423 | -45.04056 | 2025-02-14 04:42:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1f23995-a749-3c98-9ff1-93741e0790d4 | -25.19828 | -50.86893 | 2025-02-14 04:44:00 | NPP-375D | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 340977e4-18a5-3e8a-ae12-b35397cb09e2 | -18.96318 | -53.68885 | 2025-02-14 04:44:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1c44acc-d332-3531-bd0c-fdbf80314ea9 | -25.1314 | -52.35309 | 2025-02-14 04:44:00 | NPP-375D | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46b6c369-8b56-3ecc-b135-e69589eeb258 | -23.33893 | -46.77228 | 2025-02-14 04:44:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a2e7a3f5-69f4-3d59-aadc-4f30ee36665e | -21.61119 | -48.45784 | 2025-02-14 04:44:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07f83b0b-a487-3898-bd5f-8dc7ff5444ed | -22.53855 | -48.81206 | 2025-02-14 04:44:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caf6dacf-e698-39d8-a63b-b3ebdb9b7eff | -19.90537 | -56.41715 | 2025-02-14 04:44:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 091dff7e-d6f0-3665-86af-84bc8547db1d | -27.52605 | -54.44957 | 2025-02-14 04:46:00 | NPP-375D | NOVO MACHADO | RIO GRANDE DO SUL | Brasil | 4313425 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 35bc3682-5af2-3ed0-b550-fe7fc8d37bd1 | 3.82502 | -60.04397 | 2025-02-14 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6594e1b3-64ff-32ce-a944-33880046a943 | 2.90067 | -60.23415 | 2025-02-14 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c90440b-8ab0-317b-b2e7-6aaf5351b0f3 | 2.90513 | -60.23351 | 2025-02-14 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c72e5b8d-2065-3822-aa88-20ae99e8762f | -7.0649 | -44.38535 | 2025-02-14 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f7874f9-65ab-38b8-8084-15cbe6e98bde | -7.05863 | -44.38451 | 2025-02-14 05:01:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7cf661b8-0ae2-3eaf-9229-9fb405d738c7 | -12.33011 | -45.6384 | 2025-02-14 05:03:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c05176d-977b-3cff-9440-a64c53e288b3 | -10.76577 | -44.7429 | 2025-02-14 05:03:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1429529e-c234-3157-9e6e-270c2b37f038 | -10.64303 | -44.49226 | 2025-02-14 05:03:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4be3b10f-4e61-397b-b01f-e378ddc77d90 | -15.23878 | -51.46014 | 2025-02-14 05:03:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7245989-8875-3707-8aa2-699e2af54923 | -10.64886 | -44.49871 | 2025-02-14 05:03:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f16fa20e-ae87-3c93-91b7-e6ab9767f3bf | -10.77153 | -44.74936 | 2025-02-14 05:03:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb2768a9-9981-35ff-b06f-c8c1ca1a645d | -10.77209 | -44.74453 | 2025-02-14 05:03:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ed438d4-1972-3a71-87b1-453d8b325eb0 | -10.6437 | -44.48665 | 2025-02-14 05:03:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 687d8a90-212e-37be-8879-dcdfd6f54b5c | -15.23935 | -51.45576 | 2025-02-14 05:03:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f68fbd-2788-33e0-8dd5-f2db8582bbfa | -12.33068 | -45.63353 | 2025-02-14 05:03:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b14868e-6f49-387c-a579-1634b44426ca | -12.33628 | -45.63926 | 2025-02-14 05:03:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da087b6c-dd17-3d9c-aa6e-bf9ea7094205 | -20.62734 | -55.70092 | 2025-02-14 05:05:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51c60d7f-84dc-3f17-9547-5cbe5d34a256 | -20.62674 | -55.7053 | 2025-02-14 05:05:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d795f5fa-77e5-323a-81df-5b15df54b048 | -20.62309 | -55.7048 | 2025-02-14 05:05:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aac81483-91d2-3c4b-b2ec-1cfda684c4f8 | -19.15502 | -55.32951 | 2025-02-14 05:05:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c60fc7a3-462c-3594-b7cb-6353f89760ab | -16.19403 | -57.29504 | 2025-02-14 05:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2efe03f-4b2c-3ea4-a334-8bf496bd4145 | -8.11752 | -43.12716 | 2025-02-14 05:42:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 15fa5657-3c45-3a58-a883-e86d7eda4f6d | -12.32826 | -45.62632 | 2025-02-14 05:44:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6323c13b-6697-32b2-a8be-3ea9af867886 | -9.58454 | -37.27081 | 2025-02-14 11:53:00 | TERRA_M-M | MONTEIRÓPOLIS | ALAGOAS | Brasil | 2705408 | 27 | 33 | nan | nan | nan | Caatinga | 7.8 |
| cb2c855e-9da1-3775-a575-1f94e9b3b237 | -6.08445 | -37.31409 | 2025-02-14 11:53:00 | TERRA_M-M | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e99a6ed0-a69b-313f-b33b-c6b94059d8b7 | -9.36107 | -37.35357 | 2025-02-14 11:53:00 | TERRA_M-M | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 7.9 |


[Clique aqui para ver as próximas entradas](README4.md)
