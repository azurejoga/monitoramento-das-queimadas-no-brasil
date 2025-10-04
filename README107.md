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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9f4aca2-6295-3601-af56-384bbdbb8713 | -7.05051 | -42.77446 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ee2318ec-d289-3cca-a34c-414fa4c1e79d | -8.5343 | -47.83189 | 2025-10-04 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17505dcc-537c-3bc0-94df-c8efd27d1839 | -2.89396 | -50.73498 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14f76d24-1ac7-38dd-a6e5-07eb72b7d38b | -2.89469 | -50.73021 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1dc63752-1d39-3184-b647-26c1d54937d0 | -7.76673 | -46.22988 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 114db621-5805-379c-a049-f1c21806f054 | -4.58785 | -47.04009 | 2025-10-04 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 690a98a6-95e7-3bb9-bf88-538157aa7344 | -4.82492 | -42.76952 | 2025-10-04 05:04:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4d4340a7-74e9-32f5-8442-ace263f19cd5 | -9.74983 | -48.90491 | 2025-10-04 05:04:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8c0db67-3b02-337f-afe9-ace41315c89e | -5.61623 | -51.93633 | 2025-10-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5481f261-28b9-3db7-a7a3-e09b2f41e882 | -8.89739 | -45.02219 | 2025-10-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40eb5ee7-b82b-3314-bb3c-08ed6830777c | -8.53995 | -50.15966 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b2b2799-4a15-317f-b41c-6489275e1448 | -8.10979 | -55.08631 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8194aad8-1c16-33bd-a4c8-5a35fb1118ed | -3.41338 | -51.52531 | 2025-10-04 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1027157e-f237-3345-991d-5ec01990ecf6 | -8.04717 | -54.89803 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 986c4b41-8668-3f7e-8538-847f029b3fed | -9.34738 | -45.79775 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61f4a9ac-f336-319d-8ffe-3e9482135f30 | -5.71623 | -44.23964 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 351d66f5-2b81-39ea-91f0-d417d22b144a | -7.05133 | -42.76786 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6a74d611-fdb7-307e-9985-c199d75c72ce | -7.93268 | -55.02303 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fadf15e-a4b5-3fd5-8109-e926a1b03358 | -9.33838 | -45.7747 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2afa3766-2674-34f4-a30e-e0fc77432b38 | -10.77038 | -45.3288 | 2025-10-04 05:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e7ec7d2-f4fd-3eb4-bde6-ed40c4edbc4b | -9.34748 | -54.51901 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc48b7b1-9354-3030-83f0-be87ad85d307 | -6.34268 | -43.4626 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7fea6e1a-6e37-3a69-9ca1-cf6b643056f2 | -4.26361 | -48.5506 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39a9207a-dd54-3b2f-83d8-4283600bd234 | -9.63082 | -54.31302 | 2025-10-04 05:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbb29015-6910-3ea5-b888-f1b0855b891d | -6.94496 | -63.10253 | 2025-10-04 05:04:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63ea491e-a994-304f-8d6a-17f5f3c191d6 | -9.90842 | -43.8012 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecd3b08d-a28e-3961-923c-f844300448d7 | -9.44651 | -50.89748 | 2025-10-04 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ce31079-4d5f-3648-aff9-710e1854ce00 | -8.17576 | -44.13675 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7167617-0c3f-31cf-8afd-abca2b964dca | -7.51439 | -44.27364 | 2025-10-04 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4938304b-e528-3078-b0c5-efb2dbd6a386 | -5.24249 | -45.54754 | 2025-10-04 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e209f3bd-5e57-33ae-bbb7-4ca9b0b174e8 | -9.26008 | -45.77744 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a372b795-12d6-3088-9a8f-d02199a23c87 | -9.32688 | -45.75727 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d946d94-b1b2-3651-9d03-14c5a5adf9e8 | -5.69653 | -42.83941 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1ec1455c-6f0b-3cea-9e97-ee9cc0209df7 | -6.16612 | -44.61636 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f44b5b9-b539-35a0-a94b-db0d7304da13 | -8.02056 | -55.42231 | 2025-10-04 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe11dc30-c171-3c5a-8eae-75aa427a08bb | -6.17609 | -43.92743 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 268e45bd-c9a5-32eb-817e-e5915441999d | -8.6307 | -54.99127 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a924c454-bd39-3321-82ae-0de2fb1f601a | -6.35053 | -43.45904 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c12acd4-5e81-31e2-95e8-312d8c388eb8 | -7.79412 | -42.5657 | 2025-10-04 05:04:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 813fc518-4f71-3de0-a8a2-38b7d227b59c | -5.70204 | -49.3067 | 2025-10-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec36b727-20a8-3626-a86e-20bdaa1d5389 | -7.70037 | -42.57259 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e9b52df2-db92-3e3f-8295-711d22f45af9 | -6.67749 | -44.2038 | 2025-10-04 05:04:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76962a21-03f8-3785-a01f-e43e44d7f037 | -9.08492 | -48.02474 | 2025-10-04 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9d6a32c-5e67-39db-afbf-d44480b032e8 | -8.04772 | -54.89445 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c3ddb8a5-ca64-39c7-9854-805808e2a2b4 | -4.64397 | -43.18228 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e53a5b5-3fa1-32f6-a5cd-b8dc815c1bbd | -7.74506 | -46.30624 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 31abfe7a-5240-3207-974f-f3d2f6b19107 | -2.81464 | -48.61323 | 2025-10-04 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91a93e36-001e-3307-9485-1690be17ed1c | -6.59064 | -44.62776 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f997858-ed88-3c76-853b-c1f08a865004 | -9.28608 | -54.52944 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72c29d2d-aebc-306a-8b96-4d96e35dc394 | -4.95886 | -45.06674 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6e1c90b1-5ad6-344e-a711-586af9c15062 | -7.78289 | -42.59824 | 2025-10-04 05:04:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5768f8c4-0c91-3355-86d1-b222f69d0b42 | -9.34248 | -45.77697 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba2c0d3e-f4b7-38f1-98f2-3b00438b149a | -5.91083 | -49.29446 | 2025-10-04 05:04:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9d51d57-f44d-3b1a-b217-46b139734642 | -8.62283 | -54.97536 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10f5b4f4-f728-377f-ad13-6db7e53a72f3 | -8.7128 | -47.98317 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78918878-8bc6-3fc9-8c02-439de3c20a07 | -5.8732 | -42.51361 | 2025-10-04 05:04:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0fea010d-fd16-391f-bd13-1b96bd5b473c | -10.53765 | -44.52131 | 2025-10-04 05:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d76ad90-b5b8-34e0-8da2-5fe18098c94b | -8.90403 | -46.60107 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8dcfbee0-23fd-3779-bc9b-2f0b37edfff2 | -6.16007 | -44.61522 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6e002d36-d3d9-3330-986e-2e73a0a46abf | -8.54173 | -55.01837 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 035f03cc-9693-3484-a616-d0663f0cbc45 | -6.88342 | -47.23843 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ab9cac3-478c-349c-b2b1-0e3d5446f723 | -6.7156 | -42.80122 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c6d105ab-eb96-3331-a9ea-767979568bbd | -5.71772 | -44.23691 | 2025-10-04 05:04:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52bc5d7d-0982-3d08-89fb-e4336ab51b8f | -4.6206 | -49.54739 | 2025-10-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f6aa30b-66cc-3e17-b82a-9e1c3cfc867f | -6.46578 | -44.57999 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f7061bb7-6ef2-3adc-ad3c-222c3c0b03fa | -5.68903 | -42.84414 | 2025-10-04 05:04:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 57499e1e-f3b4-3594-861c-4938c80b8c16 | -8.6183 | -54.95996 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f3d9f26-0039-3752-84f7-c87a828280dc | -7.93323 | -55.01948 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfd82f4e-0ef8-33ec-9b7e-3f4b2867d224 | -7.74218 | -42.52271 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 83b98503-b2b1-3d79-844d-c75728aa61a7 | -9.94103 | -50.23996 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96f4e9c4-222c-3c37-b031-e83caff91fc5 | -9.27579 | -49.01588 | 2025-10-04 05:04:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c321c554-781d-3d8d-b055-bc3e069d4ca2 | -5.98912 | -43.48369 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3239c315-94ee-3dbe-b6a6-ba7f206db9c3 | -8.05663 | -44.80302 | 2025-10-04 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ae68ce8-9655-361c-bbf4-91a0aae64b25 | -8.84376 | -46.845 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a72a89a0-4778-3b24-9083-526e1d745e96 | -9.32932 | -45.75187 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b8c4559-de13-3ba8-87b6-653acc612065 | -9.34682 | -45.79047 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4e39754-76cf-34a1-aeca-4ddbe895d904 | -6.38281 | -46.51342 | 2025-10-04 05:04:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 190b5c04-6ea0-3527-a002-72e3818f1569 | -6.66366 | -42.82569 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| fdf110d3-f074-3f55-8eca-79cd98d1cd34 | -7.166 | -46.21462 | 2025-10-04 05:04:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03c0fc93-15e7-35fd-8a23-43786fa3d676 | -9.31737 | -54.53051 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbd1e62f-6944-382e-b0d7-3b66a20fec71 | -9.35269 | -45.80293 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8ab6afe-edf0-3e7b-be85-339d592a096a | -8.63125 | -54.98768 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1cf30f81-d60b-3d0e-b245-2e4da406fb49 | -8.64204 | -54.58828 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e3b5683-ca31-3cd4-909e-a8c26497ac5b | -9.94757 | -50.89374 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2828b316-0d19-3e5e-8c75-8fa886ed98b5 | -7.54974 | -42.39583 | 2025-10-04 05:04:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f0e20956-788a-37b1-b403-d79567a9ded4 | -9.33156 | -54.5319 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6abca831-4fe9-3e66-90ab-9884d60c890e | -13.11606 | -47.94186 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c1d0a49d-720b-31be-aed6-f158bf927aba | -14.04592 | -53.92726 | 2025-10-04 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 197dfadd-c236-3326-8deb-2f49c801c389 | -13.35066 | -47.2154 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0a6e800-15d9-3ce3-aa4c-97dd2ca4d710 | -10.29861 | -50.28492 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce21da3f-4ae8-3753-8c1c-d926e721b5c9 | -11.47843 | -45.02252 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 376080bc-344d-3725-b0c5-b82e004de2ae | -11.92354 | -46.37173 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4fb7b57f-d883-343a-bf85-4d146ece9dd8 | -13.33687 | -47.57962 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 421dca9b-1039-3cde-bea2-96328756ff5f | -11.83788 | -44.93443 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be20aa3b-5726-36dc-80b2-60c828505614 | -14.64842 | -48.30825 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4ef0071-5b6b-3873-9943-764a41109609 | -10.57899 | -48.70016 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25338aa1-490f-38d0-88e1-ca24d1930837 | -11.50058 | -43.50089 | 2025-10-04 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49e59e3b-7c54-3870-ab71-ef3f4de4ef29 | -11.7879 | -46.82658 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f26d24f-3b7e-3e76-88d4-be21fa592885 | -11.92047 | -46.40467 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4af138b2-74e8-3ff9-af76-20547b20880e | -15.59044 | -52.4596 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README108.md)
