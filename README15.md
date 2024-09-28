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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb210b36-2ec9-3eaa-a533-973defdd33a7 | -5.71346 | -46.44539 | 2024-09-28 00:26:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 78419367-ba65-30c1-92e3-28860934ed95 | -5.70359 | -46.46412 | 2024-09-28 00:26:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 851d00ab-81a4-3207-8011-1ad0b9809ded | -5.59774 | -46.25929 | 2024-09-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a789c0b5-de8c-3c24-8a50-24bc317f021e | -5.57 | -46.28603 | 2024-09-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| aee5738a-fc2c-387d-9293-dc1523e79ee6 | -5.5642 | -46.28029 | 2024-09-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| b9a40894-efde-3b4a-ad71-4997d8cf2ceb | -5.56219 | -44.20955 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a17b6d8f-e0a7-36d2-92b1-79030782bc76 | -5.55236 | -44.68255 | 2024-09-28 00:26:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 873b606a-bf71-3eba-9a43-f4e3f78a9f31 | -5.55068 | -44.6698 | 2024-09-28 00:26:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 09adffb2-696e-348d-8ca9-d8fc76401c88 | -5.54494 | -44.67693 | 2024-09-28 00:26:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6c55a343-08a8-30fe-a4d7-351294ce2240 | -5.39653 | -44.65172 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 908c02e9-4ea5-3b55-9670-10e8db22bd8d | -5.39485 | -44.63918 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f3fece74-68cb-3904-9b7d-7a2de969fbbc | -5.38806 | -45.36087 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4465cb33-231b-3647-a0d7-a4a214fafb88 | -5.32779 | -47.70515 | 2024-09-28 00:26:00 | TERRA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a7bf9074-7de7-3aca-93f0-560b8688e597 | -5.2558 | -44.73413 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cef6a0c3-4c4f-38df-916c-dcba1d46bcf9 | -5.2541 | -44.72167 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8b2a3978-6b3f-32fd-bbde-8b52bcddc820 | -5.25082 | -44.62034 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0c3b30a4-ea49-381c-adb4-b5f43b28ff8b | -5.22208 | -44.48724 | 2024-09-28 00:26:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| db1e17cf-8931-3981-b38b-3fae3d6b4d64 | -5.2212 | -48.18618 | 2024-09-28 00:26:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4a0f152a-e527-32eb-b84c-5b9af5b97eb4 | -5.20319 | -44.94341 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0b7de119-66e0-3c4e-ade7-da37b8ff2538 | -5.19436 | -44.95794 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ae941e81-9858-3b58-929c-ee6a3b13ea67 | -5.19259 | -44.94494 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4cf42dae-2257-3fd1-9564-27fea32f171a | -5.19083 | -44.93204 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b1b598ca-7057-3236-9c56-6094d42def3b | -5.11625 | -45.99288 | 2024-09-28 00:26:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| be5eecc9-fced-39bb-85ed-95feac3e97e0 | -5.09591 | -45.83972 | 2024-09-28 00:26:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 5f2da036-ad29-3ab3-b191-045b25c0fd10 | -5.09393 | -45.82485 | 2024-09-28 00:26:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fa38747c-50c9-32f0-b780-7be3a5ccb99f | -4.99049 | -45.40165 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 0e6b6577-9eb7-3cd8-8636-a21635937fcd | -4.97951 | -45.40303 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9b32c18f-deb3-30ff-b13c-b2b79bb266c8 | -4.93632 | -45.67696 | 2024-09-28 00:26:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2261763a-4930-3b8c-b5bb-16b5a601a964 | -4.9362 | -45.67082 | 2024-09-28 00:26:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 8026d38d-2502-392f-bbc1-3a7076f5350a | -4.79183 | -45.26652 | 2024-09-28 00:26:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8a7c3837-a7af-3cff-9726-c2de47894b9e | -4.78901 | -45.27249 | 2024-09-28 00:26:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c8640625-e481-3313-8049-f8f7e92a04a7 | -4.5892 | -48.03093 | 2024-09-28 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| fb75a62c-ca15-3e70-9d0f-f07e3fc3de7e | -4.58617 | -48.00833 | 2024-09-28 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| ac071303-c047-34e4-95ac-11806824591f | -4.57569 | -48.03262 | 2024-09-28 00:26:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 36b367c0-ffdf-37f9-83e0-2f96e69724bb | -4.55539 | -46.41943 | 2024-09-28 00:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c1003317-c750-3f3c-98a4-31ddaba875c3 | -4.55318 | -46.40309 | 2024-09-28 00:26:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5ebdf50f-c3f6-325f-85a4-ba304a2be7f3 | -4.40484 | -50.70529 | 2024-09-28 00:26:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| eea5444c-35a9-3b7d-8f02-69a857f122f2 | -4.13418 | -46.69455 | 2024-09-28 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 52202dce-c455-3bd0-b222-cd1266f8e968 | -3.91945 | -46.46471 | 2024-09-28 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 37742ff3-7760-3c58-8935-ffb198bda58b | -3.9172 | -46.44823 | 2024-09-28 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 32d09a33-8bab-3b2a-bf67-3249e7e91fbd | -3.90768 | -46.46602 | 2024-09-28 00:26:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 80063f3b-5715-3660-81c4-411346fcf934 | -3.69577 | -47.60948 | 2024-09-28 00:26:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 9d75d911-d8ca-3ed3-8bae-3b419d6ae6e7 | -3.57678 | -50.55395 | 2024-09-28 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| eb896eea-2be5-30cb-ac45-568fa96cead8 | -3.57254 | -50.58184 | 2024-09-28 00:26:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 65e62c35-7e2d-3a3c-b574-9bfa9dcde3be | -3.1999 | -50.45823 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1d7d53ee-bf47-3c67-b53c-6852f59c5c10 | -3.19535 | -50.42513 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 49e89c9d-d300-31f7-85a8-95ab43c089aa | -3.19261 | -50.45256 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c6f7d374-6ef8-3836-92d4-3767986c8658 | -3.18831 | -50.41931 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| bcc68347-1832-3b4f-aa53-1357f3d1986a | -3.0922 | -50.5057 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 494157e6-f7db-3f94-92ab-36935bbcf578 | -3.08799 | -50.47293 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 2d3837fb-d933-3c46-a277-40b6e9bc3110 | -3.08359 | -50.51204 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 66ddd814-75ae-33a7-844c-dfdde3913e7c | -3.07914 | -50.47913 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.9 |
| f2cd2414-d66e-30c3-8d7f-cdd4f4036bdd | -3.01537 | -51.05717 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 62aa23ad-0014-3a27-9243-158561ca6251 | -3.01033 | -51.06307 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| e17aac25-6d06-3039-8d50-1aa50749d352 | -2.8978 | -50.48281 | 2024-09-28 00:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 09ce0a47-3949-3a99-94fb-86b66a7e9e0c | -2.71681 | -46.74081 | 2024-09-28 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 56f9d323-24ee-31ec-a03c-5655427d9e7f | -2.71463 | -46.72454 | 2024-09-28 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ae81a038-2713-32f1-92ed-dd2d74038b0e | -2.63099 | -48.05294 | 2024-09-28 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 5aa2891f-073b-3483-a1c1-96706e543873 | -2.59463 | -46.00026 | 2024-09-28 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 151.6 |
| d3be54e8-bf44-3981-9698-bfe917556313 | -2.59364 | -46.00669 | 2024-09-28 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c9405274-086c-3363-a4ba-ed5ff73bbb37 | -2.59275 | -45.98607 | 2024-09-28 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 249.1 |
| bb8f8178-8427-3f87-bcd2-bc68cde16239 | -2.59164 | -45.99245 | 2024-09-28 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 332.2 |
| e416155c-c232-3b23-b236-87508db55348 | -2.58966 | -45.97834 | 2024-09-28 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 18d0bfea-d8db-38da-8a01-df3db04b16d1 | -2.53251 | -47.23198 | 2024-09-28 00:26:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 6cdb6bc7-f144-3971-810c-d2ca2e7a2bf4 | -2.47623 | -48.06519 | 2024-09-28 00:26:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 5bec9ae8-b7b3-3523-9ae6-d709b2944699 | -2.47341 | -48.04468 | 2024-09-28 00:26:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d5244299-1981-3fd2-b2ef-000be6beeae8 | -2.38091 | -46.53661 | 2024-09-28 00:26:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bf4b0eb7-cf92-3055-8c5f-d163e808f982 | -2.36131 | -47.60139 | 2024-09-28 00:26:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a946fcb4-adda-3d58-93ff-4602fa70f39c | -7.38537 | -44.09713 | 2024-09-28 00:26:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 01e44a78-1331-34a4-ab9c-005c972f15ed | -1.17737 | -46.71936 | 2024-09-28 00:28:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 32e3423d-a28e-3e96-8542-0ac67499fe0a | -1.17526 | -46.70413 | 2024-09-28 00:28:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 6603ab38-ed29-3b4c-b7b3-a18220f1964f | -2.87921 | -51.67252 | 2024-09-28 00:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| a98e99ee-a332-3d54-9b06-b655c42d4f30 | -2.87794 | -51.67717 | 2024-09-28 00:28:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| cae093b5-8068-33a9-b3f2-5d8ca2c44013 | -2.36001 | -47.60699 | 2024-09-28 00:28:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e96b4575-951c-3020-bc3f-6c898d85cd9c | -2.11595 | -47.13697 | 2024-09-28 00:28:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 6684089b-1ea2-3f5c-996f-f336477b68cc | -2.11366 | -47.1199 | 2024-09-28 00:28:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 189.9 |
| 2c1870ae-285f-34d1-90bf-cb7673d825d2 | -2.11091 | -47.14338 | 2024-09-28 00:28:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6c13aa02-5d50-38d9-b1d8-e98d5e3702a6 | -2.10849 | -47.12633 | 2024-09-28 00:28:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 215.8 |
| 4dc603af-99cc-32b2-a95d-6d4f8907127f | -2.10609 | -47.1093 | 2024-09-28 00:28:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 63464353-29f1-3b08-be54-bdb64b5c8b75 | -2.10394 | -47.13874 | 2024-09-28 00:28:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 3089c0b5-b059-3457-a18f-2298ade6827a | -2.10167 | -47.12164 | 2024-09-28 00:28:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 39e66119-bc38-3c22-a9f1-d73f161195ce | -12.67 | -54.71 | 2024-09-28 01:04:14 | MSG-03 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9652af13-0f90-3a43-a58c-1983f6d328da | -12.7 | -54.72 | 2024-09-28 01:04:14 | MSG-03 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a9ef0f7-4a76-304a-bef3-6392e391cefb | -10.66 | -46.0 | 2024-09-28 01:04:25 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0f47269-b363-3c66-9700-9e3b6fbc94c9 | -10.65 | -45.96 | 2024-09-28 01:04:25 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bd7dd2fc-a10b-33a5-ae25-05bcd1a3ee08 | -10.57 | -46.08 | 2024-09-28 01:04:25 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ad5d30c-7a5b-3f12-aeeb-dff6495cca58 | -10.57 | -46.03 | 2024-09-28 01:04:25 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52d2ce2c-294b-3a2c-9773-78d332b02c68 | -10.6 | -46.09 | 2024-09-28 01:04:25 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb1921bc-c5eb-3dbf-9a82-6a7c4911d8af | -7.87 | -44.62 | 2024-09-28 01:04:41 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b07f2090-b3db-3a33-a1ae-4cf80b087333 | -7.87 | -44.58 | 2024-09-28 01:04:41 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f97c7c29-4a40-341d-81f9-eb8b839a069c | -7.9 | -44.63 | 2024-09-28 01:04:41 | MSG-03 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 93445ce7-4733-37ea-81a3-b3676a60beb9 | -22.835899 | -47.031502 | 2024-09-28 01:04:45 | METOP-C | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 96566c58-0cb6-3c37-bd83-b13eb986850b | -21.298 | -41.9146 | 2024-09-28 01:04:48 | METOP-C | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 772d2e64-edc8-3b3a-82fa-b779b913fb98 | -21.302601 | -41.9314 | 2024-09-28 01:04:48 | METOP-C | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8763fb6-f9db-3e3e-b440-593fcfdbab85 | -21.139099 | -42.2495 | 2024-09-28 01:04:52 | METOP-C | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 18795823-19c3-3dd8-b25a-d762d0c6bcfa | -21.129499 | -42.252399 | 2024-09-28 01:04:53 | METOP-C | EUGENÓPOLIS | MINAS GERAIS | Brasil | 3124906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1854835-c376-3fd9-9c25-3b65d6b18a50 | -22.349199 | -47.646198 | 2024-09-28 01:04:55 | METOP-C | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2fa88ecb-259a-3fe3-b552-4151b07a22f1 | -21.040001 | -42.6535 | 2024-09-28 01:04:56 | METOP-C | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a731c93-1d98-3338-a96d-2685b9433ab8 | -21.0303 | -42.656399 | 2024-09-28 01:04:56 | METOP-C | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e06ae444-5649-3bbb-8e58-fd1b01423e0f | -21.0345 | -42.6717 | 2024-09-28 01:04:56 | METOP-C | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README16.md)
