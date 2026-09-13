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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68030f90-b471-3586-914e-12995314d2d9 | -2.82713 | -49.23347 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e90665c-6674-378d-a9fa-6509189eb804 | -6.50722 | -47.6009 | 2026-09-13 05:10:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8978a841-a6af-376a-aaf8-0d88bdc6340d | -4.86416 | -56.02021 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8538196-2d71-357b-9a26-7a72247b6495 | -7.01345 | -44.63389 | 2026-09-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89dbf0cf-ce09-3560-b91f-4b9f0e41fd82 | -3.79145 | -48.93605 | 2026-09-13 05:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 257484d6-b682-3f3b-a172-89baf9e07be8 | -2.6727 | -57.53614 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01e00df0-404f-3497-8478-d69a5b95ea4a | -8.5809 | -54.57632 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ad4db05-29e1-3de6-9343-4fe9e7013d32 | -6.34775 | -52.74874 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be3e6e1f-bf68-3ded-b5b0-68fc9f237936 | -2.94489 | -50.41801 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3be8e24-2787-3b31-ab56-496f16e1b84e | -6.31137 | -59.95876 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 960e20a1-6188-34cb-84dd-5b0c14b17460 | -4.92373 | -45.83801 | 2026-09-13 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d00cd967-57b2-3544-a8c0-8370ebabe5ca | -6.24146 | -51.70646 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e92ad47d-99ac-3e28-8c1e-5a37ee557e2d | -6.06693 | -57.86055 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 263501af-e73b-3f4d-8b67-c42e2fd2c7b8 | -5.96953 | -57.76967 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e0db1e43-97ba-3b8c-b313-12ab563c84cd | -2.8265 | -49.2375 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d3bdd29-d584-3a64-9126-f44e4efef4d0 | -2.95444 | -50.40903 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a18f6c37-81b2-3ade-a1a8-89392f5a5646 | -2.95659 | -50.41167 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c8a5c29-9fea-37de-b177-fe837d14760b | -7.86614 | -54.6947 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d73d8fb3-9b1e-3288-92ab-88decf43e9a8 | -3.04428 | -51.26732 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 291a3cc1-e1e8-35d6-8a18-b45af983a149 | -3.04931 | -51.26149 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 603b3e73-f6b0-30d5-a302-ad47c409d070 | -8.04522 | -54.85201 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9d4634c-d4a9-37af-8890-66ff8fa17b79 | -3.33333 | -42.29976 | 2026-09-13 05:10:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 98e6aa50-fafa-32f6-84fa-97f0b36b1d7b | -7.5173 | -47.3363 | 2026-09-13 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7358bea3-098f-3042-a516-808ac0d4810f | -7.20158 | -45.9276 | 2026-09-13 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1e18ced-0555-3894-8a94-334db06546cd | -5.98533 | -57.71547 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3228404c-90e6-3ab5-8c92-78319ffbdccc | -2.73953 | -57.64142 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 455efc8e-6097-3fc9-8f88-c352d320e553 | -2.46888 | -48.04066 | 2026-09-13 05:10:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da27721c-4e96-3718-be39-9a945557a777 | -8.53872 | -54.71424 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c5bd7f0-5fbe-336d-aba3-49ba2f1e0dc9 | -6.59056 | -58.8703 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f51e4eb-b545-3a95-bda0-dc14693bb33f | -2.6109 | -54.76078 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d26e0b1-3986-337e-892e-b31642c17ba4 | -3.57586 | -55.59723 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d65e1351-8019-3b53-adb3-e87622c289c2 | -4.92787 | -45.83874 | 2026-09-13 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef2d8353-24e0-300b-979e-298f1b274a72 | -5.97859 | -57.77862 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c984bc-5649-346d-ac2d-49217bd32812 | -5.96611 | -57.76913 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3ad4ef3e-5afc-3dd8-9b24-64dc04d402bd | -4.92429 | -45.83415 | 2026-09-13 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de101e45-0719-3b7c-b309-64e645678150 | -2.66471 | -57.5191 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c382d9cd-0d9b-3e10-891d-737b05b7f1b4 | -1.1914 | -55.72093 | 2026-09-13 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3762de31-5fd8-37f1-b576-2ce249a8f495 | -6.59411 | -58.87089 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6020013a-ce34-39c3-8e6b-aa48c5bfdc74 | -8.05309 | -54.84581 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7e381e1-97c3-362a-b9fc-a5f4b8594455 | -6.31061 | -59.96335 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b17664a-1246-3991-9b9e-ea88d52a9049 | -3.04622 | -51.25634 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ee9b8cd-4f68-3f69-a93a-f33b61b0ec22 | -2.96454 | -50.41287 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7955efb-8f02-3af2-83db-6ffa2dd58c9d | -1.73179 | -55.24893 | 2026-09-13 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 258b1069-cbad-3541-b633-9f50a9eb55b4 | -5.02246 | -49.99597 | 2026-09-13 05:10:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7befe5fd-b3f9-384c-9f65-ccf5628f402f | -9.37683 | -50.11067 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c786b10e-7603-3ee0-8823-112198dfec0c | -4.55477 | -55.03447 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 678cabcb-cb6f-3d99-a386-7df5d6902df2 | -3.06598 | -59.26915 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90cb9053-c2b0-3506-802a-1a2f118971af | -2.9615 | -50.38998 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe4ce720-48c2-39c6-bcc3-5d5661df4d30 | -7.95968 | -43.99942 | 2026-09-13 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1c609f9-bce5-351e-82fa-664d4e13dcaf | -2.96158 | -50.41534 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c67bef7a-54c3-3b2b-b991-0190d999f30b | -6.23477 | -51.68343 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf46a137-11b4-3b55-89e4-211ea8dbfd92 | -6.25924 | -57.77768 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 141d3327-e6a9-39cf-84f5-7ff9738887be | -2.72141 | -57.6425 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c577f28f-7d63-3f4f-8430-df2c87755ce6 | -2.9648 | -50.39489 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0605a44b-58cf-3a12-b968-b1029df2e73d | -2.11368 | -48.99873 | 2026-09-13 05:10:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fbbb915-0e84-36ca-9ae2-c87ef91b4a04 | -3.0495 | -51.25875 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a1fb854-2795-3c13-a61f-d11ca8ece8ba | -2.93761 | -50.38636 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b7d6e3c2-55a3-3e49-b6c4-f380133acb36 | -1.46567 | -52.96257 | 2026-09-13 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 071a3f35-b656-34e3-9941-69604627f4a4 | -1.7169 | -54.9579 | 2026-09-13 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2cff443-3f4f-33b1-b22b-8cb8a02ee062 | -7.9607 | -43.99729 | 2026-09-13 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b854a749-2919-37e9-b041-7c0f8d29235f | -6.98759 | -59.76329 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50e823a7-d65e-30f5-b4cb-4a68350ed4a9 | -6.33964 | -57.86624 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3fa8007-e7b1-3450-be52-e7f57a0a8485 | -6.30497 | -52.93327 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12c74234-50a0-353f-83fc-4f766360e339 | -6.61383 | -58.8617 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c93f2e3-ec05-3cba-a261-90bc2864d9eb | -4.80635 | -42.89516 | 2026-09-13 05:10:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cd8d7b8e-5b5e-3c32-bdf7-f54af3d92b45 | -6.22679 | -51.69945 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95019f38-c865-3f60-b1ee-7cf0af62e5a9 | -2.90549 | -51.93535 | 2026-09-13 05:10:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 245af578-9221-351f-b6b6-21162f311077 | -6.02727 | -59.94009 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6b61ebe-5ed8-3031-9db0-3bff4a6916bb | -3.64443 | -58.62715 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5cabc3ad-19bb-3ffc-99ca-c263b42b60c2 | -8.05536 | -54.85359 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 150219d5-ad1e-36be-81cf-c3ebe0e8bceb | -5.98201 | -57.77919 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d143b2c6-f634-39ac-90db-f5dadfa68a1c | -7.86727 | -54.70992 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb902317-cf8a-3aaa-ad17-55b106a0ecc0 | -3.60132 | -59.07635 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| df75a718-1fc8-3ff5-a8a6-5c82cc421abc | -8.04915 | -54.84891 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd3a6fae-ab6c-33b8-a45c-1e1f973a9f3d | -5.96072 | -47.21127 | 2026-09-13 05:10:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec8955d0-cc5a-36e8-a0c1-f8f8cef8c7be | -6.07984 | -57.88934 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09d952f0-b582-3043-b5ef-94df426f5ab0 | -2.68254 | -57.54165 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| da1a2772-876f-3620-b6a5-b4264e774590 | -3.21116 | -53.94551 | 2026-09-13 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e06a607-4a1f-31e8-bd1b-3059193aff2a | -6.66044 | -58.88519 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a99fa8f-d868-3474-b5a9-6f716b00b670 | -8.1134 | -54.79185 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32324789-7639-3269-9144-b058c1fc683f | -2.96239 | -50.41023 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fcd8b328-1dcc-3ecf-ad3f-be31e6e3b700 | -7.12094 | -59.63583 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 817a9257-be5f-3e76-a100-d42443d319f8 | -2.67802 | -57.52517 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1063c93f-0735-392c-a039-3c4e4eed9801 | -3.40249 | -48.89376 | 2026-09-13 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14fede66-7be0-3033-a714-8c305ddc9f8d | -2.67557 | -57.54054 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ff839a00-47bc-3582-8160-51ed9fb1cdbe | -6.85606 | -47.42617 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac5214ed-d78c-3ee2-b536-ee6341105c29 | -5.12078 | -55.96568 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6060e5a4-0314-372f-8710-550d07fc1aa1 | -6.24368 | -57.80924 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4d21064-4990-3136-b1ba-dbf59db9e0aa | -3.16578 | -58.64422 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9051108-772c-35f9-b43b-72eaff70545d | -2.73478 | -57.64861 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84e69c5c-4532-3f1c-aa60-0fe939623cbf | -4.23919 | -55.16222 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3b1bc02-2e4a-31a8-9105-96af7e299ed9 | -6.23063 | -51.70002 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8e0dc22-a8c8-3dbe-8435-ace438ed7491 | -3.56718 | -53.00818 | 2026-09-13 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a5c4cd2-c84d-3852-919e-cca3881c95ab | -2.94012 | -50.39639 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbab3986-1767-35c4-bad4-50ab03ad0aa4 | -3.04572 | -51.2582 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9938ba6-27f7-3fce-b46c-06fe62c24338 | -6.00951 | -57.67406 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de5ece95-0ae4-36cb-a9b1-bd5b86109e63 | -5.60885 | -44.84968 | 2026-09-13 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ea60468-31ff-3766-9465-0fac71a03d62 | -5.96893 | -57.77335 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acbad672-65df-3609-8a06-f709de1c4181 | -6.59805 | -58.84668 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c39bbfc-53e4-3b6a-a953-ef15f390b5cc | -5.97696 | -57.76707 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
