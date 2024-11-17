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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c1c3678-dedd-3a77-916f-4971085fd217 | -8.44034 | -44.19835 | 2024-11-17 01:02:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 111dad4f-359a-3a41-94e6-79d97312d6b5 | -9.86543 | -47.52542 | 2024-11-17 01:02:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7501b1c2-52d9-3c97-b7ef-fff9b650e32b | -10.54677 | -44.67191 | 2024-11-17 01:02:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ed19d88e-01c8-36ed-87f5-915065c17ef4 | -6.47758 | -47.51291 | 2024-11-17 01:02:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e96fedc6-22c9-344a-8fa7-f38a96a860f4 | -9.87113 | -47.52871 | 2024-11-17 01:02:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2e16667f-9ef3-350f-bdea-093e5d9c898b | -6.49573 | -47.49879 | 2024-11-17 01:02:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d47dbc43-b6ea-3f27-b042-fe3bd1a31c58 | -12.26692 | -44.98071 | 2024-11-17 01:02:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7800bcd7-8d86-331d-b85d-6a96b502d096 | -8.44602 | -44.20948 | 2024-11-17 01:02:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 96d49af6-5541-35f6-ad19-a9ff46047ad2 | -11.15629 | -45.1146 | 2024-11-17 01:02:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26e1f6ad-dca0-3cf0-bea6-1024503a93d5 | -9.12593 | -44.43155 | 2024-11-17 01:02:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| ada99f25-e519-3ccc-9636-96dfa5a71a30 | -12.26904 | -44.9941 | 2024-11-17 01:02:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e7810aab-f00a-30d3-bd83-16abd592afa4 | -9.86691 | -47.53572 | 2024-11-17 01:02:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8441c234-10f7-3cdd-b56e-18e213ed6e6f | -12.44388 | -43.79052 | 2024-11-17 01:02:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4478482a-5d4a-3130-93c3-fde74ca0943a | -8.4526 | -44.19608 | 2024-11-17 01:02:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 07296e0e-5067-3a4b-bf0c-9930d076a396 | -6.81895 | -46.78135 | 2024-11-17 01:02:00 | TERRA_M-M | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d4d9698b-c2e6-31cd-b08c-e1a5a9b8ab40 | -8.44307 | -44.21624 | 2024-11-17 01:02:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 60ff59c9-76d5-38fa-b466-9cb8ceb08660 | -8.44313 | -44.19147 | 2024-11-17 01:02:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 170e342b-4bd3-3729-82ca-d56066705ae3 | -11.18503 | -44.6243 | 2024-11-17 01:02:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fc9123ef-2440-381a-9e4d-ced99fb47fe0 | -6.38715 | -45.68369 | 2024-11-17 01:02:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f6c3cd93-c8f1-3b3d-80a0-85a52b4a2089 | -9.39067 | -40.326 | 2024-11-17 01:02:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 1e45382b-a2de-3852-a668-7acc4606c6c8 | -12.39629 | -57.5208 | 2024-11-17 01:02:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| a2193fe3-757b-32b6-b1a3-7224c4c70c01 | -8.44879 | -44.22681 | 2024-11-17 01:02:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 16530e0f-999c-3eff-84dc-6d7003507238 | -10.53748 | -44.67994 | 2024-11-17 01:02:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6b71cc1a-ed10-32e3-a267-e3a466236041 | -9.11812 | -44.42119 | 2024-11-17 01:02:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| d051b86c-5238-3818-9b95-cf91a7d5cd76 | -12.55992 | -57.77516 | 2024-11-17 01:02:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8ee02780-25fa-3e28-bfb3-3baa70475f1b | -6.92323 | -47.83519 | 2024-11-17 01:02:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 11624fe9-ba9e-38c9-aeb9-fc4dbd0c5e6f | -10.99279 | -49.35832 | 2024-11-17 01:02:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1102ee08-a024-335d-bed5-18ff2c936715 | -9.40096 | -40.32938 | 2024-11-17 01:02:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 62019b4e-68f3-3c74-b92d-b39195a29c0d | -11.15818 | -45.10765 | 2024-11-17 01:02:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a8d91b04-346a-3d17-b639-592887bfa37a | -11.00165 | -49.35702 | 2024-11-17 01:02:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d1363fa2-b315-3426-9c0f-bbc2adbb1b16 | -1.30145 | -51.73556 | 2024-11-17 01:04:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a558ffd7-2099-3754-a9e7-0c73d8669675 | -3.56296 | -50.24715 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6355a8fd-f2a8-3f20-88f3-e27ce1b4f4a2 | -3.83925 | -51.30541 | 2024-11-17 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9b5ad366-bfc9-3e62-851b-954eaebaecea | -2.93076 | -46.72873 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| f32d335b-13e7-3021-b788-2c60ca48411a | -3.6154 | -50.15946 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 364d9ed3-4832-3f99-845b-0ea2f9694327 | -2.6026 | -47.53989 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d4883fc2-1f57-3895-acae-d165f697d312 | -2.68189 | -46.20411 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| b27efa9a-d747-3fd8-960e-209302025ba1 | -1.87727 | -50.05396 | 2024-11-17 01:04:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c99760ae-c2c3-3cd0-970a-89be90216561 | -2.87326 | -46.72262 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 064dc557-9f7c-3b01-955b-ba2a6e4cf681 | -1.37647 | -47.25849 | 2024-11-17 01:04:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c1fc38e0-25d5-3bc4-ab0d-36c5149eef6f | -3.08092 | -45.46462 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| dac25086-50f9-3737-aacb-df67055af7d2 | -2.6006 | -47.57174 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| b9b72809-db80-30d6-a369-a45732f08011 | -2.93864 | -53.30394 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 59a05592-d5a1-3e61-8875-5844f2c67bae | -2.83151 | -46.67573 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f211f812-8075-353d-93ca-65da62fc9426 | -1.90718 | -46.5624 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 0f27c58c-a7db-352a-ac42-3ed50e1f8778 | -0.89744 | -51.94864 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 3fa0d6a8-4589-3ae9-8b1d-f07e647c7583 | -0.77434 | -49.48587 | 2024-11-17 01:04:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e9ccbc2-15d7-388e-8bff-0b746268d67c | -4.74484 | -48.12806 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 540f8ae5-4e05-3500-a07c-78ce9cd45506 | -2.67619 | -46.22758 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| b26cae0e-118f-3f64-a833-979d8451ae10 | -3.69231 | -50.12075 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8ccfcc96-3841-3477-adf4-4367b3d7c49b | -1.80138 | -48.43386 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9afdbd7-eb7c-3799-a516-a35e99f0a8b4 | -2.67426 | -46.85112 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bcf12970-155d-3b38-b81a-9c2792f68744 | -4.66778 | -49.52258 | 2024-11-17 01:04:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2dae6b09-a634-34ec-a456-0638b8aad891 | -2.66236 | -46.21356 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 30f9cc33-a21f-3196-b6cd-69108b79d629 | 0.61127 | -51.7657 | 2024-11-17 01:04:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5f11f584-11f0-30b8-bd83-76776b5cec0f | -3.69767 | -51.08022 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 15f97f08-fe7d-32ae-9bc4-f134f9b6a309 | -2.93561 | -48.06926 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9d90d5ac-ccca-38d0-b0ea-361829a2f153 | -3.5655 | -50.26519 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 13db30c0-019b-3cde-9b21-351009984b7a | -1.8031 | -48.45101 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cd82a1ed-da13-3a11-856b-21487d3fdd26 | -2.80334 | -52.99494 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 91c74cfe-25e5-39be-b471-c00c6a79b0db | -3.39436 | -53.26984 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 24411c45-4af5-31cd-893b-81de9294db27 | -5.27387 | -47.18672 | 2024-11-17 01:04:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d0831d81-d4c6-312b-9ebe-da442db22a61 | -3.62308 | -50.21375 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e616a3db-3e8a-33e5-b241-91a02c7fc2b8 | -1.92082 | -46.57588 | 2024-11-17 01:04:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 15912f9e-6822-393f-94bd-4c1833f58979 | -4.55238 | -48.00128 | 2024-11-17 01:04:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 573ab740-b42d-3273-8cc5-74caf677f095 | -1.62073 | -47.52586 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7f31be17-5fc5-365c-9166-4352b11d1b55 | -4.29741 | -48.07911 | 2024-11-17 01:04:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc4a3a15-fa66-3a43-87f1-71786bdcae2b | -1.49993 | -47.4013 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9b645560-803c-3fd8-815c-a2b17ccddfea | -4.13959 | -49.36571 | 2024-11-17 01:04:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 80561a0e-18b4-3b7d-89d6-97a4dc6be1a0 | -2.91864 | -45.15692 | 2024-11-17 01:04:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d052de17-2a3d-3dbd-89b9-3b33f4d3f2f0 | -3.63332 | -50.22158 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2d28700d-c02c-36af-937b-90fdf93b6524 | -2.17914 | -48.50916 | 2024-11-17 01:04:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c60f1352-08d8-30b9-b4a9-2599eb3b22b4 | -4.40442 | -45.5096 | 2024-11-17 01:04:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 31948bff-4868-3733-aa08-b6b31227f1e3 | -0.88668 | -51.80671 | 2024-11-17 01:04:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0a0a964f-fabc-3c35-8add-a1ae14fc3507 | -0.10377 | -51.60715 | 2024-11-17 01:04:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 17.8 |
| edce49cb-ba0c-3368-807c-0fe150ae3e4a | -3.92532 | -46.52413 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3278940b-1133-3c53-942b-0f0909c7579f | -2.86216 | -46.72424 | 2024-11-17 01:04:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 212.2 |
| 91d9d689-af63-3a45-95d1-4d88bf7249a1 | -3.36361 | -51.45727 | 2024-11-17 01:04:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b22d04a-21f4-33a2-853c-5b44759e5a9d | -3.89403 | -49.98093 | 2024-11-17 01:04:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac2ea20f-7879-3da3-9dd7-b1bb96b73a88 | -1.28659 | -51.95298 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9af7b432-5fde-397e-a36f-668d2d932e70 | -2.70887 | -53.18002 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc58c61a-0031-3733-b99d-c4fc8a8757d2 | -2.25526 | -50.45067 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4258aad4-ee00-34c7-8f56-aac90c038f7c | -3.03133 | -54.10704 | 2024-11-17 01:04:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6ce6fbc3-b253-3cf9-84c9-6eb74ff823d5 | -1.62936 | -53.29652 | 2024-11-17 01:04:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0df90dd8-a25d-3357-a063-c9d61c1a6003 | -0.31536 | -48.70305 | 2024-11-17 01:04:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 58b8303f-16b0-358b-a9c4-93866197d0c2 | -4.03749 | -45.47448 | 2024-11-17 01:04:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| be700fe2-bc4a-32fc-a2fa-a4b154eb7a80 | -3.71143 | -51.84158 | 2024-11-17 01:04:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c087a675-f93b-35ef-8191-b9cee427d7c1 | -2.59583 | -47.56657 | 2024-11-17 01:04:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f059dd6d-828c-3452-a28f-fe63788f719a | -2.18483 | -50.34013 | 2024-11-17 01:04:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a9812943-5ceb-360d-baae-415870556b4a | -3.65891 | -50.60789 | 2024-11-17 01:04:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| a06da223-a6a3-3677-ac9f-dff27ff1c63a | -2.60019 | -51.79956 | 2024-11-17 01:04:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 097003a4-339c-3ba6-b23c-78edc94c7f4c | -1.22276 | -47.23591 | 2024-11-17 01:04:00 | TERRA_M-M | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| aa6fc479-76dc-3b9b-888c-b3a328ef9bc9 | -3.95464 | -46.72077 | 2024-11-17 01:04:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| dc5c204a-a972-3bb2-95c8-8c1b8111e1bd | -2.67955 | -46.18839 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ce7368d6-29e7-388f-82d8-b9c5054d895d | -2.28106 | -47.91828 | 2024-11-17 01:04:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 45f5f6e2-2b2e-3ea3-9732-ebbe1bc8888f | -2.92949 | -45.42615 | 2024-11-17 01:04:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| da192b78-c5d5-3e3e-bc13-529e5ee5db7f | -3.17785 | -53.24196 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8cee90da-d83e-30a0-9bee-cba3d72949da | -2.66948 | -46.18017 | 2024-11-17 01:04:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f03aeebf-a65b-33d1-8af8-e2ec2c5f6d5f | -3.37231 | -52.719 | 2024-11-17 01:04:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ffcc72bf-8c3b-3096-bc34-1dae9dfcf339 | -1.40342 | -51.07983 | 2024-11-17 01:04:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README12.md)
