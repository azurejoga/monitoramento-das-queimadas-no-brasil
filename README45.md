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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d32398d4-6df4-326f-b96b-1f809077afba | -9.41246 | -50.13705 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d2c3107-1c94-3a88-a5ba-0c1830647046 | -11.37014 | -43.95816 | 2026-09-14 04:53:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5216d9c5-b9e6-3413-8ef7-3a28fd239ec2 | -3.60427 | -59.07358 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c2ab7de-9bd1-33b0-b276-39d7fc22e6f0 | -6.0748 | -59.92039 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc099479-2f1a-38fb-a1e9-8444c1ab9f91 | -6.2882 | -59.93361 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e027c915-a2ce-3ae8-a5d6-22bdcdedf6cb | -6.10733 | -57.62917 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5c3d80c-e549-329d-862c-73a81df0c7e1 | -6.38032 | -55.26098 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ba3f473-1668-3a9c-899b-0849a26ca0ea | -6.74064 | -50.9232 | 2026-09-14 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aefcc7d-d51b-344d-83ba-1a46cb61d2e7 | -6.37005 | -58.29916 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8007bb0d-6f36-3bee-90f4-157c51dac468 | -7.09845 | -41.80215 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 49e7ace0-f31a-32d5-b479-4e7eef067d82 | -7.01695 | -44.64373 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68df6ee9-0b9f-3476-9b34-d85fc77723e3 | -5.11625 | -55.95255 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3d79f88-12de-353e-a238-0f2a9520d424 | -10.54355 | -51.31214 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49a3efef-0961-306b-82b9-a0c8e2128845 | -9.41756 | -50.14922 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 192cfeb3-8db1-3825-82e5-d53c687ab1f6 | -7.51809 | -55.27645 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 767e4d21-3845-3fb0-be9c-13c3176d551d | -6.02207 | -59.94709 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84c08b1c-502c-3ef9-8d58-8f133c20ae95 | -10.66935 | -54.16819 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 2c884981-a86c-3e15-ac30-7acde23a3125 | -6.31077 | -59.96506 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5888319-1c23-3adf-9646-2682a535adbd | -6.58908 | -58.86473 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90f4fcf1-dce9-3a46-97d6-a20f61330077 | -11.18862 | -42.8073 | 2026-09-14 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81dbf157-9c95-3e9b-9d93-96bd37587fca | -5.8889 | -45.57286 | 2026-09-14 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76f6228d-e214-3e9c-888b-bd8a7925971f | -6.28167 | -55.27161 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9b2a9c9-ad95-384a-afe2-25fdc1efeee5 | -9.45194 | -40.39076 | 2026-09-14 04:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| aa9363d5-edea-3660-928b-4fe1b5245079 | -4.53568 | -54.96677 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c102dcb-a57c-390e-b30b-a991c34d23ca | -9.45578 | -47.85083 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c8c4877-7ab1-3215-b16e-e6486d75de0a | -6.10963 | -57.66945 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e09a64a2-610f-333d-adea-b23ce3be3fed | -12.39548 | -44.41621 | 2026-09-14 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46dcfbdb-d002-33a2-966c-fa14b997b4b7 | -7.86475 | -54.72116 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ec1165f-b419-37f1-b71c-9839bf348e68 | -6.10519 | -57.66865 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 907f759b-3cc4-302c-b9a0-00399f28c5fe | -7.87128 | -54.72645 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29290d8b-0be0-337a-838e-206daf337c00 | -11.23438 | -43.44379 | 2026-09-14 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e0000ef-35ac-32f0-b96e-526c32788f30 | -10.10751 | -48.86425 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7eec35d4-443f-3789-b2c4-c2f60c5741fb | -6.32833 | -60.01675 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b02a7e7c-6782-356e-accc-3f5d19fe0e70 | -6.10868 | -57.86654 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d5ef1c0-e2f7-3dce-b8ce-15dc3472fcd9 | -9.37499 | -50.1767 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a18cf2a-3d74-3c3e-8a8f-cdde2fe42cbd | -12.39622 | -44.41054 | 2026-09-14 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 43d6e36b-c9d8-3d01-a17a-5129da15f592 | -9.37669 | -50.18832 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c6e1a3d-931f-3650-bd1c-d32dc64f1480 | -5.07552 | -56.25293 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 151c3eb8-e553-3b67-aa56-764239f1a614 | -3.60377 | -59.07659 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7724ddae-f7b7-378f-acb4-52b060795238 | -9.44867 | -47.8735 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 914f80de-6617-3a9a-a8f6-05a4a3f5150f | -6.31243 | -59.95578 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86443c61-838b-30a6-80b6-8029da0fbdda | -9.36533 | -50.1487 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aa3e180-5f6b-3f62-83e2-59f5c607dc39 | -9.4039 | -50.19255 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0546975-662c-3461-83a9-b3ffb0c7cb0f | -6.81236 | -59.43282 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21c81d94-ed82-330c-8c1a-dafa713d6c4b | -9.11871 | -51.58578 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0bc5349-3065-3bf0-aba3-8243a3e90792 | -6.28773 | -55.28207 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb306954-d51d-3e48-aa19-c4ae5eec2bfd | -3.59967 | -59.06971 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cbdb55aa-88f1-3093-a65a-aaccbd3d51f3 | -8.1469 | -54.80694 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0be65b57-1cee-3684-957b-c835daeb962b | -6.87234 | -55.29033 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e1c118-4173-32af-b3aa-600fa4307763 | -6.74395 | -50.92372 | 2026-09-14 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95bc950d-e151-303b-9234-43ef1c1ea13c | -5.12724 | -55.96115 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31012dc7-e271-3faf-9136-69b8adf22479 | -6.1062 | -57.86372 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 404fbb5b-dc1d-3b89-8b71-9a18c9a26fd9 | -4.53186 | -54.96619 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25a73e4a-156b-399a-bc6f-3a4a892e5ab0 | -7.10721 | -42.1035 | 2026-09-14 04:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0914be5c-850d-35ed-b849-f5dbb2276ac6 | -6.28833 | -59.94147 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 384811f3-b1bf-3417-8840-0d4433e71878 | -7.9696 | -43.98383 | 2026-09-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58e332a8-1d1e-3940-baca-8a8cbabd4cdd | -10.54634 | -51.31619 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff215b46-ff48-32dd-8ee1-c4aba8cd22b4 | -10.68367 | -54.16672 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4585dbdb-5efa-3a38-8bef-f868bd2527e8 | -9.4113 | -50.16719 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5cf024e1-bea4-3070-9079-314ee89fbd56 | -6.08623 | -57.86234 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17d6e991-9bc6-3517-8308-38a3328a9646 | -15.56119 | -48.79103 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21d1a8d2-5e17-38f4-9ef7-49c67c5bbb4e | -11.23617 | -54.11554 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8aeb96c8-7e38-3f57-825e-8daf14342bd4 | -3.73381 | -61.75246 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb4cf569-6520-3ee9-acd0-909b043e9841 | -7.09798 | -55.63548 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e72199e1-f0fc-3a18-9d00-2a12a907cae8 | -4.40221 | -55.23334 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08db6d17-95c5-32a5-80ea-e83d45d726e1 | -10.65724 | -54.1352 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d6f2a3b7-e0c2-3c34-ae4a-ae1ffae91865 | -10.54188 | -51.30097 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38ab65ee-1e8e-3cd3-b85f-7ee5d8e02702 | -5.80023 | -52.11524 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83501c7f-e6ce-3493-bbe7-3f22e8590797 | -7.77413 | -46.66703 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd62c713-00c3-3e71-9558-a18dd3fa6e43 | -10.58243 | -51.34384 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7d048b4-edd1-385f-b2b6-ebb642897ea4 | -3.71961 | -58.87415 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5aeef8e3-b92e-3f63-a7c8-05a196448fca | -16.23299 | -52.65096 | 2026-09-14 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b229f664-4447-30bf-829a-d262b1abc9e4 | -5.90805 | -52.10019 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0798ba1b-cc80-3935-b0f1-4504c7c040a9 | -10.49188 | -51.31501 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0578fb31-99fc-369e-be8d-0a2fcb501b0f | -8.53372 | -54.71104 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f125d4fe-6f02-3208-8fa5-a5b018a3f8bf | -5.35495 | -47.37856 | 2026-09-14 04:53:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7ccd180-c0b2-3090-b73c-3dfd023dc0ff | -10.66717 | -54.16007 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 10642ccd-7390-3722-aa3d-e7bfbdd785b3 | -9.68636 | -54.8418 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9535934-aab5-39a6-82c7-e3ca13e51c1a | -3.72624 | -61.7604 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2640408d-26c2-3955-9f0c-99aa3c860a5c | -6.28545 | -55.2723 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9272ff35-1784-3678-8ff8-a1ad5caddc4c | -10.95352 | -48.36203 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08d99bcb-512d-360d-bf64-82a9b8d1b3c5 | -6.59615 | -58.85358 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be892a3c-375f-3124-a44d-4e180a44897e | -6.84472 | -55.5683 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b531008f-aed1-3f54-9852-5735fd252282 | -7.47247 | -42.11504 | 2026-09-14 04:53:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a5fcb0a1-5f8c-3e70-b9e7-f7ac1065b0c2 | -3.78588 | -55.87653 | 2026-09-14 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed7807ff-b114-3a64-88ab-3ef1429a90b5 | -10.67992 | -54.14681 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f6822952-b1a4-3dff-841b-30b4c4d1f175 | -6.66769 | -50.91137 | 2026-09-14 04:53:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31041995-1bcd-3dfe-a37e-57534cb79056 | -6.14913 | -57.69703 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46ed6f3a-cdbf-3668-8204-2d9c4b2bd047 | -9.43565 | -47.85957 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b7258ac-f4c3-364e-9564-e8fe4ea3b4eb | -11.24767 | -54.15202 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 892eb366-3c00-3867-969e-e59a4f5936ca | -6.1035 | -55.66588 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 24209616-d120-3095-bd71-c0601a8f6ec5 | -10.54466 | -51.30506 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4369c614-207b-379e-bf5e-fc596fdd6ba1 | -11.25816 | -54.13075 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f612473-eb66-34a2-8333-3ee98672a60b | -10.67682 | -54.16558 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 01fceba6-b636-3df5-8955-9feaad8f0c7b | -6.07643 | -57.86544 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 606df7db-fa34-3d87-b38f-e83549c16550 | -4.13385 | -54.02339 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45580f28-a850-309f-8594-f6ceebcf4680 | -10.68149 | -54.15863 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 31.2 |
| a7a75f6e-c271-37f4-ab56-0190baad2472 | -9.44424 | -47.87993 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4eca3d8c-c09f-3c21-a334-49bea0dff7a1 | -6.08171 | -57.86166 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1eca29fb-bc54-3704-86b2-826e2e97aafd | -4.39089 | -55.20561 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README46.md)
