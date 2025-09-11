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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cf03868-cf6b-3edb-925d-28ca9bd7e55b | -8.03642 | -49.05285 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1f053d5-fb5d-3fa6-b39a-473c2ffd9add | -9.08908 | -47.08554 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8db30f31-7ae8-3a41-b475-b79f4deaccf1 | -6.80653 | -52.80473 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 132cc86b-88d6-3ca2-8aaa-d8d0eb864bf3 | -5.22462 | -45.43032 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c47a198-bd72-364a-a38d-1fdd917882ae | -8.80633 | -48.09884 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9c5c35f-21a2-39b0-843d-0ebd063f6788 | -4.89389 | -55.90975 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54996394-2677-38b8-9587-d7789af0bd85 | -5.84971 | -45.12737 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b466baf-7273-33ec-86d1-e7cf44ff4685 | -7.73595 | -50.74487 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc18919c-5aa8-34db-8ae8-8a50adcb5b7d | -5.76887 | -42.44309 | 2025-09-11 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d7f89e4b-3a38-31c9-bd57-a25cb93247e5 | -9.05415 | -46.96738 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a69b668-c296-34f8-afa9-f90cd97aae9c | -5.5496 | -43.04552 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ab19762-af41-3bf6-bc4c-466d5d062369 | -6.81457 | -44.88713 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1fdc6dd-aac9-3e63-99d8-e300f05aff3f | -6.95897 | -44.8183 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d952322b-9544-3f02-96ee-8660d6c7898d | -8.02223 | -48.65003 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a5e5773-f4d4-3c4c-8185-b1a8310c3651 | -5.5492 | -45.08587 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68ae4cd4-3b9d-3019-ba79-93fa4ed71935 | -7.33149 | -49.60738 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12181fb5-6000-3afb-9748-574eddd91c96 | -7.58772 | -47.75928 | 2025-09-11 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9237289e-25dd-3090-8f77-2fc3645f6e66 | -7.90996 | -46.85184 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab36945d-1b6b-3325-9275-be06eee19821 | -5.59104 | -51.938 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c864f8ce-0448-3a8a-8420-62700a8149ae | -7.78567 | -50.77433 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 24f9ebbf-7be2-33cb-9dbb-d4f771901ff3 | -9.06965 | -47.0808 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b0b6511-9152-3364-8313-5648e0cfaab3 | -4.45834 | -55.04806 | 2025-09-11 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bfd4525-c83c-3aec-bb35-23a53e7d8fec | -8.02576 | -48.65059 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9070807c-d889-3b9f-904d-31a96e293a3d | -7.75592 | -50.76937 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff3550d7-40e1-3bad-8b32-ceeaf6e54d26 | -8.48276 | -47.28608 | 2025-09-11 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b7bb8cd-1a5e-30da-9359-dd78e2e31d68 | -6.38099 | -47.25695 | 2025-09-11 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c598807-1686-37ac-ae19-2105f5935f14 | -5.3948 | -43.43174 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f68b28fd-6b5e-3290-9e33-c5d82ddbf7f6 | -6.53949 | -42.44334 | 2025-09-11 04:44:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 32478fb1-61e3-3eff-96f7-96ba70e5be08 | -7.86698 | -47.86331 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f38a3f9d-0598-3b99-ac90-f9f3db9cd2f9 | -7.55796 | -48.20575 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deda01fe-fa11-353f-8b86-086f18fdfabc | -7.44889 | -44.97015 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b51b2841-2ec2-3ba4-b993-4176732d5edf | -6.18198 | -53.26573 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ed47abd-1823-3734-9144-10aa976c7f40 | -7.731 | -50.75474 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1c010df-b284-3b37-a1ff-e52067dd54b8 | -9.06644 | -47.07549 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43724bbd-5279-368e-b94a-f912839c7945 | -6.55332 | -43.98238 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| faa28062-cf8f-3eb5-a4c3-89d88bd031dc | -6.27639 | -43.38919 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6cf2670-3292-318d-b4e4-39de8c116738 | -6.3072 | -45.66025 | 2025-09-11 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97e240f5-1aa3-3c70-8da2-a9910e7b56ac | -7.87194 | -46.72898 | 2025-09-11 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b27c162e-37fa-3c0b-9bd1-1bb53ef4e9a2 | -6.40163 | -43.50208 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d7ade2a-e8e9-3c49-b787-31ed8f272c60 | -6.35114 | -43.41276 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6588789d-76e4-386e-91b3-a46abcc3257e | -6.3996 | -42.60595 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c86cdcc0-de32-35c6-bbc6-243595f0bbb1 | -5.35915 | -43.41095 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13dffd93-f43d-3d53-8aca-37abafb1b67a | -8.08758 | -52.34329 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a2d347d-d5bd-3faf-b903-0889c2d5ba49 | -7.50344 | -48.26181 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fdfc49b-607a-37c9-8ab7-47ead6bca0ec | -5.73847 | -45.60019 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15055157-03b5-3576-beee-6fa0f76f6071 | -8.52523 | -45.69116 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d734c69-50f6-3272-ba83-5af8aa8963c6 | -8.07884 | -50.1805 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b623bce-d44b-31fb-bb5a-1467fac7f3c9 | -7.46567 | -45.28991 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a891ee42-64d9-3032-b46c-8142c6c8381c | -5.22283 | -45.43249 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72d3cc51-d54a-318e-9b54-87d6c19c332e | -7.39187 | -47.37046 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e082f45-f59f-3f41-a68f-7314dd95afbe | -6.31769 | -43.44081 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5832596e-a87a-3176-8100-e25c9d370aaa | -3.52952 | -59.60953 | 2025-09-11 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77787f6c-8cea-3988-92cc-f4afb8f1f891 | -5.33996 | -44.80316 | 2025-09-11 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d346305-5165-3eaa-8aac-781545de0b63 | -8.66121 | -45.73307 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20458104-dba5-373e-82f7-b36041db5230 | -8.16576 | -46.06863 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7dc360be-7bf8-3835-a453-b04ac1debf67 | -8.16724 | -46.08792 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64d08b4d-fcaa-3f29-8d9e-16b33ff37088 | -5.42757 | -45.87656 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa22731b-03b7-3936-8835-469c76cc9faf | -7.91927 | -44.84611 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a87037b0-e931-3e8d-9828-9181ac2afa73 | -6.56255 | -44.2118 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 89cec792-def7-359f-b491-c5fcd48673e3 | -6.72882 | -43.02592 | 2025-09-11 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 93a122b8-62ba-3cb0-859d-16ed1d976dd0 | -9.11418 | -46.96946 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 227c8f33-1c44-3d31-b685-3418879bd936 | -8.51675 | -45.68988 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75310a09-f98e-36d2-bfaa-7a1dbda9b3fc | -9.07072 | -47.04631 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4f0760a-2f95-3624-a09e-85b5ff5fe80f | -7.09938 | -50.7552 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1ff3d68-4c6c-3d7c-9a16-5674081751bd | -7.76255 | -50.77043 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3c40aa8a-9be1-3da3-a642-365a75187037 | -6.53989 | -42.44039 | 2025-09-11 04:44:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b7b31210-42db-32d4-bea0-656f98c15b94 | -7.41327 | -45.85484 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 490eb526-785f-3dac-8eef-c50c3642f636 | -7.26291 | -44.6126 | 2025-09-11 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63fc74a3-96e8-33f4-8045-4ec45d39104c | -3.86365 | -52.39256 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4f70c7b-cdfe-397b-a0ca-9f6c65bf0cc6 | -9.06574 | -47.08026 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c61f53c5-cd55-3499-9558-297e529618f4 | -6.41777 | -44.49746 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf4ba80c-ae2c-3d8c-ac12-bd1caddce465 | -8.97158 | -46.06877 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 966d3fc3-58f3-34fd-893a-907a2bcc8260 | -8.0441 | -48.67305 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b6d5d139-4fb2-3866-b731-2449ade102b7 | -7.73649 | -50.74141 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a81eca9e-60f5-37de-bb62-b9d4682e7696 | -8.19502 | -50.11039 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bdb46b0-13ad-362d-a763-3cae025f7077 | -4.86975 | -42.77077 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 60ee7736-0d8a-3f03-9ef8-701a02bb7cae | -9.15087 | -46.05459 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58e71542-8972-32b6-938b-d8dc658c5d55 | -7.38709 | -47.3511 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adab4238-da45-3a6e-87cd-d266225ac89e | -8.10391 | -49.25077 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 080c1b08-3f2c-3ec4-9d64-a8c4d56598b7 | -7.71516 | -44.7991 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d301da0-e0ac-3c6e-ad05-65e6b38b2392 | -8.07775 | -50.18755 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff75890c-e428-3d4e-a640-fc62d1320f78 | -6.20228 | -45.61132 | 2025-09-11 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30661ff7-e0a7-3d25-9747-984d8a5eabe8 | -6.42223 | -44.49814 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 523cad49-7d5a-3ccc-9ee7-54e7ebe717b9 | -3.6485 | -48.32971 | 2025-09-11 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea9e11cd-d9ab-31be-b1da-6ff938573da7 | -6.55863 | -43.97834 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a916d607-882d-374d-8b5f-cf2908055daa | -6.25323 | -43.41333 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 294ebfb3-9ef0-3ca3-b0c2-b6d94344d07a | -6.6559 | -51.99172 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9751d6b0-4cdc-36d1-abd6-2cbd706567ea | -9.0853 | -47.083 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f48c4472-f398-38c7-ad97-726940673e9d | -6.8589 | -47.8587 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4496f4fb-4049-30e9-9027-9d89ea837d52 | -7.20405 | -44.95572 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52b76ba1-794d-33ac-9379-6620dd4db1b6 | -6.99542 | -44.78381 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a5f8bef-d84b-3612-86f4-28c3a84da533 | -7.88717 | -46.04771 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47d5227a-8e52-3b00-80d9-5a44652e708b | -6.10112 | -45.93041 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2444bdc0-f0cb-3a1b-a97e-b66b3dd29b5b | -8.07973 | -52.37086 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d91a6e9-ed2d-3080-b858-72797d325dc6 | -6.89493 | -50.43423 | 2025-09-11 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f26fdd3c-3848-3167-bfee-4e3bd2e2e0d5 | -5.38985 | -45.93787 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5537604e-cfdb-37b6-a0e3-3d1b4c3001b2 | -8.42265 | -49.08487 | 2025-09-11 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a49cd826-4bde-3c65-afad-2c2a9acd1961 | -7.50563 | -48.26123 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f468d667-1c84-3aa7-adf9-fc1f2fdd192f | -2.55665 | -47.71647 | 2025-09-11 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67a1a8c6-d8c8-3871-bd51-cb891afa135a | -3.32067 | -48.72824 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README90.md)
