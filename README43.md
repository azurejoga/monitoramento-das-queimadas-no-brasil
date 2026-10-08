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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cfbf8e9-8a0d-3227-82b3-24fda1b97924 | -7.4443 | -63.5401 | 2026-10-08 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9513d129-ce34-3386-8bd4-649589c37d5e | -3.1792 | -50.4551 | 2026-10-08 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 9cc89683-72f5-33cf-8bba-14d82b91b341 | -3.0191 | -53.9071 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8f8f0d58-f879-351c-918a-d2792d258b5f | -2.7612 | -54.1142 | 2026-10-08 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| ef0acccb-5c77-3a81-9034-d9e680931fce | -10.6717 | -51.976 | 2026-10-08 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| aae3e510-8754-3e37-86a0-dccfcb879909 | -8.0895 | -55.311 | 2026-10-08 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 3196f95d-9849-3515-93b9-c5bd0d71d8e8 | -5.6932 | -53.487 | 2026-10-08 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 277.5 |
| 76d62eae-80de-3f89-ac29-19cc40d8dbdb | -3.0913 | -54.287 | 2026-10-08 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 87b1512c-f4bc-3878-be27-0685247ee9d9 | -3.1972 | -50.5592 | 2026-10-08 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 6a18338b-ad17-3346-b38a-9804586715fb | -3.1115 | -53.7637 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 4979c0ae-ba39-3e27-afce-7f12cc026199 | -8.3882 | -46.3006 | 2026-10-08 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 05499441-88ba-3fbd-9bde-b26a1950f726 | -8.7228 | -45.1812 | 2026-10-08 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 282.2 |
| 1322c03e-d6e5-3c03-a493-a4146a29db77 | -2.7797 | -54.0736 | 2026-10-08 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e48dcc7e-0803-3729-b801-891d1af42821 | -2.1629 | -59.217 | 2026-10-08 01:00:00 | GOES-19 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| d1cf6bef-a752-30a4-b99e-e4a4d96fbde9 | 1.6937 | -55.6263 | 2026-10-08 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 1ab24b74-cbba-3d42-9348-51cfbab0a00f | -3.5515 | -59.4807 | 2026-10-08 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c705b044-e309-34db-b997-d2d43b5c41b1 | -3.2199 | -54.3038 | 2026-10-08 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2bfe5324-b05d-3bd9-81ab-ba11d8a0ce5d | -2.499 | -56.0675 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cb59aac4-7831-369f-9147-98fb8ff9756c | -2.572 | -56.1842 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 1c23ecc7-b36f-36eb-b28f-b25940a9ada9 | -8.537 | -66.9764 | 2026-10-08 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 3b7860ac-d4ba-3de9-aca6-1f108ced55d1 | -3.0373 | -53.9469 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 2257f59a-8dd3-38ac-a19c-fa2e57e46297 | -4.2954 | -49.0807 | 2026-10-08 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d9762c6f-5a4e-397d-a8cf-e2e48453c6b8 | -2.4987 | -56.1659 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 96c6dad4-07ec-3166-ac7a-179682e0eb2f | -3.8567 | -55.9769 | 2026-10-08 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 1b107d7b-8b66-3c0d-87ec-cc491da13f63 | -3.1973 | -50.5382 | 2026-10-08 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| ff3a2895-0177-360d-847e-c8be31b406ea | -3.478 | -59.597 | 2026-10-08 01:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4a2afcb7-b244-3e53-ab28-2ed3144e2021 | -2.8575 | -59.1107 | 2026-10-08 01:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| bc372d45-7247-32a9-a426-79ca80a3d34a | -5.7117 | -53.4862 | 2026-10-08 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 299.5 |
| 594ffa71-651f-3b0e-8bf8-9a0292071146 | -3.019 | -53.9473 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e13aa13b-6535-375c-b064-dc41edfc6d03 | -6.2343 | -52.848 | 2026-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| b0fcf015-639d-32b5-b49a-03fa6512d6d0 | -1.3934 | -48.9321 | 2026-10-08 01:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| c5c5b48f-ed60-3aa8-90b3-063ac7207ba0 | -2.4988 | -56.1462 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f5d992c7-aac9-31d8-acc6-e64e922bcf78 | -2.572 | -56.1646 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| d5c83c08-a339-37c4-9fa4-0dd0e8d84668 | -4.4507 | -47.9112 | 2026-10-08 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 2ffc78a7-45c9-3063-abda-efbdc8389564 | -6.0935 | -49.411 | 2026-10-08 01:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7f583eaf-d0d3-3ed0-81cb-1d21a735f6f2 | -4.3471 | -43.8021 | 2026-10-08 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 61ec140a-2091-3038-911a-67441eaaa038 | -8.7417 | -45.1791 | 2026-10-08 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 262957cf-e02d-39fc-b803-d9a8ea39f4c2 | -3.1285 | -54.1657 | 2026-10-08 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b4199aef-0ae4-3988-a858-1f7d7c19376b | -3.5865 | -54.5742 | 2026-10-08 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c92f6190-8663-3d1c-9cbc-89163651edc3 | -3.1114 | -53.8041 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| b53a8b4d-42b2-357e-8a0d-caac9e2ef661 | -3.0917 | -54.1867 | 2026-10-08 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 72715f44-b11c-36ea-97ec-fb2d659ee909 | -6.2158 | -52.849 | 2026-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3c90d70a-fa76-36d1-92a6-9c984c147b1d | -9.0592 | -65.9209 | 2026-10-08 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| fe120b29-13c6-3eb4-8d66-801133776cd0 | -3.1114 | -53.7839 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 6e010ed1-cfa8-3e73-999a-dca47d43b9c4 | -3.11 | -54.1862 | 2026-10-08 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| ca43a91e-4312-3863-9334-f3b8d10d666a | -5.7498 | -41.7534 | 2026-10-08 01:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 66589a85-844e-3e72-b656-a4176d8f127d | -2.7152 | -57.472 | 2026-10-08 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0497941c-6ca9-3e81-9a5b-2b95316b4fe4 | -6.2157 | -52.8695 | 2026-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 39163c77-c8b2-3a6b-b1a4-08f68f9a75e8 | -8.7039 | -45.1832 | 2026-10-08 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 2d6740f2-e50e-38d4-8af3-b8325ff71dd8 | -5.7119 | -53.4658 | 2026-10-08 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f1fc0403-66da-3841-af01-bbe0f0784f93 | -2.7796 | -54.0937 | 2026-10-08 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 259190b6-9436-3839-862a-0e006091c8b9 | -6.8764 | -43.685 | 2026-10-08 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 780fad82-1d23-3b4e-a804-c05645311635 | -8.7225 | -45.204 | 2026-10-08 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 71ec20b7-2de7-3551-8595-54e88a510c9a | -4.1176 | -59.8888 | 2026-10-08 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a43f6a5b-34f4-3f87-a309-fdbf4e66be80 | -2.7613 | -54.0941 | 2026-10-08 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 559644c9-ee83-36ad-a9b9-587089c69a62 | -3.0558 | -53.9263 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 89444c75-a78f-3d27-80e5-fffd0d1477f1 | -6.895 | -43.7066 | 2026-10-08 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 78d2ce7f-b2ea-369b-ada8-9397fc671fb9 | -3.1697 | -58.6437 | 2026-10-08 01:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 2943e216-0058-3e11-8e75-c09c63b9aec1 | -2.9448 | -54.1501 | 2026-10-08 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e2dc5c39-ea55-3722-99b7-80fd83db42c7 | -3.019 | -53.9272 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 081e6378-8003-38c2-8bb6-2411a6a68530 | -6.15 | -39.4409 | 2026-10-08 01:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 116.4 |
| 8c491600-7d84-3222-bbe5-5dab14531a8a | -8.7231 | -45.1583 | 2026-10-08 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 974a0397-df25-32d8-9d1a-ed2d2e465d11 | -3.8383 | -55.9774 | 2026-10-08 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| fef7402a-5f19-3c67-89cd-bf6e067201b7 | -10.4337 | -47.2824 | 2026-10-08 01:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f4d9ee29-0cd5-371c-aa10-f5185a1866ba | 1.6938 | -55.6066 | 2026-10-08 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 4d24578d-a766-3b28-81d0-3fc02c2a1777 | -9.4749 | -64.3713 | 2026-10-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d8c7b08d-44c8-32b8-9b10-61ac173a396b | -8.742 | -45.1563 | 2026-10-08 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 3fb8b7b2-f7f1-3da6-97c6-fca99c6fe9d4 | -8.6107 | -67.0301 | 2026-10-08 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b5256214-9877-350a-9895-9021262a97a5 | -3.2554 | -54.6631 | 2026-10-08 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| c29da9dd-1f0d-336c-8daa-8fc429de4535 | -9.0591 | -65.9396 | 2026-10-08 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 7c80d126-a970-3e70-9b10-0e2e392ee311 | -6.1689 | -39.4391 | 2026-10-08 01:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 89.6 |
| e0d8e0e2-7c49-3f39-ac79-97ef831097ba | -3.2157 | -50.5586 | 2026-10-08 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| ab3d9bcf-17bb-39d6-a76e-cab1c19fe6f8 | -4.0628 | -59.8328 | 2026-10-08 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a17d7418-db1f-39e8-8c61-4bc43b54dc98 | -3.6049 | -54.5736 | 2026-10-08 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| bcfc9414-19a3-3f82-bfd5-060b8fcff492 | -6.2342 | -52.8685 | 2026-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| fc43ccf5-4e47-3ded-9b20-5b016d2738e2 | -9.4935 | -64.3706 | 2026-10-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6408d578-674e-31db-b265-d196f85b09ae | -3.1101 | -54.1661 | 2026-10-08 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 533abcb9-4455-3220-ae2d-0fc3515f1545 | -9.4936 | -64.3518 | 2026-10-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 6b42e33f-7c25-3280-8c1f-70fd76a9318a | -3.0914 | -54.2669 | 2026-10-08 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6a8c30dd-06aa-3983-845b-c014625865dc | -6.6317 | -43.73 | 2026-10-08 01:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 99fa0cff-5ed9-34c1-a3e1-9f83df496cf3 | -5.6934 | -53.4667 | 2026-10-08 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ad563f52-bfea-31e2-b6ea-aaca2d2c95d8 | -5.6931 | -53.5073 | 2026-10-08 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 81af5156-e906-3301-84f3-b19a6587405f | -2.798 | -54.0933 | 2026-10-08 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| e22a70e1-7e55-3591-819d-cc7d63c12b7f | -2.4988 | -56.1266 | 2026-10-08 01:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d2a85a0f-8f99-30dd-8d77-1a8dab69c0b3 | -9.475 | -64.3525 | 2026-10-08 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 7dd296bd-f0e7-326c-b79b-466495134b2b | -3.073 | -54.2874 | 2026-10-08 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| db91023d-5d75-35a2-a9e8-04fc34f51866 | -3.0374 | -53.9268 | 2026-10-08 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9c2dd9ac-53e3-3ab8-bed1-551c1c0bf06d | -6.2527 | -52.8675 | 2026-10-08 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b9fe63d4-7a08-394d-8b4c-54d0cf50a454 | -3.478 | -59.5779 | 2026-10-08 01:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| ee8f1c84-61f9-36f9-b9ca-7840ba7d261a | -6.8952 | -43.6833 | 2026-10-08 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 6ac623e5-6d29-3528-ad1d-7d182e5e4eb8 | -5.9587 | -55.3448 | 2026-10-08 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4f523957-bec0-3741-a095-3851e34136f8 | -3.2313 | -46.9596 | 2026-10-08 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2ee7174a-81ce-38de-b97e-7af36cac007d | -3.1097 | -54.2865 | 2026-10-08 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b59513e6-dcae-3a47-98a5-5c29cea449a4 | -12.232 | -44.7194 | 2026-10-08 01:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 7229b506-ed49-3369-a315-9a135963972f | -3.1278 | -54.3662 | 2026-10-08 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 3d03dc6a-a8ba-3dda-ac93-cde1eaf83685 | -9.4935 | -64.3706 | 2026-10-08 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 4613044b-9f17-30b6-bd69-40604066c924 | -3.0373 | -53.9469 | 2026-10-08 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8a73ed71-d016-32bd-9182-dd6def11e8c1 | -6.2342 | -52.8685 | 2026-10-08 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 326f9d27-bd75-30dc-b57f-3a8cd4f48045 | -5.7116 | -53.5065 | 2026-10-08 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 187.8 |
| 3d8cd7d4-fa28-3df4-b7d2-68ef0ced6cd5 | -4.4506 | -47.9329 | 2026-10-08 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |


[Clique aqui para ver as próximas entradas](README44.md)
