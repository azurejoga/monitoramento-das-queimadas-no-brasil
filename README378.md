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

## Dados Diários - Página 378

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d61bc53f-d38c-303d-9f79-cc3e4d6f31d8 | -3.77994 | -44.60555 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 65918c46-fced-3b1d-8b83-2c561d821cfb | -3.25593 | -43.87279 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c226fb55-71c3-39b6-a4f1-77d5cb0d0df7 | -2.0885 | -46.57776 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| ddade16b-075d-3008-b9df-75c552f176ef | -5.40953 | -45.63401 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7248d614-cc2c-31db-b0b8-05c11082a88f | -5.41803 | -45.86648 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 459e3ac2-97ee-3dc4-aa16-8201b31fde24 | -5.30698 | -45.6962 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7ea93680-5be0-3a46-844e-485a72eb3a28 | -3.47148 | -44.30738 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ed2a40c1-c012-316b-9de1-0b91dc4e935d | -3.45436 | -60.24725 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4d040d5d-f319-30ec-9d8d-cd3667e4c073 | -4.37048 | -55.3197 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 99778217-8057-3a15-88cd-793d2bc6ff53 | -2.6407 | -56.54094 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccb23a24-91f6-39ea-8492-c698f4e580e6 | -2.08084 | -46.57187 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| c96d825b-d769-3b09-8e41-a08521544f8f | -1.47961 | -53.61496 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 26467758-dfa0-3999-be7d-dd274ac24fbc | -4.75821 | -55.65809 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7794d0c-1ffe-3f81-abab-384c000a737e | -2.99898 | -54.08324 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 9df50eb1-20d0-3bfd-b48e-48fb0cb61e5b | -3.31427 | -58.22411 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3541630e-e59c-318f-b2a1-1f2735791a09 | -1.19982 | -54.21003 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 57b16979-b54a-3ed5-b0d8-7a30440aea52 | -3.73694 | -55.38795 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ac735f7c-8eeb-3064-ab92-be251b6d552f | -4.89162 | -49.04412 | 2026-10-08 16:39:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 56db68a8-e007-3f90-b6ed-4542666a7ef7 | -3.22582 | -53.88988 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1282f98f-e7fc-3041-98ad-1af25a49cfb8 | -2.0575 | -54.30199 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 12635d77-274f-3c99-a848-ea2b2b93c772 | -2.40033 | -49.59111 | 2026-10-08 16:39:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bb664050-c004-335e-81e9-b948c2c00d07 | -2.22383 | -60.07322 | 2026-10-08 16:39:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e100c48e-7c23-3623-ba81-1ecb5b585136 | -1.05399 | -53.59494 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 86229dba-9f87-32f6-9378-019336b3afcd | -3.51812 | -58.02865 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ae686d24-c172-3f7f-aff9-3fd48a55fee3 | -5.74491 | -53.4549 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5a1400d9-05b6-3db0-8dbf-68c789f36a39 | -5.40862 | -45.69449 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| addc81d2-831e-39e2-8ce6-c89b482f5f5b | -6.11383 | -53.50917 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e3ce9095-2eff-3454-86d7-7f3f43cd7512 | -3.37172 | -56.96811 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c83989f7-62a9-38f8-9f0d-073487daabf5 | -6.15401 | -52.64748 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 9d51e1ce-59b4-3704-b420-49d49fed0e45 | -3.4637 | -39.50764 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 73f3ff0d-58cc-31e9-ba7a-586e4704b702 | -5.62656 | -43.04476 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ecc4a5d5-253c-3ddf-a421-5559a69366fd | -3.03821 | -57.48516 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4139c7da-c710-3c65-8574-a0200d6ffe96 | -7.23188 | -55.09683 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3e8be0c0-620b-358b-b28f-d5f4a239d504 | -3.17135 | -50.44394 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 332e3d4d-d69b-34f5-80c2-a8b27209f2d5 | -6.15585 | -52.64482 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| c7215e0d-d491-3491-a080-850623e6ccc4 | -4.14222 | -43.19956 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9838eaf7-501e-3fbc-9f48-e52fefe9686b | -3.29052 | -54.00264 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| e28cb2fc-1df3-3843-a281-1f53de18fcc1 | -3.4551 | -39.45409 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 13.0 |
| d18c9e4f-1685-33bf-9cc5-be709abca9a0 | -2.74097 | -54.12168 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 197.5 |
| 4f8e09e6-31fa-3819-aa9e-3b8518c98c2b | -5.2858 | -42.73797 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 5e2c476e-8dca-3789-87b7-4c5a5c0b1dcf | -3.01422 | -54.04757 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 6becc3c2-bb24-39dc-83d4-aac2d7f91d12 | -2.73367 | -44.3258 | 2026-10-08 16:39:00 | NOAA-20 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 169b8d19-ca02-371d-89c5-c3c488bf1037 | -6.09664 | -53.49081 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4f837e77-d772-32b1-b944-b0eb3eb4c4e8 | -4.47901 | -49.66737 | 2026-10-08 16:39:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4b9f8db0-3a13-35aa-828d-11ec35d18892 | -6.31934 | -53.30583 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e09d177b-b093-35e1-a8db-b6ded8b0564f | -1.82971 | -55.09133 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79fbe8b0-0204-3eea-a612-cc7a788cec60 | -6.07407 | -59.88273 | 2026-10-08 16:39:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8d5e2df8-68c2-3dc0-bd47-7e54b3f7b590 | -4.90755 | -42.47509 | 2026-10-08 16:39:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 929c1009-1da4-3fb2-acd7-6f20e3235334 | -5.63846 | -45.79923 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cb4ab043-93c1-3a4a-86f6-48d2b4345e25 | -3.73103 | -39.53645 | 2026-10-08 16:39:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| fec9f208-c247-31ec-b58b-300bd4142eee | -5.89105 | -44.12309 | 2026-10-08 16:39:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2369742d-c4e7-3f46-9686-4c2c548357a2 | -4.06009 | -55.32338 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 799845c3-39c0-3ec1-bc9b-d5709882738a | -3.77436 | -52.62453 | 2026-10-08 16:39:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 0dd17023-a928-313b-b4c5-2d89a5ef39fc | -7.61189 | -55.71489 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e3631a3b-4c4e-3aba-bf23-34d830b94425 | -3.07391 | -53.96214 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 6a101b92-e7df-3033-877a-e9349a38ee45 | -5.61155 | -43.08908 | 2026-10-08 16:39:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| e8f6bb13-ed6b-3af4-93e4-1710a99c5e0b | -3.00365 | -51.12409 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f642cc40-5ad3-352c-81db-d2ccc6e6279c | -3.30749 | -44.65271 | 2026-10-08 16:39:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d470e460-c76e-371b-beba-3825d0dcdf5c | -5.10282 | -46.202 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8c173045-eb8f-33c7-a651-59c232294df4 | -3.27473 | -44.19957 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 509c2bb6-bfbe-322c-b8e7-df3ad5646a8a | -2.05507 | -54.31783 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 41e95d8f-d743-3619-90ef-bb2d19bbe94f | -1.33276 | -55.42878 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 861c3445-ed38-3e9b-8d1c-102c3bfbc868 | -4.12527 | -38.35743 | 2026-10-08 16:39:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 27de09d1-7ddc-3fe8-9ede-18142f58d865 | -2.92299 | -54.1337 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff6044a4-dffa-3e08-80de-83fe2032a5bf | -5.79343 | -43.75167 | 2026-10-08 16:39:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b3cf0102-6423-32ba-9c26-7059a250e6ad | -5.17643 | -48.96643 | 2026-10-08 16:39:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 66338526-cfec-377c-9ae1-88491a4a7d1f | -5.47451 | -41.21887 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f2b8d67c-3ab3-3d83-888d-0f1802547773 | -2.52207 | -57.24379 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 86143aee-c8c9-3336-8c1e-122fd93e77d9 | -6.14042 | -53.07212 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 54eec495-108b-35a4-8fb6-83c344958f09 | -4.66225 | -55.92659 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b49df9c8-4d7c-3bc3-911f-232321ec146c | -3.27823 | -44.19903 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7464f6cc-a4c8-34d8-adba-c3a3f05cd082 | -5.6989 | -53.47908 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ff1eacd9-c6d8-3219-b87b-ca10ef30f8c5 | -6.84403 | -59.30138 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e52b0a1d-2db1-3972-88bb-3007b602af27 | -2.7903 | -57.64267 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6c13c5d6-6f58-3d2a-b3a8-6ee40cd64bcc | -3.55857 | -44.55664 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8fde3876-4ad0-37d6-b1cf-5dc3e84877b5 | -3.50487 | -59.32634 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 99fbbf24-c596-30d2-8806-ad93ca73254a | -3.70936 | -57.21738 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ded9661a-ea7a-387e-ad3b-55960885b607 | -3.77946 | -59.19267 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ecc4767-601a-3acb-8c7c-77e98bac2e01 | -3.83743 | -55.98162 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d304b908-3239-376f-9a44-d0dc37910bfc | -5.2388 | -56.11404 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bc81e9cf-464b-370d-8ea2-c46d4e926630 | -3.96954 | -51.86595 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4888198a-428b-3da1-8a5e-c2026a4c2be5 | -3.33126 | -42.92136 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 112cec08-d7a5-3908-bf97-dee43820aa3c | -2.46525 | -46.44385 | 2026-10-08 16:39:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d9736568-f062-324b-9e68-fba9bc8085db | -2.47284 | -56.09264 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 99b3cdf5-e403-3b34-aee6-95c4e4c0069c | -1.72108 | -55.44948 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f70a178-68fb-3597-986f-e53e8a57367d | -2.83271 | -58.35 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71015063-dea2-3093-90d8-12dc85025004 | -3.4747 | -59.50293 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9ea76717-4b94-37c6-aa28-e88afd8c9bb2 | -5.23553 | -56.11435 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ece5f484-640d-3efc-9714-4fffaba5e638 | -3.44398 | -56.93679 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 957bcf98-3aa3-3bc2-933c-4760dd26632d | -7.22745 | -55.15894 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 90f64fc0-4f9f-3f38-9300-3dee7bc68cfb | -2.73299 | -57.4637 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f6a61adb-521d-3b12-a559-e9c5eec24113 | -5.52026 | -45.6264 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d3fb42f5-6de6-3fa3-bed6-b9510fa53db7 | -5.46028 | -45.58936 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 190d35a5-11bb-3ffc-bd07-675c1ab0741c | -3.29782 | -54.08453 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6c87f27c-9e77-3c02-bdec-21467374ac32 | -1.40722 | -55.41492 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50c9489-ab3d-372d-b0da-bbe333d3e5bc | -3.05788 | -53.91902 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| b4c9809d-c3d9-3dd8-b99f-b403bce992d6 | -4.31727 | -41.22824 | 2026-10-08 16:39:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 609df2da-a693-36ad-a4ae-8608391d82a7 | -2.26422 | -49.81181 | 2026-10-08 16:39:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 250eea98-6895-307f-8bcd-21291fa8f994 | -6.21111 | -53.54192 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ff18fe1b-4988-3e9e-92af-bf300145b597 | -3.17924 | -50.54821 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README379.md)
