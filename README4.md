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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e1f09dd-0be9-3c9e-b9f5-06005a42ea81 | -18.50809 | -49.01664 | 2025-08-31 00:28:00 | TERRA_M-M | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 5bf36030-4aab-30e9-9fcf-f535ec56ef73 | -17.96246 | -42.98615 | 2025-08-31 00:28:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 1a42b5f3-2560-35dc-acf3-4d7bce9a19a5 | -11.88332 | -46.73026 | 2025-08-31 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f254024d-93a3-3e67-8b75-910d3f2aba6d | -11.82325 | -46.44263 | 2025-08-31 00:28:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 39011812-269c-3d00-af3e-bdf1da7fe3ac | -15.67404 | -43.23334 | 2025-08-31 00:28:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 737c6497-f1f0-367d-8fc3-acfe168f4fe7 | -13.39953 | -46.84167 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b1338166-db23-37a0-955d-971d2745d289 | -11.89214 | -46.72895 | 2025-08-31 00:28:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 112e3ac2-c8aa-3efe-95ad-9807fb4a62e5 | -14.82369 | -46.74791 | 2025-08-31 00:28:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d5243bd5-96d6-35e0-a429-5437c1f69c68 | -13.31381 | -46.88783 | 2025-08-31 00:28:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f0030990-8e60-3f65-8941-7644dd0f7cbd | -18.1566 | -50.24945 | 2025-08-31 00:28:00 | TERRA_M-M | CASTELÂNDIA | GOIÁS | Brasil | 5205059 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d2e8ca58-cbec-3586-8027-629166b83f88 | -12.0976 | -44.717 | 2025-08-31 00:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 97424034-94e3-3f88-ac5b-bffb50c7d788 | -8.8939 | -45.094 | 2025-08-31 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 09a6b52e-bf41-3af0-bcaf-a1f6eaccdcef | -14.5448 | -51.9943 | 2025-08-31 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 85c850a2-b843-347a-91e9-ae9ad1773e8c | -9.2745 | -67.6433 | 2025-08-31 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 3eb87be0-f782-33cc-a6a2-ef0db2344e6c | -6.1665 | -43.3273 | 2025-08-31 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c9912748-1f5a-35a3-b3bf-b2a036b80707 | -13.3636 | -46.95 | 2025-08-31 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| adf932ec-6eb2-3b18-8a1d-4aa14228eac7 | -12.9192 | -56.9873 | 2025-08-31 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| cfc2f452-af67-3aa4-8161-ca7892137660 | -8.8337 | -66.7275 | 2025-08-31 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 90d40efb-4af9-3d33-8ae3-f777bc13c410 | -7.9265 | -63.0158 | 2025-08-31 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 4a3a849b-ada9-3866-86f9-1ca29c89b966 | -7.0951 | -44.3128 | 2025-08-31 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| f2beee9c-eb34-322c-b078-ae895d9b1f1e | -10.9326 | -50.8316 | 2025-08-31 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1f617765-a3fa-3887-8dac-90de57526e30 | -11.3504 | -43.637 | 2025-08-31 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| c4fd844e-5796-3d7c-875d-4798c1283dfb | -3.5995 | -47.5142 | 2025-08-31 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 766c6ea3-8e71-3218-89be-a2ab1dde10a7 | -11.3112 | -43.69 | 2025-08-31 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 842f4e26-2085-39d7-8a34-ddc75f9c41a3 | -7.0948 | -44.3358 | 2025-08-31 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4441ab1f-017e-30fd-b7be-705063798f40 | -13.3443 | -46.953 | 2025-08-31 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 7ac6c4b4-e5ad-3e20-8b38-380774abfee2 | -7.1139 | -44.3111 | 2025-08-31 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 1a6755ac-3cfa-33c1-a458-7b97f3abab0a | -16.2417 | -52.675 | 2025-08-31 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7d1dc0b6-71f5-3617-8324-065365625c9d | -12.9194 | -56.9672 | 2025-08-31 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1f98b83a-ade7-3e43-9ffb-33702f1f23b7 | -11.8373 | -46.4287 | 2025-08-31 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 19ef5080-f803-316c-8bef-bbcb09babe0f | -16.2217 | -52.6992 | 2025-08-31 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| b2071a41-49c4-3be0-b849-fd46dfcf0f7f | -10.1986 | -55.4457 | 2025-08-31 00:30:00 | GOES-19 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 811408c0-84cd-37ef-8de3-983df5dff335 | -16.2225 | -52.6565 | 2025-08-31 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d881ed9c-8aca-38a8-8be1-058c5b01ff0d | -11.3116 | -43.6664 | 2025-08-31 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 997e82f5-a555-3992-acd4-e9f8e263c85d | -6.1853 | -43.3257 | 2025-08-31 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| b41d765a-6576-3c37-a572-efed179907f2 | -10.3313 | -59.2011 | 2025-08-31 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 44347cd5-f2bb-3f72-b483-26c1fc739067 | -7.0774 | -63.1948 | 2025-08-31 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 15fef42d-4428-3468-9e53-a9f79e9b5cee | -8.6673 | -62.8369 | 2025-08-31 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2bff63d7-e245-3586-89df-62e23e11d221 | -9.0799 | -65.4536 | 2025-08-31 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3c0abb18-ddb1-3cdf-9f2d-a802a36dfe43 | -10.3126 | -59.2023 | 2025-08-31 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 43bbe41f-0636-36ac-b96c-f8424fc95c3e | -13.4986 | -46.9517 | 2025-08-31 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 0f31b91b-ebef-3177-b76a-9103ca2f493e | -9.0613 | -65.4542 | 2025-08-31 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 20853c80-c482-3bba-ba58-5250eba3e882 | -7.908 | -63.0164 | 2025-08-31 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8ea2c6b3-8e5d-3068-9e79-0e9aba9f24b5 | -11.3304 | -43.6871 | 2025-08-31 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 45d155c4-4992-3200-a590-4afab345c8a5 | -9.7498 | -65.0938 | 2025-08-31 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8b8a8bfd-0aed-34ea-bbe7-3c44c7f5e327 | -8.875 | -45.0961 | 2025-08-31 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c10c7c2f-7c03-371d-8cf2-f89e4bd0c9d5 | -11.3701 | -43.6104 | 2025-08-31 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| c25c6ee9-837e-3d4f-877e-889fb5eb6cbb | -9.0614 | -65.4355 | 2025-08-31 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 69afbe64-2b70-39c5-b9ce-6ab843aa1d13 | -3.8146 | -48.9515 | 2025-08-31 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6f6a21d1-7bfc-3d25-9a53-e33fe1119e56 | -9.0615 | -65.4169 | 2025-08-31 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7b334a2b-f564-3460-82ea-1ea9dddb5bd3 | -16.2221 | -52.6778 | 2025-08-31 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| a175be0d-6673-3325-ba5f-7edcfb9c04c9 | -10.1172 | -58.0196 | 2025-08-31 00:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9c786c5f-75cd-37f7-884f-7009168e55ac | -10.1359 | -58.0183 | 2025-08-31 00:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 12e96772-db59-393d-b0fe-fdf0ad0b150e | -11.3509 | -43.6133 | 2025-08-31 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 8243ea5b-0208-32e6-b84e-fcdaf390466a | -8.6487 | -62.8376 | 2025-08-31 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 68bed29b-f0bc-3cbc-8edb-8b96f42e2fdf | -8.8522 | -66.727 | 2025-08-31 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2de116b1-9b7a-343d-9e94-96765520e447 | -19.0926 | -48.3106 | 2025-08-31 00:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 6df27ed6-586d-3352-974a-6da7c27323fc | -18.6051 | -50.192 | 2025-08-31 00:30:00 | GOES-19 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| 2ae6b7fc-b6e8-3705-a359-16fde5ac3071 | -16.2025 | -52.6807 | 2025-08-31 00:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 86c4214b-5a38-315f-a535-1f8580ecb63e | -14.5452 | -51.9729 | 2025-08-31 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 71416236-0dc5-3e21-bf55-f4dd45c29c2f | -9.0799 | -65.4349 | 2025-08-31 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 46226137-81f8-3adf-82eb-ef57c706d3f8 | -10.9515 | -50.8296 | 2025-08-31 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| da0daf1f-ae27-329c-99f0-a55926bb49e2 | -7.1136 | -44.3341 | 2025-08-31 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ac40a806-d956-3393-ae64-2ea61c838dec | -8.88458 | -45.10796 | 2025-08-31 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 82af30e5-f8ca-36a6-b13e-60e3daf438de | -8.29394 | -44.92268 | 2025-08-31 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8f6d6ff8-9289-3c79-b172-155f2b40f598 | -11.7821 | -47.39873 | 2025-08-31 00:30:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7c48cf62-91ea-3827-8632-5e50d4e14276 | -9.69404 | -48.29596 | 2025-08-31 00:30:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dc7a0cd9-eb66-3d8a-8b47-071a209b48e2 | -8.89099 | -45.08585 | 2025-08-31 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| cc359bf9-a91a-3dfe-bd91-83b7ca58d2b6 | -11.00517 | -46.84684 | 2025-08-31 00:30:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 758931c2-6b2a-3cb2-845e-2614f591debf | -8.33677 | -46.29055 | 2025-08-31 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a02f5bec-82f7-38bd-b2de-ccf4c3db1c97 | -11.30105 | -43.65733 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ed7818a1-817f-3286-b7f2-97cc4504c73f | -10.03154 | -46.01898 | 2025-08-31 00:30:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| da560fad-c00f-3403-ba7c-a6916ae0f6e1 | -10.93089 | -46.84538 | 2025-08-31 00:30:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 682a8e40-d43e-348d-936e-057096b6cf77 | -8.29374 | -46.31226 | 2025-08-31 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f6a9cb55-6aa6-33fd-849d-4a0a163b206a | -10.95185 | -50.83866 | 2025-08-31 00:30:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 7d9386d6-583b-3241-bae5-4ed3876f0e38 | -10.02734 | -48.3806 | 2025-08-31 00:30:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b2bf9ff0-5741-3c62-b7ef-8d2ed5e31b52 | -10.4754 | -51.63339 | 2025-08-31 00:30:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| be792428-123f-31b1-a377-7723d77fb8f8 | -7.38158 | -43.40092 | 2025-08-31 00:30:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8cb8d0df-de76-3c4f-a875-a3caed2d8317 | -11.31621 | -43.69052 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 8c2e8f03-f516-3c19-a635-3a7e9c3dcd65 | -9.20044 | -54.58089 | 2025-08-31 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7c52fefc-ced7-3194-b322-034dc48c9dde | -8.97153 | -46.73867 | 2025-08-31 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dd79da47-bcd6-35bc-bc9c-6c9c3d0b7592 | -9.68494 | -48.30307 | 2025-08-31 00:30:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 21abace1-1edf-38ef-b480-94bc5f20b095 | -11.84402 | -51.49651 | 2025-08-31 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 18fdf104-e7e5-3cea-a790-888914bc0e79 | -8.5551 | -51.30463 | 2025-08-31 00:30:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 3ec5fd66-7fc4-32aa-8074-d44e59b1765d | -11.29929 | -43.64554 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| c63d8966-44b1-3c1c-bdfa-b9bb10300bdd | -11.3145 | -43.67895 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 4a95db88-49ae-3aeb-abe9-a56b5218a24f | -12.18698 | -50.11882 | 2025-08-31 00:30:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d32d229-c22d-338d-8e2f-e6fb23cb8bef | -8.30356 | -44.92125 | 2025-08-31 00:30:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 34801192-e46e-32e7-bf0b-0d08346e16ac | -7.58894 | -42.71785 | 2025-08-31 00:30:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 51b6c443-ad6e-3646-ab6b-f0d496b69666 | -8.85695 | -45.73304 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d03cc8f3-a878-301f-8d59-1a35b3aa5b49 | -10.41433 | -50.85629 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 702b0115-43ec-3af5-8496-4b5388762ba9 | -7.95461 | -46.39022 | 2025-08-31 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f7fb460f-eb01-3c26-b395-5032f3980c24 | -6.96651 | -40.94218 | 2025-08-31 00:30:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 86ba80b3-0cdc-3bfa-8485-a833ad50217b | -9.68707 | -47.04816 | 2025-08-31 00:30:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 75c7a8f3-b4f1-35fd-8cfe-9fac26488a84 | -10.48812 | -51.62578 | 2025-08-31 00:30:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d3e4c4dc-c900-3d08-9406-21bc8c8ce3d6 | -8.84915 | -45.74399 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2ca53ce4-c196-3fb0-8542-471f76a5bef2 | -10.0337 | -48.08427 | 2025-08-31 00:30:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 79b465b5-7cdf-39c9-965d-eccb8114f39f | -10.60294 | -44.32372 | 2025-08-31 00:30:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 13332ca6-e46c-3b1e-bf3d-ebea00038cae | -6.97104 | -40.94677 | 2025-08-31 00:30:00 | TERRA_M-M | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 43.3 |
| 84eda710-28c4-3af5-9b68-f9e32a85c424 | -11.32275 | -43.66576 | 2025-08-31 00:30:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |


[Clique aqui para ver as próximas entradas](README5.md)
