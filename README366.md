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

## Dados Diários - Página 366

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d846fb08-a560-3cd2-86ff-a466b928b262 | -6.64278 | -52.95434 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3a46548b-fd0b-35e2-9d97-431bef5570ee | -6.66765 | -58.86429 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 98443e44-059f-347a-a7d1-ad6261742e9b | -6.23465 | -52.84379 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5cf54796-6b23-3145-bbaf-d5ec501e2471 | -2.04239 | -46.31994 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07ffffd5-32fa-3cd0-ab0f-d9bd98dc4e5c | -3.28615 | -45.15398 | 2026-10-08 16:39:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| effcaddf-2925-341b-8b13-07aa01066a11 | -4.69058 | -42.92669 | 2026-10-08 16:39:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a1662b0-d4bf-3003-8106-76cc816365aa | -6.83779 | -59.29741 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 51189312-a83f-3610-8e1c-97f7389299ae | -6.14014 | -47.95676 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7d143c0-6644-36da-82f9-6376b429f253 | -6.45327 | -52.70439 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| b65a05f8-f02a-303e-8322-7d076df34df6 | -6.15646 | -52.64924 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 897e8e80-03b8-38b6-b8e0-fec46308069c | -1.38079 | -55.40439 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21278e6a-4ef1-3312-925c-2aaa0c266ee7 | -1.3994 | -53.2306 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| bc7dec68-90d3-3855-b012-c10e82c540c0 | -3.58731 | -54.69157 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 04d1342f-2fa7-3b65-ad01-131ba53deb39 | -5.67647 | -46.35867 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1d6266b-1dc1-31c9-ada6-974988ed914b | -3.00621 | -54.05901 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 33f2bd5d-e8d8-3d1b-97e3-18308f84ba9a | -3.5972 | -44.35034 | 2026-10-08 16:39:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b11401b4-d229-3d9e-a7dd-50641550c289 | -7.23544 | -55.12397 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 110c3fa3-fed1-3940-9555-765f09be4c30 | -5.88604 | -52.50679 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6b6c70c4-9817-3467-8aae-1072f619f269 | -4.67005 | -56.21855 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0ae1a217-5455-3d0f-b047-a09945058eb4 | -3.30278 | -54.05252 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| d6c54a87-8310-3358-89dc-f18f69b3a292 | -5.28799 | -48.1072 | 2026-10-08 16:39:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| aac6bca0-0d79-31db-a85b-b6dcebe1a8c2 | -5.43485 | -46.64509 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 2d6a0fa1-53d3-3891-b46c-b855e5e7b85b | -3.16827 | -50.44884 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 03627543-c9a0-3141-bd71-1af8765cd8dc | -1.77226 | -55.02157 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7fc92fa3-5814-3ef8-97f7-0b67dd06103a | -4.92167 | -40.3667 | 2026-10-08 16:39:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 0435b3e8-bf46-397f-8574-de9c05511814 | -5.31675 | -43.65126 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bcc2cba1-81a8-35fe-ba9b-09c4e56d715a | -3.4915 | -59.37709 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 50d991df-ef26-3bad-aa25-3ab0ef61a53d | -2.98459 | -54.11647 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 095c84d2-41d7-338b-9e5a-19ff3cdd0ae1 | -3.02607 | -42.92817 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 44ca746c-fa14-36f4-a367-76469d7da3c1 | -3.6823 | -44.80933 | 2026-10-08 16:39:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c03c8bb2-ecf6-34d0-9bca-889a0e54de56 | -2.45208 | -46.02429 | 2026-10-08 16:39:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6428015-102f-3617-9d18-9f377f72c540 | -3.65395 | -59.15411 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7c99e8d3-b0e2-3906-b48f-24e5becffb49 | -3.25596 | -43.59075 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 57a9b1c5-7b83-347a-985d-24b9982cd2a9 | -3.04388 | -54.15199 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4f8b8392-3ff9-3ccf-803a-4199f1d434fd | -3.76125 | -58.9926 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1ad5a93b-0600-3109-952c-5b45f87ef0ef | -4.06624 | -38.21833 | 2026-10-08 16:39:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 104bdb60-8a73-363f-bac8-5b39fbf9897d | -4.93754 | -42.80795 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 70df5d84-b8a0-316a-817e-b1dfee875f2b | -3.00228 | -43.2811 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87f9628e-9651-3260-bad8-6153cfc38098 | -0.60615 | -56.81158 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7d66a138-2411-3dba-9cbb-18967430776a | -1.54369 | -54.8215 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| e4ca452c-5dc9-36a3-a040-f86b3ba0bd47 | -2.56675 | -56.15302 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f550fa41-055d-3ae6-9a90-947d261de4f1 | -0.5752 | -52.22349 | 2026-10-08 16:39:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 63c705f6-3f91-3dbc-bfd9-263d2dcec9d1 | -2.78152 | -56.50769 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5ce07833-9c9a-3c0f-9bed-4ef81c821a2b | -1.30189 | -55.96755 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 10178a8c-65e4-3f74-ace8-f90bd1ed4358 | -3.30559 | -53.69706 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 6ed5cf6d-d953-38e7-9ead-d45888117381 | -1.53189 | -54.54694 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5d2d3646-df13-3469-809c-5dfa8e6562ea | -1.52321 | -54.52193 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 99178441-0bd6-3d42-9707-feec5f4c3392 | -4.94359 | -42.72721 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8f1b3605-4413-3d16-a065-8b08896747b8 | -5.29969 | -45.71505 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4dac4fbe-60a7-3466-a018-1385ad524d30 | -3.13721 | -42.67266 | 2026-10-08 16:39:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dcf878a9-cd76-3afb-8d3c-c468c94db7c2 | -3.01895 | -54.04689 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 384cf747-266e-3c1a-87d3-e6630f3b34fb | -3.31378 | -54.70716 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f5b8246e-ed58-32e9-a09b-8fbafad32149 | -2.98914 | -54.90338 | 2026-10-08 16:39:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 196ef4f8-e247-3331-a5e1-37d93be56577 | -1.32347 | -55.43585 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e1a25561-a0c5-3d67-82dc-1e3a09598b69 | -3.18228 | -58.83551 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 351d4ae3-7c41-359b-a75a-cba6fe8ac6c8 | -5.37845 | -45.93965 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 52e01708-ed3f-3b91-8dff-0869aa15f0ad | -2.26525 | -56.59587 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fe0ccd40-b5a8-3152-8e1b-75c275410903 | -2.92357 | -58.52763 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4ce92674-db41-3057-a72c-db67e5136e98 | -2.79538 | -57.61729 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07b873b6-6ded-3a42-b2a8-fefb43cf3e37 | -3.76954 | -44.3582 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 17701a6a-487a-39d3-add6-f8b9d156ea60 | -6.04253 | -53.49116 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b7703127-a210-3c5e-bf40-b474a2511aa7 | -4.00275 | -46.93472 | 2026-10-08 16:39:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b3a4e542-c48d-3237-9f28-91f099bdc4d4 | -1.52336 | -54.81871 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 316311cc-9d5e-3396-abf9-7db32a99ff10 | -3.17188 | -43.98303 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6aa8e39d-ee28-3069-b80a-9107da7ff9c8 | -3.79277 | -41.64999 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 67ded44e-e9a1-37c6-aa76-daad882664fb | -3.34467 | -42.49118 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c71d6092-7464-39c5-983c-4eca8a1a1df7 | -1.75367 | -56.19007 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 145880c8-cda4-31a5-bc06-6ef5b6636e11 | -5.87019 | -45.96061 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7a34ff82-c1b2-383e-942d-e69d226ccc43 | -2.73402 | -54.10727 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 55bd0dfc-eab2-3098-b4c5-3f2c83353c73 | -1.32856 | -55.43529 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dd4d4742-7b4f-3998-9dcd-8e8d5d588d62 | -3.43635 | -59.53943 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fb9cc18f-c693-38f8-8661-f178fe564b8c | -2.06497 | -46.55665 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89255da5-bf79-3f46-9884-08e83e77c3d2 | -0.09481 | -49.48384 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f3864b0d-9dff-32e6-9ec7-1f7b72c5322d | -3.55345 | -44.56888 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d54606aa-989a-3d1a-9478-afb23e22ad40 | -3.37077 | -53.53441 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 399088ab-f5c9-3b5f-ab38-5b8ca4ae23ba | -3.7955 | -41.66716 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c8a4da93-00bf-3b78-b80d-c98c6f7053f5 | -5.94685 | -45.37638 | 2026-10-08 16:39:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f39127c6-0dad-3d5d-a7d2-ce3f79d79fa6 | -1.54842 | -52.75276 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f0f60750-4dcb-37f3-99d8-a9657a9b7bda | -5.87402 | -45.96356 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| a952a3f1-f83b-3d25-9ff1-1f400438eb14 | -3.0086 | -54.05095 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 98a9b1c9-1b61-3c5a-b1d2-094e7df70219 | -5.26467 | -47.90365 | 2026-10-08 16:39:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| c464583b-4c29-3cab-9cbb-34721b9bb769 | -6.12387 | -52.72539 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ae76f231-305d-3242-8df3-64c24a74784f | -2.56924 | -56.17023 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 945ed95b-c5f3-32fc-83e8-0f3aea6ab369 | -3.78987 | -41.65748 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| b00c2a4b-8a4c-305b-b152-933820dc7642 | -1.33699 | -52.44619 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 820ed3c6-3f2e-36af-9411-6a2f578c1253 | -3.06205 | -54.37947 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ebfa5a4c-4cea-35a4-b057-4e7760c29c09 | -2.94055 | -54.18028 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c879c5ce-f50f-3fa0-b250-0fb0911d43ba | -6.66796 | -58.85672 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 56edd2fe-f8b0-341a-98d8-94c02f3c0a5f | -3.26487 | -41.63281 | 2026-10-08 16:39:00 | NOAA-20 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e9ae4988-e158-3961-8152-0d4b7470ddd0 | -4.08075 | -44.10407 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| bd58d1f2-ca20-35cf-b7c7-136d03bdf482 | -1.7118 | -55.43719 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b8ca580-e7d3-3489-ac5d-0f98bb974066 | -3.71255 | -59.64305 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8797e1fa-1633-36d3-9b1f-045ed5c33c0a | -3.51666 | -54.5297 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 11e7878f-886b-36cf-bbc6-145f429de78e | -5.3698 | -45.72875 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bddb8ad-b073-30b4-8865-4759d3b74547 | -2.47874 | -56.09528 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 27aec352-1650-34e8-8791-e0be3ec6fdd4 | -6.45058 | -52.65347 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c69dd38b-cf97-3326-9a67-4a09fe3a66d3 | -3.48149 | -44.39537 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bd144ff6-eddd-37a1-acf8-dbc4e8e39f8f | -6.20194 | -51.43315 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 0cd82151-9018-3e59-b9aa-8ab54ad99c9a | -1.42007 | -55.19355 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6d30c62e-c0ea-3d3d-a81e-020e128eba6a | -3.26291 | -58.2073 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README367.md)
