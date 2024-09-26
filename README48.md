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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 739cac71-558f-3ae4-abac-1477cd69be63 | -12.5026 | -48.9198 | 2024-09-26 02:56:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| eab2c602-76ab-33bb-ae38-16ec90385f4b | -12.841 | -62.7067 | 2024-09-26 02:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 6639d75a-4a39-3800-aba0-47e86e0a9dad | -12.8411 | -62.6874 | 2024-09-26 02:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d83e2192-6b3f-34bd-a83a-3ab16bfd521f | -12.8599 | -62.7056 | 2024-09-26 02:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6b1f0475-6696-3325-8eca-d3d0a3389881 | -12.8601 | -62.6863 | 2024-09-26 02:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a976100d-67ea-36d8-87a1-667c2f81d7e0 | -13.4993 | -61.2698 | 2024-09-26 02:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9c5c2025-2e18-365c-a6ce-528dc72c427b | -14.863 | -51.5019 | 2024-09-26 02:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| a768da78-80b7-3010-b51f-a57bd27a1681 | -14.8824 | -51.4992 | 2024-09-26 02:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 4f8dd33c-ed09-35d2-bdca-ff46db1b1370 | -15.3368 | -58.1852 | 2024-09-26 02:56:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9b5d4214-efbc-3283-a39b-ab6a2ebe38a2 | -15.3371 | -58.1651 | 2024-09-26 02:56:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| e7929a08-88cb-3256-bd30-cfa18af597fc | -15.3562 | -58.1833 | 2024-09-26 02:56:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d1199d67-abbf-3696-9c25-9230d15a0392 | -15.3564 | -58.1632 | 2024-09-26 02:56:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 88b11608-a7b5-3f5e-8530-1bc9bd934d3b | -16.118 | -51.9867 | 2024-09-26 02:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 4dc2f898-7998-3c1a-b6dd-1ccc1b994ba1 | -16.0985 | -51.9896 | 2024-09-26 02:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6f46a085-a560-38aa-80e8-a8b07d260f38 | -16.098 | -52.0111 | 2024-09-26 02:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b91f8559-ca33-3b68-a65a-a48651537f06 | -16.1176 | -52.0082 | 2024-09-26 02:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| bd79d7f6-666f-31c3-b66f-f13641b0b9a7 | -17.0798 | -56.1529 | 2024-09-26 02:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 91479d54-3a7b-3761-965a-a31b7a963e5f | -17.0995 | -56.1504 | 2024-09-26 02:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| 10ca4c07-154d-3751-af4b-9190d6c8b958 | -20.608 | -51.4986 | 2024-09-26 02:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 206.1 |
| c3529740-7785-3ad6-a671-8798bca0dd32 | -20.6074 | -51.5209 | 2024-09-26 02:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 202.1 |
| d873bcf4-ae4a-3868-a1a6-ba48a9d025fa | -20.6279 | -51.5169 | 2024-09-26 02:57:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.1 |
| 6d5880c6-985e-3d3b-9636-a34712ae4baf | -22.2162 | -47.5603 | 2024-09-26 02:57:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 88d9daab-df4e-3a58-8ba6-837c7ad55cbd | -21.85 | -47.3 | 2024-09-26 03:03:20 | MSG-03 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb13ddbf-9c2f-3174-afb0-25792d34c5f8 | -12.77 | -51.24 | 2024-09-26 03:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e81ddaf9-203e-3971-b0c9-6d6e7d37c5ef | -12.83 | -51.2 | 2024-09-26 03:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 90a4bb68-5ef1-381d-8270-373294319d62 | -12.83 | -51.26 | 2024-09-26 03:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a763d58-33d4-3279-8560-0a9c9a545c07 | -12.8 | -51.19 | 2024-09-26 03:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6363e1db-119c-32bf-82c1-769229fef3ef | -12.8 | -51.25 | 2024-09-26 03:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d076b8c-57d1-3f94-9f29-be941f3602fa | -12.8 | -51.31 | 2024-09-26 03:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a7c957fb-a57e-3900-a8bf-936482e2076a | -12.77 | -51.18 | 2024-09-26 03:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 664423e1-9637-330b-a18d-13e8359a5412 | -11.19 | -54.76 | 2024-09-26 03:04:23 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4af3e30a-820c-36ba-85f8-c1ec4824db09 | -11.19 | -54.82 | 2024-09-26 03:04:23 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6633f52e-f5cd-342b-bbe8-c136d980f6fa | -7.37 | -55.5 | 2024-09-26 03:04:44 | MSG-03 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8930c5-333d-3725-a43c-92b5b2177a25 | -2.6785 | -57.531 | 2024-09-26 03:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 484e8c07-26f4-37e7-b759-79bbc584cefb | -2.6968 | -57.5307 | 2024-09-26 03:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6df8f344-7cd9-3c37-9cea-e8d6c4077d6d | -3.3505 | -53.7775 | 2024-09-26 03:05:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 4308384b-c8c8-36d9-8fac-bd0ab8e2b3a5 | -3.5673 | -50.3794 | 2024-09-26 03:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 61cf2ddd-8853-3e55-aeaf-a88f9964669d | -3.5488 | -50.38 | 2024-09-26 03:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| b692a722-fd66-3896-b635-4c3ed337e55e | -3.9208 | -46.4459 | 2024-09-26 03:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 77663383-0c4e-33e7-b470-1f8b37f934be | -6.8024 | -59.3044 | 2024-09-26 03:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 12a5aeb3-2764-32f2-99ff-f6e788e2cc8c | -6.9306 | -63.1053 | 2024-09-26 03:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6a8087da-976e-31ab-9660-b8caf4613afe | -6.9305 | -63.1241 | 2024-09-26 03:05:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| ba074a1a-e9bb-36a2-a3c6-a17ff0db96d2 | -7.3824 | -55.4924 | 2024-09-26 03:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 190.3 |
| ed6584cc-b519-3195-b630-cd2cc97eb597 | -7.3823 | -55.5124 | 2024-09-26 03:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 352.1 |
| 31cd2c5e-8366-3068-b2e0-41412d355e62 | -7.3821 | -55.5324 | 2024-09-26 03:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| bc601e2d-02b6-305e-baa1-c5011a82e01e | -7.3639 | -55.4935 | 2024-09-26 03:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| ceddda42-7367-35ba-9eb5-1b211f687b6c | -7.3637 | -55.5134 | 2024-09-26 03:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 304.6 |
| d128f37b-6229-31a7-ab56-3c8f36878b8a | -7.3636 | -55.5334 | 2024-09-26 03:05:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| b8e03287-3c76-34a3-a702-f910cbcdf0bb | -7.5705 | -55.1617 | 2024-09-26 03:05:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9b403ed9-4c55-3035-894b-e8e675f5b912 | -7.8341 | -54.724 | 2024-09-26 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 6f15f1ce-9f1b-3553-8eae-1d43328d4da7 | -7.834 | -54.7442 | 2024-09-26 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ac9841e3-b800-3a05-b125-3bd126761f92 | -7.8156 | -54.7252 | 2024-09-26 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 220.5 |
| 882f35dc-5c52-302c-90ed-9252f2a7ae0a | -7.8154 | -54.7453 | 2024-09-26 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 190.9 |
| cb560732-5a72-3ae1-b0e9-6b96f98da10a | -7.797 | -54.7263 | 2024-09-26 03:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 0ebf695e-f1a9-3d7a-83ca-c96bb5d3baa8 | -8.1757 | -61.3946 | 2024-09-26 03:05:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 9be6e8ab-d258-3520-b630-02f83cc3a17a | -8.1394 | -61.2817 | 2024-09-26 03:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6c4577eb-1f6e-3cfa-bdf1-e88cbb2ea392 | -8.3155 | -54.9956 | 2024-09-26 03:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d523c876-dd4e-3edb-ac3d-bba6e8e61147 | -8.3153 | -55.0157 | 2024-09-26 03:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 95474cfb-8eb3-3b26-80f2-0d2f77f9e852 | -9.1046 | -61.1237 | 2024-09-26 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 4376eca8-9a1b-3561-952e-2b06d90f7460 | -9.1035 | -61.2769 | 2024-09-26 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 5347f962-3f68-3b04-b889-623944efc7ab | -9.086 | -61.1245 | 2024-09-26 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 05bc76cc-20b0-3837-81ed-02f43f410283 | -9.0468 | -61.4325 | 2024-09-26 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| ba265912-d335-3568-8caf-268f015b984e | -9.3462 | -51.0704 | 2024-09-26 03:05:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 611f2d3b-8944-3b6d-971c-e4d074b0c8d3 | -9.3459 | -51.0915 | 2024-09-26 03:05:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| a767d2e6-8457-3930-834e-2ccf317d80df | -10.0515 | -53.4432 | 2024-09-26 03:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 59b813cc-aae4-331f-a098-f093748768bd | -10.0513 | -53.4638 | 2024-09-26 03:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ea65b91e-34e1-3583-8aee-dce25d3ccab0 | -10.0327 | -53.4448 | 2024-09-26 03:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b707541c-1ae1-3b9c-a4d2-a8adee943bed | -10.0324 | -53.4654 | 2024-09-26 03:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| f81257eb-1356-3c48-ad20-983a4df2122f | -10.0322 | -53.4859 | 2024-09-26 03:06:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3d968fb6-91bc-3ddf-9a3b-6f3c62e71d46 | -11.222 | -45.536 | 2024-09-26 03:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 2970c33d-1382-36af-8c32-c64311b73fc7 | -11.2788 | -65.2793 | 2024-09-26 03:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 88131784-7d96-3d12-bba7-8157b5374e93 | -11.2786 | -65.2982 | 2024-09-26 03:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 60e1a742-13b8-3b65-b94b-a245c7aca9b4 | -11.26 | -65.2801 | 2024-09-26 03:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 4354c245-e32a-3331-832d-106f49015830 | -11.2599 | -65.299 | 2024-09-26 03:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 08329ee0-d9df-3189-b307-597a4a6fd8ff | -11.2413 | -65.2809 | 2024-09-26 03:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.0 |
| df8d1f1c-2b90-3dc5-b73f-b6f31caa3876 | -11.2412 | -65.2997 | 2024-09-26 03:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 996dd984-a898-3371-a846-7d532e9c475a | -12.2367 | -45.5045 | 2024-09-26 03:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b3fd87cb-4689-3255-b6a9-543d9adbd790 | -12.5467 | -53.494 | 2024-09-26 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 023cbd44-f776-37d2-a71c-438b433d29f7 | -12.5276 | -53.496 | 2024-09-26 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c9e3810a-9875-3c80-a41d-7123b1fac28a | -12.5273 | -53.5168 | 2024-09-26 03:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 2ca7ed07-9ee0-3573-a89b-269a667b56bc | -12.5218 | -48.9173 | 2024-09-26 03:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 745ed4c0-f355-3f1c-a733-c7981e63a678 | -12.5026 | -48.9198 | 2024-09-26 03:06:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| c94df482-3aee-3a6e-9e40-80f47e867972 | -12.841 | -62.7067 | 2024-09-26 03:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ff9f949f-ec14-369e-81af-b2bf8a3bc1de | -14.863 | -51.5019 | 2024-09-26 03:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 1f6b50ee-0e35-3bc7-94dc-1bf9cebef59f | -14.8824 | -51.4992 | 2024-09-26 03:06:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 69247553-d9a1-3404-8180-7ff13f608bc7 | -15.3368 | -58.1852 | 2024-09-26 03:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d7f9924d-3db2-3439-badf-01d5f0d798b1 | -15.3371 | -58.1651 | 2024-09-26 03:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b99eecce-0e8c-347c-bef2-637f812a8cac | -15.3564 | -58.1632 | 2024-09-26 03:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1ad7e964-1b8b-3642-9408-1ce13d194485 | -15.3562 | -58.1833 | 2024-09-26 03:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d2c3b681-9d6d-37bb-905c-778a9f22e139 | -16.118 | -51.9867 | 2024-09-26 03:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 7ee6d437-87af-3beb-aa26-f457ee9f6b08 | -16.1176 | -52.0082 | 2024-09-26 03:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 99ec06a2-27c9-3187-8545-b1a0ccf7aedc | -16.0985 | -51.9896 | 2024-09-26 03:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 0efb228d-4fb2-3793-abf2-1c3126954161 | -16.098 | -52.0111 | 2024-09-26 03:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 73b4f153-a292-3a11-9d1e-00f505bf2f5a | -20.608 | -51.4986 | 2024-09-26 03:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 164.2 |
| a316517c-f2d1-3e0e-b130-2367196ab6ad | -20.6074 | -51.5209 | 2024-09-26 03:07:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 166.4 |
| 3b97dfc5-1a5e-32ca-88d5-224cdee82e68 | -20.6279 | -51.5169 | 2024-09-26 03:07:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| 0b663e20-dd49-3449-8e60-6da346d178dd | -21.8724 | -47.2928 | 2024-09-26 03:07:06 | GOES-16 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 148.2 |
| 8cf6b6e3-8e18-34b9-b19e-dce7dbb287d3 | -21.8516 | -47.2981 | 2024-09-26 03:07:06 | GOES-16 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| 2c17d482-9e39-31a2-b9e1-d512cf650173 | -21.9374 | -48.5688 | 2024-09-26 03:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| f45ec9f1-aafd-3fb1-a0ad-dca7dc046d16 | -22.2162 | -47.5603 | 2024-09-26 03:07:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |


[Clique aqui para ver as próximas entradas](README49.md)
